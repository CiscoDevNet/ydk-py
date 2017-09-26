""" Cisco_IOS_XR_sdr_invmgr_diag_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR sdr\-invmgr\-diag package operational data.

This module contains definitions
for the following management objects\:
  diag\: Diag information

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
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
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"racks" : ("racks", Diag.Racks)}
        self._child_list_classes = {}

        self.racks = Diag.Racks()
        self.racks.parent = self
        self._children_name_map["racks"] = "racks"
        self._children_yang_names.add("racks")
        self._segment_path = lambda: "Cisco-IOS-XR-sdr-invmgr-diag-oper:diag"


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
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"rack" : ("rack", Diag.Racks.Rack)}

            self.rack = YList(self)
            self._segment_path = lambda: "racks"
            self._absolute_path = lambda: "Cisco-IOS-XR-sdr-invmgr-diag-oper:diag/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Diag.Racks, [], name, value)


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
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"chassis" : ("chassis", Diag.Racks.Rack.Chassis), "fan-traies" : ("fan_traies", Diag.Racks.Rack.FanTraies), "power-shelfs" : ("power_shelfs", Diag.Racks.Rack.PowerShelfs), "slots" : ("slots", Diag.Racks.Rack.Slots)}
                self._child_list_classes = {}

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
                self._segment_path = lambda: "rack" + "[rack-name='" + self.rack_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-sdr-invmgr-diag-oper:diag/racks/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Diag.Racks.Rack, ['rack_name'], name, value)


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
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"rma" : ("rma", Diag.Racks.Rack.Chassis.Rma)}
                    self._child_list_classes = {}

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
                    self._segment_path = lambda: "chassis"

                def __setattr__(self, name, value):
                    self._perform_setattr(Diag.Racks.Rack.Chassis, ['asset_alias', 'asset_id', 'base_mac_address1', 'base_mac_address2', 'base_mac_address3', 'base_mac_address4', 'block_checksum', 'block_count', 'block_length', 'block_signature', 'block_version', 'chassis_sid', 'clei', 'controller_family', 'controller_type', 'description', 'dev_num1', 'dev_num2', 'dev_num3', 'dev_num4', 'dev_num5', 'dev_num6', 'dev_num7', 'eci', 'eeprom_size', 'engineer_use', 'fru_major_type', 'fru_minor_type', 'hw_version', 'hwid', 'idprom_format_rev', 'mac_add_blk_size1', 'mac_add_blk_size2', 'mac_add_blk_size3', 'mac_add_blk_size4', 'manu_test_data', 'mfg_bits', 'mfg_deviation', 'oem_string', 'part_number', 'part_revision', 'pca_num', 'pcavid', 'pcb_serial_num', 'pid', 'power_consumption', 'power_supply_type', 'product_id', 'rma_code', 'serial_number', 'snmpoid', 'top_assem_part_num', 'top_assem_vid', 'udi_description', 'udi_name', 'vid'], name, value)


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
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.rma_history = YLeaf(YType.str, "rma-history")

                        self.rma_number = YLeaf(YType.str, "rma-number")

                        self.test_history = YLeaf(YType.str, "test-history")
                        self._segment_path = lambda: "rma"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Diag.Racks.Rack.Chassis.Rma, ['rma_history', 'rma_number', 'test_history'], name, value)


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
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"fan-tray" : ("fan_tray", Diag.Racks.Rack.FanTraies.FanTray)}

                    self.fan_tray = YList(self)
                    self._segment_path = lambda: "fan-traies"

                def __setattr__(self, name, value):
                    self._perform_setattr(Diag.Racks.Rack.FanTraies, [], name, value)


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
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"fanses" : ("fanses", Diag.Racks.Rack.FanTraies.FanTray.Fanses)}
                        self._child_list_classes = {}

                        self.fan_tray_name = YLeaf(YType.str, "fan-tray-name")

                        self.fanses = Diag.Racks.Rack.FanTraies.FanTray.Fanses()
                        self.fanses.parent = self
                        self._children_name_map["fanses"] = "fanses"
                        self._children_yang_names.add("fanses")
                        self._segment_path = lambda: "fan-tray" + "[fan-tray-name='" + self.fan_tray_name.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Diag.Racks.Rack.FanTraies.FanTray, ['fan_tray_name'], name, value)


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
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"fans" : ("fans", Diag.Racks.Rack.FanTraies.FanTray.Fanses.Fans)}

                            self.fans = YList(self)
                            self._segment_path = lambda: "fanses"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Diag.Racks.Rack.FanTraies.FanTray.Fanses, [], name, value)


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
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"information" : ("information", Diag.Racks.Rack.FanTraies.FanTray.Fanses.Fans.Information)}
                                self._child_list_classes = {}

                                self.fans_name = YLeaf(YType.str, "fans-name")

                                self.information = Diag.Racks.Rack.FanTraies.FanTray.Fanses.Fans.Information()
                                self.information.parent = self
                                self._children_name_map["information"] = "information"
                                self._children_yang_names.add("information")
                                self._segment_path = lambda: "fans" + "[fans-name='" + self.fans_name.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Diag.Racks.Rack.FanTraies.FanTray.Fanses.Fans, ['fans_name'], name, value)


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
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {"rma" : ("rma", Diag.Racks.Rack.FanTraies.FanTray.Fanses.Fans.Information.Rma)}
                                    self._child_list_classes = {}

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
                                    self._segment_path = lambda: "information"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Diag.Racks.Rack.FanTraies.FanTray.Fanses.Fans.Information, ['asset_alias', 'asset_id', 'base_mac_address1', 'base_mac_address2', 'base_mac_address3', 'base_mac_address4', 'block_checksum', 'block_count', 'block_length', 'block_signature', 'block_version', 'chassis_sid', 'clei', 'controller_family', 'controller_type', 'description', 'dev_num1', 'dev_num2', 'dev_num3', 'dev_num4', 'dev_num5', 'dev_num6', 'dev_num7', 'eci', 'eeprom_size', 'engineer_use', 'fru_major_type', 'fru_minor_type', 'hw_version', 'hwid', 'idprom_format_rev', 'mac_add_blk_size1', 'mac_add_blk_size2', 'mac_add_blk_size3', 'mac_add_blk_size4', 'manu_test_data', 'mfg_bits', 'mfg_deviation', 'oem_string', 'part_number', 'part_revision', 'pca_num', 'pcavid', 'pcb_serial_num', 'pid', 'power_consumption', 'power_supply_type', 'product_id', 'rma_code', 'serial_number', 'snmpoid', 'top_assem_part_num', 'top_assem_vid', 'udi_description', 'udi_name', 'vid'], name, value)


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
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.rma_history = YLeaf(YType.str, "rma-history")

                                        self.rma_number = YLeaf(YType.str, "rma-number")

                                        self.test_history = YLeaf(YType.str, "test-history")
                                        self._segment_path = lambda: "rma"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Diag.Racks.Rack.FanTraies.FanTray.Fanses.Fans.Information.Rma, ['rma_history', 'rma_number', 'test_history'], name, value)


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
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"power-shelf" : ("power_shelf", Diag.Racks.Rack.PowerShelfs.PowerShelf)}

                    self.power_shelf = YList(self)
                    self._segment_path = lambda: "power-shelfs"

                def __setattr__(self, name, value):
                    self._perform_setattr(Diag.Racks.Rack.PowerShelfs, [], name, value)


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
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"power-supplies" : ("power_supplies", Diag.Racks.Rack.PowerShelfs.PowerShelf.PowerSupplies)}
                        self._child_list_classes = {}

                        self.power_shelf_name = YLeaf(YType.str, "power-shelf-name")

                        self.power_supplies = Diag.Racks.Rack.PowerShelfs.PowerShelf.PowerSupplies()
                        self.power_supplies.parent = self
                        self._children_name_map["power_supplies"] = "power-supplies"
                        self._children_yang_names.add("power-supplies")
                        self._segment_path = lambda: "power-shelf" + "[power-shelf-name='" + self.power_shelf_name.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Diag.Racks.Rack.PowerShelfs.PowerShelf, ['power_shelf_name'], name, value)


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
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"power-supply" : ("power_supply", Diag.Racks.Rack.PowerShelfs.PowerShelf.PowerSupplies.PowerSupply)}

                            self.power_supply = YList(self)
                            self._segment_path = lambda: "power-supplies"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Diag.Racks.Rack.PowerShelfs.PowerShelf.PowerSupplies, [], name, value)


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
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"information" : ("information", Diag.Racks.Rack.PowerShelfs.PowerShelf.PowerSupplies.PowerSupply.Information)}
                                self._child_list_classes = {}

                                self.power_supply_name = YLeaf(YType.str, "power-supply-name")

                                self.information = Diag.Racks.Rack.PowerShelfs.PowerShelf.PowerSupplies.PowerSupply.Information()
                                self.information.parent = self
                                self._children_name_map["information"] = "information"
                                self._children_yang_names.add("information")
                                self._segment_path = lambda: "power-supply" + "[power-supply-name='" + self.power_supply_name.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Diag.Racks.Rack.PowerShelfs.PowerShelf.PowerSupplies.PowerSupply, ['power_supply_name'], name, value)


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
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {"rma" : ("rma", Diag.Racks.Rack.PowerShelfs.PowerShelf.PowerSupplies.PowerSupply.Information.Rma)}
                                    self._child_list_classes = {}

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
                                    self._segment_path = lambda: "information"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Diag.Racks.Rack.PowerShelfs.PowerShelf.PowerSupplies.PowerSupply.Information, ['asset_alias', 'asset_id', 'base_mac_address1', 'base_mac_address2', 'base_mac_address3', 'base_mac_address4', 'block_checksum', 'block_count', 'block_length', 'block_signature', 'block_version', 'chassis_sid', 'clei', 'controller_family', 'controller_type', 'description', 'dev_num1', 'dev_num2', 'dev_num3', 'dev_num4', 'dev_num5', 'dev_num6', 'dev_num7', 'eci', 'eeprom_size', 'engineer_use', 'fru_major_type', 'fru_minor_type', 'hw_version', 'hwid', 'idprom_format_rev', 'mac_add_blk_size1', 'mac_add_blk_size2', 'mac_add_blk_size3', 'mac_add_blk_size4', 'manu_test_data', 'mfg_bits', 'mfg_deviation', 'oem_string', 'part_number', 'part_revision', 'pca_num', 'pcavid', 'pcb_serial_num', 'pid', 'power_consumption', 'power_supply_type', 'product_id', 'rma_code', 'serial_number', 'snmpoid', 'top_assem_part_num', 'top_assem_vid', 'udi_description', 'udi_name', 'vid'], name, value)


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
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.rma_history = YLeaf(YType.str, "rma-history")

                                        self.rma_number = YLeaf(YType.str, "rma-number")

                                        self.test_history = YLeaf(YType.str, "test-history")
                                        self._segment_path = lambda: "rma"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Diag.Racks.Rack.PowerShelfs.PowerShelf.PowerSupplies.PowerSupply.Information.Rma, ['rma_history', 'rma_number', 'test_history'], name, value)


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
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"slot" : ("slot", Diag.Racks.Rack.Slots.Slot)}

                    self.slot = YList(self)
                    self._segment_path = lambda: "slots"

                def __setattr__(self, name, value):
                    self._perform_setattr(Diag.Racks.Rack.Slots, [], name, value)


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
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"instances" : ("instances", Diag.Racks.Rack.Slots.Slot.Instances)}
                        self._child_list_classes = {}

                        self.slot_name = YLeaf(YType.str, "slot-name")

                        self.instances = Diag.Racks.Rack.Slots.Slot.Instances()
                        self.instances.parent = self
                        self._children_name_map["instances"] = "instances"
                        self._children_yang_names.add("instances")
                        self._segment_path = lambda: "slot" + "[slot-name='" + self.slot_name.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Diag.Racks.Rack.Slots.Slot, ['slot_name'], name, value)


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
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"instance" : ("instance", Diag.Racks.Rack.Slots.Slot.Instances.Instance)}

                            self.instance = YList(self)
                            self._segment_path = lambda: "instances"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Diag.Racks.Rack.Slots.Slot.Instances, [], name, value)


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
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"detail" : ("detail", Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail)}
                                self._child_list_classes = {}

                                self.name = YLeaf(YType.str, "name")

                                self.detail = Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail()
                                self.detail.parent = self
                                self._children_name_map["detail"] = "detail"
                                self._children_yang_names.add("detail")
                                self._segment_path = lambda: "instance" + "[name='" + self.name.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Diag.Racks.Rack.Slots.Slot.Instances.Instance, ['name'], name, value)


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
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {"card-instance" : ("card_instance", Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.CardInstance)}
                                    self._child_list_classes = {}

                                    self.node_operational_state = YLeaf(YType.str, "node-operational-state")

                                    self.card_instance = Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.CardInstance()
                                    self.card_instance.parent = self
                                    self._children_name_map["card_instance"] = "card-instance"
                                    self._children_yang_names.add("card-instance")
                                    self._segment_path = lambda: "detail"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail, ['node_operational_state'], name, value)


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
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {"rma" : ("rma", Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.CardInstance.Rma)}
                                        self._child_list_classes = {}

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
                                        self._segment_path = lambda: "card-instance"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.CardInstance, ['asset_alias', 'asset_id', 'base_mac_address1', 'base_mac_address2', 'base_mac_address3', 'base_mac_address4', 'block_checksum', 'block_count', 'block_length', 'block_signature', 'block_version', 'chassis_sid', 'clei', 'controller_family', 'controller_type', 'description', 'dev_num1', 'dev_num2', 'dev_num3', 'dev_num4', 'dev_num5', 'dev_num6', 'dev_num7', 'eci', 'eeprom_size', 'engineer_use', 'fru_major_type', 'fru_minor_type', 'hw_version', 'hwid', 'idprom_format_rev', 'mac_add_blk_size1', 'mac_add_blk_size2', 'mac_add_blk_size3', 'mac_add_blk_size4', 'manu_test_data', 'mfg_bits', 'mfg_deviation', 'oem_string', 'part_number', 'part_revision', 'pca_num', 'pcavid', 'pcb_serial_num', 'pid', 'power_consumption', 'power_supply_type', 'product_id', 'rma_code', 'serial_number', 'snmpoid', 'top_assem_part_num', 'top_assem_vid', 'udi_description', 'udi_name', 'vid'], name, value)


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
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.rma_history = YLeaf(YType.str, "rma-history")

                                            self.rma_number = YLeaf(YType.str, "rma-number")

                                            self.test_history = YLeaf(YType.str, "test-history")
                                            self._segment_path = lambda: "rma"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.CardInstance.Rma, ['rma_history', 'rma_number', 'test_history'], name, value)

    def clone_ptr(self):
        self._top_entity = Diag()
        return self._top_entity

