


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'SnmpSecurityLevel_Enum' : _MetaInfoEnum('SnmpSecurityLevel_Enum', 'ydk.models.snmp.SNMP_FRAMEWORK_MIB',
        {
            'noAuthNoPriv':'NOAUTHNOPRIV',
            'authNoPriv':'AUTHNOPRIV',
            'authPriv':'AUTHPRIV',
        }, 'SNMP-FRAMEWORK-MIB', _yang_ns._namespaces['SNMP-FRAMEWORK-MIB']),
    'SNMPFRAMEWORKMIB.SnmpEngine' : {
        'meta_info' : _MetaInfoClass('SNMPFRAMEWORKMIB.SnmpEngine',
            False, 
            [
            _MetaInfoClassMember('snmpEngineBoots', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'snmpengineboots',
                'SNMP-FRAMEWORK-MIB', False),
            _MetaInfoClassMember('snmpEngineID', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9a-fA-F]){2}(:([0-9a-fA-F]){2})*)?'], 
                '''                ''',
                'snmpengineid',
                'SNMP-FRAMEWORK-MIB', False),
            _MetaInfoClassMember('snmpEngineMaxMessageSize', ATTRIBUTE, 'int' , None, None, 
                [(484, 2147483647)], [], 
                '''                ''',
                'snmpenginemaxmessagesize',
                'SNMP-FRAMEWORK-MIB', False),
            _MetaInfoClassMember('snmpEngineTime', ATTRIBUTE, 'int' , None, None, 
                [(0, 2147483647)], [], 
                '''                ''',
                'snmpenginetime',
                'SNMP-FRAMEWORK-MIB', False),
            ],
            'SNMP-FRAMEWORK-MIB',
            'snmpEngine',
            _yang_ns._namespaces['SNMP-FRAMEWORK-MIB'],
        'ydk.models.snmp.SNMP_FRAMEWORK_MIB'
        ),
    },
    'SNMPFRAMEWORKMIB' : {
        'meta_info' : _MetaInfoClass('SNMPFRAMEWORKMIB',
            False, 
            [
            _MetaInfoClassMember('snmpEngine', REFERENCE_CLASS, 'SnmpEngine' , 'ydk.models.snmp.SNMP_FRAMEWORK_MIB', 'SNMPFRAMEWORKMIB.SnmpEngine', 
                [], [], 
                '''                ''',
                'snmpengine',
                'SNMP-FRAMEWORK-MIB', False),
            ],
            'SNMP-FRAMEWORK-MIB',
            'SNMP-FRAMEWORK-MIB',
            _yang_ns._namespaces['SNMP-FRAMEWORK-MIB'],
        'ydk.models.snmp.SNMP_FRAMEWORK_MIB'
        ),
    },
}
_meta_table['SNMPFRAMEWORKMIB.SnmpEngine']['meta_info'].parent =_meta_table['SNMPFRAMEWORKMIB']['meta_info']
