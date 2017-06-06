


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'StormControlActionIdentity' : {
        'meta_info' : _MetaInfoClass('StormControlActionIdentity',
            False, 
            [
            ],
            'cisco-storm-control',
            'storm-control-action',
            _yang_ns._namespaces['cisco-storm-control'],
        'ydk.models.cisco_ios_xe.cisco_storm_control'
        ),
    },
    'ActionShutdownIdentity' : {
        'meta_info' : _MetaInfoClass('ActionShutdownIdentity',
            False, 
            [
            ],
            'cisco-storm-control',
            'action-shutdown',
            _yang_ns._namespaces['cisco-storm-control'],
        'ydk.models.cisco_ios_xe.cisco_storm_control'
        ),
    },
    'ActionDropIdentity' : {
        'meta_info' : _MetaInfoClass('ActionDropIdentity',
            False, 
            [
            ],
            'cisco-storm-control',
            'action-drop',
            _yang_ns._namespaces['cisco-storm-control'],
        'ydk.models.cisco_ios_xe.cisco_storm_control'
        ),
    },
    'ActionSnmpTrapIdentity' : {
        'meta_info' : _MetaInfoClass('ActionSnmpTrapIdentity',
            False, 
            [
            ],
            'cisco-storm-control',
            'action-snmp-trap',
            _yang_ns._namespaces['cisco-storm-control'],
        'ydk.models.cisco_ios_xe.cisco_storm_control'
        ),
    },
}
