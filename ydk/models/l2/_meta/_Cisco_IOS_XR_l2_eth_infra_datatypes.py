


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'VlanTagOrCvpEnum' : _MetaInfoEnum('VlanTagOrCvpEnum', 'ydk.models.l2.Cisco_IOS_XR_l2_eth_infra_datatypes',
        {
            'native-with-cvlan-preservation':'NATIVE_WITH_CVLAN_PRESERVATION',
        }, 'Cisco-IOS-XR-l2-eth-infra-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-l2-eth-infra-datatypes']),
    'RewriteEnum' : _MetaInfoEnum('RewriteEnum', 'ydk.models.l2.Cisco_IOS_XR_l2_eth_infra_datatypes',
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
    'VlanEnum' : _MetaInfoEnum('VlanEnum', 'ydk.models.l2.Cisco_IOS_XR_l2_eth_infra_datatypes',
        {
            'vlan-type-dot1ad':'VLAN_TYPE_DOT1AD',
            'vlan-type-dot1q':'VLAN_TYPE_DOT1Q',
        }, 'Cisco-IOS-XR-l2-eth-infra-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-l2-eth-infra-datatypes']),
    'EthertypeMatchEnum' : _MetaInfoEnum('EthertypeMatchEnum', 'ydk.models.l2.Cisco_IOS_XR_l2_eth_infra_datatypes',
        {
            'ppp-over-ethernet':'PPP_OVER_ETHERNET',
        }, 'Cisco-IOS-XR-l2-eth-infra-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-l2-eth-infra-datatypes']),
    'VlanTagOrNullEnum' : _MetaInfoEnum('VlanTagOrNullEnum', 'ydk.models.l2.Cisco_IOS_XR_l2_eth_infra_datatypes',
        {
            'any':'ANY',
        }, 'Cisco-IOS-XR-l2-eth-infra-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-l2-eth-infra-datatypes']),
    'VlanTagOrAnyEnum' : _MetaInfoEnum('VlanTagOrAnyEnum', 'ydk.models.l2.Cisco_IOS_XR_l2_eth_infra_datatypes',
        {
            'any':'ANY',
        }, 'Cisco-IOS-XR-l2-eth-infra-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-l2-eth-infra-datatypes']),
    'VlanTagOrNativeEnum' : _MetaInfoEnum('VlanTagOrNativeEnum', 'ydk.models.l2.Cisco_IOS_XR_l2_eth_infra_datatypes',
        {
            'native':'NATIVE',
            'native-with-cvlan-preservation':'NATIVE_WITH_CVLAN_PRESERVATION',
        }, 'Cisco-IOS-XR-l2-eth-infra-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-l2-eth-infra-datatypes']),
    'MatchEnum' : _MetaInfoEnum('MatchEnum', 'ydk.models.l2.Cisco_IOS_XR_l2_eth_infra_datatypes',
        {
            'match-default':'MATCH_DEFAULT',
            'match-untagged':'MATCH_UNTAGGED',
            'match-dot1q':'MATCH_DOT1Q',
            'match-dot1ad':'MATCH_DOT1AD',
            'match-dot1q-priority':'MATCH_DOT1Q_PRIORITY',
            'match-dot1ad-priority':'MATCH_DOT1AD_PRIORITY',
        }, 'Cisco-IOS-XR-l2-eth-infra-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-l2-eth-infra-datatypes']),
}
