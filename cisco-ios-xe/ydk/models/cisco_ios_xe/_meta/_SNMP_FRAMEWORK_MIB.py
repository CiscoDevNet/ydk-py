


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'SnmpsecuritylevelEnum' : _MetaInfoEnum('SnmpsecuritylevelEnum', 'ydk.models.cisco_ios_xe.SNMP_FRAMEWORK_MIB',
        {
            'noAuthNoPriv':'noAuthNoPriv',
            'authNoPriv':'authNoPriv',
            'authPriv':'authPriv',
        }, 'SNMP-FRAMEWORK-MIB', _yang_ns._namespaces['SNMP-FRAMEWORK-MIB']),
    'SnmpauthprotocolsIdentity' : {
        'meta_info' : _MetaInfoClass('SnmpauthprotocolsIdentity',
            False, 
            [
            ],
            'SNMP-FRAMEWORK-MIB',
            'snmpAuthProtocols',
            _yang_ns._namespaces['SNMP-FRAMEWORK-MIB'],
        'ydk.models.cisco_ios_xe.SNMP_FRAMEWORK_MIB'
        ),
    },
    'SnmpprivprotocolsIdentity' : {
        'meta_info' : _MetaInfoClass('SnmpprivprotocolsIdentity',
            False, 
            [
            ],
            'SNMP-FRAMEWORK-MIB',
            'snmpPrivProtocols',
            _yang_ns._namespaces['SNMP-FRAMEWORK-MIB'],
        'ydk.models.cisco_ios_xe.SNMP_FRAMEWORK_MIB'
        ),
    },
    'SnmpFrameworkMib.Snmpengine' : {
        'meta_info' : _MetaInfoClass('SnmpFrameworkMib.Snmpengine',
            False, 
            [
            _MetaInfoClassMember('snmpEngineBoots', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                The number of times that the SNMP engine has
                (re-)initialized itself since snmpEngineID
                was last configured.
                ''',
                'snmpengineboots',
                'SNMP-FRAMEWORK-MIB', False),
            _MetaInfoClassMember('snmpEngineID', ATTRIBUTE, 'str' , None, None, 
                [(5, 32)], [], 
                '''                An SNMP engine's administratively-unique identifier.
                
                This information SHOULD be stored in non-volatile
                storage so that it remains constant across
                re-initializations of the SNMP engine.
                ''',
                'snmpengineid',
                'SNMP-FRAMEWORK-MIB', False),
            _MetaInfoClassMember('snmpEngineMaxMessageSize', ATTRIBUTE, 'int' , None, None, 
                [('484', '2147483647')], [], 
                '''                The maximum length in octets of an SNMP message
                which this SNMP engine can send or receive and
                process, determined as the minimum of the maximum
                message size values supported among all of the
                transports available to and supported by the engine.
                ''',
                'snmpenginemaxmessagesize',
                'SNMP-FRAMEWORK-MIB', False),
            _MetaInfoClassMember('snmpEngineTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                The number of seconds since the value of
                the snmpEngineBoots object last changed.
                When incrementing this object's value would
                cause it to exceed its maximum,
                snmpEngineBoots is incremented as if a
                re-initialization had occurred, and this
                object's value consequently reverts to zero.
                ''',
                'snmpenginetime',
                'SNMP-FRAMEWORK-MIB', False),
            ],
            'SNMP-FRAMEWORK-MIB',
            'snmpEngine',
            _yang_ns._namespaces['SNMP-FRAMEWORK-MIB'],
        'ydk.models.cisco_ios_xe.SNMP_FRAMEWORK_MIB'
        ),
    },
    'SnmpFrameworkMib' : {
        'meta_info' : _MetaInfoClass('SnmpFrameworkMib',
            False, 
            [
            _MetaInfoClassMember('snmpEngine', REFERENCE_CLASS, 'Snmpengine' , 'ydk.models.cisco_ios_xe.SNMP_FRAMEWORK_MIB', 'SnmpFrameworkMib.Snmpengine', 
                [], [], 
                '''                ''',
                'snmpengine',
                'SNMP-FRAMEWORK-MIB', False),
            ],
            'SNMP-FRAMEWORK-MIB',
            'SNMP-FRAMEWORK-MIB',
            _yang_ns._namespaces['SNMP-FRAMEWORK-MIB'],
        'ydk.models.cisco_ios_xe.SNMP_FRAMEWORK_MIB'
        ),
    },
}
_meta_table['SnmpFrameworkMib.Snmpengine']['meta_info'].parent =_meta_table['SnmpFrameworkMib']['meta_info']
