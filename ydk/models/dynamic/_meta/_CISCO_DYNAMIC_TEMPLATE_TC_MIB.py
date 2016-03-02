


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'DynamicTemplateTargetType_Enum' : _MetaInfoEnum('DynamicTemplateTargetType_Enum', 'ydk.models.dynamic.CISCO_DYNAMIC_TEMPLATE_TC_MIB',
        {
            'other':'OTHER',
            'interface':'INTERFACE',
        }, 'CISCO-DYNAMIC-TEMPLATE-TC-MIB', _yang_ns._namespaces['CISCO-DYNAMIC-TEMPLATE-TC-MIB']),
    'DynamicTemplateType_Enum' : _MetaInfoEnum('DynamicTemplateType_Enum', 'ydk.models.dynamic.CISCO_DYNAMIC_TEMPLATE_TC_MIB',
        {
            'other':'OTHER',
            'derived':'DERIVED',
            'ppp':'PPP',
            'ethernet':'ETHERNET',
            'ipSubscriber':'IPSUBSCRIBER',
            'service':'SERVICE',
        }, 'CISCO-DYNAMIC-TEMPLATE-TC-MIB', _yang_ns._namespaces['CISCO-DYNAMIC-TEMPLATE-TC-MIB']),
}
