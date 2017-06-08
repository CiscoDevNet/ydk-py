


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns

_meta_table = {
    'TtlActionIdentity' : {
        'meta_info' : _MetaInfoClass('TtlActionIdentity',
            False, 
            [
            ],
            'ietf-i2rs-rib',
            'ttl-action',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'IpRouteMatchTypeIdentity' : {
        'meta_info' : _MetaInfoClass('IpRouteMatchTypeIdentity',
            False, 
            [
            ],
            'ietf-i2rs-rib',
            'ip-route-match-type',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'HopLimitActionIdentity' : {
        'meta_info' : _MetaInfoClass('HopLimitActionIdentity',
            False, 
            [
            ],
            'ietf-i2rs-rib',
            'hop-limit-action',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteChangeReasonIdentity' : {
        'meta_info' : _MetaInfoClass('RouteChangeReasonIdentity',
            False, 
            [
            ],
            'ietf-i2rs-rib',
            'route-change-reason',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteInstalledStateIdentity' : {
        'meta_info' : _MetaInfoClass('RouteInstalledStateIdentity',
            False, 
            [
            ],
            'ietf-i2rs-rib',
            'route-installed-state',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'TunnelTypeIdentity' : {
        'meta_info' : _MetaInfoClass('TunnelTypeIdentity',
            False, 
            [
            ],
            'ietf-i2rs-rib',
            'tunnel-type',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteTypeIdentity' : {
        'meta_info' : _MetaInfoClass('RouteTypeIdentity',
            False, 
            [
            ],
            'ietf-i2rs-rib',
            'route-type',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'NexthopStateIdentity' : {
        'meta_info' : _MetaInfoClass('NexthopStateIdentity',
            False, 
            [
            ],
            'ietf-i2rs-rib',
            'nexthop-state',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RibFamilyIdentity' : {
        'meta_info' : _MetaInfoClass('RibFamilyIdentity',
            False, 
            [
            ],
            'ietf-i2rs-rib',
            'rib-family',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteStateIdentity' : {
        'meta_info' : _MetaInfoClass('RouteStateIdentity',
            False, 
            [
            ],
            'ietf-i2rs-rib',
            'route-state',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'SpecialNexthopIdentity' : {
        'meta_info' : _MetaInfoClass('SpecialNexthopIdentity',
            False, 
            [
            ],
            'ietf-i2rs-rib',
            'special-nexthop',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'TunnelDecapActionIdentity' : {
        'meta_info' : _MetaInfoClass('TunnelDecapActionIdentity',
            False, 
            [
            ],
            'ietf-i2rs-rib',
            'tunnel-decap-action',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'MplsLabelActionIdentity' : {
        'meta_info' : _MetaInfoClass('MplsLabelActionIdentity',
            False, 
            [
            ],
            'ietf-i2rs-rib',
            'mpls-label-action',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RoutingInstance.InterfaceList' : {
        'meta_info' : _MetaInfoClass('RoutingInstance.InterfaceList',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                A reference to the name of a network layer interface.
                ''',
                'name',
                'ietf-i2rs-rib', True),
            ],
            'ietf-i2rs-rib',
            'interface-list',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RoutingInstance.RibList.RouteList.Match.Ipv4.DestSrcIpv4Address' : {
        'meta_info' : _MetaInfoClass('RoutingInstance.RibList.RouteList.Match.Ipv4.DestSrcIpv4Address',
            False, 
            [
            _MetaInfoClassMember('dest-ipv4-prefix', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                '''                The IPv4 destination address of the match.
                ''',
                'dest_ipv4_prefix',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('src-ipv4-prefix', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                '''                The IPv4 source address of the match
                ''',
                'src_ipv4_prefix',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'dest-src-ipv4-address',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RoutingInstance.RibList.RouteList.Match.Ipv4' : {
        'meta_info' : _MetaInfoClass('RoutingInstance.RibList.RouteList.Match.Ipv4',
            False, 
            [
            _MetaInfoClassMember('dest-ipv4-prefix', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                '''                An IPv4 destination address as the match.
                ''',
                'dest_ipv4_prefix',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('dest-src-ipv4-address', REFERENCE_CLASS, 'DestSrcIpv4Address' , 'ydk.models.ietf.ietf_i2rs_rib', 'RoutingInstance.RibList.RouteList.Match.Ipv4.DestSrcIpv4Address', 
                [], [], 
                '''                A combination of an IPv4 source and
                an IPv4 destination address as the match.
                ''',
                'dest_src_ipv4_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('src-ipv4-prefix', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                '''                An IPv4 source address as the match.
                ''',
                'src_ipv4_prefix',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'ipv4',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RoutingInstance.RibList.RouteList.Match.Ipv6.DestSrcIpv6Address' : {
        'meta_info' : _MetaInfoClass('RoutingInstance.RibList.RouteList.Match.Ipv6.DestSrcIpv6Address',
            False, 
            [
            _MetaInfoClassMember('dest-ipv6-prefix', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                '''                The IPv6 destination address of the match
                ''',
                'dest_ipv6_prefix',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('src-ipv6-prefix', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                '''                The IPv6 source address of the match.
                ''',
                'src_ipv6_prefix',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'dest-src-ipv6-address',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RoutingInstance.RibList.RouteList.Match.Ipv6' : {
        'meta_info' : _MetaInfoClass('RoutingInstance.RibList.RouteList.Match.Ipv6',
            False, 
            [
            _MetaInfoClassMember('dest-ipv6-prefix', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                '''                An IPv6 destination address as the match.
                ''',
                'dest_ipv6_prefix',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('dest-src-ipv6-address', REFERENCE_CLASS, 'DestSrcIpv6Address' , 'ydk.models.ietf.ietf_i2rs_rib', 'RoutingInstance.RibList.RouteList.Match.Ipv6.DestSrcIpv6Address', 
                [], [], 
                '''                A combination of an IPv6 source and
                an IPv6 destination address as the match.
                ''',
                'dest_src_ipv6_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('src-ipv6-prefix', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                '''                An IPv6 source address as the match.
                ''',
                'src_ipv6_prefix',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'ipv6',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RoutingInstance.RibList.RouteList.Match' : {
        'meta_info' : _MetaInfoClass('RoutingInstance.RibList.RouteList.Match',
            False, 
            [
            _MetaInfoClassMember('interface-identifier', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The interface used for matching.
                ''',
                'interface_identifier',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ipv4', REFERENCE_CLASS, 'Ipv4' , 'ydk.models.ietf.ietf_i2rs_rib', 'RoutingInstance.RibList.RouteList.Match.Ipv4', 
                [], [], 
                '''                IPv4 route match.
                ''',
                'ipv4',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ipv6', REFERENCE_CLASS, 'Ipv6' , 'ydk.models.ietf.ietf_i2rs_rib', 'RoutingInstance.RibList.RouteList.Match.Ipv6', 
                [], [], 
                '''                IPv6 route match.
                ''',
                'ipv6',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('mac-address', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The MAC address used for matching.
                ''',
                'mac_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('mpls-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The label used for matching.
                ''',
                'mpls_label',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'match',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RoutingInstance.RibList.RouteList.Nexthop.NexthopBase.EgressInterfaceIpv4Address' : {
        'meta_info' : _MetaInfoClass('RoutingInstance.RibList.RouteList.Nexthop.NexthopBase.EgressInterfaceIpv4Address',
            False, 
            [
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The nexthop points to an interface with
                an IPv4 address.
                ''',
                'ipv4_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('outgoing-interface', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the outgoing interface.
                ''',
                'outgoing_interface',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'egress-interface-ipv4-address',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RoutingInstance.RibList.RouteList.Nexthop.NexthopBase.EgressInterfaceIpv6Address' : {
        'meta_info' : _MetaInfoClass('RoutingInstance.RibList.RouteList.Nexthop.NexthopBase.EgressInterfaceIpv6Address',
            False, 
            [
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                The nexthop points to an interface with
                an IPv6 address.
                ''',
                'ipv6_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('outgoing-interface', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the outgoing interface.
                ''',
                'outgoing_interface',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'egress-interface-ipv6-address',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RoutingInstance.RibList.RouteList.Nexthop.NexthopBase.EgressInterfaceMacAddress' : {
        'meta_info' : _MetaInfoClass('RoutingInstance.RibList.RouteList.Nexthop.NexthopBase.EgressInterfaceMacAddress',
            False, 
            [
            _MetaInfoClassMember('ieee-mac-address', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The nexthop points to an interface with
                a specific mac-address.
                ''',
                'ieee_mac_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('outgoing-interface', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the outgoing interface.
                ''',
                'outgoing_interface',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'egress-interface-mac-address',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RoutingInstance.RibList.RouteList.Nexthop.NexthopBase.TunnelEncap.Ipv4Header' : {
        'meta_info' : _MetaInfoClass('RoutingInstance.RibList.RouteList.Nexthop.NexthopBase.TunnelEncap.Ipv4Header',
            False, 
            [
            _MetaInfoClassMember('dest-ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The destination IP address of the header.
                ''',
                'dest_ipv4_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('dscp', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The DSCP field of the header.
                ''',
                'dscp',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('protocol', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The protocol id of the header.
                ''',
                'protocol',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('src-ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The source IP address of the header.
                ''',
                'src_ipv4_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ttl', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The TTL of the header.
                ''',
                'ttl',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'ipv4-header',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RoutingInstance.RibList.RouteList.Nexthop.NexthopBase.TunnelEncap.Ipv6Header' : {
        'meta_info' : _MetaInfoClass('RoutingInstance.RibList.RouteList.Nexthop.NexthopBase.TunnelEncap.Ipv6Header',
            False, 
            [
            _MetaInfoClassMember('dest-ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                The destination IP address of the header.
                ''',
                'dest_ipv6_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('flow-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The flow label of the header.
                ''',
                'flow_label',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('hop-limit', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The hop limit the header.
                ''',
                'hop_limit',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('next-header', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The next header of the IPv6 header.
                ''',
                'next_header',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('src-ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                The source IP address of the header.
                ''',
                'src_ipv6_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('traffic-class', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The traffic class value of the header.
                ''',
                'traffic_class',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'ipv6-header',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RoutingInstance.RibList.RouteList.Nexthop.NexthopBase.TunnelEncap.MplsHeader.LabelOperations.LabelPush' : {
        'meta_info' : _MetaInfoClass('RoutingInstance.RibList.RouteList.Nexthop.NexthopBase.TunnelEncap.MplsHeader.LabelOperations.LabelPush',
            False, 
            [
            _MetaInfoClassMember('label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The label to be pushed.
                ''',
                'label',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('s-bit', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                The s-bit of the label to be pushed. 
                ''',
                's_bit',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('tc-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The traffic class value of the label to be pushed.
                ''',
                'tc_value',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ttl-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The TTL value of the label to be pushed.
                ''',
                'ttl_value',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'label-push',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RoutingInstance.RibList.RouteList.Nexthop.NexthopBase.TunnelEncap.MplsHeader.LabelOperations.LabelSwap' : {
        'meta_info' : _MetaInfoClass('RoutingInstance.RibList.RouteList.Nexthop.NexthopBase.TunnelEncap.MplsHeader.LabelOperations.LabelSwap',
            False, 
            [
            _MetaInfoClassMember('in-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The label to be swapped.
                ''',
                'in_label',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('out-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The out MPLS label.
                ''',
                'out_label',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ttl-action', REFERENCE_IDENTITY_CLASS, 'TtlActionIdentity' , 'ydk.models.ietf.ietf_i2rs_rib', 'TtlActionIdentity', 
                [], [], 
                '''                The label ttl actions:
                - No-action, or
                - Copy to inner label,or
                - Decrease (the in label) by 1 and
                  copy to the out label.
                ''',
                'ttl_action',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'label-swap',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RoutingInstance.RibList.RouteList.Nexthop.NexthopBase.TunnelEncap.MplsHeader.LabelOperations' : {
        'meta_info' : _MetaInfoClass('RoutingInstance.RibList.RouteList.Nexthop.NexthopBase.TunnelEncap.MplsHeader.LabelOperations',
            False, 
            [
            _MetaInfoClassMember('label-oper-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                An optional identifier that points
                to a label operation.
                ''',
                'label_oper_id',
                'ietf-i2rs-rib', True),
            _MetaInfoClassMember('label-push', REFERENCE_CLASS, 'LabelPush' , 'ydk.models.ietf.ietf_i2rs_rib', 'RoutingInstance.RibList.RouteList.Nexthop.NexthopBase.TunnelEncap.MplsHeader.LabelOperations.LabelPush', 
                [], [], 
                '''                Label push operation.
                ''',
                'label_push',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('label-swap', REFERENCE_CLASS, 'LabelSwap' , 'ydk.models.ietf.ietf_i2rs_rib', 'RoutingInstance.RibList.RouteList.Nexthop.NexthopBase.TunnelEncap.MplsHeader.LabelOperations.LabelSwap', 
                [], [], 
                '''                Label swap operation.
                ''',
                'label_swap',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'label-operations',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RoutingInstance.RibList.RouteList.Nexthop.NexthopBase.TunnelEncap.MplsHeader' : {
        'meta_info' : _MetaInfoClass('RoutingInstance.RibList.RouteList.Nexthop.NexthopBase.TunnelEncap.MplsHeader',
            False, 
            [
            _MetaInfoClassMember('label-operations', REFERENCE_LIST, 'LabelOperations' , 'ydk.models.ietf.ietf_i2rs_rib', 'RoutingInstance.RibList.RouteList.Nexthop.NexthopBase.TunnelEncap.MplsHeader.LabelOperations', 
                [], [], 
                '''                Label operations.
                ''',
                'label_operations',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'mpls-header',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RoutingInstance.RibList.RouteList.Nexthop.NexthopBase.TunnelEncap.GreHeader' : {
        'meta_info' : _MetaInfoClass('RoutingInstance.RibList.RouteList.Nexthop.NexthopBase.TunnelEncap.GreHeader',
            False, 
            [
            _MetaInfoClassMember('ipv4-dest', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The destination IP address of the GRE header.
                ''',
                'ipv4_dest',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ipv6-dest', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                The destination IP address of the GRE header.
                ''',
                'ipv6_dest',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('key', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The GRE key of the GRE header.
                ''',
                'key',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('protocol-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The protocol type of the GRE header.
                ''',
                'protocol_type',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'gre-header',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RoutingInstance.RibList.RouteList.Nexthop.NexthopBase.TunnelEncap.NvgreHeader' : {
        'meta_info' : _MetaInfoClass('RoutingInstance.RibList.RouteList.Nexthop.NexthopBase.TunnelEncap.NvgreHeader',
            False, 
            [
            _MetaInfoClassMember('dest-ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The destination IP address of the header.
                ''',
                'dest_ipv4_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('dest-ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                The destination IP address of the header.
                ''',
                'dest_ipv6_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('dscp', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The DSCP field of the header.
                ''',
                'dscp',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('flow-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The flow identifier of the NvGRE header.
                ''',
                'flow_id',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('flow-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The flow label of the header.
                ''',
                'flow_label',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('hop-limit', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The hop limit the header.
                ''',
                'hop_limit',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('next-header', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The next header of the IPv6 header.
                ''',
                'next_header',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('protocol', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The protocol id of the header.
                ''',
                'protocol',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('src-ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The source IP address of the header.
                ''',
                'src_ipv4_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('src-ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                The source IP address of the header.
                ''',
                'src_ipv6_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('traffic-class', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The traffic class value of the header.
                ''',
                'traffic_class',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ttl', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The TTL of the header.
                ''',
                'ttl',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('virtual-subnet-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The subnet identifier of the NvGRE header.
                ''',
                'virtual_subnet_id',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'nvgre-header',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RoutingInstance.RibList.RouteList.Nexthop.NexthopBase.TunnelEncap.VxlanHeader' : {
        'meta_info' : _MetaInfoClass('RoutingInstance.RibList.RouteList.Nexthop.NexthopBase.TunnelEncap.VxlanHeader',
            False, 
            [
            _MetaInfoClassMember('dest-ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The destination IP address of the header.
                ''',
                'dest_ipv4_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('dest-ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                The destination IP address of the header.
                ''',
                'dest_ipv6_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('dscp', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The DSCP field of the header.
                ''',
                'dscp',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('flow-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The flow label of the header.
                ''',
                'flow_label',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('hop-limit', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The hop limit the header.
                ''',
                'hop_limit',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('next-header', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The next header of the IPv6 header.
                ''',
                'next_header',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('protocol', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The protocol id of the header.
                ''',
                'protocol',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('src-ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The source IP address of the header.
                ''',
                'src_ipv4_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('src-ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                The source IP address of the header.
                ''',
                'src_ipv6_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('traffic-class', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The traffic class value of the header.
                ''',
                'traffic_class',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ttl', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The TTL of the header.
                ''',
                'ttl',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('vxlan-identifier', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The VxLAN identifier of the VxLAN header.
                ''',
                'vxlan_identifier',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'vxlan-header',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RoutingInstance.RibList.RouteList.Nexthop.NexthopBase.TunnelEncap' : {
        'meta_info' : _MetaInfoClass('RoutingInstance.RibList.RouteList.Nexthop.NexthopBase.TunnelEncap',
            False, 
            [
            _MetaInfoClassMember('gre-header', REFERENCE_CLASS, 'GreHeader' , 'ydk.models.ietf.ietf_i2rs_rib', 'RoutingInstance.RibList.RouteList.Nexthop.NexthopBase.TunnelEncap.GreHeader', 
                [], [], 
                '''                GRE header.
                ''',
                'gre_header',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ipv4-header', REFERENCE_CLASS, 'Ipv4Header' , 'ydk.models.ietf.ietf_i2rs_rib', 'RoutingInstance.RibList.RouteList.Nexthop.NexthopBase.TunnelEncap.Ipv4Header', 
                [], [], 
                '''                IPv4 header.
                ''',
                'ipv4_header',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ipv6-header', REFERENCE_CLASS, 'Ipv6Header' , 'ydk.models.ietf.ietf_i2rs_rib', 'RoutingInstance.RibList.RouteList.Nexthop.NexthopBase.TunnelEncap.Ipv6Header', 
                [], [], 
                '''                IPv6 header.
                ''',
                'ipv6_header',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('mpls-header', REFERENCE_CLASS, 'MplsHeader' , 'ydk.models.ietf.ietf_i2rs_rib', 'RoutingInstance.RibList.RouteList.Nexthop.NexthopBase.TunnelEncap.MplsHeader', 
                [], [], 
                '''                MPLS header.
                ''',
                'mpls_header',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('nvgre-header', REFERENCE_CLASS, 'NvgreHeader' , 'ydk.models.ietf.ietf_i2rs_rib', 'RoutingInstance.RibList.RouteList.Nexthop.NexthopBase.TunnelEncap.NvgreHeader', 
                [], [], 
                '''                NvGRE header.
                ''',
                'nvgre_header',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('vxlan-header', REFERENCE_CLASS, 'VxlanHeader' , 'ydk.models.ietf.ietf_i2rs_rib', 'RoutingInstance.RibList.RouteList.Nexthop.NexthopBase.TunnelEncap.VxlanHeader', 
                [], [], 
                '''                VxLAN header.
                ''',
                'vxlan_header',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'tunnel-encap',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RoutingInstance.RibList.RouteList.Nexthop.NexthopBase.TunnelDecap.Ipv4Decap' : {
        'meta_info' : _MetaInfoClass('RoutingInstance.RibList.RouteList.Nexthop.NexthopBase.TunnelDecap.Ipv4Decap',
            False, 
            [
            _MetaInfoClassMember('ipv4-decap', REFERENCE_IDENTITY_CLASS, 'TunnelDecapActionIdentity' , 'ydk.models.ietf.ietf_i2rs_rib', 'TunnelDecapActionIdentity', 
                [], [], 
                '''                IPv4 decap operations.
                ''',
                'ipv4_decap',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ttl-action', REFERENCE_IDENTITY_CLASS, 'TtlActionIdentity' , 'ydk.models.ietf.ietf_i2rs_rib', 'TtlActionIdentity', 
                [], [], 
                '''                The ttl actions:
                no-action or copy to inner header.
                ''',
                'ttl_action',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'ipv4-decap',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RoutingInstance.RibList.RouteList.Nexthop.NexthopBase.TunnelDecap.Ipv6Decap' : {
        'meta_info' : _MetaInfoClass('RoutingInstance.RibList.RouteList.Nexthop.NexthopBase.TunnelDecap.Ipv6Decap',
            False, 
            [
            _MetaInfoClassMember('hop-limit-action', REFERENCE_IDENTITY_CLASS, 'HopLimitActionIdentity' , 'ydk.models.ietf.ietf_i2rs_rib', 'HopLimitActionIdentity', 
                [], [], 
                '''                The hop limit actions:
                no-action or copy to inner header.
                ''',
                'hop_limit_action',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ipv6-decap', REFERENCE_IDENTITY_CLASS, 'TunnelDecapActionIdentity' , 'ydk.models.ietf.ietf_i2rs_rib', 'TunnelDecapActionIdentity', 
                [], [], 
                '''                IPv6 decap operations.
                ''',
                'ipv6_decap',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'ipv6-decap',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RoutingInstance.RibList.RouteList.Nexthop.NexthopBase.TunnelDecap.LabelPop' : {
        'meta_info' : _MetaInfoClass('RoutingInstance.RibList.RouteList.Nexthop.NexthopBase.TunnelDecap.LabelPop',
            False, 
            [
            _MetaInfoClassMember('label-pop', REFERENCE_IDENTITY_CLASS, 'MplsLabelActionIdentity' , 'ydk.models.ietf.ietf_i2rs_rib', 'MplsLabelActionIdentity', 
                [], [], 
                '''                Pop a label from the label stack.
                ''',
                'label_pop',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ttl-action', REFERENCE_IDENTITY_CLASS, 'TtlActionIdentity' , 'ydk.models.ietf.ietf_i2rs_rib', 'TtlActionIdentity', 
                [], [], 
                '''                The label ttl action.
                ''',
                'ttl_action',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'label-pop',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RoutingInstance.RibList.RouteList.Nexthop.NexthopBase.TunnelDecap' : {
        'meta_info' : _MetaInfoClass('RoutingInstance.RibList.RouteList.Nexthop.NexthopBase.TunnelDecap',
            False, 
            [
            _MetaInfoClassMember('ipv4-decap', REFERENCE_CLASS, 'Ipv4Decap' , 'ydk.models.ietf.ietf_i2rs_rib', 'RoutingInstance.RibList.RouteList.Nexthop.NexthopBase.TunnelDecap.Ipv4Decap', 
                [], [], 
                '''                IPv4 decap.
                ''',
                'ipv4_decap',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ipv6-decap', REFERENCE_CLASS, 'Ipv6Decap' , 'ydk.models.ietf.ietf_i2rs_rib', 'RoutingInstance.RibList.RouteList.Nexthop.NexthopBase.TunnelDecap.Ipv6Decap', 
                [], [], 
                '''                IPv6 decap.
                ''',
                'ipv6_decap',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('label-pop', REFERENCE_CLASS, 'LabelPop' , 'ydk.models.ietf.ietf_i2rs_rib', 'RoutingInstance.RibList.RouteList.Nexthop.NexthopBase.TunnelDecap.LabelPop', 
                [], [], 
                '''                MPLS decap.
                ''',
                'label_pop',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'tunnel-decap',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RoutingInstance.RibList.RouteList.Nexthop.NexthopBase.LogicalTunnel' : {
        'meta_info' : _MetaInfoClass('RoutingInstance.RibList.RouteList.Nexthop.NexthopBase.LogicalTunnel',
            False, 
            [
            _MetaInfoClassMember('tunnel-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                A tunnel name that points to a logical tunnel.
                ''',
                'tunnel_name',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('tunnel-type', REFERENCE_IDENTITY_CLASS, 'TunnelTypeIdentity' , 'ydk.models.ietf.ietf_i2rs_rib', 'TunnelTypeIdentity', 
                [], [], 
                '''                A tunnel type.
                ''',
                'tunnel_type',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'logical-tunnel',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RoutingInstance.RibList.RouteList.Nexthop.NexthopBase' : {
        'meta_info' : _MetaInfoClass('RoutingInstance.RibList.RouteList.Nexthop.NexthopBase',
            False, 
            [
            _MetaInfoClassMember('egress-interface-ipv4-address', REFERENCE_CLASS, 'EgressInterfaceIpv4Address' , 'ydk.models.ietf.ietf_i2rs_rib', 'RoutingInstance.RibList.RouteList.Nexthop.NexthopBase.EgressInterfaceIpv4Address', 
                [], [], 
                '''                The nexthop is an egress-interface and an IP
                address. This can be used in cases e.g. where
                the IP address is a link-local address.
                ''',
                'egress_interface_ipv4_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('egress-interface-ipv6-address', REFERENCE_CLASS, 'EgressInterfaceIpv6Address' , 'ydk.models.ietf.ietf_i2rs_rib', 'RoutingInstance.RibList.RouteList.Nexthop.NexthopBase.EgressInterfaceIpv6Address', 
                [], [], 
                '''                The nexthop is an egress-interface and an IP
                address. This can be used in cases e.g. where
                the IP address is a link-local address.
                ''',
                'egress_interface_ipv6_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('egress-interface-mac-address', REFERENCE_CLASS, 'EgressInterfaceMacAddress' , 'ydk.models.ietf.ietf_i2rs_rib', 'RoutingInstance.RibList.RouteList.Nexthop.NexthopBase.EgressInterfaceMacAddress', 
                [], [], 
                '''                The egress interface must be an Ethernet
                interface. Address resolution is not required
                for this nexthop.
                ''',
                'egress_interface_mac_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The nexthop is an IPv4 address.
                ''',
                'ipv4_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                The nexthop is an IPv6 address.
                ''',
                'ipv6_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('logical-tunnel', REFERENCE_CLASS, 'LogicalTunnel' , 'ydk.models.ietf.ietf_i2rs_rib', 'RoutingInstance.RibList.RouteList.Nexthop.NexthopBase.LogicalTunnel', 
                [], [], 
                '''                This can be a MPLS LSP or a GRE tunnel (or others
                as defined in this document), that is represented
                by a unique identifier (e.g. name).
                ''',
                'logical_tunnel',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('nexthop-ref', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A nexthop reference that points to a nexthop.
                ''',
                'nexthop_ref',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('outgoing-interface', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The nexthop is an outgoing interface.
                ''',
                'outgoing_interface',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('rib-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                A nexthop pointing to a RIB indicates that the
                route lookup needs to continue in the specified
                rib. This is a way to perform chained lookups.
                ''',
                'rib_name',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('special', REFERENCE_IDENTITY_CLASS, 'SpecialNexthopIdentity' , 'ydk.models.ietf.ietf_i2rs_rib', 'SpecialNexthopIdentity', 
                [], [], 
                '''                A special nexthop.
                ''',
                'special',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('tunnel-decap', REFERENCE_CLASS, 'TunnelDecap' , 'ydk.models.ietf.ietf_i2rs_rib', 'RoutingInstance.RibList.RouteList.Nexthop.NexthopBase.TunnelDecap', 
                [], [], 
                '''                This is to specify decapsulating a tunnel header.
                ''',
                'tunnel_decap',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('tunnel-encap', REFERENCE_CLASS, 'TunnelEncap' , 'ydk.models.ietf.ietf_i2rs_rib', 'RoutingInstance.RibList.RouteList.Nexthop.NexthopBase.TunnelEncap', 
                [], [], 
                '''                This can be an encap representing an IP tunnel or
                MPLS tunnel or others as defined in info model.
                An optional egress interface can be chained to the
                tunnel encap to indicate which interface to send
                the packet out on.  The egress interface is useful
                when the network device contains Ethernet interfaces
                and one needs to perform address resolution for the
                IP packet.
                ''',
                'tunnel_encap',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'nexthop-base',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RoutingInstance.RibList.RouteList.Nexthop.NexthopChain.NexthopList' : {
        'meta_info' : _MetaInfoClass('RoutingInstance.RibList.RouteList.Nexthop.NexthopChain.NexthopList',
            False, 
            [
            _MetaInfoClassMember('nexthop-member-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A nexthop identifier that points
                to a nexthop list member.
                A nexthop list member is a nexthop.
                ''',
                'nexthop_member_id',
                'ietf-i2rs-rib', True),
            ],
            'ietf-i2rs-rib',
            'nexthop-list',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RoutingInstance.RibList.RouteList.Nexthop.NexthopChain' : {
        'meta_info' : _MetaInfoClass('RoutingInstance.RibList.RouteList.Nexthop.NexthopChain',
            False, 
            [
            _MetaInfoClassMember('nexthop-list', REFERENCE_LIST, 'NexthopList' , 'ydk.models.ietf.ietf_i2rs_rib', 'RoutingInstance.RibList.RouteList.Nexthop.NexthopChain.NexthopList', 
                [], [], 
                '''                A list of nexthops.
                ''',
                'nexthop_list',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'nexthop-chain',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RoutingInstance.RibList.RouteList.Nexthop.NexthopReplicates.NexthopList' : {
        'meta_info' : _MetaInfoClass('RoutingInstance.RibList.RouteList.Nexthop.NexthopReplicates.NexthopList',
            False, 
            [
            _MetaInfoClassMember('nexthop-member-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A nexthop identifier that points
                to a nexthop list member.
                A nexthop list member is a nexthop.
                ''',
                'nexthop_member_id',
                'ietf-i2rs-rib', True),
            ],
            'ietf-i2rs-rib',
            'nexthop-list',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RoutingInstance.RibList.RouteList.Nexthop.NexthopReplicates' : {
        'meta_info' : _MetaInfoClass('RoutingInstance.RibList.RouteList.Nexthop.NexthopReplicates',
            False, 
            [
            _MetaInfoClassMember('nexthop-list', REFERENCE_LIST, 'NexthopList' , 'ydk.models.ietf.ietf_i2rs_rib', 'RoutingInstance.RibList.RouteList.Nexthop.NexthopReplicates.NexthopList', 
                [], [], 
                '''                A list of nexthops.
                ''',
                'nexthop_list',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'nexthop-replicates',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RoutingInstance.RibList.RouteList.Nexthop.NexthopProtection.NexthopList' : {
        'meta_info' : _MetaInfoClass('RoutingInstance.RibList.RouteList.Nexthop.NexthopProtection.NexthopList',
            False, 
            [
            _MetaInfoClassMember('nexthop-member-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A nexthop identifier that points
                to a nexthop list member.
                A nexthop list member is a nexthop.
                ''',
                'nexthop_member_id',
                'ietf-i2rs-rib', True),
            _MetaInfoClassMember('nexthop-preference', ATTRIBUTE, 'int' , None, None, 
                [('1', '99')], [], 
                '''                Nexthop-preference is used for protection schemes.
                It is an integer value between 1 and 99.  Lower
                values are more preferred. To download a
                primary/standby/tertiary group to the FIB, the
                nexthops that are resolved and are most preferred
                are selected.
                ''',
                'nexthop_preference',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'nexthop-list',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RoutingInstance.RibList.RouteList.Nexthop.NexthopProtection' : {
        'meta_info' : _MetaInfoClass('RoutingInstance.RibList.RouteList.Nexthop.NexthopProtection',
            False, 
            [
            _MetaInfoClassMember('nexthop-list', REFERENCE_LIST, 'NexthopList' , 'ydk.models.ietf.ietf_i2rs_rib', 'RoutingInstance.RibList.RouteList.Nexthop.NexthopProtection.NexthopList', 
                [], [], 
                '''                A list of nexthop.
                ''',
                'nexthop_list',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'nexthop-protection',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RoutingInstance.RibList.RouteList.Nexthop.NexthopLb.NexthopList' : {
        'meta_info' : _MetaInfoClass('RoutingInstance.RibList.RouteList.Nexthop.NexthopLb.NexthopList',
            False, 
            [
            _MetaInfoClassMember('nexthop-member-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A nexthop identifier that points
                to a nexthop list member.
                A nexthop list member is a nexthop.
                ''',
                'nexthop_member_id',
                'ietf-i2rs-rib', True),
            _MetaInfoClassMember('nexthop-lb-weight', ATTRIBUTE, 'int' , None, None, 
                [('1', '99')], [], 
                '''                The weight of a nexthop of
                the load balance nexthops.
                ''',
                'nexthop_lb_weight',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'nexthop-list',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RoutingInstance.RibList.RouteList.Nexthop.NexthopLb' : {
        'meta_info' : _MetaInfoClass('RoutingInstance.RibList.RouteList.Nexthop.NexthopLb',
            False, 
            [
            _MetaInfoClassMember('nexthop-list', REFERENCE_LIST, 'NexthopList' , 'ydk.models.ietf.ietf_i2rs_rib', 'RoutingInstance.RibList.RouteList.Nexthop.NexthopLb.NexthopList', 
                [], [], 
                '''                A list of nexthop.
                ''',
                'nexthop_list',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'nexthop-lb',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RoutingInstance.RibList.RouteList.Nexthop' : {
        'meta_info' : _MetaInfoClass('RoutingInstance.RibList.RouteList.Nexthop',
            False, 
            [
            _MetaInfoClassMember('nexthop-base', REFERENCE_CLASS, 'NexthopBase' , 'ydk.models.ietf.ietf_i2rs_rib', 'RoutingInstance.RibList.RouteList.Nexthop.NexthopBase', 
                [], [], 
                '''                The base nexthop.
                ''',
                'nexthop_base',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('nexthop-chain', REFERENCE_CLASS, 'NexthopChain' , 'ydk.models.ietf.ietf_i2rs_rib', 'RoutingInstance.RibList.RouteList.Nexthop.NexthopChain', 
                [], [], 
                '''                A chain nexthop.
                ''',
                'nexthop_chain',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('nexthop-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                An identifier that refers to a nexthop.
                ''',
                'nexthop_id',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('nexthop-lb', REFERENCE_CLASS, 'NexthopLb' , 'ydk.models.ietf.ietf_i2rs_rib', 'RoutingInstance.RibList.RouteList.Nexthop.NexthopLb', 
                [], [], 
                '''                A load balance nexthop.
                ''',
                'nexthop_lb',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('nexthop-protection', REFERENCE_CLASS, 'NexthopProtection' , 'ydk.models.ietf.ietf_i2rs_rib', 'RoutingInstance.RibList.RouteList.Nexthop.NexthopProtection', 
                [], [], 
                '''                A protection nexthop.
                ''',
                'nexthop_protection',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('nexthop-replicates', REFERENCE_CLASS, 'NexthopReplicates' , 'ydk.models.ietf.ietf_i2rs_rib', 'RoutingInstance.RibList.RouteList.Nexthop.NexthopReplicates', 
                [], [], 
                '''                A replicates nexthop.
                ''',
                'nexthop_replicates',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('sharing-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                To indicate whether a nexthop is sharable
                or non-sharable.
                true - sharable, means the nexthop can be shared
                       with other routes
                false - non-sharable, means the nexthop can not
                       be shared with other routes.
                ''',
                'sharing_flag',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'nexthop',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RoutingInstance.RibList.RouteList.RouteStatus' : {
        'meta_info' : _MetaInfoClass('RoutingInstance.RibList.RouteList.RouteStatus',
            False, 
            [
            _MetaInfoClassMember('route-installed-state', REFERENCE_IDENTITY_CLASS, 'RouteInstalledStateIdentity' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteInstalledStateIdentity', 
                [], [], 
                '''                Indicate that a route's installed states:
                Installed or uninstalled.
                ''',
                'route_installed_state',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('route-reason', REFERENCE_IDENTITY_CLASS, 'RouteChangeReasonIdentity' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteChangeReasonIdentity', 
                [], [], 
                '''                Indicate the reason that causes the route change.
                ''',
                'route_reason',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('route-state', REFERENCE_IDENTITY_CLASS, 'RouteStateIdentity' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteStateIdentity', 
                [], [], 
                '''                Indicate a route's state: Active or Inactive.
                ''',
                'route_state',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'route-status',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RoutingInstance.RibList.RouteList.RouteAttributes.AddressFamilyRouteAttributes' : {
        'meta_info' : _MetaInfoClass('RoutingInstance.RibList.RouteList.RouteAttributes.AddressFamilyRouteAttributes',
            False, 
            [
            ],
            'ietf-i2rs-rib',
            'address-family-route-attributes',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RoutingInstance.RibList.RouteList.RouteAttributes' : {
        'meta_info' : _MetaInfoClass('RoutingInstance.RibList.RouteList.RouteAttributes',
            False, 
            [
            _MetaInfoClassMember('address-family-route-attributes', REFERENCE_CLASS, 'AddressFamilyRouteAttributes' , 'ydk.models.ietf.ietf_i2rs_rib', 'RoutingInstance.RibList.RouteList.RouteAttributes.AddressFamilyRouteAttributes', 
                [], [], 
                '''                Address family related route attributes.
                ''',
                'address_family_route_attributes',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('local-only', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicate whether the attributes is local only.
                ''',
                'local_only',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('route-preference', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ROUTE_PREFERENCE: This is a numerical value that
                allows for comparing routes from different
                protocols.  Static configuration is also
                considered a protocol for the purpose of this
                field.  It is also known as administrative-distance.
                The lower the value, the higher the preference.
                ''',
                'route_preference',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'route-attributes',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RoutingInstance.RibList.RouteList.RouteVendorAttributes' : {
        'meta_info' : _MetaInfoClass('RoutingInstance.RibList.RouteList.RouteVendorAttributes',
            False, 
            [
            ],
            'ietf-i2rs-rib',
            'route-vendor-attributes',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RoutingInstance.RibList.RouteList' : {
        'meta_info' : _MetaInfoClass('RoutingInstance.RibList.RouteList',
            False, 
            [
            _MetaInfoClassMember('route-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Route index.
                ''',
                'route_index',
                'ietf-i2rs-rib', True),
            _MetaInfoClassMember('match', REFERENCE_CLASS, 'Match' , 'ydk.models.ietf.ietf_i2rs_rib', 'RoutingInstance.RibList.RouteList.Match', 
                [], [], 
                '''                The match condition specifies the
                kind of route (IPv4, MPLS, etc.)
                and the set of fields to match on.
                ''',
                'match',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('nexthop', REFERENCE_CLASS, 'Nexthop' , 'ydk.models.ietf.ietf_i2rs_rib', 'RoutingInstance.RibList.RouteList.Nexthop', 
                [], [], 
                '''                The nexthop of the route.
                ''',
                'nexthop',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('route-attributes', REFERENCE_CLASS, 'RouteAttributes' , 'ydk.models.ietf.ietf_i2rs_rib', 'RoutingInstance.RibList.RouteList.RouteAttributes', 
                [], [], 
                '''                Route attributes.
                ''',
                'route_attributes',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('route-status', REFERENCE_CLASS, 'RouteStatus' , 'ydk.models.ietf.ietf_i2rs_rib', 'RoutingInstance.RibList.RouteList.RouteStatus', 
                [], [], 
                '''                The status information of the route.
                ''',
                'route_status',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('route-vendor-attributes', REFERENCE_CLASS, 'RouteVendorAttributes' , 'ydk.models.ietf.ietf_i2rs_rib', 'RoutingInstance.RibList.RouteList.RouteVendorAttributes', 
                [], [], 
                '''                Route vendor attributes.
                ''',
                'route_vendor_attributes',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'route-list',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RoutingInstance.RibList.NexthopList' : {
        'meta_info' : _MetaInfoClass('RoutingInstance.RibList.NexthopList',
            False, 
            [
            _MetaInfoClassMember('nexthop-member-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A nexthop identifier that points
                to a nexthop list member.
                A nexthop list member is a nexthop.
                ''',
                'nexthop_member_id',
                'ietf-i2rs-rib', True),
            ],
            'ietf-i2rs-rib',
            'nexthop-list',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RoutingInstance.RibList' : {
        'meta_info' : _MetaInfoClass('RoutingInstance.RibList',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                A reference to the name of each rib.
                ''',
                'name',
                'ietf-i2rs-rib', True),
            _MetaInfoClassMember('address-family', REFERENCE_IDENTITY_CLASS, 'RibFamilyIdentity' , 'ydk.models.ietf.ietf_i2rs_rib', 'RibFamilyIdentity', 
                [], [], 
                '''                The address family of a rib.
                ''',
                'address_family',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ip-rpf-check', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Each RIB can be optionally associated with a
                ENABLE_IP_RPF_CHECK attribute that enables Reverse
                path forwarding (RPF) checks on all IP routes in that
                RIB.  Reverse path forwarding (RPF) check is used to
                prevent spoofing and limit malicious traffic.
                ''',
                'ip_rpf_check',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('nexthop-list', REFERENCE_LIST, 'NexthopList' , 'ydk.models.ietf.ietf_i2rs_rib', 'RoutingInstance.RibList.NexthopList', 
                [], [], 
                '''                A list of nexthops.
                ''',
                'nexthop_list',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('route-list', REFERENCE_LIST, 'RouteList' , 'ydk.models.ietf.ietf_i2rs_rib', 'RoutingInstance.RibList.RouteList', 
                [], [], 
                '''                A list of routes of a rib.
                ''',
                'route_list',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'rib-list',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RoutingInstance' : {
        'meta_info' : _MetaInfoClass('RoutingInstance',
            False, 
            [
            _MetaInfoClassMember('interface-list', REFERENCE_LIST, 'InterfaceList' , 'ydk.models.ietf.ietf_i2rs_rib', 'RoutingInstance.InterfaceList', 
                [], [], 
                '''                This represents the list of interfaces associated
                with this routing instance. The interface list helps
                constrain the boundaries of packet forwarding.
                Packets coming on these interfaces are directly
                associated with the given routing instance. The
                interface list contains a list of identifiers, with
                each identifier uniquely identifying an interface.
                ''',
                'interface_list',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('lookup-limit', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                A limit on how many levels of a lookup can be performed.
                ''',
                'lookup_limit',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The name of the routing instance. This MUST
                be unique across all routing instances in
                a given network device.
                ''',
                'name',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('rib-list', REFERENCE_LIST, 'RibList' , 'ydk.models.ietf.ietf_i2rs_rib', 'RoutingInstance.RibList', 
                [], [], 
                '''                A list of RIBs that are associated with the routing
                instance.
                ''',
                'rib_list',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('router-id', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'], 
                '''                Router ID - 32-bit number in the form of a dotted quad.
                ''',
                'router_id',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'routing-instance',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RibAddRpc.Input' : {
        'meta_info' : _MetaInfoClass('RibAddRpc.Input',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                A reference to the name of the RIB
                that is to be added.
                ''',
                'name',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('address-family', REFERENCE_IDENTITY_CLASS, 'RibFamilyIdentity' , 'ydk.models.ietf.ietf_i2rs_rib', 'RibFamilyIdentity', 
                [], [], 
                '''                The address family of the rib.
                ''',
                'address_family',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ip-rpf-check', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Each RIB can be optionally associated with a
                ENABLE_IP_RPF_CHECK attribute that enables Reverse
                path forwarding (RPF) checks on all IP routes in that
                RIB.  Reverse path forwarding (RPF) check is used to
                prevent spoofing and limit malicious traffic.
                ''',
                'ip_rpf_check',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'input',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RibAddRpc.Output' : {
        'meta_info' : _MetaInfoClass('RibAddRpc.Output',
            False, 
            [
            _MetaInfoClassMember('result', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Return the result of the rib-add operation.
                true  - success;
                false - failed
                ''',
                'result',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('reason', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The specific reason that causes the failure.
                ''',
                'reason',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'output',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RibAddRpc' : {
        'meta_info' : _MetaInfoClass('RibAddRpc',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.ietf.ietf_i2rs_rib', 'RibAddRpc.Input', 
                [], [], 
                '''                ''',
                'input',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('output', REFERENCE_CLASS, 'Output' , 'ydk.models.ietf.ietf_i2rs_rib', 'RibAddRpc.Output', 
                [], [], 
                '''                ''',
                'output',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'rib-add',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RibDeleteRpc.Input' : {
        'meta_info' : _MetaInfoClass('RibDeleteRpc.Input',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                A reference to the name of the RIB
                that is to be deleted.
                ''',
                'name',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'input',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RibDeleteRpc.Output' : {
        'meta_info' : _MetaInfoClass('RibDeleteRpc.Output',
            False, 
            [
            _MetaInfoClassMember('result', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Return the result of the rib-delete operation.
                true  - success;
                false - failed
                ''',
                'result',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('reason', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The specific reason that causes failure.
                ''',
                'reason',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'output',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RibDeleteRpc' : {
        'meta_info' : _MetaInfoClass('RibDeleteRpc',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.ietf.ietf_i2rs_rib', 'RibDeleteRpc.Input', 
                [], [], 
                '''                ''',
                'input',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('output', REFERENCE_CLASS, 'Output' , 'ydk.models.ietf.ietf_i2rs_rib', 'RibDeleteRpc.Output', 
                [], [], 
                '''                ''',
                'output',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'rib-delete',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteAddRpc.Input.Routes.RouteList.Match.Ipv4.DestSrcIpv4Address' : {
        'meta_info' : _MetaInfoClass('RouteAddRpc.Input.Routes.RouteList.Match.Ipv4.DestSrcIpv4Address',
            False, 
            [
            _MetaInfoClassMember('dest-ipv4-prefix', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                '''                The IPv4 destination address of the match.
                ''',
                'dest_ipv4_prefix',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('src-ipv4-prefix', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                '''                The IPv4 source address of the match
                ''',
                'src_ipv4_prefix',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'dest-src-ipv4-address',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteAddRpc.Input.Routes.RouteList.Match.Ipv4' : {
        'meta_info' : _MetaInfoClass('RouteAddRpc.Input.Routes.RouteList.Match.Ipv4',
            False, 
            [
            _MetaInfoClassMember('dest-ipv4-prefix', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                '''                An IPv4 destination address as the match.
                ''',
                'dest_ipv4_prefix',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('src-ipv4-prefix', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                '''                An IPv4 source address as the match.
                ''',
                'src_ipv4_prefix',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('dest-src-ipv4-address', REFERENCE_CLASS, 'DestSrcIpv4Address' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteAddRpc.Input.Routes.RouteList.Match.Ipv4.DestSrcIpv4Address', 
                [], [], 
                '''                A combination of an IPv4 source and
                an IPv4 destination address as the match.
                ''',
                'dest_src_ipv4_address',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'ipv4',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteAddRpc.Input.Routes.RouteList.Match.Ipv6.DestSrcIpv6Address' : {
        'meta_info' : _MetaInfoClass('RouteAddRpc.Input.Routes.RouteList.Match.Ipv6.DestSrcIpv6Address',
            False, 
            [
            _MetaInfoClassMember('dest-ipv6-prefix', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                '''                The IPv6 destination address of the match
                ''',
                'dest_ipv6_prefix',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('src-ipv6-prefix', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                '''                The IPv6 source address of the match.
                ''',
                'src_ipv6_prefix',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'dest-src-ipv6-address',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteAddRpc.Input.Routes.RouteList.Match.Ipv6' : {
        'meta_info' : _MetaInfoClass('RouteAddRpc.Input.Routes.RouteList.Match.Ipv6',
            False, 
            [
            _MetaInfoClassMember('dest-ipv6-prefix', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                '''                An IPv6 destination address as the match.
                ''',
                'dest_ipv6_prefix',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('src-ipv6-prefix', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                '''                An IPv6 source address as the match.
                ''',
                'src_ipv6_prefix',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('dest-src-ipv6-address', REFERENCE_CLASS, 'DestSrcIpv6Address' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteAddRpc.Input.Routes.RouteList.Match.Ipv6.DestSrcIpv6Address', 
                [], [], 
                '''                A combination of an IPv6 source and
                an IPv6 destination address as the match.
                ''',
                'dest_src_ipv6_address',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'ipv6',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteAddRpc.Input.Routes.RouteList.Match' : {
        'meta_info' : _MetaInfoClass('RouteAddRpc.Input.Routes.RouteList.Match',
            False, 
            [
            _MetaInfoClassMember('ipv4', REFERENCE_CLASS, 'Ipv4' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteAddRpc.Input.Routes.RouteList.Match.Ipv4', 
                [], [], 
                '''                IPv4 route match.
                ''',
                'ipv4',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ipv6', REFERENCE_CLASS, 'Ipv6' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteAddRpc.Input.Routes.RouteList.Match.Ipv6', 
                [], [], 
                '''                IPv6 route match.
                ''',
                'ipv6',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('mpls-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The label used for matching.
                ''',
                'mpls_label',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('mac-address', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The MAC address used for matching.
                ''',
                'mac_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('interface-identifier', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The interface used for matching.
                ''',
                'interface_identifier',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'match',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteAddRpc.Input.Routes.RouteList.RouteAttributes.AddressFamilyRouteAttributes' : {
        'meta_info' : _MetaInfoClass('RouteAddRpc.Input.Routes.RouteList.RouteAttributes.AddressFamilyRouteAttributes',
            False, 
            [
            ],
            'ietf-i2rs-rib',
            'address-family-route-attributes',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteAddRpc.Input.Routes.RouteList.RouteAttributes' : {
        'meta_info' : _MetaInfoClass('RouteAddRpc.Input.Routes.RouteList.RouteAttributes',
            False, 
            [
            _MetaInfoClassMember('route-preference', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ROUTE_PREFERENCE: This is a numerical value that
                allows for comparing routes from different
                protocols.  Static configuration is also
                considered a protocol for the purpose of this
                field.  It is also known as administrative-distance.
                The lower the value, the higher the preference.
                ''',
                'route_preference',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('local-only', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicate whether the attributes is local only.
                ''',
                'local_only',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('address-family-route-attributes', REFERENCE_CLASS, 'AddressFamilyRouteAttributes' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteAddRpc.Input.Routes.RouteList.RouteAttributes.AddressFamilyRouteAttributes', 
                [], [], 
                '''                Address family related route attributes.
                ''',
                'address_family_route_attributes',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'route-attributes',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteAddRpc.Input.Routes.RouteList.RouteVendorAttributes' : {
        'meta_info' : _MetaInfoClass('RouteAddRpc.Input.Routes.RouteList.RouteVendorAttributes',
            False, 
            [
            ],
            'ietf-i2rs-rib',
            'route-vendor-attributes',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopBase.EgressInterfaceIpv4Address' : {
        'meta_info' : _MetaInfoClass('RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopBase.EgressInterfaceIpv4Address',
            False, 
            [
            _MetaInfoClassMember('outgoing-interface', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the outgoing interface.
                ''',
                'outgoing_interface',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The nexthop points to an interface with
                an IPv4 address.
                ''',
                'ipv4_address',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'egress-interface-ipv4-address',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopBase.EgressInterfaceIpv6Address' : {
        'meta_info' : _MetaInfoClass('RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopBase.EgressInterfaceIpv6Address',
            False, 
            [
            _MetaInfoClassMember('outgoing-interface', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the outgoing interface.
                ''',
                'outgoing_interface',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                The nexthop points to an interface with
                an IPv6 address.
                ''',
                'ipv6_address',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'egress-interface-ipv6-address',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopBase.EgressInterfaceMacAddress' : {
        'meta_info' : _MetaInfoClass('RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopBase.EgressInterfaceMacAddress',
            False, 
            [
            _MetaInfoClassMember('outgoing-interface', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the outgoing interface.
                ''',
                'outgoing_interface',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ieee-mac-address', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The nexthop points to an interface with
                a specific mac-address.
                ''',
                'ieee_mac_address',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'egress-interface-mac-address',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopBase.TunnelEncap.Ipv4Header' : {
        'meta_info' : _MetaInfoClass('RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopBase.TunnelEncap.Ipv4Header',
            False, 
            [
            _MetaInfoClassMember('src-ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The source IP address of the header.
                ''',
                'src_ipv4_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('dest-ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The destination IP address of the header.
                ''',
                'dest_ipv4_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('protocol', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The protocol id of the header.
                ''',
                'protocol',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ttl', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The TTL of the header.
                ''',
                'ttl',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('dscp', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The DSCP field of the header.
                ''',
                'dscp',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'ipv4-header',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopBase.TunnelEncap.Ipv6Header' : {
        'meta_info' : _MetaInfoClass('RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopBase.TunnelEncap.Ipv6Header',
            False, 
            [
            _MetaInfoClassMember('src-ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                The source IP address of the header.
                ''',
                'src_ipv6_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('dest-ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                The destination IP address of the header.
                ''',
                'dest_ipv6_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('next-header', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The next header of the IPv6 header.
                ''',
                'next_header',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('traffic-class', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The traffic class value of the header.
                ''',
                'traffic_class',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('flow-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The flow label of the header.
                ''',
                'flow_label',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('hop-limit', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The hop limit the header.
                ''',
                'hop_limit',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'ipv6-header',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopBase.TunnelEncap.MplsHeader.LabelOperations.LabelPush' : {
        'meta_info' : _MetaInfoClass('RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopBase.TunnelEncap.MplsHeader.LabelOperations.LabelPush',
            False, 
            [
            _MetaInfoClassMember('label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The label to be pushed.
                ''',
                'label',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('s-bit', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                The s-bit of the label to be pushed. 
                ''',
                's_bit',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('tc-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The traffic class value of the label to be pushed.
                ''',
                'tc_value',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ttl-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The TTL value of the label to be pushed.
                ''',
                'ttl_value',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'label-push',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopBase.TunnelEncap.MplsHeader.LabelOperations.LabelSwap' : {
        'meta_info' : _MetaInfoClass('RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopBase.TunnelEncap.MplsHeader.LabelOperations.LabelSwap',
            False, 
            [
            _MetaInfoClassMember('in-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The label to be swapped.
                ''',
                'in_label',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('out-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The out MPLS label.
                ''',
                'out_label',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ttl-action', REFERENCE_IDENTITY_CLASS, 'TtlActionIdentity' , 'ydk.models.ietf.ietf_i2rs_rib', 'TtlActionIdentity', 
                [], [], 
                '''                The label ttl actions:
                - No-action, or
                - Copy to inner label,or
                - Decrease (the in label) by 1 and
                  copy to the out label.
                ''',
                'ttl_action',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'label-swap',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopBase.TunnelEncap.MplsHeader.LabelOperations' : {
        'meta_info' : _MetaInfoClass('RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopBase.TunnelEncap.MplsHeader.LabelOperations',
            False, 
            [
            _MetaInfoClassMember('label-oper-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                An optional identifier that points
                to a label operation.
                ''',
                'label_oper_id',
                'ietf-i2rs-rib', True),
            _MetaInfoClassMember('label-push', REFERENCE_CLASS, 'LabelPush' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopBase.TunnelEncap.MplsHeader.LabelOperations.LabelPush', 
                [], [], 
                '''                Label push operation.
                ''',
                'label_push',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('label-swap', REFERENCE_CLASS, 'LabelSwap' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopBase.TunnelEncap.MplsHeader.LabelOperations.LabelSwap', 
                [], [], 
                '''                Label swap operation.
                ''',
                'label_swap',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'label-operations',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopBase.TunnelEncap.MplsHeader' : {
        'meta_info' : _MetaInfoClass('RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopBase.TunnelEncap.MplsHeader',
            False, 
            [
            _MetaInfoClassMember('label-operations', REFERENCE_LIST, 'LabelOperations' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopBase.TunnelEncap.MplsHeader.LabelOperations', 
                [], [], 
                '''                Label operations.
                ''',
                'label_operations',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'mpls-header',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopBase.TunnelEncap.GreHeader' : {
        'meta_info' : _MetaInfoClass('RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopBase.TunnelEncap.GreHeader',
            False, 
            [
            _MetaInfoClassMember('ipv4-dest', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The destination IP address of the GRE header.
                ''',
                'ipv4_dest',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ipv6-dest', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                The destination IP address of the GRE header.
                ''',
                'ipv6_dest',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('protocol-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The protocol type of the GRE header.
                ''',
                'protocol_type',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('key', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The GRE key of the GRE header.
                ''',
                'key',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'gre-header',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopBase.TunnelEncap.NvgreHeader' : {
        'meta_info' : _MetaInfoClass('RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopBase.TunnelEncap.NvgreHeader',
            False, 
            [
            _MetaInfoClassMember('src-ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The source IP address of the header.
                ''',
                'src_ipv4_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('dest-ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The destination IP address of the header.
                ''',
                'dest_ipv4_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('protocol', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The protocol id of the header.
                ''',
                'protocol',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ttl', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The TTL of the header.
                ''',
                'ttl',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('dscp', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The DSCP field of the header.
                ''',
                'dscp',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('src-ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                The source IP address of the header.
                ''',
                'src_ipv6_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('dest-ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                The destination IP address of the header.
                ''',
                'dest_ipv6_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('next-header', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The next header of the IPv6 header.
                ''',
                'next_header',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('traffic-class', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The traffic class value of the header.
                ''',
                'traffic_class',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('flow-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The flow label of the header.
                ''',
                'flow_label',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('hop-limit', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The hop limit the header.
                ''',
                'hop_limit',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('virtual-subnet-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The subnet identifier of the NvGRE header.
                ''',
                'virtual_subnet_id',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('flow-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The flow identifier of the NvGRE header.
                ''',
                'flow_id',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'nvgre-header',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopBase.TunnelEncap.VxlanHeader' : {
        'meta_info' : _MetaInfoClass('RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopBase.TunnelEncap.VxlanHeader',
            False, 
            [
            _MetaInfoClassMember('src-ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The source IP address of the header.
                ''',
                'src_ipv4_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('dest-ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The destination IP address of the header.
                ''',
                'dest_ipv4_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('protocol', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The protocol id of the header.
                ''',
                'protocol',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ttl', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The TTL of the header.
                ''',
                'ttl',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('dscp', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The DSCP field of the header.
                ''',
                'dscp',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('src-ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                The source IP address of the header.
                ''',
                'src_ipv6_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('dest-ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                The destination IP address of the header.
                ''',
                'dest_ipv6_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('next-header', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The next header of the IPv6 header.
                ''',
                'next_header',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('traffic-class', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The traffic class value of the header.
                ''',
                'traffic_class',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('flow-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The flow label of the header.
                ''',
                'flow_label',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('hop-limit', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The hop limit the header.
                ''',
                'hop_limit',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('vxlan-identifier', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The VxLAN identifier of the VxLAN header.
                ''',
                'vxlan_identifier',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'vxlan-header',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopBase.TunnelEncap' : {
        'meta_info' : _MetaInfoClass('RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopBase.TunnelEncap',
            False, 
            [
            _MetaInfoClassMember('ipv4-header', REFERENCE_CLASS, 'Ipv4Header' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopBase.TunnelEncap.Ipv4Header', 
                [], [], 
                '''                IPv4 header.
                ''',
                'ipv4_header',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ipv6-header', REFERENCE_CLASS, 'Ipv6Header' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopBase.TunnelEncap.Ipv6Header', 
                [], [], 
                '''                IPv6 header.
                ''',
                'ipv6_header',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('mpls-header', REFERENCE_CLASS, 'MplsHeader' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopBase.TunnelEncap.MplsHeader', 
                [], [], 
                '''                MPLS header.
                ''',
                'mpls_header',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('gre-header', REFERENCE_CLASS, 'GreHeader' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopBase.TunnelEncap.GreHeader', 
                [], [], 
                '''                GRE header.
                ''',
                'gre_header',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('nvgre-header', REFERENCE_CLASS, 'NvgreHeader' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopBase.TunnelEncap.NvgreHeader', 
                [], [], 
                '''                NvGRE header.
                ''',
                'nvgre_header',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('vxlan-header', REFERENCE_CLASS, 'VxlanHeader' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopBase.TunnelEncap.VxlanHeader', 
                [], [], 
                '''                VxLAN header.
                ''',
                'vxlan_header',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'tunnel-encap',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopBase.TunnelDecap.Ipv4Decap' : {
        'meta_info' : _MetaInfoClass('RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopBase.TunnelDecap.Ipv4Decap',
            False, 
            [
            _MetaInfoClassMember('ipv4-decap', REFERENCE_IDENTITY_CLASS, 'TunnelDecapActionIdentity' , 'ydk.models.ietf.ietf_i2rs_rib', 'TunnelDecapActionIdentity', 
                [], [], 
                '''                IPv4 decap operations.
                ''',
                'ipv4_decap',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ttl-action', REFERENCE_IDENTITY_CLASS, 'TtlActionIdentity' , 'ydk.models.ietf.ietf_i2rs_rib', 'TtlActionIdentity', 
                [], [], 
                '''                The ttl actions:
                no-action or copy to inner header.
                ''',
                'ttl_action',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'ipv4-decap',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopBase.TunnelDecap.Ipv6Decap' : {
        'meta_info' : _MetaInfoClass('RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopBase.TunnelDecap.Ipv6Decap',
            False, 
            [
            _MetaInfoClassMember('ipv6-decap', REFERENCE_IDENTITY_CLASS, 'TunnelDecapActionIdentity' , 'ydk.models.ietf.ietf_i2rs_rib', 'TunnelDecapActionIdentity', 
                [], [], 
                '''                IPv6 decap operations.
                ''',
                'ipv6_decap',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('hop-limit-action', REFERENCE_IDENTITY_CLASS, 'HopLimitActionIdentity' , 'ydk.models.ietf.ietf_i2rs_rib', 'HopLimitActionIdentity', 
                [], [], 
                '''                The hop limit actions:
                no-action or copy to inner header.
                ''',
                'hop_limit_action',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'ipv6-decap',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopBase.TunnelDecap.LabelPop' : {
        'meta_info' : _MetaInfoClass('RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopBase.TunnelDecap.LabelPop',
            False, 
            [
            _MetaInfoClassMember('label-pop', REFERENCE_IDENTITY_CLASS, 'MplsLabelActionIdentity' , 'ydk.models.ietf.ietf_i2rs_rib', 'MplsLabelActionIdentity', 
                [], [], 
                '''                Pop a label from the label stack.
                ''',
                'label_pop',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ttl-action', REFERENCE_IDENTITY_CLASS, 'TtlActionIdentity' , 'ydk.models.ietf.ietf_i2rs_rib', 'TtlActionIdentity', 
                [], [], 
                '''                The label ttl action.
                ''',
                'ttl_action',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'label-pop',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopBase.TunnelDecap' : {
        'meta_info' : _MetaInfoClass('RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopBase.TunnelDecap',
            False, 
            [
            _MetaInfoClassMember('ipv4-decap', REFERENCE_CLASS, 'Ipv4Decap' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopBase.TunnelDecap.Ipv4Decap', 
                [], [], 
                '''                IPv4 decap.
                ''',
                'ipv4_decap',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ipv6-decap', REFERENCE_CLASS, 'Ipv6Decap' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopBase.TunnelDecap.Ipv6Decap', 
                [], [], 
                '''                IPv6 decap.
                ''',
                'ipv6_decap',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('label-pop', REFERENCE_CLASS, 'LabelPop' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopBase.TunnelDecap.LabelPop', 
                [], [], 
                '''                MPLS decap.
                ''',
                'label_pop',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'tunnel-decap',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopBase.LogicalTunnel' : {
        'meta_info' : _MetaInfoClass('RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopBase.LogicalTunnel',
            False, 
            [
            _MetaInfoClassMember('tunnel-type', REFERENCE_IDENTITY_CLASS, 'TunnelTypeIdentity' , 'ydk.models.ietf.ietf_i2rs_rib', 'TunnelTypeIdentity', 
                [], [], 
                '''                A tunnel type.
                ''',
                'tunnel_type',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('tunnel-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                A tunnel name that points to a logical tunnel.
                ''',
                'tunnel_name',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'logical-tunnel',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopBase' : {
        'meta_info' : _MetaInfoClass('RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopBase',
            False, 
            [
            _MetaInfoClassMember('special', REFERENCE_IDENTITY_CLASS, 'SpecialNexthopIdentity' , 'ydk.models.ietf.ietf_i2rs_rib', 'SpecialNexthopIdentity', 
                [], [], 
                '''                A special nexthop.
                ''',
                'special',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('outgoing-interface', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The nexthop is an outgoing interface.
                ''',
                'outgoing_interface',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The nexthop is an IPv4 address.
                ''',
                'ipv4_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                The nexthop is an IPv6 address.
                ''',
                'ipv6_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('egress-interface-ipv4-address', REFERENCE_CLASS, 'EgressInterfaceIpv4Address' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopBase.EgressInterfaceIpv4Address', 
                [], [], 
                '''                The nexthop is an egress-interface and an IP
                address. This can be used in cases e.g. where
                the IP address is a link-local address.
                ''',
                'egress_interface_ipv4_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('egress-interface-ipv6-address', REFERENCE_CLASS, 'EgressInterfaceIpv6Address' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopBase.EgressInterfaceIpv6Address', 
                [], [], 
                '''                The nexthop is an egress-interface and an IP
                address. This can be used in cases e.g. where
                the IP address is a link-local address.
                ''',
                'egress_interface_ipv6_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('egress-interface-mac-address', REFERENCE_CLASS, 'EgressInterfaceMacAddress' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopBase.EgressInterfaceMacAddress', 
                [], [], 
                '''                The egress interface must be an Ethernet
                interface. Address resolution is not required
                for this nexthop.
                ''',
                'egress_interface_mac_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('tunnel-encap', REFERENCE_CLASS, 'TunnelEncap' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopBase.TunnelEncap', 
                [], [], 
                '''                This can be an encap representing an IP tunnel or
                MPLS tunnel or others as defined in info model.
                An optional egress interface can be chained to the
                tunnel encap to indicate which interface to send
                the packet out on.  The egress interface is useful
                when the network device contains Ethernet interfaces
                and one needs to perform address resolution for the
                IP packet.
                ''',
                'tunnel_encap',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('tunnel-decap', REFERENCE_CLASS, 'TunnelDecap' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopBase.TunnelDecap', 
                [], [], 
                '''                This is to specify decapsulating a tunnel header.
                ''',
                'tunnel_decap',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('logical-tunnel', REFERENCE_CLASS, 'LogicalTunnel' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopBase.LogicalTunnel', 
                [], [], 
                '''                This can be a MPLS LSP or a GRE tunnel (or others
                as defined in this document), that is represented
                by a unique identifier (e.g. name).
                ''',
                'logical_tunnel',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('rib-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                A nexthop pointing to a RIB indicates that the
                route lookup needs to continue in the specified
                rib. This is a way to perform chained lookups.
                ''',
                'rib_name',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('nexthop-ref', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A nexthop reference that points to a nexthop.
                ''',
                'nexthop_ref',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'nexthop-base',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopChain.NexthopList' : {
        'meta_info' : _MetaInfoClass('RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopChain.NexthopList',
            False, 
            [
            _MetaInfoClassMember('nexthop-member-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A nexthop identifier that points
                to a nexthop list member.
                A nexthop list member is a nexthop.
                ''',
                'nexthop_member_id',
                'ietf-i2rs-rib', True),
            ],
            'ietf-i2rs-rib',
            'nexthop-list',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopChain' : {
        'meta_info' : _MetaInfoClass('RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopChain',
            False, 
            [
            _MetaInfoClassMember('nexthop-list', REFERENCE_LIST, 'NexthopList' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopChain.NexthopList', 
                [], [], 
                '''                A list of nexthops.
                ''',
                'nexthop_list',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'nexthop-chain',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopReplicates.NexthopList' : {
        'meta_info' : _MetaInfoClass('RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopReplicates.NexthopList',
            False, 
            [
            _MetaInfoClassMember('nexthop-member-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A nexthop identifier that points
                to a nexthop list member.
                A nexthop list member is a nexthop.
                ''',
                'nexthop_member_id',
                'ietf-i2rs-rib', True),
            ],
            'ietf-i2rs-rib',
            'nexthop-list',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopReplicates' : {
        'meta_info' : _MetaInfoClass('RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopReplicates',
            False, 
            [
            _MetaInfoClassMember('nexthop-list', REFERENCE_LIST, 'NexthopList' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopReplicates.NexthopList', 
                [], [], 
                '''                A list of nexthops.
                ''',
                'nexthop_list',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'nexthop-replicates',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopProtection.NexthopList' : {
        'meta_info' : _MetaInfoClass('RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopProtection.NexthopList',
            False, 
            [
            _MetaInfoClassMember('nexthop-member-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A nexthop identifier that points
                to a nexthop list member.
                A nexthop list member is a nexthop.
                ''',
                'nexthop_member_id',
                'ietf-i2rs-rib', True),
            _MetaInfoClassMember('nexthop-preference', ATTRIBUTE, 'int' , None, None, 
                [('1', '99')], [], 
                '''                Nexthop-preference is used for protection schemes.
                It is an integer value between 1 and 99.  Lower
                values are more preferred. To download a
                primary/standby/tertiary group to the FIB, the
                nexthops that are resolved and are most preferred
                are selected.
                ''',
                'nexthop_preference',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'nexthop-list',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopProtection' : {
        'meta_info' : _MetaInfoClass('RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopProtection',
            False, 
            [
            _MetaInfoClassMember('nexthop-list', REFERENCE_LIST, 'NexthopList' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopProtection.NexthopList', 
                [], [], 
                '''                A list of nexthop.
                ''',
                'nexthop_list',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'nexthop-protection',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopLb.NexthopList' : {
        'meta_info' : _MetaInfoClass('RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopLb.NexthopList',
            False, 
            [
            _MetaInfoClassMember('nexthop-member-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A nexthop identifier that points
                to a nexthop list member.
                A nexthop list member is a nexthop.
                ''',
                'nexthop_member_id',
                'ietf-i2rs-rib', True),
            _MetaInfoClassMember('nexthop-lb-weight', ATTRIBUTE, 'int' , None, None, 
                [('1', '99')], [], 
                '''                The weight of a nexthop of
                the load balance nexthops.
                ''',
                'nexthop_lb_weight',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'nexthop-list',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopLb' : {
        'meta_info' : _MetaInfoClass('RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopLb',
            False, 
            [
            _MetaInfoClassMember('nexthop-list', REFERENCE_LIST, 'NexthopList' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopLb.NexthopList', 
                [], [], 
                '''                A list of nexthop.
                ''',
                'nexthop_list',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'nexthop-lb',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteAddRpc.Input.Routes.RouteList.Nexthop' : {
        'meta_info' : _MetaInfoClass('RouteAddRpc.Input.Routes.RouteList.Nexthop',
            False, 
            [
            _MetaInfoClassMember('nexthop-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                An identifier that refers to a nexthop.
                ''',
                'nexthop_id',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('sharing-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                To indicate whether a nexthop is sharable
                or non-sharable.
                true - sharable, means the nexthop can be shared
                       with other routes
                false - non-sharable, means the nexthop can not
                       be shared with other routes.
                ''',
                'sharing_flag',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('nexthop-base', REFERENCE_CLASS, 'NexthopBase' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopBase', 
                [], [], 
                '''                The base nexthop.
                ''',
                'nexthop_base',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('nexthop-chain', REFERENCE_CLASS, 'NexthopChain' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopChain', 
                [], [], 
                '''                A chain nexthop.
                ''',
                'nexthop_chain',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('nexthop-replicates', REFERENCE_CLASS, 'NexthopReplicates' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopReplicates', 
                [], [], 
                '''                A replicates nexthop.
                ''',
                'nexthop_replicates',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('nexthop-protection', REFERENCE_CLASS, 'NexthopProtection' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopProtection', 
                [], [], 
                '''                A protection nexthop.
                ''',
                'nexthop_protection',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('nexthop-lb', REFERENCE_CLASS, 'NexthopLb' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopLb', 
                [], [], 
                '''                A load balance nexthop.
                ''',
                'nexthop_lb',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'nexthop',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteAddRpc.Input.Routes.RouteList' : {
        'meta_info' : _MetaInfoClass('RouteAddRpc.Input.Routes.RouteList',
            False, 
            [
            _MetaInfoClassMember('route-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Route index.
                ''',
                'route_index',
                'ietf-i2rs-rib', True),
            _MetaInfoClassMember('match', REFERENCE_CLASS, 'Match' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteAddRpc.Input.Routes.RouteList.Match', 
                [], [], 
                '''                The match condition specifies the
                kind of route (IPv4, MPLS, etc.)
                and the set of fields to match on.
                ''',
                'match',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('route-attributes', REFERENCE_CLASS, 'RouteAttributes' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteAddRpc.Input.Routes.RouteList.RouteAttributes', 
                [], [], 
                '''                The route attributes.
                ''',
                'route_attributes',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('route-vendor-attributes', REFERENCE_CLASS, 'RouteVendorAttributes' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteAddRpc.Input.Routes.RouteList.RouteVendorAttributes', 
                [], [], 
                '''                The route vendor attributes.
                ''',
                'route_vendor_attributes',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('nexthop', REFERENCE_CLASS, 'Nexthop' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteAddRpc.Input.Routes.RouteList.Nexthop', 
                [], [], 
                '''                The nexthop of the added route.
                ''',
                'nexthop',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'route-list',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteAddRpc.Input.Routes' : {
        'meta_info' : _MetaInfoClass('RouteAddRpc.Input.Routes',
            False, 
            [
            _MetaInfoClassMember('route-list', REFERENCE_LIST, 'RouteList' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteAddRpc.Input.Routes.RouteList', 
                [], [], 
                '''                The list of routes to be added.
                ''',
                'route_list',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'routes',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteAddRpc.Input' : {
        'meta_info' : _MetaInfoClass('RouteAddRpc.Input',
            False, 
            [
            _MetaInfoClassMember('return-failure-detail', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Whether return the failure detail.
                true  - return the failure detail;
                false - do not return the failure detail;
                the default is false.
                ''',
                'return_failure_detail',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('rib-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                A reference to the name of a rib.
                ''',
                'rib_name',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('routes', REFERENCE_CLASS, 'Routes' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteAddRpc.Input.Routes', 
                [], [], 
                '''                The routes to be added to the rib.
                ''',
                'routes',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'input',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteAddRpc.Output.FailureDetail.FailedRoutes' : {
        'meta_info' : _MetaInfoClass('RouteAddRpc.Output.FailureDetail.FailedRoutes',
            False, 
            [
            _MetaInfoClassMember('route-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The route index of the failed route.
                ''',
                'route_index',
                'ietf-i2rs-rib', True),
            _MetaInfoClassMember('error-code', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The error code that reflects the failure reason.
                ''',
                'error_code',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'failed-routes',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteAddRpc.Output.FailureDetail' : {
        'meta_info' : _MetaInfoClass('RouteAddRpc.Output.FailureDetail',
            False, 
            [
            _MetaInfoClassMember('failed-routes', REFERENCE_LIST, 'FailedRoutes' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteAddRpc.Output.FailureDetail.FailedRoutes', 
                [], [], 
                '''                The list of failed routes.
                ''',
                'failed_routes',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'failure-detail',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteAddRpc.Output' : {
        'meta_info' : _MetaInfoClass('RouteAddRpc.Output',
            False, 
            [
            _MetaInfoClassMember('success-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The numbers of routes that are successfully
                added/deleted/updated.
                ''',
                'success_count',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('failed-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The numbers of the routes that are failed
                to be added/deleted/updated.
                ''',
                'failed_count',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('failure-detail', REFERENCE_CLASS, 'FailureDetail' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteAddRpc.Output.FailureDetail', 
                [], [], 
                '''                The failure detail reflects the reason why a route
                operation fails. It is a array that includes the route
                index and error code of the failed route.
                ''',
                'failure_detail',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'output',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteAddRpc' : {
        'meta_info' : _MetaInfoClass('RouteAddRpc',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteAddRpc.Input', 
                [], [], 
                '''                ''',
                'input',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('output', REFERENCE_CLASS, 'Output' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteAddRpc.Output', 
                [], [], 
                '''                ''',
                'output',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'route-add',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteDeleteRpc.Input.Routes.RouteList.Match.Ipv4.DestSrcIpv4Address' : {
        'meta_info' : _MetaInfoClass('RouteDeleteRpc.Input.Routes.RouteList.Match.Ipv4.DestSrcIpv4Address',
            False, 
            [
            _MetaInfoClassMember('dest-ipv4-prefix', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                '''                The IPv4 destination address of the match.
                ''',
                'dest_ipv4_prefix',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('src-ipv4-prefix', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                '''                The IPv4 source address of the match
                ''',
                'src_ipv4_prefix',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'dest-src-ipv4-address',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteDeleteRpc.Input.Routes.RouteList.Match.Ipv4' : {
        'meta_info' : _MetaInfoClass('RouteDeleteRpc.Input.Routes.RouteList.Match.Ipv4',
            False, 
            [
            _MetaInfoClassMember('dest-ipv4-prefix', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                '''                An IPv4 destination address as the match.
                ''',
                'dest_ipv4_prefix',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('src-ipv4-prefix', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                '''                An IPv4 source address as the match.
                ''',
                'src_ipv4_prefix',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('dest-src-ipv4-address', REFERENCE_CLASS, 'DestSrcIpv4Address' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteDeleteRpc.Input.Routes.RouteList.Match.Ipv4.DestSrcIpv4Address', 
                [], [], 
                '''                A combination of an IPv4 source and
                an IPv4 destination address as the match.
                ''',
                'dest_src_ipv4_address',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'ipv4',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteDeleteRpc.Input.Routes.RouteList.Match.Ipv6.DestSrcIpv6Address' : {
        'meta_info' : _MetaInfoClass('RouteDeleteRpc.Input.Routes.RouteList.Match.Ipv6.DestSrcIpv6Address',
            False, 
            [
            _MetaInfoClassMember('dest-ipv6-prefix', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                '''                The IPv6 destination address of the match
                ''',
                'dest_ipv6_prefix',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('src-ipv6-prefix', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                '''                The IPv6 source address of the match.
                ''',
                'src_ipv6_prefix',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'dest-src-ipv6-address',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteDeleteRpc.Input.Routes.RouteList.Match.Ipv6' : {
        'meta_info' : _MetaInfoClass('RouteDeleteRpc.Input.Routes.RouteList.Match.Ipv6',
            False, 
            [
            _MetaInfoClassMember('dest-ipv6-prefix', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                '''                An IPv6 destination address as the match.
                ''',
                'dest_ipv6_prefix',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('src-ipv6-prefix', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                '''                An IPv6 source address as the match.
                ''',
                'src_ipv6_prefix',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('dest-src-ipv6-address', REFERENCE_CLASS, 'DestSrcIpv6Address' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteDeleteRpc.Input.Routes.RouteList.Match.Ipv6.DestSrcIpv6Address', 
                [], [], 
                '''                A combination of an IPv6 source and
                an IPv6 destination address as the match.
                ''',
                'dest_src_ipv6_address',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'ipv6',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteDeleteRpc.Input.Routes.RouteList.Match' : {
        'meta_info' : _MetaInfoClass('RouteDeleteRpc.Input.Routes.RouteList.Match',
            False, 
            [
            _MetaInfoClassMember('ipv4', REFERENCE_CLASS, 'Ipv4' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteDeleteRpc.Input.Routes.RouteList.Match.Ipv4', 
                [], [], 
                '''                IPv4 route match.
                ''',
                'ipv4',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ipv6', REFERENCE_CLASS, 'Ipv6' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteDeleteRpc.Input.Routes.RouteList.Match.Ipv6', 
                [], [], 
                '''                IPv6 route match.
                ''',
                'ipv6',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('mpls-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The label used for matching.
                ''',
                'mpls_label',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('mac-address', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The MAC address used for matching.
                ''',
                'mac_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('interface-identifier', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The interface used for matching.
                ''',
                'interface_identifier',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'match',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteDeleteRpc.Input.Routes.RouteList' : {
        'meta_info' : _MetaInfoClass('RouteDeleteRpc.Input.Routes.RouteList',
            False, 
            [
            _MetaInfoClassMember('route-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Route index.
                ''',
                'route_index',
                'ietf-i2rs-rib', True),
            _MetaInfoClassMember('match', REFERENCE_CLASS, 'Match' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteDeleteRpc.Input.Routes.RouteList.Match', 
                [], [], 
                '''                The match condition specifies the
                kind of route (IPv4, MPLS, etc.)
                and the set of fields to match on.
                ''',
                'match',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'route-list',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteDeleteRpc.Input.Routes' : {
        'meta_info' : _MetaInfoClass('RouteDeleteRpc.Input.Routes',
            False, 
            [
            _MetaInfoClassMember('route-list', REFERENCE_LIST, 'RouteList' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteDeleteRpc.Input.Routes.RouteList', 
                [], [], 
                '''                The list of routes to be deleted.
                ''',
                'route_list',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'routes',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteDeleteRpc.Input' : {
        'meta_info' : _MetaInfoClass('RouteDeleteRpc.Input',
            False, 
            [
            _MetaInfoClassMember('return-failure-detail', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Whether return the failure detail.
                true  - return the failure detail;
                false - do not return the failure detail;
                the default is false.
                ''',
                'return_failure_detail',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('rib-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                A reference to the name of a rib.
                ''',
                'rib_name',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('routes', REFERENCE_CLASS, 'Routes' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteDeleteRpc.Input.Routes', 
                [], [], 
                '''                The routes to be added to the rib.
                ''',
                'routes',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'input',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteDeleteRpc.Output.FailureDetail.FailedRoutes' : {
        'meta_info' : _MetaInfoClass('RouteDeleteRpc.Output.FailureDetail.FailedRoutes',
            False, 
            [
            _MetaInfoClassMember('route-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The route index of the failed route.
                ''',
                'route_index',
                'ietf-i2rs-rib', True),
            _MetaInfoClassMember('error-code', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The error code that reflects the failure reason.
                ''',
                'error_code',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'failed-routes',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteDeleteRpc.Output.FailureDetail' : {
        'meta_info' : _MetaInfoClass('RouteDeleteRpc.Output.FailureDetail',
            False, 
            [
            _MetaInfoClassMember('failed-routes', REFERENCE_LIST, 'FailedRoutes' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteDeleteRpc.Output.FailureDetail.FailedRoutes', 
                [], [], 
                '''                The list of failed routes.
                ''',
                'failed_routes',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'failure-detail',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteDeleteRpc.Output' : {
        'meta_info' : _MetaInfoClass('RouteDeleteRpc.Output',
            False, 
            [
            _MetaInfoClassMember('success-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The numbers of routes that are successfully
                added/deleted/updated.
                ''',
                'success_count',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('failed-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The numbers of the routes that are failed
                to be added/deleted/updated.
                ''',
                'failed_count',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('failure-detail', REFERENCE_CLASS, 'FailureDetail' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteDeleteRpc.Output.FailureDetail', 
                [], [], 
                '''                The failure detail reflects the reason why a route
                operation fails. It is a array that includes the route
                index and error code of the failed route.
                ''',
                'failure_detail',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'output',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteDeleteRpc' : {
        'meta_info' : _MetaInfoClass('RouteDeleteRpc',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteDeleteRpc.Input', 
                [], [], 
                '''                ''',
                'input',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('output', REFERENCE_CLASS, 'Output' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteDeleteRpc.Output', 
                [], [], 
                '''                ''',
                'output',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'route-delete',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.InputRoutes.RouteList.Match.Ipv4.DestSrcIpv4Address' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.InputRoutes.RouteList.Match.Ipv4.DestSrcIpv4Address',
            False, 
            [
            _MetaInfoClassMember('dest-ipv4-prefix', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                '''                The IPv4 destination address of the match.
                ''',
                'dest_ipv4_prefix',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('src-ipv4-prefix', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                '''                The IPv4 source address of the match
                ''',
                'src_ipv4_prefix',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'dest-src-ipv4-address',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.InputRoutes.RouteList.Match.Ipv4' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.InputRoutes.RouteList.Match.Ipv4',
            False, 
            [
            _MetaInfoClassMember('dest-ipv4-prefix', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                '''                An IPv4 destination address as the match.
                ''',
                'dest_ipv4_prefix',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('src-ipv4-prefix', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                '''                An IPv4 source address as the match.
                ''',
                'src_ipv4_prefix',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('dest-src-ipv4-address', REFERENCE_CLASS, 'DestSrcIpv4Address' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.InputRoutes.RouteList.Match.Ipv4.DestSrcIpv4Address', 
                [], [], 
                '''                A combination of an IPv4 source and
                an IPv4 destination address as the match.
                ''',
                'dest_src_ipv4_address',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'ipv4',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.InputRoutes.RouteList.Match.Ipv6.DestSrcIpv6Address' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.InputRoutes.RouteList.Match.Ipv6.DestSrcIpv6Address',
            False, 
            [
            _MetaInfoClassMember('dest-ipv6-prefix', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                '''                The IPv6 destination address of the match
                ''',
                'dest_ipv6_prefix',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('src-ipv6-prefix', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                '''                The IPv6 source address of the match.
                ''',
                'src_ipv6_prefix',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'dest-src-ipv6-address',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.InputRoutes.RouteList.Match.Ipv6' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.InputRoutes.RouteList.Match.Ipv6',
            False, 
            [
            _MetaInfoClassMember('dest-ipv6-prefix', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                '''                An IPv6 destination address as the match.
                ''',
                'dest_ipv6_prefix',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('src-ipv6-prefix', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                '''                An IPv6 source address as the match.
                ''',
                'src_ipv6_prefix',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('dest-src-ipv6-address', REFERENCE_CLASS, 'DestSrcIpv6Address' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.InputRoutes.RouteList.Match.Ipv6.DestSrcIpv6Address', 
                [], [], 
                '''                A combination of an IPv6 source and
                an IPv6 destination address as the match.
                ''',
                'dest_src_ipv6_address',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'ipv6',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.InputRoutes.RouteList.Match' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.InputRoutes.RouteList.Match',
            False, 
            [
            _MetaInfoClassMember('ipv4', REFERENCE_CLASS, 'Ipv4' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.InputRoutes.RouteList.Match.Ipv4', 
                [], [], 
                '''                IPv4 route match.
                ''',
                'ipv4',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ipv6', REFERENCE_CLASS, 'Ipv6' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.InputRoutes.RouteList.Match.Ipv6', 
                [], [], 
                '''                IPv6 route match.
                ''',
                'ipv6',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('mpls-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The label used for matching.
                ''',
                'mpls_label',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('mac-address', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The MAC address used for matching.
                ''',
                'mac_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('interface-identifier', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The interface used for matching.
                ''',
                'interface_identifier',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'match',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopBase.EgressInterfaceIpv4Address' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopBase.EgressInterfaceIpv4Address',
            False, 
            [
            _MetaInfoClassMember('outgoing-interface', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the outgoing interface.
                ''',
                'outgoing_interface',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The nexthop points to an interface with
                an IPv4 address.
                ''',
                'ipv4_address',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'egress-interface-ipv4-address',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopBase.EgressInterfaceIpv6Address' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopBase.EgressInterfaceIpv6Address',
            False, 
            [
            _MetaInfoClassMember('outgoing-interface', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the outgoing interface.
                ''',
                'outgoing_interface',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                The nexthop points to an interface with
                an IPv6 address.
                ''',
                'ipv6_address',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'egress-interface-ipv6-address',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopBase.EgressInterfaceMacAddress' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopBase.EgressInterfaceMacAddress',
            False, 
            [
            _MetaInfoClassMember('outgoing-interface', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the outgoing interface.
                ''',
                'outgoing_interface',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ieee-mac-address', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The nexthop points to an interface with
                a specific mac-address.
                ''',
                'ieee_mac_address',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'egress-interface-mac-address',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopBase.TunnelEncap.Ipv4Header' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopBase.TunnelEncap.Ipv4Header',
            False, 
            [
            _MetaInfoClassMember('src-ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The source IP address of the header.
                ''',
                'src_ipv4_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('dest-ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The destination IP address of the header.
                ''',
                'dest_ipv4_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('protocol', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The protocol id of the header.
                ''',
                'protocol',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ttl', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The TTL of the header.
                ''',
                'ttl',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('dscp', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The DSCP field of the header.
                ''',
                'dscp',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'ipv4-header',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopBase.TunnelEncap.Ipv6Header' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopBase.TunnelEncap.Ipv6Header',
            False, 
            [
            _MetaInfoClassMember('src-ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                The source IP address of the header.
                ''',
                'src_ipv6_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('dest-ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                The destination IP address of the header.
                ''',
                'dest_ipv6_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('next-header', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The next header of the IPv6 header.
                ''',
                'next_header',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('traffic-class', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The traffic class value of the header.
                ''',
                'traffic_class',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('flow-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The flow label of the header.
                ''',
                'flow_label',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('hop-limit', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The hop limit the header.
                ''',
                'hop_limit',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'ipv6-header',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopBase.TunnelEncap.MplsHeader.LabelOperations.LabelPush' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopBase.TunnelEncap.MplsHeader.LabelOperations.LabelPush',
            False, 
            [
            _MetaInfoClassMember('label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The label to be pushed.
                ''',
                'label',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('s-bit', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                The s-bit of the label to be pushed. 
                ''',
                's_bit',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('tc-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The traffic class value of the label to be pushed.
                ''',
                'tc_value',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ttl-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The TTL value of the label to be pushed.
                ''',
                'ttl_value',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'label-push',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopBase.TunnelEncap.MplsHeader.LabelOperations.LabelSwap' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopBase.TunnelEncap.MplsHeader.LabelOperations.LabelSwap',
            False, 
            [
            _MetaInfoClassMember('in-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The label to be swapped.
                ''',
                'in_label',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('out-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The out MPLS label.
                ''',
                'out_label',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ttl-action', REFERENCE_IDENTITY_CLASS, 'TtlActionIdentity' , 'ydk.models.ietf.ietf_i2rs_rib', 'TtlActionIdentity', 
                [], [], 
                '''                The label ttl actions:
                - No-action, or
                - Copy to inner label,or
                - Decrease (the in label) by 1 and
                  copy to the out label.
                ''',
                'ttl_action',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'label-swap',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopBase.TunnelEncap.MplsHeader.LabelOperations' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopBase.TunnelEncap.MplsHeader.LabelOperations',
            False, 
            [
            _MetaInfoClassMember('label-oper-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                An optional identifier that points
                to a label operation.
                ''',
                'label_oper_id',
                'ietf-i2rs-rib', True),
            _MetaInfoClassMember('label-push', REFERENCE_CLASS, 'LabelPush' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopBase.TunnelEncap.MplsHeader.LabelOperations.LabelPush', 
                [], [], 
                '''                Label push operation.
                ''',
                'label_push',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('label-swap', REFERENCE_CLASS, 'LabelSwap' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopBase.TunnelEncap.MplsHeader.LabelOperations.LabelSwap', 
                [], [], 
                '''                Label swap operation.
                ''',
                'label_swap',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'label-operations',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopBase.TunnelEncap.MplsHeader' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopBase.TunnelEncap.MplsHeader',
            False, 
            [
            _MetaInfoClassMember('label-operations', REFERENCE_LIST, 'LabelOperations' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopBase.TunnelEncap.MplsHeader.LabelOperations', 
                [], [], 
                '''                Label operations.
                ''',
                'label_operations',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'mpls-header',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopBase.TunnelEncap.GreHeader' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopBase.TunnelEncap.GreHeader',
            False, 
            [
            _MetaInfoClassMember('ipv4-dest', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The destination IP address of the GRE header.
                ''',
                'ipv4_dest',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ipv6-dest', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                The destination IP address of the GRE header.
                ''',
                'ipv6_dest',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('protocol-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The protocol type of the GRE header.
                ''',
                'protocol_type',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('key', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The GRE key of the GRE header.
                ''',
                'key',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'gre-header',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopBase.TunnelEncap.NvgreHeader' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopBase.TunnelEncap.NvgreHeader',
            False, 
            [
            _MetaInfoClassMember('src-ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The source IP address of the header.
                ''',
                'src_ipv4_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('dest-ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The destination IP address of the header.
                ''',
                'dest_ipv4_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('protocol', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The protocol id of the header.
                ''',
                'protocol',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ttl', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The TTL of the header.
                ''',
                'ttl',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('dscp', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The DSCP field of the header.
                ''',
                'dscp',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('src-ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                The source IP address of the header.
                ''',
                'src_ipv6_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('dest-ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                The destination IP address of the header.
                ''',
                'dest_ipv6_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('next-header', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The next header of the IPv6 header.
                ''',
                'next_header',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('traffic-class', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The traffic class value of the header.
                ''',
                'traffic_class',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('flow-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The flow label of the header.
                ''',
                'flow_label',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('hop-limit', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The hop limit the header.
                ''',
                'hop_limit',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('virtual-subnet-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The subnet identifier of the NvGRE header.
                ''',
                'virtual_subnet_id',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('flow-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The flow identifier of the NvGRE header.
                ''',
                'flow_id',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'nvgre-header',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopBase.TunnelEncap.VxlanHeader' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopBase.TunnelEncap.VxlanHeader',
            False, 
            [
            _MetaInfoClassMember('src-ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The source IP address of the header.
                ''',
                'src_ipv4_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('dest-ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The destination IP address of the header.
                ''',
                'dest_ipv4_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('protocol', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The protocol id of the header.
                ''',
                'protocol',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ttl', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The TTL of the header.
                ''',
                'ttl',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('dscp', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The DSCP field of the header.
                ''',
                'dscp',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('src-ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                The source IP address of the header.
                ''',
                'src_ipv6_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('dest-ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                The destination IP address of the header.
                ''',
                'dest_ipv6_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('next-header', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The next header of the IPv6 header.
                ''',
                'next_header',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('traffic-class', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The traffic class value of the header.
                ''',
                'traffic_class',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('flow-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The flow label of the header.
                ''',
                'flow_label',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('hop-limit', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The hop limit the header.
                ''',
                'hop_limit',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('vxlan-identifier', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The VxLAN identifier of the VxLAN header.
                ''',
                'vxlan_identifier',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'vxlan-header',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopBase.TunnelEncap' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopBase.TunnelEncap',
            False, 
            [
            _MetaInfoClassMember('ipv4-header', REFERENCE_CLASS, 'Ipv4Header' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopBase.TunnelEncap.Ipv4Header', 
                [], [], 
                '''                IPv4 header.
                ''',
                'ipv4_header',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ipv6-header', REFERENCE_CLASS, 'Ipv6Header' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopBase.TunnelEncap.Ipv6Header', 
                [], [], 
                '''                IPv6 header.
                ''',
                'ipv6_header',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('mpls-header', REFERENCE_CLASS, 'MplsHeader' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopBase.TunnelEncap.MplsHeader', 
                [], [], 
                '''                MPLS header.
                ''',
                'mpls_header',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('gre-header', REFERENCE_CLASS, 'GreHeader' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopBase.TunnelEncap.GreHeader', 
                [], [], 
                '''                GRE header.
                ''',
                'gre_header',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('nvgre-header', REFERENCE_CLASS, 'NvgreHeader' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopBase.TunnelEncap.NvgreHeader', 
                [], [], 
                '''                NvGRE header.
                ''',
                'nvgre_header',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('vxlan-header', REFERENCE_CLASS, 'VxlanHeader' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopBase.TunnelEncap.VxlanHeader', 
                [], [], 
                '''                VxLAN header.
                ''',
                'vxlan_header',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'tunnel-encap',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopBase.TunnelDecap.Ipv4Decap' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopBase.TunnelDecap.Ipv4Decap',
            False, 
            [
            _MetaInfoClassMember('ipv4-decap', REFERENCE_IDENTITY_CLASS, 'TunnelDecapActionIdentity' , 'ydk.models.ietf.ietf_i2rs_rib', 'TunnelDecapActionIdentity', 
                [], [], 
                '''                IPv4 decap operations.
                ''',
                'ipv4_decap',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ttl-action', REFERENCE_IDENTITY_CLASS, 'TtlActionIdentity' , 'ydk.models.ietf.ietf_i2rs_rib', 'TtlActionIdentity', 
                [], [], 
                '''                The ttl actions:
                no-action or copy to inner header.
                ''',
                'ttl_action',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'ipv4-decap',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopBase.TunnelDecap.Ipv6Decap' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopBase.TunnelDecap.Ipv6Decap',
            False, 
            [
            _MetaInfoClassMember('ipv6-decap', REFERENCE_IDENTITY_CLASS, 'TunnelDecapActionIdentity' , 'ydk.models.ietf.ietf_i2rs_rib', 'TunnelDecapActionIdentity', 
                [], [], 
                '''                IPv6 decap operations.
                ''',
                'ipv6_decap',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('hop-limit-action', REFERENCE_IDENTITY_CLASS, 'HopLimitActionIdentity' , 'ydk.models.ietf.ietf_i2rs_rib', 'HopLimitActionIdentity', 
                [], [], 
                '''                The hop limit actions:
                no-action or copy to inner header.
                ''',
                'hop_limit_action',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'ipv6-decap',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopBase.TunnelDecap.LabelPop' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopBase.TunnelDecap.LabelPop',
            False, 
            [
            _MetaInfoClassMember('label-pop', REFERENCE_IDENTITY_CLASS, 'MplsLabelActionIdentity' , 'ydk.models.ietf.ietf_i2rs_rib', 'MplsLabelActionIdentity', 
                [], [], 
                '''                Pop a label from the label stack.
                ''',
                'label_pop',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ttl-action', REFERENCE_IDENTITY_CLASS, 'TtlActionIdentity' , 'ydk.models.ietf.ietf_i2rs_rib', 'TtlActionIdentity', 
                [], [], 
                '''                The label ttl action.
                ''',
                'ttl_action',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'label-pop',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopBase.TunnelDecap' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopBase.TunnelDecap',
            False, 
            [
            _MetaInfoClassMember('ipv4-decap', REFERENCE_CLASS, 'Ipv4Decap' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopBase.TunnelDecap.Ipv4Decap', 
                [], [], 
                '''                IPv4 decap.
                ''',
                'ipv4_decap',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ipv6-decap', REFERENCE_CLASS, 'Ipv6Decap' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopBase.TunnelDecap.Ipv6Decap', 
                [], [], 
                '''                IPv6 decap.
                ''',
                'ipv6_decap',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('label-pop', REFERENCE_CLASS, 'LabelPop' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopBase.TunnelDecap.LabelPop', 
                [], [], 
                '''                MPLS decap.
                ''',
                'label_pop',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'tunnel-decap',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopBase.LogicalTunnel' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopBase.LogicalTunnel',
            False, 
            [
            _MetaInfoClassMember('tunnel-type', REFERENCE_IDENTITY_CLASS, 'TunnelTypeIdentity' , 'ydk.models.ietf.ietf_i2rs_rib', 'TunnelTypeIdentity', 
                [], [], 
                '''                A tunnel type.
                ''',
                'tunnel_type',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('tunnel-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                A tunnel name that points to a logical tunnel.
                ''',
                'tunnel_name',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'logical-tunnel',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopBase' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopBase',
            False, 
            [
            _MetaInfoClassMember('special', REFERENCE_IDENTITY_CLASS, 'SpecialNexthopIdentity' , 'ydk.models.ietf.ietf_i2rs_rib', 'SpecialNexthopIdentity', 
                [], [], 
                '''                A special nexthop.
                ''',
                'special',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('outgoing-interface', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The nexthop is an outgoing interface.
                ''',
                'outgoing_interface',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The nexthop is an IPv4 address.
                ''',
                'ipv4_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                The nexthop is an IPv6 address.
                ''',
                'ipv6_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('egress-interface-ipv4-address', REFERENCE_CLASS, 'EgressInterfaceIpv4Address' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopBase.EgressInterfaceIpv4Address', 
                [], [], 
                '''                The nexthop is an egress-interface and an IP
                address. This can be used in cases e.g. where
                the IP address is a link-local address.
                ''',
                'egress_interface_ipv4_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('egress-interface-ipv6-address', REFERENCE_CLASS, 'EgressInterfaceIpv6Address' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopBase.EgressInterfaceIpv6Address', 
                [], [], 
                '''                The nexthop is an egress-interface and an IP
                address. This can be used in cases e.g. where
                the IP address is a link-local address.
                ''',
                'egress_interface_ipv6_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('egress-interface-mac-address', REFERENCE_CLASS, 'EgressInterfaceMacAddress' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopBase.EgressInterfaceMacAddress', 
                [], [], 
                '''                The egress interface must be an Ethernet
                interface. Address resolution is not required
                for this nexthop.
                ''',
                'egress_interface_mac_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('tunnel-encap', REFERENCE_CLASS, 'TunnelEncap' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopBase.TunnelEncap', 
                [], [], 
                '''                This can be an encap representing an IP tunnel or
                MPLS tunnel or others as defined in info model.
                An optional egress interface can be chained to the
                tunnel encap to indicate which interface to send
                the packet out on.  The egress interface is useful
                when the network device contains Ethernet interfaces
                and one needs to perform address resolution for the
                IP packet.
                ''',
                'tunnel_encap',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('tunnel-decap', REFERENCE_CLASS, 'TunnelDecap' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopBase.TunnelDecap', 
                [], [], 
                '''                This is to specify decapsulating a tunnel header.
                ''',
                'tunnel_decap',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('logical-tunnel', REFERENCE_CLASS, 'LogicalTunnel' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopBase.LogicalTunnel', 
                [], [], 
                '''                This can be a MPLS LSP or a GRE tunnel (or others
                as defined in this document), that is represented
                by a unique identifier (e.g. name).
                ''',
                'logical_tunnel',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('rib-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                A nexthop pointing to a RIB indicates that the
                route lookup needs to continue in the specified
                rib. This is a way to perform chained lookups.
                ''',
                'rib_name',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('nexthop-ref', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A nexthop reference that points to a nexthop.
                ''',
                'nexthop_ref',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'nexthop-base',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopChain.NexthopList' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopChain.NexthopList',
            False, 
            [
            _MetaInfoClassMember('nexthop-member-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A nexthop identifier that points
                to a nexthop list member.
                A nexthop list member is a nexthop.
                ''',
                'nexthop_member_id',
                'ietf-i2rs-rib', True),
            ],
            'ietf-i2rs-rib',
            'nexthop-list',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopChain' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopChain',
            False, 
            [
            _MetaInfoClassMember('nexthop-list', REFERENCE_LIST, 'NexthopList' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopChain.NexthopList', 
                [], [], 
                '''                A list of nexthops.
                ''',
                'nexthop_list',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'nexthop-chain',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopReplicates.NexthopList' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopReplicates.NexthopList',
            False, 
            [
            _MetaInfoClassMember('nexthop-member-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A nexthop identifier that points
                to a nexthop list member.
                A nexthop list member is a nexthop.
                ''',
                'nexthop_member_id',
                'ietf-i2rs-rib', True),
            ],
            'ietf-i2rs-rib',
            'nexthop-list',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopReplicates' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopReplicates',
            False, 
            [
            _MetaInfoClassMember('nexthop-list', REFERENCE_LIST, 'NexthopList' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopReplicates.NexthopList', 
                [], [], 
                '''                A list of nexthops.
                ''',
                'nexthop_list',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'nexthop-replicates',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopProtection.NexthopList' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopProtection.NexthopList',
            False, 
            [
            _MetaInfoClassMember('nexthop-member-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A nexthop identifier that points
                to a nexthop list member.
                A nexthop list member is a nexthop.
                ''',
                'nexthop_member_id',
                'ietf-i2rs-rib', True),
            _MetaInfoClassMember('nexthop-preference', ATTRIBUTE, 'int' , None, None, 
                [('1', '99')], [], 
                '''                Nexthop-preference is used for protection schemes.
                It is an integer value between 1 and 99.  Lower
                values are more preferred. To download a
                primary/standby/tertiary group to the FIB, the
                nexthops that are resolved and are most preferred
                are selected.
                ''',
                'nexthop_preference',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'nexthop-list',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopProtection' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopProtection',
            False, 
            [
            _MetaInfoClassMember('nexthop-list', REFERENCE_LIST, 'NexthopList' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopProtection.NexthopList', 
                [], [], 
                '''                A list of nexthop.
                ''',
                'nexthop_list',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'nexthop-protection',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopLb.NexthopList' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopLb.NexthopList',
            False, 
            [
            _MetaInfoClassMember('nexthop-member-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A nexthop identifier that points
                to a nexthop list member.
                A nexthop list member is a nexthop.
                ''',
                'nexthop_member_id',
                'ietf-i2rs-rib', True),
            _MetaInfoClassMember('nexthop-lb-weight', ATTRIBUTE, 'int' , None, None, 
                [('1', '99')], [], 
                '''                The weight of a nexthop of
                the load balance nexthops.
                ''',
                'nexthop_lb_weight',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'nexthop-list',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopLb' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopLb',
            False, 
            [
            _MetaInfoClassMember('nexthop-list', REFERENCE_LIST, 'NexthopList' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopLb.NexthopList', 
                [], [], 
                '''                A list of nexthop.
                ''',
                'nexthop_list',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'nexthop-lb',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop',
            False, 
            [
            _MetaInfoClassMember('nexthop-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                An identifier that refers to a nexthop.
                ''',
                'nexthop_id',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('sharing-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                To indicate whether a nexthop is sharable
                or non-sharable.
                true - sharable, means the nexthop can be shared
                       with other routes
                false - non-sharable, means the nexthop can not
                       be shared with other routes.
                ''',
                'sharing_flag',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('nexthop-base', REFERENCE_CLASS, 'NexthopBase' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopBase', 
                [], [], 
                '''                The base nexthop.
                ''',
                'nexthop_base',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('nexthop-chain', REFERENCE_CLASS, 'NexthopChain' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopChain', 
                [], [], 
                '''                A chain nexthop.
                ''',
                'nexthop_chain',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('nexthop-replicates', REFERENCE_CLASS, 'NexthopReplicates' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopReplicates', 
                [], [], 
                '''                A replicates nexthop.
                ''',
                'nexthop_replicates',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('nexthop-protection', REFERENCE_CLASS, 'NexthopProtection' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopProtection', 
                [], [], 
                '''                A protection nexthop.
                ''',
                'nexthop_protection',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('nexthop-lb', REFERENCE_CLASS, 'NexthopLb' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopLb', 
                [], [], 
                '''                A load balance nexthop.
                ''',
                'nexthop_lb',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'updated-nexthop',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedRouteAttr.AddressFamilyRouteAttributes' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedRouteAttr.AddressFamilyRouteAttributes',
            False, 
            [
            ],
            'ietf-i2rs-rib',
            'address-family-route-attributes',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedRouteAttr' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedRouteAttr',
            False, 
            [
            _MetaInfoClassMember('route-preference', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ROUTE_PREFERENCE: This is a numerical value that
                allows for comparing routes from different
                protocols.  Static configuration is also
                considered a protocol for the purpose of this
                field.  It is also known as administrative-distance.
                The lower the value, the higher the preference.
                ''',
                'route_preference',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('local-only', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicate whether the attributes is local only.
                ''',
                'local_only',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('address-family-route-attributes', REFERENCE_CLASS, 'AddressFamilyRouteAttributes' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedRouteAttr.AddressFamilyRouteAttributes', 
                [], [], 
                '''                Address family related route attributes.
                ''',
                'address_family_route_attributes',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'updated-route-attr',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedRouteVendorAttr' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedRouteVendorAttr',
            False, 
            [
            ],
            'ietf-i2rs-rib',
            'updated-route-vendor-attr',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.InputRoutes.RouteList' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.InputRoutes.RouteList',
            False, 
            [
            _MetaInfoClassMember('route-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Route index.
                ''',
                'route_index',
                'ietf-i2rs-rib', True),
            _MetaInfoClassMember('match', REFERENCE_CLASS, 'Match' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.InputRoutes.RouteList.Match', 
                [], [], 
                '''                The match condition specifies the
                kind of route (IPv4, MPLS, etc.)
                and the set of fields to match on.
                ''',
                'match',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('updated-nexthop', REFERENCE_CLASS, 'UpdatedNexthop' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop', 
                [], [], 
                '''                The nexthop used for updating.
                ''',
                'updated_nexthop',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('updated-route-attr', REFERENCE_CLASS, 'UpdatedRouteAttr' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedRouteAttr', 
                [], [], 
                '''                The route attributes used for updating.
                ''',
                'updated_route_attr',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('updated-route-vendor-attr', REFERENCE_CLASS, 'UpdatedRouteVendorAttr' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedRouteVendorAttr', 
                [], [], 
                '''                The vendor route attributes used for updating.
                ''',
                'updated_route_vendor_attr',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'route-list',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.InputRoutes' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.InputRoutes',
            False, 
            [
            _MetaInfoClassMember('route-list', REFERENCE_LIST, 'RouteList' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.InputRoutes.RouteList', 
                [], [], 
                '''                The list of routes to be updated.
                ''',
                'route_list',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'input-routes',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.InputRouteAttributes.AddressFamilyRouteAttributes' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.InputRouteAttributes.AddressFamilyRouteAttributes',
            False, 
            [
            ],
            'ietf-i2rs-rib',
            'address-family-route-attributes',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.InputRouteAttributes' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.InputRouteAttributes',
            False, 
            [
            _MetaInfoClassMember('route-preference', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ROUTE_PREFERENCE: This is a numerical value that
                allows for comparing routes from different
                protocols.  Static configuration is also
                considered a protocol for the purpose of this
                field.  It is also known as administrative-distance.
                The lower the value, the higher the preference.
                ''',
                'route_preference',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('local-only', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicate whether the attributes is local only.
                ''',
                'local_only',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('address-family-route-attributes', REFERENCE_CLASS, 'AddressFamilyRouteAttributes' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.InputRouteAttributes.AddressFamilyRouteAttributes', 
                [], [], 
                '''                Address family related route attributes.
                ''',
                'address_family_route_attributes',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'input-route-attributes',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopBase.EgressInterfaceIpv4Address' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopBase.EgressInterfaceIpv4Address',
            False, 
            [
            _MetaInfoClassMember('outgoing-interface', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the outgoing interface.
                ''',
                'outgoing_interface',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The nexthop points to an interface with
                an IPv4 address.
                ''',
                'ipv4_address',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'egress-interface-ipv4-address',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopBase.EgressInterfaceIpv6Address' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopBase.EgressInterfaceIpv6Address',
            False, 
            [
            _MetaInfoClassMember('outgoing-interface', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the outgoing interface.
                ''',
                'outgoing_interface',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                The nexthop points to an interface with
                an IPv6 address.
                ''',
                'ipv6_address',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'egress-interface-ipv6-address',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopBase.EgressInterfaceMacAddress' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopBase.EgressInterfaceMacAddress',
            False, 
            [
            _MetaInfoClassMember('outgoing-interface', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the outgoing interface.
                ''',
                'outgoing_interface',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ieee-mac-address', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The nexthop points to an interface with
                a specific mac-address.
                ''',
                'ieee_mac_address',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'egress-interface-mac-address',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopBase.TunnelEncap.Ipv4Header' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopBase.TunnelEncap.Ipv4Header',
            False, 
            [
            _MetaInfoClassMember('src-ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The source IP address of the header.
                ''',
                'src_ipv4_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('dest-ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The destination IP address of the header.
                ''',
                'dest_ipv4_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('protocol', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The protocol id of the header.
                ''',
                'protocol',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ttl', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The TTL of the header.
                ''',
                'ttl',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('dscp', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The DSCP field of the header.
                ''',
                'dscp',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'ipv4-header',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopBase.TunnelEncap.Ipv6Header' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopBase.TunnelEncap.Ipv6Header',
            False, 
            [
            _MetaInfoClassMember('src-ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                The source IP address of the header.
                ''',
                'src_ipv6_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('dest-ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                The destination IP address of the header.
                ''',
                'dest_ipv6_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('next-header', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The next header of the IPv6 header.
                ''',
                'next_header',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('traffic-class', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The traffic class value of the header.
                ''',
                'traffic_class',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('flow-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The flow label of the header.
                ''',
                'flow_label',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('hop-limit', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The hop limit the header.
                ''',
                'hop_limit',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'ipv6-header',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopBase.TunnelEncap.MplsHeader.LabelOperations.LabelPush' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopBase.TunnelEncap.MplsHeader.LabelOperations.LabelPush',
            False, 
            [
            _MetaInfoClassMember('label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The label to be pushed.
                ''',
                'label',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('s-bit', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                The s-bit of the label to be pushed. 
                ''',
                's_bit',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('tc-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The traffic class value of the label to be pushed.
                ''',
                'tc_value',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ttl-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The TTL value of the label to be pushed.
                ''',
                'ttl_value',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'label-push',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopBase.TunnelEncap.MplsHeader.LabelOperations.LabelSwap' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopBase.TunnelEncap.MplsHeader.LabelOperations.LabelSwap',
            False, 
            [
            _MetaInfoClassMember('in-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The label to be swapped.
                ''',
                'in_label',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('out-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The out MPLS label.
                ''',
                'out_label',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ttl-action', REFERENCE_IDENTITY_CLASS, 'TtlActionIdentity' , 'ydk.models.ietf.ietf_i2rs_rib', 'TtlActionIdentity', 
                [], [], 
                '''                The label ttl actions:
                - No-action, or
                - Copy to inner label,or
                - Decrease (the in label) by 1 and
                  copy to the out label.
                ''',
                'ttl_action',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'label-swap',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopBase.TunnelEncap.MplsHeader.LabelOperations' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopBase.TunnelEncap.MplsHeader.LabelOperations',
            False, 
            [
            _MetaInfoClassMember('label-oper-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                An optional identifier that points
                to a label operation.
                ''',
                'label_oper_id',
                'ietf-i2rs-rib', True),
            _MetaInfoClassMember('label-push', REFERENCE_CLASS, 'LabelPush' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopBase.TunnelEncap.MplsHeader.LabelOperations.LabelPush', 
                [], [], 
                '''                Label push operation.
                ''',
                'label_push',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('label-swap', REFERENCE_CLASS, 'LabelSwap' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopBase.TunnelEncap.MplsHeader.LabelOperations.LabelSwap', 
                [], [], 
                '''                Label swap operation.
                ''',
                'label_swap',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'label-operations',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopBase.TunnelEncap.MplsHeader' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopBase.TunnelEncap.MplsHeader',
            False, 
            [
            _MetaInfoClassMember('label-operations', REFERENCE_LIST, 'LabelOperations' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopBase.TunnelEncap.MplsHeader.LabelOperations', 
                [], [], 
                '''                Label operations.
                ''',
                'label_operations',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'mpls-header',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopBase.TunnelEncap.GreHeader' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopBase.TunnelEncap.GreHeader',
            False, 
            [
            _MetaInfoClassMember('ipv4-dest', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The destination IP address of the GRE header.
                ''',
                'ipv4_dest',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ipv6-dest', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                The destination IP address of the GRE header.
                ''',
                'ipv6_dest',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('protocol-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The protocol type of the GRE header.
                ''',
                'protocol_type',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('key', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The GRE key of the GRE header.
                ''',
                'key',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'gre-header',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopBase.TunnelEncap.NvgreHeader' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopBase.TunnelEncap.NvgreHeader',
            False, 
            [
            _MetaInfoClassMember('src-ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The source IP address of the header.
                ''',
                'src_ipv4_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('dest-ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The destination IP address of the header.
                ''',
                'dest_ipv4_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('protocol', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The protocol id of the header.
                ''',
                'protocol',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ttl', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The TTL of the header.
                ''',
                'ttl',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('dscp', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The DSCP field of the header.
                ''',
                'dscp',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('src-ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                The source IP address of the header.
                ''',
                'src_ipv6_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('dest-ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                The destination IP address of the header.
                ''',
                'dest_ipv6_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('next-header', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The next header of the IPv6 header.
                ''',
                'next_header',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('traffic-class', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The traffic class value of the header.
                ''',
                'traffic_class',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('flow-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The flow label of the header.
                ''',
                'flow_label',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('hop-limit', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The hop limit the header.
                ''',
                'hop_limit',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('virtual-subnet-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The subnet identifier of the NvGRE header.
                ''',
                'virtual_subnet_id',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('flow-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The flow identifier of the NvGRE header.
                ''',
                'flow_id',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'nvgre-header',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopBase.TunnelEncap.VxlanHeader' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopBase.TunnelEncap.VxlanHeader',
            False, 
            [
            _MetaInfoClassMember('src-ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The source IP address of the header.
                ''',
                'src_ipv4_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('dest-ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The destination IP address of the header.
                ''',
                'dest_ipv4_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('protocol', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The protocol id of the header.
                ''',
                'protocol',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ttl', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The TTL of the header.
                ''',
                'ttl',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('dscp', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The DSCP field of the header.
                ''',
                'dscp',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('src-ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                The source IP address of the header.
                ''',
                'src_ipv6_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('dest-ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                The destination IP address of the header.
                ''',
                'dest_ipv6_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('next-header', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The next header of the IPv6 header.
                ''',
                'next_header',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('traffic-class', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The traffic class value of the header.
                ''',
                'traffic_class',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('flow-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The flow label of the header.
                ''',
                'flow_label',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('hop-limit', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The hop limit the header.
                ''',
                'hop_limit',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('vxlan-identifier', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The VxLAN identifier of the VxLAN header.
                ''',
                'vxlan_identifier',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'vxlan-header',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopBase.TunnelEncap' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopBase.TunnelEncap',
            False, 
            [
            _MetaInfoClassMember('ipv4-header', REFERENCE_CLASS, 'Ipv4Header' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopBase.TunnelEncap.Ipv4Header', 
                [], [], 
                '''                IPv4 header.
                ''',
                'ipv4_header',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ipv6-header', REFERENCE_CLASS, 'Ipv6Header' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopBase.TunnelEncap.Ipv6Header', 
                [], [], 
                '''                IPv6 header.
                ''',
                'ipv6_header',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('mpls-header', REFERENCE_CLASS, 'MplsHeader' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopBase.TunnelEncap.MplsHeader', 
                [], [], 
                '''                MPLS header.
                ''',
                'mpls_header',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('gre-header', REFERENCE_CLASS, 'GreHeader' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopBase.TunnelEncap.GreHeader', 
                [], [], 
                '''                GRE header.
                ''',
                'gre_header',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('nvgre-header', REFERENCE_CLASS, 'NvgreHeader' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopBase.TunnelEncap.NvgreHeader', 
                [], [], 
                '''                NvGRE header.
                ''',
                'nvgre_header',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('vxlan-header', REFERENCE_CLASS, 'VxlanHeader' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopBase.TunnelEncap.VxlanHeader', 
                [], [], 
                '''                VxLAN header.
                ''',
                'vxlan_header',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'tunnel-encap',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopBase.TunnelDecap.Ipv4Decap' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopBase.TunnelDecap.Ipv4Decap',
            False, 
            [
            _MetaInfoClassMember('ipv4-decap', REFERENCE_IDENTITY_CLASS, 'TunnelDecapActionIdentity' , 'ydk.models.ietf.ietf_i2rs_rib', 'TunnelDecapActionIdentity', 
                [], [], 
                '''                IPv4 decap operations.
                ''',
                'ipv4_decap',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ttl-action', REFERENCE_IDENTITY_CLASS, 'TtlActionIdentity' , 'ydk.models.ietf.ietf_i2rs_rib', 'TtlActionIdentity', 
                [], [], 
                '''                The ttl actions:
                no-action or copy to inner header.
                ''',
                'ttl_action',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'ipv4-decap',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopBase.TunnelDecap.Ipv6Decap' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopBase.TunnelDecap.Ipv6Decap',
            False, 
            [
            _MetaInfoClassMember('ipv6-decap', REFERENCE_IDENTITY_CLASS, 'TunnelDecapActionIdentity' , 'ydk.models.ietf.ietf_i2rs_rib', 'TunnelDecapActionIdentity', 
                [], [], 
                '''                IPv6 decap operations.
                ''',
                'ipv6_decap',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('hop-limit-action', REFERENCE_IDENTITY_CLASS, 'HopLimitActionIdentity' , 'ydk.models.ietf.ietf_i2rs_rib', 'HopLimitActionIdentity', 
                [], [], 
                '''                The hop limit actions:
                no-action or copy to inner header.
                ''',
                'hop_limit_action',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'ipv6-decap',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopBase.TunnelDecap.LabelPop' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopBase.TunnelDecap.LabelPop',
            False, 
            [
            _MetaInfoClassMember('label-pop', REFERENCE_IDENTITY_CLASS, 'MplsLabelActionIdentity' , 'ydk.models.ietf.ietf_i2rs_rib', 'MplsLabelActionIdentity', 
                [], [], 
                '''                Pop a label from the label stack.
                ''',
                'label_pop',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ttl-action', REFERENCE_IDENTITY_CLASS, 'TtlActionIdentity' , 'ydk.models.ietf.ietf_i2rs_rib', 'TtlActionIdentity', 
                [], [], 
                '''                The label ttl action.
                ''',
                'ttl_action',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'label-pop',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopBase.TunnelDecap' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopBase.TunnelDecap',
            False, 
            [
            _MetaInfoClassMember('ipv4-decap', REFERENCE_CLASS, 'Ipv4Decap' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopBase.TunnelDecap.Ipv4Decap', 
                [], [], 
                '''                IPv4 decap.
                ''',
                'ipv4_decap',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ipv6-decap', REFERENCE_CLASS, 'Ipv6Decap' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopBase.TunnelDecap.Ipv6Decap', 
                [], [], 
                '''                IPv6 decap.
                ''',
                'ipv6_decap',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('label-pop', REFERENCE_CLASS, 'LabelPop' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopBase.TunnelDecap.LabelPop', 
                [], [], 
                '''                MPLS decap.
                ''',
                'label_pop',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'tunnel-decap',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopBase.LogicalTunnel' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopBase.LogicalTunnel',
            False, 
            [
            _MetaInfoClassMember('tunnel-type', REFERENCE_IDENTITY_CLASS, 'TunnelTypeIdentity' , 'ydk.models.ietf.ietf_i2rs_rib', 'TunnelTypeIdentity', 
                [], [], 
                '''                A tunnel type.
                ''',
                'tunnel_type',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('tunnel-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                A tunnel name that points to a logical tunnel.
                ''',
                'tunnel_name',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'logical-tunnel',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopBase' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopBase',
            False, 
            [
            _MetaInfoClassMember('special', REFERENCE_IDENTITY_CLASS, 'SpecialNexthopIdentity' , 'ydk.models.ietf.ietf_i2rs_rib', 'SpecialNexthopIdentity', 
                [], [], 
                '''                A special nexthop.
                ''',
                'special',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('outgoing-interface', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The nexthop is an outgoing interface.
                ''',
                'outgoing_interface',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The nexthop is an IPv4 address.
                ''',
                'ipv4_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                The nexthop is an IPv6 address.
                ''',
                'ipv6_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('egress-interface-ipv4-address', REFERENCE_CLASS, 'EgressInterfaceIpv4Address' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopBase.EgressInterfaceIpv4Address', 
                [], [], 
                '''                The nexthop is an egress-interface and an IP
                address. This can be used in cases e.g. where
                the IP address is a link-local address.
                ''',
                'egress_interface_ipv4_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('egress-interface-ipv6-address', REFERENCE_CLASS, 'EgressInterfaceIpv6Address' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopBase.EgressInterfaceIpv6Address', 
                [], [], 
                '''                The nexthop is an egress-interface and an IP
                address. This can be used in cases e.g. where
                the IP address is a link-local address.
                ''',
                'egress_interface_ipv6_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('egress-interface-mac-address', REFERENCE_CLASS, 'EgressInterfaceMacAddress' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopBase.EgressInterfaceMacAddress', 
                [], [], 
                '''                The egress interface must be an Ethernet
                interface. Address resolution is not required
                for this nexthop.
                ''',
                'egress_interface_mac_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('tunnel-encap', REFERENCE_CLASS, 'TunnelEncap' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopBase.TunnelEncap', 
                [], [], 
                '''                This can be an encap representing an IP tunnel or
                MPLS tunnel or others as defined in info model.
                An optional egress interface can be chained to the
                tunnel encap to indicate which interface to send
                the packet out on.  The egress interface is useful
                when the network device contains Ethernet interfaces
                and one needs to perform address resolution for the
                IP packet.
                ''',
                'tunnel_encap',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('tunnel-decap', REFERENCE_CLASS, 'TunnelDecap' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopBase.TunnelDecap', 
                [], [], 
                '''                This is to specify decapsulating a tunnel header.
                ''',
                'tunnel_decap',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('logical-tunnel', REFERENCE_CLASS, 'LogicalTunnel' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopBase.LogicalTunnel', 
                [], [], 
                '''                This can be a MPLS LSP or a GRE tunnel (or others
                as defined in this document), that is represented
                by a unique identifier (e.g. name).
                ''',
                'logical_tunnel',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('rib-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                A nexthop pointing to a RIB indicates that the
                route lookup needs to continue in the specified
                rib. This is a way to perform chained lookups.
                ''',
                'rib_name',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('nexthop-ref', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A nexthop reference that points to a nexthop.
                ''',
                'nexthop_ref',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'nexthop-base',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopChain.NexthopList' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopChain.NexthopList',
            False, 
            [
            _MetaInfoClassMember('nexthop-member-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A nexthop identifier that points
                to a nexthop list member.
                A nexthop list member is a nexthop.
                ''',
                'nexthop_member_id',
                'ietf-i2rs-rib', True),
            ],
            'ietf-i2rs-rib',
            'nexthop-list',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopChain' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopChain',
            False, 
            [
            _MetaInfoClassMember('nexthop-list', REFERENCE_LIST, 'NexthopList' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopChain.NexthopList', 
                [], [], 
                '''                A list of nexthops.
                ''',
                'nexthop_list',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'nexthop-chain',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopReplicates.NexthopList' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopReplicates.NexthopList',
            False, 
            [
            _MetaInfoClassMember('nexthop-member-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A nexthop identifier that points
                to a nexthop list member.
                A nexthop list member is a nexthop.
                ''',
                'nexthop_member_id',
                'ietf-i2rs-rib', True),
            ],
            'ietf-i2rs-rib',
            'nexthop-list',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopReplicates' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopReplicates',
            False, 
            [
            _MetaInfoClassMember('nexthop-list', REFERENCE_LIST, 'NexthopList' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopReplicates.NexthopList', 
                [], [], 
                '''                A list of nexthops.
                ''',
                'nexthop_list',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'nexthop-replicates',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopProtection.NexthopList' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopProtection.NexthopList',
            False, 
            [
            _MetaInfoClassMember('nexthop-member-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A nexthop identifier that points
                to a nexthop list member.
                A nexthop list member is a nexthop.
                ''',
                'nexthop_member_id',
                'ietf-i2rs-rib', True),
            _MetaInfoClassMember('nexthop-preference', ATTRIBUTE, 'int' , None, None, 
                [('1', '99')], [], 
                '''                Nexthop-preference is used for protection schemes.
                It is an integer value between 1 and 99.  Lower
                values are more preferred. To download a
                primary/standby/tertiary group to the FIB, the
                nexthops that are resolved and are most preferred
                are selected.
                ''',
                'nexthop_preference',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'nexthop-list',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopProtection' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopProtection',
            False, 
            [
            _MetaInfoClassMember('nexthop-list', REFERENCE_LIST, 'NexthopList' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopProtection.NexthopList', 
                [], [], 
                '''                A list of nexthop.
                ''',
                'nexthop_list',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'nexthop-protection',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopLb.NexthopList' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopLb.NexthopList',
            False, 
            [
            _MetaInfoClassMember('nexthop-member-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A nexthop identifier that points
                to a nexthop list member.
                A nexthop list member is a nexthop.
                ''',
                'nexthop_member_id',
                'ietf-i2rs-rib', True),
            _MetaInfoClassMember('nexthop-lb-weight', ATTRIBUTE, 'int' , None, None, 
                [('1', '99')], [], 
                '''                The weight of a nexthop of
                the load balance nexthops.
                ''',
                'nexthop_lb_weight',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'nexthop-list',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopLb' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopLb',
            False, 
            [
            _MetaInfoClassMember('nexthop-list', REFERENCE_LIST, 'NexthopList' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopLb.NexthopList', 
                [], [], 
                '''                A list of nexthop.
                ''',
                'nexthop_list',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'nexthop-lb',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop',
            False, 
            [
            _MetaInfoClassMember('nexthop-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                An identifier that refers to a nexthop.
                ''',
                'nexthop_id',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('sharing-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                To indicate whether a nexthop is sharable
                or non-sharable.
                true - sharable, means the nexthop can be shared
                       with other routes
                false - non-sharable, means the nexthop can not
                       be shared with other routes.
                ''',
                'sharing_flag',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('nexthop-base', REFERENCE_CLASS, 'NexthopBase' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopBase', 
                [], [], 
                '''                The base nexthop.
                ''',
                'nexthop_base',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('nexthop-chain', REFERENCE_CLASS, 'NexthopChain' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopChain', 
                [], [], 
                '''                A chain nexthop.
                ''',
                'nexthop_chain',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('nexthop-replicates', REFERENCE_CLASS, 'NexthopReplicates' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopReplicates', 
                [], [], 
                '''                A replicates nexthop.
                ''',
                'nexthop_replicates',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('nexthop-protection', REFERENCE_CLASS, 'NexthopProtection' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopProtection', 
                [], [], 
                '''                A protection nexthop.
                ''',
                'nexthop_protection',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('nexthop-lb', REFERENCE_CLASS, 'NexthopLb' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopLb', 
                [], [], 
                '''                A load balance nexthop.
                ''',
                'nexthop_lb',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'updated-nexthop',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.UpdateParametors.UpdatedRouteAttr.AddressFamilyRouteAttributes' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.UpdateParametors.UpdatedRouteAttr.AddressFamilyRouteAttributes',
            False, 
            [
            ],
            'ietf-i2rs-rib',
            'address-family-route-attributes',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.UpdateParametors.UpdatedRouteAttr' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.UpdateParametors.UpdatedRouteAttr',
            False, 
            [
            _MetaInfoClassMember('route-preference', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ROUTE_PREFERENCE: This is a numerical value that
                allows for comparing routes from different
                protocols.  Static configuration is also
                considered a protocol for the purpose of this
                field.  It is also known as administrative-distance.
                The lower the value, the higher the preference.
                ''',
                'route_preference',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('local-only', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicate whether the attributes is local only.
                ''',
                'local_only',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('address-family-route-attributes', REFERENCE_CLASS, 'AddressFamilyRouteAttributes' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.UpdateParametors.UpdatedRouteAttr.AddressFamilyRouteAttributes', 
                [], [], 
                '''                Address family related route attributes.
                ''',
                'address_family_route_attributes',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'updated-route-attr',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.UpdateParametors.UpdatedRouteVendorAttr' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.UpdateParametors.UpdatedRouteVendorAttr',
            False, 
            [
            ],
            'ietf-i2rs-rib',
            'updated-route-vendor-attr',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.UpdateParametors' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.UpdateParametors',
            False, 
            [
            _MetaInfoClassMember('updated-nexthop', REFERENCE_CLASS, 'UpdatedNexthop' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop', 
                [], [], 
                '''                The nexthop used for updating.
                ''',
                'updated_nexthop',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('updated-route-attr', REFERENCE_CLASS, 'UpdatedRouteAttr' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.UpdateParametors.UpdatedRouteAttr', 
                [], [], 
                '''                The route attributes used for updating.
                ''',
                'updated_route_attr',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('updated-route-vendor-attr', REFERENCE_CLASS, 'UpdatedRouteVendorAttr' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.UpdateParametors.UpdatedRouteVendorAttr', 
                [], [], 
                '''                The vendor route attributes used for updating.
                ''',
                'updated_route_vendor_attr',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'update-parametors',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.InputRouteVendorAttributes' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.InputRouteVendorAttributes',
            False, 
            [
            ],
            'ietf-i2rs-rib',
            'input-route-vendor-attributes',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopBase.EgressInterfaceIpv4Address' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopBase.EgressInterfaceIpv4Address',
            False, 
            [
            _MetaInfoClassMember('outgoing-interface', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the outgoing interface.
                ''',
                'outgoing_interface',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The nexthop points to an interface with
                an IPv4 address.
                ''',
                'ipv4_address',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'egress-interface-ipv4-address',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopBase.EgressInterfaceIpv6Address' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopBase.EgressInterfaceIpv6Address',
            False, 
            [
            _MetaInfoClassMember('outgoing-interface', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the outgoing interface.
                ''',
                'outgoing_interface',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                The nexthop points to an interface with
                an IPv6 address.
                ''',
                'ipv6_address',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'egress-interface-ipv6-address',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopBase.EgressInterfaceMacAddress' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopBase.EgressInterfaceMacAddress',
            False, 
            [
            _MetaInfoClassMember('outgoing-interface', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the outgoing interface.
                ''',
                'outgoing_interface',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ieee-mac-address', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The nexthop points to an interface with
                a specific mac-address.
                ''',
                'ieee_mac_address',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'egress-interface-mac-address',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopBase.TunnelEncap.Ipv4Header' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopBase.TunnelEncap.Ipv4Header',
            False, 
            [
            _MetaInfoClassMember('src-ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The source IP address of the header.
                ''',
                'src_ipv4_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('dest-ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The destination IP address of the header.
                ''',
                'dest_ipv4_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('protocol', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The protocol id of the header.
                ''',
                'protocol',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ttl', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The TTL of the header.
                ''',
                'ttl',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('dscp', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The DSCP field of the header.
                ''',
                'dscp',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'ipv4-header',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopBase.TunnelEncap.Ipv6Header' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopBase.TunnelEncap.Ipv6Header',
            False, 
            [
            _MetaInfoClassMember('src-ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                The source IP address of the header.
                ''',
                'src_ipv6_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('dest-ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                The destination IP address of the header.
                ''',
                'dest_ipv6_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('next-header', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The next header of the IPv6 header.
                ''',
                'next_header',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('traffic-class', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The traffic class value of the header.
                ''',
                'traffic_class',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('flow-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The flow label of the header.
                ''',
                'flow_label',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('hop-limit', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The hop limit the header.
                ''',
                'hop_limit',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'ipv6-header',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopBase.TunnelEncap.MplsHeader.LabelOperations.LabelPush' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopBase.TunnelEncap.MplsHeader.LabelOperations.LabelPush',
            False, 
            [
            _MetaInfoClassMember('label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The label to be pushed.
                ''',
                'label',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('s-bit', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                The s-bit of the label to be pushed. 
                ''',
                's_bit',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('tc-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The traffic class value of the label to be pushed.
                ''',
                'tc_value',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ttl-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The TTL value of the label to be pushed.
                ''',
                'ttl_value',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'label-push',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopBase.TunnelEncap.MplsHeader.LabelOperations.LabelSwap' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopBase.TunnelEncap.MplsHeader.LabelOperations.LabelSwap',
            False, 
            [
            _MetaInfoClassMember('in-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The label to be swapped.
                ''',
                'in_label',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('out-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The out MPLS label.
                ''',
                'out_label',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ttl-action', REFERENCE_IDENTITY_CLASS, 'TtlActionIdentity' , 'ydk.models.ietf.ietf_i2rs_rib', 'TtlActionIdentity', 
                [], [], 
                '''                The label ttl actions:
                - No-action, or
                - Copy to inner label,or
                - Decrease (the in label) by 1 and
                  copy to the out label.
                ''',
                'ttl_action',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'label-swap',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopBase.TunnelEncap.MplsHeader.LabelOperations' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopBase.TunnelEncap.MplsHeader.LabelOperations',
            False, 
            [
            _MetaInfoClassMember('label-oper-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                An optional identifier that points
                to a label operation.
                ''',
                'label_oper_id',
                'ietf-i2rs-rib', True),
            _MetaInfoClassMember('label-push', REFERENCE_CLASS, 'LabelPush' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopBase.TunnelEncap.MplsHeader.LabelOperations.LabelPush', 
                [], [], 
                '''                Label push operation.
                ''',
                'label_push',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('label-swap', REFERENCE_CLASS, 'LabelSwap' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopBase.TunnelEncap.MplsHeader.LabelOperations.LabelSwap', 
                [], [], 
                '''                Label swap operation.
                ''',
                'label_swap',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'label-operations',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopBase.TunnelEncap.MplsHeader' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopBase.TunnelEncap.MplsHeader',
            False, 
            [
            _MetaInfoClassMember('label-operations', REFERENCE_LIST, 'LabelOperations' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopBase.TunnelEncap.MplsHeader.LabelOperations', 
                [], [], 
                '''                Label operations.
                ''',
                'label_operations',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'mpls-header',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopBase.TunnelEncap.GreHeader' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopBase.TunnelEncap.GreHeader',
            False, 
            [
            _MetaInfoClassMember('ipv4-dest', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The destination IP address of the GRE header.
                ''',
                'ipv4_dest',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ipv6-dest', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                The destination IP address of the GRE header.
                ''',
                'ipv6_dest',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('protocol-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The protocol type of the GRE header.
                ''',
                'protocol_type',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('key', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The GRE key of the GRE header.
                ''',
                'key',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'gre-header',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopBase.TunnelEncap.NvgreHeader' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopBase.TunnelEncap.NvgreHeader',
            False, 
            [
            _MetaInfoClassMember('src-ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The source IP address of the header.
                ''',
                'src_ipv4_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('dest-ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The destination IP address of the header.
                ''',
                'dest_ipv4_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('protocol', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The protocol id of the header.
                ''',
                'protocol',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ttl', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The TTL of the header.
                ''',
                'ttl',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('dscp', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The DSCP field of the header.
                ''',
                'dscp',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('src-ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                The source IP address of the header.
                ''',
                'src_ipv6_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('dest-ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                The destination IP address of the header.
                ''',
                'dest_ipv6_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('next-header', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The next header of the IPv6 header.
                ''',
                'next_header',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('traffic-class', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The traffic class value of the header.
                ''',
                'traffic_class',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('flow-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The flow label of the header.
                ''',
                'flow_label',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('hop-limit', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The hop limit the header.
                ''',
                'hop_limit',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('virtual-subnet-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The subnet identifier of the NvGRE header.
                ''',
                'virtual_subnet_id',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('flow-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The flow identifier of the NvGRE header.
                ''',
                'flow_id',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'nvgre-header',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopBase.TunnelEncap.VxlanHeader' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopBase.TunnelEncap.VxlanHeader',
            False, 
            [
            _MetaInfoClassMember('src-ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The source IP address of the header.
                ''',
                'src_ipv4_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('dest-ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The destination IP address of the header.
                ''',
                'dest_ipv4_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('protocol', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The protocol id of the header.
                ''',
                'protocol',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ttl', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The TTL of the header.
                ''',
                'ttl',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('dscp', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The DSCP field of the header.
                ''',
                'dscp',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('src-ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                The source IP address of the header.
                ''',
                'src_ipv6_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('dest-ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                The destination IP address of the header.
                ''',
                'dest_ipv6_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('next-header', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The next header of the IPv6 header.
                ''',
                'next_header',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('traffic-class', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The traffic class value of the header.
                ''',
                'traffic_class',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('flow-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The flow label of the header.
                ''',
                'flow_label',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('hop-limit', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The hop limit the header.
                ''',
                'hop_limit',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('vxlan-identifier', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The VxLAN identifier of the VxLAN header.
                ''',
                'vxlan_identifier',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'vxlan-header',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopBase.TunnelEncap' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopBase.TunnelEncap',
            False, 
            [
            _MetaInfoClassMember('ipv4-header', REFERENCE_CLASS, 'Ipv4Header' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopBase.TunnelEncap.Ipv4Header', 
                [], [], 
                '''                IPv4 header.
                ''',
                'ipv4_header',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ipv6-header', REFERENCE_CLASS, 'Ipv6Header' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopBase.TunnelEncap.Ipv6Header', 
                [], [], 
                '''                IPv6 header.
                ''',
                'ipv6_header',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('mpls-header', REFERENCE_CLASS, 'MplsHeader' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopBase.TunnelEncap.MplsHeader', 
                [], [], 
                '''                MPLS header.
                ''',
                'mpls_header',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('gre-header', REFERENCE_CLASS, 'GreHeader' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopBase.TunnelEncap.GreHeader', 
                [], [], 
                '''                GRE header.
                ''',
                'gre_header',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('nvgre-header', REFERENCE_CLASS, 'NvgreHeader' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopBase.TunnelEncap.NvgreHeader', 
                [], [], 
                '''                NvGRE header.
                ''',
                'nvgre_header',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('vxlan-header', REFERENCE_CLASS, 'VxlanHeader' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopBase.TunnelEncap.VxlanHeader', 
                [], [], 
                '''                VxLAN header.
                ''',
                'vxlan_header',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'tunnel-encap',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopBase.TunnelDecap.Ipv4Decap' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopBase.TunnelDecap.Ipv4Decap',
            False, 
            [
            _MetaInfoClassMember('ipv4-decap', REFERENCE_IDENTITY_CLASS, 'TunnelDecapActionIdentity' , 'ydk.models.ietf.ietf_i2rs_rib', 'TunnelDecapActionIdentity', 
                [], [], 
                '''                IPv4 decap operations.
                ''',
                'ipv4_decap',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ttl-action', REFERENCE_IDENTITY_CLASS, 'TtlActionIdentity' , 'ydk.models.ietf.ietf_i2rs_rib', 'TtlActionIdentity', 
                [], [], 
                '''                The ttl actions:
                no-action or copy to inner header.
                ''',
                'ttl_action',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'ipv4-decap',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopBase.TunnelDecap.Ipv6Decap' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopBase.TunnelDecap.Ipv6Decap',
            False, 
            [
            _MetaInfoClassMember('ipv6-decap', REFERENCE_IDENTITY_CLASS, 'TunnelDecapActionIdentity' , 'ydk.models.ietf.ietf_i2rs_rib', 'TunnelDecapActionIdentity', 
                [], [], 
                '''                IPv6 decap operations.
                ''',
                'ipv6_decap',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('hop-limit-action', REFERENCE_IDENTITY_CLASS, 'HopLimitActionIdentity' , 'ydk.models.ietf.ietf_i2rs_rib', 'HopLimitActionIdentity', 
                [], [], 
                '''                The hop limit actions:
                no-action or copy to inner header.
                ''',
                'hop_limit_action',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'ipv6-decap',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopBase.TunnelDecap.LabelPop' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopBase.TunnelDecap.LabelPop',
            False, 
            [
            _MetaInfoClassMember('label-pop', REFERENCE_IDENTITY_CLASS, 'MplsLabelActionIdentity' , 'ydk.models.ietf.ietf_i2rs_rib', 'MplsLabelActionIdentity', 
                [], [], 
                '''                Pop a label from the label stack.
                ''',
                'label_pop',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ttl-action', REFERENCE_IDENTITY_CLASS, 'TtlActionIdentity' , 'ydk.models.ietf.ietf_i2rs_rib', 'TtlActionIdentity', 
                [], [], 
                '''                The label ttl action.
                ''',
                'ttl_action',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'label-pop',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopBase.TunnelDecap' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopBase.TunnelDecap',
            False, 
            [
            _MetaInfoClassMember('ipv4-decap', REFERENCE_CLASS, 'Ipv4Decap' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopBase.TunnelDecap.Ipv4Decap', 
                [], [], 
                '''                IPv4 decap.
                ''',
                'ipv4_decap',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ipv6-decap', REFERENCE_CLASS, 'Ipv6Decap' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopBase.TunnelDecap.Ipv6Decap', 
                [], [], 
                '''                IPv6 decap.
                ''',
                'ipv6_decap',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('label-pop', REFERENCE_CLASS, 'LabelPop' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopBase.TunnelDecap.LabelPop', 
                [], [], 
                '''                MPLS decap.
                ''',
                'label_pop',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'tunnel-decap',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopBase.LogicalTunnel' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopBase.LogicalTunnel',
            False, 
            [
            _MetaInfoClassMember('tunnel-type', REFERENCE_IDENTITY_CLASS, 'TunnelTypeIdentity' , 'ydk.models.ietf.ietf_i2rs_rib', 'TunnelTypeIdentity', 
                [], [], 
                '''                A tunnel type.
                ''',
                'tunnel_type',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('tunnel-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                A tunnel name that points to a logical tunnel.
                ''',
                'tunnel_name',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'logical-tunnel',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopBase' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopBase',
            False, 
            [
            _MetaInfoClassMember('special', REFERENCE_IDENTITY_CLASS, 'SpecialNexthopIdentity' , 'ydk.models.ietf.ietf_i2rs_rib', 'SpecialNexthopIdentity', 
                [], [], 
                '''                A special nexthop.
                ''',
                'special',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('outgoing-interface', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The nexthop is an outgoing interface.
                ''',
                'outgoing_interface',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The nexthop is an IPv4 address.
                ''',
                'ipv4_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                The nexthop is an IPv6 address.
                ''',
                'ipv6_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('egress-interface-ipv4-address', REFERENCE_CLASS, 'EgressInterfaceIpv4Address' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopBase.EgressInterfaceIpv4Address', 
                [], [], 
                '''                The nexthop is an egress-interface and an IP
                address. This can be used in cases e.g. where
                the IP address is a link-local address.
                ''',
                'egress_interface_ipv4_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('egress-interface-ipv6-address', REFERENCE_CLASS, 'EgressInterfaceIpv6Address' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopBase.EgressInterfaceIpv6Address', 
                [], [], 
                '''                The nexthop is an egress-interface and an IP
                address. This can be used in cases e.g. where
                the IP address is a link-local address.
                ''',
                'egress_interface_ipv6_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('egress-interface-mac-address', REFERENCE_CLASS, 'EgressInterfaceMacAddress' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopBase.EgressInterfaceMacAddress', 
                [], [], 
                '''                The egress interface must be an Ethernet
                interface. Address resolution is not required
                for this nexthop.
                ''',
                'egress_interface_mac_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('tunnel-encap', REFERENCE_CLASS, 'TunnelEncap' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopBase.TunnelEncap', 
                [], [], 
                '''                This can be an encap representing an IP tunnel or
                MPLS tunnel or others as defined in info model.
                An optional egress interface can be chained to the
                tunnel encap to indicate which interface to send
                the packet out on.  The egress interface is useful
                when the network device contains Ethernet interfaces
                and one needs to perform address resolution for the
                IP packet.
                ''',
                'tunnel_encap',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('tunnel-decap', REFERENCE_CLASS, 'TunnelDecap' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopBase.TunnelDecap', 
                [], [], 
                '''                This is to specify decapsulating a tunnel header.
                ''',
                'tunnel_decap',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('logical-tunnel', REFERENCE_CLASS, 'LogicalTunnel' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopBase.LogicalTunnel', 
                [], [], 
                '''                This can be a MPLS LSP or a GRE tunnel (or others
                as defined in this document), that is represented
                by a unique identifier (e.g. name).
                ''',
                'logical_tunnel',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('rib-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                A nexthop pointing to a RIB indicates that the
                route lookup needs to continue in the specified
                rib. This is a way to perform chained lookups.
                ''',
                'rib_name',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('nexthop-ref', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A nexthop reference that points to a nexthop.
                ''',
                'nexthop_ref',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'nexthop-base',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopChain.NexthopList' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopChain.NexthopList',
            False, 
            [
            _MetaInfoClassMember('nexthop-member-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A nexthop identifier that points
                to a nexthop list member.
                A nexthop list member is a nexthop.
                ''',
                'nexthop_member_id',
                'ietf-i2rs-rib', True),
            ],
            'ietf-i2rs-rib',
            'nexthop-list',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopChain' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopChain',
            False, 
            [
            _MetaInfoClassMember('nexthop-list', REFERENCE_LIST, 'NexthopList' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopChain.NexthopList', 
                [], [], 
                '''                A list of nexthops.
                ''',
                'nexthop_list',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'nexthop-chain',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopReplicates.NexthopList' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopReplicates.NexthopList',
            False, 
            [
            _MetaInfoClassMember('nexthop-member-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A nexthop identifier that points
                to a nexthop list member.
                A nexthop list member is a nexthop.
                ''',
                'nexthop_member_id',
                'ietf-i2rs-rib', True),
            ],
            'ietf-i2rs-rib',
            'nexthop-list',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopReplicates' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopReplicates',
            False, 
            [
            _MetaInfoClassMember('nexthop-list', REFERENCE_LIST, 'NexthopList' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopReplicates.NexthopList', 
                [], [], 
                '''                A list of nexthops.
                ''',
                'nexthop_list',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'nexthop-replicates',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopProtection.NexthopList' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopProtection.NexthopList',
            False, 
            [
            _MetaInfoClassMember('nexthop-member-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A nexthop identifier that points
                to a nexthop list member.
                A nexthop list member is a nexthop.
                ''',
                'nexthop_member_id',
                'ietf-i2rs-rib', True),
            _MetaInfoClassMember('nexthop-preference', ATTRIBUTE, 'int' , None, None, 
                [('1', '99')], [], 
                '''                Nexthop-preference is used for protection schemes.
                It is an integer value between 1 and 99.  Lower
                values are more preferred. To download a
                primary/standby/tertiary group to the FIB, the
                nexthops that are resolved and are most preferred
                are selected.
                ''',
                'nexthop_preference',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'nexthop-list',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopProtection' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopProtection',
            False, 
            [
            _MetaInfoClassMember('nexthop-list', REFERENCE_LIST, 'NexthopList' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopProtection.NexthopList', 
                [], [], 
                '''                A list of nexthop.
                ''',
                'nexthop_list',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'nexthop-protection',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopLb.NexthopList' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopLb.NexthopList',
            False, 
            [
            _MetaInfoClassMember('nexthop-member-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A nexthop identifier that points
                to a nexthop list member.
                A nexthop list member is a nexthop.
                ''',
                'nexthop_member_id',
                'ietf-i2rs-rib', True),
            _MetaInfoClassMember('nexthop-lb-weight', ATTRIBUTE, 'int' , None, None, 
                [('1', '99')], [], 
                '''                The weight of a nexthop of
                the load balance nexthops.
                ''',
                'nexthop_lb_weight',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'nexthop-list',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopLb' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopLb',
            False, 
            [
            _MetaInfoClassMember('nexthop-list', REFERENCE_LIST, 'NexthopList' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopLb.NexthopList', 
                [], [], 
                '''                A list of nexthop.
                ''',
                'nexthop_list',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'nexthop-lb',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop',
            False, 
            [
            _MetaInfoClassMember('nexthop-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                An identifier that refers to a nexthop.
                ''',
                'nexthop_id',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('sharing-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                To indicate whether a nexthop is sharable
                or non-sharable.
                true - sharable, means the nexthop can be shared
                       with other routes
                false - non-sharable, means the nexthop can not
                       be shared with other routes.
                ''',
                'sharing_flag',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('nexthop-base', REFERENCE_CLASS, 'NexthopBase' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopBase', 
                [], [], 
                '''                The base nexthop.
                ''',
                'nexthop_base',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('nexthop-chain', REFERENCE_CLASS, 'NexthopChain' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopChain', 
                [], [], 
                '''                A chain nexthop.
                ''',
                'nexthop_chain',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('nexthop-replicates', REFERENCE_CLASS, 'NexthopReplicates' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopReplicates', 
                [], [], 
                '''                A replicates nexthop.
                ''',
                'nexthop_replicates',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('nexthop-protection', REFERENCE_CLASS, 'NexthopProtection' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopProtection', 
                [], [], 
                '''                A protection nexthop.
                ''',
                'nexthop_protection',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('nexthop-lb', REFERENCE_CLASS, 'NexthopLb' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopLb', 
                [], [], 
                '''                A load balance nexthop.
                ''',
                'nexthop_lb',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'updated-nexthop',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedRouteAttr.AddressFamilyRouteAttributes' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedRouteAttr.AddressFamilyRouteAttributes',
            False, 
            [
            ],
            'ietf-i2rs-rib',
            'address-family-route-attributes',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedRouteAttr' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedRouteAttr',
            False, 
            [
            _MetaInfoClassMember('route-preference', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ROUTE_PREFERENCE: This is a numerical value that
                allows for comparing routes from different
                protocols.  Static configuration is also
                considered a protocol for the purpose of this
                field.  It is also known as administrative-distance.
                The lower the value, the higher the preference.
                ''',
                'route_preference',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('local-only', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicate whether the attributes is local only.
                ''',
                'local_only',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('address-family-route-attributes', REFERENCE_CLASS, 'AddressFamilyRouteAttributes' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedRouteAttr.AddressFamilyRouteAttributes', 
                [], [], 
                '''                Address family related route attributes.
                ''',
                'address_family_route_attributes',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'updated-route-attr',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedRouteVendorAttr' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedRouteVendorAttr',
            False, 
            [
            ],
            'ietf-i2rs-rib',
            'updated-route-vendor-attr',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.UpdateParametersVendor' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.UpdateParametersVendor',
            False, 
            [
            _MetaInfoClassMember('updated-nexthop', REFERENCE_CLASS, 'UpdatedNexthop' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop', 
                [], [], 
                '''                The nexthop used for updating.
                ''',
                'updated_nexthop',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('updated-route-attr', REFERENCE_CLASS, 'UpdatedRouteAttr' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedRouteAttr', 
                [], [], 
                '''                The route attributes used for updating.
                ''',
                'updated_route_attr',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('updated-route-vendor-attr', REFERENCE_CLASS, 'UpdatedRouteVendorAttr' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedRouteVendorAttr', 
                [], [], 
                '''                The vendor route attributes used for updating.
                ''',
                'updated_route_vendor_attr',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'update-parameters-vendor',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.InputNexthop.NexthopBase.EgressInterfaceIpv4Address' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.InputNexthop.NexthopBase.EgressInterfaceIpv4Address',
            False, 
            [
            _MetaInfoClassMember('outgoing-interface', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the outgoing interface.
                ''',
                'outgoing_interface',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The nexthop points to an interface with
                an IPv4 address.
                ''',
                'ipv4_address',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'egress-interface-ipv4-address',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.InputNexthop.NexthopBase.EgressInterfaceIpv6Address' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.InputNexthop.NexthopBase.EgressInterfaceIpv6Address',
            False, 
            [
            _MetaInfoClassMember('outgoing-interface', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the outgoing interface.
                ''',
                'outgoing_interface',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                The nexthop points to an interface with
                an IPv6 address.
                ''',
                'ipv6_address',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'egress-interface-ipv6-address',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.InputNexthop.NexthopBase.EgressInterfaceMacAddress' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.InputNexthop.NexthopBase.EgressInterfaceMacAddress',
            False, 
            [
            _MetaInfoClassMember('outgoing-interface', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the outgoing interface.
                ''',
                'outgoing_interface',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ieee-mac-address', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The nexthop points to an interface with
                a specific mac-address.
                ''',
                'ieee_mac_address',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'egress-interface-mac-address',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.InputNexthop.NexthopBase.TunnelEncap.Ipv4Header' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.InputNexthop.NexthopBase.TunnelEncap.Ipv4Header',
            False, 
            [
            _MetaInfoClassMember('src-ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The source IP address of the header.
                ''',
                'src_ipv4_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('dest-ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The destination IP address of the header.
                ''',
                'dest_ipv4_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('protocol', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The protocol id of the header.
                ''',
                'protocol',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ttl', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The TTL of the header.
                ''',
                'ttl',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('dscp', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The DSCP field of the header.
                ''',
                'dscp',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'ipv4-header',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.InputNexthop.NexthopBase.TunnelEncap.Ipv6Header' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.InputNexthop.NexthopBase.TunnelEncap.Ipv6Header',
            False, 
            [
            _MetaInfoClassMember('src-ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                The source IP address of the header.
                ''',
                'src_ipv6_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('dest-ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                The destination IP address of the header.
                ''',
                'dest_ipv6_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('next-header', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The next header of the IPv6 header.
                ''',
                'next_header',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('traffic-class', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The traffic class value of the header.
                ''',
                'traffic_class',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('flow-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The flow label of the header.
                ''',
                'flow_label',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('hop-limit', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The hop limit the header.
                ''',
                'hop_limit',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'ipv6-header',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.InputNexthop.NexthopBase.TunnelEncap.MplsHeader.LabelOperations.LabelPush' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.InputNexthop.NexthopBase.TunnelEncap.MplsHeader.LabelOperations.LabelPush',
            False, 
            [
            _MetaInfoClassMember('label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The label to be pushed.
                ''',
                'label',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('s-bit', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                The s-bit of the label to be pushed. 
                ''',
                's_bit',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('tc-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The traffic class value of the label to be pushed.
                ''',
                'tc_value',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ttl-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The TTL value of the label to be pushed.
                ''',
                'ttl_value',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'label-push',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.InputNexthop.NexthopBase.TunnelEncap.MplsHeader.LabelOperations.LabelSwap' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.InputNexthop.NexthopBase.TunnelEncap.MplsHeader.LabelOperations.LabelSwap',
            False, 
            [
            _MetaInfoClassMember('in-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The label to be swapped.
                ''',
                'in_label',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('out-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The out MPLS label.
                ''',
                'out_label',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ttl-action', REFERENCE_IDENTITY_CLASS, 'TtlActionIdentity' , 'ydk.models.ietf.ietf_i2rs_rib', 'TtlActionIdentity', 
                [], [], 
                '''                The label ttl actions:
                - No-action, or
                - Copy to inner label,or
                - Decrease (the in label) by 1 and
                  copy to the out label.
                ''',
                'ttl_action',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'label-swap',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.InputNexthop.NexthopBase.TunnelEncap.MplsHeader.LabelOperations' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.InputNexthop.NexthopBase.TunnelEncap.MplsHeader.LabelOperations',
            False, 
            [
            _MetaInfoClassMember('label-oper-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                An optional identifier that points
                to a label operation.
                ''',
                'label_oper_id',
                'ietf-i2rs-rib', True),
            _MetaInfoClassMember('label-push', REFERENCE_CLASS, 'LabelPush' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.InputNexthop.NexthopBase.TunnelEncap.MplsHeader.LabelOperations.LabelPush', 
                [], [], 
                '''                Label push operation.
                ''',
                'label_push',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('label-swap', REFERENCE_CLASS, 'LabelSwap' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.InputNexthop.NexthopBase.TunnelEncap.MplsHeader.LabelOperations.LabelSwap', 
                [], [], 
                '''                Label swap operation.
                ''',
                'label_swap',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'label-operations',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.InputNexthop.NexthopBase.TunnelEncap.MplsHeader' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.InputNexthop.NexthopBase.TunnelEncap.MplsHeader',
            False, 
            [
            _MetaInfoClassMember('label-operations', REFERENCE_LIST, 'LabelOperations' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.InputNexthop.NexthopBase.TunnelEncap.MplsHeader.LabelOperations', 
                [], [], 
                '''                Label operations.
                ''',
                'label_operations',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'mpls-header',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.InputNexthop.NexthopBase.TunnelEncap.GreHeader' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.InputNexthop.NexthopBase.TunnelEncap.GreHeader',
            False, 
            [
            _MetaInfoClassMember('ipv4-dest', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The destination IP address of the GRE header.
                ''',
                'ipv4_dest',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ipv6-dest', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                The destination IP address of the GRE header.
                ''',
                'ipv6_dest',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('protocol-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The protocol type of the GRE header.
                ''',
                'protocol_type',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('key', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The GRE key of the GRE header.
                ''',
                'key',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'gre-header',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.InputNexthop.NexthopBase.TunnelEncap.NvgreHeader' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.InputNexthop.NexthopBase.TunnelEncap.NvgreHeader',
            False, 
            [
            _MetaInfoClassMember('src-ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The source IP address of the header.
                ''',
                'src_ipv4_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('dest-ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The destination IP address of the header.
                ''',
                'dest_ipv4_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('protocol', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The protocol id of the header.
                ''',
                'protocol',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ttl', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The TTL of the header.
                ''',
                'ttl',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('dscp', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The DSCP field of the header.
                ''',
                'dscp',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('src-ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                The source IP address of the header.
                ''',
                'src_ipv6_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('dest-ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                The destination IP address of the header.
                ''',
                'dest_ipv6_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('next-header', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The next header of the IPv6 header.
                ''',
                'next_header',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('traffic-class', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The traffic class value of the header.
                ''',
                'traffic_class',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('flow-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The flow label of the header.
                ''',
                'flow_label',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('hop-limit', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The hop limit the header.
                ''',
                'hop_limit',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('virtual-subnet-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The subnet identifier of the NvGRE header.
                ''',
                'virtual_subnet_id',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('flow-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The flow identifier of the NvGRE header.
                ''',
                'flow_id',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'nvgre-header',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.InputNexthop.NexthopBase.TunnelEncap.VxlanHeader' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.InputNexthop.NexthopBase.TunnelEncap.VxlanHeader',
            False, 
            [
            _MetaInfoClassMember('src-ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The source IP address of the header.
                ''',
                'src_ipv4_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('dest-ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The destination IP address of the header.
                ''',
                'dest_ipv4_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('protocol', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The protocol id of the header.
                ''',
                'protocol',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ttl', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The TTL of the header.
                ''',
                'ttl',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('dscp', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The DSCP field of the header.
                ''',
                'dscp',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('src-ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                The source IP address of the header.
                ''',
                'src_ipv6_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('dest-ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                The destination IP address of the header.
                ''',
                'dest_ipv6_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('next-header', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The next header of the IPv6 header.
                ''',
                'next_header',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('traffic-class', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The traffic class value of the header.
                ''',
                'traffic_class',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('flow-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The flow label of the header.
                ''',
                'flow_label',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('hop-limit', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The hop limit the header.
                ''',
                'hop_limit',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('vxlan-identifier', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The VxLAN identifier of the VxLAN header.
                ''',
                'vxlan_identifier',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'vxlan-header',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.InputNexthop.NexthopBase.TunnelEncap' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.InputNexthop.NexthopBase.TunnelEncap',
            False, 
            [
            _MetaInfoClassMember('ipv4-header', REFERENCE_CLASS, 'Ipv4Header' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.InputNexthop.NexthopBase.TunnelEncap.Ipv4Header', 
                [], [], 
                '''                IPv4 header.
                ''',
                'ipv4_header',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ipv6-header', REFERENCE_CLASS, 'Ipv6Header' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.InputNexthop.NexthopBase.TunnelEncap.Ipv6Header', 
                [], [], 
                '''                IPv6 header.
                ''',
                'ipv6_header',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('mpls-header', REFERENCE_CLASS, 'MplsHeader' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.InputNexthop.NexthopBase.TunnelEncap.MplsHeader', 
                [], [], 
                '''                MPLS header.
                ''',
                'mpls_header',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('gre-header', REFERENCE_CLASS, 'GreHeader' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.InputNexthop.NexthopBase.TunnelEncap.GreHeader', 
                [], [], 
                '''                GRE header.
                ''',
                'gre_header',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('nvgre-header', REFERENCE_CLASS, 'NvgreHeader' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.InputNexthop.NexthopBase.TunnelEncap.NvgreHeader', 
                [], [], 
                '''                NvGRE header.
                ''',
                'nvgre_header',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('vxlan-header', REFERENCE_CLASS, 'VxlanHeader' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.InputNexthop.NexthopBase.TunnelEncap.VxlanHeader', 
                [], [], 
                '''                VxLAN header.
                ''',
                'vxlan_header',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'tunnel-encap',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.InputNexthop.NexthopBase.TunnelDecap.Ipv4Decap' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.InputNexthop.NexthopBase.TunnelDecap.Ipv4Decap',
            False, 
            [
            _MetaInfoClassMember('ipv4-decap', REFERENCE_IDENTITY_CLASS, 'TunnelDecapActionIdentity' , 'ydk.models.ietf.ietf_i2rs_rib', 'TunnelDecapActionIdentity', 
                [], [], 
                '''                IPv4 decap operations.
                ''',
                'ipv4_decap',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ttl-action', REFERENCE_IDENTITY_CLASS, 'TtlActionIdentity' , 'ydk.models.ietf.ietf_i2rs_rib', 'TtlActionIdentity', 
                [], [], 
                '''                The ttl actions:
                no-action or copy to inner header.
                ''',
                'ttl_action',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'ipv4-decap',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.InputNexthop.NexthopBase.TunnelDecap.Ipv6Decap' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.InputNexthop.NexthopBase.TunnelDecap.Ipv6Decap',
            False, 
            [
            _MetaInfoClassMember('ipv6-decap', REFERENCE_IDENTITY_CLASS, 'TunnelDecapActionIdentity' , 'ydk.models.ietf.ietf_i2rs_rib', 'TunnelDecapActionIdentity', 
                [], [], 
                '''                IPv6 decap operations.
                ''',
                'ipv6_decap',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('hop-limit-action', REFERENCE_IDENTITY_CLASS, 'HopLimitActionIdentity' , 'ydk.models.ietf.ietf_i2rs_rib', 'HopLimitActionIdentity', 
                [], [], 
                '''                The hop limit actions:
                no-action or copy to inner header.
                ''',
                'hop_limit_action',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'ipv6-decap',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.InputNexthop.NexthopBase.TunnelDecap.LabelPop' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.InputNexthop.NexthopBase.TunnelDecap.LabelPop',
            False, 
            [
            _MetaInfoClassMember('label-pop', REFERENCE_IDENTITY_CLASS, 'MplsLabelActionIdentity' , 'ydk.models.ietf.ietf_i2rs_rib', 'MplsLabelActionIdentity', 
                [], [], 
                '''                Pop a label from the label stack.
                ''',
                'label_pop',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ttl-action', REFERENCE_IDENTITY_CLASS, 'TtlActionIdentity' , 'ydk.models.ietf.ietf_i2rs_rib', 'TtlActionIdentity', 
                [], [], 
                '''                The label ttl action.
                ''',
                'ttl_action',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'label-pop',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.InputNexthop.NexthopBase.TunnelDecap' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.InputNexthop.NexthopBase.TunnelDecap',
            False, 
            [
            _MetaInfoClassMember('ipv4-decap', REFERENCE_CLASS, 'Ipv4Decap' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.InputNexthop.NexthopBase.TunnelDecap.Ipv4Decap', 
                [], [], 
                '''                IPv4 decap.
                ''',
                'ipv4_decap',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ipv6-decap', REFERENCE_CLASS, 'Ipv6Decap' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.InputNexthop.NexthopBase.TunnelDecap.Ipv6Decap', 
                [], [], 
                '''                IPv6 decap.
                ''',
                'ipv6_decap',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('label-pop', REFERENCE_CLASS, 'LabelPop' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.InputNexthop.NexthopBase.TunnelDecap.LabelPop', 
                [], [], 
                '''                MPLS decap.
                ''',
                'label_pop',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'tunnel-decap',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.InputNexthop.NexthopBase.LogicalTunnel' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.InputNexthop.NexthopBase.LogicalTunnel',
            False, 
            [
            _MetaInfoClassMember('tunnel-type', REFERENCE_IDENTITY_CLASS, 'TunnelTypeIdentity' , 'ydk.models.ietf.ietf_i2rs_rib', 'TunnelTypeIdentity', 
                [], [], 
                '''                A tunnel type.
                ''',
                'tunnel_type',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('tunnel-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                A tunnel name that points to a logical tunnel.
                ''',
                'tunnel_name',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'logical-tunnel',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.InputNexthop.NexthopBase' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.InputNexthop.NexthopBase',
            False, 
            [
            _MetaInfoClassMember('special', REFERENCE_IDENTITY_CLASS, 'SpecialNexthopIdentity' , 'ydk.models.ietf.ietf_i2rs_rib', 'SpecialNexthopIdentity', 
                [], [], 
                '''                A special nexthop.
                ''',
                'special',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('outgoing-interface', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The nexthop is an outgoing interface.
                ''',
                'outgoing_interface',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The nexthop is an IPv4 address.
                ''',
                'ipv4_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                The nexthop is an IPv6 address.
                ''',
                'ipv6_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('egress-interface-ipv4-address', REFERENCE_CLASS, 'EgressInterfaceIpv4Address' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.InputNexthop.NexthopBase.EgressInterfaceIpv4Address', 
                [], [], 
                '''                The nexthop is an egress-interface and an IP
                address. This can be used in cases e.g. where
                the IP address is a link-local address.
                ''',
                'egress_interface_ipv4_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('egress-interface-ipv6-address', REFERENCE_CLASS, 'EgressInterfaceIpv6Address' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.InputNexthop.NexthopBase.EgressInterfaceIpv6Address', 
                [], [], 
                '''                The nexthop is an egress-interface and an IP
                address. This can be used in cases e.g. where
                the IP address is a link-local address.
                ''',
                'egress_interface_ipv6_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('egress-interface-mac-address', REFERENCE_CLASS, 'EgressInterfaceMacAddress' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.InputNexthop.NexthopBase.EgressInterfaceMacAddress', 
                [], [], 
                '''                The egress interface must be an Ethernet
                interface. Address resolution is not required
                for this nexthop.
                ''',
                'egress_interface_mac_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('tunnel-encap', REFERENCE_CLASS, 'TunnelEncap' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.InputNexthop.NexthopBase.TunnelEncap', 
                [], [], 
                '''                This can be an encap representing an IP tunnel or
                MPLS tunnel or others as defined in info model.
                An optional egress interface can be chained to the
                tunnel encap to indicate which interface to send
                the packet out on.  The egress interface is useful
                when the network device contains Ethernet interfaces
                and one needs to perform address resolution for the
                IP packet.
                ''',
                'tunnel_encap',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('tunnel-decap', REFERENCE_CLASS, 'TunnelDecap' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.InputNexthop.NexthopBase.TunnelDecap', 
                [], [], 
                '''                This is to specify decapsulating a tunnel header.
                ''',
                'tunnel_decap',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('logical-tunnel', REFERENCE_CLASS, 'LogicalTunnel' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.InputNexthop.NexthopBase.LogicalTunnel', 
                [], [], 
                '''                This can be a MPLS LSP or a GRE tunnel (or others
                as defined in this document), that is represented
                by a unique identifier (e.g. name).
                ''',
                'logical_tunnel',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('rib-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                A nexthop pointing to a RIB indicates that the
                route lookup needs to continue in the specified
                rib. This is a way to perform chained lookups.
                ''',
                'rib_name',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('nexthop-ref', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A nexthop reference that points to a nexthop.
                ''',
                'nexthop_ref',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'nexthop-base',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.InputNexthop.NexthopChain.NexthopList' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.InputNexthop.NexthopChain.NexthopList',
            False, 
            [
            _MetaInfoClassMember('nexthop-member-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A nexthop identifier that points
                to a nexthop list member.
                A nexthop list member is a nexthop.
                ''',
                'nexthop_member_id',
                'ietf-i2rs-rib', True),
            ],
            'ietf-i2rs-rib',
            'nexthop-list',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.InputNexthop.NexthopChain' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.InputNexthop.NexthopChain',
            False, 
            [
            _MetaInfoClassMember('nexthop-list', REFERENCE_LIST, 'NexthopList' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.InputNexthop.NexthopChain.NexthopList', 
                [], [], 
                '''                A list of nexthops.
                ''',
                'nexthop_list',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'nexthop-chain',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.InputNexthop.NexthopReplicates.NexthopList' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.InputNexthop.NexthopReplicates.NexthopList',
            False, 
            [
            _MetaInfoClassMember('nexthop-member-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A nexthop identifier that points
                to a nexthop list member.
                A nexthop list member is a nexthop.
                ''',
                'nexthop_member_id',
                'ietf-i2rs-rib', True),
            ],
            'ietf-i2rs-rib',
            'nexthop-list',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.InputNexthop.NexthopReplicates' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.InputNexthop.NexthopReplicates',
            False, 
            [
            _MetaInfoClassMember('nexthop-list', REFERENCE_LIST, 'NexthopList' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.InputNexthop.NexthopReplicates.NexthopList', 
                [], [], 
                '''                A list of nexthops.
                ''',
                'nexthop_list',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'nexthop-replicates',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.InputNexthop.NexthopProtection.NexthopList' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.InputNexthop.NexthopProtection.NexthopList',
            False, 
            [
            _MetaInfoClassMember('nexthop-member-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A nexthop identifier that points
                to a nexthop list member.
                A nexthop list member is a nexthop.
                ''',
                'nexthop_member_id',
                'ietf-i2rs-rib', True),
            _MetaInfoClassMember('nexthop-preference', ATTRIBUTE, 'int' , None, None, 
                [('1', '99')], [], 
                '''                Nexthop-preference is used for protection schemes.
                It is an integer value between 1 and 99.  Lower
                values are more preferred. To download a
                primary/standby/tertiary group to the FIB, the
                nexthops that are resolved and are most preferred
                are selected.
                ''',
                'nexthop_preference',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'nexthop-list',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.InputNexthop.NexthopProtection' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.InputNexthop.NexthopProtection',
            False, 
            [
            _MetaInfoClassMember('nexthop-list', REFERENCE_LIST, 'NexthopList' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.InputNexthop.NexthopProtection.NexthopList', 
                [], [], 
                '''                A list of nexthop.
                ''',
                'nexthop_list',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'nexthop-protection',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.InputNexthop.NexthopLb.NexthopList' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.InputNexthop.NexthopLb.NexthopList',
            False, 
            [
            _MetaInfoClassMember('nexthop-member-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A nexthop identifier that points
                to a nexthop list member.
                A nexthop list member is a nexthop.
                ''',
                'nexthop_member_id',
                'ietf-i2rs-rib', True),
            _MetaInfoClassMember('nexthop-lb-weight', ATTRIBUTE, 'int' , None, None, 
                [('1', '99')], [], 
                '''                The weight of a nexthop of
                the load balance nexthops.
                ''',
                'nexthop_lb_weight',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'nexthop-list',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.InputNexthop.NexthopLb' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.InputNexthop.NexthopLb',
            False, 
            [
            _MetaInfoClassMember('nexthop-list', REFERENCE_LIST, 'NexthopList' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.InputNexthop.NexthopLb.NexthopList', 
                [], [], 
                '''                A list of nexthop.
                ''',
                'nexthop_list',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'nexthop-lb',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.InputNexthop' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.InputNexthop',
            False, 
            [
            _MetaInfoClassMember('nexthop-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                An identifier that refers to a nexthop.
                ''',
                'nexthop_id',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('sharing-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                To indicate whether a nexthop is sharable
                or non-sharable.
                true - sharable, means the nexthop can be shared
                       with other routes
                false - non-sharable, means the nexthop can not
                       be shared with other routes.
                ''',
                'sharing_flag',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('nexthop-base', REFERENCE_CLASS, 'NexthopBase' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.InputNexthop.NexthopBase', 
                [], [], 
                '''                The base nexthop.
                ''',
                'nexthop_base',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('nexthop-chain', REFERENCE_CLASS, 'NexthopChain' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.InputNexthop.NexthopChain', 
                [], [], 
                '''                A chain nexthop.
                ''',
                'nexthop_chain',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('nexthop-replicates', REFERENCE_CLASS, 'NexthopReplicates' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.InputNexthop.NexthopReplicates', 
                [], [], 
                '''                A replicates nexthop.
                ''',
                'nexthop_replicates',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('nexthop-protection', REFERENCE_CLASS, 'NexthopProtection' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.InputNexthop.NexthopProtection', 
                [], [], 
                '''                A protection nexthop.
                ''',
                'nexthop_protection',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('nexthop-lb', REFERENCE_CLASS, 'NexthopLb' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.InputNexthop.NexthopLb', 
                [], [], 
                '''                A load balance nexthop.
                ''',
                'nexthop_lb',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'input-nexthop',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopBase.EgressInterfaceIpv4Address' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopBase.EgressInterfaceIpv4Address',
            False, 
            [
            _MetaInfoClassMember('outgoing-interface', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the outgoing interface.
                ''',
                'outgoing_interface',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The nexthop points to an interface with
                an IPv4 address.
                ''',
                'ipv4_address',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'egress-interface-ipv4-address',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopBase.EgressInterfaceIpv6Address' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopBase.EgressInterfaceIpv6Address',
            False, 
            [
            _MetaInfoClassMember('outgoing-interface', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the outgoing interface.
                ''',
                'outgoing_interface',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                The nexthop points to an interface with
                an IPv6 address.
                ''',
                'ipv6_address',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'egress-interface-ipv6-address',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopBase.EgressInterfaceMacAddress' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopBase.EgressInterfaceMacAddress',
            False, 
            [
            _MetaInfoClassMember('outgoing-interface', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the outgoing interface.
                ''',
                'outgoing_interface',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ieee-mac-address', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The nexthop points to an interface with
                a specific mac-address.
                ''',
                'ieee_mac_address',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'egress-interface-mac-address',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopBase.TunnelEncap.Ipv4Header' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopBase.TunnelEncap.Ipv4Header',
            False, 
            [
            _MetaInfoClassMember('src-ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The source IP address of the header.
                ''',
                'src_ipv4_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('dest-ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The destination IP address of the header.
                ''',
                'dest_ipv4_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('protocol', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The protocol id of the header.
                ''',
                'protocol',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ttl', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The TTL of the header.
                ''',
                'ttl',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('dscp', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The DSCP field of the header.
                ''',
                'dscp',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'ipv4-header',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopBase.TunnelEncap.Ipv6Header' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopBase.TunnelEncap.Ipv6Header',
            False, 
            [
            _MetaInfoClassMember('src-ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                The source IP address of the header.
                ''',
                'src_ipv6_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('dest-ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                The destination IP address of the header.
                ''',
                'dest_ipv6_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('next-header', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The next header of the IPv6 header.
                ''',
                'next_header',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('traffic-class', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The traffic class value of the header.
                ''',
                'traffic_class',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('flow-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The flow label of the header.
                ''',
                'flow_label',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('hop-limit', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The hop limit the header.
                ''',
                'hop_limit',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'ipv6-header',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopBase.TunnelEncap.MplsHeader.LabelOperations.LabelPush' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopBase.TunnelEncap.MplsHeader.LabelOperations.LabelPush',
            False, 
            [
            _MetaInfoClassMember('label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The label to be pushed.
                ''',
                'label',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('s-bit', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                The s-bit of the label to be pushed. 
                ''',
                's_bit',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('tc-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The traffic class value of the label to be pushed.
                ''',
                'tc_value',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ttl-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The TTL value of the label to be pushed.
                ''',
                'ttl_value',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'label-push',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopBase.TunnelEncap.MplsHeader.LabelOperations.LabelSwap' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopBase.TunnelEncap.MplsHeader.LabelOperations.LabelSwap',
            False, 
            [
            _MetaInfoClassMember('in-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The label to be swapped.
                ''',
                'in_label',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('out-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The out MPLS label.
                ''',
                'out_label',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ttl-action', REFERENCE_IDENTITY_CLASS, 'TtlActionIdentity' , 'ydk.models.ietf.ietf_i2rs_rib', 'TtlActionIdentity', 
                [], [], 
                '''                The label ttl actions:
                - No-action, or
                - Copy to inner label,or
                - Decrease (the in label) by 1 and
                  copy to the out label.
                ''',
                'ttl_action',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'label-swap',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopBase.TunnelEncap.MplsHeader.LabelOperations' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopBase.TunnelEncap.MplsHeader.LabelOperations',
            False, 
            [
            _MetaInfoClassMember('label-oper-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                An optional identifier that points
                to a label operation.
                ''',
                'label_oper_id',
                'ietf-i2rs-rib', True),
            _MetaInfoClassMember('label-push', REFERENCE_CLASS, 'LabelPush' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopBase.TunnelEncap.MplsHeader.LabelOperations.LabelPush', 
                [], [], 
                '''                Label push operation.
                ''',
                'label_push',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('label-swap', REFERENCE_CLASS, 'LabelSwap' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopBase.TunnelEncap.MplsHeader.LabelOperations.LabelSwap', 
                [], [], 
                '''                Label swap operation.
                ''',
                'label_swap',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'label-operations',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopBase.TunnelEncap.MplsHeader' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopBase.TunnelEncap.MplsHeader',
            False, 
            [
            _MetaInfoClassMember('label-operations', REFERENCE_LIST, 'LabelOperations' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopBase.TunnelEncap.MplsHeader.LabelOperations', 
                [], [], 
                '''                Label operations.
                ''',
                'label_operations',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'mpls-header',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopBase.TunnelEncap.GreHeader' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopBase.TunnelEncap.GreHeader',
            False, 
            [
            _MetaInfoClassMember('ipv4-dest', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The destination IP address of the GRE header.
                ''',
                'ipv4_dest',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ipv6-dest', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                The destination IP address of the GRE header.
                ''',
                'ipv6_dest',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('protocol-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The protocol type of the GRE header.
                ''',
                'protocol_type',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('key', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The GRE key of the GRE header.
                ''',
                'key',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'gre-header',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopBase.TunnelEncap.NvgreHeader' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopBase.TunnelEncap.NvgreHeader',
            False, 
            [
            _MetaInfoClassMember('src-ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The source IP address of the header.
                ''',
                'src_ipv4_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('dest-ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The destination IP address of the header.
                ''',
                'dest_ipv4_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('protocol', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The protocol id of the header.
                ''',
                'protocol',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ttl', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The TTL of the header.
                ''',
                'ttl',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('dscp', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The DSCP field of the header.
                ''',
                'dscp',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('src-ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                The source IP address of the header.
                ''',
                'src_ipv6_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('dest-ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                The destination IP address of the header.
                ''',
                'dest_ipv6_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('next-header', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The next header of the IPv6 header.
                ''',
                'next_header',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('traffic-class', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The traffic class value of the header.
                ''',
                'traffic_class',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('flow-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The flow label of the header.
                ''',
                'flow_label',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('hop-limit', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The hop limit the header.
                ''',
                'hop_limit',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('virtual-subnet-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The subnet identifier of the NvGRE header.
                ''',
                'virtual_subnet_id',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('flow-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The flow identifier of the NvGRE header.
                ''',
                'flow_id',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'nvgre-header',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopBase.TunnelEncap.VxlanHeader' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopBase.TunnelEncap.VxlanHeader',
            False, 
            [
            _MetaInfoClassMember('src-ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The source IP address of the header.
                ''',
                'src_ipv4_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('dest-ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The destination IP address of the header.
                ''',
                'dest_ipv4_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('protocol', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The protocol id of the header.
                ''',
                'protocol',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ttl', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The TTL of the header.
                ''',
                'ttl',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('dscp', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The DSCP field of the header.
                ''',
                'dscp',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('src-ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                The source IP address of the header.
                ''',
                'src_ipv6_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('dest-ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                The destination IP address of the header.
                ''',
                'dest_ipv6_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('next-header', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The next header of the IPv6 header.
                ''',
                'next_header',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('traffic-class', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The traffic class value of the header.
                ''',
                'traffic_class',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('flow-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The flow label of the header.
                ''',
                'flow_label',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('hop-limit', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The hop limit the header.
                ''',
                'hop_limit',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('vxlan-identifier', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The VxLAN identifier of the VxLAN header.
                ''',
                'vxlan_identifier',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'vxlan-header',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopBase.TunnelEncap' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopBase.TunnelEncap',
            False, 
            [
            _MetaInfoClassMember('ipv4-header', REFERENCE_CLASS, 'Ipv4Header' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopBase.TunnelEncap.Ipv4Header', 
                [], [], 
                '''                IPv4 header.
                ''',
                'ipv4_header',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ipv6-header', REFERENCE_CLASS, 'Ipv6Header' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopBase.TunnelEncap.Ipv6Header', 
                [], [], 
                '''                IPv6 header.
                ''',
                'ipv6_header',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('mpls-header', REFERENCE_CLASS, 'MplsHeader' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopBase.TunnelEncap.MplsHeader', 
                [], [], 
                '''                MPLS header.
                ''',
                'mpls_header',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('gre-header', REFERENCE_CLASS, 'GreHeader' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopBase.TunnelEncap.GreHeader', 
                [], [], 
                '''                GRE header.
                ''',
                'gre_header',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('nvgre-header', REFERENCE_CLASS, 'NvgreHeader' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopBase.TunnelEncap.NvgreHeader', 
                [], [], 
                '''                NvGRE header.
                ''',
                'nvgre_header',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('vxlan-header', REFERENCE_CLASS, 'VxlanHeader' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopBase.TunnelEncap.VxlanHeader', 
                [], [], 
                '''                VxLAN header.
                ''',
                'vxlan_header',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'tunnel-encap',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopBase.TunnelDecap.Ipv4Decap' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopBase.TunnelDecap.Ipv4Decap',
            False, 
            [
            _MetaInfoClassMember('ipv4-decap', REFERENCE_IDENTITY_CLASS, 'TunnelDecapActionIdentity' , 'ydk.models.ietf.ietf_i2rs_rib', 'TunnelDecapActionIdentity', 
                [], [], 
                '''                IPv4 decap operations.
                ''',
                'ipv4_decap',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ttl-action', REFERENCE_IDENTITY_CLASS, 'TtlActionIdentity' , 'ydk.models.ietf.ietf_i2rs_rib', 'TtlActionIdentity', 
                [], [], 
                '''                The ttl actions:
                no-action or copy to inner header.
                ''',
                'ttl_action',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'ipv4-decap',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopBase.TunnelDecap.Ipv6Decap' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopBase.TunnelDecap.Ipv6Decap',
            False, 
            [
            _MetaInfoClassMember('ipv6-decap', REFERENCE_IDENTITY_CLASS, 'TunnelDecapActionIdentity' , 'ydk.models.ietf.ietf_i2rs_rib', 'TunnelDecapActionIdentity', 
                [], [], 
                '''                IPv6 decap operations.
                ''',
                'ipv6_decap',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('hop-limit-action', REFERENCE_IDENTITY_CLASS, 'HopLimitActionIdentity' , 'ydk.models.ietf.ietf_i2rs_rib', 'HopLimitActionIdentity', 
                [], [], 
                '''                The hop limit actions:
                no-action or copy to inner header.
                ''',
                'hop_limit_action',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'ipv6-decap',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopBase.TunnelDecap.LabelPop' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopBase.TunnelDecap.LabelPop',
            False, 
            [
            _MetaInfoClassMember('label-pop', REFERENCE_IDENTITY_CLASS, 'MplsLabelActionIdentity' , 'ydk.models.ietf.ietf_i2rs_rib', 'MplsLabelActionIdentity', 
                [], [], 
                '''                Pop a label from the label stack.
                ''',
                'label_pop',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ttl-action', REFERENCE_IDENTITY_CLASS, 'TtlActionIdentity' , 'ydk.models.ietf.ietf_i2rs_rib', 'TtlActionIdentity', 
                [], [], 
                '''                The label ttl action.
                ''',
                'ttl_action',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'label-pop',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopBase.TunnelDecap' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopBase.TunnelDecap',
            False, 
            [
            _MetaInfoClassMember('ipv4-decap', REFERENCE_CLASS, 'Ipv4Decap' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopBase.TunnelDecap.Ipv4Decap', 
                [], [], 
                '''                IPv4 decap.
                ''',
                'ipv4_decap',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ipv6-decap', REFERENCE_CLASS, 'Ipv6Decap' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopBase.TunnelDecap.Ipv6Decap', 
                [], [], 
                '''                IPv6 decap.
                ''',
                'ipv6_decap',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('label-pop', REFERENCE_CLASS, 'LabelPop' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopBase.TunnelDecap.LabelPop', 
                [], [], 
                '''                MPLS decap.
                ''',
                'label_pop',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'tunnel-decap',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopBase.LogicalTunnel' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopBase.LogicalTunnel',
            False, 
            [
            _MetaInfoClassMember('tunnel-type', REFERENCE_IDENTITY_CLASS, 'TunnelTypeIdentity' , 'ydk.models.ietf.ietf_i2rs_rib', 'TunnelTypeIdentity', 
                [], [], 
                '''                A tunnel type.
                ''',
                'tunnel_type',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('tunnel-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                A tunnel name that points to a logical tunnel.
                ''',
                'tunnel_name',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'logical-tunnel',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopBase' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopBase',
            False, 
            [
            _MetaInfoClassMember('special', REFERENCE_IDENTITY_CLASS, 'SpecialNexthopIdentity' , 'ydk.models.ietf.ietf_i2rs_rib', 'SpecialNexthopIdentity', 
                [], [], 
                '''                A special nexthop.
                ''',
                'special',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('outgoing-interface', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The nexthop is an outgoing interface.
                ''',
                'outgoing_interface',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The nexthop is an IPv4 address.
                ''',
                'ipv4_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                The nexthop is an IPv6 address.
                ''',
                'ipv6_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('egress-interface-ipv4-address', REFERENCE_CLASS, 'EgressInterfaceIpv4Address' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopBase.EgressInterfaceIpv4Address', 
                [], [], 
                '''                The nexthop is an egress-interface and an IP
                address. This can be used in cases e.g. where
                the IP address is a link-local address.
                ''',
                'egress_interface_ipv4_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('egress-interface-ipv6-address', REFERENCE_CLASS, 'EgressInterfaceIpv6Address' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopBase.EgressInterfaceIpv6Address', 
                [], [], 
                '''                The nexthop is an egress-interface and an IP
                address. This can be used in cases e.g. where
                the IP address is a link-local address.
                ''',
                'egress_interface_ipv6_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('egress-interface-mac-address', REFERENCE_CLASS, 'EgressInterfaceMacAddress' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopBase.EgressInterfaceMacAddress', 
                [], [], 
                '''                The egress interface must be an Ethernet
                interface. Address resolution is not required
                for this nexthop.
                ''',
                'egress_interface_mac_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('tunnel-encap', REFERENCE_CLASS, 'TunnelEncap' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopBase.TunnelEncap', 
                [], [], 
                '''                This can be an encap representing an IP tunnel or
                MPLS tunnel or others as defined in info model.
                An optional egress interface can be chained to the
                tunnel encap to indicate which interface to send
                the packet out on.  The egress interface is useful
                when the network device contains Ethernet interfaces
                and one needs to perform address resolution for the
                IP packet.
                ''',
                'tunnel_encap',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('tunnel-decap', REFERENCE_CLASS, 'TunnelDecap' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopBase.TunnelDecap', 
                [], [], 
                '''                This is to specify decapsulating a tunnel header.
                ''',
                'tunnel_decap',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('logical-tunnel', REFERENCE_CLASS, 'LogicalTunnel' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopBase.LogicalTunnel', 
                [], [], 
                '''                This can be a MPLS LSP or a GRE tunnel (or others
                as defined in this document), that is represented
                by a unique identifier (e.g. name).
                ''',
                'logical_tunnel',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('rib-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                A nexthop pointing to a RIB indicates that the
                route lookup needs to continue in the specified
                rib. This is a way to perform chained lookups.
                ''',
                'rib_name',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('nexthop-ref', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A nexthop reference that points to a nexthop.
                ''',
                'nexthop_ref',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'nexthop-base',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopChain.NexthopList' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopChain.NexthopList',
            False, 
            [
            _MetaInfoClassMember('nexthop-member-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A nexthop identifier that points
                to a nexthop list member.
                A nexthop list member is a nexthop.
                ''',
                'nexthop_member_id',
                'ietf-i2rs-rib', True),
            ],
            'ietf-i2rs-rib',
            'nexthop-list',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopChain' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopChain',
            False, 
            [
            _MetaInfoClassMember('nexthop-list', REFERENCE_LIST, 'NexthopList' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopChain.NexthopList', 
                [], [], 
                '''                A list of nexthops.
                ''',
                'nexthop_list',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'nexthop-chain',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopReplicates.NexthopList' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopReplicates.NexthopList',
            False, 
            [
            _MetaInfoClassMember('nexthop-member-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A nexthop identifier that points
                to a nexthop list member.
                A nexthop list member is a nexthop.
                ''',
                'nexthop_member_id',
                'ietf-i2rs-rib', True),
            ],
            'ietf-i2rs-rib',
            'nexthop-list',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopReplicates' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopReplicates',
            False, 
            [
            _MetaInfoClassMember('nexthop-list', REFERENCE_LIST, 'NexthopList' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopReplicates.NexthopList', 
                [], [], 
                '''                A list of nexthops.
                ''',
                'nexthop_list',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'nexthop-replicates',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopProtection.NexthopList' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopProtection.NexthopList',
            False, 
            [
            _MetaInfoClassMember('nexthop-member-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A nexthop identifier that points
                to a nexthop list member.
                A nexthop list member is a nexthop.
                ''',
                'nexthop_member_id',
                'ietf-i2rs-rib', True),
            _MetaInfoClassMember('nexthop-preference', ATTRIBUTE, 'int' , None, None, 
                [('1', '99')], [], 
                '''                Nexthop-preference is used for protection schemes.
                It is an integer value between 1 and 99.  Lower
                values are more preferred. To download a
                primary/standby/tertiary group to the FIB, the
                nexthops that are resolved and are most preferred
                are selected.
                ''',
                'nexthop_preference',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'nexthop-list',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopProtection' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopProtection',
            False, 
            [
            _MetaInfoClassMember('nexthop-list', REFERENCE_LIST, 'NexthopList' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopProtection.NexthopList', 
                [], [], 
                '''                A list of nexthop.
                ''',
                'nexthop_list',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'nexthop-protection',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopLb.NexthopList' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopLb.NexthopList',
            False, 
            [
            _MetaInfoClassMember('nexthop-member-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A nexthop identifier that points
                to a nexthop list member.
                A nexthop list member is a nexthop.
                ''',
                'nexthop_member_id',
                'ietf-i2rs-rib', True),
            _MetaInfoClassMember('nexthop-lb-weight', ATTRIBUTE, 'int' , None, None, 
                [('1', '99')], [], 
                '''                The weight of a nexthop of
                the load balance nexthops.
                ''',
                'nexthop_lb_weight',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'nexthop-list',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopLb' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopLb',
            False, 
            [
            _MetaInfoClassMember('nexthop-list', REFERENCE_LIST, 'NexthopList' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopLb.NexthopList', 
                [], [], 
                '''                A list of nexthop.
                ''',
                'nexthop_list',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'nexthop-lb',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop',
            False, 
            [
            _MetaInfoClassMember('nexthop-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                An identifier that refers to a nexthop.
                ''',
                'nexthop_id',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('sharing-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                To indicate whether a nexthop is sharable
                or non-sharable.
                true - sharable, means the nexthop can be shared
                       with other routes
                false - non-sharable, means the nexthop can not
                       be shared with other routes.
                ''',
                'sharing_flag',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('nexthop-base', REFERENCE_CLASS, 'NexthopBase' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopBase', 
                [], [], 
                '''                The base nexthop.
                ''',
                'nexthop_base',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('nexthop-chain', REFERENCE_CLASS, 'NexthopChain' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopChain', 
                [], [], 
                '''                A chain nexthop.
                ''',
                'nexthop_chain',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('nexthop-replicates', REFERENCE_CLASS, 'NexthopReplicates' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopReplicates', 
                [], [], 
                '''                A replicates nexthop.
                ''',
                'nexthop_replicates',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('nexthop-protection', REFERENCE_CLASS, 'NexthopProtection' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopProtection', 
                [], [], 
                '''                A protection nexthop.
                ''',
                'nexthop_protection',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('nexthop-lb', REFERENCE_CLASS, 'NexthopLb' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopLb', 
                [], [], 
                '''                A load balance nexthop.
                ''',
                'nexthop_lb',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'updated-nexthop',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedRouteAttr.AddressFamilyRouteAttributes' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedRouteAttr.AddressFamilyRouteAttributes',
            False, 
            [
            ],
            'ietf-i2rs-rib',
            'address-family-route-attributes',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedRouteAttr' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedRouteAttr',
            False, 
            [
            _MetaInfoClassMember('route-preference', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ROUTE_PREFERENCE: This is a numerical value that
                allows for comparing routes from different
                protocols.  Static configuration is also
                considered a protocol for the purpose of this
                field.  It is also known as administrative-distance.
                The lower the value, the higher the preference.
                ''',
                'route_preference',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('local-only', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicate whether the attributes is local only.
                ''',
                'local_only',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('address-family-route-attributes', REFERENCE_CLASS, 'AddressFamilyRouteAttributes' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedRouteAttr.AddressFamilyRouteAttributes', 
                [], [], 
                '''                Address family related route attributes.
                ''',
                'address_family_route_attributes',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'updated-route-attr',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedRouteVendorAttr' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedRouteVendorAttr',
            False, 
            [
            ],
            'ietf-i2rs-rib',
            'updated-route-vendor-attr',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input.UpdateParametersNexthop' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input.UpdateParametersNexthop',
            False, 
            [
            _MetaInfoClassMember('updated-nexthop', REFERENCE_CLASS, 'UpdatedNexthop' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop', 
                [], [], 
                '''                The nexthop used for updating.
                ''',
                'updated_nexthop',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('updated-route-attr', REFERENCE_CLASS, 'UpdatedRouteAttr' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedRouteAttr', 
                [], [], 
                '''                The route attributes used for updating.
                ''',
                'updated_route_attr',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('updated-route-vendor-attr', REFERENCE_CLASS, 'UpdatedRouteVendorAttr' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedRouteVendorAttr', 
                [], [], 
                '''                The vendor route attributes used for updating.
                ''',
                'updated_route_vendor_attr',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'update-parameters-nexthop',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Input' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Input',
            False, 
            [
            _MetaInfoClassMember('return-failure-detail', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Whether return the failure detail.
                true  - return the failure detail;
                false - do not return the failure detail;
                the default is false.
                ''',
                'return_failure_detail',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('rib-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                A reference to the name of a rib.
                ''',
                'rib_name',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('input-routes', REFERENCE_CLASS, 'InputRoutes' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.InputRoutes', 
                [], [], 
                '''                The matched routes to be updated.
                ''',
                'input_routes',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('input-route-attributes', REFERENCE_CLASS, 'InputRouteAttributes' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.InputRouteAttributes', 
                [], [], 
                '''                The route attributes are used for matching.
                ''',
                'input_route_attributes',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('update-parametors', REFERENCE_CLASS, 'UpdateParametors' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.UpdateParametors', 
                [], [], 
                '''                Update options:
                1. update the nexthop
                2. update the route attributes
                3. update the route-vendor-attributes.
                ''',
                'update_parametors',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('input-route-vendor-attributes', REFERENCE_CLASS, 'InputRouteVendorAttributes' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.InputRouteVendorAttributes', 
                [], [], 
                '''                The vendor route attributes are used for matching.
                ''',
                'input_route_vendor_attributes',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('update-parameters-vendor', REFERENCE_CLASS, 'UpdateParametersVendor' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.UpdateParametersVendor', 
                [], [], 
                '''                Update options:
                1. update the nexthop
                2. update the route attributes
                3. update the route-vendor-attributes.
                ''',
                'update_parameters_vendor',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('input-nexthop', REFERENCE_CLASS, 'InputNexthop' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.InputNexthop', 
                [], [], 
                '''                The nexthop used for matching.
                ''',
                'input_nexthop',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('update-parameters-nexthop', REFERENCE_CLASS, 'UpdateParametersNexthop' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input.UpdateParametersNexthop', 
                [], [], 
                '''                Update options:
                1. update the nexthop
                2. update the route attributes
                3. update the route-vendor-attributes.
                ''',
                'update_parameters_nexthop',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'input',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Output.FailureDetail.FailedRoutes' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Output.FailureDetail.FailedRoutes',
            False, 
            [
            _MetaInfoClassMember('route-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The route index of the failed route.
                ''',
                'route_index',
                'ietf-i2rs-rib', True),
            _MetaInfoClassMember('error-code', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The error code that reflects the failure reason.
                ''',
                'error_code',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'failed-routes',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Output.FailureDetail' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Output.FailureDetail',
            False, 
            [
            _MetaInfoClassMember('failed-routes', REFERENCE_LIST, 'FailedRoutes' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Output.FailureDetail.FailedRoutes', 
                [], [], 
                '''                The list of failed routes.
                ''',
                'failed_routes',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'failure-detail',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc.Output' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc.Output',
            False, 
            [
            _MetaInfoClassMember('success-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The numbers of routes that are successfully
                added/deleted/updated.
                ''',
                'success_count',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('failed-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The numbers of the routes that are failed
                to be added/deleted/updated.
                ''',
                'failed_count',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('failure-detail', REFERENCE_CLASS, 'FailureDetail' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Output.FailureDetail', 
                [], [], 
                '''                The failure detail reflects the reason why a route
                operation fails. It is a array that includes the route
                index and error code of the failed route.
                ''',
                'failure_detail',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'output',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'RouteUpdateRpc' : {
        'meta_info' : _MetaInfoClass('RouteUpdateRpc',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Input', 
                [], [], 
                '''                ''',
                'input',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('output', REFERENCE_CLASS, 'Output' , 'ydk.models.ietf.ietf_i2rs_rib', 'RouteUpdateRpc.Output', 
                [], [], 
                '''                ''',
                'output',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'route-update',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'NhAddRpc.Input.NexthopBase.EgressInterfaceIpv4Address' : {
        'meta_info' : _MetaInfoClass('NhAddRpc.Input.NexthopBase.EgressInterfaceIpv4Address',
            False, 
            [
            _MetaInfoClassMember('outgoing-interface', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the outgoing interface.
                ''',
                'outgoing_interface',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The nexthop points to an interface with
                an IPv4 address.
                ''',
                'ipv4_address',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'egress-interface-ipv4-address',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'NhAddRpc.Input.NexthopBase.EgressInterfaceIpv6Address' : {
        'meta_info' : _MetaInfoClass('NhAddRpc.Input.NexthopBase.EgressInterfaceIpv6Address',
            False, 
            [
            _MetaInfoClassMember('outgoing-interface', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the outgoing interface.
                ''',
                'outgoing_interface',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                The nexthop points to an interface with
                an IPv6 address.
                ''',
                'ipv6_address',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'egress-interface-ipv6-address',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'NhAddRpc.Input.NexthopBase.EgressInterfaceMacAddress' : {
        'meta_info' : _MetaInfoClass('NhAddRpc.Input.NexthopBase.EgressInterfaceMacAddress',
            False, 
            [
            _MetaInfoClassMember('outgoing-interface', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the outgoing interface.
                ''',
                'outgoing_interface',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ieee-mac-address', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The nexthop points to an interface with
                a specific mac-address.
                ''',
                'ieee_mac_address',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'egress-interface-mac-address',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'NhAddRpc.Input.NexthopBase.TunnelEncap.Ipv4Header' : {
        'meta_info' : _MetaInfoClass('NhAddRpc.Input.NexthopBase.TunnelEncap.Ipv4Header',
            False, 
            [
            _MetaInfoClassMember('src-ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The source IP address of the header.
                ''',
                'src_ipv4_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('dest-ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The destination IP address of the header.
                ''',
                'dest_ipv4_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('protocol', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The protocol id of the header.
                ''',
                'protocol',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ttl', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The TTL of the header.
                ''',
                'ttl',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('dscp', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The DSCP field of the header.
                ''',
                'dscp',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'ipv4-header',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'NhAddRpc.Input.NexthopBase.TunnelEncap.Ipv6Header' : {
        'meta_info' : _MetaInfoClass('NhAddRpc.Input.NexthopBase.TunnelEncap.Ipv6Header',
            False, 
            [
            _MetaInfoClassMember('src-ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                The source IP address of the header.
                ''',
                'src_ipv6_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('dest-ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                The destination IP address of the header.
                ''',
                'dest_ipv6_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('next-header', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The next header of the IPv6 header.
                ''',
                'next_header',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('traffic-class', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The traffic class value of the header.
                ''',
                'traffic_class',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('flow-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The flow label of the header.
                ''',
                'flow_label',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('hop-limit', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The hop limit the header.
                ''',
                'hop_limit',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'ipv6-header',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'NhAddRpc.Input.NexthopBase.TunnelEncap.MplsHeader.LabelOperations.LabelPush' : {
        'meta_info' : _MetaInfoClass('NhAddRpc.Input.NexthopBase.TunnelEncap.MplsHeader.LabelOperations.LabelPush',
            False, 
            [
            _MetaInfoClassMember('label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The label to be pushed.
                ''',
                'label',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('s-bit', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                The s-bit of the label to be pushed. 
                ''',
                's_bit',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('tc-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The traffic class value of the label to be pushed.
                ''',
                'tc_value',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ttl-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The TTL value of the label to be pushed.
                ''',
                'ttl_value',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'label-push',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'NhAddRpc.Input.NexthopBase.TunnelEncap.MplsHeader.LabelOperations.LabelSwap' : {
        'meta_info' : _MetaInfoClass('NhAddRpc.Input.NexthopBase.TunnelEncap.MplsHeader.LabelOperations.LabelSwap',
            False, 
            [
            _MetaInfoClassMember('in-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The label to be swapped.
                ''',
                'in_label',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('out-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The out MPLS label.
                ''',
                'out_label',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ttl-action', REFERENCE_IDENTITY_CLASS, 'TtlActionIdentity' , 'ydk.models.ietf.ietf_i2rs_rib', 'TtlActionIdentity', 
                [], [], 
                '''                The label ttl actions:
                - No-action, or
                - Copy to inner label,or
                - Decrease (the in label) by 1 and
                  copy to the out label.
                ''',
                'ttl_action',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'label-swap',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'NhAddRpc.Input.NexthopBase.TunnelEncap.MplsHeader.LabelOperations' : {
        'meta_info' : _MetaInfoClass('NhAddRpc.Input.NexthopBase.TunnelEncap.MplsHeader.LabelOperations',
            False, 
            [
            _MetaInfoClassMember('label-oper-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                An optional identifier that points
                to a label operation.
                ''',
                'label_oper_id',
                'ietf-i2rs-rib', True),
            _MetaInfoClassMember('label-push', REFERENCE_CLASS, 'LabelPush' , 'ydk.models.ietf.ietf_i2rs_rib', 'NhAddRpc.Input.NexthopBase.TunnelEncap.MplsHeader.LabelOperations.LabelPush', 
                [], [], 
                '''                Label push operation.
                ''',
                'label_push',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('label-swap', REFERENCE_CLASS, 'LabelSwap' , 'ydk.models.ietf.ietf_i2rs_rib', 'NhAddRpc.Input.NexthopBase.TunnelEncap.MplsHeader.LabelOperations.LabelSwap', 
                [], [], 
                '''                Label swap operation.
                ''',
                'label_swap',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'label-operations',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'NhAddRpc.Input.NexthopBase.TunnelEncap.MplsHeader' : {
        'meta_info' : _MetaInfoClass('NhAddRpc.Input.NexthopBase.TunnelEncap.MplsHeader',
            False, 
            [
            _MetaInfoClassMember('label-operations', REFERENCE_LIST, 'LabelOperations' , 'ydk.models.ietf.ietf_i2rs_rib', 'NhAddRpc.Input.NexthopBase.TunnelEncap.MplsHeader.LabelOperations', 
                [], [], 
                '''                Label operations.
                ''',
                'label_operations',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'mpls-header',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'NhAddRpc.Input.NexthopBase.TunnelEncap.GreHeader' : {
        'meta_info' : _MetaInfoClass('NhAddRpc.Input.NexthopBase.TunnelEncap.GreHeader',
            False, 
            [
            _MetaInfoClassMember('ipv4-dest', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The destination IP address of the GRE header.
                ''',
                'ipv4_dest',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ipv6-dest', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                The destination IP address of the GRE header.
                ''',
                'ipv6_dest',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('protocol-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The protocol type of the GRE header.
                ''',
                'protocol_type',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('key', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The GRE key of the GRE header.
                ''',
                'key',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'gre-header',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'NhAddRpc.Input.NexthopBase.TunnelEncap.NvgreHeader' : {
        'meta_info' : _MetaInfoClass('NhAddRpc.Input.NexthopBase.TunnelEncap.NvgreHeader',
            False, 
            [
            _MetaInfoClassMember('src-ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The source IP address of the header.
                ''',
                'src_ipv4_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('dest-ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The destination IP address of the header.
                ''',
                'dest_ipv4_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('protocol', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The protocol id of the header.
                ''',
                'protocol',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ttl', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The TTL of the header.
                ''',
                'ttl',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('dscp', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The DSCP field of the header.
                ''',
                'dscp',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('src-ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                The source IP address of the header.
                ''',
                'src_ipv6_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('dest-ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                The destination IP address of the header.
                ''',
                'dest_ipv6_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('next-header', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The next header of the IPv6 header.
                ''',
                'next_header',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('traffic-class', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The traffic class value of the header.
                ''',
                'traffic_class',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('flow-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The flow label of the header.
                ''',
                'flow_label',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('hop-limit', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The hop limit the header.
                ''',
                'hop_limit',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('virtual-subnet-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The subnet identifier of the NvGRE header.
                ''',
                'virtual_subnet_id',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('flow-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The flow identifier of the NvGRE header.
                ''',
                'flow_id',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'nvgre-header',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'NhAddRpc.Input.NexthopBase.TunnelEncap.VxlanHeader' : {
        'meta_info' : _MetaInfoClass('NhAddRpc.Input.NexthopBase.TunnelEncap.VxlanHeader',
            False, 
            [
            _MetaInfoClassMember('src-ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The source IP address of the header.
                ''',
                'src_ipv4_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('dest-ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The destination IP address of the header.
                ''',
                'dest_ipv4_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('protocol', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The protocol id of the header.
                ''',
                'protocol',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ttl', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The TTL of the header.
                ''',
                'ttl',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('dscp', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The DSCP field of the header.
                ''',
                'dscp',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('src-ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                The source IP address of the header.
                ''',
                'src_ipv6_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('dest-ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                The destination IP address of the header.
                ''',
                'dest_ipv6_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('next-header', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The next header of the IPv6 header.
                ''',
                'next_header',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('traffic-class', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The traffic class value of the header.
                ''',
                'traffic_class',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('flow-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The flow label of the header.
                ''',
                'flow_label',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('hop-limit', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The hop limit the header.
                ''',
                'hop_limit',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('vxlan-identifier', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The VxLAN identifier of the VxLAN header.
                ''',
                'vxlan_identifier',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'vxlan-header',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'NhAddRpc.Input.NexthopBase.TunnelEncap' : {
        'meta_info' : _MetaInfoClass('NhAddRpc.Input.NexthopBase.TunnelEncap',
            False, 
            [
            _MetaInfoClassMember('ipv4-header', REFERENCE_CLASS, 'Ipv4Header' , 'ydk.models.ietf.ietf_i2rs_rib', 'NhAddRpc.Input.NexthopBase.TunnelEncap.Ipv4Header', 
                [], [], 
                '''                IPv4 header.
                ''',
                'ipv4_header',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ipv6-header', REFERENCE_CLASS, 'Ipv6Header' , 'ydk.models.ietf.ietf_i2rs_rib', 'NhAddRpc.Input.NexthopBase.TunnelEncap.Ipv6Header', 
                [], [], 
                '''                IPv6 header.
                ''',
                'ipv6_header',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('mpls-header', REFERENCE_CLASS, 'MplsHeader' , 'ydk.models.ietf.ietf_i2rs_rib', 'NhAddRpc.Input.NexthopBase.TunnelEncap.MplsHeader', 
                [], [], 
                '''                MPLS header.
                ''',
                'mpls_header',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('gre-header', REFERENCE_CLASS, 'GreHeader' , 'ydk.models.ietf.ietf_i2rs_rib', 'NhAddRpc.Input.NexthopBase.TunnelEncap.GreHeader', 
                [], [], 
                '''                GRE header.
                ''',
                'gre_header',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('nvgre-header', REFERENCE_CLASS, 'NvgreHeader' , 'ydk.models.ietf.ietf_i2rs_rib', 'NhAddRpc.Input.NexthopBase.TunnelEncap.NvgreHeader', 
                [], [], 
                '''                NvGRE header.
                ''',
                'nvgre_header',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('vxlan-header', REFERENCE_CLASS, 'VxlanHeader' , 'ydk.models.ietf.ietf_i2rs_rib', 'NhAddRpc.Input.NexthopBase.TunnelEncap.VxlanHeader', 
                [], [], 
                '''                VxLAN header.
                ''',
                'vxlan_header',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'tunnel-encap',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'NhAddRpc.Input.NexthopBase.TunnelDecap.Ipv4Decap' : {
        'meta_info' : _MetaInfoClass('NhAddRpc.Input.NexthopBase.TunnelDecap.Ipv4Decap',
            False, 
            [
            _MetaInfoClassMember('ipv4-decap', REFERENCE_IDENTITY_CLASS, 'TunnelDecapActionIdentity' , 'ydk.models.ietf.ietf_i2rs_rib', 'TunnelDecapActionIdentity', 
                [], [], 
                '''                IPv4 decap operations.
                ''',
                'ipv4_decap',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ttl-action', REFERENCE_IDENTITY_CLASS, 'TtlActionIdentity' , 'ydk.models.ietf.ietf_i2rs_rib', 'TtlActionIdentity', 
                [], [], 
                '''                The ttl actions:
                no-action or copy to inner header.
                ''',
                'ttl_action',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'ipv4-decap',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'NhAddRpc.Input.NexthopBase.TunnelDecap.Ipv6Decap' : {
        'meta_info' : _MetaInfoClass('NhAddRpc.Input.NexthopBase.TunnelDecap.Ipv6Decap',
            False, 
            [
            _MetaInfoClassMember('ipv6-decap', REFERENCE_IDENTITY_CLASS, 'TunnelDecapActionIdentity' , 'ydk.models.ietf.ietf_i2rs_rib', 'TunnelDecapActionIdentity', 
                [], [], 
                '''                IPv6 decap operations.
                ''',
                'ipv6_decap',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('hop-limit-action', REFERENCE_IDENTITY_CLASS, 'HopLimitActionIdentity' , 'ydk.models.ietf.ietf_i2rs_rib', 'HopLimitActionIdentity', 
                [], [], 
                '''                The hop limit actions:
                no-action or copy to inner header.
                ''',
                'hop_limit_action',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'ipv6-decap',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'NhAddRpc.Input.NexthopBase.TunnelDecap.LabelPop' : {
        'meta_info' : _MetaInfoClass('NhAddRpc.Input.NexthopBase.TunnelDecap.LabelPop',
            False, 
            [
            _MetaInfoClassMember('label-pop', REFERENCE_IDENTITY_CLASS, 'MplsLabelActionIdentity' , 'ydk.models.ietf.ietf_i2rs_rib', 'MplsLabelActionIdentity', 
                [], [], 
                '''                Pop a label from the label stack.
                ''',
                'label_pop',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ttl-action', REFERENCE_IDENTITY_CLASS, 'TtlActionIdentity' , 'ydk.models.ietf.ietf_i2rs_rib', 'TtlActionIdentity', 
                [], [], 
                '''                The label ttl action.
                ''',
                'ttl_action',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'label-pop',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'NhAddRpc.Input.NexthopBase.TunnelDecap' : {
        'meta_info' : _MetaInfoClass('NhAddRpc.Input.NexthopBase.TunnelDecap',
            False, 
            [
            _MetaInfoClassMember('ipv4-decap', REFERENCE_CLASS, 'Ipv4Decap' , 'ydk.models.ietf.ietf_i2rs_rib', 'NhAddRpc.Input.NexthopBase.TunnelDecap.Ipv4Decap', 
                [], [], 
                '''                IPv4 decap.
                ''',
                'ipv4_decap',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ipv6-decap', REFERENCE_CLASS, 'Ipv6Decap' , 'ydk.models.ietf.ietf_i2rs_rib', 'NhAddRpc.Input.NexthopBase.TunnelDecap.Ipv6Decap', 
                [], [], 
                '''                IPv6 decap.
                ''',
                'ipv6_decap',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('label-pop', REFERENCE_CLASS, 'LabelPop' , 'ydk.models.ietf.ietf_i2rs_rib', 'NhAddRpc.Input.NexthopBase.TunnelDecap.LabelPop', 
                [], [], 
                '''                MPLS decap.
                ''',
                'label_pop',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'tunnel-decap',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'NhAddRpc.Input.NexthopBase.LogicalTunnel' : {
        'meta_info' : _MetaInfoClass('NhAddRpc.Input.NexthopBase.LogicalTunnel',
            False, 
            [
            _MetaInfoClassMember('tunnel-type', REFERENCE_IDENTITY_CLASS, 'TunnelTypeIdentity' , 'ydk.models.ietf.ietf_i2rs_rib', 'TunnelTypeIdentity', 
                [], [], 
                '''                A tunnel type.
                ''',
                'tunnel_type',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('tunnel-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                A tunnel name that points to a logical tunnel.
                ''',
                'tunnel_name',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'logical-tunnel',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'NhAddRpc.Input.NexthopBase' : {
        'meta_info' : _MetaInfoClass('NhAddRpc.Input.NexthopBase',
            False, 
            [
            _MetaInfoClassMember('special', REFERENCE_IDENTITY_CLASS, 'SpecialNexthopIdentity' , 'ydk.models.ietf.ietf_i2rs_rib', 'SpecialNexthopIdentity', 
                [], [], 
                '''                A special nexthop.
                ''',
                'special',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('outgoing-interface', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The nexthop is an outgoing interface.
                ''',
                'outgoing_interface',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The nexthop is an IPv4 address.
                ''',
                'ipv4_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                The nexthop is an IPv6 address.
                ''',
                'ipv6_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('egress-interface-ipv4-address', REFERENCE_CLASS, 'EgressInterfaceIpv4Address' , 'ydk.models.ietf.ietf_i2rs_rib', 'NhAddRpc.Input.NexthopBase.EgressInterfaceIpv4Address', 
                [], [], 
                '''                The nexthop is an egress-interface and an IP
                address. This can be used in cases e.g. where
                the IP address is a link-local address.
                ''',
                'egress_interface_ipv4_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('egress-interface-ipv6-address', REFERENCE_CLASS, 'EgressInterfaceIpv6Address' , 'ydk.models.ietf.ietf_i2rs_rib', 'NhAddRpc.Input.NexthopBase.EgressInterfaceIpv6Address', 
                [], [], 
                '''                The nexthop is an egress-interface and an IP
                address. This can be used in cases e.g. where
                the IP address is a link-local address.
                ''',
                'egress_interface_ipv6_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('egress-interface-mac-address', REFERENCE_CLASS, 'EgressInterfaceMacAddress' , 'ydk.models.ietf.ietf_i2rs_rib', 'NhAddRpc.Input.NexthopBase.EgressInterfaceMacAddress', 
                [], [], 
                '''                The egress interface must be an Ethernet
                interface. Address resolution is not required
                for this nexthop.
                ''',
                'egress_interface_mac_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('tunnel-encap', REFERENCE_CLASS, 'TunnelEncap' , 'ydk.models.ietf.ietf_i2rs_rib', 'NhAddRpc.Input.NexthopBase.TunnelEncap', 
                [], [], 
                '''                This can be an encap representing an IP tunnel or
                MPLS tunnel or others as defined in info model.
                An optional egress interface can be chained to the
                tunnel encap to indicate which interface to send
                the packet out on.  The egress interface is useful
                when the network device contains Ethernet interfaces
                and one needs to perform address resolution for the
                IP packet.
                ''',
                'tunnel_encap',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('tunnel-decap', REFERENCE_CLASS, 'TunnelDecap' , 'ydk.models.ietf.ietf_i2rs_rib', 'NhAddRpc.Input.NexthopBase.TunnelDecap', 
                [], [], 
                '''                This is to specify decapsulating a tunnel header.
                ''',
                'tunnel_decap',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('logical-tunnel', REFERENCE_CLASS, 'LogicalTunnel' , 'ydk.models.ietf.ietf_i2rs_rib', 'NhAddRpc.Input.NexthopBase.LogicalTunnel', 
                [], [], 
                '''                This can be a MPLS LSP or a GRE tunnel (or others
                as defined in this document), that is represented
                by a unique identifier (e.g. name).
                ''',
                'logical_tunnel',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('rib-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                A nexthop pointing to a RIB indicates that the
                route lookup needs to continue in the specified
                rib. This is a way to perform chained lookups.
                ''',
                'rib_name',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('nexthop-ref', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A nexthop reference that points to a nexthop.
                ''',
                'nexthop_ref',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'nexthop-base',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'NhAddRpc.Input.NexthopChain.NexthopList' : {
        'meta_info' : _MetaInfoClass('NhAddRpc.Input.NexthopChain.NexthopList',
            False, 
            [
            _MetaInfoClassMember('nexthop-member-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A nexthop identifier that points
                to a nexthop list member.
                A nexthop list member is a nexthop.
                ''',
                'nexthop_member_id',
                'ietf-i2rs-rib', True),
            ],
            'ietf-i2rs-rib',
            'nexthop-list',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'NhAddRpc.Input.NexthopChain' : {
        'meta_info' : _MetaInfoClass('NhAddRpc.Input.NexthopChain',
            False, 
            [
            _MetaInfoClassMember('nexthop-list', REFERENCE_LIST, 'NexthopList' , 'ydk.models.ietf.ietf_i2rs_rib', 'NhAddRpc.Input.NexthopChain.NexthopList', 
                [], [], 
                '''                A list of nexthops.
                ''',
                'nexthop_list',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'nexthop-chain',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'NhAddRpc.Input.NexthopReplicates.NexthopList' : {
        'meta_info' : _MetaInfoClass('NhAddRpc.Input.NexthopReplicates.NexthopList',
            False, 
            [
            _MetaInfoClassMember('nexthop-member-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A nexthop identifier that points
                to a nexthop list member.
                A nexthop list member is a nexthop.
                ''',
                'nexthop_member_id',
                'ietf-i2rs-rib', True),
            ],
            'ietf-i2rs-rib',
            'nexthop-list',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'NhAddRpc.Input.NexthopReplicates' : {
        'meta_info' : _MetaInfoClass('NhAddRpc.Input.NexthopReplicates',
            False, 
            [
            _MetaInfoClassMember('nexthop-list', REFERENCE_LIST, 'NexthopList' , 'ydk.models.ietf.ietf_i2rs_rib', 'NhAddRpc.Input.NexthopReplicates.NexthopList', 
                [], [], 
                '''                A list of nexthops.
                ''',
                'nexthop_list',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'nexthop-replicates',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'NhAddRpc.Input.NexthopProtection.NexthopList' : {
        'meta_info' : _MetaInfoClass('NhAddRpc.Input.NexthopProtection.NexthopList',
            False, 
            [
            _MetaInfoClassMember('nexthop-member-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A nexthop identifier that points
                to a nexthop list member.
                A nexthop list member is a nexthop.
                ''',
                'nexthop_member_id',
                'ietf-i2rs-rib', True),
            _MetaInfoClassMember('nexthop-preference', ATTRIBUTE, 'int' , None, None, 
                [('1', '99')], [], 
                '''                Nexthop-preference is used for protection schemes.
                It is an integer value between 1 and 99.  Lower
                values are more preferred. To download a
                primary/standby/tertiary group to the FIB, the
                nexthops that are resolved and are most preferred
                are selected.
                ''',
                'nexthop_preference',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'nexthop-list',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'NhAddRpc.Input.NexthopProtection' : {
        'meta_info' : _MetaInfoClass('NhAddRpc.Input.NexthopProtection',
            False, 
            [
            _MetaInfoClassMember('nexthop-list', REFERENCE_LIST, 'NexthopList' , 'ydk.models.ietf.ietf_i2rs_rib', 'NhAddRpc.Input.NexthopProtection.NexthopList', 
                [], [], 
                '''                A list of nexthop.
                ''',
                'nexthop_list',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'nexthop-protection',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'NhAddRpc.Input.NexthopLb.NexthopList' : {
        'meta_info' : _MetaInfoClass('NhAddRpc.Input.NexthopLb.NexthopList',
            False, 
            [
            _MetaInfoClassMember('nexthop-member-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A nexthop identifier that points
                to a nexthop list member.
                A nexthop list member is a nexthop.
                ''',
                'nexthop_member_id',
                'ietf-i2rs-rib', True),
            _MetaInfoClassMember('nexthop-lb-weight', ATTRIBUTE, 'int' , None, None, 
                [('1', '99')], [], 
                '''                The weight of a nexthop of
                the load balance nexthops.
                ''',
                'nexthop_lb_weight',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'nexthop-list',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'NhAddRpc.Input.NexthopLb' : {
        'meta_info' : _MetaInfoClass('NhAddRpc.Input.NexthopLb',
            False, 
            [
            _MetaInfoClassMember('nexthop-list', REFERENCE_LIST, 'NexthopList' , 'ydk.models.ietf.ietf_i2rs_rib', 'NhAddRpc.Input.NexthopLb.NexthopList', 
                [], [], 
                '''                A list of nexthop.
                ''',
                'nexthop_list',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'nexthop-lb',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'NhAddRpc.Input' : {
        'meta_info' : _MetaInfoClass('NhAddRpc.Input',
            False, 
            [
            _MetaInfoClassMember('rib-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                A reference to the name of a rib.
                ''',
                'rib_name',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('nexthop-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                An identifier that refers to a nexthop.
                ''',
                'nexthop_id',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('sharing-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                To indicate whether a nexthop is sharable
                or non-sharable.
                true - sharable, means the nexthop can be shared
                       with other routes
                false - non-sharable, means the nexthop can not
                       be shared with other routes.
                ''',
                'sharing_flag',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('nexthop-base', REFERENCE_CLASS, 'NexthopBase' , 'ydk.models.ietf.ietf_i2rs_rib', 'NhAddRpc.Input.NexthopBase', 
                [], [], 
                '''                The base nexthop.
                ''',
                'nexthop_base',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('nexthop-chain', REFERENCE_CLASS, 'NexthopChain' , 'ydk.models.ietf.ietf_i2rs_rib', 'NhAddRpc.Input.NexthopChain', 
                [], [], 
                '''                A chain nexthop.
                ''',
                'nexthop_chain',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('nexthop-replicates', REFERENCE_CLASS, 'NexthopReplicates' , 'ydk.models.ietf.ietf_i2rs_rib', 'NhAddRpc.Input.NexthopReplicates', 
                [], [], 
                '''                A replicates nexthop.
                ''',
                'nexthop_replicates',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('nexthop-protection', REFERENCE_CLASS, 'NexthopProtection' , 'ydk.models.ietf.ietf_i2rs_rib', 'NhAddRpc.Input.NexthopProtection', 
                [], [], 
                '''                A protection nexthop.
                ''',
                'nexthop_protection',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('nexthop-lb', REFERENCE_CLASS, 'NexthopLb' , 'ydk.models.ietf.ietf_i2rs_rib', 'NhAddRpc.Input.NexthopLb', 
                [], [], 
                '''                A load balance nexthop.
                ''',
                'nexthop_lb',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'input',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'NhAddRpc.Output' : {
        'meta_info' : _MetaInfoClass('NhAddRpc.Output',
            False, 
            [
            _MetaInfoClassMember('result', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Return the result of the rib-add operation.
                true  - success;
                false - failed;
                ''',
                'result',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('reason', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The specific reason that causes the failure.
                ''',
                'reason',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('nexthop-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A nexthop identifier that is allocated to the nexthop.
                ''',
                'nexthop_id',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'output',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'NhAddRpc' : {
        'meta_info' : _MetaInfoClass('NhAddRpc',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.ietf.ietf_i2rs_rib', 'NhAddRpc.Input', 
                [], [], 
                '''                ''',
                'input',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('output', REFERENCE_CLASS, 'Output' , 'ydk.models.ietf.ietf_i2rs_rib', 'NhAddRpc.Output', 
                [], [], 
                '''                ''',
                'output',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'nh-add',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'NhDeleteRpc.Input.NexthopBase.EgressInterfaceIpv4Address' : {
        'meta_info' : _MetaInfoClass('NhDeleteRpc.Input.NexthopBase.EgressInterfaceIpv4Address',
            False, 
            [
            _MetaInfoClassMember('outgoing-interface', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the outgoing interface.
                ''',
                'outgoing_interface',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The nexthop points to an interface with
                an IPv4 address.
                ''',
                'ipv4_address',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'egress-interface-ipv4-address',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'NhDeleteRpc.Input.NexthopBase.EgressInterfaceIpv6Address' : {
        'meta_info' : _MetaInfoClass('NhDeleteRpc.Input.NexthopBase.EgressInterfaceIpv6Address',
            False, 
            [
            _MetaInfoClassMember('outgoing-interface', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the outgoing interface.
                ''',
                'outgoing_interface',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                The nexthop points to an interface with
                an IPv6 address.
                ''',
                'ipv6_address',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'egress-interface-ipv6-address',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'NhDeleteRpc.Input.NexthopBase.EgressInterfaceMacAddress' : {
        'meta_info' : _MetaInfoClass('NhDeleteRpc.Input.NexthopBase.EgressInterfaceMacAddress',
            False, 
            [
            _MetaInfoClassMember('outgoing-interface', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the outgoing interface.
                ''',
                'outgoing_interface',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ieee-mac-address', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The nexthop points to an interface with
                a specific mac-address.
                ''',
                'ieee_mac_address',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'egress-interface-mac-address',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'NhDeleteRpc.Input.NexthopBase.TunnelEncap.Ipv4Header' : {
        'meta_info' : _MetaInfoClass('NhDeleteRpc.Input.NexthopBase.TunnelEncap.Ipv4Header',
            False, 
            [
            _MetaInfoClassMember('src-ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The source IP address of the header.
                ''',
                'src_ipv4_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('dest-ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The destination IP address of the header.
                ''',
                'dest_ipv4_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('protocol', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The protocol id of the header.
                ''',
                'protocol',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ttl', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The TTL of the header.
                ''',
                'ttl',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('dscp', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The DSCP field of the header.
                ''',
                'dscp',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'ipv4-header',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'NhDeleteRpc.Input.NexthopBase.TunnelEncap.Ipv6Header' : {
        'meta_info' : _MetaInfoClass('NhDeleteRpc.Input.NexthopBase.TunnelEncap.Ipv6Header',
            False, 
            [
            _MetaInfoClassMember('src-ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                The source IP address of the header.
                ''',
                'src_ipv6_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('dest-ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                The destination IP address of the header.
                ''',
                'dest_ipv6_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('next-header', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The next header of the IPv6 header.
                ''',
                'next_header',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('traffic-class', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The traffic class value of the header.
                ''',
                'traffic_class',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('flow-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The flow label of the header.
                ''',
                'flow_label',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('hop-limit', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The hop limit the header.
                ''',
                'hop_limit',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'ipv6-header',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'NhDeleteRpc.Input.NexthopBase.TunnelEncap.MplsHeader.LabelOperations.LabelPush' : {
        'meta_info' : _MetaInfoClass('NhDeleteRpc.Input.NexthopBase.TunnelEncap.MplsHeader.LabelOperations.LabelPush',
            False, 
            [
            _MetaInfoClassMember('label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The label to be pushed.
                ''',
                'label',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('s-bit', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                The s-bit of the label to be pushed. 
                ''',
                's_bit',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('tc-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The traffic class value of the label to be pushed.
                ''',
                'tc_value',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ttl-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The TTL value of the label to be pushed.
                ''',
                'ttl_value',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'label-push',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'NhDeleteRpc.Input.NexthopBase.TunnelEncap.MplsHeader.LabelOperations.LabelSwap' : {
        'meta_info' : _MetaInfoClass('NhDeleteRpc.Input.NexthopBase.TunnelEncap.MplsHeader.LabelOperations.LabelSwap',
            False, 
            [
            _MetaInfoClassMember('in-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The label to be swapped.
                ''',
                'in_label',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('out-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The out MPLS label.
                ''',
                'out_label',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ttl-action', REFERENCE_IDENTITY_CLASS, 'TtlActionIdentity' , 'ydk.models.ietf.ietf_i2rs_rib', 'TtlActionIdentity', 
                [], [], 
                '''                The label ttl actions:
                - No-action, or
                - Copy to inner label,or
                - Decrease (the in label) by 1 and
                  copy to the out label.
                ''',
                'ttl_action',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'label-swap',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'NhDeleteRpc.Input.NexthopBase.TunnelEncap.MplsHeader.LabelOperations' : {
        'meta_info' : _MetaInfoClass('NhDeleteRpc.Input.NexthopBase.TunnelEncap.MplsHeader.LabelOperations',
            False, 
            [
            _MetaInfoClassMember('label-oper-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                An optional identifier that points
                to a label operation.
                ''',
                'label_oper_id',
                'ietf-i2rs-rib', True),
            _MetaInfoClassMember('label-push', REFERENCE_CLASS, 'LabelPush' , 'ydk.models.ietf.ietf_i2rs_rib', 'NhDeleteRpc.Input.NexthopBase.TunnelEncap.MplsHeader.LabelOperations.LabelPush', 
                [], [], 
                '''                Label push operation.
                ''',
                'label_push',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('label-swap', REFERENCE_CLASS, 'LabelSwap' , 'ydk.models.ietf.ietf_i2rs_rib', 'NhDeleteRpc.Input.NexthopBase.TunnelEncap.MplsHeader.LabelOperations.LabelSwap', 
                [], [], 
                '''                Label swap operation.
                ''',
                'label_swap',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'label-operations',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'NhDeleteRpc.Input.NexthopBase.TunnelEncap.MplsHeader' : {
        'meta_info' : _MetaInfoClass('NhDeleteRpc.Input.NexthopBase.TunnelEncap.MplsHeader',
            False, 
            [
            _MetaInfoClassMember('label-operations', REFERENCE_LIST, 'LabelOperations' , 'ydk.models.ietf.ietf_i2rs_rib', 'NhDeleteRpc.Input.NexthopBase.TunnelEncap.MplsHeader.LabelOperations', 
                [], [], 
                '''                Label operations.
                ''',
                'label_operations',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'mpls-header',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'NhDeleteRpc.Input.NexthopBase.TunnelEncap.GreHeader' : {
        'meta_info' : _MetaInfoClass('NhDeleteRpc.Input.NexthopBase.TunnelEncap.GreHeader',
            False, 
            [
            _MetaInfoClassMember('ipv4-dest', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The destination IP address of the GRE header.
                ''',
                'ipv4_dest',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ipv6-dest', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                The destination IP address of the GRE header.
                ''',
                'ipv6_dest',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('protocol-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The protocol type of the GRE header.
                ''',
                'protocol_type',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('key', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The GRE key of the GRE header.
                ''',
                'key',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'gre-header',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'NhDeleteRpc.Input.NexthopBase.TunnelEncap.NvgreHeader' : {
        'meta_info' : _MetaInfoClass('NhDeleteRpc.Input.NexthopBase.TunnelEncap.NvgreHeader',
            False, 
            [
            _MetaInfoClassMember('src-ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The source IP address of the header.
                ''',
                'src_ipv4_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('dest-ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The destination IP address of the header.
                ''',
                'dest_ipv4_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('protocol', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The protocol id of the header.
                ''',
                'protocol',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ttl', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The TTL of the header.
                ''',
                'ttl',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('dscp', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The DSCP field of the header.
                ''',
                'dscp',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('src-ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                The source IP address of the header.
                ''',
                'src_ipv6_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('dest-ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                The destination IP address of the header.
                ''',
                'dest_ipv6_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('next-header', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The next header of the IPv6 header.
                ''',
                'next_header',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('traffic-class', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The traffic class value of the header.
                ''',
                'traffic_class',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('flow-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The flow label of the header.
                ''',
                'flow_label',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('hop-limit', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The hop limit the header.
                ''',
                'hop_limit',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('virtual-subnet-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The subnet identifier of the NvGRE header.
                ''',
                'virtual_subnet_id',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('flow-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The flow identifier of the NvGRE header.
                ''',
                'flow_id',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'nvgre-header',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'NhDeleteRpc.Input.NexthopBase.TunnelEncap.VxlanHeader' : {
        'meta_info' : _MetaInfoClass('NhDeleteRpc.Input.NexthopBase.TunnelEncap.VxlanHeader',
            False, 
            [
            _MetaInfoClassMember('src-ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The source IP address of the header.
                ''',
                'src_ipv4_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('dest-ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The destination IP address of the header.
                ''',
                'dest_ipv4_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('protocol', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The protocol id of the header.
                ''',
                'protocol',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ttl', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The TTL of the header.
                ''',
                'ttl',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('dscp', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The DSCP field of the header.
                ''',
                'dscp',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('src-ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                The source IP address of the header.
                ''',
                'src_ipv6_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('dest-ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                The destination IP address of the header.
                ''',
                'dest_ipv6_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('next-header', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The next header of the IPv6 header.
                ''',
                'next_header',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('traffic-class', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The traffic class value of the header.
                ''',
                'traffic_class',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('flow-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The flow label of the header.
                ''',
                'flow_label',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('hop-limit', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The hop limit the header.
                ''',
                'hop_limit',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('vxlan-identifier', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The VxLAN identifier of the VxLAN header.
                ''',
                'vxlan_identifier',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'vxlan-header',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'NhDeleteRpc.Input.NexthopBase.TunnelEncap' : {
        'meta_info' : _MetaInfoClass('NhDeleteRpc.Input.NexthopBase.TunnelEncap',
            False, 
            [
            _MetaInfoClassMember('ipv4-header', REFERENCE_CLASS, 'Ipv4Header' , 'ydk.models.ietf.ietf_i2rs_rib', 'NhDeleteRpc.Input.NexthopBase.TunnelEncap.Ipv4Header', 
                [], [], 
                '''                IPv4 header.
                ''',
                'ipv4_header',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ipv6-header', REFERENCE_CLASS, 'Ipv6Header' , 'ydk.models.ietf.ietf_i2rs_rib', 'NhDeleteRpc.Input.NexthopBase.TunnelEncap.Ipv6Header', 
                [], [], 
                '''                IPv6 header.
                ''',
                'ipv6_header',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('mpls-header', REFERENCE_CLASS, 'MplsHeader' , 'ydk.models.ietf.ietf_i2rs_rib', 'NhDeleteRpc.Input.NexthopBase.TunnelEncap.MplsHeader', 
                [], [], 
                '''                MPLS header.
                ''',
                'mpls_header',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('gre-header', REFERENCE_CLASS, 'GreHeader' , 'ydk.models.ietf.ietf_i2rs_rib', 'NhDeleteRpc.Input.NexthopBase.TunnelEncap.GreHeader', 
                [], [], 
                '''                GRE header.
                ''',
                'gre_header',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('nvgre-header', REFERENCE_CLASS, 'NvgreHeader' , 'ydk.models.ietf.ietf_i2rs_rib', 'NhDeleteRpc.Input.NexthopBase.TunnelEncap.NvgreHeader', 
                [], [], 
                '''                NvGRE header.
                ''',
                'nvgre_header',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('vxlan-header', REFERENCE_CLASS, 'VxlanHeader' , 'ydk.models.ietf.ietf_i2rs_rib', 'NhDeleteRpc.Input.NexthopBase.TunnelEncap.VxlanHeader', 
                [], [], 
                '''                VxLAN header.
                ''',
                'vxlan_header',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'tunnel-encap',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'NhDeleteRpc.Input.NexthopBase.TunnelDecap.Ipv4Decap' : {
        'meta_info' : _MetaInfoClass('NhDeleteRpc.Input.NexthopBase.TunnelDecap.Ipv4Decap',
            False, 
            [
            _MetaInfoClassMember('ipv4-decap', REFERENCE_IDENTITY_CLASS, 'TunnelDecapActionIdentity' , 'ydk.models.ietf.ietf_i2rs_rib', 'TunnelDecapActionIdentity', 
                [], [], 
                '''                IPv4 decap operations.
                ''',
                'ipv4_decap',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ttl-action', REFERENCE_IDENTITY_CLASS, 'TtlActionIdentity' , 'ydk.models.ietf.ietf_i2rs_rib', 'TtlActionIdentity', 
                [], [], 
                '''                The ttl actions:
                no-action or copy to inner header.
                ''',
                'ttl_action',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'ipv4-decap',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'NhDeleteRpc.Input.NexthopBase.TunnelDecap.Ipv6Decap' : {
        'meta_info' : _MetaInfoClass('NhDeleteRpc.Input.NexthopBase.TunnelDecap.Ipv6Decap',
            False, 
            [
            _MetaInfoClassMember('ipv6-decap', REFERENCE_IDENTITY_CLASS, 'TunnelDecapActionIdentity' , 'ydk.models.ietf.ietf_i2rs_rib', 'TunnelDecapActionIdentity', 
                [], [], 
                '''                IPv6 decap operations.
                ''',
                'ipv6_decap',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('hop-limit-action', REFERENCE_IDENTITY_CLASS, 'HopLimitActionIdentity' , 'ydk.models.ietf.ietf_i2rs_rib', 'HopLimitActionIdentity', 
                [], [], 
                '''                The hop limit actions:
                no-action or copy to inner header.
                ''',
                'hop_limit_action',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'ipv6-decap',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'NhDeleteRpc.Input.NexthopBase.TunnelDecap.LabelPop' : {
        'meta_info' : _MetaInfoClass('NhDeleteRpc.Input.NexthopBase.TunnelDecap.LabelPop',
            False, 
            [
            _MetaInfoClassMember('label-pop', REFERENCE_IDENTITY_CLASS, 'MplsLabelActionIdentity' , 'ydk.models.ietf.ietf_i2rs_rib', 'MplsLabelActionIdentity', 
                [], [], 
                '''                Pop a label from the label stack.
                ''',
                'label_pop',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ttl-action', REFERENCE_IDENTITY_CLASS, 'TtlActionIdentity' , 'ydk.models.ietf.ietf_i2rs_rib', 'TtlActionIdentity', 
                [], [], 
                '''                The label ttl action.
                ''',
                'ttl_action',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'label-pop',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'NhDeleteRpc.Input.NexthopBase.TunnelDecap' : {
        'meta_info' : _MetaInfoClass('NhDeleteRpc.Input.NexthopBase.TunnelDecap',
            False, 
            [
            _MetaInfoClassMember('ipv4-decap', REFERENCE_CLASS, 'Ipv4Decap' , 'ydk.models.ietf.ietf_i2rs_rib', 'NhDeleteRpc.Input.NexthopBase.TunnelDecap.Ipv4Decap', 
                [], [], 
                '''                IPv4 decap.
                ''',
                'ipv4_decap',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ipv6-decap', REFERENCE_CLASS, 'Ipv6Decap' , 'ydk.models.ietf.ietf_i2rs_rib', 'NhDeleteRpc.Input.NexthopBase.TunnelDecap.Ipv6Decap', 
                [], [], 
                '''                IPv6 decap.
                ''',
                'ipv6_decap',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('label-pop', REFERENCE_CLASS, 'LabelPop' , 'ydk.models.ietf.ietf_i2rs_rib', 'NhDeleteRpc.Input.NexthopBase.TunnelDecap.LabelPop', 
                [], [], 
                '''                MPLS decap.
                ''',
                'label_pop',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'tunnel-decap',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'NhDeleteRpc.Input.NexthopBase.LogicalTunnel' : {
        'meta_info' : _MetaInfoClass('NhDeleteRpc.Input.NexthopBase.LogicalTunnel',
            False, 
            [
            _MetaInfoClassMember('tunnel-type', REFERENCE_IDENTITY_CLASS, 'TunnelTypeIdentity' , 'ydk.models.ietf.ietf_i2rs_rib', 'TunnelTypeIdentity', 
                [], [], 
                '''                A tunnel type.
                ''',
                'tunnel_type',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('tunnel-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                A tunnel name that points to a logical tunnel.
                ''',
                'tunnel_name',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'logical-tunnel',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'NhDeleteRpc.Input.NexthopBase' : {
        'meta_info' : _MetaInfoClass('NhDeleteRpc.Input.NexthopBase',
            False, 
            [
            _MetaInfoClassMember('special', REFERENCE_IDENTITY_CLASS, 'SpecialNexthopIdentity' , 'ydk.models.ietf.ietf_i2rs_rib', 'SpecialNexthopIdentity', 
                [], [], 
                '''                A special nexthop.
                ''',
                'special',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('outgoing-interface', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The nexthop is an outgoing interface.
                ''',
                'outgoing_interface',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The nexthop is an IPv4 address.
                ''',
                'ipv4_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                The nexthop is an IPv6 address.
                ''',
                'ipv6_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('egress-interface-ipv4-address', REFERENCE_CLASS, 'EgressInterfaceIpv4Address' , 'ydk.models.ietf.ietf_i2rs_rib', 'NhDeleteRpc.Input.NexthopBase.EgressInterfaceIpv4Address', 
                [], [], 
                '''                The nexthop is an egress-interface and an IP
                address. This can be used in cases e.g. where
                the IP address is a link-local address.
                ''',
                'egress_interface_ipv4_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('egress-interface-ipv6-address', REFERENCE_CLASS, 'EgressInterfaceIpv6Address' , 'ydk.models.ietf.ietf_i2rs_rib', 'NhDeleteRpc.Input.NexthopBase.EgressInterfaceIpv6Address', 
                [], [], 
                '''                The nexthop is an egress-interface and an IP
                address. This can be used in cases e.g. where
                the IP address is a link-local address.
                ''',
                'egress_interface_ipv6_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('egress-interface-mac-address', REFERENCE_CLASS, 'EgressInterfaceMacAddress' , 'ydk.models.ietf.ietf_i2rs_rib', 'NhDeleteRpc.Input.NexthopBase.EgressInterfaceMacAddress', 
                [], [], 
                '''                The egress interface must be an Ethernet
                interface. Address resolution is not required
                for this nexthop.
                ''',
                'egress_interface_mac_address',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('tunnel-encap', REFERENCE_CLASS, 'TunnelEncap' , 'ydk.models.ietf.ietf_i2rs_rib', 'NhDeleteRpc.Input.NexthopBase.TunnelEncap', 
                [], [], 
                '''                This can be an encap representing an IP tunnel or
                MPLS tunnel or others as defined in info model.
                An optional egress interface can be chained to the
                tunnel encap to indicate which interface to send
                the packet out on.  The egress interface is useful
                when the network device contains Ethernet interfaces
                and one needs to perform address resolution for the
                IP packet.
                ''',
                'tunnel_encap',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('tunnel-decap', REFERENCE_CLASS, 'TunnelDecap' , 'ydk.models.ietf.ietf_i2rs_rib', 'NhDeleteRpc.Input.NexthopBase.TunnelDecap', 
                [], [], 
                '''                This is to specify decapsulating a tunnel header.
                ''',
                'tunnel_decap',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('logical-tunnel', REFERENCE_CLASS, 'LogicalTunnel' , 'ydk.models.ietf.ietf_i2rs_rib', 'NhDeleteRpc.Input.NexthopBase.LogicalTunnel', 
                [], [], 
                '''                This can be a MPLS LSP or a GRE tunnel (or others
                as defined in this document), that is represented
                by a unique identifier (e.g. name).
                ''',
                'logical_tunnel',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('rib-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                A nexthop pointing to a RIB indicates that the
                route lookup needs to continue in the specified
                rib. This is a way to perform chained lookups.
                ''',
                'rib_name',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('nexthop-ref', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A nexthop reference that points to a nexthop.
                ''',
                'nexthop_ref',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'nexthop-base',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'NhDeleteRpc.Input.NexthopChain.NexthopList' : {
        'meta_info' : _MetaInfoClass('NhDeleteRpc.Input.NexthopChain.NexthopList',
            False, 
            [
            _MetaInfoClassMember('nexthop-member-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A nexthop identifier that points
                to a nexthop list member.
                A nexthop list member is a nexthop.
                ''',
                'nexthop_member_id',
                'ietf-i2rs-rib', True),
            ],
            'ietf-i2rs-rib',
            'nexthop-list',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'NhDeleteRpc.Input.NexthopChain' : {
        'meta_info' : _MetaInfoClass('NhDeleteRpc.Input.NexthopChain',
            False, 
            [
            _MetaInfoClassMember('nexthop-list', REFERENCE_LIST, 'NexthopList' , 'ydk.models.ietf.ietf_i2rs_rib', 'NhDeleteRpc.Input.NexthopChain.NexthopList', 
                [], [], 
                '''                A list of nexthops.
                ''',
                'nexthop_list',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'nexthop-chain',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'NhDeleteRpc.Input.NexthopReplicates.NexthopList' : {
        'meta_info' : _MetaInfoClass('NhDeleteRpc.Input.NexthopReplicates.NexthopList',
            False, 
            [
            _MetaInfoClassMember('nexthop-member-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A nexthop identifier that points
                to a nexthop list member.
                A nexthop list member is a nexthop.
                ''',
                'nexthop_member_id',
                'ietf-i2rs-rib', True),
            ],
            'ietf-i2rs-rib',
            'nexthop-list',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'NhDeleteRpc.Input.NexthopReplicates' : {
        'meta_info' : _MetaInfoClass('NhDeleteRpc.Input.NexthopReplicates',
            False, 
            [
            _MetaInfoClassMember('nexthop-list', REFERENCE_LIST, 'NexthopList' , 'ydk.models.ietf.ietf_i2rs_rib', 'NhDeleteRpc.Input.NexthopReplicates.NexthopList', 
                [], [], 
                '''                A list of nexthops.
                ''',
                'nexthop_list',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'nexthop-replicates',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'NhDeleteRpc.Input.NexthopProtection.NexthopList' : {
        'meta_info' : _MetaInfoClass('NhDeleteRpc.Input.NexthopProtection.NexthopList',
            False, 
            [
            _MetaInfoClassMember('nexthop-member-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A nexthop identifier that points
                to a nexthop list member.
                A nexthop list member is a nexthop.
                ''',
                'nexthop_member_id',
                'ietf-i2rs-rib', True),
            _MetaInfoClassMember('nexthop-preference', ATTRIBUTE, 'int' , None, None, 
                [('1', '99')], [], 
                '''                Nexthop-preference is used for protection schemes.
                It is an integer value between 1 and 99.  Lower
                values are more preferred. To download a
                primary/standby/tertiary group to the FIB, the
                nexthops that are resolved and are most preferred
                are selected.
                ''',
                'nexthop_preference',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'nexthop-list',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'NhDeleteRpc.Input.NexthopProtection' : {
        'meta_info' : _MetaInfoClass('NhDeleteRpc.Input.NexthopProtection',
            False, 
            [
            _MetaInfoClassMember('nexthop-list', REFERENCE_LIST, 'NexthopList' , 'ydk.models.ietf.ietf_i2rs_rib', 'NhDeleteRpc.Input.NexthopProtection.NexthopList', 
                [], [], 
                '''                A list of nexthop.
                ''',
                'nexthop_list',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'nexthop-protection',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'NhDeleteRpc.Input.NexthopLb.NexthopList' : {
        'meta_info' : _MetaInfoClass('NhDeleteRpc.Input.NexthopLb.NexthopList',
            False, 
            [
            _MetaInfoClassMember('nexthop-member-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A nexthop identifier that points
                to a nexthop list member.
                A nexthop list member is a nexthop.
                ''',
                'nexthop_member_id',
                'ietf-i2rs-rib', True),
            _MetaInfoClassMember('nexthop-lb-weight', ATTRIBUTE, 'int' , None, None, 
                [('1', '99')], [], 
                '''                The weight of a nexthop of
                the load balance nexthops.
                ''',
                'nexthop_lb_weight',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'nexthop-list',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'NhDeleteRpc.Input.NexthopLb' : {
        'meta_info' : _MetaInfoClass('NhDeleteRpc.Input.NexthopLb',
            False, 
            [
            _MetaInfoClassMember('nexthop-list', REFERENCE_LIST, 'NexthopList' , 'ydk.models.ietf.ietf_i2rs_rib', 'NhDeleteRpc.Input.NexthopLb.NexthopList', 
                [], [], 
                '''                A list of nexthop.
                ''',
                'nexthop_list',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'nexthop-lb',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'NhDeleteRpc.Input' : {
        'meta_info' : _MetaInfoClass('NhDeleteRpc.Input',
            False, 
            [
            _MetaInfoClassMember('rib-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                A reference to the name of a rib.
                ''',
                'rib_name',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('nexthop-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                An identifier that refers to a nexthop.
                ''',
                'nexthop_id',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('sharing-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                To indicate whether a nexthop is sharable
                or non-sharable.
                true - sharable, means the nexthop can be shared
                       with other routes
                false - non-sharable, means the nexthop can not
                       be shared with other routes.
                ''',
                'sharing_flag',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('nexthop-base', REFERENCE_CLASS, 'NexthopBase' , 'ydk.models.ietf.ietf_i2rs_rib', 'NhDeleteRpc.Input.NexthopBase', 
                [], [], 
                '''                The base nexthop.
                ''',
                'nexthop_base',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('nexthop-chain', REFERENCE_CLASS, 'NexthopChain' , 'ydk.models.ietf.ietf_i2rs_rib', 'NhDeleteRpc.Input.NexthopChain', 
                [], [], 
                '''                A chain nexthop.
                ''',
                'nexthop_chain',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('nexthop-replicates', REFERENCE_CLASS, 'NexthopReplicates' , 'ydk.models.ietf.ietf_i2rs_rib', 'NhDeleteRpc.Input.NexthopReplicates', 
                [], [], 
                '''                A replicates nexthop.
                ''',
                'nexthop_replicates',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('nexthop-protection', REFERENCE_CLASS, 'NexthopProtection' , 'ydk.models.ietf.ietf_i2rs_rib', 'NhDeleteRpc.Input.NexthopProtection', 
                [], [], 
                '''                A protection nexthop.
                ''',
                'nexthop_protection',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('nexthop-lb', REFERENCE_CLASS, 'NexthopLb' , 'ydk.models.ietf.ietf_i2rs_rib', 'NhDeleteRpc.Input.NexthopLb', 
                [], [], 
                '''                A load balance nexthop.
                ''',
                'nexthop_lb',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'input',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'NhDeleteRpc.Output' : {
        'meta_info' : _MetaInfoClass('NhDeleteRpc.Output',
            False, 
            [
            _MetaInfoClassMember('result', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Return the result of the rib-add operation.
                true  - success;
                false - failed.
                ''',
                'result',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('reason', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The specific reason that causes the failure.
                ''',
                'reason',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'output',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'NhDeleteRpc' : {
        'meta_info' : _MetaInfoClass('NhDeleteRpc',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.ietf.ietf_i2rs_rib', 'NhDeleteRpc.Input', 
                [], [], 
                '''                ''',
                'input',
                'ietf-i2rs-rib', False),
            _MetaInfoClassMember('output', REFERENCE_CLASS, 'Output' , 'ydk.models.ietf.ietf_i2rs_rib', 'NhDeleteRpc.Output', 
                [], [], 
                '''                ''',
                'output',
                'ietf-i2rs-rib', False),
            ],
            'ietf-i2rs-rib',
            'nh-delete',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'MplsRibFamilyIdentity' : {
        'meta_info' : _MetaInfoClass('MplsRibFamilyIdentity',
            False, 
            [
            ],
            'ietf-i2rs-rib',
            'mpls-rib-family',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'Ipv4RibFamilyIdentity' : {
        'meta_info' : _MetaInfoClass('Ipv4RibFamilyIdentity',
            False, 
            [
            ],
            'ietf-i2rs-rib',
            'ipv4-rib-family',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'LabelPushIdentity' : {
        'meta_info' : _MetaInfoClass('LabelPushIdentity',
            False, 
            [
            ],
            'ietf-i2rs-rib',
            'label-push',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'Ipv4DecapIdentity' : {
        'meta_info' : _MetaInfoClass('Ipv4DecapIdentity',
            False, 
            [
            ],
            'ietf-i2rs-rib',
            'ipv4-decap',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'UnresolvedNexthopIdentity' : {
        'meta_info' : _MetaInfoClass('UnresolvedNexthopIdentity',
            False, 
            [
            ],
            'ietf-i2rs-rib',
            'unresolved-nexthop',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'NoActionIdentity' : {
        'meta_info' : _MetaInfoClass('NoActionIdentity',
            False, 
            [
            ],
            'ietf-i2rs-rib',
            'no-action',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'InstalledIdentity' : {
        'meta_info' : _MetaInfoClass('InstalledIdentity',
            False, 
            [
            ],
            'ietf-i2rs-rib',
            'installed',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'ActiveIdentity' : {
        'meta_info' : _MetaInfoClass('ActiveIdentity',
            False, 
            [
            ],
            'ietf-i2rs-rib',
            'active',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'InactiveIdentity' : {
        'meta_info' : _MetaInfoClass('InactiveIdentity',
            False, 
            [
            ],
            'ietf-i2rs-rib',
            'inactive',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'ResolvedNexthopIdentity' : {
        'meta_info' : _MetaInfoClass('ResolvedNexthopIdentity',
            False, 
            [
            ],
            'ietf-i2rs-rib',
            'resolved-nexthop',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'DecreaseAndCopyToInnerIdentity' : {
        'meta_info' : _MetaInfoClass('DecreaseAndCopyToInnerIdentity',
            False, 
            [
            ],
            'ietf-i2rs-rib',
            'decrease-and-copy-to-inner',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'IeeeMacIdentity' : {
        'meta_info' : _MetaInfoClass('IeeeMacIdentity',
            False, 
            [
            ],
            'ietf-i2rs-rib',
            'ieee-mac',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'IeeeMacRibFamilyIdentity' : {
        'meta_info' : _MetaInfoClass('IeeeMacRibFamilyIdentity',
            False, 
            [
            ],
            'ietf-i2rs-rib',
            'ieee-mac-rib-family',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'LabelPopIdentity' : {
        'meta_info' : _MetaInfoClass('LabelPopIdentity',
            False, 
            [
            ],
            'ietf-i2rs-rib',
            'label-pop',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'MatchIpSrcDestIdentity' : {
        'meta_info' : _MetaInfoClass('MatchIpSrcDestIdentity',
            False, 
            [
            ],
            'ietf-i2rs-rib',
            'match-ip-src-dest',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'HopLimitNoActionIdentity' : {
        'meta_info' : _MetaInfoClass('HopLimitNoActionIdentity',
            False, 
            [
            ],
            'ietf-i2rs-rib',
            'hop-limit-no-action',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'UninstalledIdentity' : {
        'meta_info' : _MetaInfoClass('UninstalledIdentity',
            False, 
            [
            ],
            'ietf-i2rs-rib',
            'uninstalled',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'HopLimitCopyToInnerIdentity' : {
        'meta_info' : _MetaInfoClass('HopLimitCopyToInnerIdentity',
            False, 
            [
            ],
            'ietf-i2rs-rib',
            'hop-limit-copy-to-inner',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'Ipv6DecapIdentity' : {
        'meta_info' : _MetaInfoClass('Ipv6DecapIdentity',
            False, 
            [
            ],
            'ietf-i2rs-rib',
            'ipv6-decap',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'HigherRoutePreferenceIdentity' : {
        'meta_info' : _MetaInfoClass('HigherRoutePreferenceIdentity',
            False, 
            [
            ],
            'ietf-i2rs-rib',
            'higher-route-preference',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'MplsTunnelIdentity' : {
        'meta_info' : _MetaInfoClass('MplsTunnelIdentity',
            False, 
            [
            ],
            'ietf-i2rs-rib',
            'mpls-tunnel',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'ResolvedIdentity' : {
        'meta_info' : _MetaInfoClass('ResolvedIdentity',
            False, 
            [
            ],
            'ietf-i2rs-rib',
            'resolved',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'Ipv6RouteIdentity' : {
        'meta_info' : _MetaInfoClass('Ipv6RouteIdentity',
            False, 
            [
            ],
            'ietf-i2rs-rib',
            'ipv6-route',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'VxlanTunnelIdentity' : {
        'meta_info' : _MetaInfoClass('VxlanTunnelIdentity',
            False, 
            [
            ],
            'ietf-i2rs-rib',
            'vxlan-tunnel',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'MatchIpSrcIdentity' : {
        'meta_info' : _MetaInfoClass('MatchIpSrcIdentity',
            False, 
            [
            ],
            'ietf-i2rs-rib',
            'match-ip-src',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'Ipv6TunnelIdentity' : {
        'meta_info' : _MetaInfoClass('Ipv6TunnelIdentity',
            False, 
            [
            ],
            'ietf-i2rs-rib',
            'ipv6-tunnel',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'LowerRoutePreferenceIdentity' : {
        'meta_info' : _MetaInfoClass('LowerRoutePreferenceIdentity',
            False, 
            [
            ],
            'ietf-i2rs-rib',
            'lower-route-preference',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'UnresolvedIdentity' : {
        'meta_info' : _MetaInfoClass('UnresolvedIdentity',
            False, 
            [
            ],
            'ietf-i2rs-rib',
            'unresolved',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'CopyToInnerIdentity' : {
        'meta_info' : _MetaInfoClass('CopyToInnerIdentity',
            False, 
            [
            ],
            'ietf-i2rs-rib',
            'copy-to-inner',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'InterfaceIdentity' : {
        'meta_info' : _MetaInfoClass('InterfaceIdentity',
            False, 
            [
            ],
            'ietf-i2rs-rib',
            'interface',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'Ipv6RibFamilyIdentity' : {
        'meta_info' : _MetaInfoClass('Ipv6RibFamilyIdentity',
            False, 
            [
            ],
            'ietf-i2rs-rib',
            'ipv6-rib-family',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'Ipv4RouteIdentity' : {
        'meta_info' : _MetaInfoClass('Ipv4RouteIdentity',
            False, 
            [
            ],
            'ietf-i2rs-rib',
            'ipv4-route',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'Ipv4TunnelIdentity' : {
        'meta_info' : _MetaInfoClass('Ipv4TunnelIdentity',
            False, 
            [
            ],
            'ietf-i2rs-rib',
            'ipv4-tunnel',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'ReceiveIdentity' : {
        'meta_info' : _MetaInfoClass('ReceiveIdentity',
            False, 
            [
            ],
            'ietf-i2rs-rib',
            'receive',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'MatchIpDestIdentity' : {
        'meta_info' : _MetaInfoClass('MatchIpDestIdentity',
            False, 
            [
            ],
            'ietf-i2rs-rib',
            'match-ip-dest',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'NvgreTunnelIdentity' : {
        'meta_info' : _MetaInfoClass('NvgreTunnelIdentity',
            False, 
            [
            ],
            'ietf-i2rs-rib',
            'nvgre-tunnel',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'DiscardWithErrorIdentity' : {
        'meta_info' : _MetaInfoClass('DiscardWithErrorIdentity',
            False, 
            [
            ],
            'ietf-i2rs-rib',
            'discard-with-error',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'CosValueIdentity' : {
        'meta_info' : _MetaInfoClass('CosValueIdentity',
            False, 
            [
            ],
            'ietf-i2rs-rib',
            'cos-value',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'LabelSwapIdentity' : {
        'meta_info' : _MetaInfoClass('LabelSwapIdentity',
            False, 
            [
            ],
            'ietf-i2rs-rib',
            'label-swap',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'MplsRouteIdentity' : {
        'meta_info' : _MetaInfoClass('MplsRouteIdentity',
            False, 
            [
            ],
            'ietf-i2rs-rib',
            'mpls-route',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'GreTunnelIdentity' : {
        'meta_info' : _MetaInfoClass('GreTunnelIdentity',
            False, 
            [
            ],
            'ietf-i2rs-rib',
            'gre-tunnel',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'DiscardIdentity' : {
        'meta_info' : _MetaInfoClass('DiscardIdentity',
            False, 
            [
            ],
            'ietf-i2rs-rib',
            'discard',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
    'DecreaseAndCopyToNextIdentity' : {
        'meta_info' : _MetaInfoClass('DecreaseAndCopyToNextIdentity',
            False, 
            [
            ],
            'ietf-i2rs-rib',
            'decrease-and-copy-to-next',
            _yang_ns._namespaces['ietf-i2rs-rib'],
        'ydk.models.ietf.ietf_i2rs_rib'
        ),
    },
}
_meta_table['RoutingInstance.RibList.RouteList.Match.Ipv4.DestSrcIpv4Address']['meta_info'].parent =_meta_table['RoutingInstance.RibList.RouteList.Match.Ipv4']['meta_info']
_meta_table['RoutingInstance.RibList.RouteList.Match.Ipv6.DestSrcIpv6Address']['meta_info'].parent =_meta_table['RoutingInstance.RibList.RouteList.Match.Ipv6']['meta_info']
_meta_table['RoutingInstance.RibList.RouteList.Match.Ipv4']['meta_info'].parent =_meta_table['RoutingInstance.RibList.RouteList.Match']['meta_info']
_meta_table['RoutingInstance.RibList.RouteList.Match.Ipv6']['meta_info'].parent =_meta_table['RoutingInstance.RibList.RouteList.Match']['meta_info']
_meta_table['RoutingInstance.RibList.RouteList.Nexthop.NexthopBase.TunnelEncap.MplsHeader.LabelOperations.LabelPush']['meta_info'].parent =_meta_table['RoutingInstance.RibList.RouteList.Nexthop.NexthopBase.TunnelEncap.MplsHeader.LabelOperations']['meta_info']
_meta_table['RoutingInstance.RibList.RouteList.Nexthop.NexthopBase.TunnelEncap.MplsHeader.LabelOperations.LabelSwap']['meta_info'].parent =_meta_table['RoutingInstance.RibList.RouteList.Nexthop.NexthopBase.TunnelEncap.MplsHeader.LabelOperations']['meta_info']
_meta_table['RoutingInstance.RibList.RouteList.Nexthop.NexthopBase.TunnelEncap.MplsHeader.LabelOperations']['meta_info'].parent =_meta_table['RoutingInstance.RibList.RouteList.Nexthop.NexthopBase.TunnelEncap.MplsHeader']['meta_info']
_meta_table['RoutingInstance.RibList.RouteList.Nexthop.NexthopBase.TunnelEncap.Ipv4Header']['meta_info'].parent =_meta_table['RoutingInstance.RibList.RouteList.Nexthop.NexthopBase.TunnelEncap']['meta_info']
_meta_table['RoutingInstance.RibList.RouteList.Nexthop.NexthopBase.TunnelEncap.Ipv6Header']['meta_info'].parent =_meta_table['RoutingInstance.RibList.RouteList.Nexthop.NexthopBase.TunnelEncap']['meta_info']
_meta_table['RoutingInstance.RibList.RouteList.Nexthop.NexthopBase.TunnelEncap.MplsHeader']['meta_info'].parent =_meta_table['RoutingInstance.RibList.RouteList.Nexthop.NexthopBase.TunnelEncap']['meta_info']
_meta_table['RoutingInstance.RibList.RouteList.Nexthop.NexthopBase.TunnelEncap.GreHeader']['meta_info'].parent =_meta_table['RoutingInstance.RibList.RouteList.Nexthop.NexthopBase.TunnelEncap']['meta_info']
_meta_table['RoutingInstance.RibList.RouteList.Nexthop.NexthopBase.TunnelEncap.NvgreHeader']['meta_info'].parent =_meta_table['RoutingInstance.RibList.RouteList.Nexthop.NexthopBase.TunnelEncap']['meta_info']
_meta_table['RoutingInstance.RibList.RouteList.Nexthop.NexthopBase.TunnelEncap.VxlanHeader']['meta_info'].parent =_meta_table['RoutingInstance.RibList.RouteList.Nexthop.NexthopBase.TunnelEncap']['meta_info']
_meta_table['RoutingInstance.RibList.RouteList.Nexthop.NexthopBase.TunnelDecap.Ipv4Decap']['meta_info'].parent =_meta_table['RoutingInstance.RibList.RouteList.Nexthop.NexthopBase.TunnelDecap']['meta_info']
_meta_table['RoutingInstance.RibList.RouteList.Nexthop.NexthopBase.TunnelDecap.Ipv6Decap']['meta_info'].parent =_meta_table['RoutingInstance.RibList.RouteList.Nexthop.NexthopBase.TunnelDecap']['meta_info']
_meta_table['RoutingInstance.RibList.RouteList.Nexthop.NexthopBase.TunnelDecap.LabelPop']['meta_info'].parent =_meta_table['RoutingInstance.RibList.RouteList.Nexthop.NexthopBase.TunnelDecap']['meta_info']
_meta_table['RoutingInstance.RibList.RouteList.Nexthop.NexthopBase.EgressInterfaceIpv4Address']['meta_info'].parent =_meta_table['RoutingInstance.RibList.RouteList.Nexthop.NexthopBase']['meta_info']
_meta_table['RoutingInstance.RibList.RouteList.Nexthop.NexthopBase.EgressInterfaceIpv6Address']['meta_info'].parent =_meta_table['RoutingInstance.RibList.RouteList.Nexthop.NexthopBase']['meta_info']
_meta_table['RoutingInstance.RibList.RouteList.Nexthop.NexthopBase.EgressInterfaceMacAddress']['meta_info'].parent =_meta_table['RoutingInstance.RibList.RouteList.Nexthop.NexthopBase']['meta_info']
_meta_table['RoutingInstance.RibList.RouteList.Nexthop.NexthopBase.TunnelEncap']['meta_info'].parent =_meta_table['RoutingInstance.RibList.RouteList.Nexthop.NexthopBase']['meta_info']
_meta_table['RoutingInstance.RibList.RouteList.Nexthop.NexthopBase.TunnelDecap']['meta_info'].parent =_meta_table['RoutingInstance.RibList.RouteList.Nexthop.NexthopBase']['meta_info']
_meta_table['RoutingInstance.RibList.RouteList.Nexthop.NexthopBase.LogicalTunnel']['meta_info'].parent =_meta_table['RoutingInstance.RibList.RouteList.Nexthop.NexthopBase']['meta_info']
_meta_table['RoutingInstance.RibList.RouteList.Nexthop.NexthopChain.NexthopList']['meta_info'].parent =_meta_table['RoutingInstance.RibList.RouteList.Nexthop.NexthopChain']['meta_info']
_meta_table['RoutingInstance.RibList.RouteList.Nexthop.NexthopReplicates.NexthopList']['meta_info'].parent =_meta_table['RoutingInstance.RibList.RouteList.Nexthop.NexthopReplicates']['meta_info']
_meta_table['RoutingInstance.RibList.RouteList.Nexthop.NexthopProtection.NexthopList']['meta_info'].parent =_meta_table['RoutingInstance.RibList.RouteList.Nexthop.NexthopProtection']['meta_info']
_meta_table['RoutingInstance.RibList.RouteList.Nexthop.NexthopLb.NexthopList']['meta_info'].parent =_meta_table['RoutingInstance.RibList.RouteList.Nexthop.NexthopLb']['meta_info']
_meta_table['RoutingInstance.RibList.RouteList.Nexthop.NexthopBase']['meta_info'].parent =_meta_table['RoutingInstance.RibList.RouteList.Nexthop']['meta_info']
_meta_table['RoutingInstance.RibList.RouteList.Nexthop.NexthopChain']['meta_info'].parent =_meta_table['RoutingInstance.RibList.RouteList.Nexthop']['meta_info']
_meta_table['RoutingInstance.RibList.RouteList.Nexthop.NexthopReplicates']['meta_info'].parent =_meta_table['RoutingInstance.RibList.RouteList.Nexthop']['meta_info']
_meta_table['RoutingInstance.RibList.RouteList.Nexthop.NexthopProtection']['meta_info'].parent =_meta_table['RoutingInstance.RibList.RouteList.Nexthop']['meta_info']
_meta_table['RoutingInstance.RibList.RouteList.Nexthop.NexthopLb']['meta_info'].parent =_meta_table['RoutingInstance.RibList.RouteList.Nexthop']['meta_info']
_meta_table['RoutingInstance.RibList.RouteList.RouteAttributes.AddressFamilyRouteAttributes']['meta_info'].parent =_meta_table['RoutingInstance.RibList.RouteList.RouteAttributes']['meta_info']
_meta_table['RoutingInstance.RibList.RouteList.Match']['meta_info'].parent =_meta_table['RoutingInstance.RibList.RouteList']['meta_info']
_meta_table['RoutingInstance.RibList.RouteList.Nexthop']['meta_info'].parent =_meta_table['RoutingInstance.RibList.RouteList']['meta_info']
_meta_table['RoutingInstance.RibList.RouteList.RouteStatus']['meta_info'].parent =_meta_table['RoutingInstance.RibList.RouteList']['meta_info']
_meta_table['RoutingInstance.RibList.RouteList.RouteAttributes']['meta_info'].parent =_meta_table['RoutingInstance.RibList.RouteList']['meta_info']
_meta_table['RoutingInstance.RibList.RouteList.RouteVendorAttributes']['meta_info'].parent =_meta_table['RoutingInstance.RibList.RouteList']['meta_info']
_meta_table['RoutingInstance.RibList.RouteList']['meta_info'].parent =_meta_table['RoutingInstance.RibList']['meta_info']
_meta_table['RoutingInstance.RibList.NexthopList']['meta_info'].parent =_meta_table['RoutingInstance.RibList']['meta_info']
_meta_table['RoutingInstance.InterfaceList']['meta_info'].parent =_meta_table['RoutingInstance']['meta_info']
_meta_table['RoutingInstance.RibList']['meta_info'].parent =_meta_table['RoutingInstance']['meta_info']
_meta_table['RibAddRpc.Input']['meta_info'].parent =_meta_table['RibAddRpc']['meta_info']
_meta_table['RibAddRpc.Output']['meta_info'].parent =_meta_table['RibAddRpc']['meta_info']
_meta_table['RibDeleteRpc.Input']['meta_info'].parent =_meta_table['RibDeleteRpc']['meta_info']
_meta_table['RibDeleteRpc.Output']['meta_info'].parent =_meta_table['RibDeleteRpc']['meta_info']
_meta_table['RouteAddRpc.Input.Routes.RouteList.Match.Ipv4.DestSrcIpv4Address']['meta_info'].parent =_meta_table['RouteAddRpc.Input.Routes.RouteList.Match.Ipv4']['meta_info']
_meta_table['RouteAddRpc.Input.Routes.RouteList.Match.Ipv6.DestSrcIpv6Address']['meta_info'].parent =_meta_table['RouteAddRpc.Input.Routes.RouteList.Match.Ipv6']['meta_info']
_meta_table['RouteAddRpc.Input.Routes.RouteList.Match.Ipv4']['meta_info'].parent =_meta_table['RouteAddRpc.Input.Routes.RouteList.Match']['meta_info']
_meta_table['RouteAddRpc.Input.Routes.RouteList.Match.Ipv6']['meta_info'].parent =_meta_table['RouteAddRpc.Input.Routes.RouteList.Match']['meta_info']
_meta_table['RouteAddRpc.Input.Routes.RouteList.RouteAttributes.AddressFamilyRouteAttributes']['meta_info'].parent =_meta_table['RouteAddRpc.Input.Routes.RouteList.RouteAttributes']['meta_info']
_meta_table['RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopBase.TunnelEncap.MplsHeader.LabelOperations.LabelPush']['meta_info'].parent =_meta_table['RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopBase.TunnelEncap.MplsHeader.LabelOperations']['meta_info']
_meta_table['RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopBase.TunnelEncap.MplsHeader.LabelOperations.LabelSwap']['meta_info'].parent =_meta_table['RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopBase.TunnelEncap.MplsHeader.LabelOperations']['meta_info']
_meta_table['RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopBase.TunnelEncap.MplsHeader.LabelOperations']['meta_info'].parent =_meta_table['RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopBase.TunnelEncap.MplsHeader']['meta_info']
_meta_table['RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopBase.TunnelEncap.Ipv4Header']['meta_info'].parent =_meta_table['RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopBase.TunnelEncap']['meta_info']
_meta_table['RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopBase.TunnelEncap.Ipv6Header']['meta_info'].parent =_meta_table['RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopBase.TunnelEncap']['meta_info']
_meta_table['RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopBase.TunnelEncap.MplsHeader']['meta_info'].parent =_meta_table['RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopBase.TunnelEncap']['meta_info']
_meta_table['RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopBase.TunnelEncap.GreHeader']['meta_info'].parent =_meta_table['RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopBase.TunnelEncap']['meta_info']
_meta_table['RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopBase.TunnelEncap.NvgreHeader']['meta_info'].parent =_meta_table['RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopBase.TunnelEncap']['meta_info']
_meta_table['RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopBase.TunnelEncap.VxlanHeader']['meta_info'].parent =_meta_table['RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopBase.TunnelEncap']['meta_info']
_meta_table['RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopBase.TunnelDecap.Ipv4Decap']['meta_info'].parent =_meta_table['RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopBase.TunnelDecap']['meta_info']
_meta_table['RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopBase.TunnelDecap.Ipv6Decap']['meta_info'].parent =_meta_table['RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopBase.TunnelDecap']['meta_info']
_meta_table['RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopBase.TunnelDecap.LabelPop']['meta_info'].parent =_meta_table['RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopBase.TunnelDecap']['meta_info']
_meta_table['RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopBase.EgressInterfaceIpv4Address']['meta_info'].parent =_meta_table['RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopBase']['meta_info']
_meta_table['RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopBase.EgressInterfaceIpv6Address']['meta_info'].parent =_meta_table['RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopBase']['meta_info']
_meta_table['RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopBase.EgressInterfaceMacAddress']['meta_info'].parent =_meta_table['RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopBase']['meta_info']
_meta_table['RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopBase.TunnelEncap']['meta_info'].parent =_meta_table['RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopBase']['meta_info']
_meta_table['RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopBase.TunnelDecap']['meta_info'].parent =_meta_table['RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopBase']['meta_info']
_meta_table['RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopBase.LogicalTunnel']['meta_info'].parent =_meta_table['RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopBase']['meta_info']
_meta_table['RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopChain.NexthopList']['meta_info'].parent =_meta_table['RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopChain']['meta_info']
_meta_table['RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopReplicates.NexthopList']['meta_info'].parent =_meta_table['RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopReplicates']['meta_info']
_meta_table['RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopProtection.NexthopList']['meta_info'].parent =_meta_table['RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopProtection']['meta_info']
_meta_table['RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopLb.NexthopList']['meta_info'].parent =_meta_table['RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopLb']['meta_info']
_meta_table['RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopBase']['meta_info'].parent =_meta_table['RouteAddRpc.Input.Routes.RouteList.Nexthop']['meta_info']
_meta_table['RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopChain']['meta_info'].parent =_meta_table['RouteAddRpc.Input.Routes.RouteList.Nexthop']['meta_info']
_meta_table['RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopReplicates']['meta_info'].parent =_meta_table['RouteAddRpc.Input.Routes.RouteList.Nexthop']['meta_info']
_meta_table['RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopProtection']['meta_info'].parent =_meta_table['RouteAddRpc.Input.Routes.RouteList.Nexthop']['meta_info']
_meta_table['RouteAddRpc.Input.Routes.RouteList.Nexthop.NexthopLb']['meta_info'].parent =_meta_table['RouteAddRpc.Input.Routes.RouteList.Nexthop']['meta_info']
_meta_table['RouteAddRpc.Input.Routes.RouteList.Match']['meta_info'].parent =_meta_table['RouteAddRpc.Input.Routes.RouteList']['meta_info']
_meta_table['RouteAddRpc.Input.Routes.RouteList.RouteAttributes']['meta_info'].parent =_meta_table['RouteAddRpc.Input.Routes.RouteList']['meta_info']
_meta_table['RouteAddRpc.Input.Routes.RouteList.RouteVendorAttributes']['meta_info'].parent =_meta_table['RouteAddRpc.Input.Routes.RouteList']['meta_info']
_meta_table['RouteAddRpc.Input.Routes.RouteList.Nexthop']['meta_info'].parent =_meta_table['RouteAddRpc.Input.Routes.RouteList']['meta_info']
_meta_table['RouteAddRpc.Input.Routes.RouteList']['meta_info'].parent =_meta_table['RouteAddRpc.Input.Routes']['meta_info']
_meta_table['RouteAddRpc.Input.Routes']['meta_info'].parent =_meta_table['RouteAddRpc.Input']['meta_info']
_meta_table['RouteAddRpc.Output.FailureDetail.FailedRoutes']['meta_info'].parent =_meta_table['RouteAddRpc.Output.FailureDetail']['meta_info']
_meta_table['RouteAddRpc.Output.FailureDetail']['meta_info'].parent =_meta_table['RouteAddRpc.Output']['meta_info']
_meta_table['RouteAddRpc.Input']['meta_info'].parent =_meta_table['RouteAddRpc']['meta_info']
_meta_table['RouteAddRpc.Output']['meta_info'].parent =_meta_table['RouteAddRpc']['meta_info']
_meta_table['RouteDeleteRpc.Input.Routes.RouteList.Match.Ipv4.DestSrcIpv4Address']['meta_info'].parent =_meta_table['RouteDeleteRpc.Input.Routes.RouteList.Match.Ipv4']['meta_info']
_meta_table['RouteDeleteRpc.Input.Routes.RouteList.Match.Ipv6.DestSrcIpv6Address']['meta_info'].parent =_meta_table['RouteDeleteRpc.Input.Routes.RouteList.Match.Ipv6']['meta_info']
_meta_table['RouteDeleteRpc.Input.Routes.RouteList.Match.Ipv4']['meta_info'].parent =_meta_table['RouteDeleteRpc.Input.Routes.RouteList.Match']['meta_info']
_meta_table['RouteDeleteRpc.Input.Routes.RouteList.Match.Ipv6']['meta_info'].parent =_meta_table['RouteDeleteRpc.Input.Routes.RouteList.Match']['meta_info']
_meta_table['RouteDeleteRpc.Input.Routes.RouteList.Match']['meta_info'].parent =_meta_table['RouteDeleteRpc.Input.Routes.RouteList']['meta_info']
_meta_table['RouteDeleteRpc.Input.Routes.RouteList']['meta_info'].parent =_meta_table['RouteDeleteRpc.Input.Routes']['meta_info']
_meta_table['RouteDeleteRpc.Input.Routes']['meta_info'].parent =_meta_table['RouteDeleteRpc.Input']['meta_info']
_meta_table['RouteDeleteRpc.Output.FailureDetail.FailedRoutes']['meta_info'].parent =_meta_table['RouteDeleteRpc.Output.FailureDetail']['meta_info']
_meta_table['RouteDeleteRpc.Output.FailureDetail']['meta_info'].parent =_meta_table['RouteDeleteRpc.Output']['meta_info']
_meta_table['RouteDeleteRpc.Input']['meta_info'].parent =_meta_table['RouteDeleteRpc']['meta_info']
_meta_table['RouteDeleteRpc.Output']['meta_info'].parent =_meta_table['RouteDeleteRpc']['meta_info']
_meta_table['RouteUpdateRpc.Input.InputRoutes.RouteList.Match.Ipv4.DestSrcIpv4Address']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.InputRoutes.RouteList.Match.Ipv4']['meta_info']
_meta_table['RouteUpdateRpc.Input.InputRoutes.RouteList.Match.Ipv6.DestSrcIpv6Address']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.InputRoutes.RouteList.Match.Ipv6']['meta_info']
_meta_table['RouteUpdateRpc.Input.InputRoutes.RouteList.Match.Ipv4']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.InputRoutes.RouteList.Match']['meta_info']
_meta_table['RouteUpdateRpc.Input.InputRoutes.RouteList.Match.Ipv6']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.InputRoutes.RouteList.Match']['meta_info']
_meta_table['RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopBase.TunnelEncap.MplsHeader.LabelOperations.LabelPush']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopBase.TunnelEncap.MplsHeader.LabelOperations']['meta_info']
_meta_table['RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopBase.TunnelEncap.MplsHeader.LabelOperations.LabelSwap']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopBase.TunnelEncap.MplsHeader.LabelOperations']['meta_info']
_meta_table['RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopBase.TunnelEncap.MplsHeader.LabelOperations']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopBase.TunnelEncap.MplsHeader']['meta_info']
_meta_table['RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopBase.TunnelEncap.Ipv4Header']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopBase.TunnelEncap']['meta_info']
_meta_table['RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopBase.TunnelEncap.Ipv6Header']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopBase.TunnelEncap']['meta_info']
_meta_table['RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopBase.TunnelEncap.MplsHeader']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopBase.TunnelEncap']['meta_info']
_meta_table['RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopBase.TunnelEncap.GreHeader']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopBase.TunnelEncap']['meta_info']
_meta_table['RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopBase.TunnelEncap.NvgreHeader']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopBase.TunnelEncap']['meta_info']
_meta_table['RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopBase.TunnelEncap.VxlanHeader']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopBase.TunnelEncap']['meta_info']
_meta_table['RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopBase.TunnelDecap.Ipv4Decap']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopBase.TunnelDecap']['meta_info']
_meta_table['RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopBase.TunnelDecap.Ipv6Decap']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopBase.TunnelDecap']['meta_info']
_meta_table['RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopBase.TunnelDecap.LabelPop']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopBase.TunnelDecap']['meta_info']
_meta_table['RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopBase.EgressInterfaceIpv4Address']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopBase']['meta_info']
_meta_table['RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopBase.EgressInterfaceIpv6Address']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopBase']['meta_info']
_meta_table['RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopBase.EgressInterfaceMacAddress']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopBase']['meta_info']
_meta_table['RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopBase.TunnelEncap']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopBase']['meta_info']
_meta_table['RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopBase.TunnelDecap']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopBase']['meta_info']
_meta_table['RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopBase.LogicalTunnel']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopBase']['meta_info']
_meta_table['RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopChain.NexthopList']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopChain']['meta_info']
_meta_table['RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopReplicates.NexthopList']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopReplicates']['meta_info']
_meta_table['RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopProtection.NexthopList']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopProtection']['meta_info']
_meta_table['RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopLb.NexthopList']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopLb']['meta_info']
_meta_table['RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopBase']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop']['meta_info']
_meta_table['RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopChain']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop']['meta_info']
_meta_table['RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopReplicates']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop']['meta_info']
_meta_table['RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopProtection']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop']['meta_info']
_meta_table['RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop.NexthopLb']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop']['meta_info']
_meta_table['RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedRouteAttr.AddressFamilyRouteAttributes']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedRouteAttr']['meta_info']
_meta_table['RouteUpdateRpc.Input.InputRoutes.RouteList.Match']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.InputRoutes.RouteList']['meta_info']
_meta_table['RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedNexthop']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.InputRoutes.RouteList']['meta_info']
_meta_table['RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedRouteAttr']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.InputRoutes.RouteList']['meta_info']
_meta_table['RouteUpdateRpc.Input.InputRoutes.RouteList.UpdatedRouteVendorAttr']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.InputRoutes.RouteList']['meta_info']
_meta_table['RouteUpdateRpc.Input.InputRoutes.RouteList']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.InputRoutes']['meta_info']
_meta_table['RouteUpdateRpc.Input.InputRouteAttributes.AddressFamilyRouteAttributes']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.InputRouteAttributes']['meta_info']
_meta_table['RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopBase.TunnelEncap.MplsHeader.LabelOperations.LabelPush']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopBase.TunnelEncap.MplsHeader.LabelOperations']['meta_info']
_meta_table['RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopBase.TunnelEncap.MplsHeader.LabelOperations.LabelSwap']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopBase.TunnelEncap.MplsHeader.LabelOperations']['meta_info']
_meta_table['RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopBase.TunnelEncap.MplsHeader.LabelOperations']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopBase.TunnelEncap.MplsHeader']['meta_info']
_meta_table['RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopBase.TunnelEncap.Ipv4Header']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopBase.TunnelEncap']['meta_info']
_meta_table['RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopBase.TunnelEncap.Ipv6Header']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopBase.TunnelEncap']['meta_info']
_meta_table['RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopBase.TunnelEncap.MplsHeader']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopBase.TunnelEncap']['meta_info']
_meta_table['RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopBase.TunnelEncap.GreHeader']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopBase.TunnelEncap']['meta_info']
_meta_table['RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopBase.TunnelEncap.NvgreHeader']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopBase.TunnelEncap']['meta_info']
_meta_table['RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopBase.TunnelEncap.VxlanHeader']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopBase.TunnelEncap']['meta_info']
_meta_table['RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopBase.TunnelDecap.Ipv4Decap']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopBase.TunnelDecap']['meta_info']
_meta_table['RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopBase.TunnelDecap.Ipv6Decap']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopBase.TunnelDecap']['meta_info']
_meta_table['RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopBase.TunnelDecap.LabelPop']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopBase.TunnelDecap']['meta_info']
_meta_table['RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopBase.EgressInterfaceIpv4Address']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopBase']['meta_info']
_meta_table['RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopBase.EgressInterfaceIpv6Address']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopBase']['meta_info']
_meta_table['RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopBase.EgressInterfaceMacAddress']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopBase']['meta_info']
_meta_table['RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopBase.TunnelEncap']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopBase']['meta_info']
_meta_table['RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopBase.TunnelDecap']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopBase']['meta_info']
_meta_table['RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopBase.LogicalTunnel']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopBase']['meta_info']
_meta_table['RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopChain.NexthopList']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopChain']['meta_info']
_meta_table['RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopReplicates.NexthopList']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopReplicates']['meta_info']
_meta_table['RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopProtection.NexthopList']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopProtection']['meta_info']
_meta_table['RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopLb.NexthopList']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopLb']['meta_info']
_meta_table['RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopBase']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop']['meta_info']
_meta_table['RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopChain']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop']['meta_info']
_meta_table['RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopReplicates']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop']['meta_info']
_meta_table['RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopProtection']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop']['meta_info']
_meta_table['RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop.NexthopLb']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop']['meta_info']
_meta_table['RouteUpdateRpc.Input.UpdateParametors.UpdatedRouteAttr.AddressFamilyRouteAttributes']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.UpdateParametors.UpdatedRouteAttr']['meta_info']
_meta_table['RouteUpdateRpc.Input.UpdateParametors.UpdatedNexthop']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.UpdateParametors']['meta_info']
_meta_table['RouteUpdateRpc.Input.UpdateParametors.UpdatedRouteAttr']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.UpdateParametors']['meta_info']
_meta_table['RouteUpdateRpc.Input.UpdateParametors.UpdatedRouteVendorAttr']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.UpdateParametors']['meta_info']
_meta_table['RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopBase.TunnelEncap.MplsHeader.LabelOperations.LabelPush']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopBase.TunnelEncap.MplsHeader.LabelOperations']['meta_info']
_meta_table['RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopBase.TunnelEncap.MplsHeader.LabelOperations.LabelSwap']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopBase.TunnelEncap.MplsHeader.LabelOperations']['meta_info']
_meta_table['RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopBase.TunnelEncap.MplsHeader.LabelOperations']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopBase.TunnelEncap.MplsHeader']['meta_info']
_meta_table['RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopBase.TunnelEncap.Ipv4Header']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopBase.TunnelEncap']['meta_info']
_meta_table['RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopBase.TunnelEncap.Ipv6Header']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopBase.TunnelEncap']['meta_info']
_meta_table['RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopBase.TunnelEncap.MplsHeader']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopBase.TunnelEncap']['meta_info']
_meta_table['RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopBase.TunnelEncap.GreHeader']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopBase.TunnelEncap']['meta_info']
_meta_table['RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopBase.TunnelEncap.NvgreHeader']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopBase.TunnelEncap']['meta_info']
_meta_table['RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopBase.TunnelEncap.VxlanHeader']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopBase.TunnelEncap']['meta_info']
_meta_table['RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopBase.TunnelDecap.Ipv4Decap']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopBase.TunnelDecap']['meta_info']
_meta_table['RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopBase.TunnelDecap.Ipv6Decap']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopBase.TunnelDecap']['meta_info']
_meta_table['RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopBase.TunnelDecap.LabelPop']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopBase.TunnelDecap']['meta_info']
_meta_table['RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopBase.EgressInterfaceIpv4Address']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopBase']['meta_info']
_meta_table['RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopBase.EgressInterfaceIpv6Address']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopBase']['meta_info']
_meta_table['RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopBase.EgressInterfaceMacAddress']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopBase']['meta_info']
_meta_table['RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopBase.TunnelEncap']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopBase']['meta_info']
_meta_table['RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopBase.TunnelDecap']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopBase']['meta_info']
_meta_table['RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopBase.LogicalTunnel']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopBase']['meta_info']
_meta_table['RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopChain.NexthopList']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopChain']['meta_info']
_meta_table['RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopReplicates.NexthopList']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopReplicates']['meta_info']
_meta_table['RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopProtection.NexthopList']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopProtection']['meta_info']
_meta_table['RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopLb.NexthopList']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopLb']['meta_info']
_meta_table['RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopBase']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop']['meta_info']
_meta_table['RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopChain']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop']['meta_info']
_meta_table['RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopReplicates']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop']['meta_info']
_meta_table['RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopProtection']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop']['meta_info']
_meta_table['RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop.NexthopLb']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop']['meta_info']
_meta_table['RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedRouteAttr.AddressFamilyRouteAttributes']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedRouteAttr']['meta_info']
_meta_table['RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedNexthop']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.UpdateParametersVendor']['meta_info']
_meta_table['RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedRouteAttr']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.UpdateParametersVendor']['meta_info']
_meta_table['RouteUpdateRpc.Input.UpdateParametersVendor.UpdatedRouteVendorAttr']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.UpdateParametersVendor']['meta_info']
_meta_table['RouteUpdateRpc.Input.InputNexthop.NexthopBase.TunnelEncap.MplsHeader.LabelOperations.LabelPush']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.InputNexthop.NexthopBase.TunnelEncap.MplsHeader.LabelOperations']['meta_info']
_meta_table['RouteUpdateRpc.Input.InputNexthop.NexthopBase.TunnelEncap.MplsHeader.LabelOperations.LabelSwap']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.InputNexthop.NexthopBase.TunnelEncap.MplsHeader.LabelOperations']['meta_info']
_meta_table['RouteUpdateRpc.Input.InputNexthop.NexthopBase.TunnelEncap.MplsHeader.LabelOperations']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.InputNexthop.NexthopBase.TunnelEncap.MplsHeader']['meta_info']
_meta_table['RouteUpdateRpc.Input.InputNexthop.NexthopBase.TunnelEncap.Ipv4Header']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.InputNexthop.NexthopBase.TunnelEncap']['meta_info']
_meta_table['RouteUpdateRpc.Input.InputNexthop.NexthopBase.TunnelEncap.Ipv6Header']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.InputNexthop.NexthopBase.TunnelEncap']['meta_info']
_meta_table['RouteUpdateRpc.Input.InputNexthop.NexthopBase.TunnelEncap.MplsHeader']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.InputNexthop.NexthopBase.TunnelEncap']['meta_info']
_meta_table['RouteUpdateRpc.Input.InputNexthop.NexthopBase.TunnelEncap.GreHeader']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.InputNexthop.NexthopBase.TunnelEncap']['meta_info']
_meta_table['RouteUpdateRpc.Input.InputNexthop.NexthopBase.TunnelEncap.NvgreHeader']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.InputNexthop.NexthopBase.TunnelEncap']['meta_info']
_meta_table['RouteUpdateRpc.Input.InputNexthop.NexthopBase.TunnelEncap.VxlanHeader']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.InputNexthop.NexthopBase.TunnelEncap']['meta_info']
_meta_table['RouteUpdateRpc.Input.InputNexthop.NexthopBase.TunnelDecap.Ipv4Decap']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.InputNexthop.NexthopBase.TunnelDecap']['meta_info']
_meta_table['RouteUpdateRpc.Input.InputNexthop.NexthopBase.TunnelDecap.Ipv6Decap']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.InputNexthop.NexthopBase.TunnelDecap']['meta_info']
_meta_table['RouteUpdateRpc.Input.InputNexthop.NexthopBase.TunnelDecap.LabelPop']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.InputNexthop.NexthopBase.TunnelDecap']['meta_info']
_meta_table['RouteUpdateRpc.Input.InputNexthop.NexthopBase.EgressInterfaceIpv4Address']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.InputNexthop.NexthopBase']['meta_info']
_meta_table['RouteUpdateRpc.Input.InputNexthop.NexthopBase.EgressInterfaceIpv6Address']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.InputNexthop.NexthopBase']['meta_info']
_meta_table['RouteUpdateRpc.Input.InputNexthop.NexthopBase.EgressInterfaceMacAddress']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.InputNexthop.NexthopBase']['meta_info']
_meta_table['RouteUpdateRpc.Input.InputNexthop.NexthopBase.TunnelEncap']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.InputNexthop.NexthopBase']['meta_info']
_meta_table['RouteUpdateRpc.Input.InputNexthop.NexthopBase.TunnelDecap']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.InputNexthop.NexthopBase']['meta_info']
_meta_table['RouteUpdateRpc.Input.InputNexthop.NexthopBase.LogicalTunnel']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.InputNexthop.NexthopBase']['meta_info']
_meta_table['RouteUpdateRpc.Input.InputNexthop.NexthopChain.NexthopList']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.InputNexthop.NexthopChain']['meta_info']
_meta_table['RouteUpdateRpc.Input.InputNexthop.NexthopReplicates.NexthopList']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.InputNexthop.NexthopReplicates']['meta_info']
_meta_table['RouteUpdateRpc.Input.InputNexthop.NexthopProtection.NexthopList']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.InputNexthop.NexthopProtection']['meta_info']
_meta_table['RouteUpdateRpc.Input.InputNexthop.NexthopLb.NexthopList']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.InputNexthop.NexthopLb']['meta_info']
_meta_table['RouteUpdateRpc.Input.InputNexthop.NexthopBase']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.InputNexthop']['meta_info']
_meta_table['RouteUpdateRpc.Input.InputNexthop.NexthopChain']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.InputNexthop']['meta_info']
_meta_table['RouteUpdateRpc.Input.InputNexthop.NexthopReplicates']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.InputNexthop']['meta_info']
_meta_table['RouteUpdateRpc.Input.InputNexthop.NexthopProtection']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.InputNexthop']['meta_info']
_meta_table['RouteUpdateRpc.Input.InputNexthop.NexthopLb']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.InputNexthop']['meta_info']
_meta_table['RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopBase.TunnelEncap.MplsHeader.LabelOperations.LabelPush']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopBase.TunnelEncap.MplsHeader.LabelOperations']['meta_info']
_meta_table['RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopBase.TunnelEncap.MplsHeader.LabelOperations.LabelSwap']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopBase.TunnelEncap.MplsHeader.LabelOperations']['meta_info']
_meta_table['RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopBase.TunnelEncap.MplsHeader.LabelOperations']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopBase.TunnelEncap.MplsHeader']['meta_info']
_meta_table['RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopBase.TunnelEncap.Ipv4Header']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopBase.TunnelEncap']['meta_info']
_meta_table['RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopBase.TunnelEncap.Ipv6Header']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopBase.TunnelEncap']['meta_info']
_meta_table['RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopBase.TunnelEncap.MplsHeader']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopBase.TunnelEncap']['meta_info']
_meta_table['RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopBase.TunnelEncap.GreHeader']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopBase.TunnelEncap']['meta_info']
_meta_table['RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopBase.TunnelEncap.NvgreHeader']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopBase.TunnelEncap']['meta_info']
_meta_table['RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopBase.TunnelEncap.VxlanHeader']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopBase.TunnelEncap']['meta_info']
_meta_table['RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopBase.TunnelDecap.Ipv4Decap']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopBase.TunnelDecap']['meta_info']
_meta_table['RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopBase.TunnelDecap.Ipv6Decap']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopBase.TunnelDecap']['meta_info']
_meta_table['RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopBase.TunnelDecap.LabelPop']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopBase.TunnelDecap']['meta_info']
_meta_table['RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopBase.EgressInterfaceIpv4Address']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopBase']['meta_info']
_meta_table['RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopBase.EgressInterfaceIpv6Address']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopBase']['meta_info']
_meta_table['RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopBase.EgressInterfaceMacAddress']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopBase']['meta_info']
_meta_table['RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopBase.TunnelEncap']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopBase']['meta_info']
_meta_table['RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopBase.TunnelDecap']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopBase']['meta_info']
_meta_table['RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopBase.LogicalTunnel']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopBase']['meta_info']
_meta_table['RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopChain.NexthopList']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopChain']['meta_info']
_meta_table['RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopReplicates.NexthopList']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopReplicates']['meta_info']
_meta_table['RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopProtection.NexthopList']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopProtection']['meta_info']
_meta_table['RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopLb.NexthopList']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopLb']['meta_info']
_meta_table['RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopBase']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop']['meta_info']
_meta_table['RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopChain']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop']['meta_info']
_meta_table['RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopReplicates']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop']['meta_info']
_meta_table['RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopProtection']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop']['meta_info']
_meta_table['RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop.NexthopLb']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop']['meta_info']
_meta_table['RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedRouteAttr.AddressFamilyRouteAttributes']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedRouteAttr']['meta_info']
_meta_table['RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedNexthop']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.UpdateParametersNexthop']['meta_info']
_meta_table['RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedRouteAttr']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.UpdateParametersNexthop']['meta_info']
_meta_table['RouteUpdateRpc.Input.UpdateParametersNexthop.UpdatedRouteVendorAttr']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input.UpdateParametersNexthop']['meta_info']
_meta_table['RouteUpdateRpc.Input.InputRoutes']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input']['meta_info']
_meta_table['RouteUpdateRpc.Input.InputRouteAttributes']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input']['meta_info']
_meta_table['RouteUpdateRpc.Input.UpdateParametors']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input']['meta_info']
_meta_table['RouteUpdateRpc.Input.InputRouteVendorAttributes']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input']['meta_info']
_meta_table['RouteUpdateRpc.Input.UpdateParametersVendor']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input']['meta_info']
_meta_table['RouteUpdateRpc.Input.InputNexthop']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input']['meta_info']
_meta_table['RouteUpdateRpc.Input.UpdateParametersNexthop']['meta_info'].parent =_meta_table['RouteUpdateRpc.Input']['meta_info']
_meta_table['RouteUpdateRpc.Output.FailureDetail.FailedRoutes']['meta_info'].parent =_meta_table['RouteUpdateRpc.Output.FailureDetail']['meta_info']
_meta_table['RouteUpdateRpc.Output.FailureDetail']['meta_info'].parent =_meta_table['RouteUpdateRpc.Output']['meta_info']
_meta_table['RouteUpdateRpc.Input']['meta_info'].parent =_meta_table['RouteUpdateRpc']['meta_info']
_meta_table['RouteUpdateRpc.Output']['meta_info'].parent =_meta_table['RouteUpdateRpc']['meta_info']
_meta_table['NhAddRpc.Input.NexthopBase.TunnelEncap.MplsHeader.LabelOperations.LabelPush']['meta_info'].parent =_meta_table['NhAddRpc.Input.NexthopBase.TunnelEncap.MplsHeader.LabelOperations']['meta_info']
_meta_table['NhAddRpc.Input.NexthopBase.TunnelEncap.MplsHeader.LabelOperations.LabelSwap']['meta_info'].parent =_meta_table['NhAddRpc.Input.NexthopBase.TunnelEncap.MplsHeader.LabelOperations']['meta_info']
_meta_table['NhAddRpc.Input.NexthopBase.TunnelEncap.MplsHeader.LabelOperations']['meta_info'].parent =_meta_table['NhAddRpc.Input.NexthopBase.TunnelEncap.MplsHeader']['meta_info']
_meta_table['NhAddRpc.Input.NexthopBase.TunnelEncap.Ipv4Header']['meta_info'].parent =_meta_table['NhAddRpc.Input.NexthopBase.TunnelEncap']['meta_info']
_meta_table['NhAddRpc.Input.NexthopBase.TunnelEncap.Ipv6Header']['meta_info'].parent =_meta_table['NhAddRpc.Input.NexthopBase.TunnelEncap']['meta_info']
_meta_table['NhAddRpc.Input.NexthopBase.TunnelEncap.MplsHeader']['meta_info'].parent =_meta_table['NhAddRpc.Input.NexthopBase.TunnelEncap']['meta_info']
_meta_table['NhAddRpc.Input.NexthopBase.TunnelEncap.GreHeader']['meta_info'].parent =_meta_table['NhAddRpc.Input.NexthopBase.TunnelEncap']['meta_info']
_meta_table['NhAddRpc.Input.NexthopBase.TunnelEncap.NvgreHeader']['meta_info'].parent =_meta_table['NhAddRpc.Input.NexthopBase.TunnelEncap']['meta_info']
_meta_table['NhAddRpc.Input.NexthopBase.TunnelEncap.VxlanHeader']['meta_info'].parent =_meta_table['NhAddRpc.Input.NexthopBase.TunnelEncap']['meta_info']
_meta_table['NhAddRpc.Input.NexthopBase.TunnelDecap.Ipv4Decap']['meta_info'].parent =_meta_table['NhAddRpc.Input.NexthopBase.TunnelDecap']['meta_info']
_meta_table['NhAddRpc.Input.NexthopBase.TunnelDecap.Ipv6Decap']['meta_info'].parent =_meta_table['NhAddRpc.Input.NexthopBase.TunnelDecap']['meta_info']
_meta_table['NhAddRpc.Input.NexthopBase.TunnelDecap.LabelPop']['meta_info'].parent =_meta_table['NhAddRpc.Input.NexthopBase.TunnelDecap']['meta_info']
_meta_table['NhAddRpc.Input.NexthopBase.EgressInterfaceIpv4Address']['meta_info'].parent =_meta_table['NhAddRpc.Input.NexthopBase']['meta_info']
_meta_table['NhAddRpc.Input.NexthopBase.EgressInterfaceIpv6Address']['meta_info'].parent =_meta_table['NhAddRpc.Input.NexthopBase']['meta_info']
_meta_table['NhAddRpc.Input.NexthopBase.EgressInterfaceMacAddress']['meta_info'].parent =_meta_table['NhAddRpc.Input.NexthopBase']['meta_info']
_meta_table['NhAddRpc.Input.NexthopBase.TunnelEncap']['meta_info'].parent =_meta_table['NhAddRpc.Input.NexthopBase']['meta_info']
_meta_table['NhAddRpc.Input.NexthopBase.TunnelDecap']['meta_info'].parent =_meta_table['NhAddRpc.Input.NexthopBase']['meta_info']
_meta_table['NhAddRpc.Input.NexthopBase.LogicalTunnel']['meta_info'].parent =_meta_table['NhAddRpc.Input.NexthopBase']['meta_info']
_meta_table['NhAddRpc.Input.NexthopChain.NexthopList']['meta_info'].parent =_meta_table['NhAddRpc.Input.NexthopChain']['meta_info']
_meta_table['NhAddRpc.Input.NexthopReplicates.NexthopList']['meta_info'].parent =_meta_table['NhAddRpc.Input.NexthopReplicates']['meta_info']
_meta_table['NhAddRpc.Input.NexthopProtection.NexthopList']['meta_info'].parent =_meta_table['NhAddRpc.Input.NexthopProtection']['meta_info']
_meta_table['NhAddRpc.Input.NexthopLb.NexthopList']['meta_info'].parent =_meta_table['NhAddRpc.Input.NexthopLb']['meta_info']
_meta_table['NhAddRpc.Input.NexthopBase']['meta_info'].parent =_meta_table['NhAddRpc.Input']['meta_info']
_meta_table['NhAddRpc.Input.NexthopChain']['meta_info'].parent =_meta_table['NhAddRpc.Input']['meta_info']
_meta_table['NhAddRpc.Input.NexthopReplicates']['meta_info'].parent =_meta_table['NhAddRpc.Input']['meta_info']
_meta_table['NhAddRpc.Input.NexthopProtection']['meta_info'].parent =_meta_table['NhAddRpc.Input']['meta_info']
_meta_table['NhAddRpc.Input.NexthopLb']['meta_info'].parent =_meta_table['NhAddRpc.Input']['meta_info']
_meta_table['NhAddRpc.Input']['meta_info'].parent =_meta_table['NhAddRpc']['meta_info']
_meta_table['NhAddRpc.Output']['meta_info'].parent =_meta_table['NhAddRpc']['meta_info']
_meta_table['NhDeleteRpc.Input.NexthopBase.TunnelEncap.MplsHeader.LabelOperations.LabelPush']['meta_info'].parent =_meta_table['NhDeleteRpc.Input.NexthopBase.TunnelEncap.MplsHeader.LabelOperations']['meta_info']
_meta_table['NhDeleteRpc.Input.NexthopBase.TunnelEncap.MplsHeader.LabelOperations.LabelSwap']['meta_info'].parent =_meta_table['NhDeleteRpc.Input.NexthopBase.TunnelEncap.MplsHeader.LabelOperations']['meta_info']
_meta_table['NhDeleteRpc.Input.NexthopBase.TunnelEncap.MplsHeader.LabelOperations']['meta_info'].parent =_meta_table['NhDeleteRpc.Input.NexthopBase.TunnelEncap.MplsHeader']['meta_info']
_meta_table['NhDeleteRpc.Input.NexthopBase.TunnelEncap.Ipv4Header']['meta_info'].parent =_meta_table['NhDeleteRpc.Input.NexthopBase.TunnelEncap']['meta_info']
_meta_table['NhDeleteRpc.Input.NexthopBase.TunnelEncap.Ipv6Header']['meta_info'].parent =_meta_table['NhDeleteRpc.Input.NexthopBase.TunnelEncap']['meta_info']
_meta_table['NhDeleteRpc.Input.NexthopBase.TunnelEncap.MplsHeader']['meta_info'].parent =_meta_table['NhDeleteRpc.Input.NexthopBase.TunnelEncap']['meta_info']
_meta_table['NhDeleteRpc.Input.NexthopBase.TunnelEncap.GreHeader']['meta_info'].parent =_meta_table['NhDeleteRpc.Input.NexthopBase.TunnelEncap']['meta_info']
_meta_table['NhDeleteRpc.Input.NexthopBase.TunnelEncap.NvgreHeader']['meta_info'].parent =_meta_table['NhDeleteRpc.Input.NexthopBase.TunnelEncap']['meta_info']
_meta_table['NhDeleteRpc.Input.NexthopBase.TunnelEncap.VxlanHeader']['meta_info'].parent =_meta_table['NhDeleteRpc.Input.NexthopBase.TunnelEncap']['meta_info']
_meta_table['NhDeleteRpc.Input.NexthopBase.TunnelDecap.Ipv4Decap']['meta_info'].parent =_meta_table['NhDeleteRpc.Input.NexthopBase.TunnelDecap']['meta_info']
_meta_table['NhDeleteRpc.Input.NexthopBase.TunnelDecap.Ipv6Decap']['meta_info'].parent =_meta_table['NhDeleteRpc.Input.NexthopBase.TunnelDecap']['meta_info']
_meta_table['NhDeleteRpc.Input.NexthopBase.TunnelDecap.LabelPop']['meta_info'].parent =_meta_table['NhDeleteRpc.Input.NexthopBase.TunnelDecap']['meta_info']
_meta_table['NhDeleteRpc.Input.NexthopBase.EgressInterfaceIpv4Address']['meta_info'].parent =_meta_table['NhDeleteRpc.Input.NexthopBase']['meta_info']
_meta_table['NhDeleteRpc.Input.NexthopBase.EgressInterfaceIpv6Address']['meta_info'].parent =_meta_table['NhDeleteRpc.Input.NexthopBase']['meta_info']
_meta_table['NhDeleteRpc.Input.NexthopBase.EgressInterfaceMacAddress']['meta_info'].parent =_meta_table['NhDeleteRpc.Input.NexthopBase']['meta_info']
_meta_table['NhDeleteRpc.Input.NexthopBase.TunnelEncap']['meta_info'].parent =_meta_table['NhDeleteRpc.Input.NexthopBase']['meta_info']
_meta_table['NhDeleteRpc.Input.NexthopBase.TunnelDecap']['meta_info'].parent =_meta_table['NhDeleteRpc.Input.NexthopBase']['meta_info']
_meta_table['NhDeleteRpc.Input.NexthopBase.LogicalTunnel']['meta_info'].parent =_meta_table['NhDeleteRpc.Input.NexthopBase']['meta_info']
_meta_table['NhDeleteRpc.Input.NexthopChain.NexthopList']['meta_info'].parent =_meta_table['NhDeleteRpc.Input.NexthopChain']['meta_info']
_meta_table['NhDeleteRpc.Input.NexthopReplicates.NexthopList']['meta_info'].parent =_meta_table['NhDeleteRpc.Input.NexthopReplicates']['meta_info']
_meta_table['NhDeleteRpc.Input.NexthopProtection.NexthopList']['meta_info'].parent =_meta_table['NhDeleteRpc.Input.NexthopProtection']['meta_info']
_meta_table['NhDeleteRpc.Input.NexthopLb.NexthopList']['meta_info'].parent =_meta_table['NhDeleteRpc.Input.NexthopLb']['meta_info']
_meta_table['NhDeleteRpc.Input.NexthopBase']['meta_info'].parent =_meta_table['NhDeleteRpc.Input']['meta_info']
_meta_table['NhDeleteRpc.Input.NexthopChain']['meta_info'].parent =_meta_table['NhDeleteRpc.Input']['meta_info']
_meta_table['NhDeleteRpc.Input.NexthopReplicates']['meta_info'].parent =_meta_table['NhDeleteRpc.Input']['meta_info']
_meta_table['NhDeleteRpc.Input.NexthopProtection']['meta_info'].parent =_meta_table['NhDeleteRpc.Input']['meta_info']
_meta_table['NhDeleteRpc.Input.NexthopLb']['meta_info'].parent =_meta_table['NhDeleteRpc.Input']['meta_info']
_meta_table['NhDeleteRpc.Input']['meta_info'].parent =_meta_table['NhDeleteRpc']['meta_info']
_meta_table['NhDeleteRpc.Output']['meta_info'].parent =_meta_table['NhDeleteRpc']['meta_info']
