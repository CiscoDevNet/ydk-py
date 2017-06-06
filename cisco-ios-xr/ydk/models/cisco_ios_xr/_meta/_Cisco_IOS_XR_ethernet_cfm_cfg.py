


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'CfmMdidFormatEnum' : _MetaInfoEnum('CfmMdidFormatEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_cfg',
        {
            'null':'null',
            'dns-like':'dns_like',
            'mac-address':'mac_address',
            'string':'string',
        }, 'Cisco-IOS-XR-ethernet-cfm-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-cfg']),
    'CfmServiceEnum' : _MetaInfoEnum('CfmServiceEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_cfg',
        {
            'bridge-domain':'bridge_domain',
            'p2p-cross-connect':'p2p_cross_connect',
            'mp2mp-cross-connect':'mp2mp_cross_connect',
            'down-meps':'down_meps',
        }, 'Cisco-IOS-XR-ethernet-cfm-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-cfg']),
    'CfmShortMaNameFormatEnum' : _MetaInfoEnum('CfmShortMaNameFormatEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_cfg',
        {
            'vlan-id':'vlan_id',
            'string':'string',
            'number':'number',
            'vpn-id':'vpn_id',
            'icc-based':'icc_based',
        }, 'Cisco-IOS-XR-ethernet-cfm-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-cfg']),
    'CfmMipPolicyEnum' : _MetaInfoEnum('CfmMipPolicyEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_cfg',
        {
            'all':'all',
            'lower-mep-only':'lower_mep_only',
        }, 'Cisco-IOS-XR-ethernet-cfm-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-cfg']),
    'CfmLmCountersCfgEnum' : _MetaInfoEnum('CfmLmCountersCfgEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_cfg',
        {
            'aggregate':'aggregate',
            'list':'list',
            'range':'range',
        }, 'Cisco-IOS-XR-ethernet-cfm-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-cfg']),
}
