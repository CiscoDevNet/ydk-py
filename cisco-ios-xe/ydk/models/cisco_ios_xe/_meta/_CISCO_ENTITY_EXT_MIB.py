


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'CiscoEntityExtMib.Ceextphysicalprocessortable.Ceextphysicalprocessorentry' : {
        'meta_info' : _MetaInfoClass('CiscoEntityExtMib.Ceextphysicalprocessortable.Ceextphysicalprocessorentry',
            False, 
            [
            _MetaInfoClassMember('entPhysicalIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'entphysicalindex',
                'CISCO-ENTITY-EXT-MIB', True),
            _MetaInfoClassMember('ceExtHCProcessorRam', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                This object represents the total number of bytes of RAM
                available on the Processor. This object is a 64-bit version
                of ceExtProcessorRam.
                ''',
                'ceexthcprocessorram',
                'CISCO-ENTITY-EXT-MIB', False),
            _MetaInfoClassMember('ceExtNVRAMSize', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total number of bytes of NVRAM in the entity.
                
                A value of 0 for this object means the entity
                does not support NVRAM or NVRAM information 
                is not available.
                ''',
                'ceextnvramsize',
                'CISCO-ENTITY-EXT-MIB', False),
            _MetaInfoClassMember('ceExtNVRAMUsed', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of bytes of NVRAM in use. This object
                is irrelevant if ceExtNVRAMSize is 0.
                ''',
                'ceextnvramused',
                'CISCO-ENTITY-EXT-MIB', False),
            _MetaInfoClassMember('ceExtProcessorRam', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total number of bytes of RAM available on the
                Processor.
                ''',
                'ceextprocessorram',
                'CISCO-ENTITY-EXT-MIB', False),
            _MetaInfoClassMember('ceExtProcessorRamOverflow', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
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
        'ydk.models.cisco_ios_xe.CISCO_ENTITY_EXT_MIB'
        ),
    },
    'CiscoEntityExtMib.Ceextphysicalprocessortable' : {
        'meta_info' : _MetaInfoClass('CiscoEntityExtMib.Ceextphysicalprocessortable',
            False, 
            [
            _MetaInfoClassMember('ceExtPhysicalProcessorEntry', REFERENCE_LIST, 'Ceextphysicalprocessorentry' , 'ydk.models.cisco_ios_xe.CISCO_ENTITY_EXT_MIB', 'CiscoEntityExtMib.Ceextphysicalprocessortable.Ceextphysicalprocessorentry', 
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
        'ydk.models.cisco_ios_xe.CISCO_ENTITY_EXT_MIB'
        ),
    },
    'CiscoEntityExtMib.Ceextconfigregtable.Ceextconfigregentry' : {
        'meta_info' : _MetaInfoClass('CiscoEntityExtMib.Ceextconfigregtable.Ceextconfigregentry',
            False, 
            [
            _MetaInfoClassMember('entPhysicalIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
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
        'ydk.models.cisco_ios_xe.CISCO_ENTITY_EXT_MIB'
        ),
    },
    'CiscoEntityExtMib.Ceextconfigregtable' : {
        'meta_info' : _MetaInfoClass('CiscoEntityExtMib.Ceextconfigregtable',
            False, 
            [
            _MetaInfoClassMember('ceExtConfigRegEntry', REFERENCE_LIST, 'Ceextconfigregentry' , 'ydk.models.cisco_ios_xe.CISCO_ENTITY_EXT_MIB', 'CiscoEntityExtMib.Ceextconfigregtable.Ceextconfigregentry', 
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
        'ydk.models.cisco_ios_xe.CISCO_ENTITY_EXT_MIB'
        ),
    },
    'CiscoEntityExtMib.Ceextentityledtable.Ceextentityledentry.CeextentityledcolorEnum' : _MetaInfoEnum('CeextentityledcolorEnum', 'ydk.models.cisco_ios_xe.CISCO_ENTITY_EXT_MIB',
        {
            'off':'off',
            'green':'green',
            'amber':'amber',
            'red':'red',
        }, 'CISCO-ENTITY-EXT-MIB', _yang_ns._namespaces['CISCO-ENTITY-EXT-MIB']),
    'CiscoEntityExtMib.Ceextentityledtable.Ceextentityledentry.CeextentityledtypeEnum' : _MetaInfoEnum('CeextentityledtypeEnum', 'ydk.models.cisco_ios_xe.CISCO_ENTITY_EXT_MIB',
        {
            'status':'status',
            'system':'system',
            'active':'active',
            'power':'power',
            'battery':'battery',
        }, 'CISCO-ENTITY-EXT-MIB', _yang_ns._namespaces['CISCO-ENTITY-EXT-MIB']),
    'CiscoEntityExtMib.Ceextentityledtable.Ceextentityledentry' : {
        'meta_info' : _MetaInfoClass('CiscoEntityExtMib.Ceextentityledtable.Ceextentityledentry',
            False, 
            [
            _MetaInfoClassMember('entPhysicalIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'entphysicalindex',
                'CISCO-ENTITY-EXT-MIB', True),
            _MetaInfoClassMember('ceExtEntityLEDType', REFERENCE_ENUM_CLASS, 'CeextentityledtypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_ENTITY_EXT_MIB', 'CiscoEntityExtMib.Ceextentityledtable.Ceextentityledentry.CeextentityledtypeEnum', 
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
            _MetaInfoClassMember('ceExtEntityLEDColor', REFERENCE_ENUM_CLASS, 'CeextentityledcolorEnum' , 'ydk.models.cisco_ios_xe.CISCO_ENTITY_EXT_MIB', 'CiscoEntityExtMib.Ceextentityledtable.Ceextentityledentry.CeextentityledcolorEnum', 
                [], [], 
                '''                The color of the LED.
                ''',
                'ceextentityledcolor',
                'CISCO-ENTITY-EXT-MIB', False),
            ],
            'CISCO-ENTITY-EXT-MIB',
            'ceExtEntityLEDEntry',
            _yang_ns._namespaces['CISCO-ENTITY-EXT-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_ENTITY_EXT_MIB'
        ),
    },
    'CiscoEntityExtMib.Ceextentityledtable' : {
        'meta_info' : _MetaInfoClass('CiscoEntityExtMib.Ceextentityledtable',
            False, 
            [
            _MetaInfoClassMember('ceExtEntityLEDEntry', REFERENCE_LIST, 'Ceextentityledentry' , 'ydk.models.cisco_ios_xe.CISCO_ENTITY_EXT_MIB', 'CiscoEntityExtMib.Ceextentityledtable.Ceextentityledentry', 
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
        'ydk.models.cisco_ios_xe.CISCO_ENTITY_EXT_MIB'
        ),
    },
    'CiscoEntityExtMib' : {
        'meta_info' : _MetaInfoClass('CiscoEntityExtMib',
            False, 
            [
            _MetaInfoClassMember('ceExtConfigRegTable', REFERENCE_CLASS, 'Ceextconfigregtable' , 'ydk.models.cisco_ios_xe.CISCO_ENTITY_EXT_MIB', 'CiscoEntityExtMib.Ceextconfigregtable', 
                [], [], 
                '''                The ceExtConfigRegTable extends
                the ENTITY-MIB entPhysicalTable.
                ''',
                'ceextconfigregtable',
                'CISCO-ENTITY-EXT-MIB', False),
            _MetaInfoClassMember('ceExtEntityLEDTable', REFERENCE_CLASS, 'Ceextentityledtable' , 'ydk.models.cisco_ios_xe.CISCO_ENTITY_EXT_MIB', 'CiscoEntityExtMib.Ceextentityledtable', 
                [], [], 
                '''                A table containing information of LED on an entity.
                ''',
                'ceextentityledtable',
                'CISCO-ENTITY-EXT-MIB', False),
            _MetaInfoClassMember('ceExtPhysicalProcessorTable', REFERENCE_CLASS, 'Ceextphysicalprocessortable' , 'ydk.models.cisco_ios_xe.CISCO_ENTITY_EXT_MIB', 'CiscoEntityExtMib.Ceextphysicalprocessortable', 
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
        'ydk.models.cisco_ios_xe.CISCO_ENTITY_EXT_MIB'
        ),
    },
}
_meta_table['CiscoEntityExtMib.Ceextphysicalprocessortable.Ceextphysicalprocessorentry']['meta_info'].parent =_meta_table['CiscoEntityExtMib.Ceextphysicalprocessortable']['meta_info']
_meta_table['CiscoEntityExtMib.Ceextconfigregtable.Ceextconfigregentry']['meta_info'].parent =_meta_table['CiscoEntityExtMib.Ceextconfigregtable']['meta_info']
_meta_table['CiscoEntityExtMib.Ceextentityledtable.Ceextentityledentry']['meta_info'].parent =_meta_table['CiscoEntityExtMib.Ceextentityledtable']['meta_info']
_meta_table['CiscoEntityExtMib.Ceextphysicalprocessortable']['meta_info'].parent =_meta_table['CiscoEntityExtMib']['meta_info']
_meta_table['CiscoEntityExtMib.Ceextconfigregtable']['meta_info'].parent =_meta_table['CiscoEntityExtMib']['meta_info']
_meta_table['CiscoEntityExtMib.Ceextentityledtable']['meta_info'].parent =_meta_table['CiscoEntityExtMib']['meta_info']
