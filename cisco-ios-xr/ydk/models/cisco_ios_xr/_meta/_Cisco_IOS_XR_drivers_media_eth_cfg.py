


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'EthernetDuplexEnum' : _MetaInfoEnum('EthernetDuplexEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_cfg',
        {
            'full':'full',
            'half':'half',
        }, 'Cisco-IOS-XR-drivers-media-eth-cfg', _yang_ns._namespaces['Cisco-IOS-XR-drivers-media-eth-cfg']),
    'EthernetSpeedEnum' : _MetaInfoEnum('EthernetSpeedEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_cfg',
        {
            '10':'Y_10',
            '100':'Y_100',
            '1000':'Y_1000',
        }, 'Cisco-IOS-XR-drivers-media-eth-cfg', _yang_ns._namespaces['Cisco-IOS-XR-drivers-media-eth-cfg']),
    'EthernetAutoNegotiationEnum' : _MetaInfoEnum('EthernetAutoNegotiationEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_cfg',
        {
            'true':'true',
            'override':'override',
        }, 'Cisco-IOS-XR-drivers-media-eth-cfg', _yang_ns._namespaces['Cisco-IOS-XR-drivers-media-eth-cfg']),
    'EthernetFlowCtrlEnum' : _MetaInfoEnum('EthernetFlowCtrlEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_cfg',
        {
            'ingress':'ingress',
            'egress':'egress',
            'bidirectional':'bidirectional',
        }, 'Cisco-IOS-XR-drivers-media-eth-cfg', _yang_ns._namespaces['Cisco-IOS-XR-drivers-media-eth-cfg']),
    'EthernetPfcEnum' : _MetaInfoEnum('EthernetPfcEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_cfg',
        {
            'on':'on',
        }, 'Cisco-IOS-XR-drivers-media-eth-cfg', _yang_ns._namespaces['Cisco-IOS-XR-drivers-media-eth-cfg']),
    'EthernetFecEnum' : _MetaInfoEnum('EthernetFecEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_cfg',
        {
            'none':'none',
            'standard':'standard',
        }, 'Cisco-IOS-XR-drivers-media-eth-cfg', _yang_ns._namespaces['Cisco-IOS-XR-drivers-media-eth-cfg']),
    'EthernetLoopbackEnum' : _MetaInfoEnum('EthernetLoopbackEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_cfg',
        {
            'external':'external',
            'internal':'internal',
            'line':'line',
        }, 'Cisco-IOS-XR-drivers-media-eth-cfg', _yang_ns._namespaces['Cisco-IOS-XR-drivers-media-eth-cfg']),
    'EthernetIpgEnum' : _MetaInfoEnum('EthernetIpgEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_cfg',
        {
            'non-standard':'non_standard',
        }, 'Cisco-IOS-XR-drivers-media-eth-cfg', _yang_ns._namespaces['Cisco-IOS-XR-drivers-media-eth-cfg']),
}
