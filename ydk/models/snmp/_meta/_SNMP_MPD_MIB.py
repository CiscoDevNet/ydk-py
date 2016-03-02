


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'SNMPMPDMIB.SnmpMPDStats' : {
        'meta_info' : _MetaInfoClass('SNMPMPDMIB.SnmpMPDStats',
            False, 
            [
            _MetaInfoClassMember('snmpInvalidMsgs', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                ''',
                'snmpinvalidmsgs',
                'SNMP-MPD-MIB', False),
            _MetaInfoClassMember('snmpUnknownPDUHandlers', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                ''',
                'snmpunknownpduhandlers',
                'SNMP-MPD-MIB', False),
            _MetaInfoClassMember('snmpUnknownSecurityModels', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                ''',
                'snmpunknownsecuritymodels',
                'SNMP-MPD-MIB', False),
            ],
            'SNMP-MPD-MIB',
            'snmpMPDStats',
            _yang_ns._namespaces['SNMP-MPD-MIB'],
        'ydk.models.snmp.SNMP_MPD_MIB'
        ),
    },
    'SNMPMPDMIB' : {
        'meta_info' : _MetaInfoClass('SNMPMPDMIB',
            False, 
            [
            _MetaInfoClassMember('snmpMPDStats', REFERENCE_CLASS, 'SnmpMPDStats' , 'ydk.models.snmp.SNMP_MPD_MIB', 'SNMPMPDMIB.SnmpMPDStats', 
                [], [], 
                '''                ''',
                'snmpmpdstats',
                'SNMP-MPD-MIB', False),
            ],
            'SNMP-MPD-MIB',
            'SNMP-MPD-MIB',
            _yang_ns._namespaces['SNMP-MPD-MIB'],
        'ydk.models.snmp.SNMP_MPD_MIB'
        ),
    },
}
_meta_table['SNMPMPDMIB.SnmpMPDStats']['meta_info'].parent =_meta_table['SNMPMPDMIB']['meta_info']
