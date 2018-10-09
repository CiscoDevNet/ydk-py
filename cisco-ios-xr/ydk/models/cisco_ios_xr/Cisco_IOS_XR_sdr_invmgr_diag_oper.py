""" Cisco_IOS_XR_sdr_invmgr_diag_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR sdr\-invmgr\-diag package operational data.

This module contains definitions
for the following management objects\:
  diag\: Diag information

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class Diag(Entity):
    """
    Diag information
    
    .. attribute:: racks
    
    	Table of racks
    	**type**\:  :py:class:`Racks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sdr_invmgr_diag_oper.Diag.Racks>`
    
    

    """

    _prefix = 'sdr-invmgr-diag-oper'
    _revision = '2018-01-31'

    def __init__(self):
        super(Diag, self).__init__()
        self._top_entity = None

        self.yang_name = "diag"
        self.yang_parent_name = "Cisco-IOS-XR-sdr-invmgr-diag-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("racks", ("racks", Diag.Racks))])
        self._leafs = OrderedDict()

        self.racks = Diag.Racks()
        self.racks.parent = self
        self._children_name_map["racks"] = "racks"
        self._segment_path = lambda: "Cisco-IOS-XR-sdr-invmgr-diag-oper:diag"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Diag, [], name, value)


    class Racks(Entity):
        """
        Table of racks
        
        .. attribute:: rack
        
        	Rack name
        	**type**\: list of  		 :py:class:`Rack <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sdr_invmgr_diag_oper.Diag.Racks.Rack>`
        
        

        """

        _prefix = 'sdr-invmgr-diag-oper'
        _revision = '2018-01-31'

        def __init__(self):
            super(Diag.Racks, self).__init__()

            self.yang_name = "racks"
            self.yang_parent_name = "diag"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("rack", ("rack", Diag.Racks.Rack))])
            self._leafs = OrderedDict()

            self.rack = YList(self)
            self._segment_path = lambda: "racks"
            self._absolute_path = lambda: "Cisco-IOS-XR-sdr-invmgr-diag-oper:diag/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Diag.Racks, [], name, value)


        class Rack(Entity):
            """
            Rack name
            
            .. attribute:: rack_name  (key)
            
            	Rack name
            	**type**\: str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: power_shelfs
            
            	Table for rack power shelf 
            	**type**\:  :py:class:`PowerShelfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sdr_invmgr_diag_oper.Diag.Racks.Rack.PowerShelfs>`
            
            .. attribute:: fan_trays
            
            	Table for rack fan trays
            	**type**\:  :py:class:`FanTrays <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sdr_invmgr_diag_oper.Diag.Racks.Rack.FanTrays>`
            
            .. attribute:: slots
            
            	Table of slots
            	**type**\:  :py:class:`Slots <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sdr_invmgr_diag_oper.Diag.Racks.Rack.Slots>`
            
            .. attribute:: chassis
            
            	Chassis information
            	**type**\:  :py:class:`Chassis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sdr_invmgr_diag_oper.Diag.Racks.Rack.Chassis>`
            
            

            """

            _prefix = 'sdr-invmgr-diag-oper'
            _revision = '2018-01-31'

            def __init__(self):
                super(Diag.Racks.Rack, self).__init__()

                self.yang_name = "rack"
                self.yang_parent_name = "racks"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['rack_name']
                self._child_classes = OrderedDict([("power-shelfs", ("power_shelfs", Diag.Racks.Rack.PowerShelfs)), ("fan-trays", ("fan_trays", Diag.Racks.Rack.FanTrays)), ("slots", ("slots", Diag.Racks.Rack.Slots)), ("chassis", ("chassis", Diag.Racks.Rack.Chassis))])
                self._leafs = OrderedDict([
                    ('rack_name', (YLeaf(YType.str, 'rack-name'), ['str'])),
                ])
                self.rack_name = None

                self.power_shelfs = Diag.Racks.Rack.PowerShelfs()
                self.power_shelfs.parent = self
                self._children_name_map["power_shelfs"] = "power-shelfs"

                self.fan_trays = Diag.Racks.Rack.FanTrays()
                self.fan_trays.parent = self
                self._children_name_map["fan_trays"] = "fan-trays"

                self.slots = Diag.Racks.Rack.Slots()
                self.slots.parent = self
                self._children_name_map["slots"] = "slots"

                self.chassis = Diag.Racks.Rack.Chassis()
                self.chassis.parent = self
                self._children_name_map["chassis"] = "chassis"
                self._segment_path = lambda: "rack" + "[rack-name='" + str(self.rack_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-sdr-invmgr-diag-oper:diag/racks/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Diag.Racks.Rack, ['rack_name'], name, value)


            class PowerShelfs(Entity):
                """
                Table for rack power shelf 
                
                .. attribute:: power_shelf
                
                	Power shelf name
                	**type**\: list of  		 :py:class:`PowerShelf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sdr_invmgr_diag_oper.Diag.Racks.Rack.PowerShelfs.PowerShelf>`
                
                

                """

                _prefix = 'sdr-invmgr-diag-oper'
                _revision = '2018-01-31'

                def __init__(self):
                    super(Diag.Racks.Rack.PowerShelfs, self).__init__()

                    self.yang_name = "power-shelfs"
                    self.yang_parent_name = "rack"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("power-shelf", ("power_shelf", Diag.Racks.Rack.PowerShelfs.PowerShelf))])
                    self._leafs = OrderedDict()

                    self.power_shelf = YList(self)
                    self._segment_path = lambda: "power-shelfs"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Diag.Racks.Rack.PowerShelfs, [], name, value)


                class PowerShelf(Entity):
                    """
                    Power shelf name
                    
                    .. attribute:: power_shelf_name  (key)
                    
                    	Power Shelf name
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: power_supplies
                    
                    	Table for rack power supply 
                    	**type**\:  :py:class:`PowerSupplies <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sdr_invmgr_diag_oper.Diag.Racks.Rack.PowerShelfs.PowerShelf.PowerSupplies>`
                    
                    

                    """

                    _prefix = 'sdr-invmgr-diag-oper'
                    _revision = '2018-01-31'

                    def __init__(self):
                        super(Diag.Racks.Rack.PowerShelfs.PowerShelf, self).__init__()

                        self.yang_name = "power-shelf"
                        self.yang_parent_name = "power-shelfs"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['power_shelf_name']
                        self._child_classes = OrderedDict([("power-supplies", ("power_supplies", Diag.Racks.Rack.PowerShelfs.PowerShelf.PowerSupplies))])
                        self._leafs = OrderedDict([
                            ('power_shelf_name', (YLeaf(YType.str, 'power-shelf-name'), ['str'])),
                        ])
                        self.power_shelf_name = None

                        self.power_supplies = Diag.Racks.Rack.PowerShelfs.PowerShelf.PowerSupplies()
                        self.power_supplies.parent = self
                        self._children_name_map["power_supplies"] = "power-supplies"
                        self._segment_path = lambda: "power-shelf" + "[power-shelf-name='" + str(self.power_shelf_name) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Diag.Racks.Rack.PowerShelfs.PowerShelf, ['power_shelf_name'], name, value)


                    class PowerSupplies(Entity):
                        """
                        Table for rack power supply 
                        
                        .. attribute:: power_supply
                        
                        	Power Supply name
                        	**type**\: list of  		 :py:class:`PowerSupply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sdr_invmgr_diag_oper.Diag.Racks.Rack.PowerShelfs.PowerShelf.PowerSupplies.PowerSupply>`
                        
                        

                        """

                        _prefix = 'sdr-invmgr-diag-oper'
                        _revision = '2018-01-31'

                        def __init__(self):
                            super(Diag.Racks.Rack.PowerShelfs.PowerShelf.PowerSupplies, self).__init__()

                            self.yang_name = "power-supplies"
                            self.yang_parent_name = "power-shelf"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("power-supply", ("power_supply", Diag.Racks.Rack.PowerShelfs.PowerShelf.PowerSupplies.PowerSupply))])
                            self._leafs = OrderedDict()

                            self.power_supply = YList(self)
                            self._segment_path = lambda: "power-supplies"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Diag.Racks.Rack.PowerShelfs.PowerShelf.PowerSupplies, [], name, value)


                        class PowerSupply(Entity):
                            """
                            Power Supply name
                            
                            .. attribute:: power_supply_name  (key)
                            
                            	Power Supply name
                            	**type**\: str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            .. attribute:: information
                            
                            	Basic information
                            	**type**\:  :py:class:`Information <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sdr_invmgr_diag_oper.Diag.Racks.Rack.PowerShelfs.PowerShelf.PowerSupplies.PowerSupply.Information>`
                            
                            

                            """

                            _prefix = 'sdr-invmgr-diag-oper'
                            _revision = '2018-01-31'

                            def __init__(self):
                                super(Diag.Racks.Rack.PowerShelfs.PowerShelf.PowerSupplies.PowerSupply, self).__init__()

                                self.yang_name = "power-supply"
                                self.yang_parent_name = "power-supplies"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['power_supply_name']
                                self._child_classes = OrderedDict([("information", ("information", Diag.Racks.Rack.PowerShelfs.PowerShelf.PowerSupplies.PowerSupply.Information))])
                                self._leafs = OrderedDict([
                                    ('power_supply_name', (YLeaf(YType.str, 'power-supply-name'), ['str'])),
                                ])
                                self.power_supply_name = None

                                self.information = Diag.Racks.Rack.PowerShelfs.PowerShelf.PowerSupplies.PowerSupply.Information()
                                self.information.parent = self
                                self._children_name_map["information"] = "information"
                                self._segment_path = lambda: "power-supply" + "[power-supply-name='" + str(self.power_supply_name) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Diag.Racks.Rack.PowerShelfs.PowerShelf.PowerSupplies.PowerSupply, ['power_supply_name'], name, value)


                            class Information(Entity):
                                """
                                Basic information
                                
                                .. attribute:: rma
                                
                                	RMA Data
                                	**type**\:  :py:class:`Rma <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sdr_invmgr_diag_oper.Diag.Racks.Rack.PowerShelfs.PowerShelf.PowerSupplies.PowerSupply.Information.Rma>`
                                
                                .. attribute:: description
                                
                                	A textual description of physical entity
                                	**type**\: str
                                
                                	**length:** 0..255
                                
                                .. attribute:: idprom_format_rev
                                
                                	IDPROM Format Revision
                                	**type**\: str
                                
                                	**length:** 0..255
                                
                                .. attribute:: controller_family
                                
                                	Controller family
                                	**type**\: str
                                
                                	**length:** 0..255
                                
                                .. attribute:: controller_type
                                
                                	Controller type
                                	**type**\: str
                                
                                	**length:** 0..255
                                
                                .. attribute:: vid
                                
                                	Version ID
                                	**type**\: str
                                
                                	**length:** 0..255
                                
                                .. attribute:: hwid
                                
                                	Hardware Revision
                                	**type**\: str
                                
                                	**length:** 0..255
                                
                                .. attribute:: pid
                                
                                	Product ID
                                	**type**\: str
                                
                                	**length:** 0..255
                                
                                .. attribute:: udi_description
                                
                                	UDI description
                                	**type**\: str
                                
                                	**length:** 0..255
                                
                                .. attribute:: udi_name
                                
                                	UDI name
                                	**type**\: str
                                
                                	**length:** 0..255
                                
                                .. attribute:: clei
                                
                                	Common Language Equipment Identifier (CLEI) code
                                	**type**\: str
                                
                                	**length:** 0..255
                                
                                .. attribute:: eci
                                
                                	Equipment Catalog Item (ECI) number
                                	**type**\: str
                                
                                	**length:** 0..255
                                
                                .. attribute:: top_assem_part_num
                                
                                	Top assembly part number
                                	**type**\: str
                                
                                	**length:** 0..255
                                
                                .. attribute:: top_assem_vid
                                
                                	Top assembly revision number
                                	**type**\: str
                                
                                	**length:** 0..255
                                
                                .. attribute:: pca_num
                                
                                	PCA number
                                	**type**\: str
                                
                                	**length:** 0..255
                                
                                .. attribute:: pcavid
                                
                                	PCA revision ID
                                	**type**\: str
                                
                                	**length:** 0..255
                                
                                .. attribute:: chassis_sid
                                
                                	Chassis serial number
                                	**type**\: str
                                
                                	**length:** 0..255
                                
                                .. attribute:: dev_num1
                                
                                	Deviation Number # 1
                                	**type**\: str
                                
                                	**length:** 0..255
                                
                                .. attribute:: dev_num2
                                
                                	Deviation Number # 2
                                	**type**\: str
                                
                                	**length:** 0..255
                                
                                .. attribute:: dev_num3
                                
                                	Deviation Number # 3
                                	**type**\: str
                                
                                	**length:** 0..255
                                
                                .. attribute:: dev_num4
                                
                                	Deviation Number # 4
                                	**type**\: str
                                
                                	**length:** 0..255
                                
                                .. attribute:: dev_num5
                                
                                	Deviation Number # 5
                                	**type**\: str
                                
                                	**length:** 0..255
                                
                                .. attribute:: dev_num6
                                
                                	Deviation Number # 6
                                	**type**\: str
                                
                                	**length:** 0..255
                                
                                .. attribute:: dev_num7
                                
                                	Deviation Number # 7
                                	**type**\: str
                                
                                	**length:** 0..255
                                
                                .. attribute:: manu_test_data
                                
                                	Manufacturing Test Data
                                	**type**\: str
                                
                                	**length:** 0..255
                                
                                .. attribute:: asset_id
                                
                                	Asset ID
                                	**type**\: str
                                
                                	**length:** 0..255
                                
                                .. attribute:: asset_alias
                                
                                	Asset Alias
                                	**type**\: str
                                
                                	**length:** 0..255
                                
                                .. attribute:: base_mac_address1
                                
                                	Base Mac Address #1
                                	**type**\: str
                                
                                	**length:** 0..255
                                
                                .. attribute:: mac_add_blk_size1
                                
                                	Mac Address Block Size #1
                                	**type**\: str
                                
                                	**length:** 0..255
                                
                                .. attribute:: base_mac_address2
                                
                                	Base Mac Address #2
                                	**type**\: str
                                
                                	**length:** 0..255
                                
                                .. attribute:: mac_add_blk_size2
                                
                                	Mac Address Block Size #2
                                	**type**\: str
                                
                                	**length:** 0..255
                                
                                .. attribute:: base_mac_address3
                                
                                	Base Mac Address #3
                                	**type**\: str
                                
                                	**length:** 0..255
                                
                                .. attribute:: mac_add_blk_size3
                                
                                	Mac Address Block Size #3
                                	**type**\: str
                                
                                	**length:** 0..255
                                
                                .. attribute:: base_mac_address4
                                
                                	Base Mac Address #4
                                	**type**\: str
                                
                                	**length:** 0..255
                                
                                .. attribute:: mac_add_blk_size4
                                
                                	Mac Address Block Size #4
                                	**type**\: str
                                
                                	**length:** 0..255
                                
                                .. attribute:: pcb_serial_num
                                
                                	PCB Serial Number
                                	**type**\: str
                                
                                	**length:** 0..255
                                
                                .. attribute:: power_supply_type
                                
                                	Power Supply Type
                                	**type**\: str
                                
                                	**length:** 0..255
                                
                                .. attribute:: power_consumption
                                
                                	Power Consumption
                                	**type**\: str
                                
                                	**length:** 0..255
                                
                                .. attribute:: block_signature
                                
                                	Block Signature
                                	**type**\: str
                                
                                	**length:** 0..255
                                
                                .. attribute:: block_version
                                
                                	Block Version
                                	**type**\: str
                                
                                	**length:** 0..255
                                
                                .. attribute:: block_length
                                
                                	Block Length
                                	**type**\: str
                                
                                	**length:** 0..255
                                
                                .. attribute:: block_checksum
                                
                                	Block Checksum
                                	**type**\: str
                                
                                	**length:** 0..255
                                
                                .. attribute:: eeprom_size
                                
                                	EEPROM Size
                                	**type**\: str
                                
                                	**length:** 0..255
                                
                                .. attribute:: block_count
                                
                                	Block Count
                                	**type**\: str
                                
                                	**length:** 0..255
                                
                                .. attribute:: fru_major_type
                                
                                	FRU Major Type
                                	**type**\: str
                                
                                	**length:** 0..255
                                
                                .. attribute:: fru_minor_type
                                
                                	FRU Minor Type
                                	**type**\: str
                                
                                	**length:** 0..255
                                
                                .. attribute:: oem_string
                                
                                	OEM String
                                	**type**\: str
                                
                                	**length:** 0..255
                                
                                .. attribute:: product_id
                                
                                	Product ID
                                	**type**\: str
                                
                                	**length:** 0..255
                                
                                .. attribute:: serial_number
                                
                                	Serial Number
                                	**type**\: str
                                
                                	**length:** 0..255
                                
                                .. attribute:: part_number
                                
                                	Part Number
                                	**type**\: str
                                
                                	**length:** 0..255
                                
                                .. attribute:: part_revision
                                
                                	Part Revision
                                	**type**\: str
                                
                                	**length:** 0..255
                                
                                .. attribute:: mfg_deviation
                                
                                	MFG Deviation
                                	**type**\: str
                                
                                	**length:** 0..255
                                
                                .. attribute:: hw_version
                                
                                	Hardware Version
                                	**type**\: str
                                
                                	**length:** 0..255
                                
                                .. attribute:: mfg_bits
                                
                                	MFG Bits
                                	**type**\: str
                                
                                	**length:** 0..255
                                
                                .. attribute:: engineer_use
                                
                                	Engineer Use
                                	**type**\: str
                                
                                	**length:** 0..255
                                
                                .. attribute:: snmpoid
                                
                                	SNMP OID
                                	**type**\: str
                                
                                	**length:** 0..255
                                
                                .. attribute:: rma_code
                                
                                	RMA Code
                                	**type**\: str
                                
                                	**length:** 0..255
                                
                                .. attribute:: eci_alpha_number
                                
                                	AlphaNumeric Equipment Catalog Item (ECI) number
                                	**type**\: str
                                
                                	**length:** 0..255
                                
                                

                                """

                                _prefix = 'sdr-invmgr-diag-oper'
                                _revision = '2018-01-31'

                                def __init__(self):
                                    super(Diag.Racks.Rack.PowerShelfs.PowerShelf.PowerSupplies.PowerSupply.Information, self).__init__()

                                    self.yang_name = "information"
                                    self.yang_parent_name = "power-supply"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("rma", ("rma", Diag.Racks.Rack.PowerShelfs.PowerShelf.PowerSupplies.PowerSupply.Information.Rma))])
                                    self._leafs = OrderedDict([
                                        ('description', (YLeaf(YType.str, 'description'), ['str'])),
                                        ('idprom_format_rev', (YLeaf(YType.str, 'idprom-format-rev'), ['str'])),
                                        ('controller_family', (YLeaf(YType.str, 'controller-family'), ['str'])),
                                        ('controller_type', (YLeaf(YType.str, 'controller-type'), ['str'])),
                                        ('vid', (YLeaf(YType.str, 'vid'), ['str'])),
                                        ('hwid', (YLeaf(YType.str, 'hwid'), ['str'])),
                                        ('pid', (YLeaf(YType.str, 'pid'), ['str'])),
                                        ('udi_description', (YLeaf(YType.str, 'udi-description'), ['str'])),
                                        ('udi_name', (YLeaf(YType.str, 'udi-name'), ['str'])),
                                        ('clei', (YLeaf(YType.str, 'clei'), ['str'])),
                                        ('eci', (YLeaf(YType.str, 'eci'), ['str'])),
                                        ('top_assem_part_num', (YLeaf(YType.str, 'top-assem-part-num'), ['str'])),
                                        ('top_assem_vid', (YLeaf(YType.str, 'top-assem-vid'), ['str'])),
                                        ('pca_num', (YLeaf(YType.str, 'pca-num'), ['str'])),
                                        ('pcavid', (YLeaf(YType.str, 'pcavid'), ['str'])),
                                        ('chassis_sid', (YLeaf(YType.str, 'chassis-sid'), ['str'])),
                                        ('dev_num1', (YLeaf(YType.str, 'dev-num1'), ['str'])),
                                        ('dev_num2', (YLeaf(YType.str, 'dev-num2'), ['str'])),
                                        ('dev_num3', (YLeaf(YType.str, 'dev-num3'), ['str'])),
                                        ('dev_num4', (YLeaf(YType.str, 'dev-num4'), ['str'])),
                                        ('dev_num5', (YLeaf(YType.str, 'dev-num5'), ['str'])),
                                        ('dev_num6', (YLeaf(YType.str, 'dev-num6'), ['str'])),
                                        ('dev_num7', (YLeaf(YType.str, 'dev-num7'), ['str'])),
                                        ('manu_test_data', (YLeaf(YType.str, 'manu-test-data'), ['str'])),
                                        ('asset_id', (YLeaf(YType.str, 'asset-id'), ['str'])),
                                        ('asset_alias', (YLeaf(YType.str, 'asset-alias'), ['str'])),
                                        ('base_mac_address1', (YLeaf(YType.str, 'base-mac-address1'), ['str'])),
                                        ('mac_add_blk_size1', (YLeaf(YType.str, 'mac-add-blk-size1'), ['str'])),
                                        ('base_mac_address2', (YLeaf(YType.str, 'base-mac-address2'), ['str'])),
                                        ('mac_add_blk_size2', (YLeaf(YType.str, 'mac-add-blk-size2'), ['str'])),
                                        ('base_mac_address3', (YLeaf(YType.str, 'base-mac-address3'), ['str'])),
                                        ('mac_add_blk_size3', (YLeaf(YType.str, 'mac-add-blk-size3'), ['str'])),
                                        ('base_mac_address4', (YLeaf(YType.str, 'base-mac-address4'), ['str'])),
                                        ('mac_add_blk_size4', (YLeaf(YType.str, 'mac-add-blk-size4'), ['str'])),
                                        ('pcb_serial_num', (YLeaf(YType.str, 'pcb-serial-num'), ['str'])),
                                        ('power_supply_type', (YLeaf(YType.str, 'power-supply-type'), ['str'])),
                                        ('power_consumption', (YLeaf(YType.str, 'power-consumption'), ['str'])),
                                        ('block_signature', (YLeaf(YType.str, 'block-signature'), ['str'])),
                                        ('block_version', (YLeaf(YType.str, 'block-version'), ['str'])),
                                        ('block_length', (YLeaf(YType.str, 'block-length'), ['str'])),
                                        ('block_checksum', (YLeaf(YType.str, 'block-checksum'), ['str'])),
                                        ('eeprom_size', (YLeaf(YType.str, 'eeprom-size'), ['str'])),
                                        ('block_count', (YLeaf(YType.str, 'block-count'), ['str'])),
                                        ('fru_major_type', (YLeaf(YType.str, 'fru-major-type'), ['str'])),
                                        ('fru_minor_type', (YLeaf(YType.str, 'fru-minor-type'), ['str'])),
                                        ('oem_string', (YLeaf(YType.str, 'oem-string'), ['str'])),
                                        ('product_id', (YLeaf(YType.str, 'product-id'), ['str'])),
                                        ('serial_number', (YLeaf(YType.str, 'serial-number'), ['str'])),
                                        ('part_number', (YLeaf(YType.str, 'part-number'), ['str'])),
                                        ('part_revision', (YLeaf(YType.str, 'part-revision'), ['str'])),
                                        ('mfg_deviation', (YLeaf(YType.str, 'mfg-deviation'), ['str'])),
                                        ('hw_version', (YLeaf(YType.str, 'hw-version'), ['str'])),
                                        ('mfg_bits', (YLeaf(YType.str, 'mfg-bits'), ['str'])),
                                        ('engineer_use', (YLeaf(YType.str, 'engineer-use'), ['str'])),
                                        ('snmpoid', (YLeaf(YType.str, 'snmpoid'), ['str'])),
                                        ('rma_code', (YLeaf(YType.str, 'rma-code'), ['str'])),
                                        ('eci_alpha_number', (YLeaf(YType.str, 'eci-alpha-number'), ['str'])),
                                    ])
                                    self.description = None
                                    self.idprom_format_rev = None
                                    self.controller_family = None
                                    self.controller_type = None
                                    self.vid = None
                                    self.hwid = None
                                    self.pid = None
                                    self.udi_description = None
                                    self.udi_name = None
                                    self.clei = None
                                    self.eci = None
                                    self.top_assem_part_num = None
                                    self.top_assem_vid = None
                                    self.pca_num = None
                                    self.pcavid = None
                                    self.chassis_sid = None
                                    self.dev_num1 = None
                                    self.dev_num2 = None
                                    self.dev_num3 = None
                                    self.dev_num4 = None
                                    self.dev_num5 = None
                                    self.dev_num6 = None
                                    self.dev_num7 = None
                                    self.manu_test_data = None
                                    self.asset_id = None
                                    self.asset_alias = None
                                    self.base_mac_address1 = None
                                    self.mac_add_blk_size1 = None
                                    self.base_mac_address2 = None
                                    self.mac_add_blk_size2 = None
                                    self.base_mac_address3 = None
                                    self.mac_add_blk_size3 = None
                                    self.base_mac_address4 = None
                                    self.mac_add_blk_size4 = None
                                    self.pcb_serial_num = None
                                    self.power_supply_type = None
                                    self.power_consumption = None
                                    self.block_signature = None
                                    self.block_version = None
                                    self.block_length = None
                                    self.block_checksum = None
                                    self.eeprom_size = None
                                    self.block_count = None
                                    self.fru_major_type = None
                                    self.fru_minor_type = None
                                    self.oem_string = None
                                    self.product_id = None
                                    self.serial_number = None
                                    self.part_number = None
                                    self.part_revision = None
                                    self.mfg_deviation = None
                                    self.hw_version = None
                                    self.mfg_bits = None
                                    self.engineer_use = None
                                    self.snmpoid = None
                                    self.rma_code = None
                                    self.eci_alpha_number = None

                                    self.rma = Diag.Racks.Rack.PowerShelfs.PowerShelf.PowerSupplies.PowerSupply.Information.Rma()
                                    self.rma.parent = self
                                    self._children_name_map["rma"] = "rma"
                                    self._segment_path = lambda: "information"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Diag.Racks.Rack.PowerShelfs.PowerShelf.PowerSupplies.PowerSupply.Information, [u'description', u'idprom_format_rev', u'controller_family', u'controller_type', u'vid', u'hwid', u'pid', u'udi_description', u'udi_name', u'clei', u'eci', u'top_assem_part_num', u'top_assem_vid', u'pca_num', u'pcavid', u'chassis_sid', u'dev_num1', u'dev_num2', u'dev_num3', u'dev_num4', u'dev_num5', u'dev_num6', u'dev_num7', u'manu_test_data', u'asset_id', u'asset_alias', u'base_mac_address1', u'mac_add_blk_size1', u'base_mac_address2', u'mac_add_blk_size2', u'base_mac_address3', u'mac_add_blk_size3', u'base_mac_address4', u'mac_add_blk_size4', u'pcb_serial_num', u'power_supply_type', u'power_consumption', u'block_signature', u'block_version', u'block_length', u'block_checksum', u'eeprom_size', u'block_count', u'fru_major_type', u'fru_minor_type', u'oem_string', u'product_id', u'serial_number', u'part_number', u'part_revision', u'mfg_deviation', u'hw_version', u'mfg_bits', u'engineer_use', u'snmpoid', u'rma_code', u'eci_alpha_number'], name, value)


                                class Rma(Entity):
                                    """
                                    RMA Data
                                    
                                    .. attribute:: test_history
                                    
                                    	Test history
                                    	**type**\: str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: rma_number
                                    
                                    	RMA tracking number format is N\-N\-N
                                    	**type**\: str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: rma_history
                                    
                                    	RMA history
                                    	**type**\: str
                                    
                                    	**length:** 0..255
                                    
                                    

                                    """

                                    _prefix = 'sdr-invmgr-diag-oper'
                                    _revision = '2018-01-31'

                                    def __init__(self):
                                        super(Diag.Racks.Rack.PowerShelfs.PowerShelf.PowerSupplies.PowerSupply.Information.Rma, self).__init__()

                                        self.yang_name = "rma"
                                        self.yang_parent_name = "information"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('test_history', (YLeaf(YType.str, 'test-history'), ['str'])),
                                            ('rma_number', (YLeaf(YType.str, 'rma-number'), ['str'])),
                                            ('rma_history', (YLeaf(YType.str, 'rma-history'), ['str'])),
                                        ])
                                        self.test_history = None
                                        self.rma_number = None
                                        self.rma_history = None
                                        self._segment_path = lambda: "rma"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Diag.Racks.Rack.PowerShelfs.PowerShelf.PowerSupplies.PowerSupply.Information.Rma, [u'test_history', u'rma_number', u'rma_history'], name, value)


            class FanTrays(Entity):
                """
                Table for rack fan trays
                
                .. attribute:: fan_tray
                
                	Fan tray name
                	**type**\: list of  		 :py:class:`FanTray <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sdr_invmgr_diag_oper.Diag.Racks.Rack.FanTrays.FanTray>`
                
                

                """

                _prefix = 'sdr-invmgr-diag-oper'
                _revision = '2018-01-31'

                def __init__(self):
                    super(Diag.Racks.Rack.FanTrays, self).__init__()

                    self.yang_name = "fan-trays"
                    self.yang_parent_name = "rack"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("fan-tray", ("fan_tray", Diag.Racks.Rack.FanTrays.FanTray))])
                    self._leafs = OrderedDict()

                    self.fan_tray = YList(self)
                    self._segment_path = lambda: "fan-trays"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Diag.Racks.Rack.FanTrays, [], name, value)


                class FanTray(Entity):
                    """
                    Fan tray name
                    
                    .. attribute:: fan_tray_name  (key)
                    
                    	Fan tray name
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: fanses
                    
                    	Table for rack fans 
                    	**type**\:  :py:class:`Fanses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sdr_invmgr_diag_oper.Diag.Racks.Rack.FanTrays.FanTray.Fanses>`
                    
                    

                    """

                    _prefix = 'sdr-invmgr-diag-oper'
                    _revision = '2018-01-31'

                    def __init__(self):
                        super(Diag.Racks.Rack.FanTrays.FanTray, self).__init__()

                        self.yang_name = "fan-tray"
                        self.yang_parent_name = "fan-trays"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['fan_tray_name']
                        self._child_classes = OrderedDict([("fanses", ("fanses", Diag.Racks.Rack.FanTrays.FanTray.Fanses))])
                        self._leafs = OrderedDict([
                            ('fan_tray_name', (YLeaf(YType.str, 'fan-tray-name'), ['str'])),
                        ])
                        self.fan_tray_name = None

                        self.fanses = Diag.Racks.Rack.FanTrays.FanTray.Fanses()
                        self.fanses.parent = self
                        self._children_name_map["fanses"] = "fanses"
                        self._segment_path = lambda: "fan-tray" + "[fan-tray-name='" + str(self.fan_tray_name) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Diag.Racks.Rack.FanTrays.FanTray, ['fan_tray_name'], name, value)


                    class Fanses(Entity):
                        """
                        Table for rack fans 
                        
                        .. attribute:: fans
                        
                        	Fan name
                        	**type**\: list of  		 :py:class:`Fans <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sdr_invmgr_diag_oper.Diag.Racks.Rack.FanTrays.FanTray.Fanses.Fans>`
                        
                        

                        """

                        _prefix = 'sdr-invmgr-diag-oper'
                        _revision = '2018-01-31'

                        def __init__(self):
                            super(Diag.Racks.Rack.FanTrays.FanTray.Fanses, self).__init__()

                            self.yang_name = "fanses"
                            self.yang_parent_name = "fan-tray"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("fans", ("fans", Diag.Racks.Rack.FanTrays.FanTray.Fanses.Fans))])
                            self._leafs = OrderedDict()

                            self.fans = YList(self)
                            self._segment_path = lambda: "fanses"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Diag.Racks.Rack.FanTrays.FanTray.Fanses, [], name, value)


                        class Fans(Entity):
                            """
                            Fan name
                            
                            .. attribute:: fans_name  (key)
                            
                            	Fans name
                            	**type**\: str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            .. attribute:: information
                            
                            	Basic information
                            	**type**\:  :py:class:`Information <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sdr_invmgr_diag_oper.Diag.Racks.Rack.FanTrays.FanTray.Fanses.Fans.Information>`
                            
                            

                            """

                            _prefix = 'sdr-invmgr-diag-oper'
                            _revision = '2018-01-31'

                            def __init__(self):
                                super(Diag.Racks.Rack.FanTrays.FanTray.Fanses.Fans, self).__init__()

                                self.yang_name = "fans"
                                self.yang_parent_name = "fanses"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['fans_name']
                                self._child_classes = OrderedDict([("information", ("information", Diag.Racks.Rack.FanTrays.FanTray.Fanses.Fans.Information))])
                                self._leafs = OrderedDict([
                                    ('fans_name', (YLeaf(YType.str, 'fans-name'), ['str'])),
                                ])
                                self.fans_name = None

                                self.information = Diag.Racks.Rack.FanTrays.FanTray.Fanses.Fans.Information()
                                self.information.parent = self
                                self._children_name_map["information"] = "information"
                                self._segment_path = lambda: "fans" + "[fans-name='" + str(self.fans_name) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Diag.Racks.Rack.FanTrays.FanTray.Fanses.Fans, ['fans_name'], name, value)


                            class Information(Entity):
                                """
                                Basic information
                                
                                .. attribute:: rma
                                
                                	RMA Data
                                	**type**\:  :py:class:`Rma <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sdr_invmgr_diag_oper.Diag.Racks.Rack.FanTrays.FanTray.Fanses.Fans.Information.Rma>`
                                
                                .. attribute:: description
                                
                                	A textual description of physical entity
                                	**type**\: str
                                
                                	**length:** 0..255
                                
                                .. attribute:: idprom_format_rev
                                
                                	IDPROM Format Revision
                                	**type**\: str
                                
                                	**length:** 0..255
                                
                                .. attribute:: controller_family
                                
                                	Controller family
                                	**type**\: str
                                
                                	**length:** 0..255
                                
                                .. attribute:: controller_type
                                
                                	Controller type
                                	**type**\: str
                                
                                	**length:** 0..255
                                
                                .. attribute:: vid
                                
                                	Version ID
                                	**type**\: str
                                
                                	**length:** 0..255
                                
                                .. attribute:: hwid
                                
                                	Hardware Revision
                                	**type**\: str
                                
                                	**length:** 0..255
                                
                                .. attribute:: pid
                                
                                	Product ID
                                	**type**\: str
                                
                                	**length:** 0..255
                                
                                .. attribute:: udi_description
                                
                                	UDI description
                                	**type**\: str
                                
                                	**length:** 0..255
                                
                                .. attribute:: udi_name
                                
                                	UDI name
                                	**type**\: str
                                
                                	**length:** 0..255
                                
                                .. attribute:: clei
                                
                                	Common Language Equipment Identifier (CLEI) code
                                	**type**\: str
                                
                                	**length:** 0..255
                                
                                .. attribute:: eci
                                
                                	Equipment Catalog Item (ECI) number
                                	**type**\: str
                                
                                	**length:** 0..255
                                
                                .. attribute:: top_assem_part_num
                                
                                	Top assembly part number
                                	**type**\: str
                                
                                	**length:** 0..255
                                
                                .. attribute:: top_assem_vid
                                
                                	Top assembly revision number
                                	**type**\: str
                                
                                	**length:** 0..255
                                
                                .. attribute:: pca_num
                                
                                	PCA number
                                	**type**\: str
                                
                                	**length:** 0..255
                                
                                .. attribute:: pcavid
                                
                                	PCA revision ID
                                	**type**\: str
                                
                                	**length:** 0..255
                                
                                .. attribute:: chassis_sid
                                
                                	Chassis serial number
                                	**type**\: str
                                
                                	**length:** 0..255
                                
                                .. attribute:: dev_num1
                                
                                	Deviation Number # 1
                                	**type**\: str
                                
                                	**length:** 0..255
                                
                                .. attribute:: dev_num2
                                
                                	Deviation Number # 2
                                	**type**\: str
                                
                                	**length:** 0..255
                                
                                .. attribute:: dev_num3
                                
                                	Deviation Number # 3
                                	**type**\: str
                                
                                	**length:** 0..255
                                
                                .. attribute:: dev_num4
                                
                                	Deviation Number # 4
                                	**type**\: str
                                
                                	**length:** 0..255
                                
                                .. attribute:: dev_num5
                                
                                	Deviation Number # 5
                                	**type**\: str
                                
                                	**length:** 0..255
                                
                                .. attribute:: dev_num6
                                
                                	Deviation Number # 6
                                	**type**\: str
                                
                                	**length:** 0..255
                                
                                .. attribute:: dev_num7
                                
                                	Deviation Number # 7
                                	**type**\: str
                                
                                	**length:** 0..255
                                
                                .. attribute:: manu_test_data
                                
                                	Manufacturing Test Data
                                	**type**\: str
                                
                                	**length:** 0..255
                                
                                .. attribute:: asset_id
                                
                                	Asset ID
                                	**type**\: str
                                
                                	**length:** 0..255
                                
                                .. attribute:: asset_alias
                                
                                	Asset Alias
                                	**type**\: str
                                
                                	**length:** 0..255
                                
                                .. attribute:: base_mac_address1
                                
                                	Base Mac Address #1
                                	**type**\: str
                                
                                	**length:** 0..255
                                
                                .. attribute:: mac_add_blk_size1
                                
                                	Mac Address Block Size #1
                                	**type**\: str
                                
                                	**length:** 0..255
                                
                                .. attribute:: base_mac_address2
                                
                                	Base Mac Address #2
                                	**type**\: str
                                
                                	**length:** 0..255
                                
                                .. attribute:: mac_add_blk_size2
                                
                                	Mac Address Block Size #2
                                	**type**\: str
                                
                                	**length:** 0..255
                                
                                .. attribute:: base_mac_address3
                                
                                	Base Mac Address #3
                                	**type**\: str
                                
                                	**length:** 0..255
                                
                                .. attribute:: mac_add_blk_size3
                                
                                	Mac Address Block Size #3
                                	**type**\: str
                                
                                	**length:** 0..255
                                
                                .. attribute:: base_mac_address4
                                
                                	Base Mac Address #4
                                	**type**\: str
                                
                                	**length:** 0..255
                                
                                .. attribute:: mac_add_blk_size4
                                
                                	Mac Address Block Size #4
                                	**type**\: str
                                
                                	**length:** 0..255
                                
                                .. attribute:: pcb_serial_num
                                
                                	PCB Serial Number
                                	**type**\: str
                                
                                	**length:** 0..255
                                
                                .. attribute:: power_supply_type
                                
                                	Power Supply Type
                                	**type**\: str
                                
                                	**length:** 0..255
                                
                                .. attribute:: power_consumption
                                
                                	Power Consumption
                                	**type**\: str
                                
                                	**length:** 0..255
                                
                                .. attribute:: block_signature
                                
                                	Block Signature
                                	**type**\: str
                                
                                	**length:** 0..255
                                
                                .. attribute:: block_version
                                
                                	Block Version
                                	**type**\: str
                                
                                	**length:** 0..255
                                
                                .. attribute:: block_length
                                
                                	Block Length
                                	**type**\: str
                                
                                	**length:** 0..255
                                
                                .. attribute:: block_checksum
                                
                                	Block Checksum
                                	**type**\: str
                                
                                	**length:** 0..255
                                
                                .. attribute:: eeprom_size
                                
                                	EEPROM Size
                                	**type**\: str
                                
                                	**length:** 0..255
                                
                                .. attribute:: block_count
                                
                                	Block Count
                                	**type**\: str
                                
                                	**length:** 0..255
                                
                                .. attribute:: fru_major_type
                                
                                	FRU Major Type
                                	**type**\: str
                                
                                	**length:** 0..255
                                
                                .. attribute:: fru_minor_type
                                
                                	FRU Minor Type
                                	**type**\: str
                                
                                	**length:** 0..255
                                
                                .. attribute:: oem_string
                                
                                	OEM String
                                	**type**\: str
                                
                                	**length:** 0..255
                                
                                .. attribute:: product_id
                                
                                	Product ID
                                	**type**\: str
                                
                                	**length:** 0..255
                                
                                .. attribute:: serial_number
                                
                                	Serial Number
                                	**type**\: str
                                
                                	**length:** 0..255
                                
                                .. attribute:: part_number
                                
                                	Part Number
                                	**type**\: str
                                
                                	**length:** 0..255
                                
                                .. attribute:: part_revision
                                
                                	Part Revision
                                	**type**\: str
                                
                                	**length:** 0..255
                                
                                .. attribute:: mfg_deviation
                                
                                	MFG Deviation
                                	**type**\: str
                                
                                	**length:** 0..255
                                
                                .. attribute:: hw_version
                                
                                	Hardware Version
                                	**type**\: str
                                
                                	**length:** 0..255
                                
                                .. attribute:: mfg_bits
                                
                                	MFG Bits
                                	**type**\: str
                                
                                	**length:** 0..255
                                
                                .. attribute:: engineer_use
                                
                                	Engineer Use
                                	**type**\: str
                                
                                	**length:** 0..255
                                
                                .. attribute:: snmpoid
                                
                                	SNMP OID
                                	**type**\: str
                                
                                	**length:** 0..255
                                
                                .. attribute:: rma_code
                                
                                	RMA Code
                                	**type**\: str
                                
                                	**length:** 0..255
                                
                                .. attribute:: eci_alpha_number
                                
                                	AlphaNumeric Equipment Catalog Item (ECI) number
                                	**type**\: str
                                
                                	**length:** 0..255
                                
                                

                                """

                                _prefix = 'sdr-invmgr-diag-oper'
                                _revision = '2018-01-31'

                                def __init__(self):
                                    super(Diag.Racks.Rack.FanTrays.FanTray.Fanses.Fans.Information, self).__init__()

                                    self.yang_name = "information"
                                    self.yang_parent_name = "fans"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("rma", ("rma", Diag.Racks.Rack.FanTrays.FanTray.Fanses.Fans.Information.Rma))])
                                    self._leafs = OrderedDict([
                                        ('description', (YLeaf(YType.str, 'description'), ['str'])),
                                        ('idprom_format_rev', (YLeaf(YType.str, 'idprom-format-rev'), ['str'])),
                                        ('controller_family', (YLeaf(YType.str, 'controller-family'), ['str'])),
                                        ('controller_type', (YLeaf(YType.str, 'controller-type'), ['str'])),
                                        ('vid', (YLeaf(YType.str, 'vid'), ['str'])),
                                        ('hwid', (YLeaf(YType.str, 'hwid'), ['str'])),
                                        ('pid', (YLeaf(YType.str, 'pid'), ['str'])),
                                        ('udi_description', (YLeaf(YType.str, 'udi-description'), ['str'])),
                                        ('udi_name', (YLeaf(YType.str, 'udi-name'), ['str'])),
                                        ('clei', (YLeaf(YType.str, 'clei'), ['str'])),
                                        ('eci', (YLeaf(YType.str, 'eci'), ['str'])),
                                        ('top_assem_part_num', (YLeaf(YType.str, 'top-assem-part-num'), ['str'])),
                                        ('top_assem_vid', (YLeaf(YType.str, 'top-assem-vid'), ['str'])),
                                        ('pca_num', (YLeaf(YType.str, 'pca-num'), ['str'])),
                                        ('pcavid', (YLeaf(YType.str, 'pcavid'), ['str'])),
                                        ('chassis_sid', (YLeaf(YType.str, 'chassis-sid'), ['str'])),
                                        ('dev_num1', (YLeaf(YType.str, 'dev-num1'), ['str'])),
                                        ('dev_num2', (YLeaf(YType.str, 'dev-num2'), ['str'])),
                                        ('dev_num3', (YLeaf(YType.str, 'dev-num3'), ['str'])),
                                        ('dev_num4', (YLeaf(YType.str, 'dev-num4'), ['str'])),
                                        ('dev_num5', (YLeaf(YType.str, 'dev-num5'), ['str'])),
                                        ('dev_num6', (YLeaf(YType.str, 'dev-num6'), ['str'])),
                                        ('dev_num7', (YLeaf(YType.str, 'dev-num7'), ['str'])),
                                        ('manu_test_data', (YLeaf(YType.str, 'manu-test-data'), ['str'])),
                                        ('asset_id', (YLeaf(YType.str, 'asset-id'), ['str'])),
                                        ('asset_alias', (YLeaf(YType.str, 'asset-alias'), ['str'])),
                                        ('base_mac_address1', (YLeaf(YType.str, 'base-mac-address1'), ['str'])),
                                        ('mac_add_blk_size1', (YLeaf(YType.str, 'mac-add-blk-size1'), ['str'])),
                                        ('base_mac_address2', (YLeaf(YType.str, 'base-mac-address2'), ['str'])),
                                        ('mac_add_blk_size2', (YLeaf(YType.str, 'mac-add-blk-size2'), ['str'])),
                                        ('base_mac_address3', (YLeaf(YType.str, 'base-mac-address3'), ['str'])),
                                        ('mac_add_blk_size3', (YLeaf(YType.str, 'mac-add-blk-size3'), ['str'])),
                                        ('base_mac_address4', (YLeaf(YType.str, 'base-mac-address4'), ['str'])),
                                        ('mac_add_blk_size4', (YLeaf(YType.str, 'mac-add-blk-size4'), ['str'])),
                                        ('pcb_serial_num', (YLeaf(YType.str, 'pcb-serial-num'), ['str'])),
                                        ('power_supply_type', (YLeaf(YType.str, 'power-supply-type'), ['str'])),
                                        ('power_consumption', (YLeaf(YType.str, 'power-consumption'), ['str'])),
                                        ('block_signature', (YLeaf(YType.str, 'block-signature'), ['str'])),
                                        ('block_version', (YLeaf(YType.str, 'block-version'), ['str'])),
                                        ('block_length', (YLeaf(YType.str, 'block-length'), ['str'])),
                                        ('block_checksum', (YLeaf(YType.str, 'block-checksum'), ['str'])),
                                        ('eeprom_size', (YLeaf(YType.str, 'eeprom-size'), ['str'])),
                                        ('block_count', (YLeaf(YType.str, 'block-count'), ['str'])),
                                        ('fru_major_type', (YLeaf(YType.str, 'fru-major-type'), ['str'])),
                                        ('fru_minor_type', (YLeaf(YType.str, 'fru-minor-type'), ['str'])),
                                        ('oem_string', (YLeaf(YType.str, 'oem-string'), ['str'])),
                                        ('product_id', (YLeaf(YType.str, 'product-id'), ['str'])),
                                        ('serial_number', (YLeaf(YType.str, 'serial-number'), ['str'])),
                                        ('part_number', (YLeaf(YType.str, 'part-number'), ['str'])),
                                        ('part_revision', (YLeaf(YType.str, 'part-revision'), ['str'])),
                                        ('mfg_deviation', (YLeaf(YType.str, 'mfg-deviation'), ['str'])),
                                        ('hw_version', (YLeaf(YType.str, 'hw-version'), ['str'])),
                                        ('mfg_bits', (YLeaf(YType.str, 'mfg-bits'), ['str'])),
                                        ('engineer_use', (YLeaf(YType.str, 'engineer-use'), ['str'])),
                                        ('snmpoid', (YLeaf(YType.str, 'snmpoid'), ['str'])),
                                        ('rma_code', (YLeaf(YType.str, 'rma-code'), ['str'])),
                                        ('eci_alpha_number', (YLeaf(YType.str, 'eci-alpha-number'), ['str'])),
                                    ])
                                    self.description = None
                                    self.idprom_format_rev = None
                                    self.controller_family = None
                                    self.controller_type = None
                                    self.vid = None
                                    self.hwid = None
                                    self.pid = None
                                    self.udi_description = None
                                    self.udi_name = None
                                    self.clei = None
                                    self.eci = None
                                    self.top_assem_part_num = None
                                    self.top_assem_vid = None
                                    self.pca_num = None
                                    self.pcavid = None
                                    self.chassis_sid = None
                                    self.dev_num1 = None
                                    self.dev_num2 = None
                                    self.dev_num3 = None
                                    self.dev_num4 = None
                                    self.dev_num5 = None
                                    self.dev_num6 = None
                                    self.dev_num7 = None
                                    self.manu_test_data = None
                                    self.asset_id = None
                                    self.asset_alias = None
                                    self.base_mac_address1 = None
                                    self.mac_add_blk_size1 = None
                                    self.base_mac_address2 = None
                                    self.mac_add_blk_size2 = None
                                    self.base_mac_address3 = None
                                    self.mac_add_blk_size3 = None
                                    self.base_mac_address4 = None
                                    self.mac_add_blk_size4 = None
                                    self.pcb_serial_num = None
                                    self.power_supply_type = None
                                    self.power_consumption = None
                                    self.block_signature = None
                                    self.block_version = None
                                    self.block_length = None
                                    self.block_checksum = None
                                    self.eeprom_size = None
                                    self.block_count = None
                                    self.fru_major_type = None
                                    self.fru_minor_type = None
                                    self.oem_string = None
                                    self.product_id = None
                                    self.serial_number = None
                                    self.part_number = None
                                    self.part_revision = None
                                    self.mfg_deviation = None
                                    self.hw_version = None
                                    self.mfg_bits = None
                                    self.engineer_use = None
                                    self.snmpoid = None
                                    self.rma_code = None
                                    self.eci_alpha_number = None

                                    self.rma = Diag.Racks.Rack.FanTrays.FanTray.Fanses.Fans.Information.Rma()
                                    self.rma.parent = self
                                    self._children_name_map["rma"] = "rma"
                                    self._segment_path = lambda: "information"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Diag.Racks.Rack.FanTrays.FanTray.Fanses.Fans.Information, [u'description', u'idprom_format_rev', u'controller_family', u'controller_type', u'vid', u'hwid', u'pid', u'udi_description', u'udi_name', u'clei', u'eci', u'top_assem_part_num', u'top_assem_vid', u'pca_num', u'pcavid', u'chassis_sid', u'dev_num1', u'dev_num2', u'dev_num3', u'dev_num4', u'dev_num5', u'dev_num6', u'dev_num7', u'manu_test_data', u'asset_id', u'asset_alias', u'base_mac_address1', u'mac_add_blk_size1', u'base_mac_address2', u'mac_add_blk_size2', u'base_mac_address3', u'mac_add_blk_size3', u'base_mac_address4', u'mac_add_blk_size4', u'pcb_serial_num', u'power_supply_type', u'power_consumption', u'block_signature', u'block_version', u'block_length', u'block_checksum', u'eeprom_size', u'block_count', u'fru_major_type', u'fru_minor_type', u'oem_string', u'product_id', u'serial_number', u'part_number', u'part_revision', u'mfg_deviation', u'hw_version', u'mfg_bits', u'engineer_use', u'snmpoid', u'rma_code', u'eci_alpha_number'], name, value)


                                class Rma(Entity):
                                    """
                                    RMA Data
                                    
                                    .. attribute:: test_history
                                    
                                    	Test history
                                    	**type**\: str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: rma_number
                                    
                                    	RMA tracking number format is N\-N\-N
                                    	**type**\: str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: rma_history
                                    
                                    	RMA history
                                    	**type**\: str
                                    
                                    	**length:** 0..255
                                    
                                    

                                    """

                                    _prefix = 'sdr-invmgr-diag-oper'
                                    _revision = '2018-01-31'

                                    def __init__(self):
                                        super(Diag.Racks.Rack.FanTrays.FanTray.Fanses.Fans.Information.Rma, self).__init__()

                                        self.yang_name = "rma"
                                        self.yang_parent_name = "information"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('test_history', (YLeaf(YType.str, 'test-history'), ['str'])),
                                            ('rma_number', (YLeaf(YType.str, 'rma-number'), ['str'])),
                                            ('rma_history', (YLeaf(YType.str, 'rma-history'), ['str'])),
                                        ])
                                        self.test_history = None
                                        self.rma_number = None
                                        self.rma_history = None
                                        self._segment_path = lambda: "rma"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Diag.Racks.Rack.FanTrays.FanTray.Fanses.Fans.Information.Rma, [u'test_history', u'rma_number', u'rma_history'], name, value)


            class Slots(Entity):
                """
                Table of slots
                
                .. attribute:: slot
                
                	Slot name
                	**type**\: list of  		 :py:class:`Slot <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sdr_invmgr_diag_oper.Diag.Racks.Rack.Slots.Slot>`
                
                

                """

                _prefix = 'sdr-invmgr-diag-oper'
                _revision = '2018-01-31'

                def __init__(self):
                    super(Diag.Racks.Rack.Slots, self).__init__()

                    self.yang_name = "slots"
                    self.yang_parent_name = "rack"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("slot", ("slot", Diag.Racks.Rack.Slots.Slot))])
                    self._leafs = OrderedDict()

                    self.slot = YList(self)
                    self._segment_path = lambda: "slots"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Diag.Racks.Rack.Slots, [], name, value)


                class Slot(Entity):
                    """
                    Slot name
                    
                    .. attribute:: slot_name  (key)
                    
                    	Slot name
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: instances
                    
                    	Table of instances
                    	**type**\:  :py:class:`Instances <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sdr_invmgr_diag_oper.Diag.Racks.Rack.Slots.Slot.Instances>`
                    
                    

                    """

                    _prefix = 'sdr-invmgr-diag-oper'
                    _revision = '2018-01-31'

                    def __init__(self):
                        super(Diag.Racks.Rack.Slots.Slot, self).__init__()

                        self.yang_name = "slot"
                        self.yang_parent_name = "slots"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['slot_name']
                        self._child_classes = OrderedDict([("instances", ("instances", Diag.Racks.Rack.Slots.Slot.Instances))])
                        self._leafs = OrderedDict([
                            ('slot_name', (YLeaf(YType.str, 'slot-name'), ['str'])),
                        ])
                        self.slot_name = None

                        self.instances = Diag.Racks.Rack.Slots.Slot.Instances()
                        self.instances.parent = self
                        self._children_name_map["instances"] = "instances"
                        self._segment_path = lambda: "slot" + "[slot-name='" + str(self.slot_name) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Diag.Racks.Rack.Slots.Slot, ['slot_name'], name, value)


                    class Instances(Entity):
                        """
                        Table of instances
                        
                        .. attribute:: instance
                        
                        	instance number
                        	**type**\: list of  		 :py:class:`Instance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sdr_invmgr_diag_oper.Diag.Racks.Rack.Slots.Slot.Instances.Instance>`
                        
                        

                        """

                        _prefix = 'sdr-invmgr-diag-oper'
                        _revision = '2018-01-31'

                        def __init__(self):
                            super(Diag.Racks.Rack.Slots.Slot.Instances, self).__init__()

                            self.yang_name = "instances"
                            self.yang_parent_name = "slot"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("instance", ("instance", Diag.Racks.Rack.Slots.Slot.Instances.Instance))])
                            self._leafs = OrderedDict()

                            self.instance = YList(self)
                            self._segment_path = lambda: "instances"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Diag.Racks.Rack.Slots.Slot.Instances, [], name, value)


                        class Instance(Entity):
                            """
                            instance number
                            
                            .. attribute:: name  (key)
                            
                            	Instance name
                            	**type**\: str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            .. attribute:: detail
                            
                            	Detail information
                            	**type**\:  :py:class:`Detail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sdr_invmgr_diag_oper.Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail>`
                            
                            

                            """

                            _prefix = 'sdr-invmgr-diag-oper'
                            _revision = '2018-01-31'

                            def __init__(self):
                                super(Diag.Racks.Rack.Slots.Slot.Instances.Instance, self).__init__()

                                self.yang_name = "instance"
                                self.yang_parent_name = "instances"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['name']
                                self._child_classes = OrderedDict([("detail", ("detail", Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail))])
                                self._leafs = OrderedDict([
                                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                ])
                                self.name = None

                                self.detail = Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail()
                                self.detail.parent = self
                                self._children_name_map["detail"] = "detail"
                                self._segment_path = lambda: "instance" + "[name='" + str(self.name) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Diag.Racks.Rack.Slots.Slot.Instances.Instance, ['name'], name, value)


                            class Detail(Entity):
                                """
                                Detail information
                                
                                .. attribute:: card_instance
                                
                                	Card instance
                                	**type**\:  :py:class:`CardInstance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sdr_invmgr_diag_oper.Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.CardInstance>`
                                
                                .. attribute:: node_operational_state
                                
                                	Node operational state 
                                	**type**\: str
                                
                                	**length:** 0..255
                                
                                

                                """

                                _prefix = 'sdr-invmgr-diag-oper'
                                _revision = '2018-01-31'

                                def __init__(self):
                                    super(Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail, self).__init__()

                                    self.yang_name = "detail"
                                    self.yang_parent_name = "instance"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("card-instance", ("card_instance", Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.CardInstance))])
                                    self._leafs = OrderedDict([
                                        ('node_operational_state', (YLeaf(YType.str, 'node-operational-state'), ['str'])),
                                    ])
                                    self.node_operational_state = None

                                    self.card_instance = Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.CardInstance()
                                    self.card_instance.parent = self
                                    self._children_name_map["card_instance"] = "card-instance"
                                    self._segment_path = lambda: "detail"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail, [u'node_operational_state'], name, value)


                                class CardInstance(Entity):
                                    """
                                    Card instance
                                    
                                    .. attribute:: rma
                                    
                                    	RMA Data
                                    	**type**\:  :py:class:`Rma <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sdr_invmgr_diag_oper.Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.CardInstance.Rma>`
                                    
                                    .. attribute:: description
                                    
                                    	A textual description of physical entity
                                    	**type**\: str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: idprom_format_rev
                                    
                                    	IDPROM Format Revision
                                    	**type**\: str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: controller_family
                                    
                                    	Controller family
                                    	**type**\: str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: controller_type
                                    
                                    	Controller type
                                    	**type**\: str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: vid
                                    
                                    	Version ID
                                    	**type**\: str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: hwid
                                    
                                    	Hardware Revision
                                    	**type**\: str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: pid
                                    
                                    	Product ID
                                    	**type**\: str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: udi_description
                                    
                                    	UDI description
                                    	**type**\: str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: udi_name
                                    
                                    	UDI name
                                    	**type**\: str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: clei
                                    
                                    	Common Language Equipment Identifier (CLEI) code
                                    	**type**\: str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: eci
                                    
                                    	Equipment Catalog Item (ECI) number
                                    	**type**\: str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: top_assem_part_num
                                    
                                    	Top assembly part number
                                    	**type**\: str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: top_assem_vid
                                    
                                    	Top assembly revision number
                                    	**type**\: str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: pca_num
                                    
                                    	PCA number
                                    	**type**\: str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: pcavid
                                    
                                    	PCA revision ID
                                    	**type**\: str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: chassis_sid
                                    
                                    	Chassis serial number
                                    	**type**\: str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: dev_num1
                                    
                                    	Deviation Number # 1
                                    	**type**\: str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: dev_num2
                                    
                                    	Deviation Number # 2
                                    	**type**\: str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: dev_num3
                                    
                                    	Deviation Number # 3
                                    	**type**\: str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: dev_num4
                                    
                                    	Deviation Number # 4
                                    	**type**\: str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: dev_num5
                                    
                                    	Deviation Number # 5
                                    	**type**\: str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: dev_num6
                                    
                                    	Deviation Number # 6
                                    	**type**\: str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: dev_num7
                                    
                                    	Deviation Number # 7
                                    	**type**\: str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: manu_test_data
                                    
                                    	Manufacturing Test Data
                                    	**type**\: str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: asset_id
                                    
                                    	Asset ID
                                    	**type**\: str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: asset_alias
                                    
                                    	Asset Alias
                                    	**type**\: str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: base_mac_address1
                                    
                                    	Base Mac Address #1
                                    	**type**\: str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: mac_add_blk_size1
                                    
                                    	Mac Address Block Size #1
                                    	**type**\: str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: base_mac_address2
                                    
                                    	Base Mac Address #2
                                    	**type**\: str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: mac_add_blk_size2
                                    
                                    	Mac Address Block Size #2
                                    	**type**\: str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: base_mac_address3
                                    
                                    	Base Mac Address #3
                                    	**type**\: str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: mac_add_blk_size3
                                    
                                    	Mac Address Block Size #3
                                    	**type**\: str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: base_mac_address4
                                    
                                    	Base Mac Address #4
                                    	**type**\: str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: mac_add_blk_size4
                                    
                                    	Mac Address Block Size #4
                                    	**type**\: str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: pcb_serial_num
                                    
                                    	PCB Serial Number
                                    	**type**\: str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: power_supply_type
                                    
                                    	Power Supply Type
                                    	**type**\: str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: power_consumption
                                    
                                    	Power Consumption
                                    	**type**\: str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: block_signature
                                    
                                    	Block Signature
                                    	**type**\: str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: block_version
                                    
                                    	Block Version
                                    	**type**\: str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: block_length
                                    
                                    	Block Length
                                    	**type**\: str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: block_checksum
                                    
                                    	Block Checksum
                                    	**type**\: str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: eeprom_size
                                    
                                    	EEPROM Size
                                    	**type**\: str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: block_count
                                    
                                    	Block Count
                                    	**type**\: str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: fru_major_type
                                    
                                    	FRU Major Type
                                    	**type**\: str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: fru_minor_type
                                    
                                    	FRU Minor Type
                                    	**type**\: str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: oem_string
                                    
                                    	OEM String
                                    	**type**\: str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: product_id
                                    
                                    	Product ID
                                    	**type**\: str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: serial_number
                                    
                                    	Serial Number
                                    	**type**\: str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: part_number
                                    
                                    	Part Number
                                    	**type**\: str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: part_revision
                                    
                                    	Part Revision
                                    	**type**\: str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: mfg_deviation
                                    
                                    	MFG Deviation
                                    	**type**\: str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: hw_version
                                    
                                    	Hardware Version
                                    	**type**\: str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: mfg_bits
                                    
                                    	MFG Bits
                                    	**type**\: str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: engineer_use
                                    
                                    	Engineer Use
                                    	**type**\: str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: snmpoid
                                    
                                    	SNMP OID
                                    	**type**\: str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: rma_code
                                    
                                    	RMA Code
                                    	**type**\: str
                                    
                                    	**length:** 0..255
                                    
                                    .. attribute:: eci_alpha_number
                                    
                                    	AlphaNumeric Equipment Catalog Item (ECI) number
                                    	**type**\: str
                                    
                                    	**length:** 0..255
                                    
                                    

                                    """

                                    _prefix = 'sdr-invmgr-diag-oper'
                                    _revision = '2018-01-31'

                                    def __init__(self):
                                        super(Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.CardInstance, self).__init__()

                                        self.yang_name = "card-instance"
                                        self.yang_parent_name = "detail"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("rma", ("rma", Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.CardInstance.Rma))])
                                        self._leafs = OrderedDict([
                                            ('description', (YLeaf(YType.str, 'description'), ['str'])),
                                            ('idprom_format_rev', (YLeaf(YType.str, 'idprom-format-rev'), ['str'])),
                                            ('controller_family', (YLeaf(YType.str, 'controller-family'), ['str'])),
                                            ('controller_type', (YLeaf(YType.str, 'controller-type'), ['str'])),
                                            ('vid', (YLeaf(YType.str, 'vid'), ['str'])),
                                            ('hwid', (YLeaf(YType.str, 'hwid'), ['str'])),
                                            ('pid', (YLeaf(YType.str, 'pid'), ['str'])),
                                            ('udi_description', (YLeaf(YType.str, 'udi-description'), ['str'])),
                                            ('udi_name', (YLeaf(YType.str, 'udi-name'), ['str'])),
                                            ('clei', (YLeaf(YType.str, 'clei'), ['str'])),
                                            ('eci', (YLeaf(YType.str, 'eci'), ['str'])),
                                            ('top_assem_part_num', (YLeaf(YType.str, 'top-assem-part-num'), ['str'])),
                                            ('top_assem_vid', (YLeaf(YType.str, 'top-assem-vid'), ['str'])),
                                            ('pca_num', (YLeaf(YType.str, 'pca-num'), ['str'])),
                                            ('pcavid', (YLeaf(YType.str, 'pcavid'), ['str'])),
                                            ('chassis_sid', (YLeaf(YType.str, 'chassis-sid'), ['str'])),
                                            ('dev_num1', (YLeaf(YType.str, 'dev-num1'), ['str'])),
                                            ('dev_num2', (YLeaf(YType.str, 'dev-num2'), ['str'])),
                                            ('dev_num3', (YLeaf(YType.str, 'dev-num3'), ['str'])),
                                            ('dev_num4', (YLeaf(YType.str, 'dev-num4'), ['str'])),
                                            ('dev_num5', (YLeaf(YType.str, 'dev-num5'), ['str'])),
                                            ('dev_num6', (YLeaf(YType.str, 'dev-num6'), ['str'])),
                                            ('dev_num7', (YLeaf(YType.str, 'dev-num7'), ['str'])),
                                            ('manu_test_data', (YLeaf(YType.str, 'manu-test-data'), ['str'])),
                                            ('asset_id', (YLeaf(YType.str, 'asset-id'), ['str'])),
                                            ('asset_alias', (YLeaf(YType.str, 'asset-alias'), ['str'])),
                                            ('base_mac_address1', (YLeaf(YType.str, 'base-mac-address1'), ['str'])),
                                            ('mac_add_blk_size1', (YLeaf(YType.str, 'mac-add-blk-size1'), ['str'])),
                                            ('base_mac_address2', (YLeaf(YType.str, 'base-mac-address2'), ['str'])),
                                            ('mac_add_blk_size2', (YLeaf(YType.str, 'mac-add-blk-size2'), ['str'])),
                                            ('base_mac_address3', (YLeaf(YType.str, 'base-mac-address3'), ['str'])),
                                            ('mac_add_blk_size3', (YLeaf(YType.str, 'mac-add-blk-size3'), ['str'])),
                                            ('base_mac_address4', (YLeaf(YType.str, 'base-mac-address4'), ['str'])),
                                            ('mac_add_blk_size4', (YLeaf(YType.str, 'mac-add-blk-size4'), ['str'])),
                                            ('pcb_serial_num', (YLeaf(YType.str, 'pcb-serial-num'), ['str'])),
                                            ('power_supply_type', (YLeaf(YType.str, 'power-supply-type'), ['str'])),
                                            ('power_consumption', (YLeaf(YType.str, 'power-consumption'), ['str'])),
                                            ('block_signature', (YLeaf(YType.str, 'block-signature'), ['str'])),
                                            ('block_version', (YLeaf(YType.str, 'block-version'), ['str'])),
                                            ('block_length', (YLeaf(YType.str, 'block-length'), ['str'])),
                                            ('block_checksum', (YLeaf(YType.str, 'block-checksum'), ['str'])),
                                            ('eeprom_size', (YLeaf(YType.str, 'eeprom-size'), ['str'])),
                                            ('block_count', (YLeaf(YType.str, 'block-count'), ['str'])),
                                            ('fru_major_type', (YLeaf(YType.str, 'fru-major-type'), ['str'])),
                                            ('fru_minor_type', (YLeaf(YType.str, 'fru-minor-type'), ['str'])),
                                            ('oem_string', (YLeaf(YType.str, 'oem-string'), ['str'])),
                                            ('product_id', (YLeaf(YType.str, 'product-id'), ['str'])),
                                            ('serial_number', (YLeaf(YType.str, 'serial-number'), ['str'])),
                                            ('part_number', (YLeaf(YType.str, 'part-number'), ['str'])),
                                            ('part_revision', (YLeaf(YType.str, 'part-revision'), ['str'])),
                                            ('mfg_deviation', (YLeaf(YType.str, 'mfg-deviation'), ['str'])),
                                            ('hw_version', (YLeaf(YType.str, 'hw-version'), ['str'])),
                                            ('mfg_bits', (YLeaf(YType.str, 'mfg-bits'), ['str'])),
                                            ('engineer_use', (YLeaf(YType.str, 'engineer-use'), ['str'])),
                                            ('snmpoid', (YLeaf(YType.str, 'snmpoid'), ['str'])),
                                            ('rma_code', (YLeaf(YType.str, 'rma-code'), ['str'])),
                                            ('eci_alpha_number', (YLeaf(YType.str, 'eci-alpha-number'), ['str'])),
                                        ])
                                        self.description = None
                                        self.idprom_format_rev = None
                                        self.controller_family = None
                                        self.controller_type = None
                                        self.vid = None
                                        self.hwid = None
                                        self.pid = None
                                        self.udi_description = None
                                        self.udi_name = None
                                        self.clei = None
                                        self.eci = None
                                        self.top_assem_part_num = None
                                        self.top_assem_vid = None
                                        self.pca_num = None
                                        self.pcavid = None
                                        self.chassis_sid = None
                                        self.dev_num1 = None
                                        self.dev_num2 = None
                                        self.dev_num3 = None
                                        self.dev_num4 = None
                                        self.dev_num5 = None
                                        self.dev_num6 = None
                                        self.dev_num7 = None
                                        self.manu_test_data = None
                                        self.asset_id = None
                                        self.asset_alias = None
                                        self.base_mac_address1 = None
                                        self.mac_add_blk_size1 = None
                                        self.base_mac_address2 = None
                                        self.mac_add_blk_size2 = None
                                        self.base_mac_address3 = None
                                        self.mac_add_blk_size3 = None
                                        self.base_mac_address4 = None
                                        self.mac_add_blk_size4 = None
                                        self.pcb_serial_num = None
                                        self.power_supply_type = None
                                        self.power_consumption = None
                                        self.block_signature = None
                                        self.block_version = None
                                        self.block_length = None
                                        self.block_checksum = None
                                        self.eeprom_size = None
                                        self.block_count = None
                                        self.fru_major_type = None
                                        self.fru_minor_type = None
                                        self.oem_string = None
                                        self.product_id = None
                                        self.serial_number = None
                                        self.part_number = None
                                        self.part_revision = None
                                        self.mfg_deviation = None
                                        self.hw_version = None
                                        self.mfg_bits = None
                                        self.engineer_use = None
                                        self.snmpoid = None
                                        self.rma_code = None
                                        self.eci_alpha_number = None

                                        self.rma = Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.CardInstance.Rma()
                                        self.rma.parent = self
                                        self._children_name_map["rma"] = "rma"
                                        self._segment_path = lambda: "card-instance"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.CardInstance, [u'description', u'idprom_format_rev', u'controller_family', u'controller_type', u'vid', u'hwid', u'pid', u'udi_description', u'udi_name', u'clei', u'eci', u'top_assem_part_num', u'top_assem_vid', u'pca_num', u'pcavid', u'chassis_sid', u'dev_num1', u'dev_num2', u'dev_num3', u'dev_num4', u'dev_num5', u'dev_num6', u'dev_num7', u'manu_test_data', u'asset_id', u'asset_alias', u'base_mac_address1', u'mac_add_blk_size1', u'base_mac_address2', u'mac_add_blk_size2', u'base_mac_address3', u'mac_add_blk_size3', u'base_mac_address4', u'mac_add_blk_size4', u'pcb_serial_num', u'power_supply_type', u'power_consumption', u'block_signature', u'block_version', u'block_length', u'block_checksum', u'eeprom_size', u'block_count', u'fru_major_type', u'fru_minor_type', u'oem_string', u'product_id', u'serial_number', u'part_number', u'part_revision', u'mfg_deviation', u'hw_version', u'mfg_bits', u'engineer_use', u'snmpoid', u'rma_code', u'eci_alpha_number'], name, value)


                                    class Rma(Entity):
                                        """
                                        RMA Data
                                        
                                        .. attribute:: test_history
                                        
                                        	Test history
                                        	**type**\: str
                                        
                                        	**length:** 0..255
                                        
                                        .. attribute:: rma_number
                                        
                                        	RMA tracking number format is N\-N\-N
                                        	**type**\: str
                                        
                                        	**length:** 0..255
                                        
                                        .. attribute:: rma_history
                                        
                                        	RMA history
                                        	**type**\: str
                                        
                                        	**length:** 0..255
                                        
                                        

                                        """

                                        _prefix = 'sdr-invmgr-diag-oper'
                                        _revision = '2018-01-31'

                                        def __init__(self):
                                            super(Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.CardInstance.Rma, self).__init__()

                                            self.yang_name = "rma"
                                            self.yang_parent_name = "card-instance"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('test_history', (YLeaf(YType.str, 'test-history'), ['str'])),
                                                ('rma_number', (YLeaf(YType.str, 'rma-number'), ['str'])),
                                                ('rma_history', (YLeaf(YType.str, 'rma-history'), ['str'])),
                                            ])
                                            self.test_history = None
                                            self.rma_number = None
                                            self.rma_history = None
                                            self._segment_path = lambda: "rma"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.CardInstance.Rma, [u'test_history', u'rma_number', u'rma_history'], name, value)


            class Chassis(Entity):
                """
                Chassis information
                
                .. attribute:: rma
                
                	RMA Data
                	**type**\:  :py:class:`Rma <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sdr_invmgr_diag_oper.Diag.Racks.Rack.Chassis.Rma>`
                
                .. attribute:: description
                
                	A textual description of physical entity
                	**type**\: str
                
                	**length:** 0..255
                
                .. attribute:: idprom_format_rev
                
                	IDPROM Format Revision
                	**type**\: str
                
                	**length:** 0..255
                
                .. attribute:: controller_family
                
                	Controller family
                	**type**\: str
                
                	**length:** 0..255
                
                .. attribute:: controller_type
                
                	Controller type
                	**type**\: str
                
                	**length:** 0..255
                
                .. attribute:: vid
                
                	Version ID
                	**type**\: str
                
                	**length:** 0..255
                
                .. attribute:: hwid
                
                	Hardware Revision
                	**type**\: str
                
                	**length:** 0..255
                
                .. attribute:: pid
                
                	Product ID
                	**type**\: str
                
                	**length:** 0..255
                
                .. attribute:: udi_description
                
                	UDI description
                	**type**\: str
                
                	**length:** 0..255
                
                .. attribute:: udi_name
                
                	UDI name
                	**type**\: str
                
                	**length:** 0..255
                
                .. attribute:: clei
                
                	Common Language Equipment Identifier (CLEI) code
                	**type**\: str
                
                	**length:** 0..255
                
                .. attribute:: eci
                
                	Equipment Catalog Item (ECI) number
                	**type**\: str
                
                	**length:** 0..255
                
                .. attribute:: top_assem_part_num
                
                	Top assembly part number
                	**type**\: str
                
                	**length:** 0..255
                
                .. attribute:: top_assem_vid
                
                	Top assembly revision number
                	**type**\: str
                
                	**length:** 0..255
                
                .. attribute:: pca_num
                
                	PCA number
                	**type**\: str
                
                	**length:** 0..255
                
                .. attribute:: pcavid
                
                	PCA revision ID
                	**type**\: str
                
                	**length:** 0..255
                
                .. attribute:: chassis_sid
                
                	Chassis serial number
                	**type**\: str
                
                	**length:** 0..255
                
                .. attribute:: dev_num1
                
                	Deviation Number # 1
                	**type**\: str
                
                	**length:** 0..255
                
                .. attribute:: dev_num2
                
                	Deviation Number # 2
                	**type**\: str
                
                	**length:** 0..255
                
                .. attribute:: dev_num3
                
                	Deviation Number # 3
                	**type**\: str
                
                	**length:** 0..255
                
                .. attribute:: dev_num4
                
                	Deviation Number # 4
                	**type**\: str
                
                	**length:** 0..255
                
                .. attribute:: dev_num5
                
                	Deviation Number # 5
                	**type**\: str
                
                	**length:** 0..255
                
                .. attribute:: dev_num6
                
                	Deviation Number # 6
                	**type**\: str
                
                	**length:** 0..255
                
                .. attribute:: dev_num7
                
                	Deviation Number # 7
                	**type**\: str
                
                	**length:** 0..255
                
                .. attribute:: manu_test_data
                
                	Manufacturing Test Data
                	**type**\: str
                
                	**length:** 0..255
                
                .. attribute:: asset_id
                
                	Asset ID
                	**type**\: str
                
                	**length:** 0..255
                
                .. attribute:: asset_alias
                
                	Asset Alias
                	**type**\: str
                
                	**length:** 0..255
                
                .. attribute:: base_mac_address1
                
                	Base Mac Address #1
                	**type**\: str
                
                	**length:** 0..255
                
                .. attribute:: mac_add_blk_size1
                
                	Mac Address Block Size #1
                	**type**\: str
                
                	**length:** 0..255
                
                .. attribute:: base_mac_address2
                
                	Base Mac Address #2
                	**type**\: str
                
                	**length:** 0..255
                
                .. attribute:: mac_add_blk_size2
                
                	Mac Address Block Size #2
                	**type**\: str
                
                	**length:** 0..255
                
                .. attribute:: base_mac_address3
                
                	Base Mac Address #3
                	**type**\: str
                
                	**length:** 0..255
                
                .. attribute:: mac_add_blk_size3
                
                	Mac Address Block Size #3
                	**type**\: str
                
                	**length:** 0..255
                
                .. attribute:: base_mac_address4
                
                	Base Mac Address #4
                	**type**\: str
                
                	**length:** 0..255
                
                .. attribute:: mac_add_blk_size4
                
                	Mac Address Block Size #4
                	**type**\: str
                
                	**length:** 0..255
                
                .. attribute:: pcb_serial_num
                
                	PCB Serial Number
                	**type**\: str
                
                	**length:** 0..255
                
                .. attribute:: power_supply_type
                
                	Power Supply Type
                	**type**\: str
                
                	**length:** 0..255
                
                .. attribute:: power_consumption
                
                	Power Consumption
                	**type**\: str
                
                	**length:** 0..255
                
                .. attribute:: block_signature
                
                	Block Signature
                	**type**\: str
                
                	**length:** 0..255
                
                .. attribute:: block_version
                
                	Block Version
                	**type**\: str
                
                	**length:** 0..255
                
                .. attribute:: block_length
                
                	Block Length
                	**type**\: str
                
                	**length:** 0..255
                
                .. attribute:: block_checksum
                
                	Block Checksum
                	**type**\: str
                
                	**length:** 0..255
                
                .. attribute:: eeprom_size
                
                	EEPROM Size
                	**type**\: str
                
                	**length:** 0..255
                
                .. attribute:: block_count
                
                	Block Count
                	**type**\: str
                
                	**length:** 0..255
                
                .. attribute:: fru_major_type
                
                	FRU Major Type
                	**type**\: str
                
                	**length:** 0..255
                
                .. attribute:: fru_minor_type
                
                	FRU Minor Type
                	**type**\: str
                
                	**length:** 0..255
                
                .. attribute:: oem_string
                
                	OEM String
                	**type**\: str
                
                	**length:** 0..255
                
                .. attribute:: product_id
                
                	Product ID
                	**type**\: str
                
                	**length:** 0..255
                
                .. attribute:: serial_number
                
                	Serial Number
                	**type**\: str
                
                	**length:** 0..255
                
                .. attribute:: part_number
                
                	Part Number
                	**type**\: str
                
                	**length:** 0..255
                
                .. attribute:: part_revision
                
                	Part Revision
                	**type**\: str
                
                	**length:** 0..255
                
                .. attribute:: mfg_deviation
                
                	MFG Deviation
                	**type**\: str
                
                	**length:** 0..255
                
                .. attribute:: hw_version
                
                	Hardware Version
                	**type**\: str
                
                	**length:** 0..255
                
                .. attribute:: mfg_bits
                
                	MFG Bits
                	**type**\: str
                
                	**length:** 0..255
                
                .. attribute:: engineer_use
                
                	Engineer Use
                	**type**\: str
                
                	**length:** 0..255
                
                .. attribute:: snmpoid
                
                	SNMP OID
                	**type**\: str
                
                	**length:** 0..255
                
                .. attribute:: rma_code
                
                	RMA Code
                	**type**\: str
                
                	**length:** 0..255
                
                .. attribute:: eci_alpha_number
                
                	AlphaNumeric Equipment Catalog Item (ECI) number
                	**type**\: str
                
                	**length:** 0..255
                
                

                """

                _prefix = 'sdr-invmgr-diag-oper'
                _revision = '2018-01-31'

                def __init__(self):
                    super(Diag.Racks.Rack.Chassis, self).__init__()

                    self.yang_name = "chassis"
                    self.yang_parent_name = "rack"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("rma", ("rma", Diag.Racks.Rack.Chassis.Rma))])
                    self._leafs = OrderedDict([
                        ('description', (YLeaf(YType.str, 'description'), ['str'])),
                        ('idprom_format_rev', (YLeaf(YType.str, 'idprom-format-rev'), ['str'])),
                        ('controller_family', (YLeaf(YType.str, 'controller-family'), ['str'])),
                        ('controller_type', (YLeaf(YType.str, 'controller-type'), ['str'])),
                        ('vid', (YLeaf(YType.str, 'vid'), ['str'])),
                        ('hwid', (YLeaf(YType.str, 'hwid'), ['str'])),
                        ('pid', (YLeaf(YType.str, 'pid'), ['str'])),
                        ('udi_description', (YLeaf(YType.str, 'udi-description'), ['str'])),
                        ('udi_name', (YLeaf(YType.str, 'udi-name'), ['str'])),
                        ('clei', (YLeaf(YType.str, 'clei'), ['str'])),
                        ('eci', (YLeaf(YType.str, 'eci'), ['str'])),
                        ('top_assem_part_num', (YLeaf(YType.str, 'top-assem-part-num'), ['str'])),
                        ('top_assem_vid', (YLeaf(YType.str, 'top-assem-vid'), ['str'])),
                        ('pca_num', (YLeaf(YType.str, 'pca-num'), ['str'])),
                        ('pcavid', (YLeaf(YType.str, 'pcavid'), ['str'])),
                        ('chassis_sid', (YLeaf(YType.str, 'chassis-sid'), ['str'])),
                        ('dev_num1', (YLeaf(YType.str, 'dev-num1'), ['str'])),
                        ('dev_num2', (YLeaf(YType.str, 'dev-num2'), ['str'])),
                        ('dev_num3', (YLeaf(YType.str, 'dev-num3'), ['str'])),
                        ('dev_num4', (YLeaf(YType.str, 'dev-num4'), ['str'])),
                        ('dev_num5', (YLeaf(YType.str, 'dev-num5'), ['str'])),
                        ('dev_num6', (YLeaf(YType.str, 'dev-num6'), ['str'])),
                        ('dev_num7', (YLeaf(YType.str, 'dev-num7'), ['str'])),
                        ('manu_test_data', (YLeaf(YType.str, 'manu-test-data'), ['str'])),
                        ('asset_id', (YLeaf(YType.str, 'asset-id'), ['str'])),
                        ('asset_alias', (YLeaf(YType.str, 'asset-alias'), ['str'])),
                        ('base_mac_address1', (YLeaf(YType.str, 'base-mac-address1'), ['str'])),
                        ('mac_add_blk_size1', (YLeaf(YType.str, 'mac-add-blk-size1'), ['str'])),
                        ('base_mac_address2', (YLeaf(YType.str, 'base-mac-address2'), ['str'])),
                        ('mac_add_blk_size2', (YLeaf(YType.str, 'mac-add-blk-size2'), ['str'])),
                        ('base_mac_address3', (YLeaf(YType.str, 'base-mac-address3'), ['str'])),
                        ('mac_add_blk_size3', (YLeaf(YType.str, 'mac-add-blk-size3'), ['str'])),
                        ('base_mac_address4', (YLeaf(YType.str, 'base-mac-address4'), ['str'])),
                        ('mac_add_blk_size4', (YLeaf(YType.str, 'mac-add-blk-size4'), ['str'])),
                        ('pcb_serial_num', (YLeaf(YType.str, 'pcb-serial-num'), ['str'])),
                        ('power_supply_type', (YLeaf(YType.str, 'power-supply-type'), ['str'])),
                        ('power_consumption', (YLeaf(YType.str, 'power-consumption'), ['str'])),
                        ('block_signature', (YLeaf(YType.str, 'block-signature'), ['str'])),
                        ('block_version', (YLeaf(YType.str, 'block-version'), ['str'])),
                        ('block_length', (YLeaf(YType.str, 'block-length'), ['str'])),
                        ('block_checksum', (YLeaf(YType.str, 'block-checksum'), ['str'])),
                        ('eeprom_size', (YLeaf(YType.str, 'eeprom-size'), ['str'])),
                        ('block_count', (YLeaf(YType.str, 'block-count'), ['str'])),
                        ('fru_major_type', (YLeaf(YType.str, 'fru-major-type'), ['str'])),
                        ('fru_minor_type', (YLeaf(YType.str, 'fru-minor-type'), ['str'])),
                        ('oem_string', (YLeaf(YType.str, 'oem-string'), ['str'])),
                        ('product_id', (YLeaf(YType.str, 'product-id'), ['str'])),
                        ('serial_number', (YLeaf(YType.str, 'serial-number'), ['str'])),
                        ('part_number', (YLeaf(YType.str, 'part-number'), ['str'])),
                        ('part_revision', (YLeaf(YType.str, 'part-revision'), ['str'])),
                        ('mfg_deviation', (YLeaf(YType.str, 'mfg-deviation'), ['str'])),
                        ('hw_version', (YLeaf(YType.str, 'hw-version'), ['str'])),
                        ('mfg_bits', (YLeaf(YType.str, 'mfg-bits'), ['str'])),
                        ('engineer_use', (YLeaf(YType.str, 'engineer-use'), ['str'])),
                        ('snmpoid', (YLeaf(YType.str, 'snmpoid'), ['str'])),
                        ('rma_code', (YLeaf(YType.str, 'rma-code'), ['str'])),
                        ('eci_alpha_number', (YLeaf(YType.str, 'eci-alpha-number'), ['str'])),
                    ])
                    self.description = None
                    self.idprom_format_rev = None
                    self.controller_family = None
                    self.controller_type = None
                    self.vid = None
                    self.hwid = None
                    self.pid = None
                    self.udi_description = None
                    self.udi_name = None
                    self.clei = None
                    self.eci = None
                    self.top_assem_part_num = None
                    self.top_assem_vid = None
                    self.pca_num = None
                    self.pcavid = None
                    self.chassis_sid = None
                    self.dev_num1 = None
                    self.dev_num2 = None
                    self.dev_num3 = None
                    self.dev_num4 = None
                    self.dev_num5 = None
                    self.dev_num6 = None
                    self.dev_num7 = None
                    self.manu_test_data = None
                    self.asset_id = None
                    self.asset_alias = None
                    self.base_mac_address1 = None
                    self.mac_add_blk_size1 = None
                    self.base_mac_address2 = None
                    self.mac_add_blk_size2 = None
                    self.base_mac_address3 = None
                    self.mac_add_blk_size3 = None
                    self.base_mac_address4 = None
                    self.mac_add_blk_size4 = None
                    self.pcb_serial_num = None
                    self.power_supply_type = None
                    self.power_consumption = None
                    self.block_signature = None
                    self.block_version = None
                    self.block_length = None
                    self.block_checksum = None
                    self.eeprom_size = None
                    self.block_count = None
                    self.fru_major_type = None
                    self.fru_minor_type = None
                    self.oem_string = None
                    self.product_id = None
                    self.serial_number = None
                    self.part_number = None
                    self.part_revision = None
                    self.mfg_deviation = None
                    self.hw_version = None
                    self.mfg_bits = None
                    self.engineer_use = None
                    self.snmpoid = None
                    self.rma_code = None
                    self.eci_alpha_number = None

                    self.rma = Diag.Racks.Rack.Chassis.Rma()
                    self.rma.parent = self
                    self._children_name_map["rma"] = "rma"
                    self._segment_path = lambda: "chassis"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Diag.Racks.Rack.Chassis, [u'description', u'idprom_format_rev', u'controller_family', u'controller_type', u'vid', u'hwid', u'pid', u'udi_description', u'udi_name', u'clei', u'eci', u'top_assem_part_num', u'top_assem_vid', u'pca_num', u'pcavid', u'chassis_sid', u'dev_num1', u'dev_num2', u'dev_num3', u'dev_num4', u'dev_num5', u'dev_num6', u'dev_num7', u'manu_test_data', u'asset_id', u'asset_alias', u'base_mac_address1', u'mac_add_blk_size1', u'base_mac_address2', u'mac_add_blk_size2', u'base_mac_address3', u'mac_add_blk_size3', u'base_mac_address4', u'mac_add_blk_size4', u'pcb_serial_num', u'power_supply_type', u'power_consumption', u'block_signature', u'block_version', u'block_length', u'block_checksum', u'eeprom_size', u'block_count', u'fru_major_type', u'fru_minor_type', u'oem_string', u'product_id', u'serial_number', u'part_number', u'part_revision', u'mfg_deviation', u'hw_version', u'mfg_bits', u'engineer_use', u'snmpoid', u'rma_code', u'eci_alpha_number'], name, value)


                class Rma(Entity):
                    """
                    RMA Data
                    
                    .. attribute:: test_history
                    
                    	Test history
                    	**type**\: str
                    
                    	**length:** 0..255
                    
                    .. attribute:: rma_number
                    
                    	RMA tracking number format is N\-N\-N
                    	**type**\: str
                    
                    	**length:** 0..255
                    
                    .. attribute:: rma_history
                    
                    	RMA history
                    	**type**\: str
                    
                    	**length:** 0..255
                    
                    

                    """

                    _prefix = 'sdr-invmgr-diag-oper'
                    _revision = '2018-01-31'

                    def __init__(self):
                        super(Diag.Racks.Rack.Chassis.Rma, self).__init__()

                        self.yang_name = "rma"
                        self.yang_parent_name = "chassis"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('test_history', (YLeaf(YType.str, 'test-history'), ['str'])),
                            ('rma_number', (YLeaf(YType.str, 'rma-number'), ['str'])),
                            ('rma_history', (YLeaf(YType.str, 'rma-history'), ['str'])),
                        ])
                        self.test_history = None
                        self.rma_number = None
                        self.rma_history = None
                        self._segment_path = lambda: "rma"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Diag.Racks.Rack.Chassis.Rma, [u'test_history', u'rma_number', u'rma_history'], name, value)

    def clone_ptr(self):
        self._top_entity = Diag()
        return self._top_entity

