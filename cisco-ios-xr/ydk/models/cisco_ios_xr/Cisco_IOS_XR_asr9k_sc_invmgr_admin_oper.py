""" Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR asr9k\-sc\-invmgr package
admin\-plane operational data.

This module contains definitions
for the following management objects\:
  inventory\: Inventory operational data

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class CardResetReason(Enum):
    """
    CardResetReason

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
    Inventory operational data
    
    .. attribute:: racks
    
    	Table of racks
    	**type**\:   :py:class:`Racks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.Inventory.Racks>`
    
    

    """

    _prefix = 'asr9k-sc-invmgr-admin-oper'
    _revision = '2017-01-04'

    def __init__(self):
        super(Inventory, self).__init__()
        self._top_entity = None

        self.yang_name = "inventory"
        self.yang_parent_name = "Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"racks" : ("racks", Inventory.Racks)}
        self._child_list_classes = {}

        self.racks = Inventory.Racks()
        self.racks.parent = self
        self._children_name_map["racks"] = "racks"
        self._children_yang_names.add("racks")
        self._segment_path = lambda: "Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:inventory"


    class Racks(Entity):
        """
        Table of racks
        
        .. attribute:: rack
        
        	Rack number
        	**type**\: list of    :py:class:`Rack <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.Inventory.Racks.Rack>`
        
        

        """

        _prefix = 'asr9k-sc-invmgr-admin-oper'
        _revision = '2017-01-04'

        def __init__(self):
            super(Inventory.Racks, self).__init__()

            self.yang_name = "racks"
            self.yang_parent_name = "inventory"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"rack" : ("rack", Inventory.Racks.Rack)}

            self.rack = YList(self)
            self._segment_path = lambda: "racks"
            self._absolute_path = lambda: "Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:inventory/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Inventory.Racks, [], name, value)


        class Rack(Entity):
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
                super(Inventory.Racks.Rack, self).__init__()

                self.yang_name = "rack"
                self.yang_parent_name = "racks"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"basic-attributes" : ("basic_attributes", Inventory.Racks.Rack.BasicAttributes), "fan-traies" : ("fan_traies", Inventory.Racks.Rack.FanTraies), "power-supply-shelfs" : ("power_supply_shelfs", Inventory.Racks.Rack.PowerSupplyShelfs), "power-supply-zones" : ("power_supply_zones", Inventory.Racks.Rack.PowerSupplyZones), "slots" : ("slots", Inventory.Racks.Rack.Slots)}
                self._child_list_classes = {}

                self.number = YLeaf(YType.int32, "number")

                self.basic_attributes = Inventory.Racks.Rack.BasicAttributes()
                self.basic_attributes.parent = self
                self._children_name_map["basic_attributes"] = "basic-attributes"
                self._children_yang_names.add("basic-attributes")

                self.fan_traies = Inventory.Racks.Rack.FanTraies()
                self.fan_traies.parent = self
                self._children_name_map["fan_traies"] = "fan-traies"
                self._children_yang_names.add("fan-traies")

                self.power_supply_shelfs = Inventory.Racks.Rack.PowerSupplyShelfs()
                self.power_supply_shelfs.parent = self
                self._children_name_map["power_supply_shelfs"] = "power-supply-shelfs"
                self._children_yang_names.add("power-supply-shelfs")

                self.power_supply_zones = Inventory.Racks.Rack.PowerSupplyZones()
                self.power_supply_zones.parent = self
                self._children_name_map["power_supply_zones"] = "power-supply-zones"
                self._children_yang_names.add("power-supply-zones")

                self.slots = Inventory.Racks.Rack.Slots()
                self.slots.parent = self
                self._children_name_map["slots"] = "slots"
                self._children_yang_names.add("slots")
                self._segment_path = lambda: "rack" + "[number='" + self.number.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper:inventory/racks/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Inventory.Racks.Rack, ['number'], name, value)


            class BasicAttributes(Entity):
                """
                Attributes
                
                .. attribute:: basic_info
                
                	Inventory information
                	**type**\:   :py:class:`BasicInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.Inventory.Racks.Rack.BasicAttributes.BasicInfo>`
                
                

                """

                _prefix = 'asr9k-sc-invmgr-admin-oper'
                _revision = '2017-01-04'

                def __init__(self):
                    super(Inventory.Racks.Rack.BasicAttributes, self).__init__()

                    self.yang_name = "basic-attributes"
                    self.yang_parent_name = "rack"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"basic-info" : ("basic_info", Inventory.Racks.Rack.BasicAttributes.BasicInfo)}
                    self._child_list_classes = {}

                    self.basic_info = Inventory.Racks.Rack.BasicAttributes.BasicInfo()
                    self.basic_info.parent = self
                    self._children_name_map["basic_info"] = "basic-info"
                    self._children_yang_names.add("basic-info")
                    self._segment_path = lambda: "basic-attributes"


                class BasicInfo(Entity):
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
                        super(Inventory.Racks.Rack.BasicAttributes.BasicInfo, self).__init__()

                        self.yang_name = "basic-info"
                        self.yang_parent_name = "basic-attributes"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.alias = YLeaf(YType.str, "alias")

                        self.asset_id_str = YLeaf(YType.str, "asset-id-str")

                        self.asset_identification = YLeaf(YType.int32, "asset-identification")

                        self.ceport = YLeaf(YType.boolean, "ceport")

                        self.chip_hardware_revision = YLeaf(YType.str, "chip-hardware-revision")

                        self.composite_class_code = YLeaf(YType.int32, "composite-class-code")

                        self.description = YLeaf(YType.str, "description")

                        self.environmental_monitor_path = YLeaf(YType.str, "environmental-monitor-path")

                        self.firmware_revision = YLeaf(YType.str, "firmware-revision")

                        self.group_flag = YLeaf(YType.boolean, "group-flag")

                        self.hardware_revision = YLeaf(YType.str, "hardware-revision")

                        self.is_field_replaceable_unit = YLeaf(YType.boolean, "is-field-replaceable-unit")

                        self.manufacturer_asset_tags = YLeaf(YType.int32, "manufacturer-asset-tags")

                        self.manufacturer_name = YLeaf(YType.str, "manufacturer-name")

                        self.memory_size = YLeaf(YType.int32, "memory-size")

                        self.model_name = YLeaf(YType.str, "model-name")

                        self.name = YLeaf(YType.str, "name")

                        self.new_deviation_number = YLeaf(YType.int32, "new-deviation-number")

                        self.physical_layer_interface_module_type = YLeaf(YType.int32, "physical-layer-interface-module-type")

                        self.redundancystate = YLeaf(YType.int32, "redundancystate")

                        self.serial_number = YLeaf(YType.str, "serial-number")

                        self.software_revision = YLeaf(YType.str, "software-revision")

                        self.unique_id = YLeaf(YType.int32, "unique-id")

                        self.unrecognized_fru = YLeaf(YType.boolean, "unrecognized-fru")

                        self.vendor_type = YLeaf(YType.str, "vendor-type")

                        self.xr_scoped = YLeaf(YType.boolean, "xr-scoped")
                        self._segment_path = lambda: "basic-info"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Inventory.Racks.Rack.BasicAttributes.BasicInfo, ['alias', 'asset_id_str', 'asset_identification', 'ceport', 'chip_hardware_revision', 'composite_class_code', 'description', 'environmental_monitor_path', 'firmware_revision', 'group_flag', 'hardware_revision', 'is_field_replaceable_unit', 'manufacturer_asset_tags', 'manufacturer_name', 'memory_size', 'model_name', 'name', 'new_deviation_number', 'physical_layer_interface_module_type', 'redundancystate', 'serial_number', 'software_revision', 'unique_id', 'unrecognized_fru', 'vendor_type', 'xr_scoped'], name, value)


            class FanTraies(Entity):
                """
                Table for rack fan trays
                
                .. attribute:: fan_tray
                
                	Fan tray number
                	**type**\: list of    :py:class:`FanTray <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.Inventory.Racks.Rack.FanTraies.FanTray>`
                
                

                """

                _prefix = 'asr9k-sc-invmgr-admin-oper'
                _revision = '2017-01-04'

                def __init__(self):
                    super(Inventory.Racks.Rack.FanTraies, self).__init__()

                    self.yang_name = "fan-traies"
                    self.yang_parent_name = "rack"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"fan-tray" : ("fan_tray", Inventory.Racks.Rack.FanTraies.FanTray)}

                    self.fan_tray = YList(self)
                    self._segment_path = lambda: "fan-traies"

                def __setattr__(self, name, value):
                    self._perform_setattr(Inventory.Racks.Rack.FanTraies, [], name, value)


                class FanTray(Entity):
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
                        super(Inventory.Racks.Rack.FanTraies.FanTray, self).__init__()

                        self.yang_name = "fan-tray"
                        self.yang_parent_name = "fan-traies"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"basic-attributes" : ("basic_attributes", Inventory.Racks.Rack.FanTraies.FanTray.BasicAttributes)}
                        self._child_list_classes = {}

                        self.number = YLeaf(YType.int32, "number")

                        self.basic_attributes = Inventory.Racks.Rack.FanTraies.FanTray.BasicAttributes()
                        self.basic_attributes.parent = self
                        self._children_name_map["basic_attributes"] = "basic-attributes"
                        self._children_yang_names.add("basic-attributes")
                        self._segment_path = lambda: "fan-tray" + "[number='" + self.number.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Inventory.Racks.Rack.FanTraies.FanTray, ['number'], name, value)


                    class BasicAttributes(Entity):
                        """
                        Attributes
                        
                        .. attribute:: basic_info
                        
                        	Inventory information
                        	**type**\:   :py:class:`BasicInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.Inventory.Racks.Rack.FanTraies.FanTray.BasicAttributes.BasicInfo>`
                        
                        

                        """

                        _prefix = 'asr9k-sc-invmgr-admin-oper'
                        _revision = '2017-01-04'

                        def __init__(self):
                            super(Inventory.Racks.Rack.FanTraies.FanTray.BasicAttributes, self).__init__()

                            self.yang_name = "basic-attributes"
                            self.yang_parent_name = "fan-tray"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"basic-info" : ("basic_info", Inventory.Racks.Rack.FanTraies.FanTray.BasicAttributes.BasicInfo)}
                            self._child_list_classes = {}

                            self.basic_info = Inventory.Racks.Rack.FanTraies.FanTray.BasicAttributes.BasicInfo()
                            self.basic_info.parent = self
                            self._children_name_map["basic_info"] = "basic-info"
                            self._children_yang_names.add("basic-info")
                            self._segment_path = lambda: "basic-attributes"


                        class BasicInfo(Entity):
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
                                super(Inventory.Racks.Rack.FanTraies.FanTray.BasicAttributes.BasicInfo, self).__init__()

                                self.yang_name = "basic-info"
                                self.yang_parent_name = "basic-attributes"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.alias = YLeaf(YType.str, "alias")

                                self.asset_id_str = YLeaf(YType.str, "asset-id-str")

                                self.asset_identification = YLeaf(YType.int32, "asset-identification")

                                self.ceport = YLeaf(YType.boolean, "ceport")

                                self.chip_hardware_revision = YLeaf(YType.str, "chip-hardware-revision")

                                self.composite_class_code = YLeaf(YType.int32, "composite-class-code")

                                self.description = YLeaf(YType.str, "description")

                                self.environmental_monitor_path = YLeaf(YType.str, "environmental-monitor-path")

                                self.firmware_revision = YLeaf(YType.str, "firmware-revision")

                                self.group_flag = YLeaf(YType.boolean, "group-flag")

                                self.hardware_revision = YLeaf(YType.str, "hardware-revision")

                                self.is_field_replaceable_unit = YLeaf(YType.boolean, "is-field-replaceable-unit")

                                self.manufacturer_asset_tags = YLeaf(YType.int32, "manufacturer-asset-tags")

                                self.manufacturer_name = YLeaf(YType.str, "manufacturer-name")

                                self.memory_size = YLeaf(YType.int32, "memory-size")

                                self.model_name = YLeaf(YType.str, "model-name")

                                self.name = YLeaf(YType.str, "name")

                                self.new_deviation_number = YLeaf(YType.int32, "new-deviation-number")

                                self.physical_layer_interface_module_type = YLeaf(YType.int32, "physical-layer-interface-module-type")

                                self.redundancystate = YLeaf(YType.int32, "redundancystate")

                                self.serial_number = YLeaf(YType.str, "serial-number")

                                self.software_revision = YLeaf(YType.str, "software-revision")

                                self.unique_id = YLeaf(YType.int32, "unique-id")

                                self.unrecognized_fru = YLeaf(YType.boolean, "unrecognized-fru")

                                self.vendor_type = YLeaf(YType.str, "vendor-type")

                                self.xr_scoped = YLeaf(YType.boolean, "xr-scoped")
                                self._segment_path = lambda: "basic-info"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Inventory.Racks.Rack.FanTraies.FanTray.BasicAttributes.BasicInfo, ['alias', 'asset_id_str', 'asset_identification', 'ceport', 'chip_hardware_revision', 'composite_class_code', 'description', 'environmental_monitor_path', 'firmware_revision', 'group_flag', 'hardware_revision', 'is_field_replaceable_unit', 'manufacturer_asset_tags', 'manufacturer_name', 'memory_size', 'model_name', 'name', 'new_deviation_number', 'physical_layer_interface_module_type', 'redundancystate', 'serial_number', 'software_revision', 'unique_id', 'unrecognized_fru', 'vendor_type', 'xr_scoped'], name, value)


            class PowerSupplyShelfs(Entity):
                """
                Table for rack power supply shelves 
                
                .. attribute:: power_supply_shelf
                
                	Power Supply Shelf number
                	**type**\: list of    :py:class:`PowerSupplyShelf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.Inventory.Racks.Rack.PowerSupplyShelfs.PowerSupplyShelf>`
                
                

                """

                _prefix = 'asr9k-sc-invmgr-admin-oper'
                _revision = '2017-01-04'

                def __init__(self):
                    super(Inventory.Racks.Rack.PowerSupplyShelfs, self).__init__()

                    self.yang_name = "power-supply-shelfs"
                    self.yang_parent_name = "rack"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"power-supply-shelf" : ("power_supply_shelf", Inventory.Racks.Rack.PowerSupplyShelfs.PowerSupplyShelf)}

                    self.power_supply_shelf = YList(self)
                    self._segment_path = lambda: "power-supply-shelfs"

                def __setattr__(self, name, value):
                    self._perform_setattr(Inventory.Racks.Rack.PowerSupplyShelfs, [], name, value)


                class PowerSupplyShelf(Entity):
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
                        super(Inventory.Racks.Rack.PowerSupplyShelfs.PowerSupplyShelf, self).__init__()

                        self.yang_name = "power-supply-shelf"
                        self.yang_parent_name = "power-supply-shelfs"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"basic-attributes" : ("basic_attributes", Inventory.Racks.Rack.PowerSupplyShelfs.PowerSupplyShelf.BasicAttributes)}
                        self._child_list_classes = {}

                        self.number = YLeaf(YType.int32, "number")

                        self.basic_attributes = Inventory.Racks.Rack.PowerSupplyShelfs.PowerSupplyShelf.BasicAttributes()
                        self.basic_attributes.parent = self
                        self._children_name_map["basic_attributes"] = "basic-attributes"
                        self._children_yang_names.add("basic-attributes")
                        self._segment_path = lambda: "power-supply-shelf" + "[number='" + self.number.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Inventory.Racks.Rack.PowerSupplyShelfs.PowerSupplyShelf, ['number'], name, value)


                    class BasicAttributes(Entity):
                        """
                        Attributes
                        
                        .. attribute:: basic_info
                        
                        	Inventory information
                        	**type**\:   :py:class:`BasicInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.Inventory.Racks.Rack.PowerSupplyShelfs.PowerSupplyShelf.BasicAttributes.BasicInfo>`
                        
                        

                        """

                        _prefix = 'asr9k-sc-invmgr-admin-oper'
                        _revision = '2017-01-04'

                        def __init__(self):
                            super(Inventory.Racks.Rack.PowerSupplyShelfs.PowerSupplyShelf.BasicAttributes, self).__init__()

                            self.yang_name = "basic-attributes"
                            self.yang_parent_name = "power-supply-shelf"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"basic-info" : ("basic_info", Inventory.Racks.Rack.PowerSupplyShelfs.PowerSupplyShelf.BasicAttributes.BasicInfo)}
                            self._child_list_classes = {}

                            self.basic_info = Inventory.Racks.Rack.PowerSupplyShelfs.PowerSupplyShelf.BasicAttributes.BasicInfo()
                            self.basic_info.parent = self
                            self._children_name_map["basic_info"] = "basic-info"
                            self._children_yang_names.add("basic-info")
                            self._segment_path = lambda: "basic-attributes"


                        class BasicInfo(Entity):
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
                                super(Inventory.Racks.Rack.PowerSupplyShelfs.PowerSupplyShelf.BasicAttributes.BasicInfo, self).__init__()

                                self.yang_name = "basic-info"
                                self.yang_parent_name = "basic-attributes"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.alias = YLeaf(YType.str, "alias")

                                self.asset_id_str = YLeaf(YType.str, "asset-id-str")

                                self.asset_identification = YLeaf(YType.int32, "asset-identification")

                                self.ceport = YLeaf(YType.boolean, "ceport")

                                self.chip_hardware_revision = YLeaf(YType.str, "chip-hardware-revision")

                                self.composite_class_code = YLeaf(YType.int32, "composite-class-code")

                                self.description = YLeaf(YType.str, "description")

                                self.environmental_monitor_path = YLeaf(YType.str, "environmental-monitor-path")

                                self.firmware_revision = YLeaf(YType.str, "firmware-revision")

                                self.group_flag = YLeaf(YType.boolean, "group-flag")

                                self.hardware_revision = YLeaf(YType.str, "hardware-revision")

                                self.is_field_replaceable_unit = YLeaf(YType.boolean, "is-field-replaceable-unit")

                                self.manufacturer_asset_tags = YLeaf(YType.int32, "manufacturer-asset-tags")

                                self.manufacturer_name = YLeaf(YType.str, "manufacturer-name")

                                self.memory_size = YLeaf(YType.int32, "memory-size")

                                self.model_name = YLeaf(YType.str, "model-name")

                                self.name = YLeaf(YType.str, "name")

                                self.new_deviation_number = YLeaf(YType.int32, "new-deviation-number")

                                self.physical_layer_interface_module_type = YLeaf(YType.int32, "physical-layer-interface-module-type")

                                self.redundancystate = YLeaf(YType.int32, "redundancystate")

                                self.serial_number = YLeaf(YType.str, "serial-number")

                                self.software_revision = YLeaf(YType.str, "software-revision")

                                self.unique_id = YLeaf(YType.int32, "unique-id")

                                self.unrecognized_fru = YLeaf(YType.boolean, "unrecognized-fru")

                                self.vendor_type = YLeaf(YType.str, "vendor-type")

                                self.xr_scoped = YLeaf(YType.boolean, "xr-scoped")
                                self._segment_path = lambda: "basic-info"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Inventory.Racks.Rack.PowerSupplyShelfs.PowerSupplyShelf.BasicAttributes.BasicInfo, ['alias', 'asset_id_str', 'asset_identification', 'ceport', 'chip_hardware_revision', 'composite_class_code', 'description', 'environmental_monitor_path', 'firmware_revision', 'group_flag', 'hardware_revision', 'is_field_replaceable_unit', 'manufacturer_asset_tags', 'manufacturer_name', 'memory_size', 'model_name', 'name', 'new_deviation_number', 'physical_layer_interface_module_type', 'redundancystate', 'serial_number', 'software_revision', 'unique_id', 'unrecognized_fru', 'vendor_type', 'xr_scoped'], name, value)


            class PowerSupplyZones(Entity):
                """
                Table for defining rack power supply zones 
                
                .. attribute:: power_supply_zone
                
                	Power Supply Zone number
                	**type**\: list of    :py:class:`PowerSupplyZone <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.Inventory.Racks.Rack.PowerSupplyZones.PowerSupplyZone>`
                
                

                """

                _prefix = 'asr9k-sc-invmgr-admin-oper'
                _revision = '2017-01-04'

                def __init__(self):
                    super(Inventory.Racks.Rack.PowerSupplyZones, self).__init__()

                    self.yang_name = "power-supply-zones"
                    self.yang_parent_name = "rack"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"power-supply-zone" : ("power_supply_zone", Inventory.Racks.Rack.PowerSupplyZones.PowerSupplyZone)}

                    self.power_supply_zone = YList(self)
                    self._segment_path = lambda: "power-supply-zones"

                def __setattr__(self, name, value):
                    self._perform_setattr(Inventory.Racks.Rack.PowerSupplyZones, [], name, value)


                class PowerSupplyZone(Entity):
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
                        super(Inventory.Racks.Rack.PowerSupplyZones.PowerSupplyZone, self).__init__()

                        self.yang_name = "power-supply-zone"
                        self.yang_parent_name = "power-supply-zones"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"power-supply-zone-attributes" : ("power_supply_zone_attributes", Inventory.Racks.Rack.PowerSupplyZones.PowerSupplyZone.PowerSupplyZoneAttributes)}
                        self._child_list_classes = {}

                        self.number = YLeaf(YType.int32, "number")

                        self.power_supply_zone_attributes = Inventory.Racks.Rack.PowerSupplyZones.PowerSupplyZone.PowerSupplyZoneAttributes()
                        self.power_supply_zone_attributes.parent = self
                        self._children_name_map["power_supply_zone_attributes"] = "power-supply-zone-attributes"
                        self._children_yang_names.add("power-supply-zone-attributes")
                        self._segment_path = lambda: "power-supply-zone" + "[number='" + self.number.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Inventory.Racks.Rack.PowerSupplyZones.PowerSupplyZone, ['number'], name, value)


                    class PowerSupplyZoneAttributes(Entity):
                        """
                        Power suppy zone attributes 
                        
                        .. attribute:: power_supply_group_info
                        
                        	Power supply group information
                        	**type**\:   :py:class:`PowerSupplyGroupInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.Inventory.Racks.Rack.PowerSupplyZones.PowerSupplyZone.PowerSupplyZoneAttributes.PowerSupplyGroupInfo>`
                        
                        

                        """

                        _prefix = 'asr9k-sc-invmgr-admin-oper'
                        _revision = '2017-01-04'

                        def __init__(self):
                            super(Inventory.Racks.Rack.PowerSupplyZones.PowerSupplyZone.PowerSupplyZoneAttributes, self).__init__()

                            self.yang_name = "power-supply-zone-attributes"
                            self.yang_parent_name = "power-supply-zone"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"power-supply-group-info" : ("power_supply_group_info", Inventory.Racks.Rack.PowerSupplyZones.PowerSupplyZone.PowerSupplyZoneAttributes.PowerSupplyGroupInfo)}
                            self._child_list_classes = {}

                            self.power_supply_group_info = Inventory.Racks.Rack.PowerSupplyZones.PowerSupplyZone.PowerSupplyZoneAttributes.PowerSupplyGroupInfo()
                            self.power_supply_group_info.parent = self
                            self._children_name_map["power_supply_group_info"] = "power-supply-group-info"
                            self._children_yang_names.add("power-supply-group-info")
                            self._segment_path = lambda: "power-supply-zone-attributes"


                        class PowerSupplyGroupInfo(Entity):
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
                                super(Inventory.Racks.Rack.PowerSupplyZones.PowerSupplyZone.PowerSupplyZoneAttributes.PowerSupplyGroupInfo, self).__init__()

                                self.yang_name = "power-supply-group-info"
                                self.yang_parent_name = "power-supply-zone-attributes"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.power_group_available_current = YLeaf(YType.int32, "power-group-available-current")

                                self.power_group_drawn_current = YLeaf(YType.int32, "power-group-drawn-current")

                                self.power_group_power_units = YLeaf(YType.str, "power-group-power-units")

                                self.power_group_redundancy_mode = YLeaf(YType.int32, "power-group-redundancy-mode")
                                self._segment_path = lambda: "power-supply-group-info"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Inventory.Racks.Rack.PowerSupplyZones.PowerSupplyZone.PowerSupplyZoneAttributes.PowerSupplyGroupInfo, ['power_group_available_current', 'power_group_drawn_current', 'power_group_power_units', 'power_group_redundancy_mode'], name, value)


            class Slots(Entity):
                """
                Slot table contains all slots in the rack
                
                .. attribute:: slot
                
                	Slot number
                	**type**\: list of    :py:class:`Slot <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.Inventory.Racks.Rack.Slots.Slot>`
                
                

                """

                _prefix = 'asr9k-sc-invmgr-admin-oper'
                _revision = '2017-01-04'

                def __init__(self):
                    super(Inventory.Racks.Rack.Slots, self).__init__()

                    self.yang_name = "slots"
                    self.yang_parent_name = "rack"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"slot" : ("slot", Inventory.Racks.Rack.Slots.Slot)}

                    self.slot = YList(self)
                    self._segment_path = lambda: "slots"

                def __setattr__(self, name, value):
                    self._perform_setattr(Inventory.Racks.Rack.Slots, [], name, value)


                class Slot(Entity):
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
                        super(Inventory.Racks.Rack.Slots.Slot, self).__init__()

                        self.yang_name = "slot"
                        self.yang_parent_name = "slots"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"basic-attributes" : ("basic_attributes", Inventory.Racks.Rack.Slots.Slot.BasicAttributes), "cards" : ("cards", Inventory.Racks.Rack.Slots.Slot.Cards)}
                        self._child_list_classes = {}

                        self.number = YLeaf(YType.int32, "number")

                        self.basic_attributes = Inventory.Racks.Rack.Slots.Slot.BasicAttributes()
                        self.basic_attributes.parent = self
                        self._children_name_map["basic_attributes"] = "basic-attributes"
                        self._children_yang_names.add("basic-attributes")

                        self.cards = Inventory.Racks.Rack.Slots.Slot.Cards()
                        self.cards.parent = self
                        self._children_name_map["cards"] = "cards"
                        self._children_yang_names.add("cards")
                        self._segment_path = lambda: "slot" + "[number='" + self.number.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Inventory.Racks.Rack.Slots.Slot, ['number'], name, value)


                    class BasicAttributes(Entity):
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
                            super(Inventory.Racks.Rack.Slots.Slot.BasicAttributes, self).__init__()

                            self.yang_name = "basic-attributes"
                            self.yang_parent_name = "slot"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"basic-info" : ("basic_info", Inventory.Racks.Rack.Slots.Slot.BasicAttributes.BasicInfo), "fru-info" : ("fru_info", Inventory.Racks.Rack.Slots.Slot.BasicAttributes.FruInfo)}
                            self._child_list_classes = {}

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
                                super(Inventory.Racks.Rack.Slots.Slot.BasicAttributes.BasicInfo, self).__init__()

                                self.yang_name = "basic-info"
                                self.yang_parent_name = "basic-attributes"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.alias = YLeaf(YType.str, "alias")

                                self.asset_id_str = YLeaf(YType.str, "asset-id-str")

                                self.asset_identification = YLeaf(YType.int32, "asset-identification")

                                self.ceport = YLeaf(YType.boolean, "ceport")

                                self.chip_hardware_revision = YLeaf(YType.str, "chip-hardware-revision")

                                self.composite_class_code = YLeaf(YType.int32, "composite-class-code")

                                self.description = YLeaf(YType.str, "description")

                                self.environmental_monitor_path = YLeaf(YType.str, "environmental-monitor-path")

                                self.firmware_revision = YLeaf(YType.str, "firmware-revision")

                                self.group_flag = YLeaf(YType.boolean, "group-flag")

                                self.hardware_revision = YLeaf(YType.str, "hardware-revision")

                                self.is_field_replaceable_unit = YLeaf(YType.boolean, "is-field-replaceable-unit")

                                self.manufacturer_asset_tags = YLeaf(YType.int32, "manufacturer-asset-tags")

                                self.manufacturer_name = YLeaf(YType.str, "manufacturer-name")

                                self.memory_size = YLeaf(YType.int32, "memory-size")

                                self.model_name = YLeaf(YType.str, "model-name")

                                self.name = YLeaf(YType.str, "name")

                                self.new_deviation_number = YLeaf(YType.int32, "new-deviation-number")

                                self.physical_layer_interface_module_type = YLeaf(YType.int32, "physical-layer-interface-module-type")

                                self.redundancystate = YLeaf(YType.int32, "redundancystate")

                                self.serial_number = YLeaf(YType.str, "serial-number")

                                self.software_revision = YLeaf(YType.str, "software-revision")

                                self.unique_id = YLeaf(YType.int32, "unique-id")

                                self.unrecognized_fru = YLeaf(YType.boolean, "unrecognized-fru")

                                self.vendor_type = YLeaf(YType.str, "vendor-type")

                                self.xr_scoped = YLeaf(YType.boolean, "xr-scoped")
                                self._segment_path = lambda: "basic-info"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.BasicAttributes.BasicInfo, ['alias', 'asset_id_str', 'asset_identification', 'ceport', 'chip_hardware_revision', 'composite_class_code', 'description', 'environmental_monitor_path', 'firmware_revision', 'group_flag', 'hardware_revision', 'is_field_replaceable_unit', 'manufacturer_asset_tags', 'manufacturer_name', 'memory_size', 'model_name', 'name', 'new_deviation_number', 'physical_layer_interface_module_type', 'redundancystate', 'serial_number', 'software_revision', 'unique_id', 'unrecognized_fru', 'vendor_type', 'xr_scoped'], name, value)


                        class FruInfo(Entity):
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
                            	**type**\:   :py:class:`CardResetReason <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.CardResetReason>`
                            
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
                                super(Inventory.Racks.Rack.Slots.Slot.BasicAttributes.FruInfo, self).__init__()

                                self.yang_name = "fru-info"
                                self.yang_parent_name = "basic-attributes"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"card-up-time" : ("card_up_time", Inventory.Racks.Rack.Slots.Slot.BasicAttributes.FruInfo.CardUpTime), "last-operational-state-change" : ("last_operational_state_change", Inventory.Racks.Rack.Slots.Slot.BasicAttributes.FruInfo.LastOperationalStateChange)}
                                self._child_list_classes = {}

                                self.card_administrative_state = YLeaf(YType.int32, "card-administrative-state")

                                self.card_monitor_state = YLeaf(YType.int32, "card-monitor-state")

                                self.card_operational_state = YLeaf(YType.int32, "card-operational-state")

                                self.card_reset_reason = YLeaf(YType.enumeration, "card-reset-reason")

                                self.power_administrative_state = YLeaf(YType.int32, "power-administrative-state")

                                self.power_current_measurement = YLeaf(YType.int32, "power-current-measurement")

                                self.power_operational_state = YLeaf(YType.int32, "power-operational-state")

                                self.card_up_time = Inventory.Racks.Rack.Slots.Slot.BasicAttributes.FruInfo.CardUpTime()
                                self.card_up_time.parent = self
                                self._children_name_map["card_up_time"] = "card-up-time"
                                self._children_yang_names.add("card-up-time")

                                self.last_operational_state_change = Inventory.Racks.Rack.Slots.Slot.BasicAttributes.FruInfo.LastOperationalStateChange()
                                self.last_operational_state_change.parent = self
                                self._children_name_map["last_operational_state_change"] = "last-operational-state-change"
                                self._children_yang_names.add("last-operational-state-change")
                                self._segment_path = lambda: "fru-info"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.BasicAttributes.FruInfo, ['card_administrative_state', 'card_monitor_state', 'card_operational_state', 'card_reset_reason', 'power_administrative_state', 'power_current_measurement', 'power_operational_state'], name, value)


                            class CardUpTime(Entity):
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
                                    super(Inventory.Racks.Rack.Slots.Slot.BasicAttributes.FruInfo.CardUpTime, self).__init__()

                                    self.yang_name = "card-up-time"
                                    self.yang_parent_name = "fru-info"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.time_in_nano_seconds = YLeaf(YType.int32, "time-in-nano-seconds")

                                    self.time_in_seconds = YLeaf(YType.int32, "time-in-seconds")
                                    self._segment_path = lambda: "card-up-time"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.BasicAttributes.FruInfo.CardUpTime, ['time_in_nano_seconds', 'time_in_seconds'], name, value)


                            class LastOperationalStateChange(Entity):
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
                                    super(Inventory.Racks.Rack.Slots.Slot.BasicAttributes.FruInfo.LastOperationalStateChange, self).__init__()

                                    self.yang_name = "last-operational-state-change"
                                    self.yang_parent_name = "fru-info"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.time_in_nano_seconds = YLeaf(YType.int32, "time-in-nano-seconds")

                                    self.time_in_seconds = YLeaf(YType.int32, "time-in-seconds")
                                    self._segment_path = lambda: "last-operational-state-change"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.BasicAttributes.FruInfo.LastOperationalStateChange, ['time_in_nano_seconds', 'time_in_seconds'], name, value)


                    class Cards(Entity):
                        """
                        Card table contains all cards in the slot
                        
                        .. attribute:: card
                        
                        	Card number
                        	**type**\: list of    :py:class:`Card <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card>`
                        
                        

                        """

                        _prefix = 'asr9k-sc-invmgr-admin-oper'
                        _revision = '2017-01-04'

                        def __init__(self):
                            super(Inventory.Racks.Rack.Slots.Slot.Cards, self).__init__()

                            self.yang_name = "cards"
                            self.yang_parent_name = "slot"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"card" : ("card", Inventory.Racks.Rack.Slots.Slot.Cards.Card)}

                            self.card = YList(self)
                            self._segment_path = lambda: "cards"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards, [], name, value)


                        class Card(Entity):
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
                                super(Inventory.Racks.Rack.Slots.Slot.Cards.Card, self).__init__()

                                self.yang_name = "card"
                                self.yang_parent_name = "cards"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"basic-attributes" : ("basic_attributes", Inventory.Racks.Rack.Slots.Slot.Cards.Card.BasicAttributes), "hw-components" : ("hw_components", Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents), "port-slots" : ("port_slots", Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots), "sensors" : ("sensors", Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors), "sub-slots" : ("sub_slots", Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots)}
                                self._child_list_classes = {}

                                self.number = YLeaf(YType.int32, "number")

                                self.basic_attributes = Inventory.Racks.Rack.Slots.Slot.Cards.Card.BasicAttributes()
                                self.basic_attributes.parent = self
                                self._children_name_map["basic_attributes"] = "basic-attributes"
                                self._children_yang_names.add("basic-attributes")

                                self.hw_components = Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents()
                                self.hw_components.parent = self
                                self._children_name_map["hw_components"] = "hw-components"
                                self._children_yang_names.add("hw-components")

                                self.port_slots = Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots()
                                self.port_slots.parent = self
                                self._children_name_map["port_slots"] = "port-slots"
                                self._children_yang_names.add("port-slots")

                                self.sensors = Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors()
                                self.sensors.parent = self
                                self._children_name_map["sensors"] = "sensors"
                                self._children_yang_names.add("sensors")

                                self.sub_slots = Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots()
                                self.sub_slots.parent = self
                                self._children_name_map["sub_slots"] = "sub-slots"
                                self._children_yang_names.add("sub-slots")
                                self._segment_path = lambda: "card" + "[number='" + self.number.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card, ['number'], name, value)


                            class BasicAttributes(Entity):
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
                                    super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.BasicAttributes, self).__init__()

                                    self.yang_name = "basic-attributes"
                                    self.yang_parent_name = "card"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {"basic-info" : ("basic_info", Inventory.Racks.Rack.Slots.Slot.Cards.Card.BasicAttributes.BasicInfo), "fru-info" : ("fru_info", Inventory.Racks.Rack.Slots.Slot.Cards.Card.BasicAttributes.FruInfo)}
                                    self._child_list_classes = {}

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
                                        super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.BasicAttributes.BasicInfo, self).__init__()

                                        self.yang_name = "basic-info"
                                        self.yang_parent_name = "basic-attributes"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.alias = YLeaf(YType.str, "alias")

                                        self.asset_id_str = YLeaf(YType.str, "asset-id-str")

                                        self.asset_identification = YLeaf(YType.int32, "asset-identification")

                                        self.ceport = YLeaf(YType.boolean, "ceport")

                                        self.chip_hardware_revision = YLeaf(YType.str, "chip-hardware-revision")

                                        self.composite_class_code = YLeaf(YType.int32, "composite-class-code")

                                        self.description = YLeaf(YType.str, "description")

                                        self.environmental_monitor_path = YLeaf(YType.str, "environmental-monitor-path")

                                        self.firmware_revision = YLeaf(YType.str, "firmware-revision")

                                        self.group_flag = YLeaf(YType.boolean, "group-flag")

                                        self.hardware_revision = YLeaf(YType.str, "hardware-revision")

                                        self.is_field_replaceable_unit = YLeaf(YType.boolean, "is-field-replaceable-unit")

                                        self.manufacturer_asset_tags = YLeaf(YType.int32, "manufacturer-asset-tags")

                                        self.manufacturer_name = YLeaf(YType.str, "manufacturer-name")

                                        self.memory_size = YLeaf(YType.int32, "memory-size")

                                        self.model_name = YLeaf(YType.str, "model-name")

                                        self.name = YLeaf(YType.str, "name")

                                        self.new_deviation_number = YLeaf(YType.int32, "new-deviation-number")

                                        self.physical_layer_interface_module_type = YLeaf(YType.int32, "physical-layer-interface-module-type")

                                        self.redundancystate = YLeaf(YType.int32, "redundancystate")

                                        self.serial_number = YLeaf(YType.str, "serial-number")

                                        self.software_revision = YLeaf(YType.str, "software-revision")

                                        self.unique_id = YLeaf(YType.int32, "unique-id")

                                        self.unrecognized_fru = YLeaf(YType.boolean, "unrecognized-fru")

                                        self.vendor_type = YLeaf(YType.str, "vendor-type")

                                        self.xr_scoped = YLeaf(YType.boolean, "xr-scoped")
                                        self._segment_path = lambda: "basic-info"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.BasicAttributes.BasicInfo, ['alias', 'asset_id_str', 'asset_identification', 'ceport', 'chip_hardware_revision', 'composite_class_code', 'description', 'environmental_monitor_path', 'firmware_revision', 'group_flag', 'hardware_revision', 'is_field_replaceable_unit', 'manufacturer_asset_tags', 'manufacturer_name', 'memory_size', 'model_name', 'name', 'new_deviation_number', 'physical_layer_interface_module_type', 'redundancystate', 'serial_number', 'software_revision', 'unique_id', 'unrecognized_fru', 'vendor_type', 'xr_scoped'], name, value)


                                class FruInfo(Entity):
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
                                    	**type**\:   :py:class:`CardResetReason <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.CardResetReason>`
                                    
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
                                        super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.BasicAttributes.FruInfo, self).__init__()

                                        self.yang_name = "fru-info"
                                        self.yang_parent_name = "basic-attributes"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {"card-up-time" : ("card_up_time", Inventory.Racks.Rack.Slots.Slot.Cards.Card.BasicAttributes.FruInfo.CardUpTime), "last-operational-state-change" : ("last_operational_state_change", Inventory.Racks.Rack.Slots.Slot.Cards.Card.BasicAttributes.FruInfo.LastOperationalStateChange)}
                                        self._child_list_classes = {}

                                        self.card_administrative_state = YLeaf(YType.int32, "card-administrative-state")

                                        self.card_monitor_state = YLeaf(YType.int32, "card-monitor-state")

                                        self.card_operational_state = YLeaf(YType.int32, "card-operational-state")

                                        self.card_reset_reason = YLeaf(YType.enumeration, "card-reset-reason")

                                        self.power_administrative_state = YLeaf(YType.int32, "power-administrative-state")

                                        self.power_current_measurement = YLeaf(YType.int32, "power-current-measurement")

                                        self.power_operational_state = YLeaf(YType.int32, "power-operational-state")

                                        self.card_up_time = Inventory.Racks.Rack.Slots.Slot.Cards.Card.BasicAttributes.FruInfo.CardUpTime()
                                        self.card_up_time.parent = self
                                        self._children_name_map["card_up_time"] = "card-up-time"
                                        self._children_yang_names.add("card-up-time")

                                        self.last_operational_state_change = Inventory.Racks.Rack.Slots.Slot.Cards.Card.BasicAttributes.FruInfo.LastOperationalStateChange()
                                        self.last_operational_state_change.parent = self
                                        self._children_name_map["last_operational_state_change"] = "last-operational-state-change"
                                        self._children_yang_names.add("last-operational-state-change")
                                        self._segment_path = lambda: "fru-info"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.BasicAttributes.FruInfo, ['card_administrative_state', 'card_monitor_state', 'card_operational_state', 'card_reset_reason', 'power_administrative_state', 'power_current_measurement', 'power_operational_state'], name, value)


                                    class CardUpTime(Entity):
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
                                            super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.BasicAttributes.FruInfo.CardUpTime, self).__init__()

                                            self.yang_name = "card-up-time"
                                            self.yang_parent_name = "fru-info"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.time_in_nano_seconds = YLeaf(YType.int32, "time-in-nano-seconds")

                                            self.time_in_seconds = YLeaf(YType.int32, "time-in-seconds")
                                            self._segment_path = lambda: "card-up-time"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.BasicAttributes.FruInfo.CardUpTime, ['time_in_nano_seconds', 'time_in_seconds'], name, value)


                                    class LastOperationalStateChange(Entity):
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
                                            super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.BasicAttributes.FruInfo.LastOperationalStateChange, self).__init__()

                                            self.yang_name = "last-operational-state-change"
                                            self.yang_parent_name = "fru-info"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.time_in_nano_seconds = YLeaf(YType.int32, "time-in-nano-seconds")

                                            self.time_in_seconds = YLeaf(YType.int32, "time-in-seconds")
                                            self._segment_path = lambda: "last-operational-state-change"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.BasicAttributes.FruInfo.LastOperationalStateChange, ['time_in_nano_seconds', 'time_in_seconds'], name, value)


                            class HwComponents(Entity):
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
                                    super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents, self).__init__()

                                    self.yang_name = "hw-components"
                                    self.yang_parent_name = "card"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {"hw-component" : ("hw_component", Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent)}

                                    self.hw_component = YList(self)
                                    self._segment_path = lambda: "hw-components"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents, [], name, value)


                                class HwComponent(Entity):
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
                                        super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent, self).__init__()

                                        self.yang_name = "hw-component"
                                        self.yang_parent_name = "hw-components"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {"basic-attributes" : ("basic_attributes", Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.BasicAttributes), "sensors" : ("sensors", Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors)}
                                        self._child_list_classes = {}

                                        self.number = YLeaf(YType.int32, "number")

                                        self.basic_attributes = Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.BasicAttributes()
                                        self.basic_attributes.parent = self
                                        self._children_name_map["basic_attributes"] = "basic-attributes"
                                        self._children_yang_names.add("basic-attributes")

                                        self.sensors = Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors()
                                        self.sensors.parent = self
                                        self._children_name_map["sensors"] = "sensors"
                                        self._children_yang_names.add("sensors")
                                        self._segment_path = lambda: "hw-component" + "[number='" + self.number.get() + "']"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent, ['number'], name, value)


                                    class BasicAttributes(Entity):
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
                                            super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.BasicAttributes, self).__init__()

                                            self.yang_name = "basic-attributes"
                                            self.yang_parent_name = "hw-component"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {"basic-info" : ("basic_info", Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.BasicAttributes.BasicInfo), "fru-info" : ("fru_info", Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.BasicAttributes.FruInfo)}
                                            self._child_list_classes = {}

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
                                                super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.BasicAttributes.BasicInfo, self).__init__()

                                                self.yang_name = "basic-info"
                                                self.yang_parent_name = "basic-attributes"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self._child_container_classes = {}
                                                self._child_list_classes = {}

                                                self.alias = YLeaf(YType.str, "alias")

                                                self.asset_id_str = YLeaf(YType.str, "asset-id-str")

                                                self.asset_identification = YLeaf(YType.int32, "asset-identification")

                                                self.ceport = YLeaf(YType.boolean, "ceport")

                                                self.chip_hardware_revision = YLeaf(YType.str, "chip-hardware-revision")

                                                self.composite_class_code = YLeaf(YType.int32, "composite-class-code")

                                                self.description = YLeaf(YType.str, "description")

                                                self.environmental_monitor_path = YLeaf(YType.str, "environmental-monitor-path")

                                                self.firmware_revision = YLeaf(YType.str, "firmware-revision")

                                                self.group_flag = YLeaf(YType.boolean, "group-flag")

                                                self.hardware_revision = YLeaf(YType.str, "hardware-revision")

                                                self.is_field_replaceable_unit = YLeaf(YType.boolean, "is-field-replaceable-unit")

                                                self.manufacturer_asset_tags = YLeaf(YType.int32, "manufacturer-asset-tags")

                                                self.manufacturer_name = YLeaf(YType.str, "manufacturer-name")

                                                self.memory_size = YLeaf(YType.int32, "memory-size")

                                                self.model_name = YLeaf(YType.str, "model-name")

                                                self.name = YLeaf(YType.str, "name")

                                                self.new_deviation_number = YLeaf(YType.int32, "new-deviation-number")

                                                self.physical_layer_interface_module_type = YLeaf(YType.int32, "physical-layer-interface-module-type")

                                                self.redundancystate = YLeaf(YType.int32, "redundancystate")

                                                self.serial_number = YLeaf(YType.str, "serial-number")

                                                self.software_revision = YLeaf(YType.str, "software-revision")

                                                self.unique_id = YLeaf(YType.int32, "unique-id")

                                                self.unrecognized_fru = YLeaf(YType.boolean, "unrecognized-fru")

                                                self.vendor_type = YLeaf(YType.str, "vendor-type")

                                                self.xr_scoped = YLeaf(YType.boolean, "xr-scoped")
                                                self._segment_path = lambda: "basic-info"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.BasicAttributes.BasicInfo, ['alias', 'asset_id_str', 'asset_identification', 'ceport', 'chip_hardware_revision', 'composite_class_code', 'description', 'environmental_monitor_path', 'firmware_revision', 'group_flag', 'hardware_revision', 'is_field_replaceable_unit', 'manufacturer_asset_tags', 'manufacturer_name', 'memory_size', 'model_name', 'name', 'new_deviation_number', 'physical_layer_interface_module_type', 'redundancystate', 'serial_number', 'software_revision', 'unique_id', 'unrecognized_fru', 'vendor_type', 'xr_scoped'], name, value)


                                        class FruInfo(Entity):
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
                                            	**type**\:   :py:class:`CardResetReason <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.CardResetReason>`
                                            
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
                                                super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.BasicAttributes.FruInfo, self).__init__()

                                                self.yang_name = "fru-info"
                                                self.yang_parent_name = "basic-attributes"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self._child_container_classes = {"card-up-time" : ("card_up_time", Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.BasicAttributes.FruInfo.CardUpTime), "last-operational-state-change" : ("last_operational_state_change", Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.BasicAttributes.FruInfo.LastOperationalStateChange)}
                                                self._child_list_classes = {}

                                                self.card_administrative_state = YLeaf(YType.int32, "card-administrative-state")

                                                self.card_monitor_state = YLeaf(YType.int32, "card-monitor-state")

                                                self.card_operational_state = YLeaf(YType.int32, "card-operational-state")

                                                self.card_reset_reason = YLeaf(YType.enumeration, "card-reset-reason")

                                                self.power_administrative_state = YLeaf(YType.int32, "power-administrative-state")

                                                self.power_current_measurement = YLeaf(YType.int32, "power-current-measurement")

                                                self.power_operational_state = YLeaf(YType.int32, "power-operational-state")

                                                self.card_up_time = Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.BasicAttributes.FruInfo.CardUpTime()
                                                self.card_up_time.parent = self
                                                self._children_name_map["card_up_time"] = "card-up-time"
                                                self._children_yang_names.add("card-up-time")

                                                self.last_operational_state_change = Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.BasicAttributes.FruInfo.LastOperationalStateChange()
                                                self.last_operational_state_change.parent = self
                                                self._children_name_map["last_operational_state_change"] = "last-operational-state-change"
                                                self._children_yang_names.add("last-operational-state-change")
                                                self._segment_path = lambda: "fru-info"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.BasicAttributes.FruInfo, ['card_administrative_state', 'card_monitor_state', 'card_operational_state', 'card_reset_reason', 'power_administrative_state', 'power_current_measurement', 'power_operational_state'], name, value)


                                            class CardUpTime(Entity):
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
                                                    super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.BasicAttributes.FruInfo.CardUpTime, self).__init__()

                                                    self.yang_name = "card-up-time"
                                                    self.yang_parent_name = "fru-info"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self._child_container_classes = {}
                                                    self._child_list_classes = {}

                                                    self.time_in_nano_seconds = YLeaf(YType.int32, "time-in-nano-seconds")

                                                    self.time_in_seconds = YLeaf(YType.int32, "time-in-seconds")
                                                    self._segment_path = lambda: "card-up-time"

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.BasicAttributes.FruInfo.CardUpTime, ['time_in_nano_seconds', 'time_in_seconds'], name, value)


                                            class LastOperationalStateChange(Entity):
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
                                                    super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.BasicAttributes.FruInfo.LastOperationalStateChange, self).__init__()

                                                    self.yang_name = "last-operational-state-change"
                                                    self.yang_parent_name = "fru-info"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self._child_container_classes = {}
                                                    self._child_list_classes = {}

                                                    self.time_in_nano_seconds = YLeaf(YType.int32, "time-in-nano-seconds")

                                                    self.time_in_seconds = YLeaf(YType.int32, "time-in-seconds")
                                                    self._segment_path = lambda: "last-operational-state-change"

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.BasicAttributes.FruInfo.LastOperationalStateChange, ['time_in_nano_seconds', 'time_in_seconds'], name, value)


                                    class Sensors(Entity):
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
                                            super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors, self).__init__()

                                            self.yang_name = "sensors"
                                            self.yang_parent_name = "hw-component"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {"sensor" : ("sensor", Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor)}

                                            self.sensor = YList(self)
                                            self._segment_path = lambda: "sensors"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors, [], name, value)


                                        class Sensor(Entity):
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
                                                super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor, self).__init__()

                                                self.yang_name = "sensor"
                                                self.yang_parent_name = "sensors"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self._child_container_classes = {"basic-attributes" : ("basic_attributes", Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.BasicAttributes)}
                                                self._child_list_classes = {}

                                                self.number = YLeaf(YType.int32, "number")

                                                self.basic_attributes = Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.BasicAttributes()
                                                self.basic_attributes.parent = self
                                                self._children_name_map["basic_attributes"] = "basic-attributes"
                                                self._children_yang_names.add("basic-attributes")
                                                self._segment_path = lambda: "sensor" + "[number='" + self.number.get() + "']"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor, ['number'], name, value)


                                            class BasicAttributes(Entity):
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
                                                    super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.BasicAttributes, self).__init__()

                                                    self.yang_name = "basic-attributes"
                                                    self.yang_parent_name = "sensor"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self._child_container_classes = {"basic-info" : ("basic_info", Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.BasicAttributes.BasicInfo), "fru-info" : ("fru_info", Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.BasicAttributes.FruInfo)}
                                                    self._child_list_classes = {}

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
                                                        super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.BasicAttributes.BasicInfo, self).__init__()

                                                        self.yang_name = "basic-info"
                                                        self.yang_parent_name = "basic-attributes"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self._child_container_classes = {}
                                                        self._child_list_classes = {}

                                                        self.alias = YLeaf(YType.str, "alias")

                                                        self.asset_id_str = YLeaf(YType.str, "asset-id-str")

                                                        self.asset_identification = YLeaf(YType.int32, "asset-identification")

                                                        self.ceport = YLeaf(YType.boolean, "ceport")

                                                        self.chip_hardware_revision = YLeaf(YType.str, "chip-hardware-revision")

                                                        self.composite_class_code = YLeaf(YType.int32, "composite-class-code")

                                                        self.description = YLeaf(YType.str, "description")

                                                        self.environmental_monitor_path = YLeaf(YType.str, "environmental-monitor-path")

                                                        self.firmware_revision = YLeaf(YType.str, "firmware-revision")

                                                        self.group_flag = YLeaf(YType.boolean, "group-flag")

                                                        self.hardware_revision = YLeaf(YType.str, "hardware-revision")

                                                        self.is_field_replaceable_unit = YLeaf(YType.boolean, "is-field-replaceable-unit")

                                                        self.manufacturer_asset_tags = YLeaf(YType.int32, "manufacturer-asset-tags")

                                                        self.manufacturer_name = YLeaf(YType.str, "manufacturer-name")

                                                        self.memory_size = YLeaf(YType.int32, "memory-size")

                                                        self.model_name = YLeaf(YType.str, "model-name")

                                                        self.name = YLeaf(YType.str, "name")

                                                        self.new_deviation_number = YLeaf(YType.int32, "new-deviation-number")

                                                        self.physical_layer_interface_module_type = YLeaf(YType.int32, "physical-layer-interface-module-type")

                                                        self.redundancystate = YLeaf(YType.int32, "redundancystate")

                                                        self.serial_number = YLeaf(YType.str, "serial-number")

                                                        self.software_revision = YLeaf(YType.str, "software-revision")

                                                        self.unique_id = YLeaf(YType.int32, "unique-id")

                                                        self.unrecognized_fru = YLeaf(YType.boolean, "unrecognized-fru")

                                                        self.vendor_type = YLeaf(YType.str, "vendor-type")

                                                        self.xr_scoped = YLeaf(YType.boolean, "xr-scoped")
                                                        self._segment_path = lambda: "basic-info"

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.BasicAttributes.BasicInfo, ['alias', 'asset_id_str', 'asset_identification', 'ceport', 'chip_hardware_revision', 'composite_class_code', 'description', 'environmental_monitor_path', 'firmware_revision', 'group_flag', 'hardware_revision', 'is_field_replaceable_unit', 'manufacturer_asset_tags', 'manufacturer_name', 'memory_size', 'model_name', 'name', 'new_deviation_number', 'physical_layer_interface_module_type', 'redundancystate', 'serial_number', 'software_revision', 'unique_id', 'unrecognized_fru', 'vendor_type', 'xr_scoped'], name, value)


                                                class FruInfo(Entity):
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
                                                    	**type**\:   :py:class:`CardResetReason <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.CardResetReason>`
                                                    
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
                                                        super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.BasicAttributes.FruInfo, self).__init__()

                                                        self.yang_name = "fru-info"
                                                        self.yang_parent_name = "basic-attributes"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self._child_container_classes = {"card-up-time" : ("card_up_time", Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.BasicAttributes.FruInfo.CardUpTime), "last-operational-state-change" : ("last_operational_state_change", Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.BasicAttributes.FruInfo.LastOperationalStateChange)}
                                                        self._child_list_classes = {}

                                                        self.card_administrative_state = YLeaf(YType.int32, "card-administrative-state")

                                                        self.card_monitor_state = YLeaf(YType.int32, "card-monitor-state")

                                                        self.card_operational_state = YLeaf(YType.int32, "card-operational-state")

                                                        self.card_reset_reason = YLeaf(YType.enumeration, "card-reset-reason")

                                                        self.power_administrative_state = YLeaf(YType.int32, "power-administrative-state")

                                                        self.power_current_measurement = YLeaf(YType.int32, "power-current-measurement")

                                                        self.power_operational_state = YLeaf(YType.int32, "power-operational-state")

                                                        self.card_up_time = Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.BasicAttributes.FruInfo.CardUpTime()
                                                        self.card_up_time.parent = self
                                                        self._children_name_map["card_up_time"] = "card-up-time"
                                                        self._children_yang_names.add("card-up-time")

                                                        self.last_operational_state_change = Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.BasicAttributes.FruInfo.LastOperationalStateChange()
                                                        self.last_operational_state_change.parent = self
                                                        self._children_name_map["last_operational_state_change"] = "last-operational-state-change"
                                                        self._children_yang_names.add("last-operational-state-change")
                                                        self._segment_path = lambda: "fru-info"

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.BasicAttributes.FruInfo, ['card_administrative_state', 'card_monitor_state', 'card_operational_state', 'card_reset_reason', 'power_administrative_state', 'power_current_measurement', 'power_operational_state'], name, value)


                                                    class CardUpTime(Entity):
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
                                                            super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.BasicAttributes.FruInfo.CardUpTime, self).__init__()

                                                            self.yang_name = "card-up-time"
                                                            self.yang_parent_name = "fru-info"
                                                            self.is_top_level_class = False
                                                            self.has_list_ancestor = True
                                                            self._child_container_classes = {}
                                                            self._child_list_classes = {}

                                                            self.time_in_nano_seconds = YLeaf(YType.int32, "time-in-nano-seconds")

                                                            self.time_in_seconds = YLeaf(YType.int32, "time-in-seconds")
                                                            self._segment_path = lambda: "card-up-time"

                                                        def __setattr__(self, name, value):
                                                            self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.BasicAttributes.FruInfo.CardUpTime, ['time_in_nano_seconds', 'time_in_seconds'], name, value)


                                                    class LastOperationalStateChange(Entity):
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
                                                            super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.BasicAttributes.FruInfo.LastOperationalStateChange, self).__init__()

                                                            self.yang_name = "last-operational-state-change"
                                                            self.yang_parent_name = "fru-info"
                                                            self.is_top_level_class = False
                                                            self.has_list_ancestor = True
                                                            self._child_container_classes = {}
                                                            self._child_list_classes = {}

                                                            self.time_in_nano_seconds = YLeaf(YType.int32, "time-in-nano-seconds")

                                                            self.time_in_seconds = YLeaf(YType.int32, "time-in-seconds")
                                                            self._segment_path = lambda: "last-operational-state-change"

                                                        def __setattr__(self, name, value):
                                                            self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.BasicAttributes.FruInfo.LastOperationalStateChange, ['time_in_nano_seconds', 'time_in_seconds'], name, value)


                            class PortSlots(Entity):
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
                                    super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots, self).__init__()

                                    self.yang_name = "port-slots"
                                    self.yang_parent_name = "card"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {"port-slot" : ("port_slot", Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot)}

                                    self.port_slot = YList(self)
                                    self._segment_path = lambda: "port-slots"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots, [], name, value)


                                class PortSlot(Entity):
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
                                        super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot, self).__init__()

                                        self.yang_name = "port-slot"
                                        self.yang_parent_name = "port-slots"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {"basic-attributes" : ("basic_attributes", Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.BasicAttributes), "port" : ("port", Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port)}
                                        self._child_list_classes = {}

                                        self.number = YLeaf(YType.int32, "number")

                                        self.basic_attributes = Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.BasicAttributes()
                                        self.basic_attributes.parent = self
                                        self._children_name_map["basic_attributes"] = "basic-attributes"
                                        self._children_yang_names.add("basic-attributes")

                                        self.port = Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port()
                                        self.port.parent = self
                                        self._children_name_map["port"] = "port"
                                        self._children_yang_names.add("port")
                                        self._segment_path = lambda: "port-slot" + "[number='" + self.number.get() + "']"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot, ['number'], name, value)


                                    class BasicAttributes(Entity):
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
                                            super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.BasicAttributes, self).__init__()

                                            self.yang_name = "basic-attributes"
                                            self.yang_parent_name = "port-slot"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {"basic-info" : ("basic_info", Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.BasicAttributes.BasicInfo), "fru-info" : ("fru_info", Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.BasicAttributes.FruInfo)}
                                            self._child_list_classes = {}

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
                                                super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.BasicAttributes.BasicInfo, self).__init__()

                                                self.yang_name = "basic-info"
                                                self.yang_parent_name = "basic-attributes"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self._child_container_classes = {}
                                                self._child_list_classes = {}

                                                self.alias = YLeaf(YType.str, "alias")

                                                self.asset_id_str = YLeaf(YType.str, "asset-id-str")

                                                self.asset_identification = YLeaf(YType.int32, "asset-identification")

                                                self.ceport = YLeaf(YType.boolean, "ceport")

                                                self.chip_hardware_revision = YLeaf(YType.str, "chip-hardware-revision")

                                                self.composite_class_code = YLeaf(YType.int32, "composite-class-code")

                                                self.description = YLeaf(YType.str, "description")

                                                self.environmental_monitor_path = YLeaf(YType.str, "environmental-monitor-path")

                                                self.firmware_revision = YLeaf(YType.str, "firmware-revision")

                                                self.group_flag = YLeaf(YType.boolean, "group-flag")

                                                self.hardware_revision = YLeaf(YType.str, "hardware-revision")

                                                self.is_field_replaceable_unit = YLeaf(YType.boolean, "is-field-replaceable-unit")

                                                self.manufacturer_asset_tags = YLeaf(YType.int32, "manufacturer-asset-tags")

                                                self.manufacturer_name = YLeaf(YType.str, "manufacturer-name")

                                                self.memory_size = YLeaf(YType.int32, "memory-size")

                                                self.model_name = YLeaf(YType.str, "model-name")

                                                self.name = YLeaf(YType.str, "name")

                                                self.new_deviation_number = YLeaf(YType.int32, "new-deviation-number")

                                                self.physical_layer_interface_module_type = YLeaf(YType.int32, "physical-layer-interface-module-type")

                                                self.redundancystate = YLeaf(YType.int32, "redundancystate")

                                                self.serial_number = YLeaf(YType.str, "serial-number")

                                                self.software_revision = YLeaf(YType.str, "software-revision")

                                                self.unique_id = YLeaf(YType.int32, "unique-id")

                                                self.unrecognized_fru = YLeaf(YType.boolean, "unrecognized-fru")

                                                self.vendor_type = YLeaf(YType.str, "vendor-type")

                                                self.xr_scoped = YLeaf(YType.boolean, "xr-scoped")
                                                self._segment_path = lambda: "basic-info"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.BasicAttributes.BasicInfo, ['alias', 'asset_id_str', 'asset_identification', 'ceport', 'chip_hardware_revision', 'composite_class_code', 'description', 'environmental_monitor_path', 'firmware_revision', 'group_flag', 'hardware_revision', 'is_field_replaceable_unit', 'manufacturer_asset_tags', 'manufacturer_name', 'memory_size', 'model_name', 'name', 'new_deviation_number', 'physical_layer_interface_module_type', 'redundancystate', 'serial_number', 'software_revision', 'unique_id', 'unrecognized_fru', 'vendor_type', 'xr_scoped'], name, value)


                                        class FruInfo(Entity):
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
                                            	**type**\:   :py:class:`CardResetReason <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.CardResetReason>`
                                            
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
                                                super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.BasicAttributes.FruInfo, self).__init__()

                                                self.yang_name = "fru-info"
                                                self.yang_parent_name = "basic-attributes"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self._child_container_classes = {"card-up-time" : ("card_up_time", Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.BasicAttributes.FruInfo.CardUpTime), "last-operational-state-change" : ("last_operational_state_change", Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.BasicAttributes.FruInfo.LastOperationalStateChange)}
                                                self._child_list_classes = {}

                                                self.card_administrative_state = YLeaf(YType.int32, "card-administrative-state")

                                                self.card_monitor_state = YLeaf(YType.int32, "card-monitor-state")

                                                self.card_operational_state = YLeaf(YType.int32, "card-operational-state")

                                                self.card_reset_reason = YLeaf(YType.enumeration, "card-reset-reason")

                                                self.power_administrative_state = YLeaf(YType.int32, "power-administrative-state")

                                                self.power_current_measurement = YLeaf(YType.int32, "power-current-measurement")

                                                self.power_operational_state = YLeaf(YType.int32, "power-operational-state")

                                                self.card_up_time = Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.BasicAttributes.FruInfo.CardUpTime()
                                                self.card_up_time.parent = self
                                                self._children_name_map["card_up_time"] = "card-up-time"
                                                self._children_yang_names.add("card-up-time")

                                                self.last_operational_state_change = Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.BasicAttributes.FruInfo.LastOperationalStateChange()
                                                self.last_operational_state_change.parent = self
                                                self._children_name_map["last_operational_state_change"] = "last-operational-state-change"
                                                self._children_yang_names.add("last-operational-state-change")
                                                self._segment_path = lambda: "fru-info"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.BasicAttributes.FruInfo, ['card_administrative_state', 'card_monitor_state', 'card_operational_state', 'card_reset_reason', 'power_administrative_state', 'power_current_measurement', 'power_operational_state'], name, value)


                                            class CardUpTime(Entity):
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
                                                    super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.BasicAttributes.FruInfo.CardUpTime, self).__init__()

                                                    self.yang_name = "card-up-time"
                                                    self.yang_parent_name = "fru-info"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self._child_container_classes = {}
                                                    self._child_list_classes = {}

                                                    self.time_in_nano_seconds = YLeaf(YType.int32, "time-in-nano-seconds")

                                                    self.time_in_seconds = YLeaf(YType.int32, "time-in-seconds")
                                                    self._segment_path = lambda: "card-up-time"

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.BasicAttributes.FruInfo.CardUpTime, ['time_in_nano_seconds', 'time_in_seconds'], name, value)


                                            class LastOperationalStateChange(Entity):
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
                                                    super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.BasicAttributes.FruInfo.LastOperationalStateChange, self).__init__()

                                                    self.yang_name = "last-operational-state-change"
                                                    self.yang_parent_name = "fru-info"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self._child_container_classes = {}
                                                    self._child_list_classes = {}

                                                    self.time_in_nano_seconds = YLeaf(YType.int32, "time-in-nano-seconds")

                                                    self.time_in_seconds = YLeaf(YType.int32, "time-in-seconds")
                                                    self._segment_path = lambda: "last-operational-state-change"

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.BasicAttributes.FruInfo.LastOperationalStateChange, ['time_in_nano_seconds', 'time_in_seconds'], name, value)


                                    class Port(Entity):
                                        """
                                        Port string
                                        
                                        .. attribute:: basic_attributes
                                        
                                        	Attributes
                                        	**type**\:   :py:class:`BasicAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.BasicAttributes>`
                                        
                                        

                                        """

                                        _prefix = 'asr9k-sc-invmgr-admin-oper'
                                        _revision = '2017-01-04'

                                        def __init__(self):
                                            super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port, self).__init__()

                                            self.yang_name = "port"
                                            self.yang_parent_name = "port-slot"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {"basic-attributes" : ("basic_attributes", Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.BasicAttributes)}
                                            self._child_list_classes = {}

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
                                            	**type**\:   :py:class:`BasicInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.BasicAttributes.BasicInfo>`
                                            
                                            .. attribute:: fru_info
                                            
                                            	Field Replaceable Unit (FRU) inventory information
                                            	**type**\:   :py:class:`FruInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.BasicAttributes.FruInfo>`
                                            
                                            

                                            """

                                            _prefix = 'asr9k-sc-invmgr-admin-oper'
                                            _revision = '2017-01-04'

                                            def __init__(self):
                                                super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.BasicAttributes, self).__init__()

                                                self.yang_name = "basic-attributes"
                                                self.yang_parent_name = "port"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self._child_container_classes = {"basic-info" : ("basic_info", Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.BasicAttributes.BasicInfo), "fru-info" : ("fru_info", Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.BasicAttributes.FruInfo)}
                                                self._child_list_classes = {}

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
                                                    super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.BasicAttributes.BasicInfo, self).__init__()

                                                    self.yang_name = "basic-info"
                                                    self.yang_parent_name = "basic-attributes"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self._child_container_classes = {}
                                                    self._child_list_classes = {}

                                                    self.alias = YLeaf(YType.str, "alias")

                                                    self.asset_id_str = YLeaf(YType.str, "asset-id-str")

                                                    self.asset_identification = YLeaf(YType.int32, "asset-identification")

                                                    self.ceport = YLeaf(YType.boolean, "ceport")

                                                    self.chip_hardware_revision = YLeaf(YType.str, "chip-hardware-revision")

                                                    self.composite_class_code = YLeaf(YType.int32, "composite-class-code")

                                                    self.description = YLeaf(YType.str, "description")

                                                    self.environmental_monitor_path = YLeaf(YType.str, "environmental-monitor-path")

                                                    self.firmware_revision = YLeaf(YType.str, "firmware-revision")

                                                    self.group_flag = YLeaf(YType.boolean, "group-flag")

                                                    self.hardware_revision = YLeaf(YType.str, "hardware-revision")

                                                    self.is_field_replaceable_unit = YLeaf(YType.boolean, "is-field-replaceable-unit")

                                                    self.manufacturer_asset_tags = YLeaf(YType.int32, "manufacturer-asset-tags")

                                                    self.manufacturer_name = YLeaf(YType.str, "manufacturer-name")

                                                    self.memory_size = YLeaf(YType.int32, "memory-size")

                                                    self.model_name = YLeaf(YType.str, "model-name")

                                                    self.name = YLeaf(YType.str, "name")

                                                    self.new_deviation_number = YLeaf(YType.int32, "new-deviation-number")

                                                    self.physical_layer_interface_module_type = YLeaf(YType.int32, "physical-layer-interface-module-type")

                                                    self.redundancystate = YLeaf(YType.int32, "redundancystate")

                                                    self.serial_number = YLeaf(YType.str, "serial-number")

                                                    self.software_revision = YLeaf(YType.str, "software-revision")

                                                    self.unique_id = YLeaf(YType.int32, "unique-id")

                                                    self.unrecognized_fru = YLeaf(YType.boolean, "unrecognized-fru")

                                                    self.vendor_type = YLeaf(YType.str, "vendor-type")

                                                    self.xr_scoped = YLeaf(YType.boolean, "xr-scoped")
                                                    self._segment_path = lambda: "basic-info"

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.BasicAttributes.BasicInfo, ['alias', 'asset_id_str', 'asset_identification', 'ceport', 'chip_hardware_revision', 'composite_class_code', 'description', 'environmental_monitor_path', 'firmware_revision', 'group_flag', 'hardware_revision', 'is_field_replaceable_unit', 'manufacturer_asset_tags', 'manufacturer_name', 'memory_size', 'model_name', 'name', 'new_deviation_number', 'physical_layer_interface_module_type', 'redundancystate', 'serial_number', 'software_revision', 'unique_id', 'unrecognized_fru', 'vendor_type', 'xr_scoped'], name, value)


                                            class FruInfo(Entity):
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
                                                	**type**\:   :py:class:`CardResetReason <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.CardResetReason>`
                                                
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
                                                    super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.BasicAttributes.FruInfo, self).__init__()

                                                    self.yang_name = "fru-info"
                                                    self.yang_parent_name = "basic-attributes"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self._child_container_classes = {"card-up-time" : ("card_up_time", Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.BasicAttributes.FruInfo.CardUpTime), "last-operational-state-change" : ("last_operational_state_change", Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.BasicAttributes.FruInfo.LastOperationalStateChange)}
                                                    self._child_list_classes = {}

                                                    self.card_administrative_state = YLeaf(YType.int32, "card-administrative-state")

                                                    self.card_monitor_state = YLeaf(YType.int32, "card-monitor-state")

                                                    self.card_operational_state = YLeaf(YType.int32, "card-operational-state")

                                                    self.card_reset_reason = YLeaf(YType.enumeration, "card-reset-reason")

                                                    self.power_administrative_state = YLeaf(YType.int32, "power-administrative-state")

                                                    self.power_current_measurement = YLeaf(YType.int32, "power-current-measurement")

                                                    self.power_operational_state = YLeaf(YType.int32, "power-operational-state")

                                                    self.card_up_time = Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.BasicAttributes.FruInfo.CardUpTime()
                                                    self.card_up_time.parent = self
                                                    self._children_name_map["card_up_time"] = "card-up-time"
                                                    self._children_yang_names.add("card-up-time")

                                                    self.last_operational_state_change = Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.BasicAttributes.FruInfo.LastOperationalStateChange()
                                                    self.last_operational_state_change.parent = self
                                                    self._children_name_map["last_operational_state_change"] = "last-operational-state-change"
                                                    self._children_yang_names.add("last-operational-state-change")
                                                    self._segment_path = lambda: "fru-info"

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.BasicAttributes.FruInfo, ['card_administrative_state', 'card_monitor_state', 'card_operational_state', 'card_reset_reason', 'power_administrative_state', 'power_current_measurement', 'power_operational_state'], name, value)


                                                class CardUpTime(Entity):
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
                                                        super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.BasicAttributes.FruInfo.CardUpTime, self).__init__()

                                                        self.yang_name = "card-up-time"
                                                        self.yang_parent_name = "fru-info"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self._child_container_classes = {}
                                                        self._child_list_classes = {}

                                                        self.time_in_nano_seconds = YLeaf(YType.int32, "time-in-nano-seconds")

                                                        self.time_in_seconds = YLeaf(YType.int32, "time-in-seconds")
                                                        self._segment_path = lambda: "card-up-time"

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.BasicAttributes.FruInfo.CardUpTime, ['time_in_nano_seconds', 'time_in_seconds'], name, value)


                                                class LastOperationalStateChange(Entity):
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
                                                        super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.BasicAttributes.FruInfo.LastOperationalStateChange, self).__init__()

                                                        self.yang_name = "last-operational-state-change"
                                                        self.yang_parent_name = "fru-info"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self._child_container_classes = {}
                                                        self._child_list_classes = {}

                                                        self.time_in_nano_seconds = YLeaf(YType.int32, "time-in-nano-seconds")

                                                        self.time_in_seconds = YLeaf(YType.int32, "time-in-seconds")
                                                        self._segment_path = lambda: "last-operational-state-change"

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.BasicAttributes.FruInfo.LastOperationalStateChange, ['time_in_nano_seconds', 'time_in_seconds'], name, value)


                            class Sensors(Entity):
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
                                    super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors, self).__init__()

                                    self.yang_name = "sensors"
                                    self.yang_parent_name = "card"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {"sensor" : ("sensor", Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor)}

                                    self.sensor = YList(self)
                                    self._segment_path = lambda: "sensors"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors, [], name, value)


                                class Sensor(Entity):
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
                                        super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor, self).__init__()

                                        self.yang_name = "sensor"
                                        self.yang_parent_name = "sensors"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {"basic-attributes" : ("basic_attributes", Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.BasicAttributes)}
                                        self._child_list_classes = {}

                                        self.number = YLeaf(YType.int32, "number")

                                        self.basic_attributes = Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.BasicAttributes()
                                        self.basic_attributes.parent = self
                                        self._children_name_map["basic_attributes"] = "basic-attributes"
                                        self._children_yang_names.add("basic-attributes")
                                        self._segment_path = lambda: "sensor" + "[number='" + self.number.get() + "']"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor, ['number'], name, value)


                                    class BasicAttributes(Entity):
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
                                            super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.BasicAttributes, self).__init__()

                                            self.yang_name = "basic-attributes"
                                            self.yang_parent_name = "sensor"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {"basic-info" : ("basic_info", Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.BasicAttributes.BasicInfo), "fru-info" : ("fru_info", Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.BasicAttributes.FruInfo)}
                                            self._child_list_classes = {}

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
                                                super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.BasicAttributes.BasicInfo, self).__init__()

                                                self.yang_name = "basic-info"
                                                self.yang_parent_name = "basic-attributes"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self._child_container_classes = {}
                                                self._child_list_classes = {}

                                                self.alias = YLeaf(YType.str, "alias")

                                                self.asset_id_str = YLeaf(YType.str, "asset-id-str")

                                                self.asset_identification = YLeaf(YType.int32, "asset-identification")

                                                self.ceport = YLeaf(YType.boolean, "ceport")

                                                self.chip_hardware_revision = YLeaf(YType.str, "chip-hardware-revision")

                                                self.composite_class_code = YLeaf(YType.int32, "composite-class-code")

                                                self.description = YLeaf(YType.str, "description")

                                                self.environmental_monitor_path = YLeaf(YType.str, "environmental-monitor-path")

                                                self.firmware_revision = YLeaf(YType.str, "firmware-revision")

                                                self.group_flag = YLeaf(YType.boolean, "group-flag")

                                                self.hardware_revision = YLeaf(YType.str, "hardware-revision")

                                                self.is_field_replaceable_unit = YLeaf(YType.boolean, "is-field-replaceable-unit")

                                                self.manufacturer_asset_tags = YLeaf(YType.int32, "manufacturer-asset-tags")

                                                self.manufacturer_name = YLeaf(YType.str, "manufacturer-name")

                                                self.memory_size = YLeaf(YType.int32, "memory-size")

                                                self.model_name = YLeaf(YType.str, "model-name")

                                                self.name = YLeaf(YType.str, "name")

                                                self.new_deviation_number = YLeaf(YType.int32, "new-deviation-number")

                                                self.physical_layer_interface_module_type = YLeaf(YType.int32, "physical-layer-interface-module-type")

                                                self.redundancystate = YLeaf(YType.int32, "redundancystate")

                                                self.serial_number = YLeaf(YType.str, "serial-number")

                                                self.software_revision = YLeaf(YType.str, "software-revision")

                                                self.unique_id = YLeaf(YType.int32, "unique-id")

                                                self.unrecognized_fru = YLeaf(YType.boolean, "unrecognized-fru")

                                                self.vendor_type = YLeaf(YType.str, "vendor-type")

                                                self.xr_scoped = YLeaf(YType.boolean, "xr-scoped")
                                                self._segment_path = lambda: "basic-info"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.BasicAttributes.BasicInfo, ['alias', 'asset_id_str', 'asset_identification', 'ceport', 'chip_hardware_revision', 'composite_class_code', 'description', 'environmental_monitor_path', 'firmware_revision', 'group_flag', 'hardware_revision', 'is_field_replaceable_unit', 'manufacturer_asset_tags', 'manufacturer_name', 'memory_size', 'model_name', 'name', 'new_deviation_number', 'physical_layer_interface_module_type', 'redundancystate', 'serial_number', 'software_revision', 'unique_id', 'unrecognized_fru', 'vendor_type', 'xr_scoped'], name, value)


                                        class FruInfo(Entity):
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
                                            	**type**\:   :py:class:`CardResetReason <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.CardResetReason>`
                                            
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
                                                super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.BasicAttributes.FruInfo, self).__init__()

                                                self.yang_name = "fru-info"
                                                self.yang_parent_name = "basic-attributes"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self._child_container_classes = {"card-up-time" : ("card_up_time", Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.BasicAttributes.FruInfo.CardUpTime), "last-operational-state-change" : ("last_operational_state_change", Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.BasicAttributes.FruInfo.LastOperationalStateChange)}
                                                self._child_list_classes = {}

                                                self.card_administrative_state = YLeaf(YType.int32, "card-administrative-state")

                                                self.card_monitor_state = YLeaf(YType.int32, "card-monitor-state")

                                                self.card_operational_state = YLeaf(YType.int32, "card-operational-state")

                                                self.card_reset_reason = YLeaf(YType.enumeration, "card-reset-reason")

                                                self.power_administrative_state = YLeaf(YType.int32, "power-administrative-state")

                                                self.power_current_measurement = YLeaf(YType.int32, "power-current-measurement")

                                                self.power_operational_state = YLeaf(YType.int32, "power-operational-state")

                                                self.card_up_time = Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.BasicAttributes.FruInfo.CardUpTime()
                                                self.card_up_time.parent = self
                                                self._children_name_map["card_up_time"] = "card-up-time"
                                                self._children_yang_names.add("card-up-time")

                                                self.last_operational_state_change = Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.BasicAttributes.FruInfo.LastOperationalStateChange()
                                                self.last_operational_state_change.parent = self
                                                self._children_name_map["last_operational_state_change"] = "last-operational-state-change"
                                                self._children_yang_names.add("last-operational-state-change")
                                                self._segment_path = lambda: "fru-info"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.BasicAttributes.FruInfo, ['card_administrative_state', 'card_monitor_state', 'card_operational_state', 'card_reset_reason', 'power_administrative_state', 'power_current_measurement', 'power_operational_state'], name, value)


                                            class CardUpTime(Entity):
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
                                                    super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.BasicAttributes.FruInfo.CardUpTime, self).__init__()

                                                    self.yang_name = "card-up-time"
                                                    self.yang_parent_name = "fru-info"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self._child_container_classes = {}
                                                    self._child_list_classes = {}

                                                    self.time_in_nano_seconds = YLeaf(YType.int32, "time-in-nano-seconds")

                                                    self.time_in_seconds = YLeaf(YType.int32, "time-in-seconds")
                                                    self._segment_path = lambda: "card-up-time"

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.BasicAttributes.FruInfo.CardUpTime, ['time_in_nano_seconds', 'time_in_seconds'], name, value)


                                            class LastOperationalStateChange(Entity):
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
                                                    super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.BasicAttributes.FruInfo.LastOperationalStateChange, self).__init__()

                                                    self.yang_name = "last-operational-state-change"
                                                    self.yang_parent_name = "fru-info"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self._child_container_classes = {}
                                                    self._child_list_classes = {}

                                                    self.time_in_nano_seconds = YLeaf(YType.int32, "time-in-nano-seconds")

                                                    self.time_in_seconds = YLeaf(YType.int32, "time-in-seconds")
                                                    self._segment_path = lambda: "last-operational-state-change"

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.BasicAttributes.FruInfo.LastOperationalStateChange, ['time_in_nano_seconds', 'time_in_seconds'], name, value)


                            class SubSlots(Entity):
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
                                    super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots, self).__init__()

                                    self.yang_name = "sub-slots"
                                    self.yang_parent_name = "card"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {"sub-slot" : ("sub_slot", Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot)}

                                    self.sub_slot = YList(self)
                                    self._segment_path = lambda: "sub-slots"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots, [], name, value)


                                class SubSlot(Entity):
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
                                        super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot, self).__init__()

                                        self.yang_name = "sub-slot"
                                        self.yang_parent_name = "sub-slots"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {"basic-attributes" : ("basic_attributes", Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.BasicAttributes), "module" : ("module", Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module)}
                                        self._child_list_classes = {}

                                        self.number = YLeaf(YType.int32, "number")

                                        self.basic_attributes = Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.BasicAttributes()
                                        self.basic_attributes.parent = self
                                        self._children_name_map["basic_attributes"] = "basic-attributes"
                                        self._children_yang_names.add("basic-attributes")

                                        self.module = Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module()
                                        self.module.parent = self
                                        self._children_name_map["module"] = "module"
                                        self._children_yang_names.add("module")
                                        self._segment_path = lambda: "sub-slot" + "[number='" + self.number.get() + "']"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot, ['number'], name, value)


                                    class BasicAttributes(Entity):
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
                                            super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.BasicAttributes, self).__init__()

                                            self.yang_name = "basic-attributes"
                                            self.yang_parent_name = "sub-slot"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {"basic-info" : ("basic_info", Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.BasicAttributes.BasicInfo), "fru-info" : ("fru_info", Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.BasicAttributes.FruInfo)}
                                            self._child_list_classes = {}

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
                                                super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.BasicAttributes.BasicInfo, self).__init__()

                                                self.yang_name = "basic-info"
                                                self.yang_parent_name = "basic-attributes"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self._child_container_classes = {}
                                                self._child_list_classes = {}

                                                self.alias = YLeaf(YType.str, "alias")

                                                self.asset_id_str = YLeaf(YType.str, "asset-id-str")

                                                self.asset_identification = YLeaf(YType.int32, "asset-identification")

                                                self.ceport = YLeaf(YType.boolean, "ceport")

                                                self.chip_hardware_revision = YLeaf(YType.str, "chip-hardware-revision")

                                                self.composite_class_code = YLeaf(YType.int32, "composite-class-code")

                                                self.description = YLeaf(YType.str, "description")

                                                self.environmental_monitor_path = YLeaf(YType.str, "environmental-monitor-path")

                                                self.firmware_revision = YLeaf(YType.str, "firmware-revision")

                                                self.group_flag = YLeaf(YType.boolean, "group-flag")

                                                self.hardware_revision = YLeaf(YType.str, "hardware-revision")

                                                self.is_field_replaceable_unit = YLeaf(YType.boolean, "is-field-replaceable-unit")

                                                self.manufacturer_asset_tags = YLeaf(YType.int32, "manufacturer-asset-tags")

                                                self.manufacturer_name = YLeaf(YType.str, "manufacturer-name")

                                                self.memory_size = YLeaf(YType.int32, "memory-size")

                                                self.model_name = YLeaf(YType.str, "model-name")

                                                self.name = YLeaf(YType.str, "name")

                                                self.new_deviation_number = YLeaf(YType.int32, "new-deviation-number")

                                                self.physical_layer_interface_module_type = YLeaf(YType.int32, "physical-layer-interface-module-type")

                                                self.redundancystate = YLeaf(YType.int32, "redundancystate")

                                                self.serial_number = YLeaf(YType.str, "serial-number")

                                                self.software_revision = YLeaf(YType.str, "software-revision")

                                                self.unique_id = YLeaf(YType.int32, "unique-id")

                                                self.unrecognized_fru = YLeaf(YType.boolean, "unrecognized-fru")

                                                self.vendor_type = YLeaf(YType.str, "vendor-type")

                                                self.xr_scoped = YLeaf(YType.boolean, "xr-scoped")
                                                self._segment_path = lambda: "basic-info"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.BasicAttributes.BasicInfo, ['alias', 'asset_id_str', 'asset_identification', 'ceport', 'chip_hardware_revision', 'composite_class_code', 'description', 'environmental_monitor_path', 'firmware_revision', 'group_flag', 'hardware_revision', 'is_field_replaceable_unit', 'manufacturer_asset_tags', 'manufacturer_name', 'memory_size', 'model_name', 'name', 'new_deviation_number', 'physical_layer_interface_module_type', 'redundancystate', 'serial_number', 'software_revision', 'unique_id', 'unrecognized_fru', 'vendor_type', 'xr_scoped'], name, value)


                                        class FruInfo(Entity):
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
                                            	**type**\:   :py:class:`CardResetReason <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.CardResetReason>`
                                            
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
                                                super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.BasicAttributes.FruInfo, self).__init__()

                                                self.yang_name = "fru-info"
                                                self.yang_parent_name = "basic-attributes"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self._child_container_classes = {"card-up-time" : ("card_up_time", Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.BasicAttributes.FruInfo.CardUpTime), "last-operational-state-change" : ("last_operational_state_change", Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.BasicAttributes.FruInfo.LastOperationalStateChange)}
                                                self._child_list_classes = {}

                                                self.card_administrative_state = YLeaf(YType.int32, "card-administrative-state")

                                                self.card_monitor_state = YLeaf(YType.int32, "card-monitor-state")

                                                self.card_operational_state = YLeaf(YType.int32, "card-operational-state")

                                                self.card_reset_reason = YLeaf(YType.enumeration, "card-reset-reason")

                                                self.power_administrative_state = YLeaf(YType.int32, "power-administrative-state")

                                                self.power_current_measurement = YLeaf(YType.int32, "power-current-measurement")

                                                self.power_operational_state = YLeaf(YType.int32, "power-operational-state")

                                                self.card_up_time = Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.BasicAttributes.FruInfo.CardUpTime()
                                                self.card_up_time.parent = self
                                                self._children_name_map["card_up_time"] = "card-up-time"
                                                self._children_yang_names.add("card-up-time")

                                                self.last_operational_state_change = Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.BasicAttributes.FruInfo.LastOperationalStateChange()
                                                self.last_operational_state_change.parent = self
                                                self._children_name_map["last_operational_state_change"] = "last-operational-state-change"
                                                self._children_yang_names.add("last-operational-state-change")
                                                self._segment_path = lambda: "fru-info"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.BasicAttributes.FruInfo, ['card_administrative_state', 'card_monitor_state', 'card_operational_state', 'card_reset_reason', 'power_administrative_state', 'power_current_measurement', 'power_operational_state'], name, value)


                                            class CardUpTime(Entity):
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
                                                    super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.BasicAttributes.FruInfo.CardUpTime, self).__init__()

                                                    self.yang_name = "card-up-time"
                                                    self.yang_parent_name = "fru-info"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self._child_container_classes = {}
                                                    self._child_list_classes = {}

                                                    self.time_in_nano_seconds = YLeaf(YType.int32, "time-in-nano-seconds")

                                                    self.time_in_seconds = YLeaf(YType.int32, "time-in-seconds")
                                                    self._segment_path = lambda: "card-up-time"

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.BasicAttributes.FruInfo.CardUpTime, ['time_in_nano_seconds', 'time_in_seconds'], name, value)


                                            class LastOperationalStateChange(Entity):
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
                                                    super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.BasicAttributes.FruInfo.LastOperationalStateChange, self).__init__()

                                                    self.yang_name = "last-operational-state-change"
                                                    self.yang_parent_name = "fru-info"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self._child_container_classes = {}
                                                    self._child_list_classes = {}

                                                    self.time_in_nano_seconds = YLeaf(YType.int32, "time-in-nano-seconds")

                                                    self.time_in_seconds = YLeaf(YType.int32, "time-in-seconds")
                                                    self._segment_path = lambda: "last-operational-state-change"

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.BasicAttributes.FruInfo.LastOperationalStateChange, ['time_in_nano_seconds', 'time_in_seconds'], name, value)


                                    class Module(Entity):
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
                                            super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module, self).__init__()

                                            self.yang_name = "module"
                                            self.yang_parent_name = "sub-slot"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {"basic-attributes" : ("basic_attributes", Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.BasicAttributes), "port-slots" : ("port_slots", Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots), "sensors" : ("sensors", Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors)}
                                            self._child_list_classes = {}

                                            self.basic_attributes = Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.BasicAttributes()
                                            self.basic_attributes.parent = self
                                            self._children_name_map["basic_attributes"] = "basic-attributes"
                                            self._children_yang_names.add("basic-attributes")

                                            self.port_slots = Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots()
                                            self.port_slots.parent = self
                                            self._children_name_map["port_slots"] = "port-slots"
                                            self._children_yang_names.add("port-slots")

                                            self.sensors = Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors()
                                            self.sensors.parent = self
                                            self._children_name_map["sensors"] = "sensors"
                                            self._children_yang_names.add("sensors")
                                            self._segment_path = lambda: "module"


                                        class BasicAttributes(Entity):
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
                                                super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.BasicAttributes, self).__init__()

                                                self.yang_name = "basic-attributes"
                                                self.yang_parent_name = "module"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self._child_container_classes = {"basic-info" : ("basic_info", Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.BasicAttributes.BasicInfo), "fru-info" : ("fru_info", Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.BasicAttributes.FruInfo)}
                                                self._child_list_classes = {}

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
                                                    super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.BasicAttributes.BasicInfo, self).__init__()

                                                    self.yang_name = "basic-info"
                                                    self.yang_parent_name = "basic-attributes"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self._child_container_classes = {}
                                                    self._child_list_classes = {}

                                                    self.alias = YLeaf(YType.str, "alias")

                                                    self.asset_id_str = YLeaf(YType.str, "asset-id-str")

                                                    self.asset_identification = YLeaf(YType.int32, "asset-identification")

                                                    self.ceport = YLeaf(YType.boolean, "ceport")

                                                    self.chip_hardware_revision = YLeaf(YType.str, "chip-hardware-revision")

                                                    self.composite_class_code = YLeaf(YType.int32, "composite-class-code")

                                                    self.description = YLeaf(YType.str, "description")

                                                    self.environmental_monitor_path = YLeaf(YType.str, "environmental-monitor-path")

                                                    self.firmware_revision = YLeaf(YType.str, "firmware-revision")

                                                    self.group_flag = YLeaf(YType.boolean, "group-flag")

                                                    self.hardware_revision = YLeaf(YType.str, "hardware-revision")

                                                    self.is_field_replaceable_unit = YLeaf(YType.boolean, "is-field-replaceable-unit")

                                                    self.manufacturer_asset_tags = YLeaf(YType.int32, "manufacturer-asset-tags")

                                                    self.manufacturer_name = YLeaf(YType.str, "manufacturer-name")

                                                    self.memory_size = YLeaf(YType.int32, "memory-size")

                                                    self.model_name = YLeaf(YType.str, "model-name")

                                                    self.name = YLeaf(YType.str, "name")

                                                    self.new_deviation_number = YLeaf(YType.int32, "new-deviation-number")

                                                    self.physical_layer_interface_module_type = YLeaf(YType.int32, "physical-layer-interface-module-type")

                                                    self.redundancystate = YLeaf(YType.int32, "redundancystate")

                                                    self.serial_number = YLeaf(YType.str, "serial-number")

                                                    self.software_revision = YLeaf(YType.str, "software-revision")

                                                    self.unique_id = YLeaf(YType.int32, "unique-id")

                                                    self.unrecognized_fru = YLeaf(YType.boolean, "unrecognized-fru")

                                                    self.vendor_type = YLeaf(YType.str, "vendor-type")

                                                    self.xr_scoped = YLeaf(YType.boolean, "xr-scoped")
                                                    self._segment_path = lambda: "basic-info"

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.BasicAttributes.BasicInfo, ['alias', 'asset_id_str', 'asset_identification', 'ceport', 'chip_hardware_revision', 'composite_class_code', 'description', 'environmental_monitor_path', 'firmware_revision', 'group_flag', 'hardware_revision', 'is_field_replaceable_unit', 'manufacturer_asset_tags', 'manufacturer_name', 'memory_size', 'model_name', 'name', 'new_deviation_number', 'physical_layer_interface_module_type', 'redundancystate', 'serial_number', 'software_revision', 'unique_id', 'unrecognized_fru', 'vendor_type', 'xr_scoped'], name, value)


                                            class FruInfo(Entity):
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
                                                	**type**\:   :py:class:`CardResetReason <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.CardResetReason>`
                                                
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
                                                    super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.BasicAttributes.FruInfo, self).__init__()

                                                    self.yang_name = "fru-info"
                                                    self.yang_parent_name = "basic-attributes"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self._child_container_classes = {"card-up-time" : ("card_up_time", Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.BasicAttributes.FruInfo.CardUpTime), "last-operational-state-change" : ("last_operational_state_change", Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.BasicAttributes.FruInfo.LastOperationalStateChange)}
                                                    self._child_list_classes = {}

                                                    self.card_administrative_state = YLeaf(YType.int32, "card-administrative-state")

                                                    self.card_monitor_state = YLeaf(YType.int32, "card-monitor-state")

                                                    self.card_operational_state = YLeaf(YType.int32, "card-operational-state")

                                                    self.card_reset_reason = YLeaf(YType.enumeration, "card-reset-reason")

                                                    self.power_administrative_state = YLeaf(YType.int32, "power-administrative-state")

                                                    self.power_current_measurement = YLeaf(YType.int32, "power-current-measurement")

                                                    self.power_operational_state = YLeaf(YType.int32, "power-operational-state")

                                                    self.card_up_time = Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.BasicAttributes.FruInfo.CardUpTime()
                                                    self.card_up_time.parent = self
                                                    self._children_name_map["card_up_time"] = "card-up-time"
                                                    self._children_yang_names.add("card-up-time")

                                                    self.last_operational_state_change = Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.BasicAttributes.FruInfo.LastOperationalStateChange()
                                                    self.last_operational_state_change.parent = self
                                                    self._children_name_map["last_operational_state_change"] = "last-operational-state-change"
                                                    self._children_yang_names.add("last-operational-state-change")
                                                    self._segment_path = lambda: "fru-info"

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.BasicAttributes.FruInfo, ['card_administrative_state', 'card_monitor_state', 'card_operational_state', 'card_reset_reason', 'power_administrative_state', 'power_current_measurement', 'power_operational_state'], name, value)


                                                class CardUpTime(Entity):
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
                                                        super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.BasicAttributes.FruInfo.CardUpTime, self).__init__()

                                                        self.yang_name = "card-up-time"
                                                        self.yang_parent_name = "fru-info"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self._child_container_classes = {}
                                                        self._child_list_classes = {}

                                                        self.time_in_nano_seconds = YLeaf(YType.int32, "time-in-nano-seconds")

                                                        self.time_in_seconds = YLeaf(YType.int32, "time-in-seconds")
                                                        self._segment_path = lambda: "card-up-time"

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.BasicAttributes.FruInfo.CardUpTime, ['time_in_nano_seconds', 'time_in_seconds'], name, value)


                                                class LastOperationalStateChange(Entity):
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
                                                        super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.BasicAttributes.FruInfo.LastOperationalStateChange, self).__init__()

                                                        self.yang_name = "last-operational-state-change"
                                                        self.yang_parent_name = "fru-info"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self._child_container_classes = {}
                                                        self._child_list_classes = {}

                                                        self.time_in_nano_seconds = YLeaf(YType.int32, "time-in-nano-seconds")

                                                        self.time_in_seconds = YLeaf(YType.int32, "time-in-seconds")
                                                        self._segment_path = lambda: "last-operational-state-change"

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.BasicAttributes.FruInfo.LastOperationalStateChange, ['time_in_nano_seconds', 'time_in_seconds'], name, value)


                                        class PortSlots(Entity):
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
                                                super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots, self).__init__()

                                                self.yang_name = "port-slots"
                                                self.yang_parent_name = "module"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self._child_container_classes = {}
                                                self._child_list_classes = {"port-slot" : ("port_slot", Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot)}

                                                self.port_slot = YList(self)
                                                self._segment_path = lambda: "port-slots"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots, [], name, value)


                                            class PortSlot(Entity):
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
                                                    super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot, self).__init__()

                                                    self.yang_name = "port-slot"
                                                    self.yang_parent_name = "port-slots"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self._child_container_classes = {"basic-attributes" : ("basic_attributes", Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.BasicAttributes), "port" : ("port", Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port)}
                                                    self._child_list_classes = {}

                                                    self.number = YLeaf(YType.int32, "number")

                                                    self.basic_attributes = Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.BasicAttributes()
                                                    self.basic_attributes.parent = self
                                                    self._children_name_map["basic_attributes"] = "basic-attributes"
                                                    self._children_yang_names.add("basic-attributes")

                                                    self.port = Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port()
                                                    self.port.parent = self
                                                    self._children_name_map["port"] = "port"
                                                    self._children_yang_names.add("port")
                                                    self._segment_path = lambda: "port-slot" + "[number='" + self.number.get() + "']"

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot, ['number'], name, value)


                                                class BasicAttributes(Entity):
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
                                                        super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.BasicAttributes, self).__init__()

                                                        self.yang_name = "basic-attributes"
                                                        self.yang_parent_name = "port-slot"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self._child_container_classes = {"basic-info" : ("basic_info", Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.BasicAttributes.BasicInfo), "fru-info" : ("fru_info", Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.BasicAttributes.FruInfo)}
                                                        self._child_list_classes = {}

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
                                                            super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.BasicAttributes.BasicInfo, self).__init__()

                                                            self.yang_name = "basic-info"
                                                            self.yang_parent_name = "basic-attributes"
                                                            self.is_top_level_class = False
                                                            self.has_list_ancestor = True
                                                            self._child_container_classes = {}
                                                            self._child_list_classes = {}

                                                            self.alias = YLeaf(YType.str, "alias")

                                                            self.asset_id_str = YLeaf(YType.str, "asset-id-str")

                                                            self.asset_identification = YLeaf(YType.int32, "asset-identification")

                                                            self.ceport = YLeaf(YType.boolean, "ceport")

                                                            self.chip_hardware_revision = YLeaf(YType.str, "chip-hardware-revision")

                                                            self.composite_class_code = YLeaf(YType.int32, "composite-class-code")

                                                            self.description = YLeaf(YType.str, "description")

                                                            self.environmental_monitor_path = YLeaf(YType.str, "environmental-monitor-path")

                                                            self.firmware_revision = YLeaf(YType.str, "firmware-revision")

                                                            self.group_flag = YLeaf(YType.boolean, "group-flag")

                                                            self.hardware_revision = YLeaf(YType.str, "hardware-revision")

                                                            self.is_field_replaceable_unit = YLeaf(YType.boolean, "is-field-replaceable-unit")

                                                            self.manufacturer_asset_tags = YLeaf(YType.int32, "manufacturer-asset-tags")

                                                            self.manufacturer_name = YLeaf(YType.str, "manufacturer-name")

                                                            self.memory_size = YLeaf(YType.int32, "memory-size")

                                                            self.model_name = YLeaf(YType.str, "model-name")

                                                            self.name = YLeaf(YType.str, "name")

                                                            self.new_deviation_number = YLeaf(YType.int32, "new-deviation-number")

                                                            self.physical_layer_interface_module_type = YLeaf(YType.int32, "physical-layer-interface-module-type")

                                                            self.redundancystate = YLeaf(YType.int32, "redundancystate")

                                                            self.serial_number = YLeaf(YType.str, "serial-number")

                                                            self.software_revision = YLeaf(YType.str, "software-revision")

                                                            self.unique_id = YLeaf(YType.int32, "unique-id")

                                                            self.unrecognized_fru = YLeaf(YType.boolean, "unrecognized-fru")

                                                            self.vendor_type = YLeaf(YType.str, "vendor-type")

                                                            self.xr_scoped = YLeaf(YType.boolean, "xr-scoped")
                                                            self._segment_path = lambda: "basic-info"

                                                        def __setattr__(self, name, value):
                                                            self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.BasicAttributes.BasicInfo, ['alias', 'asset_id_str', 'asset_identification', 'ceport', 'chip_hardware_revision', 'composite_class_code', 'description', 'environmental_monitor_path', 'firmware_revision', 'group_flag', 'hardware_revision', 'is_field_replaceable_unit', 'manufacturer_asset_tags', 'manufacturer_name', 'memory_size', 'model_name', 'name', 'new_deviation_number', 'physical_layer_interface_module_type', 'redundancystate', 'serial_number', 'software_revision', 'unique_id', 'unrecognized_fru', 'vendor_type', 'xr_scoped'], name, value)


                                                    class FruInfo(Entity):
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
                                                        	**type**\:   :py:class:`CardResetReason <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.CardResetReason>`
                                                        
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
                                                            super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.BasicAttributes.FruInfo, self).__init__()

                                                            self.yang_name = "fru-info"
                                                            self.yang_parent_name = "basic-attributes"
                                                            self.is_top_level_class = False
                                                            self.has_list_ancestor = True
                                                            self._child_container_classes = {"card-up-time" : ("card_up_time", Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.BasicAttributes.FruInfo.CardUpTime), "last-operational-state-change" : ("last_operational_state_change", Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.BasicAttributes.FruInfo.LastOperationalStateChange)}
                                                            self._child_list_classes = {}

                                                            self.card_administrative_state = YLeaf(YType.int32, "card-administrative-state")

                                                            self.card_monitor_state = YLeaf(YType.int32, "card-monitor-state")

                                                            self.card_operational_state = YLeaf(YType.int32, "card-operational-state")

                                                            self.card_reset_reason = YLeaf(YType.enumeration, "card-reset-reason")

                                                            self.power_administrative_state = YLeaf(YType.int32, "power-administrative-state")

                                                            self.power_current_measurement = YLeaf(YType.int32, "power-current-measurement")

                                                            self.power_operational_state = YLeaf(YType.int32, "power-operational-state")

                                                            self.card_up_time = Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.BasicAttributes.FruInfo.CardUpTime()
                                                            self.card_up_time.parent = self
                                                            self._children_name_map["card_up_time"] = "card-up-time"
                                                            self._children_yang_names.add("card-up-time")

                                                            self.last_operational_state_change = Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.BasicAttributes.FruInfo.LastOperationalStateChange()
                                                            self.last_operational_state_change.parent = self
                                                            self._children_name_map["last_operational_state_change"] = "last-operational-state-change"
                                                            self._children_yang_names.add("last-operational-state-change")
                                                            self._segment_path = lambda: "fru-info"

                                                        def __setattr__(self, name, value):
                                                            self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.BasicAttributes.FruInfo, ['card_administrative_state', 'card_monitor_state', 'card_operational_state', 'card_reset_reason', 'power_administrative_state', 'power_current_measurement', 'power_operational_state'], name, value)


                                                        class CardUpTime(Entity):
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
                                                                super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.BasicAttributes.FruInfo.CardUpTime, self).__init__()

                                                                self.yang_name = "card-up-time"
                                                                self.yang_parent_name = "fru-info"
                                                                self.is_top_level_class = False
                                                                self.has_list_ancestor = True
                                                                self._child_container_classes = {}
                                                                self._child_list_classes = {}

                                                                self.time_in_nano_seconds = YLeaf(YType.int32, "time-in-nano-seconds")

                                                                self.time_in_seconds = YLeaf(YType.int32, "time-in-seconds")
                                                                self._segment_path = lambda: "card-up-time"

                                                            def __setattr__(self, name, value):
                                                                self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.BasicAttributes.FruInfo.CardUpTime, ['time_in_nano_seconds', 'time_in_seconds'], name, value)


                                                        class LastOperationalStateChange(Entity):
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
                                                                super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.BasicAttributes.FruInfo.LastOperationalStateChange, self).__init__()

                                                                self.yang_name = "last-operational-state-change"
                                                                self.yang_parent_name = "fru-info"
                                                                self.is_top_level_class = False
                                                                self.has_list_ancestor = True
                                                                self._child_container_classes = {}
                                                                self._child_list_classes = {}

                                                                self.time_in_nano_seconds = YLeaf(YType.int32, "time-in-nano-seconds")

                                                                self.time_in_seconds = YLeaf(YType.int32, "time-in-seconds")
                                                                self._segment_path = lambda: "last-operational-state-change"

                                                            def __setattr__(self, name, value):
                                                                self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.BasicAttributes.FruInfo.LastOperationalStateChange, ['time_in_nano_seconds', 'time_in_seconds'], name, value)


                                                class Port(Entity):
                                                    """
                                                    Port string
                                                    
                                                    .. attribute:: basic_attributes
                                                    
                                                    	Attributes
                                                    	**type**\:   :py:class:`BasicAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.BasicAttributes>`
                                                    
                                                    

                                                    """

                                                    _prefix = 'asr9k-sc-invmgr-admin-oper'
                                                    _revision = '2017-01-04'

                                                    def __init__(self):
                                                        super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port, self).__init__()

                                                        self.yang_name = "port"
                                                        self.yang_parent_name = "port-slot"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self._child_container_classes = {"basic-attributes" : ("basic_attributes", Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.BasicAttributes)}
                                                        self._child_list_classes = {}

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
                                                        	**type**\:   :py:class:`BasicInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.BasicAttributes.BasicInfo>`
                                                        
                                                        .. attribute:: fru_info
                                                        
                                                        	Field Replaceable Unit (FRU) inventory information
                                                        	**type**\:   :py:class:`FruInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.BasicAttributes.FruInfo>`
                                                        
                                                        

                                                        """

                                                        _prefix = 'asr9k-sc-invmgr-admin-oper'
                                                        _revision = '2017-01-04'

                                                        def __init__(self):
                                                            super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.BasicAttributes, self).__init__()

                                                            self.yang_name = "basic-attributes"
                                                            self.yang_parent_name = "port"
                                                            self.is_top_level_class = False
                                                            self.has_list_ancestor = True
                                                            self._child_container_classes = {"basic-info" : ("basic_info", Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.BasicAttributes.BasicInfo), "fru-info" : ("fru_info", Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.BasicAttributes.FruInfo)}
                                                            self._child_list_classes = {}

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
                                                                super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.BasicAttributes.BasicInfo, self).__init__()

                                                                self.yang_name = "basic-info"
                                                                self.yang_parent_name = "basic-attributes"
                                                                self.is_top_level_class = False
                                                                self.has_list_ancestor = True
                                                                self._child_container_classes = {}
                                                                self._child_list_classes = {}

                                                                self.alias = YLeaf(YType.str, "alias")

                                                                self.asset_id_str = YLeaf(YType.str, "asset-id-str")

                                                                self.asset_identification = YLeaf(YType.int32, "asset-identification")

                                                                self.ceport = YLeaf(YType.boolean, "ceport")

                                                                self.chip_hardware_revision = YLeaf(YType.str, "chip-hardware-revision")

                                                                self.composite_class_code = YLeaf(YType.int32, "composite-class-code")

                                                                self.description = YLeaf(YType.str, "description")

                                                                self.environmental_monitor_path = YLeaf(YType.str, "environmental-monitor-path")

                                                                self.firmware_revision = YLeaf(YType.str, "firmware-revision")

                                                                self.group_flag = YLeaf(YType.boolean, "group-flag")

                                                                self.hardware_revision = YLeaf(YType.str, "hardware-revision")

                                                                self.is_field_replaceable_unit = YLeaf(YType.boolean, "is-field-replaceable-unit")

                                                                self.manufacturer_asset_tags = YLeaf(YType.int32, "manufacturer-asset-tags")

                                                                self.manufacturer_name = YLeaf(YType.str, "manufacturer-name")

                                                                self.memory_size = YLeaf(YType.int32, "memory-size")

                                                                self.model_name = YLeaf(YType.str, "model-name")

                                                                self.name = YLeaf(YType.str, "name")

                                                                self.new_deviation_number = YLeaf(YType.int32, "new-deviation-number")

                                                                self.physical_layer_interface_module_type = YLeaf(YType.int32, "physical-layer-interface-module-type")

                                                                self.redundancystate = YLeaf(YType.int32, "redundancystate")

                                                                self.serial_number = YLeaf(YType.str, "serial-number")

                                                                self.software_revision = YLeaf(YType.str, "software-revision")

                                                                self.unique_id = YLeaf(YType.int32, "unique-id")

                                                                self.unrecognized_fru = YLeaf(YType.boolean, "unrecognized-fru")

                                                                self.vendor_type = YLeaf(YType.str, "vendor-type")

                                                                self.xr_scoped = YLeaf(YType.boolean, "xr-scoped")
                                                                self._segment_path = lambda: "basic-info"

                                                            def __setattr__(self, name, value):
                                                                self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.BasicAttributes.BasicInfo, ['alias', 'asset_id_str', 'asset_identification', 'ceport', 'chip_hardware_revision', 'composite_class_code', 'description', 'environmental_monitor_path', 'firmware_revision', 'group_flag', 'hardware_revision', 'is_field_replaceable_unit', 'manufacturer_asset_tags', 'manufacturer_name', 'memory_size', 'model_name', 'name', 'new_deviation_number', 'physical_layer_interface_module_type', 'redundancystate', 'serial_number', 'software_revision', 'unique_id', 'unrecognized_fru', 'vendor_type', 'xr_scoped'], name, value)


                                                        class FruInfo(Entity):
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
                                                            	**type**\:   :py:class:`CardResetReason <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.CardResetReason>`
                                                            
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
                                                                super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.BasicAttributes.FruInfo, self).__init__()

                                                                self.yang_name = "fru-info"
                                                                self.yang_parent_name = "basic-attributes"
                                                                self.is_top_level_class = False
                                                                self.has_list_ancestor = True
                                                                self._child_container_classes = {"card-up-time" : ("card_up_time", Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.BasicAttributes.FruInfo.CardUpTime), "last-operational-state-change" : ("last_operational_state_change", Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.BasicAttributes.FruInfo.LastOperationalStateChange)}
                                                                self._child_list_classes = {}

                                                                self.card_administrative_state = YLeaf(YType.int32, "card-administrative-state")

                                                                self.card_monitor_state = YLeaf(YType.int32, "card-monitor-state")

                                                                self.card_operational_state = YLeaf(YType.int32, "card-operational-state")

                                                                self.card_reset_reason = YLeaf(YType.enumeration, "card-reset-reason")

                                                                self.power_administrative_state = YLeaf(YType.int32, "power-administrative-state")

                                                                self.power_current_measurement = YLeaf(YType.int32, "power-current-measurement")

                                                                self.power_operational_state = YLeaf(YType.int32, "power-operational-state")

                                                                self.card_up_time = Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.BasicAttributes.FruInfo.CardUpTime()
                                                                self.card_up_time.parent = self
                                                                self._children_name_map["card_up_time"] = "card-up-time"
                                                                self._children_yang_names.add("card-up-time")

                                                                self.last_operational_state_change = Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.BasicAttributes.FruInfo.LastOperationalStateChange()
                                                                self.last_operational_state_change.parent = self
                                                                self._children_name_map["last_operational_state_change"] = "last-operational-state-change"
                                                                self._children_yang_names.add("last-operational-state-change")
                                                                self._segment_path = lambda: "fru-info"

                                                            def __setattr__(self, name, value):
                                                                self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.BasicAttributes.FruInfo, ['card_administrative_state', 'card_monitor_state', 'card_operational_state', 'card_reset_reason', 'power_administrative_state', 'power_current_measurement', 'power_operational_state'], name, value)


                                                            class CardUpTime(Entity):
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
                                                                    super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.BasicAttributes.FruInfo.CardUpTime, self).__init__()

                                                                    self.yang_name = "card-up-time"
                                                                    self.yang_parent_name = "fru-info"
                                                                    self.is_top_level_class = False
                                                                    self.has_list_ancestor = True
                                                                    self._child_container_classes = {}
                                                                    self._child_list_classes = {}

                                                                    self.time_in_nano_seconds = YLeaf(YType.int32, "time-in-nano-seconds")

                                                                    self.time_in_seconds = YLeaf(YType.int32, "time-in-seconds")
                                                                    self._segment_path = lambda: "card-up-time"

                                                                def __setattr__(self, name, value):
                                                                    self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.BasicAttributes.FruInfo.CardUpTime, ['time_in_nano_seconds', 'time_in_seconds'], name, value)


                                                            class LastOperationalStateChange(Entity):
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
                                                                    super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.BasicAttributes.FruInfo.LastOperationalStateChange, self).__init__()

                                                                    self.yang_name = "last-operational-state-change"
                                                                    self.yang_parent_name = "fru-info"
                                                                    self.is_top_level_class = False
                                                                    self.has_list_ancestor = True
                                                                    self._child_container_classes = {}
                                                                    self._child_list_classes = {}

                                                                    self.time_in_nano_seconds = YLeaf(YType.int32, "time-in-nano-seconds")

                                                                    self.time_in_seconds = YLeaf(YType.int32, "time-in-seconds")
                                                                    self._segment_path = lambda: "last-operational-state-change"

                                                                def __setattr__(self, name, value):
                                                                    self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.BasicAttributes.FruInfo.LastOperationalStateChange, ['time_in_nano_seconds', 'time_in_seconds'], name, value)


                                        class Sensors(Entity):
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
                                                super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors, self).__init__()

                                                self.yang_name = "sensors"
                                                self.yang_parent_name = "module"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self._child_container_classes = {}
                                                self._child_list_classes = {"sensor" : ("sensor", Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor)}

                                                self.sensor = YList(self)
                                                self._segment_path = lambda: "sensors"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors, [], name, value)


                                            class Sensor(Entity):
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
                                                    super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor, self).__init__()

                                                    self.yang_name = "sensor"
                                                    self.yang_parent_name = "sensors"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self._child_container_classes = {"basic-attributes" : ("basic_attributes", Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.BasicAttributes)}
                                                    self._child_list_classes = {}

                                                    self.number = YLeaf(YType.int32, "number")

                                                    self.basic_attributes = Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.BasicAttributes()
                                                    self.basic_attributes.parent = self
                                                    self._children_name_map["basic_attributes"] = "basic-attributes"
                                                    self._children_yang_names.add("basic-attributes")
                                                    self._segment_path = lambda: "sensor" + "[number='" + self.number.get() + "']"

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor, ['number'], name, value)


                                                class BasicAttributes(Entity):
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
                                                        super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.BasicAttributes, self).__init__()

                                                        self.yang_name = "basic-attributes"
                                                        self.yang_parent_name = "sensor"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self._child_container_classes = {"basic-info" : ("basic_info", Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.BasicAttributes.BasicInfo), "fru-info" : ("fru_info", Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.BasicAttributes.FruInfo)}
                                                        self._child_list_classes = {}

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
                                                            super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.BasicAttributes.BasicInfo, self).__init__()

                                                            self.yang_name = "basic-info"
                                                            self.yang_parent_name = "basic-attributes"
                                                            self.is_top_level_class = False
                                                            self.has_list_ancestor = True
                                                            self._child_container_classes = {}
                                                            self._child_list_classes = {}

                                                            self.alias = YLeaf(YType.str, "alias")

                                                            self.asset_id_str = YLeaf(YType.str, "asset-id-str")

                                                            self.asset_identification = YLeaf(YType.int32, "asset-identification")

                                                            self.ceport = YLeaf(YType.boolean, "ceport")

                                                            self.chip_hardware_revision = YLeaf(YType.str, "chip-hardware-revision")

                                                            self.composite_class_code = YLeaf(YType.int32, "composite-class-code")

                                                            self.description = YLeaf(YType.str, "description")

                                                            self.environmental_monitor_path = YLeaf(YType.str, "environmental-monitor-path")

                                                            self.firmware_revision = YLeaf(YType.str, "firmware-revision")

                                                            self.group_flag = YLeaf(YType.boolean, "group-flag")

                                                            self.hardware_revision = YLeaf(YType.str, "hardware-revision")

                                                            self.is_field_replaceable_unit = YLeaf(YType.boolean, "is-field-replaceable-unit")

                                                            self.manufacturer_asset_tags = YLeaf(YType.int32, "manufacturer-asset-tags")

                                                            self.manufacturer_name = YLeaf(YType.str, "manufacturer-name")

                                                            self.memory_size = YLeaf(YType.int32, "memory-size")

                                                            self.model_name = YLeaf(YType.str, "model-name")

                                                            self.name = YLeaf(YType.str, "name")

                                                            self.new_deviation_number = YLeaf(YType.int32, "new-deviation-number")

                                                            self.physical_layer_interface_module_type = YLeaf(YType.int32, "physical-layer-interface-module-type")

                                                            self.redundancystate = YLeaf(YType.int32, "redundancystate")

                                                            self.serial_number = YLeaf(YType.str, "serial-number")

                                                            self.software_revision = YLeaf(YType.str, "software-revision")

                                                            self.unique_id = YLeaf(YType.int32, "unique-id")

                                                            self.unrecognized_fru = YLeaf(YType.boolean, "unrecognized-fru")

                                                            self.vendor_type = YLeaf(YType.str, "vendor-type")

                                                            self.xr_scoped = YLeaf(YType.boolean, "xr-scoped")
                                                            self._segment_path = lambda: "basic-info"

                                                        def __setattr__(self, name, value):
                                                            self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.BasicAttributes.BasicInfo, ['alias', 'asset_id_str', 'asset_identification', 'ceport', 'chip_hardware_revision', 'composite_class_code', 'description', 'environmental_monitor_path', 'firmware_revision', 'group_flag', 'hardware_revision', 'is_field_replaceable_unit', 'manufacturer_asset_tags', 'manufacturer_name', 'memory_size', 'model_name', 'name', 'new_deviation_number', 'physical_layer_interface_module_type', 'redundancystate', 'serial_number', 'software_revision', 'unique_id', 'unrecognized_fru', 'vendor_type', 'xr_scoped'], name, value)


                                                    class FruInfo(Entity):
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
                                                        	**type**\:   :py:class:`CardResetReason <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper.CardResetReason>`
                                                        
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
                                                            super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.BasicAttributes.FruInfo, self).__init__()

                                                            self.yang_name = "fru-info"
                                                            self.yang_parent_name = "basic-attributes"
                                                            self.is_top_level_class = False
                                                            self.has_list_ancestor = True
                                                            self._child_container_classes = {"card-up-time" : ("card_up_time", Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.BasicAttributes.FruInfo.CardUpTime), "last-operational-state-change" : ("last_operational_state_change", Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.BasicAttributes.FruInfo.LastOperationalStateChange)}
                                                            self._child_list_classes = {}

                                                            self.card_administrative_state = YLeaf(YType.int32, "card-administrative-state")

                                                            self.card_monitor_state = YLeaf(YType.int32, "card-monitor-state")

                                                            self.card_operational_state = YLeaf(YType.int32, "card-operational-state")

                                                            self.card_reset_reason = YLeaf(YType.enumeration, "card-reset-reason")

                                                            self.power_administrative_state = YLeaf(YType.int32, "power-administrative-state")

                                                            self.power_current_measurement = YLeaf(YType.int32, "power-current-measurement")

                                                            self.power_operational_state = YLeaf(YType.int32, "power-operational-state")

                                                            self.card_up_time = Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.BasicAttributes.FruInfo.CardUpTime()
                                                            self.card_up_time.parent = self
                                                            self._children_name_map["card_up_time"] = "card-up-time"
                                                            self._children_yang_names.add("card-up-time")

                                                            self.last_operational_state_change = Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.BasicAttributes.FruInfo.LastOperationalStateChange()
                                                            self.last_operational_state_change.parent = self
                                                            self._children_name_map["last_operational_state_change"] = "last-operational-state-change"
                                                            self._children_yang_names.add("last-operational-state-change")
                                                            self._segment_path = lambda: "fru-info"

                                                        def __setattr__(self, name, value):
                                                            self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.BasicAttributes.FruInfo, ['card_administrative_state', 'card_monitor_state', 'card_operational_state', 'card_reset_reason', 'power_administrative_state', 'power_current_measurement', 'power_operational_state'], name, value)


                                                        class CardUpTime(Entity):
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
                                                                super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.BasicAttributes.FruInfo.CardUpTime, self).__init__()

                                                                self.yang_name = "card-up-time"
                                                                self.yang_parent_name = "fru-info"
                                                                self.is_top_level_class = False
                                                                self.has_list_ancestor = True
                                                                self._child_container_classes = {}
                                                                self._child_list_classes = {}

                                                                self.time_in_nano_seconds = YLeaf(YType.int32, "time-in-nano-seconds")

                                                                self.time_in_seconds = YLeaf(YType.int32, "time-in-seconds")
                                                                self._segment_path = lambda: "card-up-time"

                                                            def __setattr__(self, name, value):
                                                                self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.BasicAttributes.FruInfo.CardUpTime, ['time_in_nano_seconds', 'time_in_seconds'], name, value)


                                                        class LastOperationalStateChange(Entity):
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
                                                                super(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.BasicAttributes.FruInfo.LastOperationalStateChange, self).__init__()

                                                                self.yang_name = "last-operational-state-change"
                                                                self.yang_parent_name = "fru-info"
                                                                self.is_top_level_class = False
                                                                self.has_list_ancestor = True
                                                                self._child_container_classes = {}
                                                                self._child_list_classes = {}

                                                                self.time_in_nano_seconds = YLeaf(YType.int32, "time-in-nano-seconds")

                                                                self.time_in_seconds = YLeaf(YType.int32, "time-in-seconds")
                                                                self._segment_path = lambda: "last-operational-state-change"

                                                            def __setattr__(self, name, value):
                                                                self._perform_setattr(Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.BasicAttributes.FruInfo.LastOperationalStateChange, ['time_in_nano_seconds', 'time_in_seconds'], name, value)

    def clone_ptr(self):
        self._top_entity = Inventory()
        return self._top_entity

