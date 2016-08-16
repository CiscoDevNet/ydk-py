


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns

_meta_table = {
    'CfmLmCountersCfgEnum' : _MetaInfoEnum('CfmLmCountersCfgEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_cfg',
        {
            'aggregate':'AGGREGATE',
            'list':'LIST',
            'range':'RANGE',
        }, 'Cisco-IOS-XR-ethernet-cfm-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-cfg']),
    'CfmMdidFormatEnum' : _MetaInfoEnum('CfmMdidFormatEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_cfg',
        {
            'null':'NULL',
            'dns-like':'DNS_LIKE',
            'mac-address':'MAC_ADDRESS',
            'string':'STRING',
        }, 'Cisco-IOS-XR-ethernet-cfm-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-cfg']),
    'CfmShortMaNameFormatEnum' : _MetaInfoEnum('CfmShortMaNameFormatEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_cfg',
        {
            'vlan-id':'VLAN_ID',
            'string':'STRING',
            'number':'NUMBER',
            'vpn-id':'VPN_ID',
            'icc-based':'ICC_BASED',
        }, 'Cisco-IOS-XR-ethernet-cfm-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-cfg']),
    'CfmServiceEnum' : _MetaInfoEnum('CfmServiceEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_cfg',
        {
            'bridge-domain':'BRIDGE_DOMAIN',
            'p2p-cross-connect':'P2P_CROSS_CONNECT',
            'mp2mp-cross-connect':'MP2MP_CROSS_CONNECT',
            'down-meps':'DOWN_MEPS',
        }, 'Cisco-IOS-XR-ethernet-cfm-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-cfg']),
    'CfmMipPolicyEnum' : _MetaInfoEnum('CfmMipPolicyEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_cfg',
        {
            'all':'ALL',
            'lower-mep-only':'LOWER_MEP_ONLY',
        }, 'Cisco-IOS-XR-ethernet-cfm-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-cfg']),
}
