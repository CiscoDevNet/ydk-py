


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYModelError
from ydk.models import _yang_ns

_meta_table = {
    'BgpSubsequentAddressFamilyEnum' : _MetaInfoEnum('BgpSubsequentAddressFamilyEnum', 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_bgp_datatypes',
        {
            'unicast':'UNICAST',
            'multicast':'MULTICAST',
            'labeled-unicast':'LABELED_UNICAST',
            'mvpn':'MVPN',
            'mspw':'MSPW',
            'tunnel':'TUNNEL',
            'vpls':'VPLS',
            'mdt':'MDT',
            'vpws':'VPWS',
            'evpn':'EVPN',
            'ls':'LS',
            'vpn':'VPN',
            'vpn-mcast':'VPN_MCAST',
            'rt-filter':'RT_FILTER',
            'flowspec':'FLOWSPEC',
            'vpn-flowspec':'VPN_FLOWSPEC',
            'all':'ALL',
        }, 'Cisco-IOS-XR-ipv4-bgp-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-datatypes']),
    'BgpNbrCapAdditionalPathsCfgEnum' : _MetaInfoEnum('BgpNbrCapAdditionalPathsCfgEnum', 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_bgp_datatypes',
        {
            'enable':'ENABLE',
            'disable':'DISABLE',
        }, 'Cisco-IOS-XR-ipv4-bgp-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-datatypes']),
    'BgpOfficialAddressFamilyEnum' : _MetaInfoEnum('BgpOfficialAddressFamilyEnum', 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_bgp_datatypes',
        {
            'ipv4':'IPV4',
            'ipv6':'IPV6',
            'l2vpn':'L2VPN',
            'ls':'LS',
            'all':'ALL',
        }, 'Cisco-IOS-XR-ipv4-bgp-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-datatypes']),
    'BgpafAdditionalPathsCfgEnum' : _MetaInfoEnum('BgpafAdditionalPathsCfgEnum', 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_bgp_datatypes',
        {
            'enable':'ENABLE',
            'disable':'DISABLE',
        }, 'Cisco-IOS-XR-ipv4-bgp-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-datatypes']),
    'BgpTosEnum' : _MetaInfoEnum('BgpTosEnum', 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_bgp_datatypes',
        {
            'precedence':'PRECEDENCE',
            'dscp':'DSCP',
        }, 'Cisco-IOS-XR-ipv4-bgp-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-datatypes']),
    'BgpAddressFamilyEnum' : _MetaInfoEnum('BgpAddressFamilyEnum', 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_bgp_datatypes',
        {
            'ipv4-unicast':'IPV4_UNICAST',
            'ipv4-multicast':'IPV4_MULTICAST',
            'ipv4-labeled-unicast':'IPV4_LABELED_UNICAST',
            'ipv4-tunnel':'IPV4_TUNNEL',
            'vp-nv4-unicast':'VP_NV4_UNICAST',
            'ipv6-unicast':'IPV6_UNICAST',
            'ipv6-multicast':'IPV6_MULTICAST',
            'ipv6-labeled-unicast':'IPV6_LABELED_UNICAST',
            'vp-nv6-unicast':'VP_NV6_UNICAST',
            'ipv4mdt':'IPV4MDT',
            'l2vpnvpls':'L2VPNVPLS',
            'ipv4rt-constraint':'IPV4RT_CONSTRAINT',
            'ipv4mvpn':'IPV4MVPN',
            'ipv6mvpn':'IPV6MVPN',
            'l2vpnevpn':'L2VPNEVPN',
            'lsls':'LSLS',
            'vp-nv4-multicast':'VP_NV4_MULTICAST',
            'vp-nv6-multicast':'VP_NV6_MULTICAST',
            'ipv4-flowspec':'IPV4_FLOWSPEC',
            'ipv6-flowspec':'IPV6_FLOWSPEC',
            'vp-nv4-flowspec':'VP_NV4_FLOWSPEC',
            'vp-nv6-flowspec':'VP_NV6_FLOWSPEC',
            'l2vpnmspw':'L2VPNMSPW',
            'all-address-family':'ALL_ADDRESS_FAMILY',
        }, 'Cisco-IOS-XR-ipv4-bgp-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-datatypes']),
    'BgpPrecedenceDscpEnum' : _MetaInfoEnum('BgpPrecedenceDscpEnum', 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_bgp_datatypes',
        {
            'af11':'AF11',
            'af12':'AF12',
            'af13':'AF13',
            'af21':'AF21',
            'af22':'AF22',
            'af23':'AF23',
            'af31':'AF31',
            'af32':'AF32',
            'af33':'AF33',
            'af41':'AF41',
            'af42':'AF42',
            'af43':'AF43',
            'cs1':'CS1',
            'cs2':'CS2',
            'cs3':'CS3',
            'cs4':'CS4',
            'cs5':'CS5',
            'cs6':'CS6',
            'cs7':'CS7',
            'ef':'EF',
            'critical':'CRITICAL',
            'flash':'FLASH',
            'flash-override':'FLASH_OVERRIDE',
            'immediate':'IMMEDIATE',
            'internet':'INTERNET',
            'network':'NETWORK',
            'priority':'PRIORITY',
            'default-or-routine':'DEFAULT_OR_ROUTINE',
        }, 'Cisco-IOS-XR-ipv4-bgp-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-datatypes']),
    'BgpUpdateFilterActionEnum' : _MetaInfoEnum('BgpUpdateFilterActionEnum', 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_bgp_datatypes',
        {
            'treat-as-withdraw':'TREAT_AS_WITHDRAW',
            'discard-attibute':'DISCARD_ATTIBUTE',
        }, 'Cisco-IOS-XR-ipv4-bgp-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-datatypes']),
}
