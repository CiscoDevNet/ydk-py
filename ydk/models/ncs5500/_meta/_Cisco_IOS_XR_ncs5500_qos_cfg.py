


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'QosFieldNotSupported_Enum' : _MetaInfoEnum('QosFieldNotSupported_Enum', 'ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_cfg',
        {
            'not-supported':'NOT_SUPPORTED',
        }, 'Cisco-IOS-XR-ncs5500-qos-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-qos-cfg']),
    'QosPolicyAccount_Enum' : _MetaInfoEnum('QosPolicyAccount_Enum', 'ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_qos_cfg',
        {
            'no-preference':'NO_PREFERENCE',
            'layer2':'LAYER2',
            'no-layer2':'NO_LAYER2',
            'user-defined':'USER_DEFINED',
            'layer1':'LAYER1',
        }, 'Cisco-IOS-XR-ncs5500-qos-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-qos-cfg']),
}
