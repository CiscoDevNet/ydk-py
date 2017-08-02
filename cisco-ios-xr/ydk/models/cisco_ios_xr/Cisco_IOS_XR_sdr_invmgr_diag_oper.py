""" Cisco_IOS_XR_sdr_invmgr_diag_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR sdr\-invmgr\-diag package operational data.

This module contains definitions
for the following management objects\:
  diag\: Diag information

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Diag(Entity):
    """
    Diag information
    
    .. attribute:: racks
    
    	Table of racks
    	**type**\:   :py:class:`Racks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sdr_invmgr_diag_oper.Diag.Racks>`
    
    

    """

    _prefix = 'sdr-invmgr-diag-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(Diag, self).__init__()
        self._top_entity = None

        self.yang_name = "diag"
        self.yang_parent_name = "Cisco-IOS-XR-sdr-invmgr-diag-oper"

        self.racks = Diag.Racks()
        self.racks.parent = self
        self._children_name_map["racks"] = "racks"
        self._children_yang_names.add("racks")


    class Racks(Entity):
        """
        Table of racks
        
        .. attribute:: rack
        
        	Rack name
        	**type**\: list of    :py:class:`Rack <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sdr_invmgr_diag_oper.Diag.Racks.Rack>`
        
        

        """

        _prefix = 'sdr-invmgr-diag-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Diag.Racks, self).__init__()

            self.yang_name = "racks"
            self.yang_parent_name = "diag"

            self.rack = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Diag.Racks, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Diag.Racks, self).__setattr__(name, value)


        class Rack(Entity):
            """
            Rack name
            
            .. attribute:: rack_name  <key>
            
            	Rack name
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: chassis
            
            	Chassis information
            	**type**\:   :py:class:`Chassis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sdr_invmgr_diag_oper.Diag.Racks.Rack.Chassis>`
            
            .. attribute:: fan_traies
            
            	Table for rack fan trays
            	**type**\:   :py:class:`FanTraies <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sdr_invmgr_diag_oper.Diag.Racks.Rack.FanTraies>`
            
            .. attribute:: power_shelfs
            
            	Table for rack power shelf 
            	**type**\:   :py:class:`PowerShelfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sdr_invmgr_diag_oper.Diag.Racks.Rack.PowerShelfs>`
            
            .. attribute:: slots
            
            	Table of slots
            	**type**\:   :py:class:`Slots <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sdr_invmgr_diag_oper.Diag.Racks.Rack.Slots>`
            
            

            """

            _prefix = 'sdr-invmgr-diag-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Diag.Racks.Rack, self).__init__()

                self.yang_name = "rack"
                self.yang_parent_name = "racks"

                self.rack_name = YLeaf(YType.str, "rack-name")

                self.chassis = Diag.Racks.Rack.Chassis()
                self.chassis.parent = self
                self._children_name_map["chassis"] = "chassis"
                self._children_yang_names.add("chassis")

                self.fan_traies = Diag.Racks.Rack.FanTraies()
                self.fan_traies.parent = self
                self._children_name_map["fan_traies"] = "fan-traies"
                self._children_yang_names.add("fan-traies")

                self.power_shelfs = Diag.Racks.Rack.PowerShelfs()
                self.power_shelfs.parent = self
                self._children_name_map["power_shelfs"] = "power-shelfs"
                self._children_yang_names.add("power-shelfs")

                self.slots = Diag.Racks.Rack.Slots()
                self.slots.parent = self
                self._children_name_map["slots"] = "slots"
                self._children_yang_names.add("slots")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("rack_name") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Diag.Racks.Rack, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Diag.Racks.Rack, self).__setattr__(name, value)


            class PowerShelfs(Entity):
                """
                Table for rack power shelf 
                
                .. attribute:: power_shelf
                
                	Power shelf name
                	**type**\: list of    :py:class:`PowerShelf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sdr_invmgr_diag_oper.Diag.Racks.Rack.PowerShelfs.PowerShelf>`
                
                

                """

                _prefix = 'sdr-invmgr-diag-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Diag.Racks.Rack.PowerShelfs, self).__init__()

                    self.yang_name = "power-shelfs"
                    self.yang_parent_name = "rack"

                    self.power_shelf = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in () and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Diag.Racks.Rack.PowerShelfs, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Diag.Racks.Rack.PowerShelfs, self).__setattr__(name, value)


                class PowerShelf(Entity):
                    """
                    Power shelf name
                    
                    .. attribute:: power_shelf_name  <key>
                    
                    	Power Shelf name
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: power_supplies
                    
                    	Table for rack power supply 
                    	**type**\:   :py:class:`PowerSupplies <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sdr_invmgr_diag_oper.Diag.Racks.Rack.PowerShelfs.PowerShelf.PowerSupplies>`
                    
                    

                    """

                    _prefix = 'sdr-invmgr-diag-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Diag.Racks.Rack.PowerShelfs.PowerShelf, self).__init__()

                        self.yang_name = "power-shelf"
                        self.yang_parent_name = "power-shelfs"

                        self.power_shelf_name = YLeaf(YType.str, "power-shelf-name")

                        self.power_supplies = Diag.Racks.Rack.PowerShelfs.PowerShelf.PowerSupplies()
                        self.power_supplies.parent = self
                        self._children_name_map["power_supplies"] = "power-supplies"
                        self._children_yang_names.add("power-supplies")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("power_shelf_name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Diag.Racks.Rack.PowerShelfs.PowerShelf, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Diag.Racks.Rack.PowerShelfs.PowerShelf, self).__setattr__(name, value)


                    class PowerSupplies(Entity):
                        """
                        Table for rack power supply 
                        
                        .. attribute:: power_supply
                        
                        	Power Supply name
                        	**type**\: list of    :py:class:`PowerSupply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sdr_invmgr_diag_oper.Diag.Racks.Rack.PowerShelfs.PowerShelf.PowerSupplies.PowerSupply>`
                        
                        

                        """

                        _prefix = 'sdr-invmgr-diag-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Diag.Racks.Rack.PowerShelfs.PowerShelf.PowerSupplies, self).__init__()

                            self.yang_name = "power-supplies"
                            self.yang_parent_name = "power-shelf"

                            self.power_supply = YList(self)

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in () and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Diag.Racks.Rack.PowerShelfs.PowerShelf.PowerSupplies, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Diag.Racks.Rack.PowerShelfs.PowerShelf.PowerSupplies, self).__setattr__(name, value)


                        class PowerSupply(Entity):
                            """
                            Power Supply name
                            
                            .. attribute:: power_supply_name  <key>
                            
                            	Power Supply name
                            	**type**\:  str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            .. attribute:: information
                            
                            	Basic information
                            	**type**\:   :py:class:`Information <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sdr_invmgr_diag_oper.Diag.Racks.Rack.PowerShelfs.PowerShelf.PowerSupplies.PowerSupply.Information>`
                            
                            

                            """

                            _prefix = 'sdr-invmgr-diag-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Diag.Racks.Rack.PowerShelfs.PowerShelf.PowerSupplies.PowerSupply, self).__init__()

                                self.yang_name = "power-supply"
                                self.yang_parent_name = "power-supplies"

                                self.power_supply_name = YLeaf(YType.str, "power-supply-name")

                                self.information = Diag.Racks.Rack.PowerShelfs.PowerShelf.PowerSupplies.PowerSupply.Information()
                                self.information.parent = self
                                self._children_name_map["information"] = "information"
                                self._children_yang_names.add("information")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("power_supply_name") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Diag.Racks.Rack.PowerShelfs.PowerShelf.PowerSupplies.PowerSupply, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Diag.Racks.Rack.PowerShelfs.PowerShelf.PowerSupplies.PowerSupply, self).__setattr__(name, value)


                            class Information(Entity):
                                """
                                Basic information
                                
                                .. attribute:: asset_alias
                                
                                	Asset Alias
                                	**type**\:  str
                                
                                	**length:** 0..255
                                
                                .. attribute:: asset_id
                                
                                	Asset ID
                                	**type**\:  str
                                
                                	**length:** 0..255
                                
                                .. attribute:: base_mac_address1
                                
                                	Base Mac Address #1
                                	**type**\:  str
                                
                                	**length:** 0..255
                                
                                .. attribute:: base_mac_address2
                                
                                	Base Mac Address #2
                                	**type**\:  str
                                
                                	**length:** 0..255
                                
                                .. attribute:: base_mac_address3
                                
                                	Base Mac Address #3
                                	**type**\:  str
                                
                                	**length:** 0..255
                                
                                .. attribute:: base_mac_address4
                                
                                	Base Mac Address #4
                                	**type**\:  str
                                
                                	**length:** 0..255
                                
                                .. attribute:: block_checksum
                                
                                	Block Checksum
                                	**type**\:  str
                                
                                	**length:** 0..255
                                
                                .. attribute:: block_count
                                
                                	Block Count
                                	**type**\:  str
                                
                                	**length:** 0..255
                                
                                .. attribute:: block_length
                                
                                	Block Length
                                	**type**\:  str
                                
                                	**length:** 0..255
                                
                                .. attribute:: block_signature
                                
                                	Block Signature
                                	**type**\:  str
                                
                                	**length:** 0..255
                                
                                .. attribute:: block_version
                                
                                	Block Version
                                	**type**\:  str
                                
                                	**length:** 0..255
                                
                                .. attribute:: chassis_sid
                                
                                	Chassis serial number
                                	**type**\:  str
                                
                                	**length:** 0..255
                                
                                .. attribute:: clei
                                
                                	Common Language Equipment Identifier (CLEI) code
                                	**type**\:  str
                                
                                	**length:** 0..255
                                
                                .. attribute:: controller_family
                                
                                	Controller family
                                	**type**\:  str
                                
                                	**length:** 0..255
                                
                                .. attribute:: controller_type
                                
                                	Controller type
                                	**type**\:  str
                                
                                	**length:** 0..255
                                
                                .. attribute:: description
                                
                                	A textual description of physical entity
                                	**type**\:  str
                                
                                	**length:** 0..255
                                
                                .. attribute:: dev_num1
                                
                                	Deviation Number # 1
                                	**type**\:  str
                                
                                	**length:** 0..255
                                
                                .. attribute:: dev_num2
                                
                                	Deviation Number # 2
                                	**type**\:  str
                                
                                	**length:** 0..255
                                
                                .. attribute:: dev_num3
                                
                                	Deviation Number # 3
                                	**type**\:  str
                                
                                	**length:** 0..255
                                
                                .. attribute:: dev_num4
                                
                                	Deviation Number # 4
                                	**type**\:  str
                                
                                	**length:** 0..255
                                
                                .. attribute:: dev_num5
                                
                                	Deviation Number # 5
                                	**type**\:  str
                                
                                	**length:** 0..255
                                
                                .. attribute:: dev_num6
                                
                                	Deviation Number # 6
                                	**type**\:  str
                                
                                	**length:** 0..255
                                
                                .. attribute:: dev_num7
                                
                                	Deviation Number # 7
                                	**type**\:  str
                                
                                	**length:** 0..255
                                
                                .. attribute:: eci
                                
                                	Equipment Catalog Item (ECI) number
                                	**type**\:  str
                                
                                	**length:** 0..255
                                
                                .. attribute:: eeprom_size
                                
                                	EEPROM Size
                                	**type**\:  str
                                
                                	**length:** 0..255
                                
                                .. attribute:: engineer_use
                                
                                	Engineer Use
                                	**type**\:  str
                                
                                	**length:** 0..255
                                
                                .. attribute:: fru_major_type
                                
                                	FRU Major Type
                                	**type**\:  str
                                
                                	**length:** 0..255
                                
                                .. attribute:: fru_minor_type
                                
                                	FRU Minor Type
                                	**type**\:  str
                                
                                	**length:** 0..255
                                
                                .. attribute:: hw_version
                                
                                	Hardware Version
                                	**type**\:  str
                                
                                	**length:** 0..255
                                
                                .. attribute:: hwid
                                
                                	Hardware Revision
                                	**type**\:  str
                                
                                	**length:** 0..255
                                
                                .. attribute:: idprom_format_rev
                                
                                	IDPROM Format Revision
                                	**type**\:  str
                                
                                	**length:** 0..255
                                
                                .. attribute:: mac_add_blk_size1
                                
                                	Mac Address Block Size #1
                                	**type**\:  str
                                
                                	**length:** 0..255
                                
                                .. attribute:: mac_add_blk_size2
                                
                                	Mac Address Block Size #2
                                	**type**\:  str
                                
                                	**length:** 0..255
                                
                                .. attribute:: mac_add_blk_size3
                                
                                	Mac Address Block Size #3
                                	**type**\:  str
                                
                                	**length:** 0..255
                                
                                .. attribute:: mac_add_blk_size4
                                
                                	Mac Address Block Size #4
                                	**type**\:  str
                                
                                	**length:** 0..255
                                
                                .. attribute:: manu_test_data
                                
                                	Manufacturing Test Data
                                	**type**\:  str
                                
                                	**length:** 0..255
                                
                                .. attribute:: mfg_bits
                                
                                	MFG Bits
                                	**type**\:  str
                                
                                	**length:** 0..255
                                
                                .. attribute:: mfg_deviation
                                
                                	MFG Deviation
                                	**type**\:  str
                                
                                	**length:** 0..255
                                
                                .. attribute:: oem_string
                                
                                	OEM String
                                	**type**\:  str
                                
                                	**length:** 0..255
                                
                                .. attribute:: part_number
                                
                                	Part Number
                                	**type**\:  str
                                
                                	**length:** 0..255
                                
                                .. attribute:: part_revision
                                
                                	Part Revision
                                	**type**\:  str
                                
                                	**length:** 0..255
                                
                                .. attribute:: pca_num
                                
                                	PCA number
                                	**type**\:  str
                                
                                	**length:** 0..255
                                
                                .. attribute:: pcavid
                                
                                	PCA revision ID
                                	**type**\:  str
                                
                                	**length:** 0..255
                                
                                .. attribute:: pcb_serial_num
                                
                                	PCB Serial Number
                                	**type**\:  str
                                
                                	**length:** 0..255
                                
                                .. attribute:: pid
                                
                                	Product ID
                                	**type**\:  str
                                
                                	**length:** 0..255
                                
                                .. attribute:: power_consumption
                                
                                	Power Consumption
                                	**type**\:  str
                                
                                	**length:** 0..255
                                
                                .. attribute:: power_supply_type
                                
                                	Power Supply Type
                                	**type**\:  str
                                
                                	**length:** 0..255
                                
                                .. attribute:: product_id
                                
                                	Product ID
                                	**type**\:  str
                                
                                	**length:** 0..255
                                
                                .. attribute:: rma
                                
                                	RMA Data
                                	**type**\:   :py:class:`Rma <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sdr_invmgr_diag_oper.Diag.Racks.Rack.PowerShelfs.PowerShelf.PowerSupplies.PowerSupply.Information.Rma>`
                                
                                .. attribute:: rma_code
                                
                                	RMA Code
                                	**type**\:  str
                                
                                	**length:** 0..255
                                
                                .. attribute:: serial_number
                                
                                	Serial Number
                                	**type**\:  str
                                
                                	**length:** 0..255
                                
                                .. attribute:: snmpoid
                                
                                	SNMP OID
                                	**type**\:  str
                                
                                	**length:** 0..255
                                
                                .. attribute:: top_assem_part_num
                                
                                	Top assembly part number
                                	**type**\:  str
                                
                                	**length:** 0..255
                                
                                .. attribute:: top_assem_vid
                                
                                	Top assembly revision number
                                	**type**\:  str
                                
                                	**length:** 0..255
                                
                                .. attribute:: udi_description
                                
                                	UDI description
                                	**type**\:  str
                                
                                	**length:** 0..255
                                
                                .. attribute:: udi_name
                                
                                	UDI name
                                	**type**\:  str
                                
                                	**length:** 0..255
                                
                                .. attribute:: vid
                                
                                	Version ID
                                	**type**\:  str
                                
                                	**length:** 0..255
                                
                                

                                """

                                _prefix = 'sdr-invmgr-diag-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Diag.Racks.Rack.PowerShelfs.PowerShelf.PowerSupplies.PowerSupply.Information, self).__init__()

                                    self.yang_name = "information"
                                    self.yang_parent_name = "power-supply"

                                    self.asset_alias = YLeaf(YType.str, "asset-alias")

                                    self.asset_id = YLeaf(YType.str, "asset-id")

                                    self.base_mac_address1 = YLeaf(YType.str, "base-mac-address1")

                                    self.base_mac_address2 = YLeaf(YType.str, "base-mac-address2")

                                    self.base_mac_address3 = YLeaf(YType.str, "base-mac-address3")

                                    self.base_mac_address4 = YLeaf(YType.str, "base-mac-address4")

                                    self.block_checksum = YLeaf(YType.str, "block-checksum")

                                    self.block_count = YLeaf(YType.str, "block-count")

                                    self.block_length = YLeaf(YType.str, "block-length")

                                    self.block_signature = YLeaf(YType.str, "block-signature")

                                    self.block_version = YLeaf(YType.str, "block-version")

                                    self.chassis_sid = YLeaf(YType.str, "chassis-sid")

                                    self.clei = YLeaf(YType.str, "clei")

                                    self.controller_family = YLeaf(YType.str, "controller-family")

                                    self.controller_type = YLeaf(YType.str, "controller-type")

                                    self.description = YLeaf(YType.str, "description")

                                    self.dev_num1 = YLeaf(YType.str, "dev-num1")

                                    self.dev_num2 = YLeaf(YType.str, "dev-num2")

                                    self.dev_num3 = YLeaf(YType.str, "dev-num3")

                                    self.dev_num4 = YLeaf(YType.str, "dev-num4")

                                    self.dev_num5 = YLeaf(YType.str, "dev-num5")

                                    self.dev_num6 = YLeaf(YType.str, "dev-num6")

                                    self.dev_num7 = YLeaf(YType.str, "dev-num7")

                                    self.eci = YLeaf(YType.str, "eci")

                                    self.eeprom_size = YLeaf(YType.str, "eeprom-size")

                                    self.engineer_use = YLeaf(YType.str, "engineer-use")

                                    self.fru_major_type = YLeaf(YType.str, "fru-major-type")

                                    self.fru_minor_type = YLeaf(YType.str, "fru-minor-type")

                                    self.hw_version = YLeaf(YType.str, "hw-version")

                                    self.hwid = YLeaf(YType.str, "hwid")

                                    self.idprom_format_rev = YLeaf(YType.str, "idprom-format-rev")

                                    self.mac_add_blk_size1 = YLeaf(YType.str, "mac-add-blk-size1")

                                    self.mac_add_blk_size2 = YLeaf(YType.str, "mac-add-blk-size2")

                                    self.mac_add_blk_size3 = YLeaf(YType.str, "mac-add-blk-size3")

                                    self.mac_add_blk_size4 = YLeaf(YType.str, "mac-add-blk-size4")

                                    self.manu_test_data = YLeaf(YType.str, "manu-test-data")

                                    self.mfg_bits = YLeaf(YType.str, "mfg-bits")

                                    self.mfg_deviation = YLeaf(YType.str, "mfg-deviation")

                                    self.oem_string = YLeaf(YType.str, "oem-string")

                                    self.part_number = YLeaf(YType.str, "part-number")

                                    self.part_revision = YLeaf(YType.str, "part-revision")

                                    self.pca_num = YLeaf(YType.str, "pca-num")

                                    self.pcavid = YLeaf(YType.str, "pcavid")

                                    self.pcb_serial_num = YLeaf(YType.str, "pcb-serial-num")

                                    self.pid = YLeaf(YType.str, "pid")

                                    self.power_consumption = YLeaf(YType.str, "power-consumption")

                                    self.power_supply_type = YLeaf(YType.str, "power-supply-type")

                                    self.product_id = YLeaf(YType.str, "product-id")

                                    self.rma_code = YLeaf(YType.str, "rma-code")

                                    self.serial_number = YLeaf(YType.str, "serial-number")

                                    self.snmpoid = YLeaf(YType.str, "snmpoid")

                                    self.top_assem_part_num = YLeaf(YType.str, "top-assem-part-num")

                                    self.top_assem_vid = YLeaf(YType.str, "top-assem-vid")

                                    self.udi_description = YLeaf(YType.str, "udi-description")

                                    self.udi_name = YLeaf(YType.str, "udi-name")

                                    self.vid = YLeaf(YType.str, "vid")

                                    self.rma = Diag.Racks.Rack.PowerShelfs.PowerShelf.PowerSupplies.PowerSupply.Information.Rma()
                                    self.rma.parent = self
                                    self._children_name_map["rma"] = "rma"
                                    self._children_yang_names.add("rma")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("asset_alias",
                                                    "asset_id",
                                                    "base_mac_address1",
                                                    "base_mac_address2",
                                                    "base_mac_address3",
                                                    "base_mac_address4",
                                                    "block_checksum",
                                                    "block_count",
                                                    "block_length",
                                                    "block_signature",
                                                    "block_version",
                                                    "chassis_sid",
                                                    "clei",
                                                    "controller_family",
                                                    "controller_type",
                                                    "description",
                                                    "dev_num1",
                                                    "dev_num2",
                                                    "dev_num3",
                                                    "dev_num4",
                                                    "dev_num5",
                                                    "dev_num6",
                                                    "dev_num7",
                                                    "eci",
                                                    "eeprom_size",
                                                    "engineer_use",
                                                    "fru_major_type",
                                                    "fru_minor_type",
                                                    "hw_version",
                                                    "hwid",
                                                    "idprom_format_rev",
                                                    "mac_add_blk_size1",
                                                    "mac_add_blk_size2",
                                                    "mac_add_blk_size3",
                                                    "mac_add_blk_size4",
                                                    "manu_test_data",
                                                    "mfg_bits",
                                                    "mfg_deviation",
                                                    "oem_string",
                                                    "part_number",
                                                    "part_revision",
                                                    "pca_num",
                                                    "pcavid",
                                                    "pcb_serial_num",
                                                    "pid",
                                                    "power_consumption",
                                                    "power_supply_type",
                                                    "product_id",
                                                    "rma_code",
                                                    "serial_number",
                                                    "snmpoid",
                                                    "top_assem_part_num",
                                                    "top_assem_vid",
                                                    "udi_description",
                                                    "udi_name",
                                                    "vid") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(Diag.Racks.Rack.PowerShelfs.PowerShelf.PowerSupplies.PowerSupply.Information, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Diag.Racks.Rack.PowerShelfs.PowerShelf.PowerSupplies.PowerSupply.Information, self).__setattr__(name, value)


                                class Rma(Entity):
                                    """
                                    RMA Data
                                    
                                    .. attribute:: rma_history
                                    
                                    	RMA history
                                    	**type**\:  str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: rma_number
                                    
                                    	RMA tracking number format is N\-N\-N
                                    	**type**\:  str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: test_history
                                    
                                    	Test history
                                    	**type**\:  str
                                    
                                    	**length:** 0..255
                                    
                                    

                                    """

                                    _prefix = 'sdr-invmgr-diag-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Diag.Racks.Rack.PowerShelfs.PowerShelf.PowerSupplies.PowerSupply.Information.Rma, self).__init__()

                                        self.yang_name = "rma"
                                        self.yang_parent_name = "information"

                                        self.rma_history = YLeaf(YType.str, "rma-history")

                                        self.rma_number = YLeaf(YType.str, "rma-number")

                                        self.test_history = YLeaf(YType.str, "test-history")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("rma_history",
                                                        "rma_number",
                                                        "test_history") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(Diag.Racks.Rack.PowerShelfs.PowerShelf.PowerSupplies.PowerSupply.Information.Rma, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(Diag.Racks.Rack.PowerShelfs.PowerShelf.PowerSupplies.PowerSupply.Information.Rma, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.rma_history.is_set or
                                            self.rma_number.is_set or
                                            self.test_history.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.rma_history.yfilter != YFilter.not_set or
                                            self.rma_number.yfilter != YFilter.not_set or
                                            self.test_history.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "rma" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.rma_history.is_set or self.rma_history.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.rma_history.get_name_leafdata())
                                        if (self.rma_number.is_set or self.rma_number.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.rma_number.get_name_leafdata())
                                        if (self.test_history.is_set or self.test_history.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.test_history.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "rma-history" or name == "rma-number" or name == "test-history"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "rma-history"):
                                            self.rma_history = value
                                            self.rma_history.value_namespace = name_space
                                            self.rma_history.value_namespace_prefix = name_space_prefix
                                        if(value_path == "rma-number"):
                                            self.rma_number = value
                                            self.rma_number.value_namespace = name_space
                                            self.rma_number.value_namespace_prefix = name_space_prefix
                                        if(value_path == "test-history"):
                                            self.test_history = value
                                            self.test_history.value_namespace = name_space
                                            self.test_history.value_namespace_prefix = name_space_prefix

                                def has_data(self):
                                    return (
                                        self.asset_alias.is_set or
                                        self.asset_id.is_set or
                                        self.base_mac_address1.is_set or
                                        self.base_mac_address2.is_set or
                                        self.base_mac_address3.is_set or
                                        self.base_mac_address4.is_set or
                                        self.block_checksum.is_set or
                                        self.block_count.is_set or
                                        self.block_length.is_set or
                                        self.block_signature.is_set or
                                        self.block_version.is_set or
                                        self.chassis_sid.is_set or
                                        self.clei.is_set or
                                        self.controller_family.is_set or
                                        self.controller_type.is_set or
                                        self.description.is_set or
                                        self.dev_num1.is_set or
                                        self.dev_num2.is_set or
                                        self.dev_num3.is_set or
                                        self.dev_num4.is_set or
                                        self.dev_num5.is_set or
                                        self.dev_num6.is_set or
                                        self.dev_num7.is_set or
                                        self.eci.is_set or
                                        self.eeprom_size.is_set or
                                        self.engineer_use.is_set or
                                        self.fru_major_type.is_set or
                                        self.fru_minor_type.is_set or
                                        self.hw_version.is_set or
                                        self.hwid.is_set or
                                        self.idprom_format_rev.is_set or
                                        self.mac_add_blk_size1.is_set or
                                        self.mac_add_blk_size2.is_set or
                                        self.mac_add_blk_size3.is_set or
                                        self.mac_add_blk_size4.is_set or
                                        self.manu_test_data.is_set or
                                        self.mfg_bits.is_set or
                                        self.mfg_deviation.is_set or
                                        self.oem_string.is_set or
                                        self.part_number.is_set or
                                        self.part_revision.is_set or
                                        self.pca_num.is_set or
                                        self.pcavid.is_set or
                                        self.pcb_serial_num.is_set or
                                        self.pid.is_set or
                                        self.power_consumption.is_set or
                                        self.power_supply_type.is_set or
                                        self.product_id.is_set or
                                        self.rma_code.is_set or
                                        self.serial_number.is_set or
                                        self.snmpoid.is_set or
                                        self.top_assem_part_num.is_set or
                                        self.top_assem_vid.is_set or
                                        self.udi_description.is_set or
                                        self.udi_name.is_set or
                                        self.vid.is_set or
                                        (self.rma is not None and self.rma.has_data()))

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.asset_alias.yfilter != YFilter.not_set or
                                        self.asset_id.yfilter != YFilter.not_set or
                                        self.base_mac_address1.yfilter != YFilter.not_set or
                                        self.base_mac_address2.yfilter != YFilter.not_set or
                                        self.base_mac_address3.yfilter != YFilter.not_set or
                                        self.base_mac_address4.yfilter != YFilter.not_set or
                                        self.block_checksum.yfilter != YFilter.not_set or
                                        self.block_count.yfilter != YFilter.not_set or
                                        self.block_length.yfilter != YFilter.not_set or
                                        self.block_signature.yfilter != YFilter.not_set or
                                        self.block_version.yfilter != YFilter.not_set or
                                        self.chassis_sid.yfilter != YFilter.not_set or
                                        self.clei.yfilter != YFilter.not_set or
                                        self.controller_family.yfilter != YFilter.not_set or
                                        self.controller_type.yfilter != YFilter.not_set or
                                        self.description.yfilter != YFilter.not_set or
                                        self.dev_num1.yfilter != YFilter.not_set or
                                        self.dev_num2.yfilter != YFilter.not_set or
                                        self.dev_num3.yfilter != YFilter.not_set or
                                        self.dev_num4.yfilter != YFilter.not_set or
                                        self.dev_num5.yfilter != YFilter.not_set or
                                        self.dev_num6.yfilter != YFilter.not_set or
                                        self.dev_num7.yfilter != YFilter.not_set or
                                        self.eci.yfilter != YFilter.not_set or
                                        self.eeprom_size.yfilter != YFilter.not_set or
                                        self.engineer_use.yfilter != YFilter.not_set or
                                        self.fru_major_type.yfilter != YFilter.not_set or
                                        self.fru_minor_type.yfilter != YFilter.not_set or
                                        self.hw_version.yfilter != YFilter.not_set or
                                        self.hwid.yfilter != YFilter.not_set or
                                        self.idprom_format_rev.yfilter != YFilter.not_set or
                                        self.mac_add_blk_size1.yfilter != YFilter.not_set or
                                        self.mac_add_blk_size2.yfilter != YFilter.not_set or
                                        self.mac_add_blk_size3.yfilter != YFilter.not_set or
                                        self.mac_add_blk_size4.yfilter != YFilter.not_set or
                                        self.manu_test_data.yfilter != YFilter.not_set or
                                        self.mfg_bits.yfilter != YFilter.not_set or
                                        self.mfg_deviation.yfilter != YFilter.not_set or
                                        self.oem_string.yfilter != YFilter.not_set or
                                        self.part_number.yfilter != YFilter.not_set or
                                        self.part_revision.yfilter != YFilter.not_set or
                                        self.pca_num.yfilter != YFilter.not_set or
                                        self.pcavid.yfilter != YFilter.not_set or
                                        self.pcb_serial_num.yfilter != YFilter.not_set or
                                        self.pid.yfilter != YFilter.not_set or
                                        self.power_consumption.yfilter != YFilter.not_set or
                                        self.power_supply_type.yfilter != YFilter.not_set or
                                        self.product_id.yfilter != YFilter.not_set or
                                        self.rma_code.yfilter != YFilter.not_set or
                                        self.serial_number.yfilter != YFilter.not_set or
                                        self.snmpoid.yfilter != YFilter.not_set or
                                        self.top_assem_part_num.yfilter != YFilter.not_set or
                                        self.top_assem_vid.yfilter != YFilter.not_set or
                                        self.udi_description.yfilter != YFilter.not_set or
                                        self.udi_name.yfilter != YFilter.not_set or
                                        self.vid.yfilter != YFilter.not_set or
                                        (self.rma is not None and self.rma.has_operation()))

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "information" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.asset_alias.is_set or self.asset_alias.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.asset_alias.get_name_leafdata())
                                    if (self.asset_id.is_set or self.asset_id.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.asset_id.get_name_leafdata())
                                    if (self.base_mac_address1.is_set or self.base_mac_address1.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.base_mac_address1.get_name_leafdata())
                                    if (self.base_mac_address2.is_set or self.base_mac_address2.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.base_mac_address2.get_name_leafdata())
                                    if (self.base_mac_address3.is_set or self.base_mac_address3.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.base_mac_address3.get_name_leafdata())
                                    if (self.base_mac_address4.is_set or self.base_mac_address4.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.base_mac_address4.get_name_leafdata())
                                    if (self.block_checksum.is_set or self.block_checksum.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.block_checksum.get_name_leafdata())
                                    if (self.block_count.is_set or self.block_count.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.block_count.get_name_leafdata())
                                    if (self.block_length.is_set or self.block_length.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.block_length.get_name_leafdata())
                                    if (self.block_signature.is_set or self.block_signature.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.block_signature.get_name_leafdata())
                                    if (self.block_version.is_set or self.block_version.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.block_version.get_name_leafdata())
                                    if (self.chassis_sid.is_set or self.chassis_sid.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.chassis_sid.get_name_leafdata())
                                    if (self.clei.is_set or self.clei.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.clei.get_name_leafdata())
                                    if (self.controller_family.is_set or self.controller_family.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.controller_family.get_name_leafdata())
                                    if (self.controller_type.is_set or self.controller_type.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.controller_type.get_name_leafdata())
                                    if (self.description.is_set or self.description.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.description.get_name_leafdata())
                                    if (self.dev_num1.is_set or self.dev_num1.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.dev_num1.get_name_leafdata())
                                    if (self.dev_num2.is_set or self.dev_num2.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.dev_num2.get_name_leafdata())
                                    if (self.dev_num3.is_set or self.dev_num3.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.dev_num3.get_name_leafdata())
                                    if (self.dev_num4.is_set or self.dev_num4.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.dev_num4.get_name_leafdata())
                                    if (self.dev_num5.is_set or self.dev_num5.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.dev_num5.get_name_leafdata())
                                    if (self.dev_num6.is_set or self.dev_num6.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.dev_num6.get_name_leafdata())
                                    if (self.dev_num7.is_set or self.dev_num7.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.dev_num7.get_name_leafdata())
                                    if (self.eci.is_set or self.eci.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.eci.get_name_leafdata())
                                    if (self.eeprom_size.is_set or self.eeprom_size.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.eeprom_size.get_name_leafdata())
                                    if (self.engineer_use.is_set or self.engineer_use.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.engineer_use.get_name_leafdata())
                                    if (self.fru_major_type.is_set or self.fru_major_type.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.fru_major_type.get_name_leafdata())
                                    if (self.fru_minor_type.is_set or self.fru_minor_type.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.fru_minor_type.get_name_leafdata())
                                    if (self.hw_version.is_set or self.hw_version.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.hw_version.get_name_leafdata())
                                    if (self.hwid.is_set or self.hwid.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.hwid.get_name_leafdata())
                                    if (self.idprom_format_rev.is_set or self.idprom_format_rev.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.idprom_format_rev.get_name_leafdata())
                                    if (self.mac_add_blk_size1.is_set or self.mac_add_blk_size1.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.mac_add_blk_size1.get_name_leafdata())
                                    if (self.mac_add_blk_size2.is_set or self.mac_add_blk_size2.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.mac_add_blk_size2.get_name_leafdata())
                                    if (self.mac_add_blk_size3.is_set or self.mac_add_blk_size3.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.mac_add_blk_size3.get_name_leafdata())
                                    if (self.mac_add_blk_size4.is_set or self.mac_add_blk_size4.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.mac_add_blk_size4.get_name_leafdata())
                                    if (self.manu_test_data.is_set or self.manu_test_data.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.manu_test_data.get_name_leafdata())
                                    if (self.mfg_bits.is_set or self.mfg_bits.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.mfg_bits.get_name_leafdata())
                                    if (self.mfg_deviation.is_set or self.mfg_deviation.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.mfg_deviation.get_name_leafdata())
                                    if (self.oem_string.is_set or self.oem_string.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.oem_string.get_name_leafdata())
                                    if (self.part_number.is_set or self.part_number.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.part_number.get_name_leafdata())
                                    if (self.part_revision.is_set or self.part_revision.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.part_revision.get_name_leafdata())
                                    if (self.pca_num.is_set or self.pca_num.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.pca_num.get_name_leafdata())
                                    if (self.pcavid.is_set or self.pcavid.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.pcavid.get_name_leafdata())
                                    if (self.pcb_serial_num.is_set or self.pcb_serial_num.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.pcb_serial_num.get_name_leafdata())
                                    if (self.pid.is_set or self.pid.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.pid.get_name_leafdata())
                                    if (self.power_consumption.is_set or self.power_consumption.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.power_consumption.get_name_leafdata())
                                    if (self.power_supply_type.is_set or self.power_supply_type.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.power_supply_type.get_name_leafdata())
                                    if (self.product_id.is_set or self.product_id.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.product_id.get_name_leafdata())
                                    if (self.rma_code.is_set or self.rma_code.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.rma_code.get_name_leafdata())
                                    if (self.serial_number.is_set or self.serial_number.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.serial_number.get_name_leafdata())
                                    if (self.snmpoid.is_set or self.snmpoid.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.snmpoid.get_name_leafdata())
                                    if (self.top_assem_part_num.is_set or self.top_assem_part_num.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.top_assem_part_num.get_name_leafdata())
                                    if (self.top_assem_vid.is_set or self.top_assem_vid.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.top_assem_vid.get_name_leafdata())
                                    if (self.udi_description.is_set or self.udi_description.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.udi_description.get_name_leafdata())
                                    if (self.udi_name.is_set or self.udi_name.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.udi_name.get_name_leafdata())
                                    if (self.vid.is_set or self.vid.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.vid.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    if (child_yang_name == "rma"):
                                        if (self.rma is None):
                                            self.rma = Diag.Racks.Rack.PowerShelfs.PowerShelf.PowerSupplies.PowerSupply.Information.Rma()
                                            self.rma.parent = self
                                            self._children_name_map["rma"] = "rma"
                                        return self.rma

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "rma" or name == "asset-alias" or name == "asset-id" or name == "base-mac-address1" or name == "base-mac-address2" or name == "base-mac-address3" or name == "base-mac-address4" or name == "block-checksum" or name == "block-count" or name == "block-length" or name == "block-signature" or name == "block-version" or name == "chassis-sid" or name == "clei" or name == "controller-family" or name == "controller-type" or name == "description" or name == "dev-num1" or name == "dev-num2" or name == "dev-num3" or name == "dev-num4" or name == "dev-num5" or name == "dev-num6" or name == "dev-num7" or name == "eci" or name == "eeprom-size" or name == "engineer-use" or name == "fru-major-type" or name == "fru-minor-type" or name == "hw-version" or name == "hwid" or name == "idprom-format-rev" or name == "mac-add-blk-size1" or name == "mac-add-blk-size2" or name == "mac-add-blk-size3" or name == "mac-add-blk-size4" or name == "manu-test-data" or name == "mfg-bits" or name == "mfg-deviation" or name == "oem-string" or name == "part-number" or name == "part-revision" or name == "pca-num" or name == "pcavid" or name == "pcb-serial-num" or name == "pid" or name == "power-consumption" or name == "power-supply-type" or name == "product-id" or name == "rma-code" or name == "serial-number" or name == "snmpoid" or name == "top-assem-part-num" or name == "top-assem-vid" or name == "udi-description" or name == "udi-name" or name == "vid"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "asset-alias"):
                                        self.asset_alias = value
                                        self.asset_alias.value_namespace = name_space
                                        self.asset_alias.value_namespace_prefix = name_space_prefix
                                    if(value_path == "asset-id"):
                                        self.asset_id = value
                                        self.asset_id.value_namespace = name_space
                                        self.asset_id.value_namespace_prefix = name_space_prefix
                                    if(value_path == "base-mac-address1"):
                                        self.base_mac_address1 = value
                                        self.base_mac_address1.value_namespace = name_space
                                        self.base_mac_address1.value_namespace_prefix = name_space_prefix
                                    if(value_path == "base-mac-address2"):
                                        self.base_mac_address2 = value
                                        self.base_mac_address2.value_namespace = name_space
                                        self.base_mac_address2.value_namespace_prefix = name_space_prefix
                                    if(value_path == "base-mac-address3"):
                                        self.base_mac_address3 = value
                                        self.base_mac_address3.value_namespace = name_space
                                        self.base_mac_address3.value_namespace_prefix = name_space_prefix
                                    if(value_path == "base-mac-address4"):
                                        self.base_mac_address4 = value
                                        self.base_mac_address4.value_namespace = name_space
                                        self.base_mac_address4.value_namespace_prefix = name_space_prefix
                                    if(value_path == "block-checksum"):
                                        self.block_checksum = value
                                        self.block_checksum.value_namespace = name_space
                                        self.block_checksum.value_namespace_prefix = name_space_prefix
                                    if(value_path == "block-count"):
                                        self.block_count = value
                                        self.block_count.value_namespace = name_space
                                        self.block_count.value_namespace_prefix = name_space_prefix
                                    if(value_path == "block-length"):
                                        self.block_length = value
                                        self.block_length.value_namespace = name_space
                                        self.block_length.value_namespace_prefix = name_space_prefix
                                    if(value_path == "block-signature"):
                                        self.block_signature = value
                                        self.block_signature.value_namespace = name_space
                                        self.block_signature.value_namespace_prefix = name_space_prefix
                                    if(value_path == "block-version"):
                                        self.block_version = value
                                        self.block_version.value_namespace = name_space
                                        self.block_version.value_namespace_prefix = name_space_prefix
                                    if(value_path == "chassis-sid"):
                                        self.chassis_sid = value
                                        self.chassis_sid.value_namespace = name_space
                                        self.chassis_sid.value_namespace_prefix = name_space_prefix
                                    if(value_path == "clei"):
                                        self.clei = value
                                        self.clei.value_namespace = name_space
                                        self.clei.value_namespace_prefix = name_space_prefix
                                    if(value_path == "controller-family"):
                                        self.controller_family = value
                                        self.controller_family.value_namespace = name_space
                                        self.controller_family.value_namespace_prefix = name_space_prefix
                                    if(value_path == "controller-type"):
                                        self.controller_type = value
                                        self.controller_type.value_namespace = name_space
                                        self.controller_type.value_namespace_prefix = name_space_prefix
                                    if(value_path == "description"):
                                        self.description = value
                                        self.description.value_namespace = name_space
                                        self.description.value_namespace_prefix = name_space_prefix
                                    if(value_path == "dev-num1"):
                                        self.dev_num1 = value
                                        self.dev_num1.value_namespace = name_space
                                        self.dev_num1.value_namespace_prefix = name_space_prefix
                                    if(value_path == "dev-num2"):
                                        self.dev_num2 = value
                                        self.dev_num2.value_namespace = name_space
                                        self.dev_num2.value_namespace_prefix = name_space_prefix
                                    if(value_path == "dev-num3"):
                                        self.dev_num3 = value
                                        self.dev_num3.value_namespace = name_space
                                        self.dev_num3.value_namespace_prefix = name_space_prefix
                                    if(value_path == "dev-num4"):
                                        self.dev_num4 = value
                                        self.dev_num4.value_namespace = name_space
                                        self.dev_num4.value_namespace_prefix = name_space_prefix
                                    if(value_path == "dev-num5"):
                                        self.dev_num5 = value
                                        self.dev_num5.value_namespace = name_space
                                        self.dev_num5.value_namespace_prefix = name_space_prefix
                                    if(value_path == "dev-num6"):
                                        self.dev_num6 = value
                                        self.dev_num6.value_namespace = name_space
                                        self.dev_num6.value_namespace_prefix = name_space_prefix
                                    if(value_path == "dev-num7"):
                                        self.dev_num7 = value
                                        self.dev_num7.value_namespace = name_space
                                        self.dev_num7.value_namespace_prefix = name_space_prefix
                                    if(value_path == "eci"):
                                        self.eci = value
                                        self.eci.value_namespace = name_space
                                        self.eci.value_namespace_prefix = name_space_prefix
                                    if(value_path == "eeprom-size"):
                                        self.eeprom_size = value
                                        self.eeprom_size.value_namespace = name_space
                                        self.eeprom_size.value_namespace_prefix = name_space_prefix
                                    if(value_path == "engineer-use"):
                                        self.engineer_use = value
                                        self.engineer_use.value_namespace = name_space
                                        self.engineer_use.value_namespace_prefix = name_space_prefix
                                    if(value_path == "fru-major-type"):
                                        self.fru_major_type = value
                                        self.fru_major_type.value_namespace = name_space
                                        self.fru_major_type.value_namespace_prefix = name_space_prefix
                                    if(value_path == "fru-minor-type"):
                                        self.fru_minor_type = value
                                        self.fru_minor_type.value_namespace = name_space
                                        self.fru_minor_type.value_namespace_prefix = name_space_prefix
                                    if(value_path == "hw-version"):
                                        self.hw_version = value
                                        self.hw_version.value_namespace = name_space
                                        self.hw_version.value_namespace_prefix = name_space_prefix
                                    if(value_path == "hwid"):
                                        self.hwid = value
                                        self.hwid.value_namespace = name_space
                                        self.hwid.value_namespace_prefix = name_space_prefix
                                    if(value_path == "idprom-format-rev"):
                                        self.idprom_format_rev = value
                                        self.idprom_format_rev.value_namespace = name_space
                                        self.idprom_format_rev.value_namespace_prefix = name_space_prefix
                                    if(value_path == "mac-add-blk-size1"):
                                        self.mac_add_blk_size1 = value
                                        self.mac_add_blk_size1.value_namespace = name_space
                                        self.mac_add_blk_size1.value_namespace_prefix = name_space_prefix
                                    if(value_path == "mac-add-blk-size2"):
                                        self.mac_add_blk_size2 = value
                                        self.mac_add_blk_size2.value_namespace = name_space
                                        self.mac_add_blk_size2.value_namespace_prefix = name_space_prefix
                                    if(value_path == "mac-add-blk-size3"):
                                        self.mac_add_blk_size3 = value
                                        self.mac_add_blk_size3.value_namespace = name_space
                                        self.mac_add_blk_size3.value_namespace_prefix = name_space_prefix
                                    if(value_path == "mac-add-blk-size4"):
                                        self.mac_add_blk_size4 = value
                                        self.mac_add_blk_size4.value_namespace = name_space
                                        self.mac_add_blk_size4.value_namespace_prefix = name_space_prefix
                                    if(value_path == "manu-test-data"):
                                        self.manu_test_data = value
                                        self.manu_test_data.value_namespace = name_space
                                        self.manu_test_data.value_namespace_prefix = name_space_prefix
                                    if(value_path == "mfg-bits"):
                                        self.mfg_bits = value
                                        self.mfg_bits.value_namespace = name_space
                                        self.mfg_bits.value_namespace_prefix = name_space_prefix
                                    if(value_path == "mfg-deviation"):
                                        self.mfg_deviation = value
                                        self.mfg_deviation.value_namespace = name_space
                                        self.mfg_deviation.value_namespace_prefix = name_space_prefix
                                    if(value_path == "oem-string"):
                                        self.oem_string = value
                                        self.oem_string.value_namespace = name_space
                                        self.oem_string.value_namespace_prefix = name_space_prefix
                                    if(value_path == "part-number"):
                                        self.part_number = value
                                        self.part_number.value_namespace = name_space
                                        self.part_number.value_namespace_prefix = name_space_prefix
                                    if(value_path == "part-revision"):
                                        self.part_revision = value
                                        self.part_revision.value_namespace = name_space
                                        self.part_revision.value_namespace_prefix = name_space_prefix
                                    if(value_path == "pca-num"):
                                        self.pca_num = value
                                        self.pca_num.value_namespace = name_space
                                        self.pca_num.value_namespace_prefix = name_space_prefix
                                    if(value_path == "pcavid"):
                                        self.pcavid = value
                                        self.pcavid.value_namespace = name_space
                                        self.pcavid.value_namespace_prefix = name_space_prefix
                                    if(value_path == "pcb-serial-num"):
                                        self.pcb_serial_num = value
                                        self.pcb_serial_num.value_namespace = name_space
                                        self.pcb_serial_num.value_namespace_prefix = name_space_prefix
                                    if(value_path == "pid"):
                                        self.pid = value
                                        self.pid.value_namespace = name_space
                                        self.pid.value_namespace_prefix = name_space_prefix
                                    if(value_path == "power-consumption"):
                                        self.power_consumption = value
                                        self.power_consumption.value_namespace = name_space
                                        self.power_consumption.value_namespace_prefix = name_space_prefix
                                    if(value_path == "power-supply-type"):
                                        self.power_supply_type = value
                                        self.power_supply_type.value_namespace = name_space
                                        self.power_supply_type.value_namespace_prefix = name_space_prefix
                                    if(value_path == "product-id"):
                                        self.product_id = value
                                        self.product_id.value_namespace = name_space
                                        self.product_id.value_namespace_prefix = name_space_prefix
                                    if(value_path == "rma-code"):
                                        self.rma_code = value
                                        self.rma_code.value_namespace = name_space
                                        self.rma_code.value_namespace_prefix = name_space_prefix
                                    if(value_path == "serial-number"):
                                        self.serial_number = value
                                        self.serial_number.value_namespace = name_space
                                        self.serial_number.value_namespace_prefix = name_space_prefix
                                    if(value_path == "snmpoid"):
                                        self.snmpoid = value
                                        self.snmpoid.value_namespace = name_space
                                        self.snmpoid.value_namespace_prefix = name_space_prefix
                                    if(value_path == "top-assem-part-num"):
                                        self.top_assem_part_num = value
                                        self.top_assem_part_num.value_namespace = name_space
                                        self.top_assem_part_num.value_namespace_prefix = name_space_prefix
                                    if(value_path == "top-assem-vid"):
                                        self.top_assem_vid = value
                                        self.top_assem_vid.value_namespace = name_space
                                        self.top_assem_vid.value_namespace_prefix = name_space_prefix
                                    if(value_path == "udi-description"):
                                        self.udi_description = value
                                        self.udi_description.value_namespace = name_space
                                        self.udi_description.value_namespace_prefix = name_space_prefix
                                    if(value_path == "udi-name"):
                                        self.udi_name = value
                                        self.udi_name.value_namespace = name_space
                                        self.udi_name.value_namespace_prefix = name_space_prefix
                                    if(value_path == "vid"):
                                        self.vid = value
                                        self.vid.value_namespace = name_space
                                        self.vid.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                return (
                                    self.power_supply_name.is_set or
                                    (self.information is not None and self.information.has_data()))

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.power_supply_name.yfilter != YFilter.not_set or
                                    (self.information is not None and self.information.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "power-supply" + "[power-supply-name='" + self.power_supply_name.get() + "']" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.power_supply_name.is_set or self.power_supply_name.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.power_supply_name.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                if (child_yang_name == "information"):
                                    if (self.information is None):
                                        self.information = Diag.Racks.Rack.PowerShelfs.PowerShelf.PowerSupplies.PowerSupply.Information()
                                        self.information.parent = self
                                        self._children_name_map["information"] = "information"
                                    return self.information

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "information" or name == "power-supply-name"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "power-supply-name"):
                                    self.power_supply_name = value
                                    self.power_supply_name.value_namespace = name_space
                                    self.power_supply_name.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.power_supply:
                                if (c.has_data()):
                                    return True
                            return False

                        def has_operation(self):
                            for c in self.power_supply:
                                if (c.has_operation()):
                                    return True
                            return self.yfilter != YFilter.not_set

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "power-supplies" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "power-supply"):
                                for c in self.power_supply:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = Diag.Racks.Rack.PowerShelfs.PowerShelf.PowerSupplies.PowerSupply()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.power_supply.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "power-supply"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass

                    def has_data(self):
                        return (
                            self.power_shelf_name.is_set or
                            (self.power_supplies is not None and self.power_supplies.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.power_shelf_name.yfilter != YFilter.not_set or
                            (self.power_supplies is not None and self.power_supplies.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "power-shelf" + "[power-shelf-name='" + self.power_shelf_name.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.power_shelf_name.is_set or self.power_shelf_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.power_shelf_name.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "power-supplies"):
                            if (self.power_supplies is None):
                                self.power_supplies = Diag.Racks.Rack.PowerShelfs.PowerShelf.PowerSupplies()
                                self.power_supplies.parent = self
                                self._children_name_map["power_supplies"] = "power-supplies"
                            return self.power_supplies

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "power-supplies" or name == "power-shelf-name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "power-shelf-name"):
                            self.power_shelf_name = value
                            self.power_shelf_name.value_namespace = name_space
                            self.power_shelf_name.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.power_shelf:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.power_shelf:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "power-shelfs" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "power-shelf"):
                        for c in self.power_shelf:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Diag.Racks.Rack.PowerShelfs.PowerShelf()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.power_shelf.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "power-shelf"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class FanTraies(Entity):
                """
                Table for rack fan trays
                
                .. attribute:: fan_tray
                
                	Fan tray name
                	**type**\: list of    :py:class:`FanTray <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sdr_invmgr_diag_oper.Diag.Racks.Rack.FanTraies.FanTray>`
                
                

                """

                _prefix = 'sdr-invmgr-diag-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Diag.Racks.Rack.FanTraies, self).__init__()

                    self.yang_name = "fan-traies"
                    self.yang_parent_name = "rack"

                    self.fan_tray = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in () and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Diag.Racks.Rack.FanTraies, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Diag.Racks.Rack.FanTraies, self).__setattr__(name, value)


                class FanTray(Entity):
                    """
                    Fan tray name
                    
                    .. attribute:: fan_tray_name  <key>
                    
                    	Fan tray name
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: fanses
                    
                    	Table for rack fans 
                    	**type**\:   :py:class:`Fanses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sdr_invmgr_diag_oper.Diag.Racks.Rack.FanTraies.FanTray.Fanses>`
                    
                    

                    """

                    _prefix = 'sdr-invmgr-diag-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Diag.Racks.Rack.FanTraies.FanTray, self).__init__()

                        self.yang_name = "fan-tray"
                        self.yang_parent_name = "fan-traies"

                        self.fan_tray_name = YLeaf(YType.str, "fan-tray-name")

                        self.fanses = Diag.Racks.Rack.FanTraies.FanTray.Fanses()
                        self.fanses.parent = self
                        self._children_name_map["fanses"] = "fanses"
                        self._children_yang_names.add("fanses")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("fan_tray_name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Diag.Racks.Rack.FanTraies.FanTray, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Diag.Racks.Rack.FanTraies.FanTray, self).__setattr__(name, value)


                    class Fanses(Entity):
                        """
                        Table for rack fans 
                        
                        .. attribute:: fans
                        
                        	Fan name
                        	**type**\: list of    :py:class:`Fans <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sdr_invmgr_diag_oper.Diag.Racks.Rack.FanTraies.FanTray.Fanses.Fans>`
                        
                        

                        """

                        _prefix = 'sdr-invmgr-diag-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Diag.Racks.Rack.FanTraies.FanTray.Fanses, self).__init__()

                            self.yang_name = "fanses"
                            self.yang_parent_name = "fan-tray"

                            self.fans = YList(self)

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in () and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Diag.Racks.Rack.FanTraies.FanTray.Fanses, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Diag.Racks.Rack.FanTraies.FanTray.Fanses, self).__setattr__(name, value)


                        class Fans(Entity):
                            """
                            Fan name
                            
                            .. attribute:: fans_name  <key>
                            
                            	Fans name
                            	**type**\:  str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            .. attribute:: information
                            
                            	Basic information
                            	**type**\:   :py:class:`Information <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sdr_invmgr_diag_oper.Diag.Racks.Rack.FanTraies.FanTray.Fanses.Fans.Information>`
                            
                            

                            """

                            _prefix = 'sdr-invmgr-diag-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Diag.Racks.Rack.FanTraies.FanTray.Fanses.Fans, self).__init__()

                                self.yang_name = "fans"
                                self.yang_parent_name = "fanses"

                                self.fans_name = YLeaf(YType.str, "fans-name")

                                self.information = Diag.Racks.Rack.FanTraies.FanTray.Fanses.Fans.Information()
                                self.information.parent = self
                                self._children_name_map["information"] = "information"
                                self._children_yang_names.add("information")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("fans_name") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Diag.Racks.Rack.FanTraies.FanTray.Fanses.Fans, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Diag.Racks.Rack.FanTraies.FanTray.Fanses.Fans, self).__setattr__(name, value)


                            class Information(Entity):
                                """
                                Basic information
                                
                                .. attribute:: asset_alias
                                
                                	Asset Alias
                                	**type**\:  str
                                
                                	**length:** 0..255
                                
                                .. attribute:: asset_id
                                
                                	Asset ID
                                	**type**\:  str
                                
                                	**length:** 0..255
                                
                                .. attribute:: base_mac_address1
                                
                                	Base Mac Address #1
                                	**type**\:  str
                                
                                	**length:** 0..255
                                
                                .. attribute:: base_mac_address2
                                
                                	Base Mac Address #2
                                	**type**\:  str
                                
                                	**length:** 0..255
                                
                                .. attribute:: base_mac_address3
                                
                                	Base Mac Address #3
                                	**type**\:  str
                                
                                	**length:** 0..255
                                
                                .. attribute:: base_mac_address4
                                
                                	Base Mac Address #4
                                	**type**\:  str
                                
                                	**length:** 0..255
                                
                                .. attribute:: block_checksum
                                
                                	Block Checksum
                                	**type**\:  str
                                
                                	**length:** 0..255
                                
                                .. attribute:: block_count
                                
                                	Block Count
                                	**type**\:  str
                                
                                	**length:** 0..255
                                
                                .. attribute:: block_length
                                
                                	Block Length
                                	**type**\:  str
                                
                                	**length:** 0..255
                                
                                .. attribute:: block_signature
                                
                                	Block Signature
                                	**type**\:  str
                                
                                	**length:** 0..255
                                
                                .. attribute:: block_version
                                
                                	Block Version
                                	**type**\:  str
                                
                                	**length:** 0..255
                                
                                .. attribute:: chassis_sid
                                
                                	Chassis serial number
                                	**type**\:  str
                                
                                	**length:** 0..255
                                
                                .. attribute:: clei
                                
                                	Common Language Equipment Identifier (CLEI) code
                                	**type**\:  str
                                
                                	**length:** 0..255
                                
                                .. attribute:: controller_family
                                
                                	Controller family
                                	**type**\:  str
                                
                                	**length:** 0..255
                                
                                .. attribute:: controller_type
                                
                                	Controller type
                                	**type**\:  str
                                
                                	**length:** 0..255
                                
                                .. attribute:: description
                                
                                	A textual description of physical entity
                                	**type**\:  str
                                
                                	**length:** 0..255
                                
                                .. attribute:: dev_num1
                                
                                	Deviation Number # 1
                                	**type**\:  str
                                
                                	**length:** 0..255
                                
                                .. attribute:: dev_num2
                                
                                	Deviation Number # 2
                                	**type**\:  str
                                
                                	**length:** 0..255
                                
                                .. attribute:: dev_num3
                                
                                	Deviation Number # 3
                                	**type**\:  str
                                
                                	**length:** 0..255
                                
                                .. attribute:: dev_num4
                                
                                	Deviation Number # 4
                                	**type**\:  str
                                
                                	**length:** 0..255
                                
                                .. attribute:: dev_num5
                                
                                	Deviation Number # 5
                                	**type**\:  str
                                
                                	**length:** 0..255
                                
                                .. attribute:: dev_num6
                                
                                	Deviation Number # 6
                                	**type**\:  str
                                
                                	**length:** 0..255
                                
                                .. attribute:: dev_num7
                                
                                	Deviation Number # 7
                                	**type**\:  str
                                
                                	**length:** 0..255
                                
                                .. attribute:: eci
                                
                                	Equipment Catalog Item (ECI) number
                                	**type**\:  str
                                
                                	**length:** 0..255
                                
                                .. attribute:: eeprom_size
                                
                                	EEPROM Size
                                	**type**\:  str
                                
                                	**length:** 0..255
                                
                                .. attribute:: engineer_use
                                
                                	Engineer Use
                                	**type**\:  str
                                
                                	**length:** 0..255
                                
                                .. attribute:: fru_major_type
                                
                                	FRU Major Type
                                	**type**\:  str
                                
                                	**length:** 0..255
                                
                                .. attribute:: fru_minor_type
                                
                                	FRU Minor Type
                                	**type**\:  str
                                
                                	**length:** 0..255
                                
                                .. attribute:: hw_version
                                
                                	Hardware Version
                                	**type**\:  str
                                
                                	**length:** 0..255
                                
                                .. attribute:: hwid
                                
                                	Hardware Revision
                                	**type**\:  str
                                
                                	**length:** 0..255
                                
                                .. attribute:: idprom_format_rev
                                
                                	IDPROM Format Revision
                                	**type**\:  str
                                
                                	**length:** 0..255
                                
                                .. attribute:: mac_add_blk_size1
                                
                                	Mac Address Block Size #1
                                	**type**\:  str
                                
                                	**length:** 0..255
                                
                                .. attribute:: mac_add_blk_size2
                                
                                	Mac Address Block Size #2
                                	**type**\:  str
                                
                                	**length:** 0..255
                                
                                .. attribute:: mac_add_blk_size3
                                
                                	Mac Address Block Size #3
                                	**type**\:  str
                                
                                	**length:** 0..255
                                
                                .. attribute:: mac_add_blk_size4
                                
                                	Mac Address Block Size #4
                                	**type**\:  str
                                
                                	**length:** 0..255
                                
                                .. attribute:: manu_test_data
                                
                                	Manufacturing Test Data
                                	**type**\:  str
                                
                                	**length:** 0..255
                                
                                .. attribute:: mfg_bits
                                
                                	MFG Bits
                                	**type**\:  str
                                
                                	**length:** 0..255
                                
                                .. attribute:: mfg_deviation
                                
                                	MFG Deviation
                                	**type**\:  str
                                
                                	**length:** 0..255
                                
                                .. attribute:: oem_string
                                
                                	OEM String
                                	**type**\:  str
                                
                                	**length:** 0..255
                                
                                .. attribute:: part_number
                                
                                	Part Number
                                	**type**\:  str
                                
                                	**length:** 0..255
                                
                                .. attribute:: part_revision
                                
                                	Part Revision
                                	**type**\:  str
                                
                                	**length:** 0..255
                                
                                .. attribute:: pca_num
                                
                                	PCA number
                                	**type**\:  str
                                
                                	**length:** 0..255
                                
                                .. attribute:: pcavid
                                
                                	PCA revision ID
                                	**type**\:  str
                                
                                	**length:** 0..255
                                
                                .. attribute:: pcb_serial_num
                                
                                	PCB Serial Number
                                	**type**\:  str
                                
                                	**length:** 0..255
                                
                                .. attribute:: pid
                                
                                	Product ID
                                	**type**\:  str
                                
                                	**length:** 0..255
                                
                                .. attribute:: power_consumption
                                
                                	Power Consumption
                                	**type**\:  str
                                
                                	**length:** 0..255
                                
                                .. attribute:: power_supply_type
                                
                                	Power Supply Type
                                	**type**\:  str
                                
                                	**length:** 0..255
                                
                                .. attribute:: product_id
                                
                                	Product ID
                                	**type**\:  str
                                
                                	**length:** 0..255
                                
                                .. attribute:: rma
                                
                                	RMA Data
                                	**type**\:   :py:class:`Rma <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sdr_invmgr_diag_oper.Diag.Racks.Rack.FanTraies.FanTray.Fanses.Fans.Information.Rma>`
                                
                                .. attribute:: rma_code
                                
                                	RMA Code
                                	**type**\:  str
                                
                                	**length:** 0..255
                                
                                .. attribute:: serial_number
                                
                                	Serial Number
                                	**type**\:  str
                                
                                	**length:** 0..255
                                
                                .. attribute:: snmpoid
                                
                                	SNMP OID
                                	**type**\:  str
                                
                                	**length:** 0..255
                                
                                .. attribute:: top_assem_part_num
                                
                                	Top assembly part number
                                	**type**\:  str
                                
                                	**length:** 0..255
                                
                                .. attribute:: top_assem_vid
                                
                                	Top assembly revision number
                                	**type**\:  str
                                
                                	**length:** 0..255
                                
                                .. attribute:: udi_description
                                
                                	UDI description
                                	**type**\:  str
                                
                                	**length:** 0..255
                                
                                .. attribute:: udi_name
                                
                                	UDI name
                                	**type**\:  str
                                
                                	**length:** 0..255
                                
                                .. attribute:: vid
                                
                                	Version ID
                                	**type**\:  str
                                
                                	**length:** 0..255
                                
                                

                                """

                                _prefix = 'sdr-invmgr-diag-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Diag.Racks.Rack.FanTraies.FanTray.Fanses.Fans.Information, self).__init__()

                                    self.yang_name = "information"
                                    self.yang_parent_name = "fans"

                                    self.asset_alias = YLeaf(YType.str, "asset-alias")

                                    self.asset_id = YLeaf(YType.str, "asset-id")

                                    self.base_mac_address1 = YLeaf(YType.str, "base-mac-address1")

                                    self.base_mac_address2 = YLeaf(YType.str, "base-mac-address2")

                                    self.base_mac_address3 = YLeaf(YType.str, "base-mac-address3")

                                    self.base_mac_address4 = YLeaf(YType.str, "base-mac-address4")

                                    self.block_checksum = YLeaf(YType.str, "block-checksum")

                                    self.block_count = YLeaf(YType.str, "block-count")

                                    self.block_length = YLeaf(YType.str, "block-length")

                                    self.block_signature = YLeaf(YType.str, "block-signature")

                                    self.block_version = YLeaf(YType.str, "block-version")

                                    self.chassis_sid = YLeaf(YType.str, "chassis-sid")

                                    self.clei = YLeaf(YType.str, "clei")

                                    self.controller_family = YLeaf(YType.str, "controller-family")

                                    self.controller_type = YLeaf(YType.str, "controller-type")

                                    self.description = YLeaf(YType.str, "description")

                                    self.dev_num1 = YLeaf(YType.str, "dev-num1")

                                    self.dev_num2 = YLeaf(YType.str, "dev-num2")

                                    self.dev_num3 = YLeaf(YType.str, "dev-num3")

                                    self.dev_num4 = YLeaf(YType.str, "dev-num4")

                                    self.dev_num5 = YLeaf(YType.str, "dev-num5")

                                    self.dev_num6 = YLeaf(YType.str, "dev-num6")

                                    self.dev_num7 = YLeaf(YType.str, "dev-num7")

                                    self.eci = YLeaf(YType.str, "eci")

                                    self.eeprom_size = YLeaf(YType.str, "eeprom-size")

                                    self.engineer_use = YLeaf(YType.str, "engineer-use")

                                    self.fru_major_type = YLeaf(YType.str, "fru-major-type")

                                    self.fru_minor_type = YLeaf(YType.str, "fru-minor-type")

                                    self.hw_version = YLeaf(YType.str, "hw-version")

                                    self.hwid = YLeaf(YType.str, "hwid")

                                    self.idprom_format_rev = YLeaf(YType.str, "idprom-format-rev")

                                    self.mac_add_blk_size1 = YLeaf(YType.str, "mac-add-blk-size1")

                                    self.mac_add_blk_size2 = YLeaf(YType.str, "mac-add-blk-size2")

                                    self.mac_add_blk_size3 = YLeaf(YType.str, "mac-add-blk-size3")

                                    self.mac_add_blk_size4 = YLeaf(YType.str, "mac-add-blk-size4")

                                    self.manu_test_data = YLeaf(YType.str, "manu-test-data")

                                    self.mfg_bits = YLeaf(YType.str, "mfg-bits")

                                    self.mfg_deviation = YLeaf(YType.str, "mfg-deviation")

                                    self.oem_string = YLeaf(YType.str, "oem-string")

                                    self.part_number = YLeaf(YType.str, "part-number")

                                    self.part_revision = YLeaf(YType.str, "part-revision")

                                    self.pca_num = YLeaf(YType.str, "pca-num")

                                    self.pcavid = YLeaf(YType.str, "pcavid")

                                    self.pcb_serial_num = YLeaf(YType.str, "pcb-serial-num")

                                    self.pid = YLeaf(YType.str, "pid")

                                    self.power_consumption = YLeaf(YType.str, "power-consumption")

                                    self.power_supply_type = YLeaf(YType.str, "power-supply-type")

                                    self.product_id = YLeaf(YType.str, "product-id")

                                    self.rma_code = YLeaf(YType.str, "rma-code")

                                    self.serial_number = YLeaf(YType.str, "serial-number")

                                    self.snmpoid = YLeaf(YType.str, "snmpoid")

                                    self.top_assem_part_num = YLeaf(YType.str, "top-assem-part-num")

                                    self.top_assem_vid = YLeaf(YType.str, "top-assem-vid")

                                    self.udi_description = YLeaf(YType.str, "udi-description")

                                    self.udi_name = YLeaf(YType.str, "udi-name")

                                    self.vid = YLeaf(YType.str, "vid")

                                    self.rma = Diag.Racks.Rack.FanTraies.FanTray.Fanses.Fans.Information.Rma()
                                    self.rma.parent = self
                                    self._children_name_map["rma"] = "rma"
                                    self._children_yang_names.add("rma")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("asset_alias",
                                                    "asset_id",
                                                    "base_mac_address1",
                                                    "base_mac_address2",
                                                    "base_mac_address3",
                                                    "base_mac_address4",
                                                    "block_checksum",
                                                    "block_count",
                                                    "block_length",
                                                    "block_signature",
                                                    "block_version",
                                                    "chassis_sid",
                                                    "clei",
                                                    "controller_family",
                                                    "controller_type",
                                                    "description",
                                                    "dev_num1",
                                                    "dev_num2",
                                                    "dev_num3",
                                                    "dev_num4",
                                                    "dev_num5",
                                                    "dev_num6",
                                                    "dev_num7",
                                                    "eci",
                                                    "eeprom_size",
                                                    "engineer_use",
                                                    "fru_major_type",
                                                    "fru_minor_type",
                                                    "hw_version",
                                                    "hwid",
                                                    "idprom_format_rev",
                                                    "mac_add_blk_size1",
                                                    "mac_add_blk_size2",
                                                    "mac_add_blk_size3",
                                                    "mac_add_blk_size4",
                                                    "manu_test_data",
                                                    "mfg_bits",
                                                    "mfg_deviation",
                                                    "oem_string",
                                                    "part_number",
                                                    "part_revision",
                                                    "pca_num",
                                                    "pcavid",
                                                    "pcb_serial_num",
                                                    "pid",
                                                    "power_consumption",
                                                    "power_supply_type",
                                                    "product_id",
                                                    "rma_code",
                                                    "serial_number",
                                                    "snmpoid",
                                                    "top_assem_part_num",
                                                    "top_assem_vid",
                                                    "udi_description",
                                                    "udi_name",
                                                    "vid") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(Diag.Racks.Rack.FanTraies.FanTray.Fanses.Fans.Information, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Diag.Racks.Rack.FanTraies.FanTray.Fanses.Fans.Information, self).__setattr__(name, value)


                                class Rma(Entity):
                                    """
                                    RMA Data
                                    
                                    .. attribute:: rma_history
                                    
                                    	RMA history
                                    	**type**\:  str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: rma_number
                                    
                                    	RMA tracking number format is N\-N\-N
                                    	**type**\:  str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: test_history
                                    
                                    	Test history
                                    	**type**\:  str
                                    
                                    	**length:** 0..255
                                    
                                    

                                    """

                                    _prefix = 'sdr-invmgr-diag-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Diag.Racks.Rack.FanTraies.FanTray.Fanses.Fans.Information.Rma, self).__init__()

                                        self.yang_name = "rma"
                                        self.yang_parent_name = "information"

                                        self.rma_history = YLeaf(YType.str, "rma-history")

                                        self.rma_number = YLeaf(YType.str, "rma-number")

                                        self.test_history = YLeaf(YType.str, "test-history")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("rma_history",
                                                        "rma_number",
                                                        "test_history") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(Diag.Racks.Rack.FanTraies.FanTray.Fanses.Fans.Information.Rma, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(Diag.Racks.Rack.FanTraies.FanTray.Fanses.Fans.Information.Rma, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.rma_history.is_set or
                                            self.rma_number.is_set or
                                            self.test_history.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.rma_history.yfilter != YFilter.not_set or
                                            self.rma_number.yfilter != YFilter.not_set or
                                            self.test_history.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "rma" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.rma_history.is_set or self.rma_history.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.rma_history.get_name_leafdata())
                                        if (self.rma_number.is_set or self.rma_number.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.rma_number.get_name_leafdata())
                                        if (self.test_history.is_set or self.test_history.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.test_history.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "rma-history" or name == "rma-number" or name == "test-history"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "rma-history"):
                                            self.rma_history = value
                                            self.rma_history.value_namespace = name_space
                                            self.rma_history.value_namespace_prefix = name_space_prefix
                                        if(value_path == "rma-number"):
                                            self.rma_number = value
                                            self.rma_number.value_namespace = name_space
                                            self.rma_number.value_namespace_prefix = name_space_prefix
                                        if(value_path == "test-history"):
                                            self.test_history = value
                                            self.test_history.value_namespace = name_space
                                            self.test_history.value_namespace_prefix = name_space_prefix

                                def has_data(self):
                                    return (
                                        self.asset_alias.is_set or
                                        self.asset_id.is_set or
                                        self.base_mac_address1.is_set or
                                        self.base_mac_address2.is_set or
                                        self.base_mac_address3.is_set or
                                        self.base_mac_address4.is_set or
                                        self.block_checksum.is_set or
                                        self.block_count.is_set or
                                        self.block_length.is_set or
                                        self.block_signature.is_set or
                                        self.block_version.is_set or
                                        self.chassis_sid.is_set or
                                        self.clei.is_set or
                                        self.controller_family.is_set or
                                        self.controller_type.is_set or
                                        self.description.is_set or
                                        self.dev_num1.is_set or
                                        self.dev_num2.is_set or
                                        self.dev_num3.is_set or
                                        self.dev_num4.is_set or
                                        self.dev_num5.is_set or
                                        self.dev_num6.is_set or
                                        self.dev_num7.is_set or
                                        self.eci.is_set or
                                        self.eeprom_size.is_set or
                                        self.engineer_use.is_set or
                                        self.fru_major_type.is_set or
                                        self.fru_minor_type.is_set or
                                        self.hw_version.is_set or
                                        self.hwid.is_set or
                                        self.idprom_format_rev.is_set or
                                        self.mac_add_blk_size1.is_set or
                                        self.mac_add_blk_size2.is_set or
                                        self.mac_add_blk_size3.is_set or
                                        self.mac_add_blk_size4.is_set or
                                        self.manu_test_data.is_set or
                                        self.mfg_bits.is_set or
                                        self.mfg_deviation.is_set or
                                        self.oem_string.is_set or
                                        self.part_number.is_set or
                                        self.part_revision.is_set or
                                        self.pca_num.is_set or
                                        self.pcavid.is_set or
                                        self.pcb_serial_num.is_set or
                                        self.pid.is_set or
                                        self.power_consumption.is_set or
                                        self.power_supply_type.is_set or
                                        self.product_id.is_set or
                                        self.rma_code.is_set or
                                        self.serial_number.is_set or
                                        self.snmpoid.is_set or
                                        self.top_assem_part_num.is_set or
                                        self.top_assem_vid.is_set or
                                        self.udi_description.is_set or
                                        self.udi_name.is_set or
                                        self.vid.is_set or
                                        (self.rma is not None and self.rma.has_data()))

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.asset_alias.yfilter != YFilter.not_set or
                                        self.asset_id.yfilter != YFilter.not_set or
                                        self.base_mac_address1.yfilter != YFilter.not_set or
                                        self.base_mac_address2.yfilter != YFilter.not_set or
                                        self.base_mac_address3.yfilter != YFilter.not_set or
                                        self.base_mac_address4.yfilter != YFilter.not_set or
                                        self.block_checksum.yfilter != YFilter.not_set or
                                        self.block_count.yfilter != YFilter.not_set or
                                        self.block_length.yfilter != YFilter.not_set or
                                        self.block_signature.yfilter != YFilter.not_set or
                                        self.block_version.yfilter != YFilter.not_set or
                                        self.chassis_sid.yfilter != YFilter.not_set or
                                        self.clei.yfilter != YFilter.not_set or
                                        self.controller_family.yfilter != YFilter.not_set or
                                        self.controller_type.yfilter != YFilter.not_set or
                                        self.description.yfilter != YFilter.not_set or
                                        self.dev_num1.yfilter != YFilter.not_set or
                                        self.dev_num2.yfilter != YFilter.not_set or
                                        self.dev_num3.yfilter != YFilter.not_set or
                                        self.dev_num4.yfilter != YFilter.not_set or
                                        self.dev_num5.yfilter != YFilter.not_set or
                                        self.dev_num6.yfilter != YFilter.not_set or
                                        self.dev_num7.yfilter != YFilter.not_set or
                                        self.eci.yfilter != YFilter.not_set or
                                        self.eeprom_size.yfilter != YFilter.not_set or
                                        self.engineer_use.yfilter != YFilter.not_set or
                                        self.fru_major_type.yfilter != YFilter.not_set or
                                        self.fru_minor_type.yfilter != YFilter.not_set or
                                        self.hw_version.yfilter != YFilter.not_set or
                                        self.hwid.yfilter != YFilter.not_set or
                                        self.idprom_format_rev.yfilter != YFilter.not_set or
                                        self.mac_add_blk_size1.yfilter != YFilter.not_set or
                                        self.mac_add_blk_size2.yfilter != YFilter.not_set or
                                        self.mac_add_blk_size3.yfilter != YFilter.not_set or
                                        self.mac_add_blk_size4.yfilter != YFilter.not_set or
                                        self.manu_test_data.yfilter != YFilter.not_set or
                                        self.mfg_bits.yfilter != YFilter.not_set or
                                        self.mfg_deviation.yfilter != YFilter.not_set or
                                        self.oem_string.yfilter != YFilter.not_set or
                                        self.part_number.yfilter != YFilter.not_set or
                                        self.part_revision.yfilter != YFilter.not_set or
                                        self.pca_num.yfilter != YFilter.not_set or
                                        self.pcavid.yfilter != YFilter.not_set or
                                        self.pcb_serial_num.yfilter != YFilter.not_set or
                                        self.pid.yfilter != YFilter.not_set or
                                        self.power_consumption.yfilter != YFilter.not_set or
                                        self.power_supply_type.yfilter != YFilter.not_set or
                                        self.product_id.yfilter != YFilter.not_set or
                                        self.rma_code.yfilter != YFilter.not_set or
                                        self.serial_number.yfilter != YFilter.not_set or
                                        self.snmpoid.yfilter != YFilter.not_set or
                                        self.top_assem_part_num.yfilter != YFilter.not_set or
                                        self.top_assem_vid.yfilter != YFilter.not_set or
                                        self.udi_description.yfilter != YFilter.not_set or
                                        self.udi_name.yfilter != YFilter.not_set or
                                        self.vid.yfilter != YFilter.not_set or
                                        (self.rma is not None and self.rma.has_operation()))

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "information" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.asset_alias.is_set or self.asset_alias.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.asset_alias.get_name_leafdata())
                                    if (self.asset_id.is_set or self.asset_id.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.asset_id.get_name_leafdata())
                                    if (self.base_mac_address1.is_set or self.base_mac_address1.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.base_mac_address1.get_name_leafdata())
                                    if (self.base_mac_address2.is_set or self.base_mac_address2.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.base_mac_address2.get_name_leafdata())
                                    if (self.base_mac_address3.is_set or self.base_mac_address3.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.base_mac_address3.get_name_leafdata())
                                    if (self.base_mac_address4.is_set or self.base_mac_address4.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.base_mac_address4.get_name_leafdata())
                                    if (self.block_checksum.is_set or self.block_checksum.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.block_checksum.get_name_leafdata())
                                    if (self.block_count.is_set or self.block_count.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.block_count.get_name_leafdata())
                                    if (self.block_length.is_set or self.block_length.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.block_length.get_name_leafdata())
                                    if (self.block_signature.is_set or self.block_signature.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.block_signature.get_name_leafdata())
                                    if (self.block_version.is_set or self.block_version.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.block_version.get_name_leafdata())
                                    if (self.chassis_sid.is_set or self.chassis_sid.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.chassis_sid.get_name_leafdata())
                                    if (self.clei.is_set or self.clei.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.clei.get_name_leafdata())
                                    if (self.controller_family.is_set or self.controller_family.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.controller_family.get_name_leafdata())
                                    if (self.controller_type.is_set or self.controller_type.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.controller_type.get_name_leafdata())
                                    if (self.description.is_set or self.description.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.description.get_name_leafdata())
                                    if (self.dev_num1.is_set or self.dev_num1.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.dev_num1.get_name_leafdata())
                                    if (self.dev_num2.is_set or self.dev_num2.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.dev_num2.get_name_leafdata())
                                    if (self.dev_num3.is_set or self.dev_num3.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.dev_num3.get_name_leafdata())
                                    if (self.dev_num4.is_set or self.dev_num4.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.dev_num4.get_name_leafdata())
                                    if (self.dev_num5.is_set or self.dev_num5.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.dev_num5.get_name_leafdata())
                                    if (self.dev_num6.is_set or self.dev_num6.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.dev_num6.get_name_leafdata())
                                    if (self.dev_num7.is_set or self.dev_num7.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.dev_num7.get_name_leafdata())
                                    if (self.eci.is_set or self.eci.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.eci.get_name_leafdata())
                                    if (self.eeprom_size.is_set or self.eeprom_size.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.eeprom_size.get_name_leafdata())
                                    if (self.engineer_use.is_set or self.engineer_use.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.engineer_use.get_name_leafdata())
                                    if (self.fru_major_type.is_set or self.fru_major_type.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.fru_major_type.get_name_leafdata())
                                    if (self.fru_minor_type.is_set or self.fru_minor_type.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.fru_minor_type.get_name_leafdata())
                                    if (self.hw_version.is_set or self.hw_version.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.hw_version.get_name_leafdata())
                                    if (self.hwid.is_set or self.hwid.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.hwid.get_name_leafdata())
                                    if (self.idprom_format_rev.is_set or self.idprom_format_rev.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.idprom_format_rev.get_name_leafdata())
                                    if (self.mac_add_blk_size1.is_set or self.mac_add_blk_size1.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.mac_add_blk_size1.get_name_leafdata())
                                    if (self.mac_add_blk_size2.is_set or self.mac_add_blk_size2.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.mac_add_blk_size2.get_name_leafdata())
                                    if (self.mac_add_blk_size3.is_set or self.mac_add_blk_size3.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.mac_add_blk_size3.get_name_leafdata())
                                    if (self.mac_add_blk_size4.is_set or self.mac_add_blk_size4.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.mac_add_blk_size4.get_name_leafdata())
                                    if (self.manu_test_data.is_set or self.manu_test_data.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.manu_test_data.get_name_leafdata())
                                    if (self.mfg_bits.is_set or self.mfg_bits.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.mfg_bits.get_name_leafdata())
                                    if (self.mfg_deviation.is_set or self.mfg_deviation.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.mfg_deviation.get_name_leafdata())
                                    if (self.oem_string.is_set or self.oem_string.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.oem_string.get_name_leafdata())
                                    if (self.part_number.is_set or self.part_number.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.part_number.get_name_leafdata())
                                    if (self.part_revision.is_set or self.part_revision.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.part_revision.get_name_leafdata())
                                    if (self.pca_num.is_set or self.pca_num.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.pca_num.get_name_leafdata())
                                    if (self.pcavid.is_set or self.pcavid.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.pcavid.get_name_leafdata())
                                    if (self.pcb_serial_num.is_set or self.pcb_serial_num.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.pcb_serial_num.get_name_leafdata())
                                    if (self.pid.is_set or self.pid.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.pid.get_name_leafdata())
                                    if (self.power_consumption.is_set or self.power_consumption.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.power_consumption.get_name_leafdata())
                                    if (self.power_supply_type.is_set or self.power_supply_type.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.power_supply_type.get_name_leafdata())
                                    if (self.product_id.is_set or self.product_id.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.product_id.get_name_leafdata())
                                    if (self.rma_code.is_set or self.rma_code.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.rma_code.get_name_leafdata())
                                    if (self.serial_number.is_set or self.serial_number.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.serial_number.get_name_leafdata())
                                    if (self.snmpoid.is_set or self.snmpoid.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.snmpoid.get_name_leafdata())
                                    if (self.top_assem_part_num.is_set or self.top_assem_part_num.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.top_assem_part_num.get_name_leafdata())
                                    if (self.top_assem_vid.is_set or self.top_assem_vid.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.top_assem_vid.get_name_leafdata())
                                    if (self.udi_description.is_set or self.udi_description.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.udi_description.get_name_leafdata())
                                    if (self.udi_name.is_set or self.udi_name.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.udi_name.get_name_leafdata())
                                    if (self.vid.is_set or self.vid.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.vid.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    if (child_yang_name == "rma"):
                                        if (self.rma is None):
                                            self.rma = Diag.Racks.Rack.FanTraies.FanTray.Fanses.Fans.Information.Rma()
                                            self.rma.parent = self
                                            self._children_name_map["rma"] = "rma"
                                        return self.rma

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "rma" or name == "asset-alias" or name == "asset-id" or name == "base-mac-address1" or name == "base-mac-address2" or name == "base-mac-address3" or name == "base-mac-address4" or name == "block-checksum" or name == "block-count" or name == "block-length" or name == "block-signature" or name == "block-version" or name == "chassis-sid" or name == "clei" or name == "controller-family" or name == "controller-type" or name == "description" or name == "dev-num1" or name == "dev-num2" or name == "dev-num3" or name == "dev-num4" or name == "dev-num5" or name == "dev-num6" or name == "dev-num7" or name == "eci" or name == "eeprom-size" or name == "engineer-use" or name == "fru-major-type" or name == "fru-minor-type" or name == "hw-version" or name == "hwid" or name == "idprom-format-rev" or name == "mac-add-blk-size1" or name == "mac-add-blk-size2" or name == "mac-add-blk-size3" or name == "mac-add-blk-size4" or name == "manu-test-data" or name == "mfg-bits" or name == "mfg-deviation" or name == "oem-string" or name == "part-number" or name == "part-revision" or name == "pca-num" or name == "pcavid" or name == "pcb-serial-num" or name == "pid" or name == "power-consumption" or name == "power-supply-type" or name == "product-id" or name == "rma-code" or name == "serial-number" or name == "snmpoid" or name == "top-assem-part-num" or name == "top-assem-vid" or name == "udi-description" or name == "udi-name" or name == "vid"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "asset-alias"):
                                        self.asset_alias = value
                                        self.asset_alias.value_namespace = name_space
                                        self.asset_alias.value_namespace_prefix = name_space_prefix
                                    if(value_path == "asset-id"):
                                        self.asset_id = value
                                        self.asset_id.value_namespace = name_space
                                        self.asset_id.value_namespace_prefix = name_space_prefix
                                    if(value_path == "base-mac-address1"):
                                        self.base_mac_address1 = value
                                        self.base_mac_address1.value_namespace = name_space
                                        self.base_mac_address1.value_namespace_prefix = name_space_prefix
                                    if(value_path == "base-mac-address2"):
                                        self.base_mac_address2 = value
                                        self.base_mac_address2.value_namespace = name_space
                                        self.base_mac_address2.value_namespace_prefix = name_space_prefix
                                    if(value_path == "base-mac-address3"):
                                        self.base_mac_address3 = value
                                        self.base_mac_address3.value_namespace = name_space
                                        self.base_mac_address3.value_namespace_prefix = name_space_prefix
                                    if(value_path == "base-mac-address4"):
                                        self.base_mac_address4 = value
                                        self.base_mac_address4.value_namespace = name_space
                                        self.base_mac_address4.value_namespace_prefix = name_space_prefix
                                    if(value_path == "block-checksum"):
                                        self.block_checksum = value
                                        self.block_checksum.value_namespace = name_space
                                        self.block_checksum.value_namespace_prefix = name_space_prefix
                                    if(value_path == "block-count"):
                                        self.block_count = value
                                        self.block_count.value_namespace = name_space
                                        self.block_count.value_namespace_prefix = name_space_prefix
                                    if(value_path == "block-length"):
                                        self.block_length = value
                                        self.block_length.value_namespace = name_space
                                        self.block_length.value_namespace_prefix = name_space_prefix
                                    if(value_path == "block-signature"):
                                        self.block_signature = value
                                        self.block_signature.value_namespace = name_space
                                        self.block_signature.value_namespace_prefix = name_space_prefix
                                    if(value_path == "block-version"):
                                        self.block_version = value
                                        self.block_version.value_namespace = name_space
                                        self.block_version.value_namespace_prefix = name_space_prefix
                                    if(value_path == "chassis-sid"):
                                        self.chassis_sid = value
                                        self.chassis_sid.value_namespace = name_space
                                        self.chassis_sid.value_namespace_prefix = name_space_prefix
                                    if(value_path == "clei"):
                                        self.clei = value
                                        self.clei.value_namespace = name_space
                                        self.clei.value_namespace_prefix = name_space_prefix
                                    if(value_path == "controller-family"):
                                        self.controller_family = value
                                        self.controller_family.value_namespace = name_space
                                        self.controller_family.value_namespace_prefix = name_space_prefix
                                    if(value_path == "controller-type"):
                                        self.controller_type = value
                                        self.controller_type.value_namespace = name_space
                                        self.controller_type.value_namespace_prefix = name_space_prefix
                                    if(value_path == "description"):
                                        self.description = value
                                        self.description.value_namespace = name_space
                                        self.description.value_namespace_prefix = name_space_prefix
                                    if(value_path == "dev-num1"):
                                        self.dev_num1 = value
                                        self.dev_num1.value_namespace = name_space
                                        self.dev_num1.value_namespace_prefix = name_space_prefix
                                    if(value_path == "dev-num2"):
                                        self.dev_num2 = value
                                        self.dev_num2.value_namespace = name_space
                                        self.dev_num2.value_namespace_prefix = name_space_prefix
                                    if(value_path == "dev-num3"):
                                        self.dev_num3 = value
                                        self.dev_num3.value_namespace = name_space
                                        self.dev_num3.value_namespace_prefix = name_space_prefix
                                    if(value_path == "dev-num4"):
                                        self.dev_num4 = value
                                        self.dev_num4.value_namespace = name_space
                                        self.dev_num4.value_namespace_prefix = name_space_prefix
                                    if(value_path == "dev-num5"):
                                        self.dev_num5 = value
                                        self.dev_num5.value_namespace = name_space
                                        self.dev_num5.value_namespace_prefix = name_space_prefix
                                    if(value_path == "dev-num6"):
                                        self.dev_num6 = value
                                        self.dev_num6.value_namespace = name_space
                                        self.dev_num6.value_namespace_prefix = name_space_prefix
                                    if(value_path == "dev-num7"):
                                        self.dev_num7 = value
                                        self.dev_num7.value_namespace = name_space
                                        self.dev_num7.value_namespace_prefix = name_space_prefix
                                    if(value_path == "eci"):
                                        self.eci = value
                                        self.eci.value_namespace = name_space
                                        self.eci.value_namespace_prefix = name_space_prefix
                                    if(value_path == "eeprom-size"):
                                        self.eeprom_size = value
                                        self.eeprom_size.value_namespace = name_space
                                        self.eeprom_size.value_namespace_prefix = name_space_prefix
                                    if(value_path == "engineer-use"):
                                        self.engineer_use = value
                                        self.engineer_use.value_namespace = name_space
                                        self.engineer_use.value_namespace_prefix = name_space_prefix
                                    if(value_path == "fru-major-type"):
                                        self.fru_major_type = value
                                        self.fru_major_type.value_namespace = name_space
                                        self.fru_major_type.value_namespace_prefix = name_space_prefix
                                    if(value_path == "fru-minor-type"):
                                        self.fru_minor_type = value
                                        self.fru_minor_type.value_namespace = name_space
                                        self.fru_minor_type.value_namespace_prefix = name_space_prefix
                                    if(value_path == "hw-version"):
                                        self.hw_version = value
                                        self.hw_version.value_namespace = name_space
                                        self.hw_version.value_namespace_prefix = name_space_prefix
                                    if(value_path == "hwid"):
                                        self.hwid = value
                                        self.hwid.value_namespace = name_space
                                        self.hwid.value_namespace_prefix = name_space_prefix
                                    if(value_path == "idprom-format-rev"):
                                        self.idprom_format_rev = value
                                        self.idprom_format_rev.value_namespace = name_space
                                        self.idprom_format_rev.value_namespace_prefix = name_space_prefix
                                    if(value_path == "mac-add-blk-size1"):
                                        self.mac_add_blk_size1 = value
                                        self.mac_add_blk_size1.value_namespace = name_space
                                        self.mac_add_blk_size1.value_namespace_prefix = name_space_prefix
                                    if(value_path == "mac-add-blk-size2"):
                                        self.mac_add_blk_size2 = value
                                        self.mac_add_blk_size2.value_namespace = name_space
                                        self.mac_add_blk_size2.value_namespace_prefix = name_space_prefix
                                    if(value_path == "mac-add-blk-size3"):
                                        self.mac_add_blk_size3 = value
                                        self.mac_add_blk_size3.value_namespace = name_space
                                        self.mac_add_blk_size3.value_namespace_prefix = name_space_prefix
                                    if(value_path == "mac-add-blk-size4"):
                                        self.mac_add_blk_size4 = value
                                        self.mac_add_blk_size4.value_namespace = name_space
                                        self.mac_add_blk_size4.value_namespace_prefix = name_space_prefix
                                    if(value_path == "manu-test-data"):
                                        self.manu_test_data = value
                                        self.manu_test_data.value_namespace = name_space
                                        self.manu_test_data.value_namespace_prefix = name_space_prefix
                                    if(value_path == "mfg-bits"):
                                        self.mfg_bits = value
                                        self.mfg_bits.value_namespace = name_space
                                        self.mfg_bits.value_namespace_prefix = name_space_prefix
                                    if(value_path == "mfg-deviation"):
                                        self.mfg_deviation = value
                                        self.mfg_deviation.value_namespace = name_space
                                        self.mfg_deviation.value_namespace_prefix = name_space_prefix
                                    if(value_path == "oem-string"):
                                        self.oem_string = value
                                        self.oem_string.value_namespace = name_space
                                        self.oem_string.value_namespace_prefix = name_space_prefix
                                    if(value_path == "part-number"):
                                        self.part_number = value
                                        self.part_number.value_namespace = name_space
                                        self.part_number.value_namespace_prefix = name_space_prefix
                                    if(value_path == "part-revision"):
                                        self.part_revision = value
                                        self.part_revision.value_namespace = name_space
                                        self.part_revision.value_namespace_prefix = name_space_prefix
                                    if(value_path == "pca-num"):
                                        self.pca_num = value
                                        self.pca_num.value_namespace = name_space
                                        self.pca_num.value_namespace_prefix = name_space_prefix
                                    if(value_path == "pcavid"):
                                        self.pcavid = value
                                        self.pcavid.value_namespace = name_space
                                        self.pcavid.value_namespace_prefix = name_space_prefix
                                    if(value_path == "pcb-serial-num"):
                                        self.pcb_serial_num = value
                                        self.pcb_serial_num.value_namespace = name_space
                                        self.pcb_serial_num.value_namespace_prefix = name_space_prefix
                                    if(value_path == "pid"):
                                        self.pid = value
                                        self.pid.value_namespace = name_space
                                        self.pid.value_namespace_prefix = name_space_prefix
                                    if(value_path == "power-consumption"):
                                        self.power_consumption = value
                                        self.power_consumption.value_namespace = name_space
                                        self.power_consumption.value_namespace_prefix = name_space_prefix
                                    if(value_path == "power-supply-type"):
                                        self.power_supply_type = value
                                        self.power_supply_type.value_namespace = name_space
                                        self.power_supply_type.value_namespace_prefix = name_space_prefix
                                    if(value_path == "product-id"):
                                        self.product_id = value
                                        self.product_id.value_namespace = name_space
                                        self.product_id.value_namespace_prefix = name_space_prefix
                                    if(value_path == "rma-code"):
                                        self.rma_code = value
                                        self.rma_code.value_namespace = name_space
                                        self.rma_code.value_namespace_prefix = name_space_prefix
                                    if(value_path == "serial-number"):
                                        self.serial_number = value
                                        self.serial_number.value_namespace = name_space
                                        self.serial_number.value_namespace_prefix = name_space_prefix
                                    if(value_path == "snmpoid"):
                                        self.snmpoid = value
                                        self.snmpoid.value_namespace = name_space
                                        self.snmpoid.value_namespace_prefix = name_space_prefix
                                    if(value_path == "top-assem-part-num"):
                                        self.top_assem_part_num = value
                                        self.top_assem_part_num.value_namespace = name_space
                                        self.top_assem_part_num.value_namespace_prefix = name_space_prefix
                                    if(value_path == "top-assem-vid"):
                                        self.top_assem_vid = value
                                        self.top_assem_vid.value_namespace = name_space
                                        self.top_assem_vid.value_namespace_prefix = name_space_prefix
                                    if(value_path == "udi-description"):
                                        self.udi_description = value
                                        self.udi_description.value_namespace = name_space
                                        self.udi_description.value_namespace_prefix = name_space_prefix
                                    if(value_path == "udi-name"):
                                        self.udi_name = value
                                        self.udi_name.value_namespace = name_space
                                        self.udi_name.value_namespace_prefix = name_space_prefix
                                    if(value_path == "vid"):
                                        self.vid = value
                                        self.vid.value_namespace = name_space
                                        self.vid.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                return (
                                    self.fans_name.is_set or
                                    (self.information is not None and self.information.has_data()))

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.fans_name.yfilter != YFilter.not_set or
                                    (self.information is not None and self.information.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "fans" + "[fans-name='" + self.fans_name.get() + "']" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.fans_name.is_set or self.fans_name.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.fans_name.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                if (child_yang_name == "information"):
                                    if (self.information is None):
                                        self.information = Diag.Racks.Rack.FanTraies.FanTray.Fanses.Fans.Information()
                                        self.information.parent = self
                                        self._children_name_map["information"] = "information"
                                    return self.information

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "information" or name == "fans-name"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "fans-name"):
                                    self.fans_name = value
                                    self.fans_name.value_namespace = name_space
                                    self.fans_name.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.fans:
                                if (c.has_data()):
                                    return True
                            return False

                        def has_operation(self):
                            for c in self.fans:
                                if (c.has_operation()):
                                    return True
                            return self.yfilter != YFilter.not_set

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "fanses" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "fans"):
                                for c in self.fans:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = Diag.Racks.Rack.FanTraies.FanTray.Fanses.Fans()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.fans.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "fans"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass

                    def has_data(self):
                        return (
                            self.fan_tray_name.is_set or
                            (self.fanses is not None and self.fanses.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.fan_tray_name.yfilter != YFilter.not_set or
                            (self.fanses is not None and self.fanses.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "fan-tray" + "[fan-tray-name='" + self.fan_tray_name.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.fan_tray_name.is_set or self.fan_tray_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.fan_tray_name.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "fanses"):
                            if (self.fanses is None):
                                self.fanses = Diag.Racks.Rack.FanTraies.FanTray.Fanses()
                                self.fanses.parent = self
                                self._children_name_map["fanses"] = "fanses"
                            return self.fanses

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "fanses" or name == "fan-tray-name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "fan-tray-name"):
                            self.fan_tray_name = value
                            self.fan_tray_name.value_namespace = name_space
                            self.fan_tray_name.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.fan_tray:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.fan_tray:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "fan-traies" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "fan-tray"):
                        for c in self.fan_tray:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Diag.Racks.Rack.FanTraies.FanTray()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.fan_tray.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "fan-tray"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class Slots(Entity):
                """
                Table of slots
                
                .. attribute:: slot
                
                	Slot name
                	**type**\: list of    :py:class:`Slot <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sdr_invmgr_diag_oper.Diag.Racks.Rack.Slots.Slot>`
                
                

                """

                _prefix = 'sdr-invmgr-diag-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Diag.Racks.Rack.Slots, self).__init__()

                    self.yang_name = "slots"
                    self.yang_parent_name = "rack"

                    self.slot = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in () and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Diag.Racks.Rack.Slots, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Diag.Racks.Rack.Slots, self).__setattr__(name, value)


                class Slot(Entity):
                    """
                    Slot name
                    
                    .. attribute:: slot_name  <key>
                    
                    	Slot name
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: instances
                    
                    	Table of instances
                    	**type**\:   :py:class:`Instances <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sdr_invmgr_diag_oper.Diag.Racks.Rack.Slots.Slot.Instances>`
                    
                    

                    """

                    _prefix = 'sdr-invmgr-diag-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Diag.Racks.Rack.Slots.Slot, self).__init__()

                        self.yang_name = "slot"
                        self.yang_parent_name = "slots"

                        self.slot_name = YLeaf(YType.str, "slot-name")

                        self.instances = Diag.Racks.Rack.Slots.Slot.Instances()
                        self.instances.parent = self
                        self._children_name_map["instances"] = "instances"
                        self._children_yang_names.add("instances")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("slot_name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Diag.Racks.Rack.Slots.Slot, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Diag.Racks.Rack.Slots.Slot, self).__setattr__(name, value)


                    class Instances(Entity):
                        """
                        Table of instances
                        
                        .. attribute:: instance
                        
                        	instance number
                        	**type**\: list of    :py:class:`Instance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sdr_invmgr_diag_oper.Diag.Racks.Rack.Slots.Slot.Instances.Instance>`
                        
                        

                        """

                        _prefix = 'sdr-invmgr-diag-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Diag.Racks.Rack.Slots.Slot.Instances, self).__init__()

                            self.yang_name = "instances"
                            self.yang_parent_name = "slot"

                            self.instance = YList(self)

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in () and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Diag.Racks.Rack.Slots.Slot.Instances, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Diag.Racks.Rack.Slots.Slot.Instances, self).__setattr__(name, value)


                        class Instance(Entity):
                            """
                            instance number
                            
                            .. attribute:: name  <key>
                            
                            	Instance name
                            	**type**\:  str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            .. attribute:: detail
                            
                            	Detail information
                            	**type**\:   :py:class:`Detail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sdr_invmgr_diag_oper.Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail>`
                            
                            

                            """

                            _prefix = 'sdr-invmgr-diag-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Diag.Racks.Rack.Slots.Slot.Instances.Instance, self).__init__()

                                self.yang_name = "instance"
                                self.yang_parent_name = "instances"

                                self.name = YLeaf(YType.str, "name")

                                self.detail = Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail()
                                self.detail.parent = self
                                self._children_name_map["detail"] = "detail"
                                self._children_yang_names.add("detail")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("name") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Diag.Racks.Rack.Slots.Slot.Instances.Instance, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Diag.Racks.Rack.Slots.Slot.Instances.Instance, self).__setattr__(name, value)


                            class Detail(Entity):
                                """
                                Detail information
                                
                                .. attribute:: card_instance
                                
                                	Card instance
                                	**type**\:   :py:class:`CardInstance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sdr_invmgr_diag_oper.Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.CardInstance>`
                                
                                .. attribute:: node_operational_state
                                
                                	Node operational state 
                                	**type**\:  str
                                
                                	**length:** 0..255
                                
                                

                                """

                                _prefix = 'sdr-invmgr-diag-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail, self).__init__()

                                    self.yang_name = "detail"
                                    self.yang_parent_name = "instance"

                                    self.node_operational_state = YLeaf(YType.str, "node-operational-state")

                                    self.card_instance = Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.CardInstance()
                                    self.card_instance.parent = self
                                    self._children_name_map["card_instance"] = "card-instance"
                                    self._children_yang_names.add("card-instance")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("node_operational_state") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail, self).__setattr__(name, value)


                                class CardInstance(Entity):
                                    """
                                    Card instance
                                    
                                    .. attribute:: asset_alias
                                    
                                    	Asset Alias
                                    	**type**\:  str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: asset_id
                                    
                                    	Asset ID
                                    	**type**\:  str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: base_mac_address1
                                    
                                    	Base Mac Address #1
                                    	**type**\:  str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: base_mac_address2
                                    
                                    	Base Mac Address #2
                                    	**type**\:  str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: base_mac_address3
                                    
                                    	Base Mac Address #3
                                    	**type**\:  str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: base_mac_address4
                                    
                                    	Base Mac Address #4
                                    	**type**\:  str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: block_checksum
                                    
                                    	Block Checksum
                                    	**type**\:  str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: block_count
                                    
                                    	Block Count
                                    	**type**\:  str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: block_length
                                    
                                    	Block Length
                                    	**type**\:  str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: block_signature
                                    
                                    	Block Signature
                                    	**type**\:  str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: block_version
                                    
                                    	Block Version
                                    	**type**\:  str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: chassis_sid
                                    
                                    	Chassis serial number
                                    	**type**\:  str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: clei
                                    
                                    	Common Language Equipment Identifier (CLEI) code
                                    	**type**\:  str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: controller_family
                                    
                                    	Controller family
                                    	**type**\:  str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: controller_type
                                    
                                    	Controller type
                                    	**type**\:  str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: description
                                    
                                    	A textual description of physical entity
                                    	**type**\:  str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: dev_num1
                                    
                                    	Deviation Number # 1
                                    	**type**\:  str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: dev_num2
                                    
                                    	Deviation Number # 2
                                    	**type**\:  str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: dev_num3
                                    
                                    	Deviation Number # 3
                                    	**type**\:  str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: dev_num4
                                    
                                    	Deviation Number # 4
                                    	**type**\:  str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: dev_num5
                                    
                                    	Deviation Number # 5
                                    	**type**\:  str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: dev_num6
                                    
                                    	Deviation Number # 6
                                    	**type**\:  str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: dev_num7
                                    
                                    	Deviation Number # 7
                                    	**type**\:  str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: eci
                                    
                                    	Equipment Catalog Item (ECI) number
                                    	**type**\:  str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: eeprom_size
                                    
                                    	EEPROM Size
                                    	**type**\:  str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: engineer_use
                                    
                                    	Engineer Use
                                    	**type**\:  str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: fru_major_type
                                    
                                    	FRU Major Type
                                    	**type**\:  str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: fru_minor_type
                                    
                                    	FRU Minor Type
                                    	**type**\:  str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: hw_version
                                    
                                    	Hardware Version
                                    	**type**\:  str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: hwid
                                    
                                    	Hardware Revision
                                    	**type**\:  str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: idprom_format_rev
                                    
                                    	IDPROM Format Revision
                                    	**type**\:  str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: mac_add_blk_size1
                                    
                                    	Mac Address Block Size #1
                                    	**type**\:  str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: mac_add_blk_size2
                                    
                                    	Mac Address Block Size #2
                                    	**type**\:  str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: mac_add_blk_size3
                                    
                                    	Mac Address Block Size #3
                                    	**type**\:  str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: mac_add_blk_size4
                                    
                                    	Mac Address Block Size #4
                                    	**type**\:  str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: manu_test_data
                                    
                                    	Manufacturing Test Data
                                    	**type**\:  str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: mfg_bits
                                    
                                    	MFG Bits
                                    	**type**\:  str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: mfg_deviation
                                    
                                    	MFG Deviation
                                    	**type**\:  str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: oem_string
                                    
                                    	OEM String
                                    	**type**\:  str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: part_number
                                    
                                    	Part Number
                                    	**type**\:  str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: part_revision
                                    
                                    	Part Revision
                                    	**type**\:  str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: pca_num
                                    
                                    	PCA number
                                    	**type**\:  str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: pcavid
                                    
                                    	PCA revision ID
                                    	**type**\:  str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: pcb_serial_num
                                    
                                    	PCB Serial Number
                                    	**type**\:  str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: pid
                                    
                                    	Product ID
                                    	**type**\:  str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: power_consumption
                                    
                                    	Power Consumption
                                    	**type**\:  str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: power_supply_type
                                    
                                    	Power Supply Type
                                    	**type**\:  str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: product_id
                                    
                                    	Product ID
                                    	**type**\:  str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: rma
                                    
                                    	RMA Data
                                    	**type**\:   :py:class:`Rma <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sdr_invmgr_diag_oper.Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.CardInstance.Rma>`
                                    
                                    .. attribute:: rma_code
                                    
                                    	RMA Code
                                    	**type**\:  str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: serial_number
                                    
                                    	Serial Number
                                    	**type**\:  str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: snmpoid
                                    
                                    	SNMP OID
                                    	**type**\:  str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: top_assem_part_num
                                    
                                    	Top assembly part number
                                    	**type**\:  str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: top_assem_vid
                                    
                                    	Top assembly revision number
                                    	**type**\:  str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: udi_description
                                    
                                    	UDI description
                                    	**type**\:  str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: udi_name
                                    
                                    	UDI name
                                    	**type**\:  str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: vid
                                    
                                    	Version ID
                                    	**type**\:  str
                                    
                                    	**length:** 0..255
                                    
                                    

                                    """

                                    _prefix = 'sdr-invmgr-diag-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.CardInstance, self).__init__()

                                        self.yang_name = "card-instance"
                                        self.yang_parent_name = "detail"

                                        self.asset_alias = YLeaf(YType.str, "asset-alias")

                                        self.asset_id = YLeaf(YType.str, "asset-id")

                                        self.base_mac_address1 = YLeaf(YType.str, "base-mac-address1")

                                        self.base_mac_address2 = YLeaf(YType.str, "base-mac-address2")

                                        self.base_mac_address3 = YLeaf(YType.str, "base-mac-address3")

                                        self.base_mac_address4 = YLeaf(YType.str, "base-mac-address4")

                                        self.block_checksum = YLeaf(YType.str, "block-checksum")

                                        self.block_count = YLeaf(YType.str, "block-count")

                                        self.block_length = YLeaf(YType.str, "block-length")

                                        self.block_signature = YLeaf(YType.str, "block-signature")

                                        self.block_version = YLeaf(YType.str, "block-version")

                                        self.chassis_sid = YLeaf(YType.str, "chassis-sid")

                                        self.clei = YLeaf(YType.str, "clei")

                                        self.controller_family = YLeaf(YType.str, "controller-family")

                                        self.controller_type = YLeaf(YType.str, "controller-type")

                                        self.description = YLeaf(YType.str, "description")

                                        self.dev_num1 = YLeaf(YType.str, "dev-num1")

                                        self.dev_num2 = YLeaf(YType.str, "dev-num2")

                                        self.dev_num3 = YLeaf(YType.str, "dev-num3")

                                        self.dev_num4 = YLeaf(YType.str, "dev-num4")

                                        self.dev_num5 = YLeaf(YType.str, "dev-num5")

                                        self.dev_num6 = YLeaf(YType.str, "dev-num6")

                                        self.dev_num7 = YLeaf(YType.str, "dev-num7")

                                        self.eci = YLeaf(YType.str, "eci")

                                        self.eeprom_size = YLeaf(YType.str, "eeprom-size")

                                        self.engineer_use = YLeaf(YType.str, "engineer-use")

                                        self.fru_major_type = YLeaf(YType.str, "fru-major-type")

                                        self.fru_minor_type = YLeaf(YType.str, "fru-minor-type")

                                        self.hw_version = YLeaf(YType.str, "hw-version")

                                        self.hwid = YLeaf(YType.str, "hwid")

                                        self.idprom_format_rev = YLeaf(YType.str, "idprom-format-rev")

                                        self.mac_add_blk_size1 = YLeaf(YType.str, "mac-add-blk-size1")

                                        self.mac_add_blk_size2 = YLeaf(YType.str, "mac-add-blk-size2")

                                        self.mac_add_blk_size3 = YLeaf(YType.str, "mac-add-blk-size3")

                                        self.mac_add_blk_size4 = YLeaf(YType.str, "mac-add-blk-size4")

                                        self.manu_test_data = YLeaf(YType.str, "manu-test-data")

                                        self.mfg_bits = YLeaf(YType.str, "mfg-bits")

                                        self.mfg_deviation = YLeaf(YType.str, "mfg-deviation")

                                        self.oem_string = YLeaf(YType.str, "oem-string")

                                        self.part_number = YLeaf(YType.str, "part-number")

                                        self.part_revision = YLeaf(YType.str, "part-revision")

                                        self.pca_num = YLeaf(YType.str, "pca-num")

                                        self.pcavid = YLeaf(YType.str, "pcavid")

                                        self.pcb_serial_num = YLeaf(YType.str, "pcb-serial-num")

                                        self.pid = YLeaf(YType.str, "pid")

                                        self.power_consumption = YLeaf(YType.str, "power-consumption")

                                        self.power_supply_type = YLeaf(YType.str, "power-supply-type")

                                        self.product_id = YLeaf(YType.str, "product-id")

                                        self.rma_code = YLeaf(YType.str, "rma-code")

                                        self.serial_number = YLeaf(YType.str, "serial-number")

                                        self.snmpoid = YLeaf(YType.str, "snmpoid")

                                        self.top_assem_part_num = YLeaf(YType.str, "top-assem-part-num")

                                        self.top_assem_vid = YLeaf(YType.str, "top-assem-vid")

                                        self.udi_description = YLeaf(YType.str, "udi-description")

                                        self.udi_name = YLeaf(YType.str, "udi-name")

                                        self.vid = YLeaf(YType.str, "vid")

                                        self.rma = Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.CardInstance.Rma()
                                        self.rma.parent = self
                                        self._children_name_map["rma"] = "rma"
                                        self._children_yang_names.add("rma")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("asset_alias",
                                                        "asset_id",
                                                        "base_mac_address1",
                                                        "base_mac_address2",
                                                        "base_mac_address3",
                                                        "base_mac_address4",
                                                        "block_checksum",
                                                        "block_count",
                                                        "block_length",
                                                        "block_signature",
                                                        "block_version",
                                                        "chassis_sid",
                                                        "clei",
                                                        "controller_family",
                                                        "controller_type",
                                                        "description",
                                                        "dev_num1",
                                                        "dev_num2",
                                                        "dev_num3",
                                                        "dev_num4",
                                                        "dev_num5",
                                                        "dev_num6",
                                                        "dev_num7",
                                                        "eci",
                                                        "eeprom_size",
                                                        "engineer_use",
                                                        "fru_major_type",
                                                        "fru_minor_type",
                                                        "hw_version",
                                                        "hwid",
                                                        "idprom_format_rev",
                                                        "mac_add_blk_size1",
                                                        "mac_add_blk_size2",
                                                        "mac_add_blk_size3",
                                                        "mac_add_blk_size4",
                                                        "manu_test_data",
                                                        "mfg_bits",
                                                        "mfg_deviation",
                                                        "oem_string",
                                                        "part_number",
                                                        "part_revision",
                                                        "pca_num",
                                                        "pcavid",
                                                        "pcb_serial_num",
                                                        "pid",
                                                        "power_consumption",
                                                        "power_supply_type",
                                                        "product_id",
                                                        "rma_code",
                                                        "serial_number",
                                                        "snmpoid",
                                                        "top_assem_part_num",
                                                        "top_assem_vid",
                                                        "udi_description",
                                                        "udi_name",
                                                        "vid") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.CardInstance, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.CardInstance, self).__setattr__(name, value)


                                    class Rma(Entity):
                                        """
                                        RMA Data
                                        
                                        .. attribute:: rma_history
                                        
                                        	RMA history
                                        	**type**\:  str
                                        
                                        	**length:** 0..255
                                        
                                        .. attribute:: rma_number
                                        
                                        	RMA tracking number format is N\-N\-N
                                        	**type**\:  str
                                        
                                        	**length:** 0..255
                                        
                                        .. attribute:: test_history
                                        
                                        	Test history
                                        	**type**\:  str
                                        
                                        	**length:** 0..255
                                        
                                        

                                        """

                                        _prefix = 'sdr-invmgr-diag-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.CardInstance.Rma, self).__init__()

                                            self.yang_name = "rma"
                                            self.yang_parent_name = "card-instance"

                                            self.rma_history = YLeaf(YType.str, "rma-history")

                                            self.rma_number = YLeaf(YType.str, "rma-number")

                                            self.test_history = YLeaf(YType.str, "test-history")

                                        def __setattr__(self, name, value):
                                            self._check_monkey_patching_error(name, value)
                                            with _handle_type_error():
                                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                        "Please use list append or extend method."
                                                                        .format(value))
                                                if isinstance(value, Enum.YLeaf):
                                                    value = value.name
                                                if name in ("rma_history",
                                                            "rma_number",
                                                            "test_history") and name in self.__dict__:
                                                    if isinstance(value, YLeaf):
                                                        self.__dict__[name].set(value.get())
                                                    elif isinstance(value, YLeafList):
                                                        super(Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.CardInstance.Rma, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.CardInstance.Rma, self).__setattr__(name, value)

                                        def has_data(self):
                                            return (
                                                self.rma_history.is_set or
                                                self.rma_number.is_set or
                                                self.test_history.is_set)

                                        def has_operation(self):
                                            return (
                                                self.yfilter != YFilter.not_set or
                                                self.rma_history.yfilter != YFilter.not_set or
                                                self.rma_number.yfilter != YFilter.not_set or
                                                self.test_history.yfilter != YFilter.not_set)

                                        def get_segment_path(self):
                                            path_buffer = ""
                                            path_buffer = "rma" + path_buffer

                                            return path_buffer

                                        def get_entity_path(self, ancestor):
                                            path_buffer = ""
                                            if (ancestor is None):
                                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                            else:
                                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                            leaf_name_data = LeafDataList()
                                            if (self.rma_history.is_set or self.rma_history.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.rma_history.get_name_leafdata())
                                            if (self.rma_number.is_set or self.rma_number.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.rma_number.get_name_leafdata())
                                            if (self.test_history.is_set or self.test_history.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.test_history.get_name_leafdata())

                                            entity_path = EntityPath(path_buffer, leaf_name_data)
                                            return entity_path

                                        def get_child_by_name(self, child_yang_name, segment_path):
                                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                            if child is not None:
                                                return child

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "rma-history" or name == "rma-number" or name == "test-history"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            if(value_path == "rma-history"):
                                                self.rma_history = value
                                                self.rma_history.value_namespace = name_space
                                                self.rma_history.value_namespace_prefix = name_space_prefix
                                            if(value_path == "rma-number"):
                                                self.rma_number = value
                                                self.rma_number.value_namespace = name_space
                                                self.rma_number.value_namespace_prefix = name_space_prefix
                                            if(value_path == "test-history"):
                                                self.test_history = value
                                                self.test_history.value_namespace = name_space
                                                self.test_history.value_namespace_prefix = name_space_prefix

                                    def has_data(self):
                                        return (
                                            self.asset_alias.is_set or
                                            self.asset_id.is_set or
                                            self.base_mac_address1.is_set or
                                            self.base_mac_address2.is_set or
                                            self.base_mac_address3.is_set or
                                            self.base_mac_address4.is_set or
                                            self.block_checksum.is_set or
                                            self.block_count.is_set or
                                            self.block_length.is_set or
                                            self.block_signature.is_set or
                                            self.block_version.is_set or
                                            self.chassis_sid.is_set or
                                            self.clei.is_set or
                                            self.controller_family.is_set or
                                            self.controller_type.is_set or
                                            self.description.is_set or
                                            self.dev_num1.is_set or
                                            self.dev_num2.is_set or
                                            self.dev_num3.is_set or
                                            self.dev_num4.is_set or
                                            self.dev_num5.is_set or
                                            self.dev_num6.is_set or
                                            self.dev_num7.is_set or
                                            self.eci.is_set or
                                            self.eeprom_size.is_set or
                                            self.engineer_use.is_set or
                                            self.fru_major_type.is_set or
                                            self.fru_minor_type.is_set or
                                            self.hw_version.is_set or
                                            self.hwid.is_set or
                                            self.idprom_format_rev.is_set or
                                            self.mac_add_blk_size1.is_set or
                                            self.mac_add_blk_size2.is_set or
                                            self.mac_add_blk_size3.is_set or
                                            self.mac_add_blk_size4.is_set or
                                            self.manu_test_data.is_set or
                                            self.mfg_bits.is_set or
                                            self.mfg_deviation.is_set or
                                            self.oem_string.is_set or
                                            self.part_number.is_set or
                                            self.part_revision.is_set or
                                            self.pca_num.is_set or
                                            self.pcavid.is_set or
                                            self.pcb_serial_num.is_set or
                                            self.pid.is_set or
                                            self.power_consumption.is_set or
                                            self.power_supply_type.is_set or
                                            self.product_id.is_set or
                                            self.rma_code.is_set or
                                            self.serial_number.is_set or
                                            self.snmpoid.is_set or
                                            self.top_assem_part_num.is_set or
                                            self.top_assem_vid.is_set or
                                            self.udi_description.is_set or
                                            self.udi_name.is_set or
                                            self.vid.is_set or
                                            (self.rma is not None and self.rma.has_data()))

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.asset_alias.yfilter != YFilter.not_set or
                                            self.asset_id.yfilter != YFilter.not_set or
                                            self.base_mac_address1.yfilter != YFilter.not_set or
                                            self.base_mac_address2.yfilter != YFilter.not_set or
                                            self.base_mac_address3.yfilter != YFilter.not_set or
                                            self.base_mac_address4.yfilter != YFilter.not_set or
                                            self.block_checksum.yfilter != YFilter.not_set or
                                            self.block_count.yfilter != YFilter.not_set or
                                            self.block_length.yfilter != YFilter.not_set or
                                            self.block_signature.yfilter != YFilter.not_set or
                                            self.block_version.yfilter != YFilter.not_set or
                                            self.chassis_sid.yfilter != YFilter.not_set or
                                            self.clei.yfilter != YFilter.not_set or
                                            self.controller_family.yfilter != YFilter.not_set or
                                            self.controller_type.yfilter != YFilter.not_set or
                                            self.description.yfilter != YFilter.not_set or
                                            self.dev_num1.yfilter != YFilter.not_set or
                                            self.dev_num2.yfilter != YFilter.not_set or
                                            self.dev_num3.yfilter != YFilter.not_set or
                                            self.dev_num4.yfilter != YFilter.not_set or
                                            self.dev_num5.yfilter != YFilter.not_set or
                                            self.dev_num6.yfilter != YFilter.not_set or
                                            self.dev_num7.yfilter != YFilter.not_set or
                                            self.eci.yfilter != YFilter.not_set or
                                            self.eeprom_size.yfilter != YFilter.not_set or
                                            self.engineer_use.yfilter != YFilter.not_set or
                                            self.fru_major_type.yfilter != YFilter.not_set or
                                            self.fru_minor_type.yfilter != YFilter.not_set or
                                            self.hw_version.yfilter != YFilter.not_set or
                                            self.hwid.yfilter != YFilter.not_set or
                                            self.idprom_format_rev.yfilter != YFilter.not_set or
                                            self.mac_add_blk_size1.yfilter != YFilter.not_set or
                                            self.mac_add_blk_size2.yfilter != YFilter.not_set or
                                            self.mac_add_blk_size3.yfilter != YFilter.not_set or
                                            self.mac_add_blk_size4.yfilter != YFilter.not_set or
                                            self.manu_test_data.yfilter != YFilter.not_set or
                                            self.mfg_bits.yfilter != YFilter.not_set or
                                            self.mfg_deviation.yfilter != YFilter.not_set or
                                            self.oem_string.yfilter != YFilter.not_set or
                                            self.part_number.yfilter != YFilter.not_set or
                                            self.part_revision.yfilter != YFilter.not_set or
                                            self.pca_num.yfilter != YFilter.not_set or
                                            self.pcavid.yfilter != YFilter.not_set or
                                            self.pcb_serial_num.yfilter != YFilter.not_set or
                                            self.pid.yfilter != YFilter.not_set or
                                            self.power_consumption.yfilter != YFilter.not_set or
                                            self.power_supply_type.yfilter != YFilter.not_set or
                                            self.product_id.yfilter != YFilter.not_set or
                                            self.rma_code.yfilter != YFilter.not_set or
                                            self.serial_number.yfilter != YFilter.not_set or
                                            self.snmpoid.yfilter != YFilter.not_set or
                                            self.top_assem_part_num.yfilter != YFilter.not_set or
                                            self.top_assem_vid.yfilter != YFilter.not_set or
                                            self.udi_description.yfilter != YFilter.not_set or
                                            self.udi_name.yfilter != YFilter.not_set or
                                            self.vid.yfilter != YFilter.not_set or
                                            (self.rma is not None and self.rma.has_operation()))

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "card-instance" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.asset_alias.is_set or self.asset_alias.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.asset_alias.get_name_leafdata())
                                        if (self.asset_id.is_set or self.asset_id.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.asset_id.get_name_leafdata())
                                        if (self.base_mac_address1.is_set or self.base_mac_address1.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.base_mac_address1.get_name_leafdata())
                                        if (self.base_mac_address2.is_set or self.base_mac_address2.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.base_mac_address2.get_name_leafdata())
                                        if (self.base_mac_address3.is_set or self.base_mac_address3.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.base_mac_address3.get_name_leafdata())
                                        if (self.base_mac_address4.is_set or self.base_mac_address4.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.base_mac_address4.get_name_leafdata())
                                        if (self.block_checksum.is_set or self.block_checksum.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.block_checksum.get_name_leafdata())
                                        if (self.block_count.is_set or self.block_count.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.block_count.get_name_leafdata())
                                        if (self.block_length.is_set or self.block_length.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.block_length.get_name_leafdata())
                                        if (self.block_signature.is_set or self.block_signature.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.block_signature.get_name_leafdata())
                                        if (self.block_version.is_set or self.block_version.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.block_version.get_name_leafdata())
                                        if (self.chassis_sid.is_set or self.chassis_sid.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.chassis_sid.get_name_leafdata())
                                        if (self.clei.is_set or self.clei.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.clei.get_name_leafdata())
                                        if (self.controller_family.is_set or self.controller_family.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.controller_family.get_name_leafdata())
                                        if (self.controller_type.is_set or self.controller_type.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.controller_type.get_name_leafdata())
                                        if (self.description.is_set or self.description.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.description.get_name_leafdata())
                                        if (self.dev_num1.is_set or self.dev_num1.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.dev_num1.get_name_leafdata())
                                        if (self.dev_num2.is_set or self.dev_num2.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.dev_num2.get_name_leafdata())
                                        if (self.dev_num3.is_set or self.dev_num3.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.dev_num3.get_name_leafdata())
                                        if (self.dev_num4.is_set or self.dev_num4.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.dev_num4.get_name_leafdata())
                                        if (self.dev_num5.is_set or self.dev_num5.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.dev_num5.get_name_leafdata())
                                        if (self.dev_num6.is_set or self.dev_num6.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.dev_num6.get_name_leafdata())
                                        if (self.dev_num7.is_set or self.dev_num7.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.dev_num7.get_name_leafdata())
                                        if (self.eci.is_set or self.eci.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.eci.get_name_leafdata())
                                        if (self.eeprom_size.is_set or self.eeprom_size.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.eeprom_size.get_name_leafdata())
                                        if (self.engineer_use.is_set or self.engineer_use.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.engineer_use.get_name_leafdata())
                                        if (self.fru_major_type.is_set or self.fru_major_type.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.fru_major_type.get_name_leafdata())
                                        if (self.fru_minor_type.is_set or self.fru_minor_type.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.fru_minor_type.get_name_leafdata())
                                        if (self.hw_version.is_set or self.hw_version.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.hw_version.get_name_leafdata())
                                        if (self.hwid.is_set or self.hwid.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.hwid.get_name_leafdata())
                                        if (self.idprom_format_rev.is_set or self.idprom_format_rev.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.idprom_format_rev.get_name_leafdata())
                                        if (self.mac_add_blk_size1.is_set or self.mac_add_blk_size1.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.mac_add_blk_size1.get_name_leafdata())
                                        if (self.mac_add_blk_size2.is_set or self.mac_add_blk_size2.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.mac_add_blk_size2.get_name_leafdata())
                                        if (self.mac_add_blk_size3.is_set or self.mac_add_blk_size3.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.mac_add_blk_size3.get_name_leafdata())
                                        if (self.mac_add_blk_size4.is_set or self.mac_add_blk_size4.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.mac_add_blk_size4.get_name_leafdata())
                                        if (self.manu_test_data.is_set or self.manu_test_data.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.manu_test_data.get_name_leafdata())
                                        if (self.mfg_bits.is_set or self.mfg_bits.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.mfg_bits.get_name_leafdata())
                                        if (self.mfg_deviation.is_set or self.mfg_deviation.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.mfg_deviation.get_name_leafdata())
                                        if (self.oem_string.is_set or self.oem_string.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.oem_string.get_name_leafdata())
                                        if (self.part_number.is_set or self.part_number.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.part_number.get_name_leafdata())
                                        if (self.part_revision.is_set or self.part_revision.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.part_revision.get_name_leafdata())
                                        if (self.pca_num.is_set or self.pca_num.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.pca_num.get_name_leafdata())
                                        if (self.pcavid.is_set or self.pcavid.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.pcavid.get_name_leafdata())
                                        if (self.pcb_serial_num.is_set or self.pcb_serial_num.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.pcb_serial_num.get_name_leafdata())
                                        if (self.pid.is_set or self.pid.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.pid.get_name_leafdata())
                                        if (self.power_consumption.is_set or self.power_consumption.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.power_consumption.get_name_leafdata())
                                        if (self.power_supply_type.is_set or self.power_supply_type.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.power_supply_type.get_name_leafdata())
                                        if (self.product_id.is_set or self.product_id.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.product_id.get_name_leafdata())
                                        if (self.rma_code.is_set or self.rma_code.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.rma_code.get_name_leafdata())
                                        if (self.serial_number.is_set or self.serial_number.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.serial_number.get_name_leafdata())
                                        if (self.snmpoid.is_set or self.snmpoid.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.snmpoid.get_name_leafdata())
                                        if (self.top_assem_part_num.is_set or self.top_assem_part_num.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.top_assem_part_num.get_name_leafdata())
                                        if (self.top_assem_vid.is_set or self.top_assem_vid.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.top_assem_vid.get_name_leafdata())
                                        if (self.udi_description.is_set or self.udi_description.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.udi_description.get_name_leafdata())
                                        if (self.udi_name.is_set or self.udi_name.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.udi_name.get_name_leafdata())
                                        if (self.vid.is_set or self.vid.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.vid.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        if (child_yang_name == "rma"):
                                            if (self.rma is None):
                                                self.rma = Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.CardInstance.Rma()
                                                self.rma.parent = self
                                                self._children_name_map["rma"] = "rma"
                                            return self.rma

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "rma" or name == "asset-alias" or name == "asset-id" or name == "base-mac-address1" or name == "base-mac-address2" or name == "base-mac-address3" or name == "base-mac-address4" or name == "block-checksum" or name == "block-count" or name == "block-length" or name == "block-signature" or name == "block-version" or name == "chassis-sid" or name == "clei" or name == "controller-family" or name == "controller-type" or name == "description" or name == "dev-num1" or name == "dev-num2" or name == "dev-num3" or name == "dev-num4" or name == "dev-num5" or name == "dev-num6" or name == "dev-num7" or name == "eci" or name == "eeprom-size" or name == "engineer-use" or name == "fru-major-type" or name == "fru-minor-type" or name == "hw-version" or name == "hwid" or name == "idprom-format-rev" or name == "mac-add-blk-size1" or name == "mac-add-blk-size2" or name == "mac-add-blk-size3" or name == "mac-add-blk-size4" or name == "manu-test-data" or name == "mfg-bits" or name == "mfg-deviation" or name == "oem-string" or name == "part-number" or name == "part-revision" or name == "pca-num" or name == "pcavid" or name == "pcb-serial-num" or name == "pid" or name == "power-consumption" or name == "power-supply-type" or name == "product-id" or name == "rma-code" or name == "serial-number" or name == "snmpoid" or name == "top-assem-part-num" or name == "top-assem-vid" or name == "udi-description" or name == "udi-name" or name == "vid"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "asset-alias"):
                                            self.asset_alias = value
                                            self.asset_alias.value_namespace = name_space
                                            self.asset_alias.value_namespace_prefix = name_space_prefix
                                        if(value_path == "asset-id"):
                                            self.asset_id = value
                                            self.asset_id.value_namespace = name_space
                                            self.asset_id.value_namespace_prefix = name_space_prefix
                                        if(value_path == "base-mac-address1"):
                                            self.base_mac_address1 = value
                                            self.base_mac_address1.value_namespace = name_space
                                            self.base_mac_address1.value_namespace_prefix = name_space_prefix
                                        if(value_path == "base-mac-address2"):
                                            self.base_mac_address2 = value
                                            self.base_mac_address2.value_namespace = name_space
                                            self.base_mac_address2.value_namespace_prefix = name_space_prefix
                                        if(value_path == "base-mac-address3"):
                                            self.base_mac_address3 = value
                                            self.base_mac_address3.value_namespace = name_space
                                            self.base_mac_address3.value_namespace_prefix = name_space_prefix
                                        if(value_path == "base-mac-address4"):
                                            self.base_mac_address4 = value
                                            self.base_mac_address4.value_namespace = name_space
                                            self.base_mac_address4.value_namespace_prefix = name_space_prefix
                                        if(value_path == "block-checksum"):
                                            self.block_checksum = value
                                            self.block_checksum.value_namespace = name_space
                                            self.block_checksum.value_namespace_prefix = name_space_prefix
                                        if(value_path == "block-count"):
                                            self.block_count = value
                                            self.block_count.value_namespace = name_space
                                            self.block_count.value_namespace_prefix = name_space_prefix
                                        if(value_path == "block-length"):
                                            self.block_length = value
                                            self.block_length.value_namespace = name_space
                                            self.block_length.value_namespace_prefix = name_space_prefix
                                        if(value_path == "block-signature"):
                                            self.block_signature = value
                                            self.block_signature.value_namespace = name_space
                                            self.block_signature.value_namespace_prefix = name_space_prefix
                                        if(value_path == "block-version"):
                                            self.block_version = value
                                            self.block_version.value_namespace = name_space
                                            self.block_version.value_namespace_prefix = name_space_prefix
                                        if(value_path == "chassis-sid"):
                                            self.chassis_sid = value
                                            self.chassis_sid.value_namespace = name_space
                                            self.chassis_sid.value_namespace_prefix = name_space_prefix
                                        if(value_path == "clei"):
                                            self.clei = value
                                            self.clei.value_namespace = name_space
                                            self.clei.value_namespace_prefix = name_space_prefix
                                        if(value_path == "controller-family"):
                                            self.controller_family = value
                                            self.controller_family.value_namespace = name_space
                                            self.controller_family.value_namespace_prefix = name_space_prefix
                                        if(value_path == "controller-type"):
                                            self.controller_type = value
                                            self.controller_type.value_namespace = name_space
                                            self.controller_type.value_namespace_prefix = name_space_prefix
                                        if(value_path == "description"):
                                            self.description = value
                                            self.description.value_namespace = name_space
                                            self.description.value_namespace_prefix = name_space_prefix
                                        if(value_path == "dev-num1"):
                                            self.dev_num1 = value
                                            self.dev_num1.value_namespace = name_space
                                            self.dev_num1.value_namespace_prefix = name_space_prefix
                                        if(value_path == "dev-num2"):
                                            self.dev_num2 = value
                                            self.dev_num2.value_namespace = name_space
                                            self.dev_num2.value_namespace_prefix = name_space_prefix
                                        if(value_path == "dev-num3"):
                                            self.dev_num3 = value
                                            self.dev_num3.value_namespace = name_space
                                            self.dev_num3.value_namespace_prefix = name_space_prefix
                                        if(value_path == "dev-num4"):
                                            self.dev_num4 = value
                                            self.dev_num4.value_namespace = name_space
                                            self.dev_num4.value_namespace_prefix = name_space_prefix
                                        if(value_path == "dev-num5"):
                                            self.dev_num5 = value
                                            self.dev_num5.value_namespace = name_space
                                            self.dev_num5.value_namespace_prefix = name_space_prefix
                                        if(value_path == "dev-num6"):
                                            self.dev_num6 = value
                                            self.dev_num6.value_namespace = name_space
                                            self.dev_num6.value_namespace_prefix = name_space_prefix
                                        if(value_path == "dev-num7"):
                                            self.dev_num7 = value
                                            self.dev_num7.value_namespace = name_space
                                            self.dev_num7.value_namespace_prefix = name_space_prefix
                                        if(value_path == "eci"):
                                            self.eci = value
                                            self.eci.value_namespace = name_space
                                            self.eci.value_namespace_prefix = name_space_prefix
                                        if(value_path == "eeprom-size"):
                                            self.eeprom_size = value
                                            self.eeprom_size.value_namespace = name_space
                                            self.eeprom_size.value_namespace_prefix = name_space_prefix
                                        if(value_path == "engineer-use"):
                                            self.engineer_use = value
                                            self.engineer_use.value_namespace = name_space
                                            self.engineer_use.value_namespace_prefix = name_space_prefix
                                        if(value_path == "fru-major-type"):
                                            self.fru_major_type = value
                                            self.fru_major_type.value_namespace = name_space
                                            self.fru_major_type.value_namespace_prefix = name_space_prefix
                                        if(value_path == "fru-minor-type"):
                                            self.fru_minor_type = value
                                            self.fru_minor_type.value_namespace = name_space
                                            self.fru_minor_type.value_namespace_prefix = name_space_prefix
                                        if(value_path == "hw-version"):
                                            self.hw_version = value
                                            self.hw_version.value_namespace = name_space
                                            self.hw_version.value_namespace_prefix = name_space_prefix
                                        if(value_path == "hwid"):
                                            self.hwid = value
                                            self.hwid.value_namespace = name_space
                                            self.hwid.value_namespace_prefix = name_space_prefix
                                        if(value_path == "idprom-format-rev"):
                                            self.idprom_format_rev = value
                                            self.idprom_format_rev.value_namespace = name_space
                                            self.idprom_format_rev.value_namespace_prefix = name_space_prefix
                                        if(value_path == "mac-add-blk-size1"):
                                            self.mac_add_blk_size1 = value
                                            self.mac_add_blk_size1.value_namespace = name_space
                                            self.mac_add_blk_size1.value_namespace_prefix = name_space_prefix
                                        if(value_path == "mac-add-blk-size2"):
                                            self.mac_add_blk_size2 = value
                                            self.mac_add_blk_size2.value_namespace = name_space
                                            self.mac_add_blk_size2.value_namespace_prefix = name_space_prefix
                                        if(value_path == "mac-add-blk-size3"):
                                            self.mac_add_blk_size3 = value
                                            self.mac_add_blk_size3.value_namespace = name_space
                                            self.mac_add_blk_size3.value_namespace_prefix = name_space_prefix
                                        if(value_path == "mac-add-blk-size4"):
                                            self.mac_add_blk_size4 = value
                                            self.mac_add_blk_size4.value_namespace = name_space
                                            self.mac_add_blk_size4.value_namespace_prefix = name_space_prefix
                                        if(value_path == "manu-test-data"):
                                            self.manu_test_data = value
                                            self.manu_test_data.value_namespace = name_space
                                            self.manu_test_data.value_namespace_prefix = name_space_prefix
                                        if(value_path == "mfg-bits"):
                                            self.mfg_bits = value
                                            self.mfg_bits.value_namespace = name_space
                                            self.mfg_bits.value_namespace_prefix = name_space_prefix
                                        if(value_path == "mfg-deviation"):
                                            self.mfg_deviation = value
                                            self.mfg_deviation.value_namespace = name_space
                                            self.mfg_deviation.value_namespace_prefix = name_space_prefix
                                        if(value_path == "oem-string"):
                                            self.oem_string = value
                                            self.oem_string.value_namespace = name_space
                                            self.oem_string.value_namespace_prefix = name_space_prefix
                                        if(value_path == "part-number"):
                                            self.part_number = value
                                            self.part_number.value_namespace = name_space
                                            self.part_number.value_namespace_prefix = name_space_prefix
                                        if(value_path == "part-revision"):
                                            self.part_revision = value
                                            self.part_revision.value_namespace = name_space
                                            self.part_revision.value_namespace_prefix = name_space_prefix
                                        if(value_path == "pca-num"):
                                            self.pca_num = value
                                            self.pca_num.value_namespace = name_space
                                            self.pca_num.value_namespace_prefix = name_space_prefix
                                        if(value_path == "pcavid"):
                                            self.pcavid = value
                                            self.pcavid.value_namespace = name_space
                                            self.pcavid.value_namespace_prefix = name_space_prefix
                                        if(value_path == "pcb-serial-num"):
                                            self.pcb_serial_num = value
                                            self.pcb_serial_num.value_namespace = name_space
                                            self.pcb_serial_num.value_namespace_prefix = name_space_prefix
                                        if(value_path == "pid"):
                                            self.pid = value
                                            self.pid.value_namespace = name_space
                                            self.pid.value_namespace_prefix = name_space_prefix
                                        if(value_path == "power-consumption"):
                                            self.power_consumption = value
                                            self.power_consumption.value_namespace = name_space
                                            self.power_consumption.value_namespace_prefix = name_space_prefix
                                        if(value_path == "power-supply-type"):
                                            self.power_supply_type = value
                                            self.power_supply_type.value_namespace = name_space
                                            self.power_supply_type.value_namespace_prefix = name_space_prefix
                                        if(value_path == "product-id"):
                                            self.product_id = value
                                            self.product_id.value_namespace = name_space
                                            self.product_id.value_namespace_prefix = name_space_prefix
                                        if(value_path == "rma-code"):
                                            self.rma_code = value
                                            self.rma_code.value_namespace = name_space
                                            self.rma_code.value_namespace_prefix = name_space_prefix
                                        if(value_path == "serial-number"):
                                            self.serial_number = value
                                            self.serial_number.value_namespace = name_space
                                            self.serial_number.value_namespace_prefix = name_space_prefix
                                        if(value_path == "snmpoid"):
                                            self.snmpoid = value
                                            self.snmpoid.value_namespace = name_space
                                            self.snmpoid.value_namespace_prefix = name_space_prefix
                                        if(value_path == "top-assem-part-num"):
                                            self.top_assem_part_num = value
                                            self.top_assem_part_num.value_namespace = name_space
                                            self.top_assem_part_num.value_namespace_prefix = name_space_prefix
                                        if(value_path == "top-assem-vid"):
                                            self.top_assem_vid = value
                                            self.top_assem_vid.value_namespace = name_space
                                            self.top_assem_vid.value_namespace_prefix = name_space_prefix
                                        if(value_path == "udi-description"):
                                            self.udi_description = value
                                            self.udi_description.value_namespace = name_space
                                            self.udi_description.value_namespace_prefix = name_space_prefix
                                        if(value_path == "udi-name"):
                                            self.udi_name = value
                                            self.udi_name.value_namespace = name_space
                                            self.udi_name.value_namespace_prefix = name_space_prefix
                                        if(value_path == "vid"):
                                            self.vid = value
                                            self.vid.value_namespace = name_space
                                            self.vid.value_namespace_prefix = name_space_prefix

                                def has_data(self):
                                    return (
                                        self.node_operational_state.is_set or
                                        (self.card_instance is not None and self.card_instance.has_data()))

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.node_operational_state.yfilter != YFilter.not_set or
                                        (self.card_instance is not None and self.card_instance.has_operation()))

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "detail" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.node_operational_state.is_set or self.node_operational_state.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.node_operational_state.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    if (child_yang_name == "card-instance"):
                                        if (self.card_instance is None):
                                            self.card_instance = Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.CardInstance()
                                            self.card_instance.parent = self
                                            self._children_name_map["card_instance"] = "card-instance"
                                        return self.card_instance

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "card-instance" or name == "node-operational-state"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "node-operational-state"):
                                        self.node_operational_state = value
                                        self.node_operational_state.value_namespace = name_space
                                        self.node_operational_state.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                return (
                                    self.name.is_set or
                                    (self.detail is not None and self.detail.has_data()))

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.name.yfilter != YFilter.not_set or
                                    (self.detail is not None and self.detail.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "instance" + "[name='" + self.name.get() + "']" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.name.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                if (child_yang_name == "detail"):
                                    if (self.detail is None):
                                        self.detail = Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail()
                                        self.detail.parent = self
                                        self._children_name_map["detail"] = "detail"
                                    return self.detail

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "detail" or name == "name"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "name"):
                                    self.name = value
                                    self.name.value_namespace = name_space
                                    self.name.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.instance:
                                if (c.has_data()):
                                    return True
                            return False

                        def has_operation(self):
                            for c in self.instance:
                                if (c.has_operation()):
                                    return True
                            return self.yfilter != YFilter.not_set

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "instances" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "instance"):
                                for c in self.instance:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = Diag.Racks.Rack.Slots.Slot.Instances.Instance()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.instance.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "instance"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass

                    def has_data(self):
                        return (
                            self.slot_name.is_set or
                            (self.instances is not None and self.instances.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.slot_name.yfilter != YFilter.not_set or
                            (self.instances is not None and self.instances.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "slot" + "[slot-name='" + self.slot_name.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.slot_name.is_set or self.slot_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.slot_name.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "instances"):
                            if (self.instances is None):
                                self.instances = Diag.Racks.Rack.Slots.Slot.Instances()
                                self.instances.parent = self
                                self._children_name_map["instances"] = "instances"
                            return self.instances

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "instances" or name == "slot-name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "slot-name"):
                            self.slot_name = value
                            self.slot_name.value_namespace = name_space
                            self.slot_name.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.slot:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.slot:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "slots" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "slot"):
                        for c in self.slot:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Diag.Racks.Rack.Slots.Slot()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.slot.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "slot"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class Chassis(Entity):
                """
                Chassis information
                
                .. attribute:: asset_alias
                
                	Asset Alias
                	**type**\:  str
                
                	**length:** 0..255
                
                .. attribute:: asset_id
                
                	Asset ID
                	**type**\:  str
                
                	**length:** 0..255
                
                .. attribute:: base_mac_address1
                
                	Base Mac Address #1
                	**type**\:  str
                
                	**length:** 0..255
                
                .. attribute:: base_mac_address2
                
                	Base Mac Address #2
                	**type**\:  str
                
                	**length:** 0..255
                
                .. attribute:: base_mac_address3
                
                	Base Mac Address #3
                	**type**\:  str
                
                	**length:** 0..255
                
                .. attribute:: base_mac_address4
                
                	Base Mac Address #4
                	**type**\:  str
                
                	**length:** 0..255
                
                .. attribute:: block_checksum
                
                	Block Checksum
                	**type**\:  str
                
                	**length:** 0..255
                
                .. attribute:: block_count
                
                	Block Count
                	**type**\:  str
                
                	**length:** 0..255
                
                .. attribute:: block_length
                
                	Block Length
                	**type**\:  str
                
                	**length:** 0..255
                
                .. attribute:: block_signature
                
                	Block Signature
                	**type**\:  str
                
                	**length:** 0..255
                
                .. attribute:: block_version
                
                	Block Version
                	**type**\:  str
                
                	**length:** 0..255
                
                .. attribute:: chassis_sid
                
                	Chassis serial number
                	**type**\:  str
                
                	**length:** 0..255
                
                .. attribute:: clei
                
                	Common Language Equipment Identifier (CLEI) code
                	**type**\:  str
                
                	**length:** 0..255
                
                .. attribute:: controller_family
                
                	Controller family
                	**type**\:  str
                
                	**length:** 0..255
                
                .. attribute:: controller_type
                
                	Controller type
                	**type**\:  str
                
                	**length:** 0..255
                
                .. attribute:: description
                
                	A textual description of physical entity
                	**type**\:  str
                
                	**length:** 0..255
                
                .. attribute:: dev_num1
                
                	Deviation Number # 1
                	**type**\:  str
                
                	**length:** 0..255
                
                .. attribute:: dev_num2
                
                	Deviation Number # 2
                	**type**\:  str
                
                	**length:** 0..255
                
                .. attribute:: dev_num3
                
                	Deviation Number # 3
                	**type**\:  str
                
                	**length:** 0..255
                
                .. attribute:: dev_num4
                
                	Deviation Number # 4
                	**type**\:  str
                
                	**length:** 0..255
                
                .. attribute:: dev_num5
                
                	Deviation Number # 5
                	**type**\:  str
                
                	**length:** 0..255
                
                .. attribute:: dev_num6
                
                	Deviation Number # 6
                	**type**\:  str
                
                	**length:** 0..255
                
                .. attribute:: dev_num7
                
                	Deviation Number # 7
                	**type**\:  str
                
                	**length:** 0..255
                
                .. attribute:: eci
                
                	Equipment Catalog Item (ECI) number
                	**type**\:  str
                
                	**length:** 0..255
                
                .. attribute:: eeprom_size
                
                	EEPROM Size
                	**type**\:  str
                
                	**length:** 0..255
                
                .. attribute:: engineer_use
                
                	Engineer Use
                	**type**\:  str
                
                	**length:** 0..255
                
                .. attribute:: fru_major_type
                
                	FRU Major Type
                	**type**\:  str
                
                	**length:** 0..255
                
                .. attribute:: fru_minor_type
                
                	FRU Minor Type
                	**type**\:  str
                
                	**length:** 0..255
                
                .. attribute:: hw_version
                
                	Hardware Version
                	**type**\:  str
                
                	**length:** 0..255
                
                .. attribute:: hwid
                
                	Hardware Revision
                	**type**\:  str
                
                	**length:** 0..255
                
                .. attribute:: idprom_format_rev
                
                	IDPROM Format Revision
                	**type**\:  str
                
                	**length:** 0..255
                
                .. attribute:: mac_add_blk_size1
                
                	Mac Address Block Size #1
                	**type**\:  str
                
                	**length:** 0..255
                
                .. attribute:: mac_add_blk_size2
                
                	Mac Address Block Size #2
                	**type**\:  str
                
                	**length:** 0..255
                
                .. attribute:: mac_add_blk_size3
                
                	Mac Address Block Size #3
                	**type**\:  str
                
                	**length:** 0..255
                
                .. attribute:: mac_add_blk_size4
                
                	Mac Address Block Size #4
                	**type**\:  str
                
                	**length:** 0..255
                
                .. attribute:: manu_test_data
                
                	Manufacturing Test Data
                	**type**\:  str
                
                	**length:** 0..255
                
                .. attribute:: mfg_bits
                
                	MFG Bits
                	**type**\:  str
                
                	**length:** 0..255
                
                .. attribute:: mfg_deviation
                
                	MFG Deviation
                	**type**\:  str
                
                	**length:** 0..255
                
                .. attribute:: oem_string
                
                	OEM String
                	**type**\:  str
                
                	**length:** 0..255
                
                .. attribute:: part_number
                
                	Part Number
                	**type**\:  str
                
                	**length:** 0..255
                
                .. attribute:: part_revision
                
                	Part Revision
                	**type**\:  str
                
                	**length:** 0..255
                
                .. attribute:: pca_num
                
                	PCA number
                	**type**\:  str
                
                	**length:** 0..255
                
                .. attribute:: pcavid
                
                	PCA revision ID
                	**type**\:  str
                
                	**length:** 0..255
                
                .. attribute:: pcb_serial_num
                
                	PCB Serial Number
                	**type**\:  str
                
                	**length:** 0..255
                
                .. attribute:: pid
                
                	Product ID
                	**type**\:  str
                
                	**length:** 0..255
                
                .. attribute:: power_consumption
                
                	Power Consumption
                	**type**\:  str
                
                	**length:** 0..255
                
                .. attribute:: power_supply_type
                
                	Power Supply Type
                	**type**\:  str
                
                	**length:** 0..255
                
                .. attribute:: product_id
                
                	Product ID
                	**type**\:  str
                
                	**length:** 0..255
                
                .. attribute:: rma
                
                	RMA Data
                	**type**\:   :py:class:`Rma <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sdr_invmgr_diag_oper.Diag.Racks.Rack.Chassis.Rma>`
                
                .. attribute:: rma_code
                
                	RMA Code
                	**type**\:  str
                
                	**length:** 0..255
                
                .. attribute:: serial_number
                
                	Serial Number
                	**type**\:  str
                
                	**length:** 0..255
                
                .. attribute:: snmpoid
                
                	SNMP OID
                	**type**\:  str
                
                	**length:** 0..255
                
                .. attribute:: top_assem_part_num
                
                	Top assembly part number
                	**type**\:  str
                
                	**length:** 0..255
                
                .. attribute:: top_assem_vid
                
                	Top assembly revision number
                	**type**\:  str
                
                	**length:** 0..255
                
                .. attribute:: udi_description
                
                	UDI description
                	**type**\:  str
                
                	**length:** 0..255
                
                .. attribute:: udi_name
                
                	UDI name
                	**type**\:  str
                
                	**length:** 0..255
                
                .. attribute:: vid
                
                	Version ID
                	**type**\:  str
                
                	**length:** 0..255
                
                

                """

                _prefix = 'sdr-invmgr-diag-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Diag.Racks.Rack.Chassis, self).__init__()

                    self.yang_name = "chassis"
                    self.yang_parent_name = "rack"

                    self.asset_alias = YLeaf(YType.str, "asset-alias")

                    self.asset_id = YLeaf(YType.str, "asset-id")

                    self.base_mac_address1 = YLeaf(YType.str, "base-mac-address1")

                    self.base_mac_address2 = YLeaf(YType.str, "base-mac-address2")

                    self.base_mac_address3 = YLeaf(YType.str, "base-mac-address3")

                    self.base_mac_address4 = YLeaf(YType.str, "base-mac-address4")

                    self.block_checksum = YLeaf(YType.str, "block-checksum")

                    self.block_count = YLeaf(YType.str, "block-count")

                    self.block_length = YLeaf(YType.str, "block-length")

                    self.block_signature = YLeaf(YType.str, "block-signature")

                    self.block_version = YLeaf(YType.str, "block-version")

                    self.chassis_sid = YLeaf(YType.str, "chassis-sid")

                    self.clei = YLeaf(YType.str, "clei")

                    self.controller_family = YLeaf(YType.str, "controller-family")

                    self.controller_type = YLeaf(YType.str, "controller-type")

                    self.description = YLeaf(YType.str, "description")

                    self.dev_num1 = YLeaf(YType.str, "dev-num1")

                    self.dev_num2 = YLeaf(YType.str, "dev-num2")

                    self.dev_num3 = YLeaf(YType.str, "dev-num3")

                    self.dev_num4 = YLeaf(YType.str, "dev-num4")

                    self.dev_num5 = YLeaf(YType.str, "dev-num5")

                    self.dev_num6 = YLeaf(YType.str, "dev-num6")

                    self.dev_num7 = YLeaf(YType.str, "dev-num7")

                    self.eci = YLeaf(YType.str, "eci")

                    self.eeprom_size = YLeaf(YType.str, "eeprom-size")

                    self.engineer_use = YLeaf(YType.str, "engineer-use")

                    self.fru_major_type = YLeaf(YType.str, "fru-major-type")

                    self.fru_minor_type = YLeaf(YType.str, "fru-minor-type")

                    self.hw_version = YLeaf(YType.str, "hw-version")

                    self.hwid = YLeaf(YType.str, "hwid")

                    self.idprom_format_rev = YLeaf(YType.str, "idprom-format-rev")

                    self.mac_add_blk_size1 = YLeaf(YType.str, "mac-add-blk-size1")

                    self.mac_add_blk_size2 = YLeaf(YType.str, "mac-add-blk-size2")

                    self.mac_add_blk_size3 = YLeaf(YType.str, "mac-add-blk-size3")

                    self.mac_add_blk_size4 = YLeaf(YType.str, "mac-add-blk-size4")

                    self.manu_test_data = YLeaf(YType.str, "manu-test-data")

                    self.mfg_bits = YLeaf(YType.str, "mfg-bits")

                    self.mfg_deviation = YLeaf(YType.str, "mfg-deviation")

                    self.oem_string = YLeaf(YType.str, "oem-string")

                    self.part_number = YLeaf(YType.str, "part-number")

                    self.part_revision = YLeaf(YType.str, "part-revision")

                    self.pca_num = YLeaf(YType.str, "pca-num")

                    self.pcavid = YLeaf(YType.str, "pcavid")

                    self.pcb_serial_num = YLeaf(YType.str, "pcb-serial-num")

                    self.pid = YLeaf(YType.str, "pid")

                    self.power_consumption = YLeaf(YType.str, "power-consumption")

                    self.power_supply_type = YLeaf(YType.str, "power-supply-type")

                    self.product_id = YLeaf(YType.str, "product-id")

                    self.rma_code = YLeaf(YType.str, "rma-code")

                    self.serial_number = YLeaf(YType.str, "serial-number")

                    self.snmpoid = YLeaf(YType.str, "snmpoid")

                    self.top_assem_part_num = YLeaf(YType.str, "top-assem-part-num")

                    self.top_assem_vid = YLeaf(YType.str, "top-assem-vid")

                    self.udi_description = YLeaf(YType.str, "udi-description")

                    self.udi_name = YLeaf(YType.str, "udi-name")

                    self.vid = YLeaf(YType.str, "vid")

                    self.rma = Diag.Racks.Rack.Chassis.Rma()
                    self.rma.parent = self
                    self._children_name_map["rma"] = "rma"
                    self._children_yang_names.add("rma")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("asset_alias",
                                    "asset_id",
                                    "base_mac_address1",
                                    "base_mac_address2",
                                    "base_mac_address3",
                                    "base_mac_address4",
                                    "block_checksum",
                                    "block_count",
                                    "block_length",
                                    "block_signature",
                                    "block_version",
                                    "chassis_sid",
                                    "clei",
                                    "controller_family",
                                    "controller_type",
                                    "description",
                                    "dev_num1",
                                    "dev_num2",
                                    "dev_num3",
                                    "dev_num4",
                                    "dev_num5",
                                    "dev_num6",
                                    "dev_num7",
                                    "eci",
                                    "eeprom_size",
                                    "engineer_use",
                                    "fru_major_type",
                                    "fru_minor_type",
                                    "hw_version",
                                    "hwid",
                                    "idprom_format_rev",
                                    "mac_add_blk_size1",
                                    "mac_add_blk_size2",
                                    "mac_add_blk_size3",
                                    "mac_add_blk_size4",
                                    "manu_test_data",
                                    "mfg_bits",
                                    "mfg_deviation",
                                    "oem_string",
                                    "part_number",
                                    "part_revision",
                                    "pca_num",
                                    "pcavid",
                                    "pcb_serial_num",
                                    "pid",
                                    "power_consumption",
                                    "power_supply_type",
                                    "product_id",
                                    "rma_code",
                                    "serial_number",
                                    "snmpoid",
                                    "top_assem_part_num",
                                    "top_assem_vid",
                                    "udi_description",
                                    "udi_name",
                                    "vid") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Diag.Racks.Rack.Chassis, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Diag.Racks.Rack.Chassis, self).__setattr__(name, value)


                class Rma(Entity):
                    """
                    RMA Data
                    
                    .. attribute:: rma_history
                    
                    	RMA history
                    	**type**\:  str
                    
                    	**length:** 0..255
                    
                    .. attribute:: rma_number
                    
                    	RMA tracking number format is N\-N\-N
                    	**type**\:  str
                    
                    	**length:** 0..255
                    
                    .. attribute:: test_history
                    
                    	Test history
                    	**type**\:  str
                    
                    	**length:** 0..255
                    
                    

                    """

                    _prefix = 'sdr-invmgr-diag-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Diag.Racks.Rack.Chassis.Rma, self).__init__()

                        self.yang_name = "rma"
                        self.yang_parent_name = "chassis"

                        self.rma_history = YLeaf(YType.str, "rma-history")

                        self.rma_number = YLeaf(YType.str, "rma-number")

                        self.test_history = YLeaf(YType.str, "test-history")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("rma_history",
                                        "rma_number",
                                        "test_history") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Diag.Racks.Rack.Chassis.Rma, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Diag.Racks.Rack.Chassis.Rma, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.rma_history.is_set or
                            self.rma_number.is_set or
                            self.test_history.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.rma_history.yfilter != YFilter.not_set or
                            self.rma_number.yfilter != YFilter.not_set or
                            self.test_history.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "rma" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.rma_history.is_set or self.rma_history.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.rma_history.get_name_leafdata())
                        if (self.rma_number.is_set or self.rma_number.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.rma_number.get_name_leafdata())
                        if (self.test_history.is_set or self.test_history.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.test_history.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "rma-history" or name == "rma-number" or name == "test-history"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "rma-history"):
                            self.rma_history = value
                            self.rma_history.value_namespace = name_space
                            self.rma_history.value_namespace_prefix = name_space_prefix
                        if(value_path == "rma-number"):
                            self.rma_number = value
                            self.rma_number.value_namespace = name_space
                            self.rma_number.value_namespace_prefix = name_space_prefix
                        if(value_path == "test-history"):
                            self.test_history = value
                            self.test_history.value_namespace = name_space
                            self.test_history.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        self.asset_alias.is_set or
                        self.asset_id.is_set or
                        self.base_mac_address1.is_set or
                        self.base_mac_address2.is_set or
                        self.base_mac_address3.is_set or
                        self.base_mac_address4.is_set or
                        self.block_checksum.is_set or
                        self.block_count.is_set or
                        self.block_length.is_set or
                        self.block_signature.is_set or
                        self.block_version.is_set or
                        self.chassis_sid.is_set or
                        self.clei.is_set or
                        self.controller_family.is_set or
                        self.controller_type.is_set or
                        self.description.is_set or
                        self.dev_num1.is_set or
                        self.dev_num2.is_set or
                        self.dev_num3.is_set or
                        self.dev_num4.is_set or
                        self.dev_num5.is_set or
                        self.dev_num6.is_set or
                        self.dev_num7.is_set or
                        self.eci.is_set or
                        self.eeprom_size.is_set or
                        self.engineer_use.is_set or
                        self.fru_major_type.is_set or
                        self.fru_minor_type.is_set or
                        self.hw_version.is_set or
                        self.hwid.is_set or
                        self.idprom_format_rev.is_set or
                        self.mac_add_blk_size1.is_set or
                        self.mac_add_blk_size2.is_set or
                        self.mac_add_blk_size3.is_set or
                        self.mac_add_blk_size4.is_set or
                        self.manu_test_data.is_set or
                        self.mfg_bits.is_set or
                        self.mfg_deviation.is_set or
                        self.oem_string.is_set or
                        self.part_number.is_set or
                        self.part_revision.is_set or
                        self.pca_num.is_set or
                        self.pcavid.is_set or
                        self.pcb_serial_num.is_set or
                        self.pid.is_set or
                        self.power_consumption.is_set or
                        self.power_supply_type.is_set or
                        self.product_id.is_set or
                        self.rma_code.is_set or
                        self.serial_number.is_set or
                        self.snmpoid.is_set or
                        self.top_assem_part_num.is_set or
                        self.top_assem_vid.is_set or
                        self.udi_description.is_set or
                        self.udi_name.is_set or
                        self.vid.is_set or
                        (self.rma is not None and self.rma.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.asset_alias.yfilter != YFilter.not_set or
                        self.asset_id.yfilter != YFilter.not_set or
                        self.base_mac_address1.yfilter != YFilter.not_set or
                        self.base_mac_address2.yfilter != YFilter.not_set or
                        self.base_mac_address3.yfilter != YFilter.not_set or
                        self.base_mac_address4.yfilter != YFilter.not_set or
                        self.block_checksum.yfilter != YFilter.not_set or
                        self.block_count.yfilter != YFilter.not_set or
                        self.block_length.yfilter != YFilter.not_set or
                        self.block_signature.yfilter != YFilter.not_set or
                        self.block_version.yfilter != YFilter.not_set or
                        self.chassis_sid.yfilter != YFilter.not_set or
                        self.clei.yfilter != YFilter.not_set or
                        self.controller_family.yfilter != YFilter.not_set or
                        self.controller_type.yfilter != YFilter.not_set or
                        self.description.yfilter != YFilter.not_set or
                        self.dev_num1.yfilter != YFilter.not_set or
                        self.dev_num2.yfilter != YFilter.not_set or
                        self.dev_num3.yfilter != YFilter.not_set or
                        self.dev_num4.yfilter != YFilter.not_set or
                        self.dev_num5.yfilter != YFilter.not_set or
                        self.dev_num6.yfilter != YFilter.not_set or
                        self.dev_num7.yfilter != YFilter.not_set or
                        self.eci.yfilter != YFilter.not_set or
                        self.eeprom_size.yfilter != YFilter.not_set or
                        self.engineer_use.yfilter != YFilter.not_set or
                        self.fru_major_type.yfilter != YFilter.not_set or
                        self.fru_minor_type.yfilter != YFilter.not_set or
                        self.hw_version.yfilter != YFilter.not_set or
                        self.hwid.yfilter != YFilter.not_set or
                        self.idprom_format_rev.yfilter != YFilter.not_set or
                        self.mac_add_blk_size1.yfilter != YFilter.not_set or
                        self.mac_add_blk_size2.yfilter != YFilter.not_set or
                        self.mac_add_blk_size3.yfilter != YFilter.not_set or
                        self.mac_add_blk_size4.yfilter != YFilter.not_set or
                        self.manu_test_data.yfilter != YFilter.not_set or
                        self.mfg_bits.yfilter != YFilter.not_set or
                        self.mfg_deviation.yfilter != YFilter.not_set or
                        self.oem_string.yfilter != YFilter.not_set or
                        self.part_number.yfilter != YFilter.not_set or
                        self.part_revision.yfilter != YFilter.not_set or
                        self.pca_num.yfilter != YFilter.not_set or
                        self.pcavid.yfilter != YFilter.not_set or
                        self.pcb_serial_num.yfilter != YFilter.not_set or
                        self.pid.yfilter != YFilter.not_set or
                        self.power_consumption.yfilter != YFilter.not_set or
                        self.power_supply_type.yfilter != YFilter.not_set or
                        self.product_id.yfilter != YFilter.not_set or
                        self.rma_code.yfilter != YFilter.not_set or
                        self.serial_number.yfilter != YFilter.not_set or
                        self.snmpoid.yfilter != YFilter.not_set or
                        self.top_assem_part_num.yfilter != YFilter.not_set or
                        self.top_assem_vid.yfilter != YFilter.not_set or
                        self.udi_description.yfilter != YFilter.not_set or
                        self.udi_name.yfilter != YFilter.not_set or
                        self.vid.yfilter != YFilter.not_set or
                        (self.rma is not None and self.rma.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "chassis" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.asset_alias.is_set or self.asset_alias.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.asset_alias.get_name_leafdata())
                    if (self.asset_id.is_set or self.asset_id.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.asset_id.get_name_leafdata())
                    if (self.base_mac_address1.is_set or self.base_mac_address1.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.base_mac_address1.get_name_leafdata())
                    if (self.base_mac_address2.is_set or self.base_mac_address2.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.base_mac_address2.get_name_leafdata())
                    if (self.base_mac_address3.is_set or self.base_mac_address3.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.base_mac_address3.get_name_leafdata())
                    if (self.base_mac_address4.is_set or self.base_mac_address4.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.base_mac_address4.get_name_leafdata())
                    if (self.block_checksum.is_set or self.block_checksum.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.block_checksum.get_name_leafdata())
                    if (self.block_count.is_set or self.block_count.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.block_count.get_name_leafdata())
                    if (self.block_length.is_set or self.block_length.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.block_length.get_name_leafdata())
                    if (self.block_signature.is_set or self.block_signature.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.block_signature.get_name_leafdata())
                    if (self.block_version.is_set or self.block_version.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.block_version.get_name_leafdata())
                    if (self.chassis_sid.is_set or self.chassis_sid.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.chassis_sid.get_name_leafdata())
                    if (self.clei.is_set or self.clei.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.clei.get_name_leafdata())
                    if (self.controller_family.is_set or self.controller_family.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.controller_family.get_name_leafdata())
                    if (self.controller_type.is_set or self.controller_type.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.controller_type.get_name_leafdata())
                    if (self.description.is_set or self.description.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.description.get_name_leafdata())
                    if (self.dev_num1.is_set or self.dev_num1.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.dev_num1.get_name_leafdata())
                    if (self.dev_num2.is_set or self.dev_num2.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.dev_num2.get_name_leafdata())
                    if (self.dev_num3.is_set or self.dev_num3.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.dev_num3.get_name_leafdata())
                    if (self.dev_num4.is_set or self.dev_num4.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.dev_num4.get_name_leafdata())
                    if (self.dev_num5.is_set or self.dev_num5.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.dev_num5.get_name_leafdata())
                    if (self.dev_num6.is_set or self.dev_num6.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.dev_num6.get_name_leafdata())
                    if (self.dev_num7.is_set or self.dev_num7.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.dev_num7.get_name_leafdata())
                    if (self.eci.is_set or self.eci.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.eci.get_name_leafdata())
                    if (self.eeprom_size.is_set or self.eeprom_size.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.eeprom_size.get_name_leafdata())
                    if (self.engineer_use.is_set or self.engineer_use.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.engineer_use.get_name_leafdata())
                    if (self.fru_major_type.is_set or self.fru_major_type.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.fru_major_type.get_name_leafdata())
                    if (self.fru_minor_type.is_set or self.fru_minor_type.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.fru_minor_type.get_name_leafdata())
                    if (self.hw_version.is_set or self.hw_version.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.hw_version.get_name_leafdata())
                    if (self.hwid.is_set or self.hwid.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.hwid.get_name_leafdata())
                    if (self.idprom_format_rev.is_set or self.idprom_format_rev.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.idprom_format_rev.get_name_leafdata())
                    if (self.mac_add_blk_size1.is_set or self.mac_add_blk_size1.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.mac_add_blk_size1.get_name_leafdata())
                    if (self.mac_add_blk_size2.is_set or self.mac_add_blk_size2.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.mac_add_blk_size2.get_name_leafdata())
                    if (self.mac_add_blk_size3.is_set or self.mac_add_blk_size3.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.mac_add_blk_size3.get_name_leafdata())
                    if (self.mac_add_blk_size4.is_set or self.mac_add_blk_size4.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.mac_add_blk_size4.get_name_leafdata())
                    if (self.manu_test_data.is_set or self.manu_test_data.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.manu_test_data.get_name_leafdata())
                    if (self.mfg_bits.is_set or self.mfg_bits.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.mfg_bits.get_name_leafdata())
                    if (self.mfg_deviation.is_set or self.mfg_deviation.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.mfg_deviation.get_name_leafdata())
                    if (self.oem_string.is_set or self.oem_string.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.oem_string.get_name_leafdata())
                    if (self.part_number.is_set or self.part_number.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.part_number.get_name_leafdata())
                    if (self.part_revision.is_set or self.part_revision.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.part_revision.get_name_leafdata())
                    if (self.pca_num.is_set or self.pca_num.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.pca_num.get_name_leafdata())
                    if (self.pcavid.is_set or self.pcavid.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.pcavid.get_name_leafdata())
                    if (self.pcb_serial_num.is_set or self.pcb_serial_num.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.pcb_serial_num.get_name_leafdata())
                    if (self.pid.is_set or self.pid.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.pid.get_name_leafdata())
                    if (self.power_consumption.is_set or self.power_consumption.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.power_consumption.get_name_leafdata())
                    if (self.power_supply_type.is_set or self.power_supply_type.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.power_supply_type.get_name_leafdata())
                    if (self.product_id.is_set or self.product_id.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.product_id.get_name_leafdata())
                    if (self.rma_code.is_set or self.rma_code.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.rma_code.get_name_leafdata())
                    if (self.serial_number.is_set or self.serial_number.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.serial_number.get_name_leafdata())
                    if (self.snmpoid.is_set or self.snmpoid.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.snmpoid.get_name_leafdata())
                    if (self.top_assem_part_num.is_set or self.top_assem_part_num.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.top_assem_part_num.get_name_leafdata())
                    if (self.top_assem_vid.is_set or self.top_assem_vid.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.top_assem_vid.get_name_leafdata())
                    if (self.udi_description.is_set or self.udi_description.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.udi_description.get_name_leafdata())
                    if (self.udi_name.is_set or self.udi_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.udi_name.get_name_leafdata())
                    if (self.vid.is_set or self.vid.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.vid.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "rma"):
                        if (self.rma is None):
                            self.rma = Diag.Racks.Rack.Chassis.Rma()
                            self.rma.parent = self
                            self._children_name_map["rma"] = "rma"
                        return self.rma

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "rma" or name == "asset-alias" or name == "asset-id" or name == "base-mac-address1" or name == "base-mac-address2" or name == "base-mac-address3" or name == "base-mac-address4" or name == "block-checksum" or name == "block-count" or name == "block-length" or name == "block-signature" or name == "block-version" or name == "chassis-sid" or name == "clei" or name == "controller-family" or name == "controller-type" or name == "description" or name == "dev-num1" or name == "dev-num2" or name == "dev-num3" or name == "dev-num4" or name == "dev-num5" or name == "dev-num6" or name == "dev-num7" or name == "eci" or name == "eeprom-size" or name == "engineer-use" or name == "fru-major-type" or name == "fru-minor-type" or name == "hw-version" or name == "hwid" or name == "idprom-format-rev" or name == "mac-add-blk-size1" or name == "mac-add-blk-size2" or name == "mac-add-blk-size3" or name == "mac-add-blk-size4" or name == "manu-test-data" or name == "mfg-bits" or name == "mfg-deviation" or name == "oem-string" or name == "part-number" or name == "part-revision" or name == "pca-num" or name == "pcavid" or name == "pcb-serial-num" or name == "pid" or name == "power-consumption" or name == "power-supply-type" or name == "product-id" or name == "rma-code" or name == "serial-number" or name == "snmpoid" or name == "top-assem-part-num" or name == "top-assem-vid" or name == "udi-description" or name == "udi-name" or name == "vid"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "asset-alias"):
                        self.asset_alias = value
                        self.asset_alias.value_namespace = name_space
                        self.asset_alias.value_namespace_prefix = name_space_prefix
                    if(value_path == "asset-id"):
                        self.asset_id = value
                        self.asset_id.value_namespace = name_space
                        self.asset_id.value_namespace_prefix = name_space_prefix
                    if(value_path == "base-mac-address1"):
                        self.base_mac_address1 = value
                        self.base_mac_address1.value_namespace = name_space
                        self.base_mac_address1.value_namespace_prefix = name_space_prefix
                    if(value_path == "base-mac-address2"):
                        self.base_mac_address2 = value
                        self.base_mac_address2.value_namespace = name_space
                        self.base_mac_address2.value_namespace_prefix = name_space_prefix
                    if(value_path == "base-mac-address3"):
                        self.base_mac_address3 = value
                        self.base_mac_address3.value_namespace = name_space
                        self.base_mac_address3.value_namespace_prefix = name_space_prefix
                    if(value_path == "base-mac-address4"):
                        self.base_mac_address4 = value
                        self.base_mac_address4.value_namespace = name_space
                        self.base_mac_address4.value_namespace_prefix = name_space_prefix
                    if(value_path == "block-checksum"):
                        self.block_checksum = value
                        self.block_checksum.value_namespace = name_space
                        self.block_checksum.value_namespace_prefix = name_space_prefix
                    if(value_path == "block-count"):
                        self.block_count = value
                        self.block_count.value_namespace = name_space
                        self.block_count.value_namespace_prefix = name_space_prefix
                    if(value_path == "block-length"):
                        self.block_length = value
                        self.block_length.value_namespace = name_space
                        self.block_length.value_namespace_prefix = name_space_prefix
                    if(value_path == "block-signature"):
                        self.block_signature = value
                        self.block_signature.value_namespace = name_space
                        self.block_signature.value_namespace_prefix = name_space_prefix
                    if(value_path == "block-version"):
                        self.block_version = value
                        self.block_version.value_namespace = name_space
                        self.block_version.value_namespace_prefix = name_space_prefix
                    if(value_path == "chassis-sid"):
                        self.chassis_sid = value
                        self.chassis_sid.value_namespace = name_space
                        self.chassis_sid.value_namespace_prefix = name_space_prefix
                    if(value_path == "clei"):
                        self.clei = value
                        self.clei.value_namespace = name_space
                        self.clei.value_namespace_prefix = name_space_prefix
                    if(value_path == "controller-family"):
                        self.controller_family = value
                        self.controller_family.value_namespace = name_space
                        self.controller_family.value_namespace_prefix = name_space_prefix
                    if(value_path == "controller-type"):
                        self.controller_type = value
                        self.controller_type.value_namespace = name_space
                        self.controller_type.value_namespace_prefix = name_space_prefix
                    if(value_path == "description"):
                        self.description = value
                        self.description.value_namespace = name_space
                        self.description.value_namespace_prefix = name_space_prefix
                    if(value_path == "dev-num1"):
                        self.dev_num1 = value
                        self.dev_num1.value_namespace = name_space
                        self.dev_num1.value_namespace_prefix = name_space_prefix
                    if(value_path == "dev-num2"):
                        self.dev_num2 = value
                        self.dev_num2.value_namespace = name_space
                        self.dev_num2.value_namespace_prefix = name_space_prefix
                    if(value_path == "dev-num3"):
                        self.dev_num3 = value
                        self.dev_num3.value_namespace = name_space
                        self.dev_num3.value_namespace_prefix = name_space_prefix
                    if(value_path == "dev-num4"):
                        self.dev_num4 = value
                        self.dev_num4.value_namespace = name_space
                        self.dev_num4.value_namespace_prefix = name_space_prefix
                    if(value_path == "dev-num5"):
                        self.dev_num5 = value
                        self.dev_num5.value_namespace = name_space
                        self.dev_num5.value_namespace_prefix = name_space_prefix
                    if(value_path == "dev-num6"):
                        self.dev_num6 = value
                        self.dev_num6.value_namespace = name_space
                        self.dev_num6.value_namespace_prefix = name_space_prefix
                    if(value_path == "dev-num7"):
                        self.dev_num7 = value
                        self.dev_num7.value_namespace = name_space
                        self.dev_num7.value_namespace_prefix = name_space_prefix
                    if(value_path == "eci"):
                        self.eci = value
                        self.eci.value_namespace = name_space
                        self.eci.value_namespace_prefix = name_space_prefix
                    if(value_path == "eeprom-size"):
                        self.eeprom_size = value
                        self.eeprom_size.value_namespace = name_space
                        self.eeprom_size.value_namespace_prefix = name_space_prefix
                    if(value_path == "engineer-use"):
                        self.engineer_use = value
                        self.engineer_use.value_namespace = name_space
                        self.engineer_use.value_namespace_prefix = name_space_prefix
                    if(value_path == "fru-major-type"):
                        self.fru_major_type = value
                        self.fru_major_type.value_namespace = name_space
                        self.fru_major_type.value_namespace_prefix = name_space_prefix
                    if(value_path == "fru-minor-type"):
                        self.fru_minor_type = value
                        self.fru_minor_type.value_namespace = name_space
                        self.fru_minor_type.value_namespace_prefix = name_space_prefix
                    if(value_path == "hw-version"):
                        self.hw_version = value
                        self.hw_version.value_namespace = name_space
                        self.hw_version.value_namespace_prefix = name_space_prefix
                    if(value_path == "hwid"):
                        self.hwid = value
                        self.hwid.value_namespace = name_space
                        self.hwid.value_namespace_prefix = name_space_prefix
                    if(value_path == "idprom-format-rev"):
                        self.idprom_format_rev = value
                        self.idprom_format_rev.value_namespace = name_space
                        self.idprom_format_rev.value_namespace_prefix = name_space_prefix
                    if(value_path == "mac-add-blk-size1"):
                        self.mac_add_blk_size1 = value
                        self.mac_add_blk_size1.value_namespace = name_space
                        self.mac_add_blk_size1.value_namespace_prefix = name_space_prefix
                    if(value_path == "mac-add-blk-size2"):
                        self.mac_add_blk_size2 = value
                        self.mac_add_blk_size2.value_namespace = name_space
                        self.mac_add_blk_size2.value_namespace_prefix = name_space_prefix
                    if(value_path == "mac-add-blk-size3"):
                        self.mac_add_blk_size3 = value
                        self.mac_add_blk_size3.value_namespace = name_space
                        self.mac_add_blk_size3.value_namespace_prefix = name_space_prefix
                    if(value_path == "mac-add-blk-size4"):
                        self.mac_add_blk_size4 = value
                        self.mac_add_blk_size4.value_namespace = name_space
                        self.mac_add_blk_size4.value_namespace_prefix = name_space_prefix
                    if(value_path == "manu-test-data"):
                        self.manu_test_data = value
                        self.manu_test_data.value_namespace = name_space
                        self.manu_test_data.value_namespace_prefix = name_space_prefix
                    if(value_path == "mfg-bits"):
                        self.mfg_bits = value
                        self.mfg_bits.value_namespace = name_space
                        self.mfg_bits.value_namespace_prefix = name_space_prefix
                    if(value_path == "mfg-deviation"):
                        self.mfg_deviation = value
                        self.mfg_deviation.value_namespace = name_space
                        self.mfg_deviation.value_namespace_prefix = name_space_prefix
                    if(value_path == "oem-string"):
                        self.oem_string = value
                        self.oem_string.value_namespace = name_space
                        self.oem_string.value_namespace_prefix = name_space_prefix
                    if(value_path == "part-number"):
                        self.part_number = value
                        self.part_number.value_namespace = name_space
                        self.part_number.value_namespace_prefix = name_space_prefix
                    if(value_path == "part-revision"):
                        self.part_revision = value
                        self.part_revision.value_namespace = name_space
                        self.part_revision.value_namespace_prefix = name_space_prefix
                    if(value_path == "pca-num"):
                        self.pca_num = value
                        self.pca_num.value_namespace = name_space
                        self.pca_num.value_namespace_prefix = name_space_prefix
                    if(value_path == "pcavid"):
                        self.pcavid = value
                        self.pcavid.value_namespace = name_space
                        self.pcavid.value_namespace_prefix = name_space_prefix
                    if(value_path == "pcb-serial-num"):
                        self.pcb_serial_num = value
                        self.pcb_serial_num.value_namespace = name_space
                        self.pcb_serial_num.value_namespace_prefix = name_space_prefix
                    if(value_path == "pid"):
                        self.pid = value
                        self.pid.value_namespace = name_space
                        self.pid.value_namespace_prefix = name_space_prefix
                    if(value_path == "power-consumption"):
                        self.power_consumption = value
                        self.power_consumption.value_namespace = name_space
                        self.power_consumption.value_namespace_prefix = name_space_prefix
                    if(value_path == "power-supply-type"):
                        self.power_supply_type = value
                        self.power_supply_type.value_namespace = name_space
                        self.power_supply_type.value_namespace_prefix = name_space_prefix
                    if(value_path == "product-id"):
                        self.product_id = value
                        self.product_id.value_namespace = name_space
                        self.product_id.value_namespace_prefix = name_space_prefix
                    if(value_path == "rma-code"):
                        self.rma_code = value
                        self.rma_code.value_namespace = name_space
                        self.rma_code.value_namespace_prefix = name_space_prefix
                    if(value_path == "serial-number"):
                        self.serial_number = value
                        self.serial_number.value_namespace = name_space
                        self.serial_number.value_namespace_prefix = name_space_prefix
                    if(value_path == "snmpoid"):
                        self.snmpoid = value
                        self.snmpoid.value_namespace = name_space
                        self.snmpoid.value_namespace_prefix = name_space_prefix
                    if(value_path == "top-assem-part-num"):
                        self.top_assem_part_num = value
                        self.top_assem_part_num.value_namespace = name_space
                        self.top_assem_part_num.value_namespace_prefix = name_space_prefix
                    if(value_path == "top-assem-vid"):
                        self.top_assem_vid = value
                        self.top_assem_vid.value_namespace = name_space
                        self.top_assem_vid.value_namespace_prefix = name_space_prefix
                    if(value_path == "udi-description"):
                        self.udi_description = value
                        self.udi_description.value_namespace = name_space
                        self.udi_description.value_namespace_prefix = name_space_prefix
                    if(value_path == "udi-name"):
                        self.udi_name = value
                        self.udi_name.value_namespace = name_space
                        self.udi_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "vid"):
                        self.vid = value
                        self.vid.value_namespace = name_space
                        self.vid.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    self.rack_name.is_set or
                    (self.chassis is not None and self.chassis.has_data()) or
                    (self.fan_traies is not None and self.fan_traies.has_data()) or
                    (self.power_shelfs is not None and self.power_shelfs.has_data()) or
                    (self.slots is not None and self.slots.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.rack_name.yfilter != YFilter.not_set or
                    (self.chassis is not None and self.chassis.has_operation()) or
                    (self.fan_traies is not None and self.fan_traies.has_operation()) or
                    (self.power_shelfs is not None and self.power_shelfs.has_operation()) or
                    (self.slots is not None and self.slots.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "rack" + "[rack-name='" + self.rack_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-sdr-invmgr-diag-oper:diag/racks/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.rack_name.is_set or self.rack_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rack_name.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "chassis"):
                    if (self.chassis is None):
                        self.chassis = Diag.Racks.Rack.Chassis()
                        self.chassis.parent = self
                        self._children_name_map["chassis"] = "chassis"
                    return self.chassis

                if (child_yang_name == "fan-traies"):
                    if (self.fan_traies is None):
                        self.fan_traies = Diag.Racks.Rack.FanTraies()
                        self.fan_traies.parent = self
                        self._children_name_map["fan_traies"] = "fan-traies"
                    return self.fan_traies

                if (child_yang_name == "power-shelfs"):
                    if (self.power_shelfs is None):
                        self.power_shelfs = Diag.Racks.Rack.PowerShelfs()
                        self.power_shelfs.parent = self
                        self._children_name_map["power_shelfs"] = "power-shelfs"
                    return self.power_shelfs

                if (child_yang_name == "slots"):
                    if (self.slots is None):
                        self.slots = Diag.Racks.Rack.Slots()
                        self.slots.parent = self
                        self._children_name_map["slots"] = "slots"
                    return self.slots

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "chassis" or name == "fan-traies" or name == "power-shelfs" or name == "slots" or name == "rack-name"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "rack-name"):
                    self.rack_name = value
                    self.rack_name.value_namespace = name_space
                    self.rack_name.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.rack:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.rack:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "racks" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-sdr-invmgr-diag-oper:diag/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "rack"):
                for c in self.rack:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Diag.Racks.Rack()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.rack.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "rack"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (self.racks is not None and self.racks.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.racks is not None and self.racks.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-sdr-invmgr-diag-oper:diag" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "racks"):
            if (self.racks is None):
                self.racks = Diag.Racks()
                self.racks.parent = self
                self._children_name_map["racks"] = "racks"
            return self.racks

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "racks"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = Diag()
        return self._top_entity

