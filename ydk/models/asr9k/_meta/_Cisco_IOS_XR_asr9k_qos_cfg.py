


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'QosFieldNotSupportedEnum' : _MetaInfoEnum('QosFieldNotSupportedEnum', 'ydk.models.asr9k.Cisco_IOS_XR_asr9k_qos_cfg',
        {
            'not-supported':'NOT_SUPPORTED',
        }, 'Cisco-IOS-XR-asr9k-qos-cfg', _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-cfg']),
    'Qosl2DataLinkEnum' : _MetaInfoEnum('Qosl2DataLinkEnum', 'ydk.models.asr9k.Cisco_IOS_XR_asr9k_qos_cfg',
        {
            'aal5':'AAL5',
        }, 'Cisco-IOS-XR-asr9k-qos-cfg', _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-cfg']),
    'QosPolicyAccountEnum' : _MetaInfoEnum('QosPolicyAccountEnum', 'ydk.models.asr9k.Cisco_IOS_XR_asr9k_qos_cfg',
        {
            'no-preference':'NO_PREFERENCE',
            'layer2':'LAYER2',
            'no-layer2':'NO_LAYER2',
            'user-defined':'USER_DEFINED',
            'layer1':'LAYER1',
        }, 'Cisco-IOS-XR-asr9k-qos-cfg', _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-cfg']),
    'Qosl2EncapEnum' : _MetaInfoEnum('Qosl2EncapEnum', 'ydk.models.asr9k.Cisco_IOS_XR_asr9k_qos_cfg',
        {
            'snap-pppoa':'SNAP_PPPOA',
            'mux-pppoa':'MUX_PPPOA',
            'snap1483-routed':'SNAP1483_ROUTED',
            'mux1483-routed':'MUX1483_ROUTED',
            'snap-rbe':'SNAP_RBE',
            'snap-dot1qrbe':'SNAP_DOT1QRBE',
            'mux-rbe':'MUX_RBE',
            'mux-dot1qrbe':'MUX_DOT1QRBE',
        }, 'Cisco-IOS-XR-asr9k-qos-cfg', _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-cfg']),
    'Qos' : {
        'meta_info' : _MetaInfoClass('Qos',
            False, 
            [
            _MetaInfoClassMember('fabric-service-policy', ATTRIBUTE, 'str' , None, None, 
                [(0, 63)], [], 
                '''                Name of the fabric service policy
                ''',
                'fabric_service_policy',
                'Cisco-IOS-XR-asr9k-qos-cfg', False),
            ],
            'Cisco-IOS-XR-asr9k-qos-cfg',
            'qos',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-qos-cfg'],
        'ydk.models.asr9k.Cisco_IOS_XR_asr9k_qos_cfg'
        ),
    },
}
