


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns

_meta_table = {
    'EthernetIpgEnum' : _MetaInfoEnum('EthernetIpgEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_cfg',
        {
            'non-standard':'NON_STANDARD',
        }, 'Cisco-IOS-XR-drivers-media-eth-cfg', _yang_ns._namespaces['Cisco-IOS-XR-drivers-media-eth-cfg']),
    'EthernetPfcEnum' : _MetaInfoEnum('EthernetPfcEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_cfg',
        {
            'on':'ON',
        }, 'Cisco-IOS-XR-drivers-media-eth-cfg', _yang_ns._namespaces['Cisco-IOS-XR-drivers-media-eth-cfg']),
    'EthernetAutoNegotiationEnum' : _MetaInfoEnum('EthernetAutoNegotiationEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_cfg',
        {
            'true':'TRUE',
            'override':'OVERRIDE',
        }, 'Cisco-IOS-XR-drivers-media-eth-cfg', _yang_ns._namespaces['Cisco-IOS-XR-drivers-media-eth-cfg']),
    'EthernetDuplexEnum' : _MetaInfoEnum('EthernetDuplexEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_cfg',
        {
            'full':'FULL',
            'half':'HALF',
        }, 'Cisco-IOS-XR-drivers-media-eth-cfg', _yang_ns._namespaces['Cisco-IOS-XR-drivers-media-eth-cfg']),
    'EthernetLoopbackEnum' : _MetaInfoEnum('EthernetLoopbackEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_cfg',
        {
            'external':'EXTERNAL',
            'internal':'INTERNAL',
            'line':'LINE',
        }, 'Cisco-IOS-XR-drivers-media-eth-cfg', _yang_ns._namespaces['Cisco-IOS-XR-drivers-media-eth-cfg']),
    'EthernetSpeedEnum' : _MetaInfoEnum('EthernetSpeedEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_cfg',
        {
            '10':'Y_10',
            '100':'Y_100',
            '1000':'Y_1000',
        }, 'Cisco-IOS-XR-drivers-media-eth-cfg', _yang_ns._namespaces['Cisco-IOS-XR-drivers-media-eth-cfg']),
    'EthernetFlowCtrlEnum' : _MetaInfoEnum('EthernetFlowCtrlEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_cfg',
        {
            'ingress':'INGRESS',
            'egress':'EGRESS',
            'bidirectional':'BIDIRECTIONAL',
        }, 'Cisco-IOS-XR-drivers-media-eth-cfg', _yang_ns._namespaces['Cisco-IOS-XR-drivers-media-eth-cfg']),
    'EthernetFecEnum' : _MetaInfoEnum('EthernetFecEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_drivers_media_eth_cfg',
        {
            'none':'NONE',
            'standard':'STANDARD',
        }, 'Cisco-IOS-XR-drivers-media-eth-cfg', _yang_ns._namespaces['Cisco-IOS-XR-drivers-media-eth-cfg']),
}
