""" Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR asr9k\-sc\-invmgr package
admin\-plane operational data.

This module contains definitions
for the following management objects\:
  inventory\: Inventory operational data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class CardResetReasonEnum(Enum):
    """
    CardResetReasonEnum

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

    reset_unknown = 1

    power_up = 2

    parity_error = 3

    clear_config_reset = 4

    manual_reset = 5

    watch_dog_timeout_reset = 6

    resource_overflow_reset = 7

    missing_task_reset = 8

    low_voltage_reset = 9

    controller_reset = 10

    system_reset = 11

    switchover_reset = 12

    upgrade_reset = 13

    downgrade_reset = 14

    cache_error_reset = 15

    device_driver_reset = 16

    software_exception_reset = 17

    restore_config_reset = 18

    abort_rev_reset = 19

    burn_boot_reset = 20

    standby_cd_healthier_reset = 21

    non_native_config_clear_reset = 22

    memory_protection_error_reset = 23

    card_reset_reason_max = 24


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper as meta
        return meta._meta_table['CardResetReasonEnum']



class Inventory(object):
    """
    Inventory operational data
    
    .. attribute:: racks
    
    	Table of racks
    	**type**\:   :py:class:`Racks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.Inventory.Racks>`
    
    

    """

    _prefix = 'asr9k-sc-invmgr-admin-oper'
    _revision = '2017-01-04'

    def __init__(self):
        self.racks = Inventory.Racks()
        self.racks.parent = self


    class Racks(object):
        """
        Table of racks
        
        .. attribute:: rack
        
        	Rack number
        	**type**\: list of    :py:class:`Rack <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.Inventory.Racks.Rack>`
        
        

        """

        _prefix = 'asr9k-sc-invmgr-admin-oper'
        _revision = '2017-01-04'

        def __init__(self):
            self.parent = None
            self.rack = YList()
            self.rack.parent = self
            self.rack.name = 'rack'


        class Rack(object):
            """
            Rack number
            
            .. attribute:: number  <key>
            
            	Rack number
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: basic_attributes
            
            	Attributes
            	**type**\:   :py:class:`BasicAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.Inventory.Racks.Rack.BasicAttributes>`
            
            .. attribute:: fan_traies
            
            	Table for rack fan trays
            	**type**\:   :py:class:`FanTraies <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.Inventory.Racks.Rack.FanTraies>`
            
            .. attribute:: power_supply_shelfs
            
            	Table for rack power supply shelves 
            	**type**\:   :py:class:`PowerSupplyShelfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.Inventory.Racks.Rack.PowerSupplyShelfs>`
            
            .. attribute:: power_supply_zones
            
            	Table for defining rack power supply zones 
            	**type**\:   :py:class:`PowerSupplyZones <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.Inventory.Racks.Rack.PowerSupplyZones>`
            
            .. attribute:: slots
            
            	Slot table contains all slots in the rack
            	**type**\:   :py:class:`Slots <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.Inventory.Racks.Rack.Slots>`
            
            

            """

            _prefix = 'asr9k-sc-invmgr-admin-oper'
            _revision = '2017-01-04'

            def __init__(self):
                self.parent = None
                self.number = None
                self.basic_attributes = Inventory.Racks.Rack.BasicAttributes()
                self.basic_attributes.parent = self
                self.fan_traies = Inventory.Racks.Rack.FanTraies()
                self.fan_traies.parent = self
                self.power_supply_shelfs = Inventory.Racks.Rack.PowerSupplyShelfs()
                self.power_supply_shelfs.parent = self
                self.power_supply_zones = Inventory.Racks.Rack.PowerSupplyZones()
                self.power_supply_zones.parent = self
                self.slots = Inventory.Racks.Rack.Slots()
                self.slots.parent = self


            class PowerSupplyShelfs(object):
                """
                Table for rack power supply shelves 
                
                .. attribute:: power_supply_shelf
                
                	Power Supply Shelf number
                	**type**\: list of    :py:class:`PowerSupplyShelf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.Inventory.Racks.Rack.PowerSupplyShelfs.PowerSupplyShelf>`
                
                

                """

                _prefix = 'asr9k-sc-invmgr-admin-oper'
                _revision = '2017-01-04'

                def __init__(self):
                    self.parent = None
                    self.power_supply_shelf = YList()
                    self.power_supply_shelf.parent = self
                    self.power_supply_shelf.name = 'power_supply_shelf'


                class PowerSupplyShelf(object):
                    """
                    Power Supply Shelf number
                    
                    .. attribute:: number  <key>
                    
                    	Power Shelf number
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: basic_attributes
                    
                    	Attributes
                    	**type**\:   :py:class:`BasicAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.Inventory.Racks.Rack.PowerSupplyShelfs.PowerSupplyShelf.BasicAttributes>`
                    
                    

                    """

                    _prefix = 'asr9k-sc-invmgr-admin-oper'
                    _revision = '2017-01-04'

                    def __init__(self):
                        self.parent = None
                        self.number = None
                        self.basic_attributes = Inventory.Racks.Rack.PowerSupplyShelfs.PowerSupplyShelf.BasicAttributes()
                        self.basic_attributes.parent = self


                    class BasicAttributes(object):
                        """
                        Attributes
                        
                        .. attribute:: basic_info
                        
                        	Inventory information
                        	**type**\:   :py:class:`BasicInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.Inventory.Racks.Rack.PowerSupplyShelfs.PowerSupplyShelf.BasicAttributes.BasicInfo>`
                        
                        

                        """

                        _prefix = 'asr9k-sc-invmgr-admin-oper'
                        _revision = '2017-01-04'

                        def __init__(self):
                            self.parent = None
                            self.basic_info = Inventory.Racks.Rack.PowerSupplyShelfs.PowerSupplyShelf.BasicAttributes.BasicInfo()
                            self.basic_info.parent = self


                        class BasicInfo(object):
                            """
                            Inventory information
                            
                            .. attribute:: alias
                            
                            	useful for storing an entity alias 
                            	**type**\:  str
                            
                            	**length:** 0..255
                            
                            .. attribute:: asset_id_str
                            
                            	asset Identification string
                            	**type**\:  str
                            
                            	**length:** 0..255
                            
                            .. attribute:: asset_identification
                            
                            	asset Identification
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: ceport
                            
                            	1 if ce port found, 0 if not
                            	**type**\:  bool
                            
                            .. attribute:: chip_hardware_revision
                            
                            	chip module hw revision string
                            	**type**\:  str
                            
                            	**length:** 0..255
                            
                            .. attribute:: composite_class_code
                            
                            	Major&minor class of the entity
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: description
                            
                            	describes in user\-readable terms       what the entity in question does
                            	**type**\:  str
                            
                            	**length:** 0..255
                            
                            .. attribute:: environmental_monitor_path
                            
                            	sysdb name of sensor in the envmon EDM
                            	**type**\:  str
                            
                            	**length:** 0..255
                            
                            .. attribute:: firmware_revision
                            
                            	firmware revision string
                            	**type**\:  str
                            
                            	**length:** 0..255
                            
                            .. attribute:: group_flag
                            
                            	indicates if this entity is group       or not
                            	**type**\:  bool
                            
                            .. attribute:: hardware_revision
                            
                            	hw revision string
                            	**type**\:  str
                            
                            	**length:** 0..255
                            
                            .. attribute:: is_field_replaceable_unit
                            
                            	1 if Field Replaceable Unit 0, if not
                            	**type**\:  bool
                            
                            .. attribute:: manufacturer_asset_tags
                            
                            	Manufacture Asset Tags
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: manufacturer_name
                            
                            	manufacturer's name
                            	**type**\:  str
                            
                            	**length:** 0..255
                            
                            .. attribute:: memory_size
                            
                            	Size of memory associated with       the entity where applicable
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: model_name
                            
                            	model name
                            	**type**\:  str
                            
                            	**length:** 0..255
                            
                            .. attribute:: name
                            
                            	name string for the entity
                            	**type**\:  str
                            
                            	**length:** 0..255
                            
                            .. attribute:: new_deviation_number
                            
                            	integer value for New Deviation Number 0x88
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: physical_layer_interface_module_type
                            
                            	integer value for plim type if     applicable to this entity
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: redundancystate
                            
                            	integer value for Redundancy State if     applicable to this entity
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: serial_number
                            
                            	serial number
                            	**type**\:  str
                            
                            	**length:** 0..255
                            
                            .. attribute:: software_revision
                            
                            	software revision string
                            	**type**\:  str
                            
                            	**length:** 0..255
                            
                            .. attribute:: unique_id
                            
                            	Unique id for an entity
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: unrecognized_fru
                            
                            	1 if UnrecognizedFRU and 0 for recognizedFRU
                            	**type**\:  bool
                            
                            .. attribute:: vendor_type
                            
                            	maps to the vendor OID string
                            	**type**\:  str
                            
                            	**length:** 0..255
                            
                            .. attribute:: xr_scoped
                            
                            	1 if xr scoped, 0 if not
                            	**type**\:  bool
                            
                            

                            """

                            _prefix = 'asr9k-sc-invmgr-admin-oper'
                            _revision = '2017-01-04'

                            def __init__(self):
                                self.parent = None
                                self.alias = None
                                self.asset_id_str = None
                                self.asset_identification = None
                                self.ceport = None
                                self.chip_hardware_revision = None
                                self.composite_class_code = None
                                self.description = None
                                self.environmental_monitor_path = None
                                self.firmware_revision = None
                                self.group_flag = None
                                self.hardware_revision = None
                                self.is_field_replaceable_unit = None
                                self.manufacturer_asset_tags = None
                                self.manufacturer_name = None
                                self.memory_size = None
                                self.model_name = None
                                self.name = None
                                self.new_deviation_number = None
                                self.physical_layer_interface_module_type = None
                                self.redundancystate = None
                                self.serial_number = None
                                self.software_revision = None
                                self.unique_id = None
                                self.unrecognized_fru = None
                                self.vendor_type = None
                                self.xr_scoped = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:basic-info'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.alias is not None:
                                    return True

                                if self.asset_id_str is not None:
                                    return True

                                if self.asset_identification is not None:
                                    return True

                                if self.ceport is not None:
                                    return True

                                if self.chip_hardware_revision is not None:
                                    return True

                                if self.composite_class_code is not None:
                                    return True

                                if self.description is not None:
                                    return True

                                if self.environmental_monitor_path is not None:
                                    return True

                                if self.firmware_revision is not None:
                                    return True

                                if self.group_flag is not None:
                                    return True

                                if self.hardware_revision is not None:
                                    return True

                                if self.is_field_replaceable_unit is not None:
                                    return True

                                if self.manufacturer_asset_tags is not None:
                                    return True

                                if self.manufacturer_name is not None:
                                    return True

                                if self.memory_size is not None:
                                    return True

                                if self.model_name is not None:
                                    return True

                                if self.name is not None:
                                    return True

                                if self.new_deviation_number is not None:
                                    return True

                                if self.physical_layer_interface_module_type is not None:
                                    return True

                                if self.redundancystate is not None:
                                    return True

                                if self.serial_number is not None:
                                    return True

                                if self.software_revision is not None:
                                    return True

                                if self.unique_id is not None:
                                    return True

                                if self.unrecognized_fru is not None:
                                    return True

                                if self.vendor_type is not None:
                                    return True

                                if self.xr_scoped is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper as meta
                                return meta._meta_table['Inventory.Racks.Rack.PowerSupplyShelfs.PowerSupplyShelf.BasicAttributes.BasicInfo']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:basic-attributes'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.basic_info is not None and self.basic_info._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper as meta
                            return meta._meta_table['Inventory.Racks.Rack.PowerSupplyShelfs.PowerSupplyShelf.BasicAttributes']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.number is None:
                            raise YPYModelError('Key property number is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:power-supply-shelf[Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:number = ' + str(self.number) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.number is not None:
                            return True

                        if self.basic_attributes is not None and self.basic_attributes._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper as meta
                        return meta._meta_table['Inventory.Racks.Rack.PowerSupplyShelfs.PowerSupplyShelf']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:power-supply-shelfs'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.power_supply_shelf is not None:
                        for child_ref in self.power_supply_shelf:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper as meta
                    return meta._meta_table['Inventory.Racks.Rack.PowerSupplyShelfs']['meta_info']


            class Slots(object):
                """
                Slot table contains all slots in the rack
                
                .. attribute:: slot
                
                	Slot number
                	**type**\: list of    :py:class:`Slot <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.Inventory.Racks.Rack.Slots.Slot>`
                
                

                """

                _prefix = 'asr9k-sc-invmgr-admin-oper'
                _revision = '2017-01-04'

                def __init__(self):
                    self.parent = None
                    self.slot = YList()
                    self.slot.parent = self
                    self.slot.name = 'slot'


                class Slot(object):
                    """
                    Slot number
                    
                    .. attribute:: number  <key>
                    
                    	Slot number
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: basic_attributes
                    
                    	Attributes
                    	**type**\:   :py:class:`BasicAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.Inventory.Racks.Rack.Slots.Slot.BasicAttributes>`
                    
                    .. attribute:: cards
                    
                    	Card table contains all cards in the slot
                    	**type**\:   :py:class:`Cards <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.Inventory.Racks.Rack.Slots.Slot.Cards>`
                    
                    

                    """

                    _prefix = 'asr9k-sc-invmgr-admin-oper'
                    _revision = '2017-01-04'

                    def __init__(self):
                        self.parent = None
                        self.number = None
                        self.basic_attributes = Inventory.Racks.Rack.Slots.Slot.BasicAttributes()
                        self.basic_attributes.parent = self
                        self.cards = Inventory.Racks.Rack.Slots.Slot.Cards()
                        self.cards.parent = self


                    class Cards(object):
                        """
                        Card table contains all cards in the slot
                        
                        .. attribute:: card
                        
                        	Card number
                        	**type**\: list of    :py:class:`Card <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card>`
                        
                        

                        """

                        _prefix = 'asr9k-sc-invmgr-admin-oper'
                        _revision = '2017-01-04'

                        def __init__(self):
                            self.parent = None
                            self.card = YList()
                            self.card.parent = self
                            self.card.name = 'card'


                        class Card(object):
                            """
                            Card number
                            
                            .. attribute:: number  <key>
                            
                            	card number
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: basic_attributes
                            
                            	Attributes
                            	**type**\:   :py:class:`BasicAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.BasicAttributes>`
                            
                            .. attribute:: hw_components
                            
                            	HWComponent table contains all HW modules within the card 
                            	**type**\:   :py:class:`HwComponents <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents>`
                            
                            .. attribute:: port_slots
                            
                            	PortSlotTable contains all optics ports in a SPA/PLIM
                            	**type**\:   :py:class:`PortSlots <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots>`
                            
                            .. attribute:: sensors
                            
                            	ModuleSensorTable contains all sensors in a Module
                            	**type**\:   :py:class:`Sensors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors>`
                            
                            .. attribute:: sub_slots
                            
                            	SubSlotTable contains all subslots in a Slot
                            	**type**\:   :py:class:`SubSlots <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots>`
                            
                            

                            """

                            _prefix = 'asr9k-sc-invmgr-admin-oper'
                            _revision = '2017-01-04'

                            def __init__(self):
                                self.parent = None
                                self.number = None
                                self.basic_attributes = Inventory.Racks.Rack.Slots.Slot.Cards.Card.BasicAttributes()
                                self.basic_attributes.parent = self
                                self.hw_components = Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents()
                                self.hw_components.parent = self
                                self.port_slots = Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots()
                                self.port_slots.parent = self
                                self.sensors = Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors()
                                self.sensors.parent = self
                                self.sub_slots = Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots()
                                self.sub_slots.parent = self


                            class SubSlots(object):
                                """
                                SubSlotTable contains all subslots in a
                                Slot
                                
                                .. attribute:: sub_slot
                                
                                	SubSlot number
                                	**type**\: list of    :py:class:`SubSlot <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot>`
                                
                                

                                """

                                _prefix = 'asr9k-sc-invmgr-admin-oper'
                                _revision = '2017-01-04'

                                def __init__(self):
                                    self.parent = None
                                    self.sub_slot = YList()
                                    self.sub_slot.parent = self
                                    self.sub_slot.name = 'sub_slot'


                                class SubSlot(object):
                                    """
                                    SubSlot number
                                    
                                    .. attribute:: number  <key>
                                    
                                    	subslot number
                                    	**type**\:  int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: basic_attributes
                                    
                                    	Attributes
                                    	**type**\:   :py:class:`BasicAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.BasicAttributes>`
                                    
                                    .. attribute:: module
                                    
                                    	Module string
                                    	**type**\:   :py:class:`Module <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module>`
                                    
                                    

                                    """

                                    _prefix = 'asr9k-sc-invmgr-admin-oper'
                                    _revision = '2017-01-04'

                                    def __init__(self):
                                        self.parent = None
                                        self.number = None
                                        self.basic_attributes = Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.BasicAttributes()
                                        self.basic_attributes.parent = self
                                        self.module = Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module()
                                        self.module.parent = self


                                    class Module(object):
                                        """
                                        Module string
                                        
                                        .. attribute:: basic_attributes
                                        
                                        	Attributes
                                        	**type**\:   :py:class:`BasicAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.BasicAttributes>`
                                        
                                        .. attribute:: port_slots
                                        
                                        	PortSlotTable contains all optics ports in a SPA/PLIM
                                        	**type**\:   :py:class:`PortSlots <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots>`
                                        
                                        .. attribute:: sensors
                                        
                                        	ModuleSensorTable contains all sensors in a Module
                                        	**type**\:   :py:class:`Sensors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors>`
                                        
                                        

                                        """

                                        _prefix = 'asr9k-sc-invmgr-admin-oper'
                                        _revision = '2017-01-04'

                                        def __init__(self):
                                            self.parent = None
                                            self.basic_attributes = Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.BasicAttributes()
                                            self.basic_attributes.parent = self
                                            self.port_slots = Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots()
                                            self.port_slots.parent = self
                                            self.sensors = Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors()
                                            self.sensors.parent = self


                                        class PortSlots(object):
                                            """
                                            PortSlotTable contains all optics ports in a
                                            SPA/PLIM.
                                            
                                            .. attribute:: port_slot
                                            
                                            	PortSlot number in the SPA/PLIM
                                            	**type**\: list of    :py:class:`PortSlot <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot>`
                                            
                                            

                                            """

                                            _prefix = 'asr9k-sc-invmgr-admin-oper'
                                            _revision = '2017-01-04'

                                            def __init__(self):
                                                self.parent = None
                                                self.port_slot = YList()
                                                self.port_slot.parent = self
                                                self.port_slot.name = 'port_slot'


                                            class PortSlot(object):
                                                """
                                                PortSlot number in the SPA/PLIM
                                                
                                                .. attribute:: number  <key>
                                                
                                                	portslot number
                                                	**type**\:  int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                .. attribute:: basic_attributes
                                                
                                                	Attributes
                                                	**type**\:   :py:class:`BasicAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.BasicAttributes>`
                                                
                                                .. attribute:: port
                                                
                                                	Port string
                                                	**type**\:   :py:class:`Port <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port>`
                                                
                                                

                                                """

                                                _prefix = 'asr9k-sc-invmgr-admin-oper'
                                                _revision = '2017-01-04'

                                                def __init__(self):
                                                    self.parent = None
                                                    self.number = None
                                                    self.basic_attributes = Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.BasicAttributes()
                                                    self.basic_attributes.parent = self
                                                    self.port = Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port()
                                                    self.port.parent = self


                                                class Port(object):
                                                    """
                                                    Port string
                                                    
                                                    .. attribute:: basic_attributes
                                                    
                                                    	Attributes
                                                    	**type**\:   :py:class:`BasicAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.BasicAttributes>`
                                                    
                                                    

                                                    """

                                                    _prefix = 'asr9k-sc-invmgr-admin-oper'
                                                    _revision = '2017-01-04'

                                                    def __init__(self):
                                                        self.parent = None
                                                        self.basic_attributes = Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.BasicAttributes()
                                                        self.basic_attributes.parent = self


                                                    class BasicAttributes(object):
                                                        """
                                                        Attributes
                                                        
                                                        .. attribute:: basic_info
                                                        
                                                        	Inventory information
                                                        	**type**\:   :py:class:`BasicInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.BasicAttributes.BasicInfo>`
                                                        
                                                        .. attribute:: fru_info
                                                        
                                                        	Field Replaceable Unit (FRU) inventory information
                                                        	**type**\:   :py:class:`FruInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.BasicAttributes.FruInfo>`
                                                        
                                                        

                                                        """

                                                        _prefix = 'asr9k-sc-invmgr-admin-oper'
                                                        _revision = '2017-01-04'

                                                        def __init__(self):
                                                            self.parent = None
                                                            self.basic_info = Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.BasicAttributes.BasicInfo()
                                                            self.basic_info.parent = self
                                                            self.fru_info = Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.BasicAttributes.FruInfo()
                                                            self.fru_info.parent = self


                                                        class FruInfo(object):
                                                            """
                                                            Field Replaceable Unit (FRU) inventory
                                                            information
                                                            
                                                            .. attribute:: card_administrative_state
                                                            
                                                            	card admin state\: shutdown or not
                                                            	**type**\:  int
                                                            
                                                            	**range:** \-2147483648..2147483647
                                                            
                                                            .. attribute:: card_monitor_state
                                                            
                                                            	card is monitored by a manager or left unmonitored
                                                            	**type**\:  int
                                                            
                                                            	**range:** \-2147483648..2147483647
                                                            
                                                            .. attribute:: card_operational_state
                                                            
                                                            	card operation state
                                                            	**type**\:  int
                                                            
                                                            	**range:** \-2147483648..2147483647
                                                            
                                                            .. attribute:: card_reset_reason
                                                            
                                                            	card reset reason enum
                                                            	**type**\:   :py:class:`CardResetReasonEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.CardResetReasonEnum>`
                                                            
                                                            .. attribute:: card_up_time
                                                            
                                                            	card up time
                                                            	**type**\:   :py:class:`CardUpTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.BasicAttributes.FruInfo.CardUpTime>`
                                                            
                                                            .. attribute:: last_operational_state_change
                                                            
                                                            	last card oper change state
                                                            	**type**\:   :py:class:`LastOperationalStateChange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.BasicAttributes.FruInfo.LastOperationalStateChange>`
                                                            
                                                            .. attribute:: power_administrative_state
                                                            
                                                            	power admin state\: up or down
                                                            	**type**\:  int
                                                            
                                                            	**range:** \-2147483648..2147483647
                                                            
                                                            .. attribute:: power_current_measurement
                                                            
                                                            	power current\: not implemented
                                                            	**type**\:  int
                                                            
                                                            	**range:** \-2147483648..2147483647
                                                            
                                                            .. attribute:: power_operational_state
                                                            
                                                            	Power operation state
                                                            	**type**\:  int
                                                            
                                                            	**range:** \-2147483648..2147483647
                                                            
                                                            

                                                            """

                                                            _prefix = 'asr9k-sc-invmgr-admin-oper'
                                                            _revision = '2017-01-04'

                                                            def __init__(self):
                                                                self.parent = None
                                                                self.card_administrative_state = None
                                                                self.card_monitor_state = None
                                                                self.card_operational_state = None
                                                                self.card_reset_reason = None
                                                                self.card_up_time = Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.BasicAttributes.FruInfo.CardUpTime()
                                                                self.card_up_time.parent = self
                                                                self.last_operational_state_change = Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.BasicAttributes.FruInfo.LastOperationalStateChange()
                                                                self.last_operational_state_change.parent = self
                                                                self.power_administrative_state = None
                                                                self.power_current_measurement = None
                                                                self.power_operational_state = None


                                                            class LastOperationalStateChange(object):
                                                                """
                                                                last card oper change state
                                                                
                                                                .. attribute:: time_in_nano_seconds
                                                                
                                                                	Time Value in Nano\-seconds
                                                                	**type**\:  int
                                                                
                                                                	**range:** \-2147483648..2147483647
                                                                
                                                                	**units**\: nanosecond
                                                                
                                                                .. attribute:: time_in_seconds
                                                                
                                                                	Time Value in Seconds
                                                                	**type**\:  int
                                                                
                                                                	**range:** \-2147483648..2147483647
                                                                
                                                                	**units**\: second
                                                                
                                                                

                                                                """

                                                                _prefix = 'asr9k-sc-invmgr-admin-oper'
                                                                _revision = '2017-01-04'

                                                                def __init__(self):
                                                                    self.parent = None
                                                                    self.time_in_nano_seconds = None
                                                                    self.time_in_seconds = None

                                                                @property
                                                                def _common_path(self):
                                                                    if self.parent is None:
                                                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                                                    return self.parent._common_path +'/Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:last-operational-state-change'

                                                                def is_config(self):
                                                                    ''' Returns True if this instance represents config data else returns False '''
                                                                    return False

                                                                def _has_data(self):
                                                                    if self.time_in_nano_seconds is not None:
                                                                        return True

                                                                    if self.time_in_seconds is not None:
                                                                        return True

                                                                    return False

                                                                @staticmethod
                                                                def _meta_info():
                                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper as meta
                                                                    return meta._meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.BasicAttributes.FruInfo.LastOperationalStateChange']['meta_info']


                                                            class CardUpTime(object):
                                                                """
                                                                card up time
                                                                
                                                                .. attribute:: time_in_nano_seconds
                                                                
                                                                	Time Value in Nano\-seconds
                                                                	**type**\:  int
                                                                
                                                                	**range:** \-2147483648..2147483647
                                                                
                                                                	**units**\: nanosecond
                                                                
                                                                .. attribute:: time_in_seconds
                                                                
                                                                	Time Value in Seconds
                                                                	**type**\:  int
                                                                
                                                                	**range:** \-2147483648..2147483647
                                                                
                                                                	**units**\: second
                                                                
                                                                

                                                                """

                                                                _prefix = 'asr9k-sc-invmgr-admin-oper'
                                                                _revision = '2017-01-04'

                                                                def __init__(self):
                                                                    self.parent = None
                                                                    self.time_in_nano_seconds = None
                                                                    self.time_in_seconds = None

                                                                @property
                                                                def _common_path(self):
                                                                    if self.parent is None:
                                                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                                                    return self.parent._common_path +'/Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:card-up-time'

                                                                def is_config(self):
                                                                    ''' Returns True if this instance represents config data else returns False '''
                                                                    return False

                                                                def _has_data(self):
                                                                    if self.time_in_nano_seconds is not None:
                                                                        return True

                                                                    if self.time_in_seconds is not None:
                                                                        return True

                                                                    return False

                                                                @staticmethod
                                                                def _meta_info():
                                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper as meta
                                                                    return meta._meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.BasicAttributes.FruInfo.CardUpTime']['meta_info']

                                                            @property
                                                            def _common_path(self):
                                                                if self.parent is None:
                                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                                return self.parent._common_path +'/Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:fru-info'

                                                            def is_config(self):
                                                                ''' Returns True if this instance represents config data else returns False '''
                                                                return False

                                                            def _has_data(self):
                                                                if self.card_administrative_state is not None:
                                                                    return True

                                                                if self.card_monitor_state is not None:
                                                                    return True

                                                                if self.card_operational_state is not None:
                                                                    return True

                                                                if self.card_reset_reason is not None:
                                                                    return True

                                                                if self.card_up_time is not None and self.card_up_time._has_data():
                                                                    return True

                                                                if self.last_operational_state_change is not None and self.last_operational_state_change._has_data():
                                                                    return True

                                                                if self.power_administrative_state is not None:
                                                                    return True

                                                                if self.power_current_measurement is not None:
                                                                    return True

                                                                if self.power_operational_state is not None:
                                                                    return True

                                                                return False

                                                            @staticmethod
                                                            def _meta_info():
                                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper as meta
                                                                return meta._meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.BasicAttributes.FruInfo']['meta_info']


                                                        class BasicInfo(object):
                                                            """
                                                            Inventory information
                                                            
                                                            .. attribute:: alias
                                                            
                                                            	useful for storing an entity alias 
                                                            	**type**\:  str
                                                            
                                                            	**length:** 0..255
                                                            
                                                            .. attribute:: asset_id_str
                                                            
                                                            	asset Identification string
                                                            	**type**\:  str
                                                            
                                                            	**length:** 0..255
                                                            
                                                            .. attribute:: asset_identification
                                                            
                                                            	asset Identification
                                                            	**type**\:  int
                                                            
                                                            	**range:** \-2147483648..2147483647
                                                            
                                                            .. attribute:: ceport
                                                            
                                                            	1 if ce port found, 0 if not
                                                            	**type**\:  bool
                                                            
                                                            .. attribute:: chip_hardware_revision
                                                            
                                                            	chip module hw revision string
                                                            	**type**\:  str
                                                            
                                                            	**length:** 0..255
                                                            
                                                            .. attribute:: composite_class_code
                                                            
                                                            	Major&minor class of the entity
                                                            	**type**\:  int
                                                            
                                                            	**range:** \-2147483648..2147483647
                                                            
                                                            .. attribute:: description
                                                            
                                                            	describes in user\-readable terms       what the entity in question does
                                                            	**type**\:  str
                                                            
                                                            	**length:** 0..255
                                                            
                                                            .. attribute:: environmental_monitor_path
                                                            
                                                            	sysdb name of sensor in the envmon EDM
                                                            	**type**\:  str
                                                            
                                                            	**length:** 0..255
                                                            
                                                            .. attribute:: firmware_revision
                                                            
                                                            	firmware revision string
                                                            	**type**\:  str
                                                            
                                                            	**length:** 0..255
                                                            
                                                            .. attribute:: group_flag
                                                            
                                                            	indicates if this entity is group       or not
                                                            	**type**\:  bool
                                                            
                                                            .. attribute:: hardware_revision
                                                            
                                                            	hw revision string
                                                            	**type**\:  str
                                                            
                                                            	**length:** 0..255
                                                            
                                                            .. attribute:: is_field_replaceable_unit
                                                            
                                                            	1 if Field Replaceable Unit 0, if not
                                                            	**type**\:  bool
                                                            
                                                            .. attribute:: manufacturer_asset_tags
                                                            
                                                            	Manufacture Asset Tags
                                                            	**type**\:  int
                                                            
                                                            	**range:** \-2147483648..2147483647
                                                            
                                                            .. attribute:: manufacturer_name
                                                            
                                                            	manufacturer's name
                                                            	**type**\:  str
                                                            
                                                            	**length:** 0..255
                                                            
                                                            .. attribute:: memory_size
                                                            
                                                            	Size of memory associated with       the entity where applicable
                                                            	**type**\:  int
                                                            
                                                            	**range:** \-2147483648..2147483647
                                                            
                                                            .. attribute:: model_name
                                                            
                                                            	model name
                                                            	**type**\:  str
                                                            
                                                            	**length:** 0..255
                                                            
                                                            .. attribute:: name
                                                            
                                                            	name string for the entity
                                                            	**type**\:  str
                                                            
                                                            	**length:** 0..255
                                                            
                                                            .. attribute:: new_deviation_number
                                                            
                                                            	integer value for New Deviation Number 0x88
                                                            	**type**\:  int
                                                            
                                                            	**range:** \-2147483648..2147483647
                                                            
                                                            .. attribute:: physical_layer_interface_module_type
                                                            
                                                            	integer value for plim type if     applicable to this entity
                                                            	**type**\:  int
                                                            
                                                            	**range:** \-2147483648..2147483647
                                                            
                                                            .. attribute:: redundancystate
                                                            
                                                            	integer value for Redundancy State if     applicable to this entity
                                                            	**type**\:  int
                                                            
                                                            	**range:** \-2147483648..2147483647
                                                            
                                                            .. attribute:: serial_number
                                                            
                                                            	serial number
                                                            	**type**\:  str
                                                            
                                                            	**length:** 0..255
                                                            
                                                            .. attribute:: software_revision
                                                            
                                                            	software revision string
                                                            	**type**\:  str
                                                            
                                                            	**length:** 0..255
                                                            
                                                            .. attribute:: unique_id
                                                            
                                                            	Unique id for an entity
                                                            	**type**\:  int
                                                            
                                                            	**range:** \-2147483648..2147483647
                                                            
                                                            .. attribute:: unrecognized_fru
                                                            
                                                            	1 if UnrecognizedFRU and 0 for recognizedFRU
                                                            	**type**\:  bool
                                                            
                                                            .. attribute:: vendor_type
                                                            
                                                            	maps to the vendor OID string
                                                            	**type**\:  str
                                                            
                                                            	**length:** 0..255
                                                            
                                                            .. attribute:: xr_scoped
                                                            
                                                            	1 if xr scoped, 0 if not
                                                            	**type**\:  bool
                                                            
                                                            

                                                            """

                                                            _prefix = 'asr9k-sc-invmgr-admin-oper'
                                                            _revision = '2017-01-04'

                                                            def __init__(self):
                                                                self.parent = None
                                                                self.alias = None
                                                                self.asset_id_str = None
                                                                self.asset_identification = None
                                                                self.ceport = None
                                                                self.chip_hardware_revision = None
                                                                self.composite_class_code = None
                                                                self.description = None
                                                                self.environmental_monitor_path = None
                                                                self.firmware_revision = None
                                                                self.group_flag = None
                                                                self.hardware_revision = None
                                                                self.is_field_replaceable_unit = None
                                                                self.manufacturer_asset_tags = None
                                                                self.manufacturer_name = None
                                                                self.memory_size = None
                                                                self.model_name = None
                                                                self.name = None
                                                                self.new_deviation_number = None
                                                                self.physical_layer_interface_module_type = None
                                                                self.redundancystate = None
                                                                self.serial_number = None
                                                                self.software_revision = None
                                                                self.unique_id = None
                                                                self.unrecognized_fru = None
                                                                self.vendor_type = None
                                                                self.xr_scoped = None

                                                            @property
                                                            def _common_path(self):
                                                                if self.parent is None:
                                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                                return self.parent._common_path +'/Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:basic-info'

                                                            def is_config(self):
                                                                ''' Returns True if this instance represents config data else returns False '''
                                                                return False

                                                            def _has_data(self):
                                                                if self.alias is not None:
                                                                    return True

                                                                if self.asset_id_str is not None:
                                                                    return True

                                                                if self.asset_identification is not None:
                                                                    return True

                                                                if self.ceport is not None:
                                                                    return True

                                                                if self.chip_hardware_revision is not None:
                                                                    return True

                                                                if self.composite_class_code is not None:
                                                                    return True

                                                                if self.description is not None:
                                                                    return True

                                                                if self.environmental_monitor_path is not None:
                                                                    return True

                                                                if self.firmware_revision is not None:
                                                                    return True

                                                                if self.group_flag is not None:
                                                                    return True

                                                                if self.hardware_revision is not None:
                                                                    return True

                                                                if self.is_field_replaceable_unit is not None:
                                                                    return True

                                                                if self.manufacturer_asset_tags is not None:
                                                                    return True

                                                                if self.manufacturer_name is not None:
                                                                    return True

                                                                if self.memory_size is not None:
                                                                    return True

                                                                if self.model_name is not None:
                                                                    return True

                                                                if self.name is not None:
                                                                    return True

                                                                if self.new_deviation_number is not None:
                                                                    return True

                                                                if self.physical_layer_interface_module_type is not None:
                                                                    return True

                                                                if self.redundancystate is not None:
                                                                    return True

                                                                if self.serial_number is not None:
                                                                    return True

                                                                if self.software_revision is not None:
                                                                    return True

                                                                if self.unique_id is not None:
                                                                    return True

                                                                if self.unrecognized_fru is not None:
                                                                    return True

                                                                if self.vendor_type is not None:
                                                                    return True

                                                                if self.xr_scoped is not None:
                                                                    return True

                                                                return False

                                                            @staticmethod
                                                            def _meta_info():
                                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper as meta
                                                                return meta._meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.BasicAttributes.BasicInfo']['meta_info']

                                                        @property
                                                        def _common_path(self):
                                                            if self.parent is None:
                                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                                            return self.parent._common_path +'/Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:basic-attributes'

                                                        def is_config(self):
                                                            ''' Returns True if this instance represents config data else returns False '''
                                                            return False

                                                        def _has_data(self):
                                                            if self.basic_info is not None and self.basic_info._has_data():
                                                                return True

                                                            if self.fru_info is not None and self.fru_info._has_data():
                                                                return True

                                                            return False

                                                        @staticmethod
                                                        def _meta_info():
                                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper as meta
                                                            return meta._meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.BasicAttributes']['meta_info']

                                                    @property
                                                    def _common_path(self):
                                                        if self.parent is None:
                                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                                        return self.parent._common_path +'/Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:port'

                                                    def is_config(self):
                                                        ''' Returns True if this instance represents config data else returns False '''
                                                        return False

                                                    def _has_data(self):
                                                        if self.basic_attributes is not None and self.basic_attributes._has_data():
                                                            return True

                                                        return False

                                                    @staticmethod
                                                    def _meta_info():
                                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper as meta
                                                        return meta._meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port']['meta_info']


                                                class BasicAttributes(object):
                                                    """
                                                    Attributes
                                                    
                                                    .. attribute:: basic_info
                                                    
                                                    	Inventory information
                                                    	**type**\:   :py:class:`BasicInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.BasicAttributes.BasicInfo>`
                                                    
                                                    .. attribute:: fru_info
                                                    
                                                    	Field Replaceable Unit (FRU) inventory information
                                                    	**type**\:   :py:class:`FruInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.BasicAttributes.FruInfo>`
                                                    
                                                    

                                                    """

                                                    _prefix = 'asr9k-sc-invmgr-admin-oper'
                                                    _revision = '2017-01-04'

                                                    def __init__(self):
                                                        self.parent = None
                                                        self.basic_info = Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.BasicAttributes.BasicInfo()
                                                        self.basic_info.parent = self
                                                        self.fru_info = Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.BasicAttributes.FruInfo()
                                                        self.fru_info.parent = self


                                                    class FruInfo(object):
                                                        """
                                                        Field Replaceable Unit (FRU) inventory
                                                        information
                                                        
                                                        .. attribute:: card_administrative_state
                                                        
                                                        	card admin state\: shutdown or not
                                                        	**type**\:  int
                                                        
                                                        	**range:** \-2147483648..2147483647
                                                        
                                                        .. attribute:: card_monitor_state
                                                        
                                                        	card is monitored by a manager or left unmonitored
                                                        	**type**\:  int
                                                        
                                                        	**range:** \-2147483648..2147483647
                                                        
                                                        .. attribute:: card_operational_state
                                                        
                                                        	card operation state
                                                        	**type**\:  int
                                                        
                                                        	**range:** \-2147483648..2147483647
                                                        
                                                        .. attribute:: card_reset_reason
                                                        
                                                        	card reset reason enum
                                                        	**type**\:   :py:class:`CardResetReasonEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.CardResetReasonEnum>`
                                                        
                                                        .. attribute:: card_up_time
                                                        
                                                        	card up time
                                                        	**type**\:   :py:class:`CardUpTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.BasicAttributes.FruInfo.CardUpTime>`
                                                        
                                                        .. attribute:: last_operational_state_change
                                                        
                                                        	last card oper change state
                                                        	**type**\:   :py:class:`LastOperationalStateChange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.BasicAttributes.FruInfo.LastOperationalStateChange>`
                                                        
                                                        .. attribute:: power_administrative_state
                                                        
                                                        	power admin state\: up or down
                                                        	**type**\:  int
                                                        
                                                        	**range:** \-2147483648..2147483647
                                                        
                                                        .. attribute:: power_current_measurement
                                                        
                                                        	power current\: not implemented
                                                        	**type**\:  int
                                                        
                                                        	**range:** \-2147483648..2147483647
                                                        
                                                        .. attribute:: power_operational_state
                                                        
                                                        	Power operation state
                                                        	**type**\:  int
                                                        
                                                        	**range:** \-2147483648..2147483647
                                                        
                                                        

                                                        """

                                                        _prefix = 'asr9k-sc-invmgr-admin-oper'
                                                        _revision = '2017-01-04'

                                                        def __init__(self):
                                                            self.parent = None
                                                            self.card_administrative_state = None
                                                            self.card_monitor_state = None
                                                            self.card_operational_state = None
                                                            self.card_reset_reason = None
                                                            self.card_up_time = Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.BasicAttributes.FruInfo.CardUpTime()
                                                            self.card_up_time.parent = self
                                                            self.last_operational_state_change = Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.BasicAttributes.FruInfo.LastOperationalStateChange()
                                                            self.last_operational_state_change.parent = self
                                                            self.power_administrative_state = None
                                                            self.power_current_measurement = None
                                                            self.power_operational_state = None


                                                        class LastOperationalStateChange(object):
                                                            """
                                                            last card oper change state
                                                            
                                                            .. attribute:: time_in_nano_seconds
                                                            
                                                            	Time Value in Nano\-seconds
                                                            	**type**\:  int
                                                            
                                                            	**range:** \-2147483648..2147483647
                                                            
                                                            	**units**\: nanosecond
                                                            
                                                            .. attribute:: time_in_seconds
                                                            
                                                            	Time Value in Seconds
                                                            	**type**\:  int
                                                            
                                                            	**range:** \-2147483648..2147483647
                                                            
                                                            	**units**\: second
                                                            
                                                            

                                                            """

                                                            _prefix = 'asr9k-sc-invmgr-admin-oper'
                                                            _revision = '2017-01-04'

                                                            def __init__(self):
                                                                self.parent = None
                                                                self.time_in_nano_seconds = None
                                                                self.time_in_seconds = None

                                                            @property
                                                            def _common_path(self):
                                                                if self.parent is None:
                                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                                return self.parent._common_path +'/Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:last-operational-state-change'

                                                            def is_config(self):
                                                                ''' Returns True if this instance represents config data else returns False '''
                                                                return False

                                                            def _has_data(self):
                                                                if self.time_in_nano_seconds is not None:
                                                                    return True

                                                                if self.time_in_seconds is not None:
                                                                    return True

                                                                return False

                                                            @staticmethod
                                                            def _meta_info():
                                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper as meta
                                                                return meta._meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.BasicAttributes.FruInfo.LastOperationalStateChange']['meta_info']


                                                        class CardUpTime(object):
                                                            """
                                                            card up time
                                                            
                                                            .. attribute:: time_in_nano_seconds
                                                            
                                                            	Time Value in Nano\-seconds
                                                            	**type**\:  int
                                                            
                                                            	**range:** \-2147483648..2147483647
                                                            
                                                            	**units**\: nanosecond
                                                            
                                                            .. attribute:: time_in_seconds
                                                            
                                                            	Time Value in Seconds
                                                            	**type**\:  int
                                                            
                                                            	**range:** \-2147483648..2147483647
                                                            
                                                            	**units**\: second
                                                            
                                                            

                                                            """

                                                            _prefix = 'asr9k-sc-invmgr-admin-oper'
                                                            _revision = '2017-01-04'

                                                            def __init__(self):
                                                                self.parent = None
                                                                self.time_in_nano_seconds = None
                                                                self.time_in_seconds = None

                                                            @property
                                                            def _common_path(self):
                                                                if self.parent is None:
                                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                                return self.parent._common_path +'/Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:card-up-time'

                                                            def is_config(self):
                                                                ''' Returns True if this instance represents config data else returns False '''
                                                                return False

                                                            def _has_data(self):
                                                                if self.time_in_nano_seconds is not None:
                                                                    return True

                                                                if self.time_in_seconds is not None:
                                                                    return True

                                                                return False

                                                            @staticmethod
                                                            def _meta_info():
                                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper as meta
                                                                return meta._meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.BasicAttributes.FruInfo.CardUpTime']['meta_info']

                                                        @property
                                                        def _common_path(self):
                                                            if self.parent is None:
                                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                                            return self.parent._common_path +'/Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:fru-info'

                                                        def is_config(self):
                                                            ''' Returns True if this instance represents config data else returns False '''
                                                            return False

                                                        def _has_data(self):
                                                            if self.card_administrative_state is not None:
                                                                return True

                                                            if self.card_monitor_state is not None:
                                                                return True

                                                            if self.card_operational_state is not None:
                                                                return True

                                                            if self.card_reset_reason is not None:
                                                                return True

                                                            if self.card_up_time is not None and self.card_up_time._has_data():
                                                                return True

                                                            if self.last_operational_state_change is not None and self.last_operational_state_change._has_data():
                                                                return True

                                                            if self.power_administrative_state is not None:
                                                                return True

                                                            if self.power_current_measurement is not None:
                                                                return True

                                                            if self.power_operational_state is not None:
                                                                return True

                                                            return False

                                                        @staticmethod
                                                        def _meta_info():
                                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper as meta
                                                            return meta._meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.BasicAttributes.FruInfo']['meta_info']


                                                    class BasicInfo(object):
                                                        """
                                                        Inventory information
                                                        
                                                        .. attribute:: alias
                                                        
                                                        	useful for storing an entity alias 
                                                        	**type**\:  str
                                                        
                                                        	**length:** 0..255
                                                        
                                                        .. attribute:: asset_id_str
                                                        
                                                        	asset Identification string
                                                        	**type**\:  str
                                                        
                                                        	**length:** 0..255
                                                        
                                                        .. attribute:: asset_identification
                                                        
                                                        	asset Identification
                                                        	**type**\:  int
                                                        
                                                        	**range:** \-2147483648..2147483647
                                                        
                                                        .. attribute:: ceport
                                                        
                                                        	1 if ce port found, 0 if not
                                                        	**type**\:  bool
                                                        
                                                        .. attribute:: chip_hardware_revision
                                                        
                                                        	chip module hw revision string
                                                        	**type**\:  str
                                                        
                                                        	**length:** 0..255
                                                        
                                                        .. attribute:: composite_class_code
                                                        
                                                        	Major&minor class of the entity
                                                        	**type**\:  int
                                                        
                                                        	**range:** \-2147483648..2147483647
                                                        
                                                        .. attribute:: description
                                                        
                                                        	describes in user\-readable terms       what the entity in question does
                                                        	**type**\:  str
                                                        
                                                        	**length:** 0..255
                                                        
                                                        .. attribute:: environmental_monitor_path
                                                        
                                                        	sysdb name of sensor in the envmon EDM
                                                        	**type**\:  str
                                                        
                                                        	**length:** 0..255
                                                        
                                                        .. attribute:: firmware_revision
                                                        
                                                        	firmware revision string
                                                        	**type**\:  str
                                                        
                                                        	**length:** 0..255
                                                        
                                                        .. attribute:: group_flag
                                                        
                                                        	indicates if this entity is group       or not
                                                        	**type**\:  bool
                                                        
                                                        .. attribute:: hardware_revision
                                                        
                                                        	hw revision string
                                                        	**type**\:  str
                                                        
                                                        	**length:** 0..255
                                                        
                                                        .. attribute:: is_field_replaceable_unit
                                                        
                                                        	1 if Field Replaceable Unit 0, if not
                                                        	**type**\:  bool
                                                        
                                                        .. attribute:: manufacturer_asset_tags
                                                        
                                                        	Manufacture Asset Tags
                                                        	**type**\:  int
                                                        
                                                        	**range:** \-2147483648..2147483647
                                                        
                                                        .. attribute:: manufacturer_name
                                                        
                                                        	manufacturer's name
                                                        	**type**\:  str
                                                        
                                                        	**length:** 0..255
                                                        
                                                        .. attribute:: memory_size
                                                        
                                                        	Size of memory associated with       the entity where applicable
                                                        	**type**\:  int
                                                        
                                                        	**range:** \-2147483648..2147483647
                                                        
                                                        .. attribute:: model_name
                                                        
                                                        	model name
                                                        	**type**\:  str
                                                        
                                                        	**length:** 0..255
                                                        
                                                        .. attribute:: name
                                                        
                                                        	name string for the entity
                                                        	**type**\:  str
                                                        
                                                        	**length:** 0..255
                                                        
                                                        .. attribute:: new_deviation_number
                                                        
                                                        	integer value for New Deviation Number 0x88
                                                        	**type**\:  int
                                                        
                                                        	**range:** \-2147483648..2147483647
                                                        
                                                        .. attribute:: physical_layer_interface_module_type
                                                        
                                                        	integer value for plim type if     applicable to this entity
                                                        	**type**\:  int
                                                        
                                                        	**range:** \-2147483648..2147483647
                                                        
                                                        .. attribute:: redundancystate
                                                        
                                                        	integer value for Redundancy State if     applicable to this entity
                                                        	**type**\:  int
                                                        
                                                        	**range:** \-2147483648..2147483647
                                                        
                                                        .. attribute:: serial_number
                                                        
                                                        	serial number
                                                        	**type**\:  str
                                                        
                                                        	**length:** 0..255
                                                        
                                                        .. attribute:: software_revision
                                                        
                                                        	software revision string
                                                        	**type**\:  str
                                                        
                                                        	**length:** 0..255
                                                        
                                                        .. attribute:: unique_id
                                                        
                                                        	Unique id for an entity
                                                        	**type**\:  int
                                                        
                                                        	**range:** \-2147483648..2147483647
                                                        
                                                        .. attribute:: unrecognized_fru
                                                        
                                                        	1 if UnrecognizedFRU and 0 for recognizedFRU
                                                        	**type**\:  bool
                                                        
                                                        .. attribute:: vendor_type
                                                        
                                                        	maps to the vendor OID string
                                                        	**type**\:  str
                                                        
                                                        	**length:** 0..255
                                                        
                                                        .. attribute:: xr_scoped
                                                        
                                                        	1 if xr scoped, 0 if not
                                                        	**type**\:  bool
                                                        
                                                        

                                                        """

                                                        _prefix = 'asr9k-sc-invmgr-admin-oper'
                                                        _revision = '2017-01-04'

                                                        def __init__(self):
                                                            self.parent = None
                                                            self.alias = None
                                                            self.asset_id_str = None
                                                            self.asset_identification = None
                                                            self.ceport = None
                                                            self.chip_hardware_revision = None
                                                            self.composite_class_code = None
                                                            self.description = None
                                                            self.environmental_monitor_path = None
                                                            self.firmware_revision = None
                                                            self.group_flag = None
                                                            self.hardware_revision = None
                                                            self.is_field_replaceable_unit = None
                                                            self.manufacturer_asset_tags = None
                                                            self.manufacturer_name = None
                                                            self.memory_size = None
                                                            self.model_name = None
                                                            self.name = None
                                                            self.new_deviation_number = None
                                                            self.physical_layer_interface_module_type = None
                                                            self.redundancystate = None
                                                            self.serial_number = None
                                                            self.software_revision = None
                                                            self.unique_id = None
                                                            self.unrecognized_fru = None
                                                            self.vendor_type = None
                                                            self.xr_scoped = None

                                                        @property
                                                        def _common_path(self):
                                                            if self.parent is None:
                                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                                            return self.parent._common_path +'/Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:basic-info'

                                                        def is_config(self):
                                                            ''' Returns True if this instance represents config data else returns False '''
                                                            return False

                                                        def _has_data(self):
                                                            if self.alias is not None:
                                                                return True

                                                            if self.asset_id_str is not None:
                                                                return True

                                                            if self.asset_identification is not None:
                                                                return True

                                                            if self.ceport is not None:
                                                                return True

                                                            if self.chip_hardware_revision is not None:
                                                                return True

                                                            if self.composite_class_code is not None:
                                                                return True

                                                            if self.description is not None:
                                                                return True

                                                            if self.environmental_monitor_path is not None:
                                                                return True

                                                            if self.firmware_revision is not None:
                                                                return True

                                                            if self.group_flag is not None:
                                                                return True

                                                            if self.hardware_revision is not None:
                                                                return True

                                                            if self.is_field_replaceable_unit is not None:
                                                                return True

                                                            if self.manufacturer_asset_tags is not None:
                                                                return True

                                                            if self.manufacturer_name is not None:
                                                                return True

                                                            if self.memory_size is not None:
                                                                return True

                                                            if self.model_name is not None:
                                                                return True

                                                            if self.name is not None:
                                                                return True

                                                            if self.new_deviation_number is not None:
                                                                return True

                                                            if self.physical_layer_interface_module_type is not None:
                                                                return True

                                                            if self.redundancystate is not None:
                                                                return True

                                                            if self.serial_number is not None:
                                                                return True

                                                            if self.software_revision is not None:
                                                                return True

                                                            if self.unique_id is not None:
                                                                return True

                                                            if self.unrecognized_fru is not None:
                                                                return True

                                                            if self.vendor_type is not None:
                                                                return True

                                                            if self.xr_scoped is not None:
                                                                return True

                                                            return False

                                                        @staticmethod
                                                        def _meta_info():
                                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper as meta
                                                            return meta._meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.BasicAttributes.BasicInfo']['meta_info']

                                                    @property
                                                    def _common_path(self):
                                                        if self.parent is None:
                                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                                        return self.parent._common_path +'/Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:basic-attributes'

                                                    def is_config(self):
                                                        ''' Returns True if this instance represents config data else returns False '''
                                                        return False

                                                    def _has_data(self):
                                                        if self.basic_info is not None and self.basic_info._has_data():
                                                            return True

                                                        if self.fru_info is not None and self.fru_info._has_data():
                                                            return True

                                                        return False

                                                    @staticmethod
                                                    def _meta_info():
                                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper as meta
                                                        return meta._meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.BasicAttributes']['meta_info']

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                                    if self.number is None:
                                                        raise YPYModelError('Key property number is None')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:port-slot[Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:number = ' + str(self.number) + ']'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if self.number is not None:
                                                        return True

                                                    if self.basic_attributes is not None and self.basic_attributes._has_data():
                                                        return True

                                                    if self.port is not None and self.port._has_data():
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper as meta
                                                    return meta._meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot']['meta_info']

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:port-slots'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.port_slot is not None:
                                                    for child_ref in self.port_slot:
                                                        if child_ref._has_data():
                                                            return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper as meta
                                                return meta._meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots']['meta_info']


                                        class Sensors(object):
                                            """
                                            ModuleSensorTable contains all sensors in a
                                            Module.
                                            
                                            .. attribute:: sensor
                                            
                                            	Sensor number in the Module
                                            	**type**\: list of    :py:class:`Sensor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor>`
                                            
                                            

                                            """

                                            _prefix = 'asr9k-sc-invmgr-admin-oper'
                                            _revision = '2017-01-04'

                                            def __init__(self):
                                                self.parent = None
                                                self.sensor = YList()
                                                self.sensor.parent = self
                                                self.sensor.name = 'sensor'


                                            class Sensor(object):
                                                """
                                                Sensor number in the Module
                                                
                                                .. attribute:: number  <key>
                                                
                                                	sensor number
                                                	**type**\:  int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                .. attribute:: basic_attributes
                                                
                                                	Attributes
                                                	**type**\:   :py:class:`BasicAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.BasicAttributes>`
                                                
                                                

                                                """

                                                _prefix = 'asr9k-sc-invmgr-admin-oper'
                                                _revision = '2017-01-04'

                                                def __init__(self):
                                                    self.parent = None
                                                    self.number = None
                                                    self.basic_attributes = Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.BasicAttributes()
                                                    self.basic_attributes.parent = self


                                                class BasicAttributes(object):
                                                    """
                                                    Attributes
                                                    
                                                    .. attribute:: basic_info
                                                    
                                                    	Inventory information
                                                    	**type**\:   :py:class:`BasicInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.BasicAttributes.BasicInfo>`
                                                    
                                                    .. attribute:: fru_info
                                                    
                                                    	Field Replaceable Unit (FRU) inventory information
                                                    	**type**\:   :py:class:`FruInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.BasicAttributes.FruInfo>`
                                                    
                                                    

                                                    """

                                                    _prefix = 'asr9k-sc-invmgr-admin-oper'
                                                    _revision = '2017-01-04'

                                                    def __init__(self):
                                                        self.parent = None
                                                        self.basic_info = Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.BasicAttributes.BasicInfo()
                                                        self.basic_info.parent = self
                                                        self.fru_info = Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.BasicAttributes.FruInfo()
                                                        self.fru_info.parent = self


                                                    class FruInfo(object):
                                                        """
                                                        Field Replaceable Unit (FRU) inventory
                                                        information
                                                        
                                                        .. attribute:: card_administrative_state
                                                        
                                                        	card admin state\: shutdown or not
                                                        	**type**\:  int
                                                        
                                                        	**range:** \-2147483648..2147483647
                                                        
                                                        .. attribute:: card_monitor_state
                                                        
                                                        	card is monitored by a manager or left unmonitored
                                                        	**type**\:  int
                                                        
                                                        	**range:** \-2147483648..2147483647
                                                        
                                                        .. attribute:: card_operational_state
                                                        
                                                        	card operation state
                                                        	**type**\:  int
                                                        
                                                        	**range:** \-2147483648..2147483647
                                                        
                                                        .. attribute:: card_reset_reason
                                                        
                                                        	card reset reason enum
                                                        	**type**\:   :py:class:`CardResetReasonEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.CardResetReasonEnum>`
                                                        
                                                        .. attribute:: card_up_time
                                                        
                                                        	card up time
                                                        	**type**\:   :py:class:`CardUpTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.BasicAttributes.FruInfo.CardUpTime>`
                                                        
                                                        .. attribute:: last_operational_state_change
                                                        
                                                        	last card oper change state
                                                        	**type**\:   :py:class:`LastOperationalStateChange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.BasicAttributes.FruInfo.LastOperationalStateChange>`
                                                        
                                                        .. attribute:: power_administrative_state
                                                        
                                                        	power admin state\: up or down
                                                        	**type**\:  int
                                                        
                                                        	**range:** \-2147483648..2147483647
                                                        
                                                        .. attribute:: power_current_measurement
                                                        
                                                        	power current\: not implemented
                                                        	**type**\:  int
                                                        
                                                        	**range:** \-2147483648..2147483647
                                                        
                                                        .. attribute:: power_operational_state
                                                        
                                                        	Power operation state
                                                        	**type**\:  int
                                                        
                                                        	**range:** \-2147483648..2147483647
                                                        
                                                        

                                                        """

                                                        _prefix = 'asr9k-sc-invmgr-admin-oper'
                                                        _revision = '2017-01-04'

                                                        def __init__(self):
                                                            self.parent = None
                                                            self.card_administrative_state = None
                                                            self.card_monitor_state = None
                                                            self.card_operational_state = None
                                                            self.card_reset_reason = None
                                                            self.card_up_time = Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.BasicAttributes.FruInfo.CardUpTime()
                                                            self.card_up_time.parent = self
                                                            self.last_operational_state_change = Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.BasicAttributes.FruInfo.LastOperationalStateChange()
                                                            self.last_operational_state_change.parent = self
                                                            self.power_administrative_state = None
                                                            self.power_current_measurement = None
                                                            self.power_operational_state = None


                                                        class LastOperationalStateChange(object):
                                                            """
                                                            last card oper change state
                                                            
                                                            .. attribute:: time_in_nano_seconds
                                                            
                                                            	Time Value in Nano\-seconds
                                                            	**type**\:  int
                                                            
                                                            	**range:** \-2147483648..2147483647
                                                            
                                                            	**units**\: nanosecond
                                                            
                                                            .. attribute:: time_in_seconds
                                                            
                                                            	Time Value in Seconds
                                                            	**type**\:  int
                                                            
                                                            	**range:** \-2147483648..2147483647
                                                            
                                                            	**units**\: second
                                                            
                                                            

                                                            """

                                                            _prefix = 'asr9k-sc-invmgr-admin-oper'
                                                            _revision = '2017-01-04'

                                                            def __init__(self):
                                                                self.parent = None
                                                                self.time_in_nano_seconds = None
                                                                self.time_in_seconds = None

                                                            @property
                                                            def _common_path(self):
                                                                if self.parent is None:
                                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                                return self.parent._common_path +'/Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:last-operational-state-change'

                                                            def is_config(self):
                                                                ''' Returns True if this instance represents config data else returns False '''
                                                                return False

                                                            def _has_data(self):
                                                                if self.time_in_nano_seconds is not None:
                                                                    return True

                                                                if self.time_in_seconds is not None:
                                                                    return True

                                                                return False

                                                            @staticmethod
                                                            def _meta_info():
                                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper as meta
                                                                return meta._meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.BasicAttributes.FruInfo.LastOperationalStateChange']['meta_info']


                                                        class CardUpTime(object):
                                                            """
                                                            card up time
                                                            
                                                            .. attribute:: time_in_nano_seconds
                                                            
                                                            	Time Value in Nano\-seconds
                                                            	**type**\:  int
                                                            
                                                            	**range:** \-2147483648..2147483647
                                                            
                                                            	**units**\: nanosecond
                                                            
                                                            .. attribute:: time_in_seconds
                                                            
                                                            	Time Value in Seconds
                                                            	**type**\:  int
                                                            
                                                            	**range:** \-2147483648..2147483647
                                                            
                                                            	**units**\: second
                                                            
                                                            

                                                            """

                                                            _prefix = 'asr9k-sc-invmgr-admin-oper'
                                                            _revision = '2017-01-04'

                                                            def __init__(self):
                                                                self.parent = None
                                                                self.time_in_nano_seconds = None
                                                                self.time_in_seconds = None

                                                            @property
                                                            def _common_path(self):
                                                                if self.parent is None:
                                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                                return self.parent._common_path +'/Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:card-up-time'

                                                            def is_config(self):
                                                                ''' Returns True if this instance represents config data else returns False '''
                                                                return False

                                                            def _has_data(self):
                                                                if self.time_in_nano_seconds is not None:
                                                                    return True

                                                                if self.time_in_seconds is not None:
                                                                    return True

                                                                return False

                                                            @staticmethod
                                                            def _meta_info():
                                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper as meta
                                                                return meta._meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.BasicAttributes.FruInfo.CardUpTime']['meta_info']

                                                        @property
                                                        def _common_path(self):
                                                            if self.parent is None:
                                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                                            return self.parent._common_path +'/Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:fru-info'

                                                        def is_config(self):
                                                            ''' Returns True if this instance represents config data else returns False '''
                                                            return False

                                                        def _has_data(self):
                                                            if self.card_administrative_state is not None:
                                                                return True

                                                            if self.card_monitor_state is not None:
                                                                return True

                                                            if self.card_operational_state is not None:
                                                                return True

                                                            if self.card_reset_reason is not None:
                                                                return True

                                                            if self.card_up_time is not None and self.card_up_time._has_data():
                                                                return True

                                                            if self.last_operational_state_change is not None and self.last_operational_state_change._has_data():
                                                                return True

                                                            if self.power_administrative_state is not None:
                                                                return True

                                                            if self.power_current_measurement is not None:
                                                                return True

                                                            if self.power_operational_state is not None:
                                                                return True

                                                            return False

                                                        @staticmethod
                                                        def _meta_info():
                                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper as meta
                                                            return meta._meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.BasicAttributes.FruInfo']['meta_info']


                                                    class BasicInfo(object):
                                                        """
                                                        Inventory information
                                                        
                                                        .. attribute:: alias
                                                        
                                                        	useful for storing an entity alias 
                                                        	**type**\:  str
                                                        
                                                        	**length:** 0..255
                                                        
                                                        .. attribute:: asset_id_str
                                                        
                                                        	asset Identification string
                                                        	**type**\:  str
                                                        
                                                        	**length:** 0..255
                                                        
                                                        .. attribute:: asset_identification
                                                        
                                                        	asset Identification
                                                        	**type**\:  int
                                                        
                                                        	**range:** \-2147483648..2147483647
                                                        
                                                        .. attribute:: ceport
                                                        
                                                        	1 if ce port found, 0 if not
                                                        	**type**\:  bool
                                                        
                                                        .. attribute:: chip_hardware_revision
                                                        
                                                        	chip module hw revision string
                                                        	**type**\:  str
                                                        
                                                        	**length:** 0..255
                                                        
                                                        .. attribute:: composite_class_code
                                                        
                                                        	Major&minor class of the entity
                                                        	**type**\:  int
                                                        
                                                        	**range:** \-2147483648..2147483647
                                                        
                                                        .. attribute:: description
                                                        
                                                        	describes in user\-readable terms       what the entity in question does
                                                        	**type**\:  str
                                                        
                                                        	**length:** 0..255
                                                        
                                                        .. attribute:: environmental_monitor_path
                                                        
                                                        	sysdb name of sensor in the envmon EDM
                                                        	**type**\:  str
                                                        
                                                        	**length:** 0..255
                                                        
                                                        .. attribute:: firmware_revision
                                                        
                                                        	firmware revision string
                                                        	**type**\:  str
                                                        
                                                        	**length:** 0..255
                                                        
                                                        .. attribute:: group_flag
                                                        
                                                        	indicates if this entity is group       or not
                                                        	**type**\:  bool
                                                        
                                                        .. attribute:: hardware_revision
                                                        
                                                        	hw revision string
                                                        	**type**\:  str
                                                        
                                                        	**length:** 0..255
                                                        
                                                        .. attribute:: is_field_replaceable_unit
                                                        
                                                        	1 if Field Replaceable Unit 0, if not
                                                        	**type**\:  bool
                                                        
                                                        .. attribute:: manufacturer_asset_tags
                                                        
                                                        	Manufacture Asset Tags
                                                        	**type**\:  int
                                                        
                                                        	**range:** \-2147483648..2147483647
                                                        
                                                        .. attribute:: manufacturer_name
                                                        
                                                        	manufacturer's name
                                                        	**type**\:  str
                                                        
                                                        	**length:** 0..255
                                                        
                                                        .. attribute:: memory_size
                                                        
                                                        	Size of memory associated with       the entity where applicable
                                                        	**type**\:  int
                                                        
                                                        	**range:** \-2147483648..2147483647
                                                        
                                                        .. attribute:: model_name
                                                        
                                                        	model name
                                                        	**type**\:  str
                                                        
                                                        	**length:** 0..255
                                                        
                                                        .. attribute:: name
                                                        
                                                        	name string for the entity
                                                        	**type**\:  str
                                                        
                                                        	**length:** 0..255
                                                        
                                                        .. attribute:: new_deviation_number
                                                        
                                                        	integer value for New Deviation Number 0x88
                                                        	**type**\:  int
                                                        
                                                        	**range:** \-2147483648..2147483647
                                                        
                                                        .. attribute:: physical_layer_interface_module_type
                                                        
                                                        	integer value for plim type if     applicable to this entity
                                                        	**type**\:  int
                                                        
                                                        	**range:** \-2147483648..2147483647
                                                        
                                                        .. attribute:: redundancystate
                                                        
                                                        	integer value for Redundancy State if     applicable to this entity
                                                        	**type**\:  int
                                                        
                                                        	**range:** \-2147483648..2147483647
                                                        
                                                        .. attribute:: serial_number
                                                        
                                                        	serial number
                                                        	**type**\:  str
                                                        
                                                        	**length:** 0..255
                                                        
                                                        .. attribute:: software_revision
                                                        
                                                        	software revision string
                                                        	**type**\:  str
                                                        
                                                        	**length:** 0..255
                                                        
                                                        .. attribute:: unique_id
                                                        
                                                        	Unique id for an entity
                                                        	**type**\:  int
                                                        
                                                        	**range:** \-2147483648..2147483647
                                                        
                                                        .. attribute:: unrecognized_fru
                                                        
                                                        	1 if UnrecognizedFRU and 0 for recognizedFRU
                                                        	**type**\:  bool
                                                        
                                                        .. attribute:: vendor_type
                                                        
                                                        	maps to the vendor OID string
                                                        	**type**\:  str
                                                        
                                                        	**length:** 0..255
                                                        
                                                        .. attribute:: xr_scoped
                                                        
                                                        	1 if xr scoped, 0 if not
                                                        	**type**\:  bool
                                                        
                                                        

                                                        """

                                                        _prefix = 'asr9k-sc-invmgr-admin-oper'
                                                        _revision = '2017-01-04'

                                                        def __init__(self):
                                                            self.parent = None
                                                            self.alias = None
                                                            self.asset_id_str = None
                                                            self.asset_identification = None
                                                            self.ceport = None
                                                            self.chip_hardware_revision = None
                                                            self.composite_class_code = None
                                                            self.description = None
                                                            self.environmental_monitor_path = None
                                                            self.firmware_revision = None
                                                            self.group_flag = None
                                                            self.hardware_revision = None
                                                            self.is_field_replaceable_unit = None
                                                            self.manufacturer_asset_tags = None
                                                            self.manufacturer_name = None
                                                            self.memory_size = None
                                                            self.model_name = None
                                                            self.name = None
                                                            self.new_deviation_number = None
                                                            self.physical_layer_interface_module_type = None
                                                            self.redundancystate = None
                                                            self.serial_number = None
                                                            self.software_revision = None
                                                            self.unique_id = None
                                                            self.unrecognized_fru = None
                                                            self.vendor_type = None
                                                            self.xr_scoped = None

                                                        @property
                                                        def _common_path(self):
                                                            if self.parent is None:
                                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                                            return self.parent._common_path +'/Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:basic-info'

                                                        def is_config(self):
                                                            ''' Returns True if this instance represents config data else returns False '''
                                                            return False

                                                        def _has_data(self):
                                                            if self.alias is not None:
                                                                return True

                                                            if self.asset_id_str is not None:
                                                                return True

                                                            if self.asset_identification is not None:
                                                                return True

                                                            if self.ceport is not None:
                                                                return True

                                                            if self.chip_hardware_revision is not None:
                                                                return True

                                                            if self.composite_class_code is not None:
                                                                return True

                                                            if self.description is not None:
                                                                return True

                                                            if self.environmental_monitor_path is not None:
                                                                return True

                                                            if self.firmware_revision is not None:
                                                                return True

                                                            if self.group_flag is not None:
                                                                return True

                                                            if self.hardware_revision is not None:
                                                                return True

                                                            if self.is_field_replaceable_unit is not None:
                                                                return True

                                                            if self.manufacturer_asset_tags is not None:
                                                                return True

                                                            if self.manufacturer_name is not None:
                                                                return True

                                                            if self.memory_size is not None:
                                                                return True

                                                            if self.model_name is not None:
                                                                return True

                                                            if self.name is not None:
                                                                return True

                                                            if self.new_deviation_number is not None:
                                                                return True

                                                            if self.physical_layer_interface_module_type is not None:
                                                                return True

                                                            if self.redundancystate is not None:
                                                                return True

                                                            if self.serial_number is not None:
                                                                return True

                                                            if self.software_revision is not None:
                                                                return True

                                                            if self.unique_id is not None:
                                                                return True

                                                            if self.unrecognized_fru is not None:
                                                                return True

                                                            if self.vendor_type is not None:
                                                                return True

                                                            if self.xr_scoped is not None:
                                                                return True

                                                            return False

                                                        @staticmethod
                                                        def _meta_info():
                                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper as meta
                                                            return meta._meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.BasicAttributes.BasicInfo']['meta_info']

                                                    @property
                                                    def _common_path(self):
                                                        if self.parent is None:
                                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                                        return self.parent._common_path +'/Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:basic-attributes'

                                                    def is_config(self):
                                                        ''' Returns True if this instance represents config data else returns False '''
                                                        return False

                                                    def _has_data(self):
                                                        if self.basic_info is not None and self.basic_info._has_data():
                                                            return True

                                                        if self.fru_info is not None and self.fru_info._has_data():
                                                            return True

                                                        return False

                                                    @staticmethod
                                                    def _meta_info():
                                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper as meta
                                                        return meta._meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.BasicAttributes']['meta_info']

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                                    if self.number is None:
                                                        raise YPYModelError('Key property number is None')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:sensor[Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:number = ' + str(self.number) + ']'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if self.number is not None:
                                                        return True

                                                    if self.basic_attributes is not None and self.basic_attributes._has_data():
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper as meta
                                                    return meta._meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor']['meta_info']

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:sensors'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.sensor is not None:
                                                    for child_ref in self.sensor:
                                                        if child_ref._has_data():
                                                            return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper as meta
                                                return meta._meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors']['meta_info']


                                        class BasicAttributes(object):
                                            """
                                            Attributes
                                            
                                            .. attribute:: basic_info
                                            
                                            	Inventory information
                                            	**type**\:   :py:class:`BasicInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.BasicAttributes.BasicInfo>`
                                            
                                            .. attribute:: fru_info
                                            
                                            	Field Replaceable Unit (FRU) inventory information
                                            	**type**\:   :py:class:`FruInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.BasicAttributes.FruInfo>`
                                            
                                            

                                            """

                                            _prefix = 'asr9k-sc-invmgr-admin-oper'
                                            _revision = '2017-01-04'

                                            def __init__(self):
                                                self.parent = None
                                                self.basic_info = Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.BasicAttributes.BasicInfo()
                                                self.basic_info.parent = self
                                                self.fru_info = Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.BasicAttributes.FruInfo()
                                                self.fru_info.parent = self


                                            class FruInfo(object):
                                                """
                                                Field Replaceable Unit (FRU) inventory
                                                information
                                                
                                                .. attribute:: card_administrative_state
                                                
                                                	card admin state\: shutdown or not
                                                	**type**\:  int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                .. attribute:: card_monitor_state
                                                
                                                	card is monitored by a manager or left unmonitored
                                                	**type**\:  int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                .. attribute:: card_operational_state
                                                
                                                	card operation state
                                                	**type**\:  int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                .. attribute:: card_reset_reason
                                                
                                                	card reset reason enum
                                                	**type**\:   :py:class:`CardResetReasonEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.CardResetReasonEnum>`
                                                
                                                .. attribute:: card_up_time
                                                
                                                	card up time
                                                	**type**\:   :py:class:`CardUpTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.BasicAttributes.FruInfo.CardUpTime>`
                                                
                                                .. attribute:: last_operational_state_change
                                                
                                                	last card oper change state
                                                	**type**\:   :py:class:`LastOperationalStateChange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.BasicAttributes.FruInfo.LastOperationalStateChange>`
                                                
                                                .. attribute:: power_administrative_state
                                                
                                                	power admin state\: up or down
                                                	**type**\:  int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                .. attribute:: power_current_measurement
                                                
                                                	power current\: not implemented
                                                	**type**\:  int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                .. attribute:: power_operational_state
                                                
                                                	Power operation state
                                                	**type**\:  int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                

                                                """

                                                _prefix = 'asr9k-sc-invmgr-admin-oper'
                                                _revision = '2017-01-04'

                                                def __init__(self):
                                                    self.parent = None
                                                    self.card_administrative_state = None
                                                    self.card_monitor_state = None
                                                    self.card_operational_state = None
                                                    self.card_reset_reason = None
                                                    self.card_up_time = Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.BasicAttributes.FruInfo.CardUpTime()
                                                    self.card_up_time.parent = self
                                                    self.last_operational_state_change = Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.BasicAttributes.FruInfo.LastOperationalStateChange()
                                                    self.last_operational_state_change.parent = self
                                                    self.power_administrative_state = None
                                                    self.power_current_measurement = None
                                                    self.power_operational_state = None


                                                class LastOperationalStateChange(object):
                                                    """
                                                    last card oper change state
                                                    
                                                    .. attribute:: time_in_nano_seconds
                                                    
                                                    	Time Value in Nano\-seconds
                                                    	**type**\:  int
                                                    
                                                    	**range:** \-2147483648..2147483647
                                                    
                                                    	**units**\: nanosecond
                                                    
                                                    .. attribute:: time_in_seconds
                                                    
                                                    	Time Value in Seconds
                                                    	**type**\:  int
                                                    
                                                    	**range:** \-2147483648..2147483647
                                                    
                                                    	**units**\: second
                                                    
                                                    

                                                    """

                                                    _prefix = 'asr9k-sc-invmgr-admin-oper'
                                                    _revision = '2017-01-04'

                                                    def __init__(self):
                                                        self.parent = None
                                                        self.time_in_nano_seconds = None
                                                        self.time_in_seconds = None

                                                    @property
                                                    def _common_path(self):
                                                        if self.parent is None:
                                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                                        return self.parent._common_path +'/Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:last-operational-state-change'

                                                    def is_config(self):
                                                        ''' Returns True if this instance represents config data else returns False '''
                                                        return False

                                                    def _has_data(self):
                                                        if self.time_in_nano_seconds is not None:
                                                            return True

                                                        if self.time_in_seconds is not None:
                                                            return True

                                                        return False

                                                    @staticmethod
                                                    def _meta_info():
                                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper as meta
                                                        return meta._meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.BasicAttributes.FruInfo.LastOperationalStateChange']['meta_info']


                                                class CardUpTime(object):
                                                    """
                                                    card up time
                                                    
                                                    .. attribute:: time_in_nano_seconds
                                                    
                                                    	Time Value in Nano\-seconds
                                                    	**type**\:  int
                                                    
                                                    	**range:** \-2147483648..2147483647
                                                    
                                                    	**units**\: nanosecond
                                                    
                                                    .. attribute:: time_in_seconds
                                                    
                                                    	Time Value in Seconds
                                                    	**type**\:  int
                                                    
                                                    	**range:** \-2147483648..2147483647
                                                    
                                                    	**units**\: second
                                                    
                                                    

                                                    """

                                                    _prefix = 'asr9k-sc-invmgr-admin-oper'
                                                    _revision = '2017-01-04'

                                                    def __init__(self):
                                                        self.parent = None
                                                        self.time_in_nano_seconds = None
                                                        self.time_in_seconds = None

                                                    @property
                                                    def _common_path(self):
                                                        if self.parent is None:
                                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                                        return self.parent._common_path +'/Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:card-up-time'

                                                    def is_config(self):
                                                        ''' Returns True if this instance represents config data else returns False '''
                                                        return False

                                                    def _has_data(self):
                                                        if self.time_in_nano_seconds is not None:
                                                            return True

                                                        if self.time_in_seconds is not None:
                                                            return True

                                                        return False

                                                    @staticmethod
                                                    def _meta_info():
                                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper as meta
                                                        return meta._meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.BasicAttributes.FruInfo.CardUpTime']['meta_info']

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:fru-info'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if self.card_administrative_state is not None:
                                                        return True

                                                    if self.card_monitor_state is not None:
                                                        return True

                                                    if self.card_operational_state is not None:
                                                        return True

                                                    if self.card_reset_reason is not None:
                                                        return True

                                                    if self.card_up_time is not None and self.card_up_time._has_data():
                                                        return True

                                                    if self.last_operational_state_change is not None and self.last_operational_state_change._has_data():
                                                        return True

                                                    if self.power_administrative_state is not None:
                                                        return True

                                                    if self.power_current_measurement is not None:
                                                        return True

                                                    if self.power_operational_state is not None:
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper as meta
                                                    return meta._meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.BasicAttributes.FruInfo']['meta_info']


                                            class BasicInfo(object):
                                                """
                                                Inventory information
                                                
                                                .. attribute:: alias
                                                
                                                	useful for storing an entity alias 
                                                	**type**\:  str
                                                
                                                	**length:** 0..255
                                                
                                                .. attribute:: asset_id_str
                                                
                                                	asset Identification string
                                                	**type**\:  str
                                                
                                                	**length:** 0..255
                                                
                                                .. attribute:: asset_identification
                                                
                                                	asset Identification
                                                	**type**\:  int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                .. attribute:: ceport
                                                
                                                	1 if ce port found, 0 if not
                                                	**type**\:  bool
                                                
                                                .. attribute:: chip_hardware_revision
                                                
                                                	chip module hw revision string
                                                	**type**\:  str
                                                
                                                	**length:** 0..255
                                                
                                                .. attribute:: composite_class_code
                                                
                                                	Major&minor class of the entity
                                                	**type**\:  int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                .. attribute:: description
                                                
                                                	describes in user\-readable terms       what the entity in question does
                                                	**type**\:  str
                                                
                                                	**length:** 0..255
                                                
                                                .. attribute:: environmental_monitor_path
                                                
                                                	sysdb name of sensor in the envmon EDM
                                                	**type**\:  str
                                                
                                                	**length:** 0..255
                                                
                                                .. attribute:: firmware_revision
                                                
                                                	firmware revision string
                                                	**type**\:  str
                                                
                                                	**length:** 0..255
                                                
                                                .. attribute:: group_flag
                                                
                                                	indicates if this entity is group       or not
                                                	**type**\:  bool
                                                
                                                .. attribute:: hardware_revision
                                                
                                                	hw revision string
                                                	**type**\:  str
                                                
                                                	**length:** 0..255
                                                
                                                .. attribute:: is_field_replaceable_unit
                                                
                                                	1 if Field Replaceable Unit 0, if not
                                                	**type**\:  bool
                                                
                                                .. attribute:: manufacturer_asset_tags
                                                
                                                	Manufacture Asset Tags
                                                	**type**\:  int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                .. attribute:: manufacturer_name
                                                
                                                	manufacturer's name
                                                	**type**\:  str
                                                
                                                	**length:** 0..255
                                                
                                                .. attribute:: memory_size
                                                
                                                	Size of memory associated with       the entity where applicable
                                                	**type**\:  int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                .. attribute:: model_name
                                                
                                                	model name
                                                	**type**\:  str
                                                
                                                	**length:** 0..255
                                                
                                                .. attribute:: name
                                                
                                                	name string for the entity
                                                	**type**\:  str
                                                
                                                	**length:** 0..255
                                                
                                                .. attribute:: new_deviation_number
                                                
                                                	integer value for New Deviation Number 0x88
                                                	**type**\:  int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                .. attribute:: physical_layer_interface_module_type
                                                
                                                	integer value for plim type if     applicable to this entity
                                                	**type**\:  int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                .. attribute:: redundancystate
                                                
                                                	integer value for Redundancy State if     applicable to this entity
                                                	**type**\:  int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                .. attribute:: serial_number
                                                
                                                	serial number
                                                	**type**\:  str
                                                
                                                	**length:** 0..255
                                                
                                                .. attribute:: software_revision
                                                
                                                	software revision string
                                                	**type**\:  str
                                                
                                                	**length:** 0..255
                                                
                                                .. attribute:: unique_id
                                                
                                                	Unique id for an entity
                                                	**type**\:  int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                .. attribute:: unrecognized_fru
                                                
                                                	1 if UnrecognizedFRU and 0 for recognizedFRU
                                                	**type**\:  bool
                                                
                                                .. attribute:: vendor_type
                                                
                                                	maps to the vendor OID string
                                                	**type**\:  str
                                                
                                                	**length:** 0..255
                                                
                                                .. attribute:: xr_scoped
                                                
                                                	1 if xr scoped, 0 if not
                                                	**type**\:  bool
                                                
                                                

                                                """

                                                _prefix = 'asr9k-sc-invmgr-admin-oper'
                                                _revision = '2017-01-04'

                                                def __init__(self):
                                                    self.parent = None
                                                    self.alias = None
                                                    self.asset_id_str = None
                                                    self.asset_identification = None
                                                    self.ceport = None
                                                    self.chip_hardware_revision = None
                                                    self.composite_class_code = None
                                                    self.description = None
                                                    self.environmental_monitor_path = None
                                                    self.firmware_revision = None
                                                    self.group_flag = None
                                                    self.hardware_revision = None
                                                    self.is_field_replaceable_unit = None
                                                    self.manufacturer_asset_tags = None
                                                    self.manufacturer_name = None
                                                    self.memory_size = None
                                                    self.model_name = None
                                                    self.name = None
                                                    self.new_deviation_number = None
                                                    self.physical_layer_interface_module_type = None
                                                    self.redundancystate = None
                                                    self.serial_number = None
                                                    self.software_revision = None
                                                    self.unique_id = None
                                                    self.unrecognized_fru = None
                                                    self.vendor_type = None
                                                    self.xr_scoped = None

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:basic-info'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if self.alias is not None:
                                                        return True

                                                    if self.asset_id_str is not None:
                                                        return True

                                                    if self.asset_identification is not None:
                                                        return True

                                                    if self.ceport is not None:
                                                        return True

                                                    if self.chip_hardware_revision is not None:
                                                        return True

                                                    if self.composite_class_code is not None:
                                                        return True

                                                    if self.description is not None:
                                                        return True

                                                    if self.environmental_monitor_path is not None:
                                                        return True

                                                    if self.firmware_revision is not None:
                                                        return True

                                                    if self.group_flag is not None:
                                                        return True

                                                    if self.hardware_revision is not None:
                                                        return True

                                                    if self.is_field_replaceable_unit is not None:
                                                        return True

                                                    if self.manufacturer_asset_tags is not None:
                                                        return True

                                                    if self.manufacturer_name is not None:
                                                        return True

                                                    if self.memory_size is not None:
                                                        return True

                                                    if self.model_name is not None:
                                                        return True

                                                    if self.name is not None:
                                                        return True

                                                    if self.new_deviation_number is not None:
                                                        return True

                                                    if self.physical_layer_interface_module_type is not None:
                                                        return True

                                                    if self.redundancystate is not None:
                                                        return True

                                                    if self.serial_number is not None:
                                                        return True

                                                    if self.software_revision is not None:
                                                        return True

                                                    if self.unique_id is not None:
                                                        return True

                                                    if self.unrecognized_fru is not None:
                                                        return True

                                                    if self.vendor_type is not None:
                                                        return True

                                                    if self.xr_scoped is not None:
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper as meta
                                                    return meta._meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.BasicAttributes.BasicInfo']['meta_info']

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:basic-attributes'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.basic_info is not None and self.basic_info._has_data():
                                                    return True

                                                if self.fru_info is not None and self.fru_info._has_data():
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper as meta
                                                return meta._meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.BasicAttributes']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:module'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.basic_attributes is not None and self.basic_attributes._has_data():
                                                return True

                                            if self.port_slots is not None and self.port_slots._has_data():
                                                return True

                                            if self.sensors is not None and self.sensors._has_data():
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper as meta
                                            return meta._meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module']['meta_info']


                                    class BasicAttributes(object):
                                        """
                                        Attributes
                                        
                                        .. attribute:: basic_info
                                        
                                        	Inventory information
                                        	**type**\:   :py:class:`BasicInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.BasicAttributes.BasicInfo>`
                                        
                                        .. attribute:: fru_info
                                        
                                        	Field Replaceable Unit (FRU) inventory information
                                        	**type**\:   :py:class:`FruInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.BasicAttributes.FruInfo>`
                                        
                                        

                                        """

                                        _prefix = 'asr9k-sc-invmgr-admin-oper'
                                        _revision = '2017-01-04'

                                        def __init__(self):
                                            self.parent = None
                                            self.basic_info = Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.BasicAttributes.BasicInfo()
                                            self.basic_info.parent = self
                                            self.fru_info = Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.BasicAttributes.FruInfo()
                                            self.fru_info.parent = self


                                        class FruInfo(object):
                                            """
                                            Field Replaceable Unit (FRU) inventory
                                            information
                                            
                                            .. attribute:: card_administrative_state
                                            
                                            	card admin state\: shutdown or not
                                            	**type**\:  int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: card_monitor_state
                                            
                                            	card is monitored by a manager or left unmonitored
                                            	**type**\:  int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: card_operational_state
                                            
                                            	card operation state
                                            	**type**\:  int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: card_reset_reason
                                            
                                            	card reset reason enum
                                            	**type**\:   :py:class:`CardResetReasonEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.CardResetReasonEnum>`
                                            
                                            .. attribute:: card_up_time
                                            
                                            	card up time
                                            	**type**\:   :py:class:`CardUpTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.BasicAttributes.FruInfo.CardUpTime>`
                                            
                                            .. attribute:: last_operational_state_change
                                            
                                            	last card oper change state
                                            	**type**\:   :py:class:`LastOperationalStateChange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.BasicAttributes.FruInfo.LastOperationalStateChange>`
                                            
                                            .. attribute:: power_administrative_state
                                            
                                            	power admin state\: up or down
                                            	**type**\:  int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: power_current_measurement
                                            
                                            	power current\: not implemented
                                            	**type**\:  int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: power_operational_state
                                            
                                            	Power operation state
                                            	**type**\:  int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            

                                            """

                                            _prefix = 'asr9k-sc-invmgr-admin-oper'
                                            _revision = '2017-01-04'

                                            def __init__(self):
                                                self.parent = None
                                                self.card_administrative_state = None
                                                self.card_monitor_state = None
                                                self.card_operational_state = None
                                                self.card_reset_reason = None
                                                self.card_up_time = Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.BasicAttributes.FruInfo.CardUpTime()
                                                self.card_up_time.parent = self
                                                self.last_operational_state_change = Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.BasicAttributes.FruInfo.LastOperationalStateChange()
                                                self.last_operational_state_change.parent = self
                                                self.power_administrative_state = None
                                                self.power_current_measurement = None
                                                self.power_operational_state = None


                                            class LastOperationalStateChange(object):
                                                """
                                                last card oper change state
                                                
                                                .. attribute:: time_in_nano_seconds
                                                
                                                	Time Value in Nano\-seconds
                                                	**type**\:  int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                	**units**\: nanosecond
                                                
                                                .. attribute:: time_in_seconds
                                                
                                                	Time Value in Seconds
                                                	**type**\:  int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                	**units**\: second
                                                
                                                

                                                """

                                                _prefix = 'asr9k-sc-invmgr-admin-oper'
                                                _revision = '2017-01-04'

                                                def __init__(self):
                                                    self.parent = None
                                                    self.time_in_nano_seconds = None
                                                    self.time_in_seconds = None

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:last-operational-state-change'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if self.time_in_nano_seconds is not None:
                                                        return True

                                                    if self.time_in_seconds is not None:
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper as meta
                                                    return meta._meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.BasicAttributes.FruInfo.LastOperationalStateChange']['meta_info']


                                            class CardUpTime(object):
                                                """
                                                card up time
                                                
                                                .. attribute:: time_in_nano_seconds
                                                
                                                	Time Value in Nano\-seconds
                                                	**type**\:  int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                	**units**\: nanosecond
                                                
                                                .. attribute:: time_in_seconds
                                                
                                                	Time Value in Seconds
                                                	**type**\:  int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                	**units**\: second
                                                
                                                

                                                """

                                                _prefix = 'asr9k-sc-invmgr-admin-oper'
                                                _revision = '2017-01-04'

                                                def __init__(self):
                                                    self.parent = None
                                                    self.time_in_nano_seconds = None
                                                    self.time_in_seconds = None

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:card-up-time'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if self.time_in_nano_seconds is not None:
                                                        return True

                                                    if self.time_in_seconds is not None:
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper as meta
                                                    return meta._meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.BasicAttributes.FruInfo.CardUpTime']['meta_info']

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:fru-info'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.card_administrative_state is not None:
                                                    return True

                                                if self.card_monitor_state is not None:
                                                    return True

                                                if self.card_operational_state is not None:
                                                    return True

                                                if self.card_reset_reason is not None:
                                                    return True

                                                if self.card_up_time is not None and self.card_up_time._has_data():
                                                    return True

                                                if self.last_operational_state_change is not None and self.last_operational_state_change._has_data():
                                                    return True

                                                if self.power_administrative_state is not None:
                                                    return True

                                                if self.power_current_measurement is not None:
                                                    return True

                                                if self.power_operational_state is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper as meta
                                                return meta._meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.BasicAttributes.FruInfo']['meta_info']


                                        class BasicInfo(object):
                                            """
                                            Inventory information
                                            
                                            .. attribute:: alias
                                            
                                            	useful for storing an entity alias 
                                            	**type**\:  str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: asset_id_str
                                            
                                            	asset Identification string
                                            	**type**\:  str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: asset_identification
                                            
                                            	asset Identification
                                            	**type**\:  int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: ceport
                                            
                                            	1 if ce port found, 0 if not
                                            	**type**\:  bool
                                            
                                            .. attribute:: chip_hardware_revision
                                            
                                            	chip module hw revision string
                                            	**type**\:  str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: composite_class_code
                                            
                                            	Major&minor class of the entity
                                            	**type**\:  int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: description
                                            
                                            	describes in user\-readable terms       what the entity in question does
                                            	**type**\:  str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: environmental_monitor_path
                                            
                                            	sysdb name of sensor in the envmon EDM
                                            	**type**\:  str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: firmware_revision
                                            
                                            	firmware revision string
                                            	**type**\:  str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: group_flag
                                            
                                            	indicates if this entity is group       or not
                                            	**type**\:  bool
                                            
                                            .. attribute:: hardware_revision
                                            
                                            	hw revision string
                                            	**type**\:  str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: is_field_replaceable_unit
                                            
                                            	1 if Field Replaceable Unit 0, if not
                                            	**type**\:  bool
                                            
                                            .. attribute:: manufacturer_asset_tags
                                            
                                            	Manufacture Asset Tags
                                            	**type**\:  int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: manufacturer_name
                                            
                                            	manufacturer's name
                                            	**type**\:  str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: memory_size
                                            
                                            	Size of memory associated with       the entity where applicable
                                            	**type**\:  int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: model_name
                                            
                                            	model name
                                            	**type**\:  str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: name
                                            
                                            	name string for the entity
                                            	**type**\:  str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: new_deviation_number
                                            
                                            	integer value for New Deviation Number 0x88
                                            	**type**\:  int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: physical_layer_interface_module_type
                                            
                                            	integer value for plim type if     applicable to this entity
                                            	**type**\:  int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: redundancystate
                                            
                                            	integer value for Redundancy State if     applicable to this entity
                                            	**type**\:  int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: serial_number
                                            
                                            	serial number
                                            	**type**\:  str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: software_revision
                                            
                                            	software revision string
                                            	**type**\:  str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: unique_id
                                            
                                            	Unique id for an entity
                                            	**type**\:  int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: unrecognized_fru
                                            
                                            	1 if UnrecognizedFRU and 0 for recognizedFRU
                                            	**type**\:  bool
                                            
                                            .. attribute:: vendor_type
                                            
                                            	maps to the vendor OID string
                                            	**type**\:  str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: xr_scoped
                                            
                                            	1 if xr scoped, 0 if not
                                            	**type**\:  bool
                                            
                                            

                                            """

                                            _prefix = 'asr9k-sc-invmgr-admin-oper'
                                            _revision = '2017-01-04'

                                            def __init__(self):
                                                self.parent = None
                                                self.alias = None
                                                self.asset_id_str = None
                                                self.asset_identification = None
                                                self.ceport = None
                                                self.chip_hardware_revision = None
                                                self.composite_class_code = None
                                                self.description = None
                                                self.environmental_monitor_path = None
                                                self.firmware_revision = None
                                                self.group_flag = None
                                                self.hardware_revision = None
                                                self.is_field_replaceable_unit = None
                                                self.manufacturer_asset_tags = None
                                                self.manufacturer_name = None
                                                self.memory_size = None
                                                self.model_name = None
                                                self.name = None
                                                self.new_deviation_number = None
                                                self.physical_layer_interface_module_type = None
                                                self.redundancystate = None
                                                self.serial_number = None
                                                self.software_revision = None
                                                self.unique_id = None
                                                self.unrecognized_fru = None
                                                self.vendor_type = None
                                                self.xr_scoped = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:basic-info'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.alias is not None:
                                                    return True

                                                if self.asset_id_str is not None:
                                                    return True

                                                if self.asset_identification is not None:
                                                    return True

                                                if self.ceport is not None:
                                                    return True

                                                if self.chip_hardware_revision is not None:
                                                    return True

                                                if self.composite_class_code is not None:
                                                    return True

                                                if self.description is not None:
                                                    return True

                                                if self.environmental_monitor_path is not None:
                                                    return True

                                                if self.firmware_revision is not None:
                                                    return True

                                                if self.group_flag is not None:
                                                    return True

                                                if self.hardware_revision is not None:
                                                    return True

                                                if self.is_field_replaceable_unit is not None:
                                                    return True

                                                if self.manufacturer_asset_tags is not None:
                                                    return True

                                                if self.manufacturer_name is not None:
                                                    return True

                                                if self.memory_size is not None:
                                                    return True

                                                if self.model_name is not None:
                                                    return True

                                                if self.name is not None:
                                                    return True

                                                if self.new_deviation_number is not None:
                                                    return True

                                                if self.physical_layer_interface_module_type is not None:
                                                    return True

                                                if self.redundancystate is not None:
                                                    return True

                                                if self.serial_number is not None:
                                                    return True

                                                if self.software_revision is not None:
                                                    return True

                                                if self.unique_id is not None:
                                                    return True

                                                if self.unrecognized_fru is not None:
                                                    return True

                                                if self.vendor_type is not None:
                                                    return True

                                                if self.xr_scoped is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper as meta
                                                return meta._meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.BasicAttributes.BasicInfo']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:basic-attributes'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.basic_info is not None and self.basic_info._has_data():
                                                return True

                                            if self.fru_info is not None and self.fru_info._has_data():
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper as meta
                                            return meta._meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.BasicAttributes']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')
                                        if self.number is None:
                                            raise YPYModelError('Key property number is None')

                                        return self.parent._common_path +'/Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:sub-slot[Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:number = ' + str(self.number) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.number is not None:
                                            return True

                                        if self.basic_attributes is not None and self.basic_attributes._has_data():
                                            return True

                                        if self.module is not None and self.module._has_data():
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper as meta
                                        return meta._meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:sub-slots'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.sub_slot is not None:
                                        for child_ref in self.sub_slot:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper as meta
                                    return meta._meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots']['meta_info']


                            class HwComponents(object):
                                """
                                HWComponent table contains all HW modules
                                within the card 
                                
                                .. attribute:: hw_component
                                
                                	HWComponent number
                                	**type**\: list of    :py:class:`HwComponent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent>`
                                
                                

                                """

                                _prefix = 'asr9k-sc-invmgr-admin-oper'
                                _revision = '2017-01-04'

                                def __init__(self):
                                    self.parent = None
                                    self.hw_component = YList()
                                    self.hw_component.parent = self
                                    self.hw_component.name = 'hw_component'


                                class HwComponent(object):
                                    """
                                    HWComponent number
                                    
                                    .. attribute:: number  <key>
                                    
                                    	node number
                                    	**type**\:  int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: basic_attributes
                                    
                                    	Attributes
                                    	**type**\:   :py:class:`BasicAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.BasicAttributes>`
                                    
                                    .. attribute:: sensors
                                    
                                    	ModuleSensorTable contains all sensors in a Module
                                    	**type**\:   :py:class:`Sensors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors>`
                                    
                                    

                                    """

                                    _prefix = 'asr9k-sc-invmgr-admin-oper'
                                    _revision = '2017-01-04'

                                    def __init__(self):
                                        self.parent = None
                                        self.number = None
                                        self.basic_attributes = Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.BasicAttributes()
                                        self.basic_attributes.parent = self
                                        self.sensors = Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors()
                                        self.sensors.parent = self


                                    class Sensors(object):
                                        """
                                        ModuleSensorTable contains all sensors in a
                                        Module.
                                        
                                        .. attribute:: sensor
                                        
                                        	Sensor number in the Module
                                        	**type**\: list of    :py:class:`Sensor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor>`
                                        
                                        

                                        """

                                        _prefix = 'asr9k-sc-invmgr-admin-oper'
                                        _revision = '2017-01-04'

                                        def __init__(self):
                                            self.parent = None
                                            self.sensor = YList()
                                            self.sensor.parent = self
                                            self.sensor.name = 'sensor'


                                        class Sensor(object):
                                            """
                                            Sensor number in the Module
                                            
                                            .. attribute:: number  <key>
                                            
                                            	sensor number
                                            	**type**\:  int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: basic_attributes
                                            
                                            	Attributes
                                            	**type**\:   :py:class:`BasicAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.BasicAttributes>`
                                            
                                            

                                            """

                                            _prefix = 'asr9k-sc-invmgr-admin-oper'
                                            _revision = '2017-01-04'

                                            def __init__(self):
                                                self.parent = None
                                                self.number = None
                                                self.basic_attributes = Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.BasicAttributes()
                                                self.basic_attributes.parent = self


                                            class BasicAttributes(object):
                                                """
                                                Attributes
                                                
                                                .. attribute:: basic_info
                                                
                                                	Inventory information
                                                	**type**\:   :py:class:`BasicInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.BasicAttributes.BasicInfo>`
                                                
                                                .. attribute:: fru_info
                                                
                                                	Field Replaceable Unit (FRU) inventory information
                                                	**type**\:   :py:class:`FruInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.BasicAttributes.FruInfo>`
                                                
                                                

                                                """

                                                _prefix = 'asr9k-sc-invmgr-admin-oper'
                                                _revision = '2017-01-04'

                                                def __init__(self):
                                                    self.parent = None
                                                    self.basic_info = Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.BasicAttributes.BasicInfo()
                                                    self.basic_info.parent = self
                                                    self.fru_info = Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.BasicAttributes.FruInfo()
                                                    self.fru_info.parent = self


                                                class FruInfo(object):
                                                    """
                                                    Field Replaceable Unit (FRU) inventory
                                                    information
                                                    
                                                    .. attribute:: card_administrative_state
                                                    
                                                    	card admin state\: shutdown or not
                                                    	**type**\:  int
                                                    
                                                    	**range:** \-2147483648..2147483647
                                                    
                                                    .. attribute:: card_monitor_state
                                                    
                                                    	card is monitored by a manager or left unmonitored
                                                    	**type**\:  int
                                                    
                                                    	**range:** \-2147483648..2147483647
                                                    
                                                    .. attribute:: card_operational_state
                                                    
                                                    	card operation state
                                                    	**type**\:  int
                                                    
                                                    	**range:** \-2147483648..2147483647
                                                    
                                                    .. attribute:: card_reset_reason
                                                    
                                                    	card reset reason enum
                                                    	**type**\:   :py:class:`CardResetReasonEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.CardResetReasonEnum>`
                                                    
                                                    .. attribute:: card_up_time
                                                    
                                                    	card up time
                                                    	**type**\:   :py:class:`CardUpTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.BasicAttributes.FruInfo.CardUpTime>`
                                                    
                                                    .. attribute:: last_operational_state_change
                                                    
                                                    	last card oper change state
                                                    	**type**\:   :py:class:`LastOperationalStateChange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.BasicAttributes.FruInfo.LastOperationalStateChange>`
                                                    
                                                    .. attribute:: power_administrative_state
                                                    
                                                    	power admin state\: up or down
                                                    	**type**\:  int
                                                    
                                                    	**range:** \-2147483648..2147483647
                                                    
                                                    .. attribute:: power_current_measurement
                                                    
                                                    	power current\: not implemented
                                                    	**type**\:  int
                                                    
                                                    	**range:** \-2147483648..2147483647
                                                    
                                                    .. attribute:: power_operational_state
                                                    
                                                    	Power operation state
                                                    	**type**\:  int
                                                    
                                                    	**range:** \-2147483648..2147483647
                                                    
                                                    

                                                    """

                                                    _prefix = 'asr9k-sc-invmgr-admin-oper'
                                                    _revision = '2017-01-04'

                                                    def __init__(self):
                                                        self.parent = None
                                                        self.card_administrative_state = None
                                                        self.card_monitor_state = None
                                                        self.card_operational_state = None
                                                        self.card_reset_reason = None
                                                        self.card_up_time = Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.BasicAttributes.FruInfo.CardUpTime()
                                                        self.card_up_time.parent = self
                                                        self.last_operational_state_change = Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.BasicAttributes.FruInfo.LastOperationalStateChange()
                                                        self.last_operational_state_change.parent = self
                                                        self.power_administrative_state = None
                                                        self.power_current_measurement = None
                                                        self.power_operational_state = None


                                                    class LastOperationalStateChange(object):
                                                        """
                                                        last card oper change state
                                                        
                                                        .. attribute:: time_in_nano_seconds
                                                        
                                                        	Time Value in Nano\-seconds
                                                        	**type**\:  int
                                                        
                                                        	**range:** \-2147483648..2147483647
                                                        
                                                        	**units**\: nanosecond
                                                        
                                                        .. attribute:: time_in_seconds
                                                        
                                                        	Time Value in Seconds
                                                        	**type**\:  int
                                                        
                                                        	**range:** \-2147483648..2147483647
                                                        
                                                        	**units**\: second
                                                        
                                                        

                                                        """

                                                        _prefix = 'asr9k-sc-invmgr-admin-oper'
                                                        _revision = '2017-01-04'

                                                        def __init__(self):
                                                            self.parent = None
                                                            self.time_in_nano_seconds = None
                                                            self.time_in_seconds = None

                                                        @property
                                                        def _common_path(self):
                                                            if self.parent is None:
                                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                                            return self.parent._common_path +'/Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:last-operational-state-change'

                                                        def is_config(self):
                                                            ''' Returns True if this instance represents config data else returns False '''
                                                            return False

                                                        def _has_data(self):
                                                            if self.time_in_nano_seconds is not None:
                                                                return True

                                                            if self.time_in_seconds is not None:
                                                                return True

                                                            return False

                                                        @staticmethod
                                                        def _meta_info():
                                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper as meta
                                                            return meta._meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.BasicAttributes.FruInfo.LastOperationalStateChange']['meta_info']


                                                    class CardUpTime(object):
                                                        """
                                                        card up time
                                                        
                                                        .. attribute:: time_in_nano_seconds
                                                        
                                                        	Time Value in Nano\-seconds
                                                        	**type**\:  int
                                                        
                                                        	**range:** \-2147483648..2147483647
                                                        
                                                        	**units**\: nanosecond
                                                        
                                                        .. attribute:: time_in_seconds
                                                        
                                                        	Time Value in Seconds
                                                        	**type**\:  int
                                                        
                                                        	**range:** \-2147483648..2147483647
                                                        
                                                        	**units**\: second
                                                        
                                                        

                                                        """

                                                        _prefix = 'asr9k-sc-invmgr-admin-oper'
                                                        _revision = '2017-01-04'

                                                        def __init__(self):
                                                            self.parent = None
                                                            self.time_in_nano_seconds = None
                                                            self.time_in_seconds = None

                                                        @property
                                                        def _common_path(self):
                                                            if self.parent is None:
                                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                                            return self.parent._common_path +'/Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:card-up-time'

                                                        def is_config(self):
                                                            ''' Returns True if this instance represents config data else returns False '''
                                                            return False

                                                        def _has_data(self):
                                                            if self.time_in_nano_seconds is not None:
                                                                return True

                                                            if self.time_in_seconds is not None:
                                                                return True

                                                            return False

                                                        @staticmethod
                                                        def _meta_info():
                                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper as meta
                                                            return meta._meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.BasicAttributes.FruInfo.CardUpTime']['meta_info']

                                                    @property
                                                    def _common_path(self):
                                                        if self.parent is None:
                                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                                        return self.parent._common_path +'/Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:fru-info'

                                                    def is_config(self):
                                                        ''' Returns True if this instance represents config data else returns False '''
                                                        return False

                                                    def _has_data(self):
                                                        if self.card_administrative_state is not None:
                                                            return True

                                                        if self.card_monitor_state is not None:
                                                            return True

                                                        if self.card_operational_state is not None:
                                                            return True

                                                        if self.card_reset_reason is not None:
                                                            return True

                                                        if self.card_up_time is not None and self.card_up_time._has_data():
                                                            return True

                                                        if self.last_operational_state_change is not None and self.last_operational_state_change._has_data():
                                                            return True

                                                        if self.power_administrative_state is not None:
                                                            return True

                                                        if self.power_current_measurement is not None:
                                                            return True

                                                        if self.power_operational_state is not None:
                                                            return True

                                                        return False

                                                    @staticmethod
                                                    def _meta_info():
                                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper as meta
                                                        return meta._meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.BasicAttributes.FruInfo']['meta_info']


                                                class BasicInfo(object):
                                                    """
                                                    Inventory information
                                                    
                                                    .. attribute:: alias
                                                    
                                                    	useful for storing an entity alias 
                                                    	**type**\:  str
                                                    
                                                    	**length:** 0..255
                                                    
                                                    .. attribute:: asset_id_str
                                                    
                                                    	asset Identification string
                                                    	**type**\:  str
                                                    
                                                    	**length:** 0..255
                                                    
                                                    .. attribute:: asset_identification
                                                    
                                                    	asset Identification
                                                    	**type**\:  int
                                                    
                                                    	**range:** \-2147483648..2147483647
                                                    
                                                    .. attribute:: ceport
                                                    
                                                    	1 if ce port found, 0 if not
                                                    	**type**\:  bool
                                                    
                                                    .. attribute:: chip_hardware_revision
                                                    
                                                    	chip module hw revision string
                                                    	**type**\:  str
                                                    
                                                    	**length:** 0..255
                                                    
                                                    .. attribute:: composite_class_code
                                                    
                                                    	Major&minor class of the entity
                                                    	**type**\:  int
                                                    
                                                    	**range:** \-2147483648..2147483647
                                                    
                                                    .. attribute:: description
                                                    
                                                    	describes in user\-readable terms       what the entity in question does
                                                    	**type**\:  str
                                                    
                                                    	**length:** 0..255
                                                    
                                                    .. attribute:: environmental_monitor_path
                                                    
                                                    	sysdb name of sensor in the envmon EDM
                                                    	**type**\:  str
                                                    
                                                    	**length:** 0..255
                                                    
                                                    .. attribute:: firmware_revision
                                                    
                                                    	firmware revision string
                                                    	**type**\:  str
                                                    
                                                    	**length:** 0..255
                                                    
                                                    .. attribute:: group_flag
                                                    
                                                    	indicates if this entity is group       or not
                                                    	**type**\:  bool
                                                    
                                                    .. attribute:: hardware_revision
                                                    
                                                    	hw revision string
                                                    	**type**\:  str
                                                    
                                                    	**length:** 0..255
                                                    
                                                    .. attribute:: is_field_replaceable_unit
                                                    
                                                    	1 if Field Replaceable Unit 0, if not
                                                    	**type**\:  bool
                                                    
                                                    .. attribute:: manufacturer_asset_tags
                                                    
                                                    	Manufacture Asset Tags
                                                    	**type**\:  int
                                                    
                                                    	**range:** \-2147483648..2147483647
                                                    
                                                    .. attribute:: manufacturer_name
                                                    
                                                    	manufacturer's name
                                                    	**type**\:  str
                                                    
                                                    	**length:** 0..255
                                                    
                                                    .. attribute:: memory_size
                                                    
                                                    	Size of memory associated with       the entity where applicable
                                                    	**type**\:  int
                                                    
                                                    	**range:** \-2147483648..2147483647
                                                    
                                                    .. attribute:: model_name
                                                    
                                                    	model name
                                                    	**type**\:  str
                                                    
                                                    	**length:** 0..255
                                                    
                                                    .. attribute:: name
                                                    
                                                    	name string for the entity
                                                    	**type**\:  str
                                                    
                                                    	**length:** 0..255
                                                    
                                                    .. attribute:: new_deviation_number
                                                    
                                                    	integer value for New Deviation Number 0x88
                                                    	**type**\:  int
                                                    
                                                    	**range:** \-2147483648..2147483647
                                                    
                                                    .. attribute:: physical_layer_interface_module_type
                                                    
                                                    	integer value for plim type if     applicable to this entity
                                                    	**type**\:  int
                                                    
                                                    	**range:** \-2147483648..2147483647
                                                    
                                                    .. attribute:: redundancystate
                                                    
                                                    	integer value for Redundancy State if     applicable to this entity
                                                    	**type**\:  int
                                                    
                                                    	**range:** \-2147483648..2147483647
                                                    
                                                    .. attribute:: serial_number
                                                    
                                                    	serial number
                                                    	**type**\:  str
                                                    
                                                    	**length:** 0..255
                                                    
                                                    .. attribute:: software_revision
                                                    
                                                    	software revision string
                                                    	**type**\:  str
                                                    
                                                    	**length:** 0..255
                                                    
                                                    .. attribute:: unique_id
                                                    
                                                    	Unique id for an entity
                                                    	**type**\:  int
                                                    
                                                    	**range:** \-2147483648..2147483647
                                                    
                                                    .. attribute:: unrecognized_fru
                                                    
                                                    	1 if UnrecognizedFRU and 0 for recognizedFRU
                                                    	**type**\:  bool
                                                    
                                                    .. attribute:: vendor_type
                                                    
                                                    	maps to the vendor OID string
                                                    	**type**\:  str
                                                    
                                                    	**length:** 0..255
                                                    
                                                    .. attribute:: xr_scoped
                                                    
                                                    	1 if xr scoped, 0 if not
                                                    	**type**\:  bool
                                                    
                                                    

                                                    """

                                                    _prefix = 'asr9k-sc-invmgr-admin-oper'
                                                    _revision = '2017-01-04'

                                                    def __init__(self):
                                                        self.parent = None
                                                        self.alias = None
                                                        self.asset_id_str = None
                                                        self.asset_identification = None
                                                        self.ceport = None
                                                        self.chip_hardware_revision = None
                                                        self.composite_class_code = None
                                                        self.description = None
                                                        self.environmental_monitor_path = None
                                                        self.firmware_revision = None
                                                        self.group_flag = None
                                                        self.hardware_revision = None
                                                        self.is_field_replaceable_unit = None
                                                        self.manufacturer_asset_tags = None
                                                        self.manufacturer_name = None
                                                        self.memory_size = None
                                                        self.model_name = None
                                                        self.name = None
                                                        self.new_deviation_number = None
                                                        self.physical_layer_interface_module_type = None
                                                        self.redundancystate = None
                                                        self.serial_number = None
                                                        self.software_revision = None
                                                        self.unique_id = None
                                                        self.unrecognized_fru = None
                                                        self.vendor_type = None
                                                        self.xr_scoped = None

                                                    @property
                                                    def _common_path(self):
                                                        if self.parent is None:
                                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                                        return self.parent._common_path +'/Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:basic-info'

                                                    def is_config(self):
                                                        ''' Returns True if this instance represents config data else returns False '''
                                                        return False

                                                    def _has_data(self):
                                                        if self.alias is not None:
                                                            return True

                                                        if self.asset_id_str is not None:
                                                            return True

                                                        if self.asset_identification is not None:
                                                            return True

                                                        if self.ceport is not None:
                                                            return True

                                                        if self.chip_hardware_revision is not None:
                                                            return True

                                                        if self.composite_class_code is not None:
                                                            return True

                                                        if self.description is not None:
                                                            return True

                                                        if self.environmental_monitor_path is not None:
                                                            return True

                                                        if self.firmware_revision is not None:
                                                            return True

                                                        if self.group_flag is not None:
                                                            return True

                                                        if self.hardware_revision is not None:
                                                            return True

                                                        if self.is_field_replaceable_unit is not None:
                                                            return True

                                                        if self.manufacturer_asset_tags is not None:
                                                            return True

                                                        if self.manufacturer_name is not None:
                                                            return True

                                                        if self.memory_size is not None:
                                                            return True

                                                        if self.model_name is not None:
                                                            return True

                                                        if self.name is not None:
                                                            return True

                                                        if self.new_deviation_number is not None:
                                                            return True

                                                        if self.physical_layer_interface_module_type is not None:
                                                            return True

                                                        if self.redundancystate is not None:
                                                            return True

                                                        if self.serial_number is not None:
                                                            return True

                                                        if self.software_revision is not None:
                                                            return True

                                                        if self.unique_id is not None:
                                                            return True

                                                        if self.unrecognized_fru is not None:
                                                            return True

                                                        if self.vendor_type is not None:
                                                            return True

                                                        if self.xr_scoped is not None:
                                                            return True

                                                        return False

                                                    @staticmethod
                                                    def _meta_info():
                                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper as meta
                                                        return meta._meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.BasicAttributes.BasicInfo']['meta_info']

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:basic-attributes'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if self.basic_info is not None and self.basic_info._has_data():
                                                        return True

                                                    if self.fru_info is not None and self.fru_info._has_data():
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper as meta
                                                    return meta._meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.BasicAttributes']['meta_info']

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                                if self.number is None:
                                                    raise YPYModelError('Key property number is None')

                                                return self.parent._common_path +'/Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:sensor[Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:number = ' + str(self.number) + ']'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.number is not None:
                                                    return True

                                                if self.basic_attributes is not None and self.basic_attributes._has_data():
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper as meta
                                                return meta._meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:sensors'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.sensor is not None:
                                                for child_ref in self.sensor:
                                                    if child_ref._has_data():
                                                        return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper as meta
                                            return meta._meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors']['meta_info']


                                    class BasicAttributes(object):
                                        """
                                        Attributes
                                        
                                        .. attribute:: basic_info
                                        
                                        	Inventory information
                                        	**type**\:   :py:class:`BasicInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.BasicAttributes.BasicInfo>`
                                        
                                        .. attribute:: fru_info
                                        
                                        	Field Replaceable Unit (FRU) inventory information
                                        	**type**\:   :py:class:`FruInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.BasicAttributes.FruInfo>`
                                        
                                        

                                        """

                                        _prefix = 'asr9k-sc-invmgr-admin-oper'
                                        _revision = '2017-01-04'

                                        def __init__(self):
                                            self.parent = None
                                            self.basic_info = Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.BasicAttributes.BasicInfo()
                                            self.basic_info.parent = self
                                            self.fru_info = Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.BasicAttributes.FruInfo()
                                            self.fru_info.parent = self


                                        class FruInfo(object):
                                            """
                                            Field Replaceable Unit (FRU) inventory
                                            information
                                            
                                            .. attribute:: card_administrative_state
                                            
                                            	card admin state\: shutdown or not
                                            	**type**\:  int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: card_monitor_state
                                            
                                            	card is monitored by a manager or left unmonitored
                                            	**type**\:  int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: card_operational_state
                                            
                                            	card operation state
                                            	**type**\:  int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: card_reset_reason
                                            
                                            	card reset reason enum
                                            	**type**\:   :py:class:`CardResetReasonEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.CardResetReasonEnum>`
                                            
                                            .. attribute:: card_up_time
                                            
                                            	card up time
                                            	**type**\:   :py:class:`CardUpTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.BasicAttributes.FruInfo.CardUpTime>`
                                            
                                            .. attribute:: last_operational_state_change
                                            
                                            	last card oper change state
                                            	**type**\:   :py:class:`LastOperationalStateChange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.BasicAttributes.FruInfo.LastOperationalStateChange>`
                                            
                                            .. attribute:: power_administrative_state
                                            
                                            	power admin state\: up or down
                                            	**type**\:  int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: power_current_measurement
                                            
                                            	power current\: not implemented
                                            	**type**\:  int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: power_operational_state
                                            
                                            	Power operation state
                                            	**type**\:  int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            

                                            """

                                            _prefix = 'asr9k-sc-invmgr-admin-oper'
                                            _revision = '2017-01-04'

                                            def __init__(self):
                                                self.parent = None
                                                self.card_administrative_state = None
                                                self.card_monitor_state = None
                                                self.card_operational_state = None
                                                self.card_reset_reason = None
                                                self.card_up_time = Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.BasicAttributes.FruInfo.CardUpTime()
                                                self.card_up_time.parent = self
                                                self.last_operational_state_change = Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.BasicAttributes.FruInfo.LastOperationalStateChange()
                                                self.last_operational_state_change.parent = self
                                                self.power_administrative_state = None
                                                self.power_current_measurement = None
                                                self.power_operational_state = None


                                            class LastOperationalStateChange(object):
                                                """
                                                last card oper change state
                                                
                                                .. attribute:: time_in_nano_seconds
                                                
                                                	Time Value in Nano\-seconds
                                                	**type**\:  int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                	**units**\: nanosecond
                                                
                                                .. attribute:: time_in_seconds
                                                
                                                	Time Value in Seconds
                                                	**type**\:  int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                	**units**\: second
                                                
                                                

                                                """

                                                _prefix = 'asr9k-sc-invmgr-admin-oper'
                                                _revision = '2017-01-04'

                                                def __init__(self):
                                                    self.parent = None
                                                    self.time_in_nano_seconds = None
                                                    self.time_in_seconds = None

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:last-operational-state-change'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if self.time_in_nano_seconds is not None:
                                                        return True

                                                    if self.time_in_seconds is not None:
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper as meta
                                                    return meta._meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.BasicAttributes.FruInfo.LastOperationalStateChange']['meta_info']


                                            class CardUpTime(object):
                                                """
                                                card up time
                                                
                                                .. attribute:: time_in_nano_seconds
                                                
                                                	Time Value in Nano\-seconds
                                                	**type**\:  int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                	**units**\: nanosecond
                                                
                                                .. attribute:: time_in_seconds
                                                
                                                	Time Value in Seconds
                                                	**type**\:  int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                	**units**\: second
                                                
                                                

                                                """

                                                _prefix = 'asr9k-sc-invmgr-admin-oper'
                                                _revision = '2017-01-04'

                                                def __init__(self):
                                                    self.parent = None
                                                    self.time_in_nano_seconds = None
                                                    self.time_in_seconds = None

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:card-up-time'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if self.time_in_nano_seconds is not None:
                                                        return True

                                                    if self.time_in_seconds is not None:
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper as meta
                                                    return meta._meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.BasicAttributes.FruInfo.CardUpTime']['meta_info']

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:fru-info'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.card_administrative_state is not None:
                                                    return True

                                                if self.card_monitor_state is not None:
                                                    return True

                                                if self.card_operational_state is not None:
                                                    return True

                                                if self.card_reset_reason is not None:
                                                    return True

                                                if self.card_up_time is not None and self.card_up_time._has_data():
                                                    return True

                                                if self.last_operational_state_change is not None and self.last_operational_state_change._has_data():
                                                    return True

                                                if self.power_administrative_state is not None:
                                                    return True

                                                if self.power_current_measurement is not None:
                                                    return True

                                                if self.power_operational_state is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper as meta
                                                return meta._meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.BasicAttributes.FruInfo']['meta_info']


                                        class BasicInfo(object):
                                            """
                                            Inventory information
                                            
                                            .. attribute:: alias
                                            
                                            	useful for storing an entity alias 
                                            	**type**\:  str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: asset_id_str
                                            
                                            	asset Identification string
                                            	**type**\:  str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: asset_identification
                                            
                                            	asset Identification
                                            	**type**\:  int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: ceport
                                            
                                            	1 if ce port found, 0 if not
                                            	**type**\:  bool
                                            
                                            .. attribute:: chip_hardware_revision
                                            
                                            	chip module hw revision string
                                            	**type**\:  str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: composite_class_code
                                            
                                            	Major&minor class of the entity
                                            	**type**\:  int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: description
                                            
                                            	describes in user\-readable terms       what the entity in question does
                                            	**type**\:  str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: environmental_monitor_path
                                            
                                            	sysdb name of sensor in the envmon EDM
                                            	**type**\:  str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: firmware_revision
                                            
                                            	firmware revision string
                                            	**type**\:  str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: group_flag
                                            
                                            	indicates if this entity is group       or not
                                            	**type**\:  bool
                                            
                                            .. attribute:: hardware_revision
                                            
                                            	hw revision string
                                            	**type**\:  str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: is_field_replaceable_unit
                                            
                                            	1 if Field Replaceable Unit 0, if not
                                            	**type**\:  bool
                                            
                                            .. attribute:: manufacturer_asset_tags
                                            
                                            	Manufacture Asset Tags
                                            	**type**\:  int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: manufacturer_name
                                            
                                            	manufacturer's name
                                            	**type**\:  str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: memory_size
                                            
                                            	Size of memory associated with       the entity where applicable
                                            	**type**\:  int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: model_name
                                            
                                            	model name
                                            	**type**\:  str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: name
                                            
                                            	name string for the entity
                                            	**type**\:  str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: new_deviation_number
                                            
                                            	integer value for New Deviation Number 0x88
                                            	**type**\:  int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: physical_layer_interface_module_type
                                            
                                            	integer value for plim type if     applicable to this entity
                                            	**type**\:  int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: redundancystate
                                            
                                            	integer value for Redundancy State if     applicable to this entity
                                            	**type**\:  int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: serial_number
                                            
                                            	serial number
                                            	**type**\:  str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: software_revision
                                            
                                            	software revision string
                                            	**type**\:  str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: unique_id
                                            
                                            	Unique id for an entity
                                            	**type**\:  int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: unrecognized_fru
                                            
                                            	1 if UnrecognizedFRU and 0 for recognizedFRU
                                            	**type**\:  bool
                                            
                                            .. attribute:: vendor_type
                                            
                                            	maps to the vendor OID string
                                            	**type**\:  str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: xr_scoped
                                            
                                            	1 if xr scoped, 0 if not
                                            	**type**\:  bool
                                            
                                            

                                            """

                                            _prefix = 'asr9k-sc-invmgr-admin-oper'
                                            _revision = '2017-01-04'

                                            def __init__(self):
                                                self.parent = None
                                                self.alias = None
                                                self.asset_id_str = None
                                                self.asset_identification = None
                                                self.ceport = None
                                                self.chip_hardware_revision = None
                                                self.composite_class_code = None
                                                self.description = None
                                                self.environmental_monitor_path = None
                                                self.firmware_revision = None
                                                self.group_flag = None
                                                self.hardware_revision = None
                                                self.is_field_replaceable_unit = None
                                                self.manufacturer_asset_tags = None
                                                self.manufacturer_name = None
                                                self.memory_size = None
                                                self.model_name = None
                                                self.name = None
                                                self.new_deviation_number = None
                                                self.physical_layer_interface_module_type = None
                                                self.redundancystate = None
                                                self.serial_number = None
                                                self.software_revision = None
                                                self.unique_id = None
                                                self.unrecognized_fru = None
                                                self.vendor_type = None
                                                self.xr_scoped = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:basic-info'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.alias is not None:
                                                    return True

                                                if self.asset_id_str is not None:
                                                    return True

                                                if self.asset_identification is not None:
                                                    return True

                                                if self.ceport is not None:
                                                    return True

                                                if self.chip_hardware_revision is not None:
                                                    return True

                                                if self.composite_class_code is not None:
                                                    return True

                                                if self.description is not None:
                                                    return True

                                                if self.environmental_monitor_path is not None:
                                                    return True

                                                if self.firmware_revision is not None:
                                                    return True

                                                if self.group_flag is not None:
                                                    return True

                                                if self.hardware_revision is not None:
                                                    return True

                                                if self.is_field_replaceable_unit is not None:
                                                    return True

                                                if self.manufacturer_asset_tags is not None:
                                                    return True

                                                if self.manufacturer_name is not None:
                                                    return True

                                                if self.memory_size is not None:
                                                    return True

                                                if self.model_name is not None:
                                                    return True

                                                if self.name is not None:
                                                    return True

                                                if self.new_deviation_number is not None:
                                                    return True

                                                if self.physical_layer_interface_module_type is not None:
                                                    return True

                                                if self.redundancystate is not None:
                                                    return True

                                                if self.serial_number is not None:
                                                    return True

                                                if self.software_revision is not None:
                                                    return True

                                                if self.unique_id is not None:
                                                    return True

                                                if self.unrecognized_fru is not None:
                                                    return True

                                                if self.vendor_type is not None:
                                                    return True

                                                if self.xr_scoped is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper as meta
                                                return meta._meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.BasicAttributes.BasicInfo']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:basic-attributes'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.basic_info is not None and self.basic_info._has_data():
                                                return True

                                            if self.fru_info is not None and self.fru_info._has_data():
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper as meta
                                            return meta._meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.BasicAttributes']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')
                                        if self.number is None:
                                            raise YPYModelError('Key property number is None')

                                        return self.parent._common_path +'/Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:hw-component[Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:number = ' + str(self.number) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.number is not None:
                                            return True

                                        if self.basic_attributes is not None and self.basic_attributes._has_data():
                                            return True

                                        if self.sensors is not None and self.sensors._has_data():
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper as meta
                                        return meta._meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:hw-components'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.hw_component is not None:
                                        for child_ref in self.hw_component:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper as meta
                                    return meta._meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents']['meta_info']


                            class PortSlots(object):
                                """
                                PortSlotTable contains all optics ports in a
                                SPA/PLIM.
                                
                                .. attribute:: port_slot
                                
                                	PortSlot number in the SPA/PLIM
                                	**type**\: list of    :py:class:`PortSlot <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot>`
                                
                                

                                """

                                _prefix = 'asr9k-sc-invmgr-admin-oper'
                                _revision = '2017-01-04'

                                def __init__(self):
                                    self.parent = None
                                    self.port_slot = YList()
                                    self.port_slot.parent = self
                                    self.port_slot.name = 'port_slot'


                                class PortSlot(object):
                                    """
                                    PortSlot number in the SPA/PLIM
                                    
                                    .. attribute:: number  <key>
                                    
                                    	portslot number
                                    	**type**\:  int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: basic_attributes
                                    
                                    	Attributes
                                    	**type**\:   :py:class:`BasicAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.BasicAttributes>`
                                    
                                    .. attribute:: port
                                    
                                    	Port string
                                    	**type**\:   :py:class:`Port <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port>`
                                    
                                    

                                    """

                                    _prefix = 'asr9k-sc-invmgr-admin-oper'
                                    _revision = '2017-01-04'

                                    def __init__(self):
                                        self.parent = None
                                        self.number = None
                                        self.basic_attributes = Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.BasicAttributes()
                                        self.basic_attributes.parent = self
                                        self.port = Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port()
                                        self.port.parent = self


                                    class Port(object):
                                        """
                                        Port string
                                        
                                        .. attribute:: basic_attributes
                                        
                                        	Attributes
                                        	**type**\:   :py:class:`BasicAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.BasicAttributes>`
                                        
                                        

                                        """

                                        _prefix = 'asr9k-sc-invmgr-admin-oper'
                                        _revision = '2017-01-04'

                                        def __init__(self):
                                            self.parent = None
                                            self.basic_attributes = Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.BasicAttributes()
                                            self.basic_attributes.parent = self


                                        class BasicAttributes(object):
                                            """
                                            Attributes
                                            
                                            .. attribute:: basic_info
                                            
                                            	Inventory information
                                            	**type**\:   :py:class:`BasicInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.BasicAttributes.BasicInfo>`
                                            
                                            .. attribute:: fru_info
                                            
                                            	Field Replaceable Unit (FRU) inventory information
                                            	**type**\:   :py:class:`FruInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.BasicAttributes.FruInfo>`
                                            
                                            

                                            """

                                            _prefix = 'asr9k-sc-invmgr-admin-oper'
                                            _revision = '2017-01-04'

                                            def __init__(self):
                                                self.parent = None
                                                self.basic_info = Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.BasicAttributes.BasicInfo()
                                                self.basic_info.parent = self
                                                self.fru_info = Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.BasicAttributes.FruInfo()
                                                self.fru_info.parent = self


                                            class FruInfo(object):
                                                """
                                                Field Replaceable Unit (FRU) inventory
                                                information
                                                
                                                .. attribute:: card_administrative_state
                                                
                                                	card admin state\: shutdown or not
                                                	**type**\:  int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                .. attribute:: card_monitor_state
                                                
                                                	card is monitored by a manager or left unmonitored
                                                	**type**\:  int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                .. attribute:: card_operational_state
                                                
                                                	card operation state
                                                	**type**\:  int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                .. attribute:: card_reset_reason
                                                
                                                	card reset reason enum
                                                	**type**\:   :py:class:`CardResetReasonEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.CardResetReasonEnum>`
                                                
                                                .. attribute:: card_up_time
                                                
                                                	card up time
                                                	**type**\:   :py:class:`CardUpTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.BasicAttributes.FruInfo.CardUpTime>`
                                                
                                                .. attribute:: last_operational_state_change
                                                
                                                	last card oper change state
                                                	**type**\:   :py:class:`LastOperationalStateChange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.BasicAttributes.FruInfo.LastOperationalStateChange>`
                                                
                                                .. attribute:: power_administrative_state
                                                
                                                	power admin state\: up or down
                                                	**type**\:  int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                .. attribute:: power_current_measurement
                                                
                                                	power current\: not implemented
                                                	**type**\:  int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                .. attribute:: power_operational_state
                                                
                                                	Power operation state
                                                	**type**\:  int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                

                                                """

                                                _prefix = 'asr9k-sc-invmgr-admin-oper'
                                                _revision = '2017-01-04'

                                                def __init__(self):
                                                    self.parent = None
                                                    self.card_administrative_state = None
                                                    self.card_monitor_state = None
                                                    self.card_operational_state = None
                                                    self.card_reset_reason = None
                                                    self.card_up_time = Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.BasicAttributes.FruInfo.CardUpTime()
                                                    self.card_up_time.parent = self
                                                    self.last_operational_state_change = Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.BasicAttributes.FruInfo.LastOperationalStateChange()
                                                    self.last_operational_state_change.parent = self
                                                    self.power_administrative_state = None
                                                    self.power_current_measurement = None
                                                    self.power_operational_state = None


                                                class LastOperationalStateChange(object):
                                                    """
                                                    last card oper change state
                                                    
                                                    .. attribute:: time_in_nano_seconds
                                                    
                                                    	Time Value in Nano\-seconds
                                                    	**type**\:  int
                                                    
                                                    	**range:** \-2147483648..2147483647
                                                    
                                                    	**units**\: nanosecond
                                                    
                                                    .. attribute:: time_in_seconds
                                                    
                                                    	Time Value in Seconds
                                                    	**type**\:  int
                                                    
                                                    	**range:** \-2147483648..2147483647
                                                    
                                                    	**units**\: second
                                                    
                                                    

                                                    """

                                                    _prefix = 'asr9k-sc-invmgr-admin-oper'
                                                    _revision = '2017-01-04'

                                                    def __init__(self):
                                                        self.parent = None
                                                        self.time_in_nano_seconds = None
                                                        self.time_in_seconds = None

                                                    @property
                                                    def _common_path(self):
                                                        if self.parent is None:
                                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                                        return self.parent._common_path +'/Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:last-operational-state-change'

                                                    def is_config(self):
                                                        ''' Returns True if this instance represents config data else returns False '''
                                                        return False

                                                    def _has_data(self):
                                                        if self.time_in_nano_seconds is not None:
                                                            return True

                                                        if self.time_in_seconds is not None:
                                                            return True

                                                        return False

                                                    @staticmethod
                                                    def _meta_info():
                                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper as meta
                                                        return meta._meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.BasicAttributes.FruInfo.LastOperationalStateChange']['meta_info']


                                                class CardUpTime(object):
                                                    """
                                                    card up time
                                                    
                                                    .. attribute:: time_in_nano_seconds
                                                    
                                                    	Time Value in Nano\-seconds
                                                    	**type**\:  int
                                                    
                                                    	**range:** \-2147483648..2147483647
                                                    
                                                    	**units**\: nanosecond
                                                    
                                                    .. attribute:: time_in_seconds
                                                    
                                                    	Time Value in Seconds
                                                    	**type**\:  int
                                                    
                                                    	**range:** \-2147483648..2147483647
                                                    
                                                    	**units**\: second
                                                    
                                                    

                                                    """

                                                    _prefix = 'asr9k-sc-invmgr-admin-oper'
                                                    _revision = '2017-01-04'

                                                    def __init__(self):
                                                        self.parent = None
                                                        self.time_in_nano_seconds = None
                                                        self.time_in_seconds = None

                                                    @property
                                                    def _common_path(self):
                                                        if self.parent is None:
                                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                                        return self.parent._common_path +'/Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:card-up-time'

                                                    def is_config(self):
                                                        ''' Returns True if this instance represents config data else returns False '''
                                                        return False

                                                    def _has_data(self):
                                                        if self.time_in_nano_seconds is not None:
                                                            return True

                                                        if self.time_in_seconds is not None:
                                                            return True

                                                        return False

                                                    @staticmethod
                                                    def _meta_info():
                                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper as meta
                                                        return meta._meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.BasicAttributes.FruInfo.CardUpTime']['meta_info']

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:fru-info'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if self.card_administrative_state is not None:
                                                        return True

                                                    if self.card_monitor_state is not None:
                                                        return True

                                                    if self.card_operational_state is not None:
                                                        return True

                                                    if self.card_reset_reason is not None:
                                                        return True

                                                    if self.card_up_time is not None and self.card_up_time._has_data():
                                                        return True

                                                    if self.last_operational_state_change is not None and self.last_operational_state_change._has_data():
                                                        return True

                                                    if self.power_administrative_state is not None:
                                                        return True

                                                    if self.power_current_measurement is not None:
                                                        return True

                                                    if self.power_operational_state is not None:
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper as meta
                                                    return meta._meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.BasicAttributes.FruInfo']['meta_info']


                                            class BasicInfo(object):
                                                """
                                                Inventory information
                                                
                                                .. attribute:: alias
                                                
                                                	useful for storing an entity alias 
                                                	**type**\:  str
                                                
                                                	**length:** 0..255
                                                
                                                .. attribute:: asset_id_str
                                                
                                                	asset Identification string
                                                	**type**\:  str
                                                
                                                	**length:** 0..255
                                                
                                                .. attribute:: asset_identification
                                                
                                                	asset Identification
                                                	**type**\:  int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                .. attribute:: ceport
                                                
                                                	1 if ce port found, 0 if not
                                                	**type**\:  bool
                                                
                                                .. attribute:: chip_hardware_revision
                                                
                                                	chip module hw revision string
                                                	**type**\:  str
                                                
                                                	**length:** 0..255
                                                
                                                .. attribute:: composite_class_code
                                                
                                                	Major&minor class of the entity
                                                	**type**\:  int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                .. attribute:: description
                                                
                                                	describes in user\-readable terms       what the entity in question does
                                                	**type**\:  str
                                                
                                                	**length:** 0..255
                                                
                                                .. attribute:: environmental_monitor_path
                                                
                                                	sysdb name of sensor in the envmon EDM
                                                	**type**\:  str
                                                
                                                	**length:** 0..255
                                                
                                                .. attribute:: firmware_revision
                                                
                                                	firmware revision string
                                                	**type**\:  str
                                                
                                                	**length:** 0..255
                                                
                                                .. attribute:: group_flag
                                                
                                                	indicates if this entity is group       or not
                                                	**type**\:  bool
                                                
                                                .. attribute:: hardware_revision
                                                
                                                	hw revision string
                                                	**type**\:  str
                                                
                                                	**length:** 0..255
                                                
                                                .. attribute:: is_field_replaceable_unit
                                                
                                                	1 if Field Replaceable Unit 0, if not
                                                	**type**\:  bool
                                                
                                                .. attribute:: manufacturer_asset_tags
                                                
                                                	Manufacture Asset Tags
                                                	**type**\:  int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                .. attribute:: manufacturer_name
                                                
                                                	manufacturer's name
                                                	**type**\:  str
                                                
                                                	**length:** 0..255
                                                
                                                .. attribute:: memory_size
                                                
                                                	Size of memory associated with       the entity where applicable
                                                	**type**\:  int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                .. attribute:: model_name
                                                
                                                	model name
                                                	**type**\:  str
                                                
                                                	**length:** 0..255
                                                
                                                .. attribute:: name
                                                
                                                	name string for the entity
                                                	**type**\:  str
                                                
                                                	**length:** 0..255
                                                
                                                .. attribute:: new_deviation_number
                                                
                                                	integer value for New Deviation Number 0x88
                                                	**type**\:  int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                .. attribute:: physical_layer_interface_module_type
                                                
                                                	integer value for plim type if     applicable to this entity
                                                	**type**\:  int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                .. attribute:: redundancystate
                                                
                                                	integer value for Redundancy State if     applicable to this entity
                                                	**type**\:  int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                .. attribute:: serial_number
                                                
                                                	serial number
                                                	**type**\:  str
                                                
                                                	**length:** 0..255
                                                
                                                .. attribute:: software_revision
                                                
                                                	software revision string
                                                	**type**\:  str
                                                
                                                	**length:** 0..255
                                                
                                                .. attribute:: unique_id
                                                
                                                	Unique id for an entity
                                                	**type**\:  int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                .. attribute:: unrecognized_fru
                                                
                                                	1 if UnrecognizedFRU and 0 for recognizedFRU
                                                	**type**\:  bool
                                                
                                                .. attribute:: vendor_type
                                                
                                                	maps to the vendor OID string
                                                	**type**\:  str
                                                
                                                	**length:** 0..255
                                                
                                                .. attribute:: xr_scoped
                                                
                                                	1 if xr scoped, 0 if not
                                                	**type**\:  bool
                                                
                                                

                                                """

                                                _prefix = 'asr9k-sc-invmgr-admin-oper'
                                                _revision = '2017-01-04'

                                                def __init__(self):
                                                    self.parent = None
                                                    self.alias = None
                                                    self.asset_id_str = None
                                                    self.asset_identification = None
                                                    self.ceport = None
                                                    self.chip_hardware_revision = None
                                                    self.composite_class_code = None
                                                    self.description = None
                                                    self.environmental_monitor_path = None
                                                    self.firmware_revision = None
                                                    self.group_flag = None
                                                    self.hardware_revision = None
                                                    self.is_field_replaceable_unit = None
                                                    self.manufacturer_asset_tags = None
                                                    self.manufacturer_name = None
                                                    self.memory_size = None
                                                    self.model_name = None
                                                    self.name = None
                                                    self.new_deviation_number = None
                                                    self.physical_layer_interface_module_type = None
                                                    self.redundancystate = None
                                                    self.serial_number = None
                                                    self.software_revision = None
                                                    self.unique_id = None
                                                    self.unrecognized_fru = None
                                                    self.vendor_type = None
                                                    self.xr_scoped = None

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:basic-info'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if self.alias is not None:
                                                        return True

                                                    if self.asset_id_str is not None:
                                                        return True

                                                    if self.asset_identification is not None:
                                                        return True

                                                    if self.ceport is not None:
                                                        return True

                                                    if self.chip_hardware_revision is not None:
                                                        return True

                                                    if self.composite_class_code is not None:
                                                        return True

                                                    if self.description is not None:
                                                        return True

                                                    if self.environmental_monitor_path is not None:
                                                        return True

                                                    if self.firmware_revision is not None:
                                                        return True

                                                    if self.group_flag is not None:
                                                        return True

                                                    if self.hardware_revision is not None:
                                                        return True

                                                    if self.is_field_replaceable_unit is not None:
                                                        return True

                                                    if self.manufacturer_asset_tags is not None:
                                                        return True

                                                    if self.manufacturer_name is not None:
                                                        return True

                                                    if self.memory_size is not None:
                                                        return True

                                                    if self.model_name is not None:
                                                        return True

                                                    if self.name is not None:
                                                        return True

                                                    if self.new_deviation_number is not None:
                                                        return True

                                                    if self.physical_layer_interface_module_type is not None:
                                                        return True

                                                    if self.redundancystate is not None:
                                                        return True

                                                    if self.serial_number is not None:
                                                        return True

                                                    if self.software_revision is not None:
                                                        return True

                                                    if self.unique_id is not None:
                                                        return True

                                                    if self.unrecognized_fru is not None:
                                                        return True

                                                    if self.vendor_type is not None:
                                                        return True

                                                    if self.xr_scoped is not None:
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper as meta
                                                    return meta._meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.BasicAttributes.BasicInfo']['meta_info']

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:basic-attributes'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.basic_info is not None and self.basic_info._has_data():
                                                    return True

                                                if self.fru_info is not None and self.fru_info._has_data():
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper as meta
                                                return meta._meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.BasicAttributes']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:port'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.basic_attributes is not None and self.basic_attributes._has_data():
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper as meta
                                            return meta._meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port']['meta_info']


                                    class BasicAttributes(object):
                                        """
                                        Attributes
                                        
                                        .. attribute:: basic_info
                                        
                                        	Inventory information
                                        	**type**\:   :py:class:`BasicInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.BasicAttributes.BasicInfo>`
                                        
                                        .. attribute:: fru_info
                                        
                                        	Field Replaceable Unit (FRU) inventory information
                                        	**type**\:   :py:class:`FruInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.BasicAttributes.FruInfo>`
                                        
                                        

                                        """

                                        _prefix = 'asr9k-sc-invmgr-admin-oper'
                                        _revision = '2017-01-04'

                                        def __init__(self):
                                            self.parent = None
                                            self.basic_info = Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.BasicAttributes.BasicInfo()
                                            self.basic_info.parent = self
                                            self.fru_info = Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.BasicAttributes.FruInfo()
                                            self.fru_info.parent = self


                                        class FruInfo(object):
                                            """
                                            Field Replaceable Unit (FRU) inventory
                                            information
                                            
                                            .. attribute:: card_administrative_state
                                            
                                            	card admin state\: shutdown or not
                                            	**type**\:  int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: card_monitor_state
                                            
                                            	card is monitored by a manager or left unmonitored
                                            	**type**\:  int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: card_operational_state
                                            
                                            	card operation state
                                            	**type**\:  int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: card_reset_reason
                                            
                                            	card reset reason enum
                                            	**type**\:   :py:class:`CardResetReasonEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.CardResetReasonEnum>`
                                            
                                            .. attribute:: card_up_time
                                            
                                            	card up time
                                            	**type**\:   :py:class:`CardUpTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.BasicAttributes.FruInfo.CardUpTime>`
                                            
                                            .. attribute:: last_operational_state_change
                                            
                                            	last card oper change state
                                            	**type**\:   :py:class:`LastOperationalStateChange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.BasicAttributes.FruInfo.LastOperationalStateChange>`
                                            
                                            .. attribute:: power_administrative_state
                                            
                                            	power admin state\: up or down
                                            	**type**\:  int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: power_current_measurement
                                            
                                            	power current\: not implemented
                                            	**type**\:  int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: power_operational_state
                                            
                                            	Power operation state
                                            	**type**\:  int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            

                                            """

                                            _prefix = 'asr9k-sc-invmgr-admin-oper'
                                            _revision = '2017-01-04'

                                            def __init__(self):
                                                self.parent = None
                                                self.card_administrative_state = None
                                                self.card_monitor_state = None
                                                self.card_operational_state = None
                                                self.card_reset_reason = None
                                                self.card_up_time = Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.BasicAttributes.FruInfo.CardUpTime()
                                                self.card_up_time.parent = self
                                                self.last_operational_state_change = Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.BasicAttributes.FruInfo.LastOperationalStateChange()
                                                self.last_operational_state_change.parent = self
                                                self.power_administrative_state = None
                                                self.power_current_measurement = None
                                                self.power_operational_state = None


                                            class LastOperationalStateChange(object):
                                                """
                                                last card oper change state
                                                
                                                .. attribute:: time_in_nano_seconds
                                                
                                                	Time Value in Nano\-seconds
                                                	**type**\:  int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                	**units**\: nanosecond
                                                
                                                .. attribute:: time_in_seconds
                                                
                                                	Time Value in Seconds
                                                	**type**\:  int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                	**units**\: second
                                                
                                                

                                                """

                                                _prefix = 'asr9k-sc-invmgr-admin-oper'
                                                _revision = '2017-01-04'

                                                def __init__(self):
                                                    self.parent = None
                                                    self.time_in_nano_seconds = None
                                                    self.time_in_seconds = None

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:last-operational-state-change'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if self.time_in_nano_seconds is not None:
                                                        return True

                                                    if self.time_in_seconds is not None:
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper as meta
                                                    return meta._meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.BasicAttributes.FruInfo.LastOperationalStateChange']['meta_info']


                                            class CardUpTime(object):
                                                """
                                                card up time
                                                
                                                .. attribute:: time_in_nano_seconds
                                                
                                                	Time Value in Nano\-seconds
                                                	**type**\:  int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                	**units**\: nanosecond
                                                
                                                .. attribute:: time_in_seconds
                                                
                                                	Time Value in Seconds
                                                	**type**\:  int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                	**units**\: second
                                                
                                                

                                                """

                                                _prefix = 'asr9k-sc-invmgr-admin-oper'
                                                _revision = '2017-01-04'

                                                def __init__(self):
                                                    self.parent = None
                                                    self.time_in_nano_seconds = None
                                                    self.time_in_seconds = None

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:card-up-time'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if self.time_in_nano_seconds is not None:
                                                        return True

                                                    if self.time_in_seconds is not None:
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper as meta
                                                    return meta._meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.BasicAttributes.FruInfo.CardUpTime']['meta_info']

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:fru-info'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.card_administrative_state is not None:
                                                    return True

                                                if self.card_monitor_state is not None:
                                                    return True

                                                if self.card_operational_state is not None:
                                                    return True

                                                if self.card_reset_reason is not None:
                                                    return True

                                                if self.card_up_time is not None and self.card_up_time._has_data():
                                                    return True

                                                if self.last_operational_state_change is not None and self.last_operational_state_change._has_data():
                                                    return True

                                                if self.power_administrative_state is not None:
                                                    return True

                                                if self.power_current_measurement is not None:
                                                    return True

                                                if self.power_operational_state is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper as meta
                                                return meta._meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.BasicAttributes.FruInfo']['meta_info']


                                        class BasicInfo(object):
                                            """
                                            Inventory information
                                            
                                            .. attribute:: alias
                                            
                                            	useful for storing an entity alias 
                                            	**type**\:  str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: asset_id_str
                                            
                                            	asset Identification string
                                            	**type**\:  str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: asset_identification
                                            
                                            	asset Identification
                                            	**type**\:  int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: ceport
                                            
                                            	1 if ce port found, 0 if not
                                            	**type**\:  bool
                                            
                                            .. attribute:: chip_hardware_revision
                                            
                                            	chip module hw revision string
                                            	**type**\:  str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: composite_class_code
                                            
                                            	Major&minor class of the entity
                                            	**type**\:  int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: description
                                            
                                            	describes in user\-readable terms       what the entity in question does
                                            	**type**\:  str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: environmental_monitor_path
                                            
                                            	sysdb name of sensor in the envmon EDM
                                            	**type**\:  str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: firmware_revision
                                            
                                            	firmware revision string
                                            	**type**\:  str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: group_flag
                                            
                                            	indicates if this entity is group       or not
                                            	**type**\:  bool
                                            
                                            .. attribute:: hardware_revision
                                            
                                            	hw revision string
                                            	**type**\:  str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: is_field_replaceable_unit
                                            
                                            	1 if Field Replaceable Unit 0, if not
                                            	**type**\:  bool
                                            
                                            .. attribute:: manufacturer_asset_tags
                                            
                                            	Manufacture Asset Tags
                                            	**type**\:  int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: manufacturer_name
                                            
                                            	manufacturer's name
                                            	**type**\:  str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: memory_size
                                            
                                            	Size of memory associated with       the entity where applicable
                                            	**type**\:  int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: model_name
                                            
                                            	model name
                                            	**type**\:  str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: name
                                            
                                            	name string for the entity
                                            	**type**\:  str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: new_deviation_number
                                            
                                            	integer value for New Deviation Number 0x88
                                            	**type**\:  int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: physical_layer_interface_module_type
                                            
                                            	integer value for plim type if     applicable to this entity
                                            	**type**\:  int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: redundancystate
                                            
                                            	integer value for Redundancy State if     applicable to this entity
                                            	**type**\:  int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: serial_number
                                            
                                            	serial number
                                            	**type**\:  str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: software_revision
                                            
                                            	software revision string
                                            	**type**\:  str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: unique_id
                                            
                                            	Unique id for an entity
                                            	**type**\:  int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: unrecognized_fru
                                            
                                            	1 if UnrecognizedFRU and 0 for recognizedFRU
                                            	**type**\:  bool
                                            
                                            .. attribute:: vendor_type
                                            
                                            	maps to the vendor OID string
                                            	**type**\:  str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: xr_scoped
                                            
                                            	1 if xr scoped, 0 if not
                                            	**type**\:  bool
                                            
                                            

                                            """

                                            _prefix = 'asr9k-sc-invmgr-admin-oper'
                                            _revision = '2017-01-04'

                                            def __init__(self):
                                                self.parent = None
                                                self.alias = None
                                                self.asset_id_str = None
                                                self.asset_identification = None
                                                self.ceport = None
                                                self.chip_hardware_revision = None
                                                self.composite_class_code = None
                                                self.description = None
                                                self.environmental_monitor_path = None
                                                self.firmware_revision = None
                                                self.group_flag = None
                                                self.hardware_revision = None
                                                self.is_field_replaceable_unit = None
                                                self.manufacturer_asset_tags = None
                                                self.manufacturer_name = None
                                                self.memory_size = None
                                                self.model_name = None
                                                self.name = None
                                                self.new_deviation_number = None
                                                self.physical_layer_interface_module_type = None
                                                self.redundancystate = None
                                                self.serial_number = None
                                                self.software_revision = None
                                                self.unique_id = None
                                                self.unrecognized_fru = None
                                                self.vendor_type = None
                                                self.xr_scoped = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:basic-info'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.alias is not None:
                                                    return True

                                                if self.asset_id_str is not None:
                                                    return True

                                                if self.asset_identification is not None:
                                                    return True

                                                if self.ceport is not None:
                                                    return True

                                                if self.chip_hardware_revision is not None:
                                                    return True

                                                if self.composite_class_code is not None:
                                                    return True

                                                if self.description is not None:
                                                    return True

                                                if self.environmental_monitor_path is not None:
                                                    return True

                                                if self.firmware_revision is not None:
                                                    return True

                                                if self.group_flag is not None:
                                                    return True

                                                if self.hardware_revision is not None:
                                                    return True

                                                if self.is_field_replaceable_unit is not None:
                                                    return True

                                                if self.manufacturer_asset_tags is not None:
                                                    return True

                                                if self.manufacturer_name is not None:
                                                    return True

                                                if self.memory_size is not None:
                                                    return True

                                                if self.model_name is not None:
                                                    return True

                                                if self.name is not None:
                                                    return True

                                                if self.new_deviation_number is not None:
                                                    return True

                                                if self.physical_layer_interface_module_type is not None:
                                                    return True

                                                if self.redundancystate is not None:
                                                    return True

                                                if self.serial_number is not None:
                                                    return True

                                                if self.software_revision is not None:
                                                    return True

                                                if self.unique_id is not None:
                                                    return True

                                                if self.unrecognized_fru is not None:
                                                    return True

                                                if self.vendor_type is not None:
                                                    return True

                                                if self.xr_scoped is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper as meta
                                                return meta._meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.BasicAttributes.BasicInfo']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:basic-attributes'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.basic_info is not None and self.basic_info._has_data():
                                                return True

                                            if self.fru_info is not None and self.fru_info._has_data():
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper as meta
                                            return meta._meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.BasicAttributes']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')
                                        if self.number is None:
                                            raise YPYModelError('Key property number is None')

                                        return self.parent._common_path +'/Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:port-slot[Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:number = ' + str(self.number) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.number is not None:
                                            return True

                                        if self.basic_attributes is not None and self.basic_attributes._has_data():
                                            return True

                                        if self.port is not None and self.port._has_data():
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper as meta
                                        return meta._meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:port-slots'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.port_slot is not None:
                                        for child_ref in self.port_slot:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper as meta
                                    return meta._meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots']['meta_info']


                            class Sensors(object):
                                """
                                ModuleSensorTable contains all sensors in a
                                Module.
                                
                                .. attribute:: sensor
                                
                                	Sensor number in the Module
                                	**type**\: list of    :py:class:`Sensor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor>`
                                
                                

                                """

                                _prefix = 'asr9k-sc-invmgr-admin-oper'
                                _revision = '2017-01-04'

                                def __init__(self):
                                    self.parent = None
                                    self.sensor = YList()
                                    self.sensor.parent = self
                                    self.sensor.name = 'sensor'


                                class Sensor(object):
                                    """
                                    Sensor number in the Module
                                    
                                    .. attribute:: number  <key>
                                    
                                    	sensor number
                                    	**type**\:  int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: basic_attributes
                                    
                                    	Attributes
                                    	**type**\:   :py:class:`BasicAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.BasicAttributes>`
                                    
                                    

                                    """

                                    _prefix = 'asr9k-sc-invmgr-admin-oper'
                                    _revision = '2017-01-04'

                                    def __init__(self):
                                        self.parent = None
                                        self.number = None
                                        self.basic_attributes = Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.BasicAttributes()
                                        self.basic_attributes.parent = self


                                    class BasicAttributes(object):
                                        """
                                        Attributes
                                        
                                        .. attribute:: basic_info
                                        
                                        	Inventory information
                                        	**type**\:   :py:class:`BasicInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.BasicAttributes.BasicInfo>`
                                        
                                        .. attribute:: fru_info
                                        
                                        	Field Replaceable Unit (FRU) inventory information
                                        	**type**\:   :py:class:`FruInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.BasicAttributes.FruInfo>`
                                        
                                        

                                        """

                                        _prefix = 'asr9k-sc-invmgr-admin-oper'
                                        _revision = '2017-01-04'

                                        def __init__(self):
                                            self.parent = None
                                            self.basic_info = Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.BasicAttributes.BasicInfo()
                                            self.basic_info.parent = self
                                            self.fru_info = Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.BasicAttributes.FruInfo()
                                            self.fru_info.parent = self


                                        class FruInfo(object):
                                            """
                                            Field Replaceable Unit (FRU) inventory
                                            information
                                            
                                            .. attribute:: card_administrative_state
                                            
                                            	card admin state\: shutdown or not
                                            	**type**\:  int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: card_monitor_state
                                            
                                            	card is monitored by a manager or left unmonitored
                                            	**type**\:  int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: card_operational_state
                                            
                                            	card operation state
                                            	**type**\:  int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: card_reset_reason
                                            
                                            	card reset reason enum
                                            	**type**\:   :py:class:`CardResetReasonEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.CardResetReasonEnum>`
                                            
                                            .. attribute:: card_up_time
                                            
                                            	card up time
                                            	**type**\:   :py:class:`CardUpTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.BasicAttributes.FruInfo.CardUpTime>`
                                            
                                            .. attribute:: last_operational_state_change
                                            
                                            	last card oper change state
                                            	**type**\:   :py:class:`LastOperationalStateChange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.BasicAttributes.FruInfo.LastOperationalStateChange>`
                                            
                                            .. attribute:: power_administrative_state
                                            
                                            	power admin state\: up or down
                                            	**type**\:  int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: power_current_measurement
                                            
                                            	power current\: not implemented
                                            	**type**\:  int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: power_operational_state
                                            
                                            	Power operation state
                                            	**type**\:  int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            

                                            """

                                            _prefix = 'asr9k-sc-invmgr-admin-oper'
                                            _revision = '2017-01-04'

                                            def __init__(self):
                                                self.parent = None
                                                self.card_administrative_state = None
                                                self.card_monitor_state = None
                                                self.card_operational_state = None
                                                self.card_reset_reason = None
                                                self.card_up_time = Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.BasicAttributes.FruInfo.CardUpTime()
                                                self.card_up_time.parent = self
                                                self.last_operational_state_change = Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.BasicAttributes.FruInfo.LastOperationalStateChange()
                                                self.last_operational_state_change.parent = self
                                                self.power_administrative_state = None
                                                self.power_current_measurement = None
                                                self.power_operational_state = None


                                            class LastOperationalStateChange(object):
                                                """
                                                last card oper change state
                                                
                                                .. attribute:: time_in_nano_seconds
                                                
                                                	Time Value in Nano\-seconds
                                                	**type**\:  int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                	**units**\: nanosecond
                                                
                                                .. attribute:: time_in_seconds
                                                
                                                	Time Value in Seconds
                                                	**type**\:  int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                	**units**\: second
                                                
                                                

                                                """

                                                _prefix = 'asr9k-sc-invmgr-admin-oper'
                                                _revision = '2017-01-04'

                                                def __init__(self):
                                                    self.parent = None
                                                    self.time_in_nano_seconds = None
                                                    self.time_in_seconds = None

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:last-operational-state-change'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if self.time_in_nano_seconds is not None:
                                                        return True

                                                    if self.time_in_seconds is not None:
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper as meta
                                                    return meta._meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.BasicAttributes.FruInfo.LastOperationalStateChange']['meta_info']


                                            class CardUpTime(object):
                                                """
                                                card up time
                                                
                                                .. attribute:: time_in_nano_seconds
                                                
                                                	Time Value in Nano\-seconds
                                                	**type**\:  int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                	**units**\: nanosecond
                                                
                                                .. attribute:: time_in_seconds
                                                
                                                	Time Value in Seconds
                                                	**type**\:  int
                                                
                                                	**range:** \-2147483648..2147483647
                                                
                                                	**units**\: second
                                                
                                                

                                                """

                                                _prefix = 'asr9k-sc-invmgr-admin-oper'
                                                _revision = '2017-01-04'

                                                def __init__(self):
                                                    self.parent = None
                                                    self.time_in_nano_seconds = None
                                                    self.time_in_seconds = None

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:card-up-time'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if self.time_in_nano_seconds is not None:
                                                        return True

                                                    if self.time_in_seconds is not None:
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper as meta
                                                    return meta._meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.BasicAttributes.FruInfo.CardUpTime']['meta_info']

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:fru-info'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.card_administrative_state is not None:
                                                    return True

                                                if self.card_monitor_state is not None:
                                                    return True

                                                if self.card_operational_state is not None:
                                                    return True

                                                if self.card_reset_reason is not None:
                                                    return True

                                                if self.card_up_time is not None and self.card_up_time._has_data():
                                                    return True

                                                if self.last_operational_state_change is not None and self.last_operational_state_change._has_data():
                                                    return True

                                                if self.power_administrative_state is not None:
                                                    return True

                                                if self.power_current_measurement is not None:
                                                    return True

                                                if self.power_operational_state is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper as meta
                                                return meta._meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.BasicAttributes.FruInfo']['meta_info']


                                        class BasicInfo(object):
                                            """
                                            Inventory information
                                            
                                            .. attribute:: alias
                                            
                                            	useful for storing an entity alias 
                                            	**type**\:  str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: asset_id_str
                                            
                                            	asset Identification string
                                            	**type**\:  str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: asset_identification
                                            
                                            	asset Identification
                                            	**type**\:  int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: ceport
                                            
                                            	1 if ce port found, 0 if not
                                            	**type**\:  bool
                                            
                                            .. attribute:: chip_hardware_revision
                                            
                                            	chip module hw revision string
                                            	**type**\:  str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: composite_class_code
                                            
                                            	Major&minor class of the entity
                                            	**type**\:  int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: description
                                            
                                            	describes in user\-readable terms       what the entity in question does
                                            	**type**\:  str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: environmental_monitor_path
                                            
                                            	sysdb name of sensor in the envmon EDM
                                            	**type**\:  str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: firmware_revision
                                            
                                            	firmware revision string
                                            	**type**\:  str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: group_flag
                                            
                                            	indicates if this entity is group       or not
                                            	**type**\:  bool
                                            
                                            .. attribute:: hardware_revision
                                            
                                            	hw revision string
                                            	**type**\:  str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: is_field_replaceable_unit
                                            
                                            	1 if Field Replaceable Unit 0, if not
                                            	**type**\:  bool
                                            
                                            .. attribute:: manufacturer_asset_tags
                                            
                                            	Manufacture Asset Tags
                                            	**type**\:  int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: manufacturer_name
                                            
                                            	manufacturer's name
                                            	**type**\:  str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: memory_size
                                            
                                            	Size of memory associated with       the entity where applicable
                                            	**type**\:  int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: model_name
                                            
                                            	model name
                                            	**type**\:  str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: name
                                            
                                            	name string for the entity
                                            	**type**\:  str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: new_deviation_number
                                            
                                            	integer value for New Deviation Number 0x88
                                            	**type**\:  int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: physical_layer_interface_module_type
                                            
                                            	integer value for plim type if     applicable to this entity
                                            	**type**\:  int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: redundancystate
                                            
                                            	integer value for Redundancy State if     applicable to this entity
                                            	**type**\:  int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: serial_number
                                            
                                            	serial number
                                            	**type**\:  str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: software_revision
                                            
                                            	software revision string
                                            	**type**\:  str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: unique_id
                                            
                                            	Unique id for an entity
                                            	**type**\:  int
                                            
                                            	**range:** \-2147483648..2147483647
                                            
                                            .. attribute:: unrecognized_fru
                                            
                                            	1 if UnrecognizedFRU and 0 for recognizedFRU
                                            	**type**\:  bool
                                            
                                            .. attribute:: vendor_type
                                            
                                            	maps to the vendor OID string
                                            	**type**\:  str
                                            
                                            	**length:** 0..255
                                            
                                            .. attribute:: xr_scoped
                                            
                                            	1 if xr scoped, 0 if not
                                            	**type**\:  bool
                                            
                                            

                                            """

                                            _prefix = 'asr9k-sc-invmgr-admin-oper'
                                            _revision = '2017-01-04'

                                            def __init__(self):
                                                self.parent = None
                                                self.alias = None
                                                self.asset_id_str = None
                                                self.asset_identification = None
                                                self.ceport = None
                                                self.chip_hardware_revision = None
                                                self.composite_class_code = None
                                                self.description = None
                                                self.environmental_monitor_path = None
                                                self.firmware_revision = None
                                                self.group_flag = None
                                                self.hardware_revision = None
                                                self.is_field_replaceable_unit = None
                                                self.manufacturer_asset_tags = None
                                                self.manufacturer_name = None
                                                self.memory_size = None
                                                self.model_name = None
                                                self.name = None
                                                self.new_deviation_number = None
                                                self.physical_layer_interface_module_type = None
                                                self.redundancystate = None
                                                self.serial_number = None
                                                self.software_revision = None
                                                self.unique_id = None
                                                self.unrecognized_fru = None
                                                self.vendor_type = None
                                                self.xr_scoped = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:basic-info'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.alias is not None:
                                                    return True

                                                if self.asset_id_str is not None:
                                                    return True

                                                if self.asset_identification is not None:
                                                    return True

                                                if self.ceport is not None:
                                                    return True

                                                if self.chip_hardware_revision is not None:
                                                    return True

                                                if self.composite_class_code is not None:
                                                    return True

                                                if self.description is not None:
                                                    return True

                                                if self.environmental_monitor_path is not None:
                                                    return True

                                                if self.firmware_revision is not None:
                                                    return True

                                                if self.group_flag is not None:
                                                    return True

                                                if self.hardware_revision is not None:
                                                    return True

                                                if self.is_field_replaceable_unit is not None:
                                                    return True

                                                if self.manufacturer_asset_tags is not None:
                                                    return True

                                                if self.manufacturer_name is not None:
                                                    return True

                                                if self.memory_size is not None:
                                                    return True

                                                if self.model_name is not None:
                                                    return True

                                                if self.name is not None:
                                                    return True

                                                if self.new_deviation_number is not None:
                                                    return True

                                                if self.physical_layer_interface_module_type is not None:
                                                    return True

                                                if self.redundancystate is not None:
                                                    return True

                                                if self.serial_number is not None:
                                                    return True

                                                if self.software_revision is not None:
                                                    return True

                                                if self.unique_id is not None:
                                                    return True

                                                if self.unrecognized_fru is not None:
                                                    return True

                                                if self.vendor_type is not None:
                                                    return True

                                                if self.xr_scoped is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper as meta
                                                return meta._meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.BasicAttributes.BasicInfo']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:basic-attributes'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.basic_info is not None and self.basic_info._has_data():
                                                return True

                                            if self.fru_info is not None and self.fru_info._has_data():
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper as meta
                                            return meta._meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.BasicAttributes']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')
                                        if self.number is None:
                                            raise YPYModelError('Key property number is None')

                                        return self.parent._common_path +'/Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:sensor[Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:number = ' + str(self.number) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.number is not None:
                                            return True

                                        if self.basic_attributes is not None and self.basic_attributes._has_data():
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper as meta
                                        return meta._meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:sensors'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.sensor is not None:
                                        for child_ref in self.sensor:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper as meta
                                    return meta._meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors']['meta_info']


                            class BasicAttributes(object):
                                """
                                Attributes
                                
                                .. attribute:: basic_info
                                
                                	Inventory information
                                	**type**\:   :py:class:`BasicInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.BasicAttributes.BasicInfo>`
                                
                                .. attribute:: fru_info
                                
                                	Field Replaceable Unit (FRU) inventory information
                                	**type**\:   :py:class:`FruInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.BasicAttributes.FruInfo>`
                                
                                

                                """

                                _prefix = 'asr9k-sc-invmgr-admin-oper'
                                _revision = '2017-01-04'

                                def __init__(self):
                                    self.parent = None
                                    self.basic_info = Inventory.Racks.Rack.Slots.Slot.Cards.Card.BasicAttributes.BasicInfo()
                                    self.basic_info.parent = self
                                    self.fru_info = Inventory.Racks.Rack.Slots.Slot.Cards.Card.BasicAttributes.FruInfo()
                                    self.fru_info.parent = self


                                class FruInfo(object):
                                    """
                                    Field Replaceable Unit (FRU) inventory
                                    information
                                    
                                    .. attribute:: card_administrative_state
                                    
                                    	card admin state\: shutdown or not
                                    	**type**\:  int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: card_monitor_state
                                    
                                    	card is monitored by a manager or left unmonitored
                                    	**type**\:  int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: card_operational_state
                                    
                                    	card operation state
                                    	**type**\:  int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: card_reset_reason
                                    
                                    	card reset reason enum
                                    	**type**\:   :py:class:`CardResetReasonEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.CardResetReasonEnum>`
                                    
                                    .. attribute:: card_up_time
                                    
                                    	card up time
                                    	**type**\:   :py:class:`CardUpTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.BasicAttributes.FruInfo.CardUpTime>`
                                    
                                    .. attribute:: last_operational_state_change
                                    
                                    	last card oper change state
                                    	**type**\:   :py:class:`LastOperationalStateChange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.BasicAttributes.FruInfo.LastOperationalStateChange>`
                                    
                                    .. attribute:: power_administrative_state
                                    
                                    	power admin state\: up or down
                                    	**type**\:  int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: power_current_measurement
                                    
                                    	power current\: not implemented
                                    	**type**\:  int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: power_operational_state
                                    
                                    	Power operation state
                                    	**type**\:  int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    

                                    """

                                    _prefix = 'asr9k-sc-invmgr-admin-oper'
                                    _revision = '2017-01-04'

                                    def __init__(self):
                                        self.parent = None
                                        self.card_administrative_state = None
                                        self.card_monitor_state = None
                                        self.card_operational_state = None
                                        self.card_reset_reason = None
                                        self.card_up_time = Inventory.Racks.Rack.Slots.Slot.Cards.Card.BasicAttributes.FruInfo.CardUpTime()
                                        self.card_up_time.parent = self
                                        self.last_operational_state_change = Inventory.Racks.Rack.Slots.Slot.Cards.Card.BasicAttributes.FruInfo.LastOperationalStateChange()
                                        self.last_operational_state_change.parent = self
                                        self.power_administrative_state = None
                                        self.power_current_measurement = None
                                        self.power_operational_state = None


                                    class LastOperationalStateChange(object):
                                        """
                                        last card oper change state
                                        
                                        .. attribute:: time_in_nano_seconds
                                        
                                        	Time Value in Nano\-seconds
                                        	**type**\:  int
                                        
                                        	**range:** \-2147483648..2147483647
                                        
                                        	**units**\: nanosecond
                                        
                                        .. attribute:: time_in_seconds
                                        
                                        	Time Value in Seconds
                                        	**type**\:  int
                                        
                                        	**range:** \-2147483648..2147483647
                                        
                                        	**units**\: second
                                        
                                        

                                        """

                                        _prefix = 'asr9k-sc-invmgr-admin-oper'
                                        _revision = '2017-01-04'

                                        def __init__(self):
                                            self.parent = None
                                            self.time_in_nano_seconds = None
                                            self.time_in_seconds = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:last-operational-state-change'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.time_in_nano_seconds is not None:
                                                return True

                                            if self.time_in_seconds is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper as meta
                                            return meta._meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.BasicAttributes.FruInfo.LastOperationalStateChange']['meta_info']


                                    class CardUpTime(object):
                                        """
                                        card up time
                                        
                                        .. attribute:: time_in_nano_seconds
                                        
                                        	Time Value in Nano\-seconds
                                        	**type**\:  int
                                        
                                        	**range:** \-2147483648..2147483647
                                        
                                        	**units**\: nanosecond
                                        
                                        .. attribute:: time_in_seconds
                                        
                                        	Time Value in Seconds
                                        	**type**\:  int
                                        
                                        	**range:** \-2147483648..2147483647
                                        
                                        	**units**\: second
                                        
                                        

                                        """

                                        _prefix = 'asr9k-sc-invmgr-admin-oper'
                                        _revision = '2017-01-04'

                                        def __init__(self):
                                            self.parent = None
                                            self.time_in_nano_seconds = None
                                            self.time_in_seconds = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:card-up-time'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.time_in_nano_seconds is not None:
                                                return True

                                            if self.time_in_seconds is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper as meta
                                            return meta._meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.BasicAttributes.FruInfo.CardUpTime']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:fru-info'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.card_administrative_state is not None:
                                            return True

                                        if self.card_monitor_state is not None:
                                            return True

                                        if self.card_operational_state is not None:
                                            return True

                                        if self.card_reset_reason is not None:
                                            return True

                                        if self.card_up_time is not None and self.card_up_time._has_data():
                                            return True

                                        if self.last_operational_state_change is not None and self.last_operational_state_change._has_data():
                                            return True

                                        if self.power_administrative_state is not None:
                                            return True

                                        if self.power_current_measurement is not None:
                                            return True

                                        if self.power_operational_state is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper as meta
                                        return meta._meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.BasicAttributes.FruInfo']['meta_info']


                                class BasicInfo(object):
                                    """
                                    Inventory information
                                    
                                    .. attribute:: alias
                                    
                                    	useful for storing an entity alias 
                                    	**type**\:  str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: asset_id_str
                                    
                                    	asset Identification string
                                    	**type**\:  str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: asset_identification
                                    
                                    	asset Identification
                                    	**type**\:  int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: ceport
                                    
                                    	1 if ce port found, 0 if not
                                    	**type**\:  bool
                                    
                                    .. attribute:: chip_hardware_revision
                                    
                                    	chip module hw revision string
                                    	**type**\:  str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: composite_class_code
                                    
                                    	Major&minor class of the entity
                                    	**type**\:  int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: description
                                    
                                    	describes in user\-readable terms       what the entity in question does
                                    	**type**\:  str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: environmental_monitor_path
                                    
                                    	sysdb name of sensor in the envmon EDM
                                    	**type**\:  str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: firmware_revision
                                    
                                    	firmware revision string
                                    	**type**\:  str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: group_flag
                                    
                                    	indicates if this entity is group       or not
                                    	**type**\:  bool
                                    
                                    .. attribute:: hardware_revision
                                    
                                    	hw revision string
                                    	**type**\:  str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: is_field_replaceable_unit
                                    
                                    	1 if Field Replaceable Unit 0, if not
                                    	**type**\:  bool
                                    
                                    .. attribute:: manufacturer_asset_tags
                                    
                                    	Manufacture Asset Tags
                                    	**type**\:  int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: manufacturer_name
                                    
                                    	manufacturer's name
                                    	**type**\:  str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: memory_size
                                    
                                    	Size of memory associated with       the entity where applicable
                                    	**type**\:  int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: model_name
                                    
                                    	model name
                                    	**type**\:  str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: name
                                    
                                    	name string for the entity
                                    	**type**\:  str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: new_deviation_number
                                    
                                    	integer value for New Deviation Number 0x88
                                    	**type**\:  int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: physical_layer_interface_module_type
                                    
                                    	integer value for plim type if     applicable to this entity
                                    	**type**\:  int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: redundancystate
                                    
                                    	integer value for Redundancy State if     applicable to this entity
                                    	**type**\:  int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: serial_number
                                    
                                    	serial number
                                    	**type**\:  str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: software_revision
                                    
                                    	software revision string
                                    	**type**\:  str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: unique_id
                                    
                                    	Unique id for an entity
                                    	**type**\:  int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    .. attribute:: unrecognized_fru
                                    
                                    	1 if UnrecognizedFRU and 0 for recognizedFRU
                                    	**type**\:  bool
                                    
                                    .. attribute:: vendor_type
                                    
                                    	maps to the vendor OID string
                                    	**type**\:  str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: xr_scoped
                                    
                                    	1 if xr scoped, 0 if not
                                    	**type**\:  bool
                                    
                                    

                                    """

                                    _prefix = 'asr9k-sc-invmgr-admin-oper'
                                    _revision = '2017-01-04'

                                    def __init__(self):
                                        self.parent = None
                                        self.alias = None
                                        self.asset_id_str = None
                                        self.asset_identification = None
                                        self.ceport = None
                                        self.chip_hardware_revision = None
                                        self.composite_class_code = None
                                        self.description = None
                                        self.environmental_monitor_path = None
                                        self.firmware_revision = None
                                        self.group_flag = None
                                        self.hardware_revision = None
                                        self.is_field_replaceable_unit = None
                                        self.manufacturer_asset_tags = None
                                        self.manufacturer_name = None
                                        self.memory_size = None
                                        self.model_name = None
                                        self.name = None
                                        self.new_deviation_number = None
                                        self.physical_layer_interface_module_type = None
                                        self.redundancystate = None
                                        self.serial_number = None
                                        self.software_revision = None
                                        self.unique_id = None
                                        self.unrecognized_fru = None
                                        self.vendor_type = None
                                        self.xr_scoped = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:basic-info'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.alias is not None:
                                            return True

                                        if self.asset_id_str is not None:
                                            return True

                                        if self.asset_identification is not None:
                                            return True

                                        if self.ceport is not None:
                                            return True

                                        if self.chip_hardware_revision is not None:
                                            return True

                                        if self.composite_class_code is not None:
                                            return True

                                        if self.description is not None:
                                            return True

                                        if self.environmental_monitor_path is not None:
                                            return True

                                        if self.firmware_revision is not None:
                                            return True

                                        if self.group_flag is not None:
                                            return True

                                        if self.hardware_revision is not None:
                                            return True

                                        if self.is_field_replaceable_unit is not None:
                                            return True

                                        if self.manufacturer_asset_tags is not None:
                                            return True

                                        if self.manufacturer_name is not None:
                                            return True

                                        if self.memory_size is not None:
                                            return True

                                        if self.model_name is not None:
                                            return True

                                        if self.name is not None:
                                            return True

                                        if self.new_deviation_number is not None:
                                            return True

                                        if self.physical_layer_interface_module_type is not None:
                                            return True

                                        if self.redundancystate is not None:
                                            return True

                                        if self.serial_number is not None:
                                            return True

                                        if self.software_revision is not None:
                                            return True

                                        if self.unique_id is not None:
                                            return True

                                        if self.unrecognized_fru is not None:
                                            return True

                                        if self.vendor_type is not None:
                                            return True

                                        if self.xr_scoped is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper as meta
                                        return meta._meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.BasicAttributes.BasicInfo']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:basic-attributes'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.basic_info is not None and self.basic_info._has_data():
                                        return True

                                    if self.fru_info is not None and self.fru_info._has_data():
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper as meta
                                    return meta._meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.BasicAttributes']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.number is None:
                                    raise YPYModelError('Key property number is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:card[Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:number = ' + str(self.number) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.number is not None:
                                    return True

                                if self.basic_attributes is not None and self.basic_attributes._has_data():
                                    return True

                                if self.hw_components is not None and self.hw_components._has_data():
                                    return True

                                if self.port_slots is not None and self.port_slots._has_data():
                                    return True

                                if self.sensors is not None and self.sensors._has_data():
                                    return True

                                if self.sub_slots is not None and self.sub_slots._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper as meta
                                return meta._meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:cards'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.card is not None:
                                for child_ref in self.card:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper as meta
                            return meta._meta_table['Inventory.Racks.Rack.Slots.Slot.Cards']['meta_info']


                    class BasicAttributes(object):
                        """
                        Attributes
                        
                        .. attribute:: basic_info
                        
                        	Inventory information
                        	**type**\:   :py:class:`BasicInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.Inventory.Racks.Rack.Slots.Slot.BasicAttributes.BasicInfo>`
                        
                        .. attribute:: fru_info
                        
                        	Field Replaceable Unit (FRU) inventory information
                        	**type**\:   :py:class:`FruInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.Inventory.Racks.Rack.Slots.Slot.BasicAttributes.FruInfo>`
                        
                        

                        """

                        _prefix = 'asr9k-sc-invmgr-admin-oper'
                        _revision = '2017-01-04'

                        def __init__(self):
                            self.parent = None
                            self.basic_info = Inventory.Racks.Rack.Slots.Slot.BasicAttributes.BasicInfo()
                            self.basic_info.parent = self
                            self.fru_info = Inventory.Racks.Rack.Slots.Slot.BasicAttributes.FruInfo()
                            self.fru_info.parent = self


                        class FruInfo(object):
                            """
                            Field Replaceable Unit (FRU) inventory
                            information
                            
                            .. attribute:: card_administrative_state
                            
                            	card admin state\: shutdown or not
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: card_monitor_state
                            
                            	card is monitored by a manager or left unmonitored
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: card_operational_state
                            
                            	card operation state
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: card_reset_reason
                            
                            	card reset reason enum
                            	**type**\:   :py:class:`CardResetReasonEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.CardResetReasonEnum>`
                            
                            .. attribute:: card_up_time
                            
                            	card up time
                            	**type**\:   :py:class:`CardUpTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.Inventory.Racks.Rack.Slots.Slot.BasicAttributes.FruInfo.CardUpTime>`
                            
                            .. attribute:: last_operational_state_change
                            
                            	last card oper change state
                            	**type**\:   :py:class:`LastOperationalStateChange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.Inventory.Racks.Rack.Slots.Slot.BasicAttributes.FruInfo.LastOperationalStateChange>`
                            
                            .. attribute:: power_administrative_state
                            
                            	power admin state\: up or down
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: power_current_measurement
                            
                            	power current\: not implemented
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: power_operational_state
                            
                            	Power operation state
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            

                            """

                            _prefix = 'asr9k-sc-invmgr-admin-oper'
                            _revision = '2017-01-04'

                            def __init__(self):
                                self.parent = None
                                self.card_administrative_state = None
                                self.card_monitor_state = None
                                self.card_operational_state = None
                                self.card_reset_reason = None
                                self.card_up_time = Inventory.Racks.Rack.Slots.Slot.BasicAttributes.FruInfo.CardUpTime()
                                self.card_up_time.parent = self
                                self.last_operational_state_change = Inventory.Racks.Rack.Slots.Slot.BasicAttributes.FruInfo.LastOperationalStateChange()
                                self.last_operational_state_change.parent = self
                                self.power_administrative_state = None
                                self.power_current_measurement = None
                                self.power_operational_state = None


                            class LastOperationalStateChange(object):
                                """
                                last card oper change state
                                
                                .. attribute:: time_in_nano_seconds
                                
                                	Time Value in Nano\-seconds
                                	**type**\:  int
                                
                                	**range:** \-2147483648..2147483647
                                
                                	**units**\: nanosecond
                                
                                .. attribute:: time_in_seconds
                                
                                	Time Value in Seconds
                                	**type**\:  int
                                
                                	**range:** \-2147483648..2147483647
                                
                                	**units**\: second
                                
                                

                                """

                                _prefix = 'asr9k-sc-invmgr-admin-oper'
                                _revision = '2017-01-04'

                                def __init__(self):
                                    self.parent = None
                                    self.time_in_nano_seconds = None
                                    self.time_in_seconds = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:last-operational-state-change'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.time_in_nano_seconds is not None:
                                        return True

                                    if self.time_in_seconds is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper as meta
                                    return meta._meta_table['Inventory.Racks.Rack.Slots.Slot.BasicAttributes.FruInfo.LastOperationalStateChange']['meta_info']


                            class CardUpTime(object):
                                """
                                card up time
                                
                                .. attribute:: time_in_nano_seconds
                                
                                	Time Value in Nano\-seconds
                                	**type**\:  int
                                
                                	**range:** \-2147483648..2147483647
                                
                                	**units**\: nanosecond
                                
                                .. attribute:: time_in_seconds
                                
                                	Time Value in Seconds
                                	**type**\:  int
                                
                                	**range:** \-2147483648..2147483647
                                
                                	**units**\: second
                                
                                

                                """

                                _prefix = 'asr9k-sc-invmgr-admin-oper'
                                _revision = '2017-01-04'

                                def __init__(self):
                                    self.parent = None
                                    self.time_in_nano_seconds = None
                                    self.time_in_seconds = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:card-up-time'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.time_in_nano_seconds is not None:
                                        return True

                                    if self.time_in_seconds is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper as meta
                                    return meta._meta_table['Inventory.Racks.Rack.Slots.Slot.BasicAttributes.FruInfo.CardUpTime']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:fru-info'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.card_administrative_state is not None:
                                    return True

                                if self.card_monitor_state is not None:
                                    return True

                                if self.card_operational_state is not None:
                                    return True

                                if self.card_reset_reason is not None:
                                    return True

                                if self.card_up_time is not None and self.card_up_time._has_data():
                                    return True

                                if self.last_operational_state_change is not None and self.last_operational_state_change._has_data():
                                    return True

                                if self.power_administrative_state is not None:
                                    return True

                                if self.power_current_measurement is not None:
                                    return True

                                if self.power_operational_state is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper as meta
                                return meta._meta_table['Inventory.Racks.Rack.Slots.Slot.BasicAttributes.FruInfo']['meta_info']


                        class BasicInfo(object):
                            """
                            Inventory information
                            
                            .. attribute:: alias
                            
                            	useful for storing an entity alias 
                            	**type**\:  str
                            
                            	**length:** 0..255
                            
                            .. attribute:: asset_id_str
                            
                            	asset Identification string
                            	**type**\:  str
                            
                            	**length:** 0..255
                            
                            .. attribute:: asset_identification
                            
                            	asset Identification
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: ceport
                            
                            	1 if ce port found, 0 if not
                            	**type**\:  bool
                            
                            .. attribute:: chip_hardware_revision
                            
                            	chip module hw revision string
                            	**type**\:  str
                            
                            	**length:** 0..255
                            
                            .. attribute:: composite_class_code
                            
                            	Major&minor class of the entity
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: description
                            
                            	describes in user\-readable terms       what the entity in question does
                            	**type**\:  str
                            
                            	**length:** 0..255
                            
                            .. attribute:: environmental_monitor_path
                            
                            	sysdb name of sensor in the envmon EDM
                            	**type**\:  str
                            
                            	**length:** 0..255
                            
                            .. attribute:: firmware_revision
                            
                            	firmware revision string
                            	**type**\:  str
                            
                            	**length:** 0..255
                            
                            .. attribute:: group_flag
                            
                            	indicates if this entity is group       or not
                            	**type**\:  bool
                            
                            .. attribute:: hardware_revision
                            
                            	hw revision string
                            	**type**\:  str
                            
                            	**length:** 0..255
                            
                            .. attribute:: is_field_replaceable_unit
                            
                            	1 if Field Replaceable Unit 0, if not
                            	**type**\:  bool
                            
                            .. attribute:: manufacturer_asset_tags
                            
                            	Manufacture Asset Tags
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: manufacturer_name
                            
                            	manufacturer's name
                            	**type**\:  str
                            
                            	**length:** 0..255
                            
                            .. attribute:: memory_size
                            
                            	Size of memory associated with       the entity where applicable
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: model_name
                            
                            	model name
                            	**type**\:  str
                            
                            	**length:** 0..255
                            
                            .. attribute:: name
                            
                            	name string for the entity
                            	**type**\:  str
                            
                            	**length:** 0..255
                            
                            .. attribute:: new_deviation_number
                            
                            	integer value for New Deviation Number 0x88
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: physical_layer_interface_module_type
                            
                            	integer value for plim type if     applicable to this entity
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: redundancystate
                            
                            	integer value for Redundancy State if     applicable to this entity
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: serial_number
                            
                            	serial number
                            	**type**\:  str
                            
                            	**length:** 0..255
                            
                            .. attribute:: software_revision
                            
                            	software revision string
                            	**type**\:  str
                            
                            	**length:** 0..255
                            
                            .. attribute:: unique_id
                            
                            	Unique id for an entity
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: unrecognized_fru
                            
                            	1 if UnrecognizedFRU and 0 for recognizedFRU
                            	**type**\:  bool
                            
                            .. attribute:: vendor_type
                            
                            	maps to the vendor OID string
                            	**type**\:  str
                            
                            	**length:** 0..255
                            
                            .. attribute:: xr_scoped
                            
                            	1 if xr scoped, 0 if not
                            	**type**\:  bool
                            
                            

                            """

                            _prefix = 'asr9k-sc-invmgr-admin-oper'
                            _revision = '2017-01-04'

                            def __init__(self):
                                self.parent = None
                                self.alias = None
                                self.asset_id_str = None
                                self.asset_identification = None
                                self.ceport = None
                                self.chip_hardware_revision = None
                                self.composite_class_code = None
                                self.description = None
                                self.environmental_monitor_path = None
                                self.firmware_revision = None
                                self.group_flag = None
                                self.hardware_revision = None
                                self.is_field_replaceable_unit = None
                                self.manufacturer_asset_tags = None
                                self.manufacturer_name = None
                                self.memory_size = None
                                self.model_name = None
                                self.name = None
                                self.new_deviation_number = None
                                self.physical_layer_interface_module_type = None
                                self.redundancystate = None
                                self.serial_number = None
                                self.software_revision = None
                                self.unique_id = None
                                self.unrecognized_fru = None
                                self.vendor_type = None
                                self.xr_scoped = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:basic-info'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.alias is not None:
                                    return True

                                if self.asset_id_str is not None:
                                    return True

                                if self.asset_identification is not None:
                                    return True

                                if self.ceport is not None:
                                    return True

                                if self.chip_hardware_revision is not None:
                                    return True

                                if self.composite_class_code is not None:
                                    return True

                                if self.description is not None:
                                    return True

                                if self.environmental_monitor_path is not None:
                                    return True

                                if self.firmware_revision is not None:
                                    return True

                                if self.group_flag is not None:
                                    return True

                                if self.hardware_revision is not None:
                                    return True

                                if self.is_field_replaceable_unit is not None:
                                    return True

                                if self.manufacturer_asset_tags is not None:
                                    return True

                                if self.manufacturer_name is not None:
                                    return True

                                if self.memory_size is not None:
                                    return True

                                if self.model_name is not None:
                                    return True

                                if self.name is not None:
                                    return True

                                if self.new_deviation_number is not None:
                                    return True

                                if self.physical_layer_interface_module_type is not None:
                                    return True

                                if self.redundancystate is not None:
                                    return True

                                if self.serial_number is not None:
                                    return True

                                if self.software_revision is not None:
                                    return True

                                if self.unique_id is not None:
                                    return True

                                if self.unrecognized_fru is not None:
                                    return True

                                if self.vendor_type is not None:
                                    return True

                                if self.xr_scoped is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper as meta
                                return meta._meta_table['Inventory.Racks.Rack.Slots.Slot.BasicAttributes.BasicInfo']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:basic-attributes'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.basic_info is not None and self.basic_info._has_data():
                                return True

                            if self.fru_info is not None and self.fru_info._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper as meta
                            return meta._meta_table['Inventory.Racks.Rack.Slots.Slot.BasicAttributes']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.number is None:
                            raise YPYModelError('Key property number is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:slot[Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:number = ' + str(self.number) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.number is not None:
                            return True

                        if self.basic_attributes is not None and self.basic_attributes._has_data():
                            return True

                        if self.cards is not None and self.cards._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper as meta
                        return meta._meta_table['Inventory.Racks.Rack.Slots.Slot']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:slots'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.slot is not None:
                        for child_ref in self.slot:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper as meta
                    return meta._meta_table['Inventory.Racks.Rack.Slots']['meta_info']


            class FanTraies(object):
                """
                Table for rack fan trays
                
                .. attribute:: fan_tray
                
                	Fan tray number
                	**type**\: list of    :py:class:`FanTray <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.Inventory.Racks.Rack.FanTraies.FanTray>`
                
                

                """

                _prefix = 'asr9k-sc-invmgr-admin-oper'
                _revision = '2017-01-04'

                def __init__(self):
                    self.parent = None
                    self.fan_tray = YList()
                    self.fan_tray.parent = self
                    self.fan_tray.name = 'fan_tray'


                class FanTray(object):
                    """
                    Fan tray number
                    
                    .. attribute:: number  <key>
                    
                    	Fan tray number
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: basic_attributes
                    
                    	Attributes
                    	**type**\:   :py:class:`BasicAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.Inventory.Racks.Rack.FanTraies.FanTray.BasicAttributes>`
                    
                    

                    """

                    _prefix = 'asr9k-sc-invmgr-admin-oper'
                    _revision = '2017-01-04'

                    def __init__(self):
                        self.parent = None
                        self.number = None
                        self.basic_attributes = Inventory.Racks.Rack.FanTraies.FanTray.BasicAttributes()
                        self.basic_attributes.parent = self


                    class BasicAttributes(object):
                        """
                        Attributes
                        
                        .. attribute:: basic_info
                        
                        	Inventory information
                        	**type**\:   :py:class:`BasicInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.Inventory.Racks.Rack.FanTraies.FanTray.BasicAttributes.BasicInfo>`
                        
                        

                        """

                        _prefix = 'asr9k-sc-invmgr-admin-oper'
                        _revision = '2017-01-04'

                        def __init__(self):
                            self.parent = None
                            self.basic_info = Inventory.Racks.Rack.FanTraies.FanTray.BasicAttributes.BasicInfo()
                            self.basic_info.parent = self


                        class BasicInfo(object):
                            """
                            Inventory information
                            
                            .. attribute:: alias
                            
                            	useful for storing an entity alias 
                            	**type**\:  str
                            
                            	**length:** 0..255
                            
                            .. attribute:: asset_id_str
                            
                            	asset Identification string
                            	**type**\:  str
                            
                            	**length:** 0..255
                            
                            .. attribute:: asset_identification
                            
                            	asset Identification
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: ceport
                            
                            	1 if ce port found, 0 if not
                            	**type**\:  bool
                            
                            .. attribute:: chip_hardware_revision
                            
                            	chip module hw revision string
                            	**type**\:  str
                            
                            	**length:** 0..255
                            
                            .. attribute:: composite_class_code
                            
                            	Major&minor class of the entity
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: description
                            
                            	describes in user\-readable terms       what the entity in question does
                            	**type**\:  str
                            
                            	**length:** 0..255
                            
                            .. attribute:: environmental_monitor_path
                            
                            	sysdb name of sensor in the envmon EDM
                            	**type**\:  str
                            
                            	**length:** 0..255
                            
                            .. attribute:: firmware_revision
                            
                            	firmware revision string
                            	**type**\:  str
                            
                            	**length:** 0..255
                            
                            .. attribute:: group_flag
                            
                            	indicates if this entity is group       or not
                            	**type**\:  bool
                            
                            .. attribute:: hardware_revision
                            
                            	hw revision string
                            	**type**\:  str
                            
                            	**length:** 0..255
                            
                            .. attribute:: is_field_replaceable_unit
                            
                            	1 if Field Replaceable Unit 0, if not
                            	**type**\:  bool
                            
                            .. attribute:: manufacturer_asset_tags
                            
                            	Manufacture Asset Tags
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: manufacturer_name
                            
                            	manufacturer's name
                            	**type**\:  str
                            
                            	**length:** 0..255
                            
                            .. attribute:: memory_size
                            
                            	Size of memory associated with       the entity where applicable
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: model_name
                            
                            	model name
                            	**type**\:  str
                            
                            	**length:** 0..255
                            
                            .. attribute:: name
                            
                            	name string for the entity
                            	**type**\:  str
                            
                            	**length:** 0..255
                            
                            .. attribute:: new_deviation_number
                            
                            	integer value for New Deviation Number 0x88
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: physical_layer_interface_module_type
                            
                            	integer value for plim type if     applicable to this entity
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: redundancystate
                            
                            	integer value for Redundancy State if     applicable to this entity
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: serial_number
                            
                            	serial number
                            	**type**\:  str
                            
                            	**length:** 0..255
                            
                            .. attribute:: software_revision
                            
                            	software revision string
                            	**type**\:  str
                            
                            	**length:** 0..255
                            
                            .. attribute:: unique_id
                            
                            	Unique id for an entity
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: unrecognized_fru
                            
                            	1 if UnrecognizedFRU and 0 for recognizedFRU
                            	**type**\:  bool
                            
                            .. attribute:: vendor_type
                            
                            	maps to the vendor OID string
                            	**type**\:  str
                            
                            	**length:** 0..255
                            
                            .. attribute:: xr_scoped
                            
                            	1 if xr scoped, 0 if not
                            	**type**\:  bool
                            
                            

                            """

                            _prefix = 'asr9k-sc-invmgr-admin-oper'
                            _revision = '2017-01-04'

                            def __init__(self):
                                self.parent = None
                                self.alias = None
                                self.asset_id_str = None
                                self.asset_identification = None
                                self.ceport = None
                                self.chip_hardware_revision = None
                                self.composite_class_code = None
                                self.description = None
                                self.environmental_monitor_path = None
                                self.firmware_revision = None
                                self.group_flag = None
                                self.hardware_revision = None
                                self.is_field_replaceable_unit = None
                                self.manufacturer_asset_tags = None
                                self.manufacturer_name = None
                                self.memory_size = None
                                self.model_name = None
                                self.name = None
                                self.new_deviation_number = None
                                self.physical_layer_interface_module_type = None
                                self.redundancystate = None
                                self.serial_number = None
                                self.software_revision = None
                                self.unique_id = None
                                self.unrecognized_fru = None
                                self.vendor_type = None
                                self.xr_scoped = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:basic-info'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.alias is not None:
                                    return True

                                if self.asset_id_str is not None:
                                    return True

                                if self.asset_identification is not None:
                                    return True

                                if self.ceport is not None:
                                    return True

                                if self.chip_hardware_revision is not None:
                                    return True

                                if self.composite_class_code is not None:
                                    return True

                                if self.description is not None:
                                    return True

                                if self.environmental_monitor_path is not None:
                                    return True

                                if self.firmware_revision is not None:
                                    return True

                                if self.group_flag is not None:
                                    return True

                                if self.hardware_revision is not None:
                                    return True

                                if self.is_field_replaceable_unit is not None:
                                    return True

                                if self.manufacturer_asset_tags is not None:
                                    return True

                                if self.manufacturer_name is not None:
                                    return True

                                if self.memory_size is not None:
                                    return True

                                if self.model_name is not None:
                                    return True

                                if self.name is not None:
                                    return True

                                if self.new_deviation_number is not None:
                                    return True

                                if self.physical_layer_interface_module_type is not None:
                                    return True

                                if self.redundancystate is not None:
                                    return True

                                if self.serial_number is not None:
                                    return True

                                if self.software_revision is not None:
                                    return True

                                if self.unique_id is not None:
                                    return True

                                if self.unrecognized_fru is not None:
                                    return True

                                if self.vendor_type is not None:
                                    return True

                                if self.xr_scoped is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper as meta
                                return meta._meta_table['Inventory.Racks.Rack.FanTraies.FanTray.BasicAttributes.BasicInfo']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:basic-attributes'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.basic_info is not None and self.basic_info._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper as meta
                            return meta._meta_table['Inventory.Racks.Rack.FanTraies.FanTray.BasicAttributes']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.number is None:
                            raise YPYModelError('Key property number is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:fan-tray[Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:number = ' + str(self.number) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.number is not None:
                            return True

                        if self.basic_attributes is not None and self.basic_attributes._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper as meta
                        return meta._meta_table['Inventory.Racks.Rack.FanTraies.FanTray']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:fan-traies'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.fan_tray is not None:
                        for child_ref in self.fan_tray:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper as meta
                    return meta._meta_table['Inventory.Racks.Rack.FanTraies']['meta_info']


            class PowerSupplyZones(object):
                """
                Table for defining rack power supply zones 
                
                .. attribute:: power_supply_zone
                
                	Power Supply Zone number
                	**type**\: list of    :py:class:`PowerSupplyZone <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.Inventory.Racks.Rack.PowerSupplyZones.PowerSupplyZone>`
                
                

                """

                _prefix = 'asr9k-sc-invmgr-admin-oper'
                _revision = '2017-01-04'

                def __init__(self):
                    self.parent = None
                    self.power_supply_zone = YList()
                    self.power_supply_zone.parent = self
                    self.power_supply_zone.name = 'power_supply_zone'


                class PowerSupplyZone(object):
                    """
                    Power Supply Zone number
                    
                    .. attribute:: number  <key>
                    
                    	Power Zone number
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: power_supply_zone_attributes
                    
                    	Power suppy zone attributes 
                    	**type**\:   :py:class:`PowerSupplyZoneAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.Inventory.Racks.Rack.PowerSupplyZones.PowerSupplyZone.PowerSupplyZoneAttributes>`
                    
                    

                    """

                    _prefix = 'asr9k-sc-invmgr-admin-oper'
                    _revision = '2017-01-04'

                    def __init__(self):
                        self.parent = None
                        self.number = None
                        self.power_supply_zone_attributes = Inventory.Racks.Rack.PowerSupplyZones.PowerSupplyZone.PowerSupplyZoneAttributes()
                        self.power_supply_zone_attributes.parent = self


                    class PowerSupplyZoneAttributes(object):
                        """
                        Power suppy zone attributes 
                        
                        .. attribute:: power_supply_group_info
                        
                        	Power supply group information
                        	**type**\:   :py:class:`PowerSupplyGroupInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.Inventory.Racks.Rack.PowerSupplyZones.PowerSupplyZone.PowerSupplyZoneAttributes.PowerSupplyGroupInfo>`
                        
                        

                        """

                        _prefix = 'asr9k-sc-invmgr-admin-oper'
                        _revision = '2017-01-04'

                        def __init__(self):
                            self.parent = None
                            self.power_supply_group_info = Inventory.Racks.Rack.PowerSupplyZones.PowerSupplyZone.PowerSupplyZoneAttributes.PowerSupplyGroupInfo()
                            self.power_supply_group_info.parent = self


                        class PowerSupplyGroupInfo(object):
                            """
                            Power supply group information
                            
                            .. attribute:: power_group_available_current
                            
                            	available current
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: power_group_drawn_current
                            
                            	drawn current
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: power_group_power_units
                            
                            	power units
                            	**type**\:  str
                            
                            .. attribute:: power_group_redundancy_mode
                            
                            	redundancy mode
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            

                            """

                            _prefix = 'asr9k-sc-invmgr-admin-oper'
                            _revision = '2017-01-04'

                            def __init__(self):
                                self.parent = None
                                self.power_group_available_current = None
                                self.power_group_drawn_current = None
                                self.power_group_power_units = None
                                self.power_group_redundancy_mode = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:power-supply-group-info'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.power_group_available_current is not None:
                                    return True

                                if self.power_group_drawn_current is not None:
                                    return True

                                if self.power_group_power_units is not None:
                                    return True

                                if self.power_group_redundancy_mode is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper as meta
                                return meta._meta_table['Inventory.Racks.Rack.PowerSupplyZones.PowerSupplyZone.PowerSupplyZoneAttributes.PowerSupplyGroupInfo']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:power-supply-zone-attributes'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.power_supply_group_info is not None and self.power_supply_group_info._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper as meta
                            return meta._meta_table['Inventory.Racks.Rack.PowerSupplyZones.PowerSupplyZone.PowerSupplyZoneAttributes']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.number is None:
                            raise YPYModelError('Key property number is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:power-supply-zone[Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:number = ' + str(self.number) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.number is not None:
                            return True

                        if self.power_supply_zone_attributes is not None and self.power_supply_zone_attributes._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper as meta
                        return meta._meta_table['Inventory.Racks.Rack.PowerSupplyZones.PowerSupplyZone']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:power-supply-zones'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.power_supply_zone is not None:
                        for child_ref in self.power_supply_zone:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper as meta
                    return meta._meta_table['Inventory.Racks.Rack.PowerSupplyZones']['meta_info']


            class BasicAttributes(object):
                """
                Attributes
                
                .. attribute:: basic_info
                
                	Inventory information
                	**type**\:   :py:class:`BasicInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.Inventory.Racks.Rack.BasicAttributes.BasicInfo>`
                
                

                """

                _prefix = 'asr9k-sc-invmgr-admin-oper'
                _revision = '2017-01-04'

                def __init__(self):
                    self.parent = None
                    self.basic_info = Inventory.Racks.Rack.BasicAttributes.BasicInfo()
                    self.basic_info.parent = self


                class BasicInfo(object):
                    """
                    Inventory information
                    
                    .. attribute:: alias
                    
                    	useful for storing an entity alias 
                    	**type**\:  str
                    
                    	**length:** 0..255
                    
                    .. attribute:: asset_id_str
                    
                    	asset Identification string
                    	**type**\:  str
                    
                    	**length:** 0..255
                    
                    .. attribute:: asset_identification
                    
                    	asset Identification
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: ceport
                    
                    	1 if ce port found, 0 if not
                    	**type**\:  bool
                    
                    .. attribute:: chip_hardware_revision
                    
                    	chip module hw revision string
                    	**type**\:  str
                    
                    	**length:** 0..255
                    
                    .. attribute:: composite_class_code
                    
                    	Major&minor class of the entity
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: description
                    
                    	describes in user\-readable terms       what the entity in question does
                    	**type**\:  str
                    
                    	**length:** 0..255
                    
                    .. attribute:: environmental_monitor_path
                    
                    	sysdb name of sensor in the envmon EDM
                    	**type**\:  str
                    
                    	**length:** 0..255
                    
                    .. attribute:: firmware_revision
                    
                    	firmware revision string
                    	**type**\:  str
                    
                    	**length:** 0..255
                    
                    .. attribute:: group_flag
                    
                    	indicates if this entity is group       or not
                    	**type**\:  bool
                    
                    .. attribute:: hardware_revision
                    
                    	hw revision string
                    	**type**\:  str
                    
                    	**length:** 0..255
                    
                    .. attribute:: is_field_replaceable_unit
                    
                    	1 if Field Replaceable Unit 0, if not
                    	**type**\:  bool
                    
                    .. attribute:: manufacturer_asset_tags
                    
                    	Manufacture Asset Tags
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: manufacturer_name
                    
                    	manufacturer's name
                    	**type**\:  str
                    
                    	**length:** 0..255
                    
                    .. attribute:: memory_size
                    
                    	Size of memory associated with       the entity where applicable
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: model_name
                    
                    	model name
                    	**type**\:  str
                    
                    	**length:** 0..255
                    
                    .. attribute:: name
                    
                    	name string for the entity
                    	**type**\:  str
                    
                    	**length:** 0..255
                    
                    .. attribute:: new_deviation_number
                    
                    	integer value for New Deviation Number 0x88
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: physical_layer_interface_module_type
                    
                    	integer value for plim type if     applicable to this entity
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: redundancystate
                    
                    	integer value for Redundancy State if     applicable to this entity
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: serial_number
                    
                    	serial number
                    	**type**\:  str
                    
                    	**length:** 0..255
                    
                    .. attribute:: software_revision
                    
                    	software revision string
                    	**type**\:  str
                    
                    	**length:** 0..255
                    
                    .. attribute:: unique_id
                    
                    	Unique id for an entity
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: unrecognized_fru
                    
                    	1 if UnrecognizedFRU and 0 for recognizedFRU
                    	**type**\:  bool
                    
                    .. attribute:: vendor_type
                    
                    	maps to the vendor OID string
                    	**type**\:  str
                    
                    	**length:** 0..255
                    
                    .. attribute:: xr_scoped
                    
                    	1 if xr scoped, 0 if not
                    	**type**\:  bool
                    
                    

                    """

                    _prefix = 'asr9k-sc-invmgr-admin-oper'
                    _revision = '2017-01-04'

                    def __init__(self):
                        self.parent = None
                        self.alias = None
                        self.asset_id_str = None
                        self.asset_identification = None
                        self.ceport = None
                        self.chip_hardware_revision = None
                        self.composite_class_code = None
                        self.description = None
                        self.environmental_monitor_path = None
                        self.firmware_revision = None
                        self.group_flag = None
                        self.hardware_revision = None
                        self.is_field_replaceable_unit = None
                        self.manufacturer_asset_tags = None
                        self.manufacturer_name = None
                        self.memory_size = None
                        self.model_name = None
                        self.name = None
                        self.new_deviation_number = None
                        self.physical_layer_interface_module_type = None
                        self.redundancystate = None
                        self.serial_number = None
                        self.software_revision = None
                        self.unique_id = None
                        self.unrecognized_fru = None
                        self.vendor_type = None
                        self.xr_scoped = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:basic-info'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.alias is not None:
                            return True

                        if self.asset_id_str is not None:
                            return True

                        if self.asset_identification is not None:
                            return True

                        if self.ceport is not None:
                            return True

                        if self.chip_hardware_revision is not None:
                            return True

                        if self.composite_class_code is not None:
                            return True

                        if self.description is not None:
                            return True

                        if self.environmental_monitor_path is not None:
                            return True

                        if self.firmware_revision is not None:
                            return True

                        if self.group_flag is not None:
                            return True

                        if self.hardware_revision is not None:
                            return True

                        if self.is_field_replaceable_unit is not None:
                            return True

                        if self.manufacturer_asset_tags is not None:
                            return True

                        if self.manufacturer_name is not None:
                            return True

                        if self.memory_size is not None:
                            return True

                        if self.model_name is not None:
                            return True

                        if self.name is not None:
                            return True

                        if self.new_deviation_number is not None:
                            return True

                        if self.physical_layer_interface_module_type is not None:
                            return True

                        if self.redundancystate is not None:
                            return True

                        if self.serial_number is not None:
                            return True

                        if self.software_revision is not None:
                            return True

                        if self.unique_id is not None:
                            return True

                        if self.unrecognized_fru is not None:
                            return True

                        if self.vendor_type is not None:
                            return True

                        if self.xr_scoped is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper as meta
                        return meta._meta_table['Inventory.Racks.Rack.BasicAttributes.BasicInfo']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:basic-attributes'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.basic_info is not None and self.basic_info._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper as meta
                    return meta._meta_table['Inventory.Racks.Rack.BasicAttributes']['meta_info']

            @property
            def _common_path(self):
                if self.number is None:
                    raise YPYModelError('Key property number is None')

                return '/Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:inventory/Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:racks/Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:rack[Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:number = ' + str(self.number) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.number is not None:
                    return True

                if self.basic_attributes is not None and self.basic_attributes._has_data():
                    return True

                if self.fan_traies is not None and self.fan_traies._has_data():
                    return True

                if self.power_supply_shelfs is not None and self.power_supply_shelfs._has_data():
                    return True

                if self.power_supply_zones is not None and self.power_supply_zones._has_data():
                    return True

                if self.slots is not None and self.slots._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper as meta
                return meta._meta_table['Inventory.Racks.Rack']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:inventory/Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:racks'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.rack is not None:
                for child_ref in self.rack:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper as meta
            return meta._meta_table['Inventory.Racks']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:inventory'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.racks is not None and self.racks._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper as meta
        return meta._meta_table['Inventory']['meta_info']


