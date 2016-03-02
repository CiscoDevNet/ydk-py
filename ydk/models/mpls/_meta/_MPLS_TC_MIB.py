


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'MplsLdpLabelTypes_Enum' : _MetaInfoEnum('MplsLdpLabelTypes_Enum', 'ydk.models.mpls.MPLS_TC_MIB',
        {
            'generic':'GENERIC',
            'atm':'ATM',
            'frameRelay':'FRAMERELAY',
        }, 'MPLS-TC-MIB', _yang_ns._namespaces['MPLS-TC-MIB']),
    'MplsInitialCreationSource_Enum' : _MetaInfoEnum('MplsInitialCreationSource_Enum', 'ydk.models.mpls.MPLS_TC_MIB',
        {
            'other':'OTHER',
            'snmp':'SNMP',
            'ldp':'LDP',
            'rsvp':'RSVP',
            'crldp':'CRLDP',
            'policyAgent':'POLICYAGENT',
            'unknown':'UNKNOWN',
        }, 'MPLS-TC-MIB', _yang_ns._namespaces['MPLS-TC-MIB']),
}
