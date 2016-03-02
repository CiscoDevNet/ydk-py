


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'CfmLmCountersCfg_Enum' : _MetaInfoEnum('CfmLmCountersCfg_Enum', 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_cfg',
        {
            'aggregate':'AGGREGATE',
            'list':'LIST',
            'range':'RANGE',
        }, 'Cisco-IOS-XR-ethernet-cfm-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-cfg']),
    'CfmMdidFormat_Enum' : _MetaInfoEnum('CfmMdidFormat_Enum', 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_cfg',
        {
            'null':'NULL',
            'dns-like':'DNS_LIKE',
            'mac-address':'MAC_ADDRESS',
            'string':'STRING',
        }, 'Cisco-IOS-XR-ethernet-cfm-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-cfg']),
    'CfmShortMaNameFormat_Enum' : _MetaInfoEnum('CfmShortMaNameFormat_Enum', 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_cfg',
        {
            'vlan-id':'VLAN_ID',
            'string':'STRING',
            'number':'NUMBER',
            'vpn-id':'VPN_ID',
            'icc-based':'ICC_BASED',
        }, 'Cisco-IOS-XR-ethernet-cfm-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-cfg']),
    'CfmService_Enum' : _MetaInfoEnum('CfmService_Enum', 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_cfg',
        {
            'bridge-domain':'BRIDGE_DOMAIN',
            'p2p-cross-connect':'P2P_CROSS_CONNECT',
            'mp2mp-cross-connect':'MP2MP_CROSS_CONNECT',
            'down-meps':'DOWN_MEPS',
        }, 'Cisco-IOS-XR-ethernet-cfm-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-cfg']),
    'CfmMipPolicy_Enum' : _MetaInfoEnum('CfmMipPolicy_Enum', 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_cfg',
        {
            'all':'ALL',
            'lower-mep-only':'LOWER_MEP_ONLY',
        }, 'Cisco-IOS-XR-ethernet-cfm-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-cfg']),
}
