


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'VlanTagOrCvp_Enum' : _MetaInfoEnum('VlanTagOrCvp_Enum', 'ydk.models.l2.Cisco_IOS_XR_l2_eth_infra_datatypes',
        {
            'native-with-cvlan-preservation':'NATIVE_WITH_CVLAN_PRESERVATION',
        }, 'Cisco-IOS-XR-l2-eth-infra-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-l2-eth-infra-datatypes']),
    'Rewrite_Enum' : _MetaInfoEnum('Rewrite_Enum', 'ydk.models.l2.Cisco_IOS_XR_l2_eth_infra_datatypes',
        {
            'pop1':'POP1',
            'pop2':'POP2',
            'push1':'PUSH1',
            'push2':'PUSH2',
            'translate1to1':'TRANSLATE1TO1',
            'translate1to2':'TRANSLATE1TO2',
            'translate2to1':'TRANSLATE2TO1',
            'translate2to2':'TRANSLATE2TO2',
        }, 'Cisco-IOS-XR-l2-eth-infra-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-l2-eth-infra-datatypes']),
    'Vlan_Enum' : _MetaInfoEnum('Vlan_Enum', 'ydk.models.l2.Cisco_IOS_XR_l2_eth_infra_datatypes',
        {
            'vlan-type-dot1ad':'VLAN_TYPE_DOT1AD',
            'vlan-type-dot1q':'VLAN_TYPE_DOT1Q',
        }, 'Cisco-IOS-XR-l2-eth-infra-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-l2-eth-infra-datatypes']),
    'EthertypeMatch_Enum' : _MetaInfoEnum('EthertypeMatch_Enum', 'ydk.models.l2.Cisco_IOS_XR_l2_eth_infra_datatypes',
        {
            'ppp-over-ethernet':'PPP_OVER_ETHERNET',
        }, 'Cisco-IOS-XR-l2-eth-infra-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-l2-eth-infra-datatypes']),
    'VlanTagOrNull_Enum' : _MetaInfoEnum('VlanTagOrNull_Enum', 'ydk.models.l2.Cisco_IOS_XR_l2_eth_infra_datatypes',
        {
            'any':'ANY',
        }, 'Cisco-IOS-XR-l2-eth-infra-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-l2-eth-infra-datatypes']),
    'VlanTagOrAny_Enum' : _MetaInfoEnum('VlanTagOrAny_Enum', 'ydk.models.l2.Cisco_IOS_XR_l2_eth_infra_datatypes',
        {
            'any':'ANY',
        }, 'Cisco-IOS-XR-l2-eth-infra-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-l2-eth-infra-datatypes']),
    'VlanTagOrNative_Enum' : _MetaInfoEnum('VlanTagOrNative_Enum', 'ydk.models.l2.Cisco_IOS_XR_l2_eth_infra_datatypes',
        {
            'native':'NATIVE',
            'native-with-cvlan-preservation':'NATIVE_WITH_CVLAN_PRESERVATION',
        }, 'Cisco-IOS-XR-l2-eth-infra-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-l2-eth-infra-datatypes']),
    'Match_Enum' : _MetaInfoEnum('Match_Enum', 'ydk.models.l2.Cisco_IOS_XR_l2_eth_infra_datatypes',
        {
            'match-default':'MATCH_DEFAULT',
            'match-untagged':'MATCH_UNTAGGED',
            'match-dot1q':'MATCH_DOT1Q',
            'match-dot1ad':'MATCH_DOT1AD',
            'match-dot1q-priority':'MATCH_DOT1Q_PRIORITY',
            'match-dot1ad-priority':'MATCH_DOT1AD_PRIORITY',
        }, 'Cisco-IOS-XR-l2-eth-infra-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-l2-eth-infra-datatypes']),
}
