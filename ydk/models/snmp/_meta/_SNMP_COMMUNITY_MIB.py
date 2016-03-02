


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'SNMPCOMMUNITYMIB.SnmpCommunityTable.SnmpCommunityEntry' : {
        'meta_info' : _MetaInfoClass('SNMPCOMMUNITYMIB.SnmpCommunityTable.SnmpCommunityEntry',
            False, 
            [
            _MetaInfoClassMember('snmpCommunityIndex', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                ''',
                'snmpcommunityindex',
                'SNMP-COMMUNITY-MIB', True),
            _MetaInfoClassMember('snmpCommunityContextEngineID', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9a-fA-F]){2}(:([0-9a-fA-F]){2})*)?'], 
                '''                ''',
                'snmpcommunitycontextengineid',
                'SNMP-COMMUNITY-MIB', False),
            _MetaInfoClassMember('snmpCommunityContextName', ATTRIBUTE, 'str' , None, None, 
                [('0', 32)], [], 
                '''                ''',
                'snmpcommunitycontextname',
                'SNMP-COMMUNITY-MIB', False),
            _MetaInfoClassMember('snmpCommunityName', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ''',
                'snmpcommunityname',
                'SNMP-COMMUNITY-MIB', False),
            _MetaInfoClassMember('snmpCommunitySecurityName', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                ''',
                'snmpcommunitysecurityname',
                'SNMP-COMMUNITY-MIB', False),
            _MetaInfoClassMember('snmpCommunityStorageType', REFERENCE_ENUM_CLASS, 'StorageType_Enum' , 'ydk.models.snmpv2.SNMPv2_TC', 'StorageType_Enum', 
                [], [], 
                '''                ''',
                'snmpcommunitystoragetype',
                'SNMP-COMMUNITY-MIB', False),
            _MetaInfoClassMember('snmpCommunityTransportTag', ATTRIBUTE, 'str' , None, None, 
                [('0', 255)], [], 
                '''                ''',
                'snmpcommunitytransporttag',
                'SNMP-COMMUNITY-MIB', False),
            ],
            'SNMP-COMMUNITY-MIB',
            'snmpCommunityEntry',
            _yang_ns._namespaces['SNMP-COMMUNITY-MIB'],
        'ydk.models.snmp.SNMP_COMMUNITY_MIB'
        ),
    },
    'SNMPCOMMUNITYMIB.SnmpCommunityTable' : {
        'meta_info' : _MetaInfoClass('SNMPCOMMUNITYMIB.SnmpCommunityTable',
            False, 
            [
            _MetaInfoClassMember('snmpCommunityEntry', REFERENCE_LIST, 'SnmpCommunityEntry' , 'ydk.models.snmp.SNMP_COMMUNITY_MIB', 'SNMPCOMMUNITYMIB.SnmpCommunityTable.SnmpCommunityEntry', 
                [], [], 
                '''                ''',
                'snmpcommunityentry',
                'SNMP-COMMUNITY-MIB', False),
            ],
            'SNMP-COMMUNITY-MIB',
            'snmpCommunityTable',
            _yang_ns._namespaces['SNMP-COMMUNITY-MIB'],
        'ydk.models.snmp.SNMP_COMMUNITY_MIB'
        ),
    },
    'SNMPCOMMUNITYMIB' : {
        'meta_info' : _MetaInfoClass('SNMPCOMMUNITYMIB',
            False, 
            [
            _MetaInfoClassMember('snmpCommunityTable', REFERENCE_CLASS, 'SnmpCommunityTable' , 'ydk.models.snmp.SNMP_COMMUNITY_MIB', 'SNMPCOMMUNITYMIB.SnmpCommunityTable', 
                [], [], 
                '''                ''',
                'snmpcommunitytable',
                'SNMP-COMMUNITY-MIB', False),
            ],
            'SNMP-COMMUNITY-MIB',
            'SNMP-COMMUNITY-MIB',
            _yang_ns._namespaces['SNMP-COMMUNITY-MIB'],
        'ydk.models.snmp.SNMP_COMMUNITY_MIB'
        ),
    },
}
_meta_table['SNMPCOMMUNITYMIB.SnmpCommunityTable.SnmpCommunityEntry']['meta_info'].parent =_meta_table['SNMPCOMMUNITYMIB.SnmpCommunityTable']['meta_info']
_meta_table['SNMPCOMMUNITYMIB.SnmpCommunityTable']['meta_info'].parent =_meta_table['SNMPCOMMUNITYMIB']['meta_info']
