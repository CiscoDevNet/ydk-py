


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'VlanEnum' : _MetaInfoEnum('VlanEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_datatypes',
        {
            'vlan-type-dot1ad':'vlan_type_dot1ad',
            'vlan-type-dot1q':'vlan_type_dot1q',
        }, 'Cisco-IOS-XR-l2-eth-infra-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-l2-eth-infra-datatypes']),
    'VlanTagOrNullEnum' : _MetaInfoEnum('VlanTagOrNullEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_datatypes',
        {
            'any':'any',
        }, 'Cisco-IOS-XR-l2-eth-infra-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-l2-eth-infra-datatypes']),
    'VlanTagOrAnyEnum' : _MetaInfoEnum('VlanTagOrAnyEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_datatypes',
        {
            'any':'any',
        }, 'Cisco-IOS-XR-l2-eth-infra-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-l2-eth-infra-datatypes']),
    'VlanTagOrCvpEnum' : _MetaInfoEnum('VlanTagOrCvpEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_datatypes',
        {
            'native-with-cvlan-preservation':'native_with_cvlan_preservation',
        }, 'Cisco-IOS-XR-l2-eth-infra-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-l2-eth-infra-datatypes']),
    'EthertypeMatchEnum' : _MetaInfoEnum('EthertypeMatchEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_datatypes',
        {
            'ppp-over-ethernet':'ppp_over_ethernet',
        }, 'Cisco-IOS-XR-l2-eth-infra-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-l2-eth-infra-datatypes']),
    'VlanTagOrNativeEnum' : _MetaInfoEnum('VlanTagOrNativeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_datatypes',
        {
            'native':'native',
            'native-with-cvlan-preservation':'native_with_cvlan_preservation',
        }, 'Cisco-IOS-XR-l2-eth-infra-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-l2-eth-infra-datatypes']),
    'MatchEnum' : _MetaInfoEnum('MatchEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_datatypes',
        {
            'match-default':'match_default',
            'match-untagged':'match_untagged',
            'match-dot1q':'match_dot1q',
            'match-dot1ad':'match_dot1ad',
            'match-dot1q-priority':'match_dot1q_priority',
            'match-dot1ad-priority':'match_dot1ad_priority',
        }, 'Cisco-IOS-XR-l2-eth-infra-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-l2-eth-infra-datatypes']),
    'RewriteEnum' : _MetaInfoEnum('RewriteEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_datatypes',
        {
            'pop1':'pop1',
            'pop2':'pop2',
            'push1':'push1',
            'push2':'push2',
            'translate1to1':'translate1to1',
            'translate1to2':'translate1to2',
            'translate2to1':'translate2to1',
            'translate2to2':'translate2to2',
        }, 'Cisco-IOS-XR-l2-eth-infra-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-l2-eth-infra-datatypes']),
}
