


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'CISCOENTITYEXTMIB.CeExtConfigRegTable.CeExtConfigRegEntry' : {
        'meta_info' : _MetaInfoClass('CISCOENTITYEXTMIB.CeExtConfigRegTable.CeExtConfigRegEntry',
            False, 
            [
            _MetaInfoClassMember('entPhysicalIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'entphysicalindex',
                'CISCO-ENTITY-EXT-MIB', True),
            _MetaInfoClassMember('ceExtConfigRegister', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The value of configuration register with which
                the processor module booted.
                ''',
                'ceextconfigregister',
                'CISCO-ENTITY-EXT-MIB', False),
            _MetaInfoClassMember('ceExtConfigRegNext', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The value of configuration register in the
                processor module at next reboot. Just after 
                the reboot this has the same value as 
                ceExtConfigRegister.
                ''',
                'ceextconfigregnext',
                'CISCO-ENTITY-EXT-MIB', False),
            _MetaInfoClassMember('ceExtKickstartImageList', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                The list of system kickstart images which
                can be used for booting.
                ''',
                'ceextkickstartimagelist',
                'CISCO-ENTITY-EXT-MIB', False),
            _MetaInfoClassMember('ceExtSysBootImageList', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                The list of system boot images which
                can be used for booting.
                ''',
                'ceextsysbootimagelist',
                'CISCO-ENTITY-EXT-MIB', False),
            ],
            'CISCO-ENTITY-EXT-MIB',
            'ceExtConfigRegEntry',
            _yang_ns._namespaces['CISCO-ENTITY-EXT-MIB'],
        'ydk.models.entity.CISCO_ENTITY_EXT_MIB'
        ),
    },
    'CISCOENTITYEXTMIB.CeExtConfigRegTable' : {
        'meta_info' : _MetaInfoClass('CISCOENTITYEXTMIB.CeExtConfigRegTable',
            False, 
            [
            _MetaInfoClassMember('ceExtConfigRegEntry', REFERENCE_LIST, 'CeExtConfigRegEntry' , 'ydk.models.entity.CISCO_ENTITY_EXT_MIB', 'CISCOENTITYEXTMIB.CeExtConfigRegTable.CeExtConfigRegEntry', 
                [], [], 
                '''                A ceExtConfigRegTable entry extends
                a corresponding entPhysicalTable entry of class
                module which has a configuration register.
                
                Entries are created by the agent at the system power-up
                or module insertion.
                
                Entries are removed when the module is reset or 
                removed.
                ''',
                'ceextconfigregentry',
                'CISCO-ENTITY-EXT-MIB', False),
            ],
            'CISCO-ENTITY-EXT-MIB',
            'ceExtConfigRegTable',
            _yang_ns._namespaces['CISCO-ENTITY-EXT-MIB'],
        'ydk.models.entity.CISCO_ENTITY_EXT_MIB'
        ),
    },
    'CISCOENTITYEXTMIB.CeExtEntityLEDTable.CeExtEntityLEDEntry.CeExtEntityLEDColor_Enum' : _MetaInfoEnum('CeExtEntityLEDColor_Enum', 'ydk.models.entity.CISCO_ENTITY_EXT_MIB',
        {
            'off':'OFF',
            'green':'GREEN',
            'amber':'AMBER',
            'red':'RED',
        }, 'CISCO-ENTITY-EXT-MIB', _yang_ns._namespaces['CISCO-ENTITY-EXT-MIB']),
    'CISCOENTITYEXTMIB.CeExtEntityLEDTable.CeExtEntityLEDEntry.CeExtEntityLEDType_Enum' : _MetaInfoEnum('CeExtEntityLEDType_Enum', 'ydk.models.entity.CISCO_ENTITY_EXT_MIB',
        {
            'status':'STATUS',
            'system':'SYSTEM',
            'active':'ACTIVE',
            'power':'POWER',
            'battery':'BATTERY',
        }, 'CISCO-ENTITY-EXT-MIB', _yang_ns._namespaces['CISCO-ENTITY-EXT-MIB']),
    'CISCOENTITYEXTMIB.CeExtEntityLEDTable.CeExtEntityLEDEntry' : {
        'meta_info' : _MetaInfoClass('CISCOENTITYEXTMIB.CeExtEntityLEDTable.CeExtEntityLEDEntry',
            False, 
            [
            _MetaInfoClassMember('ceExtEntityLEDType', REFERENCE_ENUM_CLASS, 'CeExtEntityLEDType_Enum' , 'ydk.models.entity.CISCO_ENTITY_EXT_MIB', 'CISCOENTITYEXTMIB.CeExtEntityLEDTable.CeExtEntityLEDEntry.CeExtEntityLEDType_Enum', 
                [], [], 
                '''                The type of LED on this entity.
                'status' - indicates the entity status.
                'system' - indicates the overall system status. 
                'active' - the redundancy status of a module, for e.g.
                           supervisor module. 
                'power'  - indicates sufficient power availability for all 
                           modules.
                'battery'- indicates the battery status.
                ''',
                'ceextentityledtype',
                'CISCO-ENTITY-EXT-MIB', True),
            _MetaInfoClassMember('entPhysicalIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'entphysicalindex',
                'CISCO-ENTITY-EXT-MIB', True),
            _MetaInfoClassMember('ceExtEntityLEDColor', REFERENCE_ENUM_CLASS, 'CeExtEntityLEDColor_Enum' , 'ydk.models.entity.CISCO_ENTITY_EXT_MIB', 'CISCOENTITYEXTMIB.CeExtEntityLEDTable.CeExtEntityLEDEntry.CeExtEntityLEDColor_Enum', 
                [], [], 
                '''                The color of the LED.
                ''',
                'ceextentityledcolor',
                'CISCO-ENTITY-EXT-MIB', False),
            ],
            'CISCO-ENTITY-EXT-MIB',
            'ceExtEntityLEDEntry',
            _yang_ns._namespaces['CISCO-ENTITY-EXT-MIB'],
        'ydk.models.entity.CISCO_ENTITY_EXT_MIB'
        ),
    },
    'CISCOENTITYEXTMIB.CeExtEntityLEDTable' : {
        'meta_info' : _MetaInfoClass('CISCOENTITYEXTMIB.CeExtEntityLEDTable',
            False, 
            [
            _MetaInfoClassMember('ceExtEntityLEDEntry', REFERENCE_LIST, 'CeExtEntityLEDEntry' , 'ydk.models.entity.CISCO_ENTITY_EXT_MIB', 'CISCOENTITYEXTMIB.CeExtEntityLEDTable.CeExtEntityLEDEntry', 
                [], [], 
                '''                An entry (conceptual row) in the ceExtEntityLEDTable,
                containing information about an LED on an entity, identified by 
                entPhysicalIndex.
                ''',
                'ceextentityledentry',
                'CISCO-ENTITY-EXT-MIB', False),
            ],
            'CISCO-ENTITY-EXT-MIB',
            'ceExtEntityLEDTable',
            _yang_ns._namespaces['CISCO-ENTITY-EXT-MIB'],
        'ydk.models.entity.CISCO_ENTITY_EXT_MIB'
        ),
    },
    'CISCOENTITYEXTMIB.CeExtPhysicalProcessorTable.CeExtPhysicalProcessorEntry' : {
        'meta_info' : _MetaInfoClass('CISCOENTITYEXTMIB.CeExtPhysicalProcessorTable.CeExtPhysicalProcessorEntry',
            False, 
            [
            _MetaInfoClassMember('entPhysicalIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'entphysicalindex',
                'CISCO-ENTITY-EXT-MIB', True),
            _MetaInfoClassMember('ceExtHCProcessorRam', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                This object represents the total number of bytes of RAM
                available on the Processor. This object is a 64-bit version
                of ceExtProcessorRam.
                ''',
                'ceexthcprocessorram',
                'CISCO-ENTITY-EXT-MIB', False),
            _MetaInfoClassMember('ceExtNVRAMSize', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total number of bytes of NVRAM in the entity.
                
                A value of 0 for this object means the entity
                does not support NVRAM or NVRAM information 
                is not available.
                ''',
                'ceextnvramsize',
                'CISCO-ENTITY-EXT-MIB', False),
            _MetaInfoClassMember('ceExtNVRAMUsed', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of bytes of NVRAM in use. This object
                is irrelevant if ceExtNVRAMSize is 0.
                ''',
                'ceextnvramused',
                'CISCO-ENTITY-EXT-MIB', False),
            _MetaInfoClassMember('ceExtProcessorRam', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total number of bytes of RAM available on the
                Processor.
                ''',
                'ceextprocessorram',
                'CISCO-ENTITY-EXT-MIB', False),
            _MetaInfoClassMember('ceExtProcessorRamOverflow', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object represents the upper 32-bit of ceExtProcessorRam.
                This object needs to be supported only if the available RAM
                bytes exceeds 32-bit, otherwise this object value would be set
                to 0.
                ''',
                'ceextprocessorramoverflow',
                'CISCO-ENTITY-EXT-MIB', False),
            ],
            'CISCO-ENTITY-EXT-MIB',
            'ceExtPhysicalProcessorEntry',
            _yang_ns._namespaces['CISCO-ENTITY-EXT-MIB'],
        'ydk.models.entity.CISCO_ENTITY_EXT_MIB'
        ),
    },
    'CISCOENTITYEXTMIB.CeExtPhysicalProcessorTable' : {
        'meta_info' : _MetaInfoClass('CISCOENTITYEXTMIB.CeExtPhysicalProcessorTable',
            False, 
            [
            _MetaInfoClassMember('ceExtPhysicalProcessorEntry', REFERENCE_LIST, 'CeExtPhysicalProcessorEntry' , 'ydk.models.entity.CISCO_ENTITY_EXT_MIB', 'CISCOENTITYEXTMIB.CeExtPhysicalProcessorTable.CeExtPhysicalProcessorEntry', 
                [], [], 
                '''                A ceExtPhysicalProcessorTable entry extends
                a corresponding entPhysicalTable entry of class
                module(entPhysicalClass = 'module').
                
                A processor module or line card which 
                has a processor will have an entry in
                this table.
                
                A processor module or line card having
                multiple processors and is a SMP(Symmetric
                multi processor) system will have only 
                one entry corresponding to all the processors 
                since the resources defined below are shared.
                
                A processor module or line card having
                multiple processors and is not an SMP system
                would register the processors as separate entities.
                
                Entries are created by the agent at the system power-up
                or module insertion.
                
                Entries are removed when the module is reset or removed.
                ''',
                'ceextphysicalprocessorentry',
                'CISCO-ENTITY-EXT-MIB', False),
            ],
            'CISCO-ENTITY-EXT-MIB',
            'ceExtPhysicalProcessorTable',
            _yang_ns._namespaces['CISCO-ENTITY-EXT-MIB'],
        'ydk.models.entity.CISCO_ENTITY_EXT_MIB'
        ),
    },
    'CISCOENTITYEXTMIB' : {
        'meta_info' : _MetaInfoClass('CISCOENTITYEXTMIB',
            False, 
            [
            _MetaInfoClassMember('ceExtConfigRegTable', REFERENCE_CLASS, 'CeExtConfigRegTable' , 'ydk.models.entity.CISCO_ENTITY_EXT_MIB', 'CISCOENTITYEXTMIB.CeExtConfigRegTable', 
                [], [], 
                '''                The ceExtConfigRegTable extends
                the ENTITY-MIB entPhysicalTable.
                ''',
                'ceextconfigregtable',
                'CISCO-ENTITY-EXT-MIB', False),
            _MetaInfoClassMember('ceExtEntityLEDTable', REFERENCE_CLASS, 'CeExtEntityLEDTable' , 'ydk.models.entity.CISCO_ENTITY_EXT_MIB', 'CISCOENTITYEXTMIB.CeExtEntityLEDTable', 
                [], [], 
                '''                A table containing information of LED on an entity.
                ''',
                'ceextentityledtable',
                'CISCO-ENTITY-EXT-MIB', False),
            _MetaInfoClassMember('ceExtPhysicalProcessorTable', REFERENCE_CLASS, 'CeExtPhysicalProcessorTable' , 'ydk.models.entity.CISCO_ENTITY_EXT_MIB', 'CISCOENTITYEXTMIB.CeExtPhysicalProcessorTable', 
                [], [], 
                '''                The ceExtPhysicalProcessorTable extends
                the ENTITY-MIB entPhysicalTable for modules
                (Non FRUs(Field Replacable Units) or FRUs).
                ''',
                'ceextphysicalprocessortable',
                'CISCO-ENTITY-EXT-MIB', False),
            ],
            'CISCO-ENTITY-EXT-MIB',
            'CISCO-ENTITY-EXT-MIB',
            _yang_ns._namespaces['CISCO-ENTITY-EXT-MIB'],
        'ydk.models.entity.CISCO_ENTITY_EXT_MIB'
        ),
    },
}
_meta_table['CISCOENTITYEXTMIB.CeExtConfigRegTable.CeExtConfigRegEntry']['meta_info'].parent =_meta_table['CISCOENTITYEXTMIB.CeExtConfigRegTable']['meta_info']
_meta_table['CISCOENTITYEXTMIB.CeExtEntityLEDTable.CeExtEntityLEDEntry']['meta_info'].parent =_meta_table['CISCOENTITYEXTMIB.CeExtEntityLEDTable']['meta_info']
_meta_table['CISCOENTITYEXTMIB.CeExtPhysicalProcessorTable.CeExtPhysicalProcessorEntry']['meta_info'].parent =_meta_table['CISCOENTITYEXTMIB.CeExtPhysicalProcessorTable']['meta_info']
_meta_table['CISCOENTITYEXTMIB.CeExtConfigRegTable']['meta_info'].parent =_meta_table['CISCOENTITYEXTMIB']['meta_info']
_meta_table['CISCOENTITYEXTMIB.CeExtEntityLEDTable']['meta_info'].parent =_meta_table['CISCOENTITYEXTMIB']['meta_info']
_meta_table['CISCOENTITYEXTMIB.CeExtPhysicalProcessorTable']['meta_info'].parent =_meta_table['CISCOENTITYEXTMIB']['meta_info']
