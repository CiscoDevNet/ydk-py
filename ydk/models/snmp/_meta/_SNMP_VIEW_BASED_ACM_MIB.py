


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'VacmViewTreeFamilyTypeType_Enum' : _MetaInfoEnum('VacmViewTreeFamilyTypeType_Enum', 'ydk.models.snmp.SNMP_VIEW_BASED_ACM_MIB',
        {
            'included':'INCLUDED',
            'excluded':'EXCLUDED',
        }, 'SNMP-VIEW-BASED-ACM-MIB', _yang_ns._namespaces['SNMP-VIEW-BASED-ACM-MIB']),
    'VacmAccessContextMatchType_Enum' : _MetaInfoEnum('VacmAccessContextMatchType_Enum', 'ydk.models.snmp.SNMP_VIEW_BASED_ACM_MIB',
        {
            'exact':'EXACT',
            'prefix':'PREFIX',
        }, 'SNMP-VIEW-BASED-ACM-MIB', _yang_ns._namespaces['SNMP-VIEW-BASED-ACM-MIB']),
    'SNMPVIEWBASEDACMMIB.VacmAccessTable.VacmAccessEntry' : {
        'meta_info' : _MetaInfoClass('SNMPVIEWBASEDACMMIB.VacmAccessTable.VacmAccessEntry',
            False, 
            [
            _MetaInfoClassMember('vacmAccessContextPrefix', ATTRIBUTE, 'str' , None, None, 
                [('0', 32)], [], 
                '''                ''',
                'vacmaccesscontextprefix',
                'SNMP-VIEW-BASED-ACM-MIB', True),
            _MetaInfoClassMember('vacmAccessSecurityLevel', REFERENCE_ENUM_CLASS, 'SnmpSecurityLevel_Enum' , 'ydk.models.snmp.SNMP_FRAMEWORK_MIB', 'SnmpSecurityLevel_Enum', 
                [], [], 
                '''                ''',
                'vacmaccesssecuritylevel',
                'SNMP-VIEW-BASED-ACM-MIB', True),
            _MetaInfoClassMember('vacmAccessSecurityModel', ATTRIBUTE, 'int' , None, None, 
                [(0, 2147483647)], [], 
                '''                ''',
                'vacmaccesssecuritymodel',
                'SNMP-VIEW-BASED-ACM-MIB', True),
            _MetaInfoClassMember('vacmGroupName', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                ''',
                'vacmgroupname',
                'SNMP-VIEW-BASED-ACM-MIB', True),
            _MetaInfoClassMember('vacmAccessContextMatch', REFERENCE_ENUM_CLASS, 'VacmAccessContextMatchType_Enum' , 'ydk.models.snmp.SNMP_VIEW_BASED_ACM_MIB', 'VacmAccessContextMatchType_Enum', 
                [], [], 
                '''                ''',
                'vacmaccesscontextmatch',
                'SNMP-VIEW-BASED-ACM-MIB', False),
            _MetaInfoClassMember('vacmAccessNotifyViewName', ATTRIBUTE, 'str' , None, None, 
                [('0', 32)], [], 
                '''                ''',
                'vacmaccessnotifyviewname',
                'SNMP-VIEW-BASED-ACM-MIB', False),
            _MetaInfoClassMember('vacmAccessReadViewName', ATTRIBUTE, 'str' , None, None, 
                [('0', 32)], [], 
                '''                ''',
                'vacmaccessreadviewname',
                'SNMP-VIEW-BASED-ACM-MIB', False),
            _MetaInfoClassMember('vacmAccessStorageType', REFERENCE_ENUM_CLASS, 'StorageType_Enum' , 'ydk.models.snmpv2.SNMPv2_TC', 'StorageType_Enum', 
                [], [], 
                '''                ''',
                'vacmaccessstoragetype',
                'SNMP-VIEW-BASED-ACM-MIB', False),
            _MetaInfoClassMember('vacmAccessWriteViewName', ATTRIBUTE, 'str' , None, None, 
                [('0', 32)], [], 
                '''                ''',
                'vacmaccesswriteviewname',
                'SNMP-VIEW-BASED-ACM-MIB', False),
            ],
            'SNMP-VIEW-BASED-ACM-MIB',
            'vacmAccessEntry',
            _yang_ns._namespaces['SNMP-VIEW-BASED-ACM-MIB'],
        'ydk.models.snmp.SNMP_VIEW_BASED_ACM_MIB'
        ),
    },
    'SNMPVIEWBASEDACMMIB.VacmAccessTable' : {
        'meta_info' : _MetaInfoClass('SNMPVIEWBASEDACMMIB.VacmAccessTable',
            False, 
            [
            _MetaInfoClassMember('vacmAccessEntry', REFERENCE_LIST, 'VacmAccessEntry' , 'ydk.models.snmp.SNMP_VIEW_BASED_ACM_MIB', 'SNMPVIEWBASEDACMMIB.VacmAccessTable.VacmAccessEntry', 
                [], [], 
                '''                ''',
                'vacmaccessentry',
                'SNMP-VIEW-BASED-ACM-MIB', False),
            ],
            'SNMP-VIEW-BASED-ACM-MIB',
            'vacmAccessTable',
            _yang_ns._namespaces['SNMP-VIEW-BASED-ACM-MIB'],
        'ydk.models.snmp.SNMP_VIEW_BASED_ACM_MIB'
        ),
    },
    'SNMPVIEWBASEDACMMIB.VacmSecurityToGroupTable.VacmSecurityToGroupEntry' : {
        'meta_info' : _MetaInfoClass('SNMPVIEWBASEDACMMIB.VacmSecurityToGroupTable.VacmSecurityToGroupEntry',
            False, 
            [
            _MetaInfoClassMember('vacmSecurityModel', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'vacmsecuritymodel',
                'SNMP-VIEW-BASED-ACM-MIB', True),
            _MetaInfoClassMember('vacmSecurityName', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                ''',
                'vacmsecurityname',
                'SNMP-VIEW-BASED-ACM-MIB', True),
            _MetaInfoClassMember('vacmGroupName', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                ''',
                'vacmgroupname',
                'SNMP-VIEW-BASED-ACM-MIB', False),
            _MetaInfoClassMember('vacmSecurityToGroupStorageType', REFERENCE_ENUM_CLASS, 'StorageType_Enum' , 'ydk.models.snmpv2.SNMPv2_TC', 'StorageType_Enum', 
                [], [], 
                '''                ''',
                'vacmsecuritytogroupstoragetype',
                'SNMP-VIEW-BASED-ACM-MIB', False),
            ],
            'SNMP-VIEW-BASED-ACM-MIB',
            'vacmSecurityToGroupEntry',
            _yang_ns._namespaces['SNMP-VIEW-BASED-ACM-MIB'],
        'ydk.models.snmp.SNMP_VIEW_BASED_ACM_MIB'
        ),
    },
    'SNMPVIEWBASEDACMMIB.VacmSecurityToGroupTable' : {
        'meta_info' : _MetaInfoClass('SNMPVIEWBASEDACMMIB.VacmSecurityToGroupTable',
            False, 
            [
            _MetaInfoClassMember('vacmSecurityToGroupEntry', REFERENCE_LIST, 'VacmSecurityToGroupEntry' , 'ydk.models.snmp.SNMP_VIEW_BASED_ACM_MIB', 'SNMPVIEWBASEDACMMIB.VacmSecurityToGroupTable.VacmSecurityToGroupEntry', 
                [], [], 
                '''                ''',
                'vacmsecuritytogroupentry',
                'SNMP-VIEW-BASED-ACM-MIB', False),
            ],
            'SNMP-VIEW-BASED-ACM-MIB',
            'vacmSecurityToGroupTable',
            _yang_ns._namespaces['SNMP-VIEW-BASED-ACM-MIB'],
        'ydk.models.snmp.SNMP_VIEW_BASED_ACM_MIB'
        ),
    },
    'SNMPVIEWBASEDACMMIB.VacmViewTreeFamilyTable.VacmViewTreeFamilyEntry' : {
        'meta_info' : _MetaInfoClass('SNMPVIEWBASEDACMMIB.VacmViewTreeFamilyTable.VacmViewTreeFamilyEntry',
            False, 
            [
            _MetaInfoClassMember('vacmViewTreeFamilySubtree', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-1](\\.[1-3]?[0-9]))|(2\\.(0|([1-9]\\d*))))(\\.(0|([1-9]\\d*)))*'], 
                '''                ''',
                'vacmviewtreefamilysubtree',
                'SNMP-VIEW-BASED-ACM-MIB', True),
            _MetaInfoClassMember('vacmViewTreeFamilyViewName', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                ''',
                'vacmviewtreefamilyviewname',
                'SNMP-VIEW-BASED-ACM-MIB', True),
            _MetaInfoClassMember('vacmViewTreeFamilyMask', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9a-fA-F]){2}(:([0-9a-fA-F]){2})*)?'], 
                '''                ''',
                'vacmviewtreefamilymask',
                'SNMP-VIEW-BASED-ACM-MIB', False),
            _MetaInfoClassMember('vacmViewTreeFamilyStorageType', REFERENCE_ENUM_CLASS, 'StorageType_Enum' , 'ydk.models.snmpv2.SNMPv2_TC', 'StorageType_Enum', 
                [], [], 
                '''                ''',
                'vacmviewtreefamilystoragetype',
                'SNMP-VIEW-BASED-ACM-MIB', False),
            _MetaInfoClassMember('vacmViewTreeFamilyType', REFERENCE_ENUM_CLASS, 'VacmViewTreeFamilyTypeType_Enum' , 'ydk.models.snmp.SNMP_VIEW_BASED_ACM_MIB', 'VacmViewTreeFamilyTypeType_Enum', 
                [], [], 
                '''                ''',
                'vacmviewtreefamilytype',
                'SNMP-VIEW-BASED-ACM-MIB', False),
            ],
            'SNMP-VIEW-BASED-ACM-MIB',
            'vacmViewTreeFamilyEntry',
            _yang_ns._namespaces['SNMP-VIEW-BASED-ACM-MIB'],
        'ydk.models.snmp.SNMP_VIEW_BASED_ACM_MIB'
        ),
    },
    'SNMPVIEWBASEDACMMIB.VacmViewTreeFamilyTable' : {
        'meta_info' : _MetaInfoClass('SNMPVIEWBASEDACMMIB.VacmViewTreeFamilyTable',
            False, 
            [
            _MetaInfoClassMember('vacmViewTreeFamilyEntry', REFERENCE_LIST, 'VacmViewTreeFamilyEntry' , 'ydk.models.snmp.SNMP_VIEW_BASED_ACM_MIB', 'SNMPVIEWBASEDACMMIB.VacmViewTreeFamilyTable.VacmViewTreeFamilyEntry', 
                [], [], 
                '''                ''',
                'vacmviewtreefamilyentry',
                'SNMP-VIEW-BASED-ACM-MIB', False),
            ],
            'SNMP-VIEW-BASED-ACM-MIB',
            'vacmViewTreeFamilyTable',
            _yang_ns._namespaces['SNMP-VIEW-BASED-ACM-MIB'],
        'ydk.models.snmp.SNMP_VIEW_BASED_ACM_MIB'
        ),
    },
    'SNMPVIEWBASEDACMMIB' : {
        'meta_info' : _MetaInfoClass('SNMPVIEWBASEDACMMIB',
            False, 
            [
            _MetaInfoClassMember('vacmAccessTable', REFERENCE_CLASS, 'VacmAccessTable' , 'ydk.models.snmp.SNMP_VIEW_BASED_ACM_MIB', 'SNMPVIEWBASEDACMMIB.VacmAccessTable', 
                [], [], 
                '''                ''',
                'vacmaccesstable',
                'SNMP-VIEW-BASED-ACM-MIB', False),
            _MetaInfoClassMember('vacmSecurityToGroupTable', REFERENCE_CLASS, 'VacmSecurityToGroupTable' , 'ydk.models.snmp.SNMP_VIEW_BASED_ACM_MIB', 'SNMPVIEWBASEDACMMIB.VacmSecurityToGroupTable', 
                [], [], 
                '''                ''',
                'vacmsecuritytogrouptable',
                'SNMP-VIEW-BASED-ACM-MIB', False),
            _MetaInfoClassMember('vacmViewTreeFamilyTable', REFERENCE_CLASS, 'VacmViewTreeFamilyTable' , 'ydk.models.snmp.SNMP_VIEW_BASED_ACM_MIB', 'SNMPVIEWBASEDACMMIB.VacmViewTreeFamilyTable', 
                [], [], 
                '''                ''',
                'vacmviewtreefamilytable',
                'SNMP-VIEW-BASED-ACM-MIB', False),
            ],
            'SNMP-VIEW-BASED-ACM-MIB',
            'SNMP-VIEW-BASED-ACM-MIB',
            _yang_ns._namespaces['SNMP-VIEW-BASED-ACM-MIB'],
        'ydk.models.snmp.SNMP_VIEW_BASED_ACM_MIB'
        ),
    },
}
_meta_table['SNMPVIEWBASEDACMMIB.VacmAccessTable.VacmAccessEntry']['meta_info'].parent =_meta_table['SNMPVIEWBASEDACMMIB.VacmAccessTable']['meta_info']
_meta_table['SNMPVIEWBASEDACMMIB.VacmSecurityToGroupTable.VacmSecurityToGroupEntry']['meta_info'].parent =_meta_table['SNMPVIEWBASEDACMMIB.VacmSecurityToGroupTable']['meta_info']
_meta_table['SNMPVIEWBASEDACMMIB.VacmViewTreeFamilyTable.VacmViewTreeFamilyEntry']['meta_info'].parent =_meta_table['SNMPVIEWBASEDACMMIB.VacmViewTreeFamilyTable']['meta_info']
_meta_table['SNMPVIEWBASEDACMMIB.VacmAccessTable']['meta_info'].parent =_meta_table['SNMPVIEWBASEDACMMIB']['meta_info']
_meta_table['SNMPVIEWBASEDACMMIB.VacmSecurityToGroupTable']['meta_info'].parent =_meta_table['SNMPVIEWBASEDACMMIB']['meta_info']
_meta_table['SNMPVIEWBASEDACMMIB.VacmViewTreeFamilyTable']['meta_info'].parent =_meta_table['SNMPVIEWBASEDACMMIB']['meta_info']
