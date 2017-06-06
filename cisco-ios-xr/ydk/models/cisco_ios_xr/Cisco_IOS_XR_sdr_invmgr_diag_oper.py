""" Cisco_IOS_XR_sdr_invmgr_diag_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR sdr\-invmgr\-diag package operational data.

This module contains definitions
for the following management objects\:
  diag\: Diag information

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class Diag(object):
    """
    Diag information
    
    .. attribute:: racks
    
    	Table of racks
    	**type**\:   :py:class:`Racks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sdr_invmgr_diag_oper.Diag.Racks>`
    
    

    """

    _prefix = 'sdr-invmgr-diag-oper'
    _revision = '2015-11-09'

    def __init__(self):
        self.racks = Diag.Racks()
        self.racks.parent = self


    class Racks(object):
        """
        Table of racks
        
        .. attribute:: rack
        
        	Rack name
        	**type**\: list of    :py:class:`Rack <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sdr_invmgr_diag_oper.Diag.Racks.Rack>`
        
        

        """

        _prefix = 'sdr-invmgr-diag-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.rack = YList()
            self.rack.parent = self
            self.rack.name = 'rack'


        class Rack(object):
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
                self.parent = None
                self.rack_name = None
                self.chassis = Diag.Racks.Rack.Chassis()
                self.chassis.parent = self
                self.fan_traies = Diag.Racks.Rack.FanTraies()
                self.fan_traies.parent = self
                self.power_shelfs = Diag.Racks.Rack.PowerShelfs()
                self.power_shelfs.parent = self
                self.slots = Diag.Racks.Rack.Slots()
                self.slots.parent = self


            class PowerShelfs(object):
                """
                Table for rack power shelf 
                
                .. attribute:: power_shelf
                
                	Power shelf name
                	**type**\: list of    :py:class:`PowerShelf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sdr_invmgr_diag_oper.Diag.Racks.Rack.PowerShelfs.PowerShelf>`
                
                

                """

                _prefix = 'sdr-invmgr-diag-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.power_shelf = YList()
                    self.power_shelf.parent = self
                    self.power_shelf.name = 'power_shelf'


                class PowerShelf(object):
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
                        self.parent = None
                        self.power_shelf_name = None
                        self.power_supplies = Diag.Racks.Rack.PowerShelfs.PowerShelf.PowerSupplies()
                        self.power_supplies.parent = self


                    class PowerSupplies(object):
                        """
                        Table for rack power supply 
                        
                        .. attribute:: power_supply
                        
                        	Power Supply name
                        	**type**\: list of    :py:class:`PowerSupply <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sdr_invmgr_diag_oper.Diag.Racks.Rack.PowerShelfs.PowerShelf.PowerSupplies.PowerSupply>`
                        
                        

                        """

                        _prefix = 'sdr-invmgr-diag-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.power_supply = YList()
                            self.power_supply.parent = self
                            self.power_supply.name = 'power_supply'


                        class PowerSupply(object):
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
                                self.parent = None
                                self.power_supply_name = None
                                self.information = Diag.Racks.Rack.PowerShelfs.PowerShelf.PowerSupplies.PowerSupply.Information()
                                self.information.parent = self


                            class Information(object):
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
                                    self.parent = None
                                    self.asset_alias = None
                                    self.asset_id = None
                                    self.base_mac_address1 = None
                                    self.base_mac_address2 = None
                                    self.base_mac_address3 = None
                                    self.base_mac_address4 = None
                                    self.block_checksum = None
                                    self.block_count = None
                                    self.block_length = None
                                    self.block_signature = None
                                    self.block_version = None
                                    self.chassis_sid = None
                                    self.clei = None
                                    self.controller_family = None
                                    self.controller_type = None
                                    self.description = None
                                    self.dev_num1 = None
                                    self.dev_num2 = None
                                    self.dev_num3 = None
                                    self.dev_num4 = None
                                    self.dev_num5 = None
                                    self.dev_num6 = None
                                    self.dev_num7 = None
                                    self.eci = None
                                    self.eeprom_size = None
                                    self.engineer_use = None
                                    self.fru_major_type = None
                                    self.fru_minor_type = None
                                    self.hw_version = None
                                    self.hwid = None
                                    self.idprom_format_rev = None
                                    self.mac_add_blk_size1 = None
                                    self.mac_add_blk_size2 = None
                                    self.mac_add_blk_size3 = None
                                    self.mac_add_blk_size4 = None
                                    self.manu_test_data = None
                                    self.mfg_bits = None
                                    self.mfg_deviation = None
                                    self.oem_string = None
                                    self.part_number = None
                                    self.part_revision = None
                                    self.pca_num = None
                                    self.pcavid = None
                                    self.pcb_serial_num = None
                                    self.pid = None
                                    self.power_consumption = None
                                    self.power_supply_type = None
                                    self.product_id = None
                                    self.rma = Diag.Racks.Rack.PowerShelfs.PowerShelf.PowerSupplies.PowerSupply.Information.Rma()
                                    self.rma.parent = self
                                    self.rma_code = None
                                    self.serial_number = None
                                    self.snmpoid = None
                                    self.top_assem_part_num = None
                                    self.top_assem_vid = None
                                    self.udi_description = None
                                    self.udi_name = None
                                    self.vid = None


                                class Rma(object):
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
                                        self.parent = None
                                        self.rma_history = None
                                        self.rma_number = None
                                        self.test_history = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-sdr-invmgr-diag-oper:rma'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.rma_history is not None:
                                            return True

                                        if self.rma_number is not None:
                                            return True

                                        if self.test_history is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sdr_invmgr_diag_oper as meta
                                        return meta._meta_table['Diag.Racks.Rack.PowerShelfs.PowerShelf.PowerSupplies.PowerSupply.Information.Rma']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-sdr-invmgr-diag-oper:information'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.asset_alias is not None:
                                        return True

                                    if self.asset_id is not None:
                                        return True

                                    if self.base_mac_address1 is not None:
                                        return True

                                    if self.base_mac_address2 is not None:
                                        return True

                                    if self.base_mac_address3 is not None:
                                        return True

                                    if self.base_mac_address4 is not None:
                                        return True

                                    if self.block_checksum is not None:
                                        return True

                                    if self.block_count is not None:
                                        return True

                                    if self.block_length is not None:
                                        return True

                                    if self.block_signature is not None:
                                        return True

                                    if self.block_version is not None:
                                        return True

                                    if self.chassis_sid is not None:
                                        return True

                                    if self.clei is not None:
                                        return True

                                    if self.controller_family is not None:
                                        return True

                                    if self.controller_type is not None:
                                        return True

                                    if self.description is not None:
                                        return True

                                    if self.dev_num1 is not None:
                                        return True

                                    if self.dev_num2 is not None:
                                        return True

                                    if self.dev_num3 is not None:
                                        return True

                                    if self.dev_num4 is not None:
                                        return True

                                    if self.dev_num5 is not None:
                                        return True

                                    if self.dev_num6 is not None:
                                        return True

                                    if self.dev_num7 is not None:
                                        return True

                                    if self.eci is not None:
                                        return True

                                    if self.eeprom_size is not None:
                                        return True

                                    if self.engineer_use is not None:
                                        return True

                                    if self.fru_major_type is not None:
                                        return True

                                    if self.fru_minor_type is not None:
                                        return True

                                    if self.hw_version is not None:
                                        return True

                                    if self.hwid is not None:
                                        return True

                                    if self.idprom_format_rev is not None:
                                        return True

                                    if self.mac_add_blk_size1 is not None:
                                        return True

                                    if self.mac_add_blk_size2 is not None:
                                        return True

                                    if self.mac_add_blk_size3 is not None:
                                        return True

                                    if self.mac_add_blk_size4 is not None:
                                        return True

                                    if self.manu_test_data is not None:
                                        return True

                                    if self.mfg_bits is not None:
                                        return True

                                    if self.mfg_deviation is not None:
                                        return True

                                    if self.oem_string is not None:
                                        return True

                                    if self.part_number is not None:
                                        return True

                                    if self.part_revision is not None:
                                        return True

                                    if self.pca_num is not None:
                                        return True

                                    if self.pcavid is not None:
                                        return True

                                    if self.pcb_serial_num is not None:
                                        return True

                                    if self.pid is not None:
                                        return True

                                    if self.power_consumption is not None:
                                        return True

                                    if self.power_supply_type is not None:
                                        return True

                                    if self.product_id is not None:
                                        return True

                                    if self.rma is not None and self.rma._has_data():
                                        return True

                                    if self.rma_code is not None:
                                        return True

                                    if self.serial_number is not None:
                                        return True

                                    if self.snmpoid is not None:
                                        return True

                                    if self.top_assem_part_num is not None:
                                        return True

                                    if self.top_assem_vid is not None:
                                        return True

                                    if self.udi_description is not None:
                                        return True

                                    if self.udi_name is not None:
                                        return True

                                    if self.vid is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sdr_invmgr_diag_oper as meta
                                    return meta._meta_table['Diag.Racks.Rack.PowerShelfs.PowerShelf.PowerSupplies.PowerSupply.Information']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.power_supply_name is None:
                                    raise YPYModelError('Key property power_supply_name is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-sdr-invmgr-diag-oper:power-supply[Cisco-IOS-XR-sdr-invmgr-diag-oper:power-supply-name = ' + str(self.power_supply_name) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.power_supply_name is not None:
                                    return True

                                if self.information is not None and self.information._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sdr_invmgr_diag_oper as meta
                                return meta._meta_table['Diag.Racks.Rack.PowerShelfs.PowerShelf.PowerSupplies.PowerSupply']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-sdr-invmgr-diag-oper:power-supplies'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.power_supply is not None:
                                for child_ref in self.power_supply:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sdr_invmgr_diag_oper as meta
                            return meta._meta_table['Diag.Racks.Rack.PowerShelfs.PowerShelf.PowerSupplies']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.power_shelf_name is None:
                            raise YPYModelError('Key property power_shelf_name is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-sdr-invmgr-diag-oper:power-shelf[Cisco-IOS-XR-sdr-invmgr-diag-oper:power-shelf-name = ' + str(self.power_shelf_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.power_shelf_name is not None:
                            return True

                        if self.power_supplies is not None and self.power_supplies._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sdr_invmgr_diag_oper as meta
                        return meta._meta_table['Diag.Racks.Rack.PowerShelfs.PowerShelf']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-sdr-invmgr-diag-oper:power-shelfs'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.power_shelf is not None:
                        for child_ref in self.power_shelf:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sdr_invmgr_diag_oper as meta
                    return meta._meta_table['Diag.Racks.Rack.PowerShelfs']['meta_info']


            class FanTraies(object):
                """
                Table for rack fan trays
                
                .. attribute:: fan_tray
                
                	Fan tray name
                	**type**\: list of    :py:class:`FanTray <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sdr_invmgr_diag_oper.Diag.Racks.Rack.FanTraies.FanTray>`
                
                

                """

                _prefix = 'sdr-invmgr-diag-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.fan_tray = YList()
                    self.fan_tray.parent = self
                    self.fan_tray.name = 'fan_tray'


                class FanTray(object):
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
                        self.parent = None
                        self.fan_tray_name = None
                        self.fanses = Diag.Racks.Rack.FanTraies.FanTray.Fanses()
                        self.fanses.parent = self


                    class Fanses(object):
                        """
                        Table for rack fans 
                        
                        .. attribute:: fans
                        
                        	Fan name
                        	**type**\: list of    :py:class:`Fans <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sdr_invmgr_diag_oper.Diag.Racks.Rack.FanTraies.FanTray.Fanses.Fans>`
                        
                        

                        """

                        _prefix = 'sdr-invmgr-diag-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.fans = YList()
                            self.fans.parent = self
                            self.fans.name = 'fans'


                        class Fans(object):
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
                                self.parent = None
                                self.fans_name = None
                                self.information = Diag.Racks.Rack.FanTraies.FanTray.Fanses.Fans.Information()
                                self.information.parent = self


                            class Information(object):
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
                                    self.parent = None
                                    self.asset_alias = None
                                    self.asset_id = None
                                    self.base_mac_address1 = None
                                    self.base_mac_address2 = None
                                    self.base_mac_address3 = None
                                    self.base_mac_address4 = None
                                    self.block_checksum = None
                                    self.block_count = None
                                    self.block_length = None
                                    self.block_signature = None
                                    self.block_version = None
                                    self.chassis_sid = None
                                    self.clei = None
                                    self.controller_family = None
                                    self.controller_type = None
                                    self.description = None
                                    self.dev_num1 = None
                                    self.dev_num2 = None
                                    self.dev_num3 = None
                                    self.dev_num4 = None
                                    self.dev_num5 = None
                                    self.dev_num6 = None
                                    self.dev_num7 = None
                                    self.eci = None
                                    self.eeprom_size = None
                                    self.engineer_use = None
                                    self.fru_major_type = None
                                    self.fru_minor_type = None
                                    self.hw_version = None
                                    self.hwid = None
                                    self.idprom_format_rev = None
                                    self.mac_add_blk_size1 = None
                                    self.mac_add_blk_size2 = None
                                    self.mac_add_blk_size3 = None
                                    self.mac_add_blk_size4 = None
                                    self.manu_test_data = None
                                    self.mfg_bits = None
                                    self.mfg_deviation = None
                                    self.oem_string = None
                                    self.part_number = None
                                    self.part_revision = None
                                    self.pca_num = None
                                    self.pcavid = None
                                    self.pcb_serial_num = None
                                    self.pid = None
                                    self.power_consumption = None
                                    self.power_supply_type = None
                                    self.product_id = None
                                    self.rma = Diag.Racks.Rack.FanTraies.FanTray.Fanses.Fans.Information.Rma()
                                    self.rma.parent = self
                                    self.rma_code = None
                                    self.serial_number = None
                                    self.snmpoid = None
                                    self.top_assem_part_num = None
                                    self.top_assem_vid = None
                                    self.udi_description = None
                                    self.udi_name = None
                                    self.vid = None


                                class Rma(object):
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
                                        self.parent = None
                                        self.rma_history = None
                                        self.rma_number = None
                                        self.test_history = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-sdr-invmgr-diag-oper:rma'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.rma_history is not None:
                                            return True

                                        if self.rma_number is not None:
                                            return True

                                        if self.test_history is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sdr_invmgr_diag_oper as meta
                                        return meta._meta_table['Diag.Racks.Rack.FanTraies.FanTray.Fanses.Fans.Information.Rma']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-sdr-invmgr-diag-oper:information'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.asset_alias is not None:
                                        return True

                                    if self.asset_id is not None:
                                        return True

                                    if self.base_mac_address1 is not None:
                                        return True

                                    if self.base_mac_address2 is not None:
                                        return True

                                    if self.base_mac_address3 is not None:
                                        return True

                                    if self.base_mac_address4 is not None:
                                        return True

                                    if self.block_checksum is not None:
                                        return True

                                    if self.block_count is not None:
                                        return True

                                    if self.block_length is not None:
                                        return True

                                    if self.block_signature is not None:
                                        return True

                                    if self.block_version is not None:
                                        return True

                                    if self.chassis_sid is not None:
                                        return True

                                    if self.clei is not None:
                                        return True

                                    if self.controller_family is not None:
                                        return True

                                    if self.controller_type is not None:
                                        return True

                                    if self.description is not None:
                                        return True

                                    if self.dev_num1 is not None:
                                        return True

                                    if self.dev_num2 is not None:
                                        return True

                                    if self.dev_num3 is not None:
                                        return True

                                    if self.dev_num4 is not None:
                                        return True

                                    if self.dev_num5 is not None:
                                        return True

                                    if self.dev_num6 is not None:
                                        return True

                                    if self.dev_num7 is not None:
                                        return True

                                    if self.eci is not None:
                                        return True

                                    if self.eeprom_size is not None:
                                        return True

                                    if self.engineer_use is not None:
                                        return True

                                    if self.fru_major_type is not None:
                                        return True

                                    if self.fru_minor_type is not None:
                                        return True

                                    if self.hw_version is not None:
                                        return True

                                    if self.hwid is not None:
                                        return True

                                    if self.idprom_format_rev is not None:
                                        return True

                                    if self.mac_add_blk_size1 is not None:
                                        return True

                                    if self.mac_add_blk_size2 is not None:
                                        return True

                                    if self.mac_add_blk_size3 is not None:
                                        return True

                                    if self.mac_add_blk_size4 is not None:
                                        return True

                                    if self.manu_test_data is not None:
                                        return True

                                    if self.mfg_bits is not None:
                                        return True

                                    if self.mfg_deviation is not None:
                                        return True

                                    if self.oem_string is not None:
                                        return True

                                    if self.part_number is not None:
                                        return True

                                    if self.part_revision is not None:
                                        return True

                                    if self.pca_num is not None:
                                        return True

                                    if self.pcavid is not None:
                                        return True

                                    if self.pcb_serial_num is not None:
                                        return True

                                    if self.pid is not None:
                                        return True

                                    if self.power_consumption is not None:
                                        return True

                                    if self.power_supply_type is not None:
                                        return True

                                    if self.product_id is not None:
                                        return True

                                    if self.rma is not None and self.rma._has_data():
                                        return True

                                    if self.rma_code is not None:
                                        return True

                                    if self.serial_number is not None:
                                        return True

                                    if self.snmpoid is not None:
                                        return True

                                    if self.top_assem_part_num is not None:
                                        return True

                                    if self.top_assem_vid is not None:
                                        return True

                                    if self.udi_description is not None:
                                        return True

                                    if self.udi_name is not None:
                                        return True

                                    if self.vid is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sdr_invmgr_diag_oper as meta
                                    return meta._meta_table['Diag.Racks.Rack.FanTraies.FanTray.Fanses.Fans.Information']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.fans_name is None:
                                    raise YPYModelError('Key property fans_name is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-sdr-invmgr-diag-oper:fans[Cisco-IOS-XR-sdr-invmgr-diag-oper:fans-name = ' + str(self.fans_name) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.fans_name is not None:
                                    return True

                                if self.information is not None and self.information._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sdr_invmgr_diag_oper as meta
                                return meta._meta_table['Diag.Racks.Rack.FanTraies.FanTray.Fanses.Fans']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-sdr-invmgr-diag-oper:fanses'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.fans is not None:
                                for child_ref in self.fans:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sdr_invmgr_diag_oper as meta
                            return meta._meta_table['Diag.Racks.Rack.FanTraies.FanTray.Fanses']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.fan_tray_name is None:
                            raise YPYModelError('Key property fan_tray_name is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-sdr-invmgr-diag-oper:fan-tray[Cisco-IOS-XR-sdr-invmgr-diag-oper:fan-tray-name = ' + str(self.fan_tray_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.fan_tray_name is not None:
                            return True

                        if self.fanses is not None and self.fanses._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sdr_invmgr_diag_oper as meta
                        return meta._meta_table['Diag.Racks.Rack.FanTraies.FanTray']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-sdr-invmgr-diag-oper:fan-traies'

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
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sdr_invmgr_diag_oper as meta
                    return meta._meta_table['Diag.Racks.Rack.FanTraies']['meta_info']


            class Slots(object):
                """
                Table of slots
                
                .. attribute:: slot
                
                	Slot name
                	**type**\: list of    :py:class:`Slot <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sdr_invmgr_diag_oper.Diag.Racks.Rack.Slots.Slot>`
                
                

                """

                _prefix = 'sdr-invmgr-diag-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.slot = YList()
                    self.slot.parent = self
                    self.slot.name = 'slot'


                class Slot(object):
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
                        self.parent = None
                        self.slot_name = None
                        self.instances = Diag.Racks.Rack.Slots.Slot.Instances()
                        self.instances.parent = self


                    class Instances(object):
                        """
                        Table of instances
                        
                        .. attribute:: instance
                        
                        	instance number
                        	**type**\: list of    :py:class:`Instance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_sdr_invmgr_diag_oper.Diag.Racks.Rack.Slots.Slot.Instances.Instance>`
                        
                        

                        """

                        _prefix = 'sdr-invmgr-diag-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.instance = YList()
                            self.instance.parent = self
                            self.instance.name = 'instance'


                        class Instance(object):
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
                                self.parent = None
                                self.name = None
                                self.detail = Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail()
                                self.detail.parent = self


                            class Detail(object):
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
                                    self.parent = None
                                    self.card_instance = Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.CardInstance()
                                    self.card_instance.parent = self
                                    self.node_operational_state = None


                                class CardInstance(object):
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
                                        self.parent = None
                                        self.asset_alias = None
                                        self.asset_id = None
                                        self.base_mac_address1 = None
                                        self.base_mac_address2 = None
                                        self.base_mac_address3 = None
                                        self.base_mac_address4 = None
                                        self.block_checksum = None
                                        self.block_count = None
                                        self.block_length = None
                                        self.block_signature = None
                                        self.block_version = None
                                        self.chassis_sid = None
                                        self.clei = None
                                        self.controller_family = None
                                        self.controller_type = None
                                        self.description = None
                                        self.dev_num1 = None
                                        self.dev_num2 = None
                                        self.dev_num3 = None
                                        self.dev_num4 = None
                                        self.dev_num5 = None
                                        self.dev_num6 = None
                                        self.dev_num7 = None
                                        self.eci = None
                                        self.eeprom_size = None
                                        self.engineer_use = None
                                        self.fru_major_type = None
                                        self.fru_minor_type = None
                                        self.hw_version = None
                                        self.hwid = None
                                        self.idprom_format_rev = None
                                        self.mac_add_blk_size1 = None
                                        self.mac_add_blk_size2 = None
                                        self.mac_add_blk_size3 = None
                                        self.mac_add_blk_size4 = None
                                        self.manu_test_data = None
                                        self.mfg_bits = None
                                        self.mfg_deviation = None
                                        self.oem_string = None
                                        self.part_number = None
                                        self.part_revision = None
                                        self.pca_num = None
                                        self.pcavid = None
                                        self.pcb_serial_num = None
                                        self.pid = None
                                        self.power_consumption = None
                                        self.power_supply_type = None
                                        self.product_id = None
                                        self.rma = Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.CardInstance.Rma()
                                        self.rma.parent = self
                                        self.rma_code = None
                                        self.serial_number = None
                                        self.snmpoid = None
                                        self.top_assem_part_num = None
                                        self.top_assem_vid = None
                                        self.udi_description = None
                                        self.udi_name = None
                                        self.vid = None


                                    class Rma(object):
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
                                            self.parent = None
                                            self.rma_history = None
                                            self.rma_number = None
                                            self.test_history = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-sdr-invmgr-diag-oper:rma'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.rma_history is not None:
                                                return True

                                            if self.rma_number is not None:
                                                return True

                                            if self.test_history is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sdr_invmgr_diag_oper as meta
                                            return meta._meta_table['Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.CardInstance.Rma']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-sdr-invmgr-diag-oper:card-instance'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.asset_alias is not None:
                                            return True

                                        if self.asset_id is not None:
                                            return True

                                        if self.base_mac_address1 is not None:
                                            return True

                                        if self.base_mac_address2 is not None:
                                            return True

                                        if self.base_mac_address3 is not None:
                                            return True

                                        if self.base_mac_address4 is not None:
                                            return True

                                        if self.block_checksum is not None:
                                            return True

                                        if self.block_count is not None:
                                            return True

                                        if self.block_length is not None:
                                            return True

                                        if self.block_signature is not None:
                                            return True

                                        if self.block_version is not None:
                                            return True

                                        if self.chassis_sid is not None:
                                            return True

                                        if self.clei is not None:
                                            return True

                                        if self.controller_family is not None:
                                            return True

                                        if self.controller_type is not None:
                                            return True

                                        if self.description is not None:
                                            return True

                                        if self.dev_num1 is not None:
                                            return True

                                        if self.dev_num2 is not None:
                                            return True

                                        if self.dev_num3 is not None:
                                            return True

                                        if self.dev_num4 is not None:
                                            return True

                                        if self.dev_num5 is not None:
                                            return True

                                        if self.dev_num6 is not None:
                                            return True

                                        if self.dev_num7 is not None:
                                            return True

                                        if self.eci is not None:
                                            return True

                                        if self.eeprom_size is not None:
                                            return True

                                        if self.engineer_use is not None:
                                            return True

                                        if self.fru_major_type is not None:
                                            return True

                                        if self.fru_minor_type is not None:
                                            return True

                                        if self.hw_version is not None:
                                            return True

                                        if self.hwid is not None:
                                            return True

                                        if self.idprom_format_rev is not None:
                                            return True

                                        if self.mac_add_blk_size1 is not None:
                                            return True

                                        if self.mac_add_blk_size2 is not None:
                                            return True

                                        if self.mac_add_blk_size3 is not None:
                                            return True

                                        if self.mac_add_blk_size4 is not None:
                                            return True

                                        if self.manu_test_data is not None:
                                            return True

                                        if self.mfg_bits is not None:
                                            return True

                                        if self.mfg_deviation is not None:
                                            return True

                                        if self.oem_string is not None:
                                            return True

                                        if self.part_number is not None:
                                            return True

                                        if self.part_revision is not None:
                                            return True

                                        if self.pca_num is not None:
                                            return True

                                        if self.pcavid is not None:
                                            return True

                                        if self.pcb_serial_num is not None:
                                            return True

                                        if self.pid is not None:
                                            return True

                                        if self.power_consumption is not None:
                                            return True

                                        if self.power_supply_type is not None:
                                            return True

                                        if self.product_id is not None:
                                            return True

                                        if self.rma is not None and self.rma._has_data():
                                            return True

                                        if self.rma_code is not None:
                                            return True

                                        if self.serial_number is not None:
                                            return True

                                        if self.snmpoid is not None:
                                            return True

                                        if self.top_assem_part_num is not None:
                                            return True

                                        if self.top_assem_vid is not None:
                                            return True

                                        if self.udi_description is not None:
                                            return True

                                        if self.udi_name is not None:
                                            return True

                                        if self.vid is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sdr_invmgr_diag_oper as meta
                                        return meta._meta_table['Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail.CardInstance']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-sdr-invmgr-diag-oper:detail'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.card_instance is not None and self.card_instance._has_data():
                                        return True

                                    if self.node_operational_state is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sdr_invmgr_diag_oper as meta
                                    return meta._meta_table['Diag.Racks.Rack.Slots.Slot.Instances.Instance.Detail']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.name is None:
                                    raise YPYModelError('Key property name is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-sdr-invmgr-diag-oper:instance[Cisco-IOS-XR-sdr-invmgr-diag-oper:name = ' + str(self.name) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.name is not None:
                                    return True

                                if self.detail is not None and self.detail._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sdr_invmgr_diag_oper as meta
                                return meta._meta_table['Diag.Racks.Rack.Slots.Slot.Instances.Instance']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-sdr-invmgr-diag-oper:instances'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.instance is not None:
                                for child_ref in self.instance:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sdr_invmgr_diag_oper as meta
                            return meta._meta_table['Diag.Racks.Rack.Slots.Slot.Instances']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.slot_name is None:
                            raise YPYModelError('Key property slot_name is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-sdr-invmgr-diag-oper:slot[Cisco-IOS-XR-sdr-invmgr-diag-oper:slot-name = ' + str(self.slot_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.slot_name is not None:
                            return True

                        if self.instances is not None and self.instances._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sdr_invmgr_diag_oper as meta
                        return meta._meta_table['Diag.Racks.Rack.Slots.Slot']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-sdr-invmgr-diag-oper:slots'

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
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sdr_invmgr_diag_oper as meta
                    return meta._meta_table['Diag.Racks.Rack.Slots']['meta_info']


            class Chassis(object):
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
                    self.parent = None
                    self.asset_alias = None
                    self.asset_id = None
                    self.base_mac_address1 = None
                    self.base_mac_address2 = None
                    self.base_mac_address3 = None
                    self.base_mac_address4 = None
                    self.block_checksum = None
                    self.block_count = None
                    self.block_length = None
                    self.block_signature = None
                    self.block_version = None
                    self.chassis_sid = None
                    self.clei = None
                    self.controller_family = None
                    self.controller_type = None
                    self.description = None
                    self.dev_num1 = None
                    self.dev_num2 = None
                    self.dev_num3 = None
                    self.dev_num4 = None
                    self.dev_num5 = None
                    self.dev_num6 = None
                    self.dev_num7 = None
                    self.eci = None
                    self.eeprom_size = None
                    self.engineer_use = None
                    self.fru_major_type = None
                    self.fru_minor_type = None
                    self.hw_version = None
                    self.hwid = None
                    self.idprom_format_rev = None
                    self.mac_add_blk_size1 = None
                    self.mac_add_blk_size2 = None
                    self.mac_add_blk_size3 = None
                    self.mac_add_blk_size4 = None
                    self.manu_test_data = None
                    self.mfg_bits = None
                    self.mfg_deviation = None
                    self.oem_string = None
                    self.part_number = None
                    self.part_revision = None
                    self.pca_num = None
                    self.pcavid = None
                    self.pcb_serial_num = None
                    self.pid = None
                    self.power_consumption = None
                    self.power_supply_type = None
                    self.product_id = None
                    self.rma = Diag.Racks.Rack.Chassis.Rma()
                    self.rma.parent = self
                    self.rma_code = None
                    self.serial_number = None
                    self.snmpoid = None
                    self.top_assem_part_num = None
                    self.top_assem_vid = None
                    self.udi_description = None
                    self.udi_name = None
                    self.vid = None


                class Rma(object):
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
                        self.parent = None
                        self.rma_history = None
                        self.rma_number = None
                        self.test_history = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-sdr-invmgr-diag-oper:rma'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.rma_history is not None:
                            return True

                        if self.rma_number is not None:
                            return True

                        if self.test_history is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sdr_invmgr_diag_oper as meta
                        return meta._meta_table['Diag.Racks.Rack.Chassis.Rma']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-sdr-invmgr-diag-oper:chassis'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.asset_alias is not None:
                        return True

                    if self.asset_id is not None:
                        return True

                    if self.base_mac_address1 is not None:
                        return True

                    if self.base_mac_address2 is not None:
                        return True

                    if self.base_mac_address3 is not None:
                        return True

                    if self.base_mac_address4 is not None:
                        return True

                    if self.block_checksum is not None:
                        return True

                    if self.block_count is not None:
                        return True

                    if self.block_length is not None:
                        return True

                    if self.block_signature is not None:
                        return True

                    if self.block_version is not None:
                        return True

                    if self.chassis_sid is not None:
                        return True

                    if self.clei is not None:
                        return True

                    if self.controller_family is not None:
                        return True

                    if self.controller_type is not None:
                        return True

                    if self.description is not None:
                        return True

                    if self.dev_num1 is not None:
                        return True

                    if self.dev_num2 is not None:
                        return True

                    if self.dev_num3 is not None:
                        return True

                    if self.dev_num4 is not None:
                        return True

                    if self.dev_num5 is not None:
                        return True

                    if self.dev_num6 is not None:
                        return True

                    if self.dev_num7 is not None:
                        return True

                    if self.eci is not None:
                        return True

                    if self.eeprom_size is not None:
                        return True

                    if self.engineer_use is not None:
                        return True

                    if self.fru_major_type is not None:
                        return True

                    if self.fru_minor_type is not None:
                        return True

                    if self.hw_version is not None:
                        return True

                    if self.hwid is not None:
                        return True

                    if self.idprom_format_rev is not None:
                        return True

                    if self.mac_add_blk_size1 is not None:
                        return True

                    if self.mac_add_blk_size2 is not None:
                        return True

                    if self.mac_add_blk_size3 is not None:
                        return True

                    if self.mac_add_blk_size4 is not None:
                        return True

                    if self.manu_test_data is not None:
                        return True

                    if self.mfg_bits is not None:
                        return True

                    if self.mfg_deviation is not None:
                        return True

                    if self.oem_string is not None:
                        return True

                    if self.part_number is not None:
                        return True

                    if self.part_revision is not None:
                        return True

                    if self.pca_num is not None:
                        return True

                    if self.pcavid is not None:
                        return True

                    if self.pcb_serial_num is not None:
                        return True

                    if self.pid is not None:
                        return True

                    if self.power_consumption is not None:
                        return True

                    if self.power_supply_type is not None:
                        return True

                    if self.product_id is not None:
                        return True

                    if self.rma is not None and self.rma._has_data():
                        return True

                    if self.rma_code is not None:
                        return True

                    if self.serial_number is not None:
                        return True

                    if self.snmpoid is not None:
                        return True

                    if self.top_assem_part_num is not None:
                        return True

                    if self.top_assem_vid is not None:
                        return True

                    if self.udi_description is not None:
                        return True

                    if self.udi_name is not None:
                        return True

                    if self.vid is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sdr_invmgr_diag_oper as meta
                    return meta._meta_table['Diag.Racks.Rack.Chassis']['meta_info']

            @property
            def _common_path(self):
                if self.rack_name is None:
                    raise YPYModelError('Key property rack_name is None')

                return '/Cisco-IOS-XR-sdr-invmgr-diag-oper:diag/Cisco-IOS-XR-sdr-invmgr-diag-oper:racks/Cisco-IOS-XR-sdr-invmgr-diag-oper:rack[Cisco-IOS-XR-sdr-invmgr-diag-oper:rack-name = ' + str(self.rack_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.rack_name is not None:
                    return True

                if self.chassis is not None and self.chassis._has_data():
                    return True

                if self.fan_traies is not None and self.fan_traies._has_data():
                    return True

                if self.power_shelfs is not None and self.power_shelfs._has_data():
                    return True

                if self.slots is not None and self.slots._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sdr_invmgr_diag_oper as meta
                return meta._meta_table['Diag.Racks.Rack']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-sdr-invmgr-diag-oper:diag/Cisco-IOS-XR-sdr-invmgr-diag-oper:racks'

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
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sdr_invmgr_diag_oper as meta
            return meta._meta_table['Diag.Racks']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-sdr-invmgr-diag-oper:diag'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.racks is not None and self.racks._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_sdr_invmgr_diag_oper as meta
        return meta._meta_table['Diag']['meta_info']


