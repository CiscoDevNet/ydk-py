


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'QosPolicyAccountEnum' : _MetaInfoEnum('QosPolicyAccountEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_qos_ma_cfg',
        {
            'layer1':'layer1',
            'layer2':'layer2',
            'nolayer2':'nolayer2',
            'user-defined':'user_defined',
        }, 'Cisco-IOS-XR-qos-ma-cfg', _yang_ns._namespaces['Cisco-IOS-XR-qos-ma-cfg']),
    'QosFieldNotSupportedEnum' : _MetaInfoEnum('QosFieldNotSupportedEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_qos_ma_cfg',
        {
            'not-supported':'not_supported',
        }, 'Cisco-IOS-XR-qos-ma-cfg', _yang_ns._namespaces['Cisco-IOS-XR-qos-ma-cfg']),
    'Qos' : {
        'meta_info' : _MetaInfoClass('Qos',
            False, 
            [
            _MetaInfoClassMember('fabric-service-policy', ATTRIBUTE, 'str' , None, None, 
                [(0, 63)], [], 
                '''                Name of the fabric service policy
                ''',
                'fabric_service_policy',
                'Cisco-IOS-XR-qos-ma-cfg', False),
            ],
            'Cisco-IOS-XR-qos-ma-cfg',
            'qos',
            _yang_ns._namespaces['Cisco-IOS-XR-qos-ma-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_qos_ma_cfg'
        ),
    },
}
