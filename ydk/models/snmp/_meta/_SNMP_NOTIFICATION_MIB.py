


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'SnmpNotifyTypeType_Enum' : _MetaInfoEnum('SnmpNotifyTypeType_Enum', 'ydk.models.snmp.SNMP_NOTIFICATION_MIB',
        {
            'trap':'TRAP',
            'inform':'INFORM',
        }, 'SNMP-NOTIFICATION-MIB', _yang_ns._namespaces['SNMP-NOTIFICATION-MIB']),
    'SnmpNotifyFilterTypeType_Enum' : _MetaInfoEnum('SnmpNotifyFilterTypeType_Enum', 'ydk.models.snmp.SNMP_NOTIFICATION_MIB',
        {
            'included':'INCLUDED',
            'excluded':'EXCLUDED',
        }, 'SNMP-NOTIFICATION-MIB', _yang_ns._namespaces['SNMP-NOTIFICATION-MIB']),
    'SNMPNOTIFICATIONMIB.SnmpNotifyFilterProfileTable.SnmpNotifyFilterProfileEntry' : {
        'meta_info' : _MetaInfoClass('SNMPNOTIFICATIONMIB.SnmpNotifyFilterProfileTable.SnmpNotifyFilterProfileEntry',
            False, 
            [
            _MetaInfoClassMember('snmpTargetParamsName', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                ''',
                'snmptargetparamsname',
                'SNMP-NOTIFICATION-MIB', True),
            _MetaInfoClassMember('snmpNotifyFilterProfileName', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                ''',
                'snmpnotifyfilterprofilename',
                'SNMP-NOTIFICATION-MIB', False),
            _MetaInfoClassMember('snmpNotifyFilterProfileStorType', REFERENCE_ENUM_CLASS, 'StorageType_Enum' , 'ydk.models.snmpv2.SNMPv2_TC', 'StorageType_Enum', 
                [], [], 
                '''                ''',
                'snmpnotifyfilterprofilestortype',
                'SNMP-NOTIFICATION-MIB', False),
            ],
            'SNMP-NOTIFICATION-MIB',
            'snmpNotifyFilterProfileEntry',
            _yang_ns._namespaces['SNMP-NOTIFICATION-MIB'],
        'ydk.models.snmp.SNMP_NOTIFICATION_MIB'
        ),
    },
    'SNMPNOTIFICATIONMIB.SnmpNotifyFilterProfileTable' : {
        'meta_info' : _MetaInfoClass('SNMPNOTIFICATIONMIB.SnmpNotifyFilterProfileTable',
            False, 
            [
            _MetaInfoClassMember('snmpNotifyFilterProfileEntry', REFERENCE_LIST, 'SnmpNotifyFilterProfileEntry' , 'ydk.models.snmp.SNMP_NOTIFICATION_MIB', 'SNMPNOTIFICATIONMIB.SnmpNotifyFilterProfileTable.SnmpNotifyFilterProfileEntry', 
                [], [], 
                '''                ''',
                'snmpnotifyfilterprofileentry',
                'SNMP-NOTIFICATION-MIB', False),
            ],
            'SNMP-NOTIFICATION-MIB',
            'snmpNotifyFilterProfileTable',
            _yang_ns._namespaces['SNMP-NOTIFICATION-MIB'],
        'ydk.models.snmp.SNMP_NOTIFICATION_MIB'
        ),
    },
    'SNMPNOTIFICATIONMIB.SnmpNotifyFilterTable.SnmpNotifyFilterEntry' : {
        'meta_info' : _MetaInfoClass('SNMPNOTIFICATIONMIB.SnmpNotifyFilterTable.SnmpNotifyFilterEntry',
            False, 
            [
            _MetaInfoClassMember('snmpNotifyFilterProfileName', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                ''',
                'snmpnotifyfilterprofilename',
                'SNMP-NOTIFICATION-MIB', True),
            _MetaInfoClassMember('snmpNotifyFilterSubtree', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-1](\\.[1-3]?[0-9]))|(2\\.(0|([1-9]\\d*))))(\\.(0|([1-9]\\d*)))*'], 
                '''                ''',
                'snmpnotifyfiltersubtree',
                'SNMP-NOTIFICATION-MIB', True),
            _MetaInfoClassMember('snmpNotifyFilterMask', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9a-fA-F]){2}(:([0-9a-fA-F]){2})*)?'], 
                '''                ''',
                'snmpnotifyfiltermask',
                'SNMP-NOTIFICATION-MIB', False),
            _MetaInfoClassMember('snmpNotifyFilterStorageType', REFERENCE_ENUM_CLASS, 'StorageType_Enum' , 'ydk.models.snmpv2.SNMPv2_TC', 'StorageType_Enum', 
                [], [], 
                '''                ''',
                'snmpnotifyfilterstoragetype',
                'SNMP-NOTIFICATION-MIB', False),
            _MetaInfoClassMember('snmpNotifyFilterType', REFERENCE_ENUM_CLASS, 'SnmpNotifyFilterTypeType_Enum' , 'ydk.models.snmp.SNMP_NOTIFICATION_MIB', 'SnmpNotifyFilterTypeType_Enum', 
                [], [], 
                '''                ''',
                'snmpnotifyfiltertype',
                'SNMP-NOTIFICATION-MIB', False),
            ],
            'SNMP-NOTIFICATION-MIB',
            'snmpNotifyFilterEntry',
            _yang_ns._namespaces['SNMP-NOTIFICATION-MIB'],
        'ydk.models.snmp.SNMP_NOTIFICATION_MIB'
        ),
    },
    'SNMPNOTIFICATIONMIB.SnmpNotifyFilterTable' : {
        'meta_info' : _MetaInfoClass('SNMPNOTIFICATIONMIB.SnmpNotifyFilterTable',
            False, 
            [
            _MetaInfoClassMember('snmpNotifyFilterEntry', REFERENCE_LIST, 'SnmpNotifyFilterEntry' , 'ydk.models.snmp.SNMP_NOTIFICATION_MIB', 'SNMPNOTIFICATIONMIB.SnmpNotifyFilterTable.SnmpNotifyFilterEntry', 
                [], [], 
                '''                ''',
                'snmpnotifyfilterentry',
                'SNMP-NOTIFICATION-MIB', False),
            ],
            'SNMP-NOTIFICATION-MIB',
            'snmpNotifyFilterTable',
            _yang_ns._namespaces['SNMP-NOTIFICATION-MIB'],
        'ydk.models.snmp.SNMP_NOTIFICATION_MIB'
        ),
    },
    'SNMPNOTIFICATIONMIB.SnmpNotifyTable.SnmpNotifyEntry' : {
        'meta_info' : _MetaInfoClass('SNMPNOTIFICATIONMIB.SnmpNotifyTable.SnmpNotifyEntry',
            False, 
            [
            _MetaInfoClassMember('snmpNotifyName', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                ''',
                'snmpnotifyname',
                'SNMP-NOTIFICATION-MIB', True),
            _MetaInfoClassMember('snmpNotifyStorageType', REFERENCE_ENUM_CLASS, 'StorageType_Enum' , 'ydk.models.snmpv2.SNMPv2_TC', 'StorageType_Enum', 
                [], [], 
                '''                ''',
                'snmpnotifystoragetype',
                'SNMP-NOTIFICATION-MIB', False),
            _MetaInfoClassMember('snmpNotifyTag', ATTRIBUTE, 'str' , None, None, 
                [('0', 255)], [], 
                '''                ''',
                'snmpnotifytag',
                'SNMP-NOTIFICATION-MIB', False),
            _MetaInfoClassMember('snmpNotifyType', REFERENCE_ENUM_CLASS, 'SnmpNotifyTypeType_Enum' , 'ydk.models.snmp.SNMP_NOTIFICATION_MIB', 'SnmpNotifyTypeType_Enum', 
                [], [], 
                '''                ''',
                'snmpnotifytype',
                'SNMP-NOTIFICATION-MIB', False),
            ],
            'SNMP-NOTIFICATION-MIB',
            'snmpNotifyEntry',
            _yang_ns._namespaces['SNMP-NOTIFICATION-MIB'],
        'ydk.models.snmp.SNMP_NOTIFICATION_MIB'
        ),
    },
    'SNMPNOTIFICATIONMIB.SnmpNotifyTable' : {
        'meta_info' : _MetaInfoClass('SNMPNOTIFICATIONMIB.SnmpNotifyTable',
            False, 
            [
            _MetaInfoClassMember('snmpNotifyEntry', REFERENCE_LIST, 'SnmpNotifyEntry' , 'ydk.models.snmp.SNMP_NOTIFICATION_MIB', 'SNMPNOTIFICATIONMIB.SnmpNotifyTable.SnmpNotifyEntry', 
                [], [], 
                '''                ''',
                'snmpnotifyentry',
                'SNMP-NOTIFICATION-MIB', False),
            ],
            'SNMP-NOTIFICATION-MIB',
            'snmpNotifyTable',
            _yang_ns._namespaces['SNMP-NOTIFICATION-MIB'],
        'ydk.models.snmp.SNMP_NOTIFICATION_MIB'
        ),
    },
    'SNMPNOTIFICATIONMIB' : {
        'meta_info' : _MetaInfoClass('SNMPNOTIFICATIONMIB',
            False, 
            [
            _MetaInfoClassMember('snmpNotifyFilterProfileTable', REFERENCE_CLASS, 'SnmpNotifyFilterProfileTable' , 'ydk.models.snmp.SNMP_NOTIFICATION_MIB', 'SNMPNOTIFICATIONMIB.SnmpNotifyFilterProfileTable', 
                [], [], 
                '''                ''',
                'snmpnotifyfilterprofiletable',
                'SNMP-NOTIFICATION-MIB', False),
            _MetaInfoClassMember('snmpNotifyFilterTable', REFERENCE_CLASS, 'SnmpNotifyFilterTable' , 'ydk.models.snmp.SNMP_NOTIFICATION_MIB', 'SNMPNOTIFICATIONMIB.SnmpNotifyFilterTable', 
                [], [], 
                '''                ''',
                'snmpnotifyfiltertable',
                'SNMP-NOTIFICATION-MIB', False),
            _MetaInfoClassMember('snmpNotifyTable', REFERENCE_CLASS, 'SnmpNotifyTable' , 'ydk.models.snmp.SNMP_NOTIFICATION_MIB', 'SNMPNOTIFICATIONMIB.SnmpNotifyTable', 
                [], [], 
                '''                ''',
                'snmpnotifytable',
                'SNMP-NOTIFICATION-MIB', False),
            ],
            'SNMP-NOTIFICATION-MIB',
            'SNMP-NOTIFICATION-MIB',
            _yang_ns._namespaces['SNMP-NOTIFICATION-MIB'],
        'ydk.models.snmp.SNMP_NOTIFICATION_MIB'
        ),
    },
}
_meta_table['SNMPNOTIFICATIONMIB.SnmpNotifyFilterProfileTable.SnmpNotifyFilterProfileEntry']['meta_info'].parent =_meta_table['SNMPNOTIFICATIONMIB.SnmpNotifyFilterProfileTable']['meta_info']
_meta_table['SNMPNOTIFICATIONMIB.SnmpNotifyFilterTable.SnmpNotifyFilterEntry']['meta_info'].parent =_meta_table['SNMPNOTIFICATIONMIB.SnmpNotifyFilterTable']['meta_info']
_meta_table['SNMPNOTIFICATIONMIB.SnmpNotifyTable.SnmpNotifyEntry']['meta_info'].parent =_meta_table['SNMPNOTIFICATIONMIB.SnmpNotifyTable']['meta_info']
_meta_table['SNMPNOTIFICATIONMIB.SnmpNotifyFilterProfileTable']['meta_info'].parent =_meta_table['SNMPNOTIFICATIONMIB']['meta_info']
_meta_table['SNMPNOTIFICATIONMIB.SnmpNotifyFilterTable']['meta_info'].parent =_meta_table['SNMPNOTIFICATIONMIB']['meta_info']
_meta_table['SNMPNOTIFICATIONMIB.SnmpNotifyTable']['meta_info'].parent =_meta_table['SNMPNOTIFICATIONMIB']['meta_info']
