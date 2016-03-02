


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'CcbptTargetDirection_Enum' : _MetaInfoEnum('CcbptTargetDirection_Enum', 'ydk.models.cbp.CISCO_CBP_TARGET_TC_MIB',
        {
            'undirected':'UNDIRECTED',
            'input':'INPUT',
            'output':'OUTPUT',
            'inOut':'INOUT',
        }, 'CISCO-CBP-TARGET-TC-MIB', _yang_ns._namespaces['CISCO-CBP-TARGET-TC-MIB']),
    'CcbptPolicySourceType_Enum' : _MetaInfoEnum('CcbptPolicySourceType_Enum', 'ydk.models.cbp.CISCO_CBP_TARGET_TC_MIB',
        {
            'ciscoCbQos':'CISCOCBQOS',
            'ciscoCbpBase':'CISCOCBPBASE',
        }, 'CISCO-CBP-TARGET-TC-MIB', _yang_ns._namespaces['CISCO-CBP-TARGET-TC-MIB']),
    'CcbptTargetType_Enum' : _MetaInfoEnum('CcbptTargetType_Enum', 'ydk.models.cbp.CISCO_CBP_TARGET_TC_MIB',
        {
            'genIf':'GENIF',
            'atmPvc':'ATMPVC',
            'frDlci':'FRDLCI',
            'entity':'ENTITY',
            'fwZone':'FWZONE',
            'fwZonePair':'FWZONEPAIR',
            'aaaSession':'AAASESSION',
        }, 'CISCO-CBP-TARGET-TC-MIB', _yang_ns._namespaces['CISCO-CBP-TARGET-TC-MIB']),
}
