


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'BgpOcAfiEnum' : _MetaInfoEnum('BgpOcAfiEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper',
        {
            'ipv4':'ipv4',
            'ipv6':'ipv6',
        }, 'Cisco-IOS-XR-ipv4-bgp-oc-oper', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper']),
    'BgpOcOriginAttrEnum' : _MetaInfoEnum('BgpOcOriginAttrEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper',
        {
            'igp':'igp',
            'egp':'egp',
            'incomplete':'incomplete',
        }, 'Cisco-IOS-XR-ipv4-bgp-oc-oper', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper']),
    'BgpOcInvalidRouteReasonEnum' : _MetaInfoEnum('BgpOcInvalidRouteReasonEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper',
        {
            'valid-route':'valid_route',
            'invalid-clsuter-loop':'invalid_clsuter_loop',
            'invalid-as-path-loop':'invalid_as_path_loop',
            'invalid-origin-at-or-id':'invalid_origin_at_or_id',
            'invalid-as-confed-loop':'invalid_as_confed_loop',
        }, 'Cisco-IOS-XR-ipv4-bgp-oc-oper', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper']),
    'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.PrefixName.Prefix' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.PrefixName.Prefix',
            False, 
            [
            _MetaInfoClassMember('afi', REFERENCE_ENUM_CLASS, 'BgpOcAfiEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'BgpOcAfiEnum', 
                [], [], 
                '''                AFI
                ''',
                'afi',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 Addr
                ''',
                'ipv4_address',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 Addr
                ''',
                'ipv6_address',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.PrefixName' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.PrefixName',
            False, 
            [
            _MetaInfoClassMember('prefix', REFERENCE_CLASS, 'Prefix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.PrefixName.Prefix', 
                [], [], 
                '''                Prefix
                ''',
                'prefix',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Prefix length
                ''',
                'prefix_length',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'prefix-name',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.RouteAttrList.NextHop' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.RouteAttrList.NextHop',
            False, 
            [
            _MetaInfoClassMember('afi', REFERENCE_ENUM_CLASS, 'BgpOcAfiEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'BgpOcAfiEnum', 
                [], [], 
                '''                AFI
                ''',
                'afi',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 Addr
                ''',
                'ipv4_address',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 Addr
                ''',
                'ipv6_address',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'next-hop',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.RouteAttrList.AggregratorAttributes' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.RouteAttrList.AggregratorAttributes',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address
                ''',
                'address',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('as4', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                AS4 number
                ''',
                'as4',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('as', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                AS number
                ''',
                'as_',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'aggregrator-attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.RouteAttrList.Community' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.RouteAttrList.Community',
            False, 
            [
            _MetaInfoClassMember('objects', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                BGP OC objects
                ''',
                'objects',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'community',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.RouteAttrList' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.RouteAttrList',
            False, 
            [
            _MetaInfoClassMember('aggregrator-attributes', REFERENCE_CLASS, 'AggregratorAttributes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.RouteAttrList.AggregratorAttributes', 
                [], [], 
                '''                AggregatorList
                ''',
                'aggregrator_attributes',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('as4-path', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                AS4 Path
                ''',
                'as4_path',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('as-path', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                AS Path
                ''',
                'as_path',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('atomic-aggr', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                AtomicAggr
                ''',
                'atomic_aggr',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('community', REFERENCE_LIST, 'Community' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.RouteAttrList.Community', 
                [], [], 
                '''                CommunityArray
                ''',
                'community',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('local-pref', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LocalPref
                ''',
                'local_pref',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('med', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Med
                ''',
                'med',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('next-hop', REFERENCE_CLASS, 'NextHop' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.RouteAttrList.NextHop', 
                [], [], 
                '''                NextHopAddress
                ''',
                'next_hop',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('origin-type', REFERENCE_ENUM_CLASS, 'BgpOcOriginAttrEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'BgpOcOriginAttrEnum', 
                [], [], 
                '''                Origin Attribute Type
                ''',
                'origin_type',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'route-attr-list',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.ExtAttributesList.ExtCommunity' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.ExtAttributesList.ExtCommunity',
            False, 
            [
            _MetaInfoClassMember('objects', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                BGP OC objects
                ''',
                'objects',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'ext-community',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.ExtAttributesList.UnknownAttributes' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.ExtAttributesList.UnknownAttributes',
            False, 
            [
            _MetaInfoClassMember('attribute-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                AttributeLength
                ''',
                'attribute_length',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('attribute-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                AttributeType
                ''',
                'attribute_type',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('attribute-value', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Atributevalue
                ''',
                'attribute_value',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'unknown-attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.ExtAttributesList' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.ExtAttributesList',
            False, 
            [
            _MetaInfoClassMember('aigp', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                AIGP
                ''',
                'aigp',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('cluster', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                ClusterList
                ''',
                'cluster',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('ext-community', REFERENCE_LIST, 'ExtCommunity' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.ExtAttributesList.ExtCommunity', 
                [], [], 
                '''                ExtendedCommunityArray
                ''',
                'ext_community',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('originator-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                OriginatorID
                ''',
                'originator_id',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('path-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                PathId
                ''',
                'path_id',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('unknown-attributes', REFERENCE_LIST, 'UnknownAttributes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.ExtAttributesList.UnknownAttributes', 
                [], [], 
                '''                UnknownAttributes
                ''',
                'unknown_attributes',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'ext-attributes-list',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.LastModifiedDate' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.LastModifiedDate',
            False, 
            [
            _MetaInfoClassMember('time-value', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                TimeValue
                ''',
                'time_value',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'last-modified-date',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.LastUpdateRecieved' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.LastUpdateRecieved',
            False, 
            [
            _MetaInfoClassMember('time-value', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                TimeValue
                ''',
                'time_value',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'last-update-recieved',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route',
            False, 
            [
            _MetaInfoClassMember('best-path', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                BestPath
                ''',
                'best_path',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('ext-attributes-list', REFERENCE_CLASS, 'ExtAttributesList' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.ExtAttributesList', 
                [], [], 
                '''                ExtAttributesList
                ''',
                'ext_attributes_list',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('invalid-reason', REFERENCE_ENUM_CLASS, 'BgpOcInvalidRouteReasonEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'BgpOcInvalidRouteReasonEnum', 
                [], [], 
                '''                IndentityRef
                ''',
                'invalid_reason',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('last-modified-date', REFERENCE_CLASS, 'LastModifiedDate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.LastModifiedDate', 
                [], [], 
                '''                LastModifiedDate
                ''',
                'last_modified_date',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('last-update-recieved', REFERENCE_CLASS, 'LastUpdateRecieved' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.LastUpdateRecieved', 
                [], [], 
                '''                LastUpdateRecieved
                ''',
                'last_update_recieved',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('neighbor-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Neighbor address
                ''',
                'neighbor_address',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False, [
                    _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Neighbor address
                        ''',
                        'neighbor_address',
                        'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
                    _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Neighbor address
                        ''',
                        'neighbor_address',
                        'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
                ]),
            _MetaInfoClassMember('path-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Path ID
                ''',
                'path_id',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('prefix-name', REFERENCE_CLASS, 'PrefixName' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.PrefixName', 
                [], [], 
                '''                Prefix
                ''',
                'prefix_name',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('route', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Network in prefix/length format
                ''',
                'route',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False, [
                    _MetaInfoClassMember('route', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                        '''                        Network in prefix/length format
                        ''',
                        'route',
                        'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
                    _MetaInfoClassMember('route', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                        '''                        Network in prefix/length format
                        ''',
                        'route',
                        'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
                ]),
            _MetaInfoClassMember('route-attr-list', REFERENCE_CLASS, 'RouteAttrList' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.RouteAttrList', 
                [], [], 
                '''                RouteAttributesList
                ''',
                'route_attr_list',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('valid-route', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                ValidRoute
                ''',
                'valid_route',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'route',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes',
            False, 
            [
            _MetaInfoClassMember('route', REFERENCE_LIST, 'Route' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route', 
                [], [], 
                '''                route entry
                ''',
                'route',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'routes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.NumRoutes' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.NumRoutes',
            False, 
            [
            _MetaInfoClassMember('num-routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                NumRoutes
                ''',
                'num_routes',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'num-routes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib',
            False, 
            [
            _MetaInfoClassMember('num-routes', REFERENCE_CLASS, 'NumRoutes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.NumRoutes', 
                [], [], 
                '''                Number of routes in adjacency rib out-bound
                post-policy table
                ''',
                'num_routes',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('routes', REFERENCE_CLASS, 'Routes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes', 
                [], [], 
                '''                routes table
                ''',
                'routes',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'loc-rib',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.PrefixName.Prefix' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.PrefixName.Prefix',
            False, 
            [
            _MetaInfoClassMember('afi', REFERENCE_ENUM_CLASS, 'BgpOcAfiEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'BgpOcAfiEnum', 
                [], [], 
                '''                AFI
                ''',
                'afi',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 Addr
                ''',
                'ipv4_address',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 Addr
                ''',
                'ipv6_address',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.PrefixName' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.PrefixName',
            False, 
            [
            _MetaInfoClassMember('prefix', REFERENCE_CLASS, 'Prefix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.PrefixName.Prefix', 
                [], [], 
                '''                Prefix
                ''',
                'prefix',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Prefix length
                ''',
                'prefix_length',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'prefix-name',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.RouteAttrList.NextHop' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.RouteAttrList.NextHop',
            False, 
            [
            _MetaInfoClassMember('afi', REFERENCE_ENUM_CLASS, 'BgpOcAfiEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'BgpOcAfiEnum', 
                [], [], 
                '''                AFI
                ''',
                'afi',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 Addr
                ''',
                'ipv4_address',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 Addr
                ''',
                'ipv6_address',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'next-hop',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.RouteAttrList.AggregratorAttributes' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.RouteAttrList.AggregratorAttributes',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address
                ''',
                'address',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('as4', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                AS4 number
                ''',
                'as4',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('as', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                AS number
                ''',
                'as_',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'aggregrator-attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.RouteAttrList.Community' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.RouteAttrList.Community',
            False, 
            [
            _MetaInfoClassMember('objects', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                BGP OC objects
                ''',
                'objects',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'community',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.RouteAttrList' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.RouteAttrList',
            False, 
            [
            _MetaInfoClassMember('aggregrator-attributes', REFERENCE_CLASS, 'AggregratorAttributes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.RouteAttrList.AggregratorAttributes', 
                [], [], 
                '''                AggregatorList
                ''',
                'aggregrator_attributes',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('as4-path', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                AS4 Path
                ''',
                'as4_path',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('as-path', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                AS Path
                ''',
                'as_path',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('atomic-aggr', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                AtomicAggr
                ''',
                'atomic_aggr',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('community', REFERENCE_LIST, 'Community' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.RouteAttrList.Community', 
                [], [], 
                '''                CommunityArray
                ''',
                'community',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('local-pref', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LocalPref
                ''',
                'local_pref',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('med', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Med
                ''',
                'med',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('next-hop', REFERENCE_CLASS, 'NextHop' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.RouteAttrList.NextHop', 
                [], [], 
                '''                NextHopAddress
                ''',
                'next_hop',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('origin-type', REFERENCE_ENUM_CLASS, 'BgpOcOriginAttrEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'BgpOcOriginAttrEnum', 
                [], [], 
                '''                Origin Attribute Type
                ''',
                'origin_type',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'route-attr-list',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.ExtAttributesList.ExtCommunity' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.ExtAttributesList.ExtCommunity',
            False, 
            [
            _MetaInfoClassMember('objects', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                BGP OC objects
                ''',
                'objects',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'ext-community',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.ExtAttributesList.UnknownAttributes' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.ExtAttributesList.UnknownAttributes',
            False, 
            [
            _MetaInfoClassMember('attribute-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                AttributeLength
                ''',
                'attribute_length',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('attribute-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                AttributeType
                ''',
                'attribute_type',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('attribute-value', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Atributevalue
                ''',
                'attribute_value',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'unknown-attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.ExtAttributesList' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.ExtAttributesList',
            False, 
            [
            _MetaInfoClassMember('aigp', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                AIGP
                ''',
                'aigp',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('cluster', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                ClusterList
                ''',
                'cluster',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('ext-community', REFERENCE_LIST, 'ExtCommunity' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.ExtAttributesList.ExtCommunity', 
                [], [], 
                '''                ExtendedCommunityArray
                ''',
                'ext_community',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('originator-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                OriginatorID
                ''',
                'originator_id',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('path-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                PathId
                ''',
                'path_id',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('unknown-attributes', REFERENCE_LIST, 'UnknownAttributes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.ExtAttributesList.UnknownAttributes', 
                [], [], 
                '''                UnknownAttributes
                ''',
                'unknown_attributes',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'ext-attributes-list',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.LastModifiedDate' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.LastModifiedDate',
            False, 
            [
            _MetaInfoClassMember('time-value', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                TimeValue
                ''',
                'time_value',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'last-modified-date',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.LastUpdateRecieved' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.LastUpdateRecieved',
            False, 
            [
            _MetaInfoClassMember('time-value', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                TimeValue
                ''',
                'time_value',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'last-update-recieved',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route',
            False, 
            [
            _MetaInfoClassMember('best-path', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                BestPath
                ''',
                'best_path',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('ext-attributes-list', REFERENCE_CLASS, 'ExtAttributesList' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.ExtAttributesList', 
                [], [], 
                '''                ExtAttributesList
                ''',
                'ext_attributes_list',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('invalid-reason', REFERENCE_ENUM_CLASS, 'BgpOcInvalidRouteReasonEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'BgpOcInvalidRouteReasonEnum', 
                [], [], 
                '''                IndentityRef
                ''',
                'invalid_reason',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('last-modified-date', REFERENCE_CLASS, 'LastModifiedDate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.LastModifiedDate', 
                [], [], 
                '''                LastModifiedDate
                ''',
                'last_modified_date',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('last-update-recieved', REFERENCE_CLASS, 'LastUpdateRecieved' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.LastUpdateRecieved', 
                [], [], 
                '''                LastUpdateRecieved
                ''',
                'last_update_recieved',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('neighbor-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Neighbor address
                ''',
                'neighbor_address',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False, [
                    _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Neighbor address
                        ''',
                        'neighbor_address',
                        'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
                    _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Neighbor address
                        ''',
                        'neighbor_address',
                        'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
                ]),
            _MetaInfoClassMember('path-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Path ID
                ''',
                'path_id',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('prefix-name', REFERENCE_CLASS, 'PrefixName' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.PrefixName', 
                [], [], 
                '''                Prefix
                ''',
                'prefix_name',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('route', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Network in prefix/length format
                ''',
                'route',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False, [
                    _MetaInfoClassMember('route', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                        '''                        Network in prefix/length format
                        ''',
                        'route',
                        'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
                    _MetaInfoClassMember('route', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                        '''                        Network in prefix/length format
                        ''',
                        'route',
                        'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
                ]),
            _MetaInfoClassMember('route-attr-list', REFERENCE_CLASS, 'RouteAttrList' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.RouteAttrList', 
                [], [], 
                '''                RouteAttributesList
                ''',
                'route_attr_list',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('valid-route', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                ValidRoute
                ''',
                'valid_route',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'route',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes',
            False, 
            [
            _MetaInfoClassMember('route', REFERENCE_LIST, 'Route' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route', 
                [], [], 
                '''                route entry
                ''',
                'route',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'routes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.NumRoutes' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.NumRoutes',
            False, 
            [
            _MetaInfoClassMember('num-routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                NumRoutes
                ''',
                'num_routes',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'num-routes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost',
            False, 
            [
            _MetaInfoClassMember('num-routes', REFERENCE_CLASS, 'NumRoutes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.NumRoutes', 
                [], [], 
                '''                Number of routes in adjacency rib out-bound
                post-policy table
                ''',
                'num_routes',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('routes', REFERENCE_CLASS, 'Routes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes', 
                [], [], 
                '''                routes table
                ''',
                'routes',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'adj-rib-in-post',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.PrefixName.Prefix' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.PrefixName.Prefix',
            False, 
            [
            _MetaInfoClassMember('afi', REFERENCE_ENUM_CLASS, 'BgpOcAfiEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'BgpOcAfiEnum', 
                [], [], 
                '''                AFI
                ''',
                'afi',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 Addr
                ''',
                'ipv4_address',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 Addr
                ''',
                'ipv6_address',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.PrefixName' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.PrefixName',
            False, 
            [
            _MetaInfoClassMember('prefix', REFERENCE_CLASS, 'Prefix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.PrefixName.Prefix', 
                [], [], 
                '''                Prefix
                ''',
                'prefix',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Prefix length
                ''',
                'prefix_length',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'prefix-name',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.RouteAttrList.NextHop' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.RouteAttrList.NextHop',
            False, 
            [
            _MetaInfoClassMember('afi', REFERENCE_ENUM_CLASS, 'BgpOcAfiEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'BgpOcAfiEnum', 
                [], [], 
                '''                AFI
                ''',
                'afi',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 Addr
                ''',
                'ipv4_address',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 Addr
                ''',
                'ipv6_address',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'next-hop',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.RouteAttrList.AggregratorAttributes' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.RouteAttrList.AggregratorAttributes',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address
                ''',
                'address',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('as4', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                AS4 number
                ''',
                'as4',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('as', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                AS number
                ''',
                'as_',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'aggregrator-attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.RouteAttrList.Community' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.RouteAttrList.Community',
            False, 
            [
            _MetaInfoClassMember('objects', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                BGP OC objects
                ''',
                'objects',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'community',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.RouteAttrList' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.RouteAttrList',
            False, 
            [
            _MetaInfoClassMember('aggregrator-attributes', REFERENCE_CLASS, 'AggregratorAttributes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.RouteAttrList.AggregratorAttributes', 
                [], [], 
                '''                AggregatorList
                ''',
                'aggregrator_attributes',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('as4-path', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                AS4 Path
                ''',
                'as4_path',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('as-path', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                AS Path
                ''',
                'as_path',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('atomic-aggr', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                AtomicAggr
                ''',
                'atomic_aggr',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('community', REFERENCE_LIST, 'Community' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.RouteAttrList.Community', 
                [], [], 
                '''                CommunityArray
                ''',
                'community',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('local-pref', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LocalPref
                ''',
                'local_pref',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('med', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Med
                ''',
                'med',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('next-hop', REFERENCE_CLASS, 'NextHop' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.RouteAttrList.NextHop', 
                [], [], 
                '''                NextHopAddress
                ''',
                'next_hop',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('origin-type', REFERENCE_ENUM_CLASS, 'BgpOcOriginAttrEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'BgpOcOriginAttrEnum', 
                [], [], 
                '''                Origin Attribute Type
                ''',
                'origin_type',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'route-attr-list',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.ExtAttributesList.ExtCommunity' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.ExtAttributesList.ExtCommunity',
            False, 
            [
            _MetaInfoClassMember('objects', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                BGP OC objects
                ''',
                'objects',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'ext-community',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.ExtAttributesList.UnknownAttributes' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.ExtAttributesList.UnknownAttributes',
            False, 
            [
            _MetaInfoClassMember('attribute-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                AttributeLength
                ''',
                'attribute_length',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('attribute-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                AttributeType
                ''',
                'attribute_type',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('attribute-value', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Atributevalue
                ''',
                'attribute_value',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'unknown-attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.ExtAttributesList' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.ExtAttributesList',
            False, 
            [
            _MetaInfoClassMember('aigp', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                AIGP
                ''',
                'aigp',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('cluster', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                ClusterList
                ''',
                'cluster',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('ext-community', REFERENCE_LIST, 'ExtCommunity' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.ExtAttributesList.ExtCommunity', 
                [], [], 
                '''                ExtendedCommunityArray
                ''',
                'ext_community',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('originator-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                OriginatorID
                ''',
                'originator_id',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('path-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                PathId
                ''',
                'path_id',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('unknown-attributes', REFERENCE_LIST, 'UnknownAttributes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.ExtAttributesList.UnknownAttributes', 
                [], [], 
                '''                UnknownAttributes
                ''',
                'unknown_attributes',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'ext-attributes-list',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.LastModifiedDate' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.LastModifiedDate',
            False, 
            [
            _MetaInfoClassMember('time-value', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                TimeValue
                ''',
                'time_value',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'last-modified-date',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.LastUpdateRecieved' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.LastUpdateRecieved',
            False, 
            [
            _MetaInfoClassMember('time-value', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                TimeValue
                ''',
                'time_value',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'last-update-recieved',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route',
            False, 
            [
            _MetaInfoClassMember('best-path', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                BestPath
                ''',
                'best_path',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('ext-attributes-list', REFERENCE_CLASS, 'ExtAttributesList' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.ExtAttributesList', 
                [], [], 
                '''                ExtAttributesList
                ''',
                'ext_attributes_list',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('invalid-reason', REFERENCE_ENUM_CLASS, 'BgpOcInvalidRouteReasonEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'BgpOcInvalidRouteReasonEnum', 
                [], [], 
                '''                IndentityRef
                ''',
                'invalid_reason',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('last-modified-date', REFERENCE_CLASS, 'LastModifiedDate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.LastModifiedDate', 
                [], [], 
                '''                LastModifiedDate
                ''',
                'last_modified_date',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('last-update-recieved', REFERENCE_CLASS, 'LastUpdateRecieved' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.LastUpdateRecieved', 
                [], [], 
                '''                LastUpdateRecieved
                ''',
                'last_update_recieved',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('neighbor-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Neighbor address
                ''',
                'neighbor_address',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False, [
                    _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Neighbor address
                        ''',
                        'neighbor_address',
                        'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
                    _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Neighbor address
                        ''',
                        'neighbor_address',
                        'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
                ]),
            _MetaInfoClassMember('path-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Path ID
                ''',
                'path_id',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('prefix-name', REFERENCE_CLASS, 'PrefixName' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.PrefixName', 
                [], [], 
                '''                Prefix
                ''',
                'prefix_name',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('route', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Network in prefix/length format
                ''',
                'route',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False, [
                    _MetaInfoClassMember('route', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                        '''                        Network in prefix/length format
                        ''',
                        'route',
                        'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
                    _MetaInfoClassMember('route', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                        '''                        Network in prefix/length format
                        ''',
                        'route',
                        'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
                ]),
            _MetaInfoClassMember('route-attr-list', REFERENCE_CLASS, 'RouteAttrList' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.RouteAttrList', 
                [], [], 
                '''                RouteAttributesList
                ''',
                'route_attr_list',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('valid-route', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                ValidRoute
                ''',
                'valid_route',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'route',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes',
            False, 
            [
            _MetaInfoClassMember('route', REFERENCE_LIST, 'Route' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route', 
                [], [], 
                '''                route entry
                ''',
                'route',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'routes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.NumRoutes' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.NumRoutes',
            False, 
            [
            _MetaInfoClassMember('num-routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                NumRoutes
                ''',
                'num_routes',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'num-routes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost',
            False, 
            [
            _MetaInfoClassMember('num-routes', REFERENCE_CLASS, 'NumRoutes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.NumRoutes', 
                [], [], 
                '''                Number of routes in adjacency rib out-bound
                post-policy table
                ''',
                'num_routes',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('routes', REFERENCE_CLASS, 'Routes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes', 
                [], [], 
                '''                routes table
                ''',
                'routes',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'adj-rib-out-post',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.PrefixName.Prefix' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.PrefixName.Prefix',
            False, 
            [
            _MetaInfoClassMember('afi', REFERENCE_ENUM_CLASS, 'BgpOcAfiEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'BgpOcAfiEnum', 
                [], [], 
                '''                AFI
                ''',
                'afi',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 Addr
                ''',
                'ipv4_address',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 Addr
                ''',
                'ipv6_address',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.PrefixName' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.PrefixName',
            False, 
            [
            _MetaInfoClassMember('prefix', REFERENCE_CLASS, 'Prefix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.PrefixName.Prefix', 
                [], [], 
                '''                Prefix
                ''',
                'prefix',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Prefix length
                ''',
                'prefix_length',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'prefix-name',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.RouteAttrList.NextHop' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.RouteAttrList.NextHop',
            False, 
            [
            _MetaInfoClassMember('afi', REFERENCE_ENUM_CLASS, 'BgpOcAfiEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'BgpOcAfiEnum', 
                [], [], 
                '''                AFI
                ''',
                'afi',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 Addr
                ''',
                'ipv4_address',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 Addr
                ''',
                'ipv6_address',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'next-hop',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.RouteAttrList.AggregratorAttributes' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.RouteAttrList.AggregratorAttributes',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address
                ''',
                'address',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('as4', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                AS4 number
                ''',
                'as4',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('as', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                AS number
                ''',
                'as_',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'aggregrator-attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.RouteAttrList.Community' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.RouteAttrList.Community',
            False, 
            [
            _MetaInfoClassMember('objects', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                BGP OC objects
                ''',
                'objects',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'community',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.RouteAttrList' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.RouteAttrList',
            False, 
            [
            _MetaInfoClassMember('aggregrator-attributes', REFERENCE_CLASS, 'AggregratorAttributes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.RouteAttrList.AggregratorAttributes', 
                [], [], 
                '''                AggregatorList
                ''',
                'aggregrator_attributes',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('as4-path', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                AS4 Path
                ''',
                'as4_path',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('as-path', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                AS Path
                ''',
                'as_path',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('atomic-aggr', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                AtomicAggr
                ''',
                'atomic_aggr',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('community', REFERENCE_LIST, 'Community' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.RouteAttrList.Community', 
                [], [], 
                '''                CommunityArray
                ''',
                'community',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('local-pref', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LocalPref
                ''',
                'local_pref',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('med', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Med
                ''',
                'med',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('next-hop', REFERENCE_CLASS, 'NextHop' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.RouteAttrList.NextHop', 
                [], [], 
                '''                NextHopAddress
                ''',
                'next_hop',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('origin-type', REFERENCE_ENUM_CLASS, 'BgpOcOriginAttrEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'BgpOcOriginAttrEnum', 
                [], [], 
                '''                Origin Attribute Type
                ''',
                'origin_type',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'route-attr-list',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.ExtAttributesList.ExtCommunity' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.ExtAttributesList.ExtCommunity',
            False, 
            [
            _MetaInfoClassMember('objects', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                BGP OC objects
                ''',
                'objects',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'ext-community',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.ExtAttributesList.UnknownAttributes' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.ExtAttributesList.UnknownAttributes',
            False, 
            [
            _MetaInfoClassMember('attribute-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                AttributeLength
                ''',
                'attribute_length',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('attribute-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                AttributeType
                ''',
                'attribute_type',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('attribute-value', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Atributevalue
                ''',
                'attribute_value',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'unknown-attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.ExtAttributesList' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.ExtAttributesList',
            False, 
            [
            _MetaInfoClassMember('aigp', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                AIGP
                ''',
                'aigp',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('cluster', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                ClusterList
                ''',
                'cluster',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('ext-community', REFERENCE_LIST, 'ExtCommunity' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.ExtAttributesList.ExtCommunity', 
                [], [], 
                '''                ExtendedCommunityArray
                ''',
                'ext_community',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('originator-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                OriginatorID
                ''',
                'originator_id',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('path-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                PathId
                ''',
                'path_id',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('unknown-attributes', REFERENCE_LIST, 'UnknownAttributes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.ExtAttributesList.UnknownAttributes', 
                [], [], 
                '''                UnknownAttributes
                ''',
                'unknown_attributes',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'ext-attributes-list',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.LastModifiedDate' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.LastModifiedDate',
            False, 
            [
            _MetaInfoClassMember('time-value', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                TimeValue
                ''',
                'time_value',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'last-modified-date',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.LastUpdateRecieved' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.LastUpdateRecieved',
            False, 
            [
            _MetaInfoClassMember('time-value', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                TimeValue
                ''',
                'time_value',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'last-update-recieved',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route',
            False, 
            [
            _MetaInfoClassMember('best-path', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                BestPath
                ''',
                'best_path',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('ext-attributes-list', REFERENCE_CLASS, 'ExtAttributesList' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.ExtAttributesList', 
                [], [], 
                '''                ExtAttributesList
                ''',
                'ext_attributes_list',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('invalid-reason', REFERENCE_ENUM_CLASS, 'BgpOcInvalidRouteReasonEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'BgpOcInvalidRouteReasonEnum', 
                [], [], 
                '''                IndentityRef
                ''',
                'invalid_reason',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('last-modified-date', REFERENCE_CLASS, 'LastModifiedDate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.LastModifiedDate', 
                [], [], 
                '''                LastModifiedDate
                ''',
                'last_modified_date',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('last-update-recieved', REFERENCE_CLASS, 'LastUpdateRecieved' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.LastUpdateRecieved', 
                [], [], 
                '''                LastUpdateRecieved
                ''',
                'last_update_recieved',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('neighbor-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Neighbor address
                ''',
                'neighbor_address',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False, [
                    _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Neighbor address
                        ''',
                        'neighbor_address',
                        'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
                    _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Neighbor address
                        ''',
                        'neighbor_address',
                        'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
                ]),
            _MetaInfoClassMember('path-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Path ID
                ''',
                'path_id',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('prefix-name', REFERENCE_CLASS, 'PrefixName' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.PrefixName', 
                [], [], 
                '''                Prefix
                ''',
                'prefix_name',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('route', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Network in prefix/length format
                ''',
                'route',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False, [
                    _MetaInfoClassMember('route', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                        '''                        Network in prefix/length format
                        ''',
                        'route',
                        'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
                    _MetaInfoClassMember('route', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                        '''                        Network in prefix/length format
                        ''',
                        'route',
                        'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
                ]),
            _MetaInfoClassMember('route-attr-list', REFERENCE_CLASS, 'RouteAttrList' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.RouteAttrList', 
                [], [], 
                '''                RouteAttributesList
                ''',
                'route_attr_list',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('valid-route', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                ValidRoute
                ''',
                'valid_route',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'route',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes',
            False, 
            [
            _MetaInfoClassMember('route', REFERENCE_LIST, 'Route' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route', 
                [], [], 
                '''                route entry
                ''',
                'route',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'routes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.NumRoutes' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.NumRoutes',
            False, 
            [
            _MetaInfoClassMember('num-routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                NumRoutes
                ''',
                'num_routes',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'num-routes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre',
            False, 
            [
            _MetaInfoClassMember('num-routes', REFERENCE_CLASS, 'NumRoutes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.NumRoutes', 
                [], [], 
                '''                Number of routes in adjacency rib out-bound
                post-policy table
                ''',
                'num_routes',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('routes', REFERENCE_CLASS, 'Routes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes', 
                [], [], 
                '''                routes table
                ''',
                'routes',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'adj-rib-out-pre',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.PrefixName.Prefix' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.PrefixName.Prefix',
            False, 
            [
            _MetaInfoClassMember('afi', REFERENCE_ENUM_CLASS, 'BgpOcAfiEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'BgpOcAfiEnum', 
                [], [], 
                '''                AFI
                ''',
                'afi',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 Addr
                ''',
                'ipv4_address',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 Addr
                ''',
                'ipv6_address',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.PrefixName' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.PrefixName',
            False, 
            [
            _MetaInfoClassMember('prefix', REFERENCE_CLASS, 'Prefix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.PrefixName.Prefix', 
                [], [], 
                '''                Prefix
                ''',
                'prefix',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Prefix length
                ''',
                'prefix_length',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'prefix-name',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.RouteAttrList.NextHop' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.RouteAttrList.NextHop',
            False, 
            [
            _MetaInfoClassMember('afi', REFERENCE_ENUM_CLASS, 'BgpOcAfiEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'BgpOcAfiEnum', 
                [], [], 
                '''                AFI
                ''',
                'afi',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 Addr
                ''',
                'ipv4_address',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 Addr
                ''',
                'ipv6_address',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'next-hop',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.RouteAttrList.AggregratorAttributes' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.RouteAttrList.AggregratorAttributes',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address
                ''',
                'address',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('as4', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                AS4 number
                ''',
                'as4',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('as', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                AS number
                ''',
                'as_',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'aggregrator-attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.RouteAttrList.Community' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.RouteAttrList.Community',
            False, 
            [
            _MetaInfoClassMember('objects', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                BGP OC objects
                ''',
                'objects',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'community',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.RouteAttrList' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.RouteAttrList',
            False, 
            [
            _MetaInfoClassMember('aggregrator-attributes', REFERENCE_CLASS, 'AggregratorAttributes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.RouteAttrList.AggregratorAttributes', 
                [], [], 
                '''                AggregatorList
                ''',
                'aggregrator_attributes',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('as4-path', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                AS4 Path
                ''',
                'as4_path',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('as-path', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                AS Path
                ''',
                'as_path',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('atomic-aggr', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                AtomicAggr
                ''',
                'atomic_aggr',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('community', REFERENCE_LIST, 'Community' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.RouteAttrList.Community', 
                [], [], 
                '''                CommunityArray
                ''',
                'community',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('local-pref', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LocalPref
                ''',
                'local_pref',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('med', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Med
                ''',
                'med',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('next-hop', REFERENCE_CLASS, 'NextHop' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.RouteAttrList.NextHop', 
                [], [], 
                '''                NextHopAddress
                ''',
                'next_hop',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('origin-type', REFERENCE_ENUM_CLASS, 'BgpOcOriginAttrEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'BgpOcOriginAttrEnum', 
                [], [], 
                '''                Origin Attribute Type
                ''',
                'origin_type',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'route-attr-list',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.ExtAttributesList.ExtCommunity' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.ExtAttributesList.ExtCommunity',
            False, 
            [
            _MetaInfoClassMember('objects', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                BGP OC objects
                ''',
                'objects',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'ext-community',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.ExtAttributesList.UnknownAttributes' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.ExtAttributesList.UnknownAttributes',
            False, 
            [
            _MetaInfoClassMember('attribute-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                AttributeLength
                ''',
                'attribute_length',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('attribute-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                AttributeType
                ''',
                'attribute_type',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('attribute-value', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Atributevalue
                ''',
                'attribute_value',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'unknown-attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.ExtAttributesList' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.ExtAttributesList',
            False, 
            [
            _MetaInfoClassMember('aigp', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                AIGP
                ''',
                'aigp',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('cluster', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                ClusterList
                ''',
                'cluster',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('ext-community', REFERENCE_LIST, 'ExtCommunity' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.ExtAttributesList.ExtCommunity', 
                [], [], 
                '''                ExtendedCommunityArray
                ''',
                'ext_community',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('originator-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                OriginatorID
                ''',
                'originator_id',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('path-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                PathId
                ''',
                'path_id',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('unknown-attributes', REFERENCE_LIST, 'UnknownAttributes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.ExtAttributesList.UnknownAttributes', 
                [], [], 
                '''                UnknownAttributes
                ''',
                'unknown_attributes',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'ext-attributes-list',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.LastModifiedDate' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.LastModifiedDate',
            False, 
            [
            _MetaInfoClassMember('time-value', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                TimeValue
                ''',
                'time_value',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'last-modified-date',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.LastUpdateRecieved' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.LastUpdateRecieved',
            False, 
            [
            _MetaInfoClassMember('time-value', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                TimeValue
                ''',
                'time_value',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'last-update-recieved',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route',
            False, 
            [
            _MetaInfoClassMember('best-path', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                BestPath
                ''',
                'best_path',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('ext-attributes-list', REFERENCE_CLASS, 'ExtAttributesList' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.ExtAttributesList', 
                [], [], 
                '''                ExtAttributesList
                ''',
                'ext_attributes_list',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('invalid-reason', REFERENCE_ENUM_CLASS, 'BgpOcInvalidRouteReasonEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'BgpOcInvalidRouteReasonEnum', 
                [], [], 
                '''                IndentityRef
                ''',
                'invalid_reason',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('last-modified-date', REFERENCE_CLASS, 'LastModifiedDate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.LastModifiedDate', 
                [], [], 
                '''                LastModifiedDate
                ''',
                'last_modified_date',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('last-update-recieved', REFERENCE_CLASS, 'LastUpdateRecieved' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.LastUpdateRecieved', 
                [], [], 
                '''                LastUpdateRecieved
                ''',
                'last_update_recieved',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('neighbor-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Neighbor address
                ''',
                'neighbor_address',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False, [
                    _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Neighbor address
                        ''',
                        'neighbor_address',
                        'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
                    _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Neighbor address
                        ''',
                        'neighbor_address',
                        'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
                ]),
            _MetaInfoClassMember('path-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Path ID
                ''',
                'path_id',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('prefix-name', REFERENCE_CLASS, 'PrefixName' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.PrefixName', 
                [], [], 
                '''                Prefix
                ''',
                'prefix_name',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('route', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Network in prefix/length format
                ''',
                'route',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False, [
                    _MetaInfoClassMember('route', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                        '''                        Network in prefix/length format
                        ''',
                        'route',
                        'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
                    _MetaInfoClassMember('route', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                        '''                        Network in prefix/length format
                        ''',
                        'route',
                        'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
                ]),
            _MetaInfoClassMember('route-attr-list', REFERENCE_CLASS, 'RouteAttrList' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.RouteAttrList', 
                [], [], 
                '''                RouteAttributesList
                ''',
                'route_attr_list',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('valid-route', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                ValidRoute
                ''',
                'valid_route',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'route',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes',
            False, 
            [
            _MetaInfoClassMember('route', REFERENCE_LIST, 'Route' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route', 
                [], [], 
                '''                route entry
                ''',
                'route',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'routes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.NumRoutes' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.NumRoutes',
            False, 
            [
            _MetaInfoClassMember('num-routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                NumRoutes
                ''',
                'num_routes',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'num-routes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre',
            False, 
            [
            _MetaInfoClassMember('num-routes', REFERENCE_CLASS, 'NumRoutes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.NumRoutes', 
                [], [], 
                '''                Number of routes in adjacency rib out-bound
                post-policy table
                ''',
                'num_routes',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('routes', REFERENCE_CLASS, 'Routes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes', 
                [], [], 
                '''                routes table
                ''',
                'routes',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'adj-rib-in-pre',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor',
            False, 
            [
            _MetaInfoClassMember('neighbor-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Neighbor Address
                ''',
                'neighbor_address',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', True, [
                    _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Neighbor Address
                        ''',
                        'neighbor_address',
                        'Cisco-IOS-XR-ipv4-bgp-oc-oper', True),
                    _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Neighbor Address
                        ''',
                        'neighbor_address',
                        'Cisco-IOS-XR-ipv4-bgp-oc-oper', True),
                ]),
            _MetaInfoClassMember('adj-rib-in-post', REFERENCE_CLASS, 'AdjRibInPost' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost', 
                [], [], 
                '''                Adjacency rib in-bound post-policy table
                ''',
                'adj_rib_in_post',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('adj-rib-in-pre', REFERENCE_CLASS, 'AdjRibInPre' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre', 
                [], [], 
                '''                Adjacency rib in-bound pre-policy table
                ''',
                'adj_rib_in_pre',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('adj-rib-out-post', REFERENCE_CLASS, 'AdjRibOutPost' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost', 
                [], [], 
                '''                Adjacency rib out-bound post-policy table
                ''',
                'adj_rib_out_post',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('adj-rib-out-pre', REFERENCE_CLASS, 'AdjRibOutPre' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre', 
                [], [], 
                '''                Adjacency rib out-bound pre-policy table
                ''',
                'adj_rib_out_pre',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'open-config-neighbor',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors',
            False, 
            [
            _MetaInfoClassMember('open-config-neighbor', REFERENCE_LIST, 'OpenConfigNeighbor' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor', 
                [], [], 
                '''                Neighbor name
                ''',
                'open_config_neighbor',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'open-config-neighbors',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast',
            False, 
            [
            _MetaInfoClassMember('loc-rib', REFERENCE_CLASS, 'LocRib' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib', 
                [], [], 
                '''                Local rib route table
                ''',
                'loc_rib',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('open-config-neighbors', REFERENCE_CLASS, 'OpenConfigNeighbors' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors', 
                [], [], 
                '''                Neighbor list
                ''',
                'open_config_neighbors',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'ipv4-unicast',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.PrefixName.Prefix' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.PrefixName.Prefix',
            False, 
            [
            _MetaInfoClassMember('afi', REFERENCE_ENUM_CLASS, 'BgpOcAfiEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'BgpOcAfiEnum', 
                [], [], 
                '''                AFI
                ''',
                'afi',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 Addr
                ''',
                'ipv4_address',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 Addr
                ''',
                'ipv6_address',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.PrefixName' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.PrefixName',
            False, 
            [
            _MetaInfoClassMember('prefix', REFERENCE_CLASS, 'Prefix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.PrefixName.Prefix', 
                [], [], 
                '''                Prefix
                ''',
                'prefix',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Prefix length
                ''',
                'prefix_length',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'prefix-name',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.RouteAttrList.NextHop' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.RouteAttrList.NextHop',
            False, 
            [
            _MetaInfoClassMember('afi', REFERENCE_ENUM_CLASS, 'BgpOcAfiEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'BgpOcAfiEnum', 
                [], [], 
                '''                AFI
                ''',
                'afi',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 Addr
                ''',
                'ipv4_address',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 Addr
                ''',
                'ipv6_address',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'next-hop',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.RouteAttrList.AggregratorAttributes' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.RouteAttrList.AggregratorAttributes',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address
                ''',
                'address',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('as4', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                AS4 number
                ''',
                'as4',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('as', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                AS number
                ''',
                'as_',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'aggregrator-attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.RouteAttrList.Community' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.RouteAttrList.Community',
            False, 
            [
            _MetaInfoClassMember('objects', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                BGP OC objects
                ''',
                'objects',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'community',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.RouteAttrList' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.RouteAttrList',
            False, 
            [
            _MetaInfoClassMember('aggregrator-attributes', REFERENCE_CLASS, 'AggregratorAttributes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.RouteAttrList.AggregratorAttributes', 
                [], [], 
                '''                AggregatorList
                ''',
                'aggregrator_attributes',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('as4-path', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                AS4 Path
                ''',
                'as4_path',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('as-path', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                AS Path
                ''',
                'as_path',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('atomic-aggr', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                AtomicAggr
                ''',
                'atomic_aggr',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('community', REFERENCE_LIST, 'Community' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.RouteAttrList.Community', 
                [], [], 
                '''                CommunityArray
                ''',
                'community',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('local-pref', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LocalPref
                ''',
                'local_pref',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('med', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Med
                ''',
                'med',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('next-hop', REFERENCE_CLASS, 'NextHop' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.RouteAttrList.NextHop', 
                [], [], 
                '''                NextHopAddress
                ''',
                'next_hop',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('origin-type', REFERENCE_ENUM_CLASS, 'BgpOcOriginAttrEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'BgpOcOriginAttrEnum', 
                [], [], 
                '''                Origin Attribute Type
                ''',
                'origin_type',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'route-attr-list',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.ExtAttributesList.ExtCommunity' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.ExtAttributesList.ExtCommunity',
            False, 
            [
            _MetaInfoClassMember('objects', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                BGP OC objects
                ''',
                'objects',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'ext-community',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.ExtAttributesList.UnknownAttributes' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.ExtAttributesList.UnknownAttributes',
            False, 
            [
            _MetaInfoClassMember('attribute-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                AttributeLength
                ''',
                'attribute_length',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('attribute-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                AttributeType
                ''',
                'attribute_type',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('attribute-value', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Atributevalue
                ''',
                'attribute_value',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'unknown-attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.ExtAttributesList' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.ExtAttributesList',
            False, 
            [
            _MetaInfoClassMember('aigp', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                AIGP
                ''',
                'aigp',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('cluster', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                ClusterList
                ''',
                'cluster',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('ext-community', REFERENCE_LIST, 'ExtCommunity' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.ExtAttributesList.ExtCommunity', 
                [], [], 
                '''                ExtendedCommunityArray
                ''',
                'ext_community',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('originator-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                OriginatorID
                ''',
                'originator_id',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('path-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                PathId
                ''',
                'path_id',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('unknown-attributes', REFERENCE_LIST, 'UnknownAttributes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.ExtAttributesList.UnknownAttributes', 
                [], [], 
                '''                UnknownAttributes
                ''',
                'unknown_attributes',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'ext-attributes-list',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.LastModifiedDate' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.LastModifiedDate',
            False, 
            [
            _MetaInfoClassMember('time-value', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                TimeValue
                ''',
                'time_value',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'last-modified-date',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.LastUpdateRecieved' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.LastUpdateRecieved',
            False, 
            [
            _MetaInfoClassMember('time-value', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                TimeValue
                ''',
                'time_value',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'last-update-recieved',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route',
            False, 
            [
            _MetaInfoClassMember('best-path', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                BestPath
                ''',
                'best_path',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('ext-attributes-list', REFERENCE_CLASS, 'ExtAttributesList' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.ExtAttributesList', 
                [], [], 
                '''                ExtAttributesList
                ''',
                'ext_attributes_list',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('invalid-reason', REFERENCE_ENUM_CLASS, 'BgpOcInvalidRouteReasonEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'BgpOcInvalidRouteReasonEnum', 
                [], [], 
                '''                IndentityRef
                ''',
                'invalid_reason',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('last-modified-date', REFERENCE_CLASS, 'LastModifiedDate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.LastModifiedDate', 
                [], [], 
                '''                LastModifiedDate
                ''',
                'last_modified_date',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('last-update-recieved', REFERENCE_CLASS, 'LastUpdateRecieved' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.LastUpdateRecieved', 
                [], [], 
                '''                LastUpdateRecieved
                ''',
                'last_update_recieved',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('neighbor-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Neighbor address
                ''',
                'neighbor_address',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False, [
                    _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Neighbor address
                        ''',
                        'neighbor_address',
                        'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
                    _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Neighbor address
                        ''',
                        'neighbor_address',
                        'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
                ]),
            _MetaInfoClassMember('path-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Path ID
                ''',
                'path_id',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('prefix-name', REFERENCE_CLASS, 'PrefixName' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.PrefixName', 
                [], [], 
                '''                Prefix
                ''',
                'prefix_name',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('route', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Network in prefix/length format
                ''',
                'route',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False, [
                    _MetaInfoClassMember('route', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                        '''                        Network in prefix/length format
                        ''',
                        'route',
                        'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
                    _MetaInfoClassMember('route', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                        '''                        Network in prefix/length format
                        ''',
                        'route',
                        'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
                ]),
            _MetaInfoClassMember('route-attr-list', REFERENCE_CLASS, 'RouteAttrList' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.RouteAttrList', 
                [], [], 
                '''                RouteAttributesList
                ''',
                'route_attr_list',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('valid-route', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                ValidRoute
                ''',
                'valid_route',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'route',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes',
            False, 
            [
            _MetaInfoClassMember('route', REFERENCE_LIST, 'Route' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route', 
                [], [], 
                '''                route entry
                ''',
                'route',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'routes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.NumRoutes' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.NumRoutes',
            False, 
            [
            _MetaInfoClassMember('num-routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                NumRoutes
                ''',
                'num_routes',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'num-routes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib',
            False, 
            [
            _MetaInfoClassMember('num-routes', REFERENCE_CLASS, 'NumRoutes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.NumRoutes', 
                [], [], 
                '''                Number of routes in adjacency rib out-bound
                post-policy table
                ''',
                'num_routes',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('routes', REFERENCE_CLASS, 'Routes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes', 
                [], [], 
                '''                routes table
                ''',
                'routes',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'loc-rib',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.PrefixName.Prefix' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.PrefixName.Prefix',
            False, 
            [
            _MetaInfoClassMember('afi', REFERENCE_ENUM_CLASS, 'BgpOcAfiEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'BgpOcAfiEnum', 
                [], [], 
                '''                AFI
                ''',
                'afi',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 Addr
                ''',
                'ipv4_address',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 Addr
                ''',
                'ipv6_address',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.PrefixName' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.PrefixName',
            False, 
            [
            _MetaInfoClassMember('prefix', REFERENCE_CLASS, 'Prefix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.PrefixName.Prefix', 
                [], [], 
                '''                Prefix
                ''',
                'prefix',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Prefix length
                ''',
                'prefix_length',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'prefix-name',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.RouteAttrList.NextHop' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.RouteAttrList.NextHop',
            False, 
            [
            _MetaInfoClassMember('afi', REFERENCE_ENUM_CLASS, 'BgpOcAfiEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'BgpOcAfiEnum', 
                [], [], 
                '''                AFI
                ''',
                'afi',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 Addr
                ''',
                'ipv4_address',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 Addr
                ''',
                'ipv6_address',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'next-hop',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.RouteAttrList.AggregratorAttributes' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.RouteAttrList.AggregratorAttributes',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address
                ''',
                'address',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('as4', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                AS4 number
                ''',
                'as4',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('as', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                AS number
                ''',
                'as_',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'aggregrator-attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.RouteAttrList.Community' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.RouteAttrList.Community',
            False, 
            [
            _MetaInfoClassMember('objects', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                BGP OC objects
                ''',
                'objects',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'community',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.RouteAttrList' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.RouteAttrList',
            False, 
            [
            _MetaInfoClassMember('aggregrator-attributes', REFERENCE_CLASS, 'AggregratorAttributes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.RouteAttrList.AggregratorAttributes', 
                [], [], 
                '''                AggregatorList
                ''',
                'aggregrator_attributes',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('as4-path', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                AS4 Path
                ''',
                'as4_path',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('as-path', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                AS Path
                ''',
                'as_path',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('atomic-aggr', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                AtomicAggr
                ''',
                'atomic_aggr',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('community', REFERENCE_LIST, 'Community' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.RouteAttrList.Community', 
                [], [], 
                '''                CommunityArray
                ''',
                'community',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('local-pref', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LocalPref
                ''',
                'local_pref',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('med', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Med
                ''',
                'med',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('next-hop', REFERENCE_CLASS, 'NextHop' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.RouteAttrList.NextHop', 
                [], [], 
                '''                NextHopAddress
                ''',
                'next_hop',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('origin-type', REFERENCE_ENUM_CLASS, 'BgpOcOriginAttrEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'BgpOcOriginAttrEnum', 
                [], [], 
                '''                Origin Attribute Type
                ''',
                'origin_type',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'route-attr-list',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.ExtAttributesList.ExtCommunity' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.ExtAttributesList.ExtCommunity',
            False, 
            [
            _MetaInfoClassMember('objects', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                BGP OC objects
                ''',
                'objects',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'ext-community',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.ExtAttributesList.UnknownAttributes' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.ExtAttributesList.UnknownAttributes',
            False, 
            [
            _MetaInfoClassMember('attribute-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                AttributeLength
                ''',
                'attribute_length',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('attribute-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                AttributeType
                ''',
                'attribute_type',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('attribute-value', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Atributevalue
                ''',
                'attribute_value',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'unknown-attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.ExtAttributesList' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.ExtAttributesList',
            False, 
            [
            _MetaInfoClassMember('aigp', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                AIGP
                ''',
                'aigp',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('cluster', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                ClusterList
                ''',
                'cluster',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('ext-community', REFERENCE_LIST, 'ExtCommunity' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.ExtAttributesList.ExtCommunity', 
                [], [], 
                '''                ExtendedCommunityArray
                ''',
                'ext_community',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('originator-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                OriginatorID
                ''',
                'originator_id',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('path-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                PathId
                ''',
                'path_id',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('unknown-attributes', REFERENCE_LIST, 'UnknownAttributes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.ExtAttributesList.UnknownAttributes', 
                [], [], 
                '''                UnknownAttributes
                ''',
                'unknown_attributes',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'ext-attributes-list',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.LastModifiedDate' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.LastModifiedDate',
            False, 
            [
            _MetaInfoClassMember('time-value', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                TimeValue
                ''',
                'time_value',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'last-modified-date',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.LastUpdateRecieved' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.LastUpdateRecieved',
            False, 
            [
            _MetaInfoClassMember('time-value', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                TimeValue
                ''',
                'time_value',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'last-update-recieved',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route',
            False, 
            [
            _MetaInfoClassMember('best-path', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                BestPath
                ''',
                'best_path',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('ext-attributes-list', REFERENCE_CLASS, 'ExtAttributesList' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.ExtAttributesList', 
                [], [], 
                '''                ExtAttributesList
                ''',
                'ext_attributes_list',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('invalid-reason', REFERENCE_ENUM_CLASS, 'BgpOcInvalidRouteReasonEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'BgpOcInvalidRouteReasonEnum', 
                [], [], 
                '''                IndentityRef
                ''',
                'invalid_reason',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('last-modified-date', REFERENCE_CLASS, 'LastModifiedDate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.LastModifiedDate', 
                [], [], 
                '''                LastModifiedDate
                ''',
                'last_modified_date',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('last-update-recieved', REFERENCE_CLASS, 'LastUpdateRecieved' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.LastUpdateRecieved', 
                [], [], 
                '''                LastUpdateRecieved
                ''',
                'last_update_recieved',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('neighbor-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Neighbor address
                ''',
                'neighbor_address',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False, [
                    _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Neighbor address
                        ''',
                        'neighbor_address',
                        'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
                    _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Neighbor address
                        ''',
                        'neighbor_address',
                        'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
                ]),
            _MetaInfoClassMember('path-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Path ID
                ''',
                'path_id',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('prefix-name', REFERENCE_CLASS, 'PrefixName' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.PrefixName', 
                [], [], 
                '''                Prefix
                ''',
                'prefix_name',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('route', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Network in prefix/length format
                ''',
                'route',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False, [
                    _MetaInfoClassMember('route', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                        '''                        Network in prefix/length format
                        ''',
                        'route',
                        'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
                    _MetaInfoClassMember('route', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                        '''                        Network in prefix/length format
                        ''',
                        'route',
                        'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
                ]),
            _MetaInfoClassMember('route-attr-list', REFERENCE_CLASS, 'RouteAttrList' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.RouteAttrList', 
                [], [], 
                '''                RouteAttributesList
                ''',
                'route_attr_list',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('valid-route', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                ValidRoute
                ''',
                'valid_route',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'route',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes',
            False, 
            [
            _MetaInfoClassMember('route', REFERENCE_LIST, 'Route' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route', 
                [], [], 
                '''                route entry
                ''',
                'route',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'routes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.NumRoutes' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.NumRoutes',
            False, 
            [
            _MetaInfoClassMember('num-routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                NumRoutes
                ''',
                'num_routes',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'num-routes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost',
            False, 
            [
            _MetaInfoClassMember('num-routes', REFERENCE_CLASS, 'NumRoutes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.NumRoutes', 
                [], [], 
                '''                Number of routes in adjacency rib out-bound
                post-policy table
                ''',
                'num_routes',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('routes', REFERENCE_CLASS, 'Routes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes', 
                [], [], 
                '''                routes table
                ''',
                'routes',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'adj-rib-in-post',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.PrefixName.Prefix' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.PrefixName.Prefix',
            False, 
            [
            _MetaInfoClassMember('afi', REFERENCE_ENUM_CLASS, 'BgpOcAfiEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'BgpOcAfiEnum', 
                [], [], 
                '''                AFI
                ''',
                'afi',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 Addr
                ''',
                'ipv4_address',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 Addr
                ''',
                'ipv6_address',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.PrefixName' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.PrefixName',
            False, 
            [
            _MetaInfoClassMember('prefix', REFERENCE_CLASS, 'Prefix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.PrefixName.Prefix', 
                [], [], 
                '''                Prefix
                ''',
                'prefix',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Prefix length
                ''',
                'prefix_length',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'prefix-name',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.RouteAttrList.NextHop' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.RouteAttrList.NextHop',
            False, 
            [
            _MetaInfoClassMember('afi', REFERENCE_ENUM_CLASS, 'BgpOcAfiEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'BgpOcAfiEnum', 
                [], [], 
                '''                AFI
                ''',
                'afi',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 Addr
                ''',
                'ipv4_address',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 Addr
                ''',
                'ipv6_address',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'next-hop',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.RouteAttrList.AggregratorAttributes' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.RouteAttrList.AggregratorAttributes',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address
                ''',
                'address',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('as4', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                AS4 number
                ''',
                'as4',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('as', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                AS number
                ''',
                'as_',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'aggregrator-attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.RouteAttrList.Community' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.RouteAttrList.Community',
            False, 
            [
            _MetaInfoClassMember('objects', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                BGP OC objects
                ''',
                'objects',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'community',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.RouteAttrList' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.RouteAttrList',
            False, 
            [
            _MetaInfoClassMember('aggregrator-attributes', REFERENCE_CLASS, 'AggregratorAttributes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.RouteAttrList.AggregratorAttributes', 
                [], [], 
                '''                AggregatorList
                ''',
                'aggregrator_attributes',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('as4-path', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                AS4 Path
                ''',
                'as4_path',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('as-path', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                AS Path
                ''',
                'as_path',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('atomic-aggr', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                AtomicAggr
                ''',
                'atomic_aggr',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('community', REFERENCE_LIST, 'Community' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.RouteAttrList.Community', 
                [], [], 
                '''                CommunityArray
                ''',
                'community',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('local-pref', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LocalPref
                ''',
                'local_pref',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('med', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Med
                ''',
                'med',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('next-hop', REFERENCE_CLASS, 'NextHop' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.RouteAttrList.NextHop', 
                [], [], 
                '''                NextHopAddress
                ''',
                'next_hop',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('origin-type', REFERENCE_ENUM_CLASS, 'BgpOcOriginAttrEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'BgpOcOriginAttrEnum', 
                [], [], 
                '''                Origin Attribute Type
                ''',
                'origin_type',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'route-attr-list',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.ExtAttributesList.ExtCommunity' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.ExtAttributesList.ExtCommunity',
            False, 
            [
            _MetaInfoClassMember('objects', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                BGP OC objects
                ''',
                'objects',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'ext-community',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.ExtAttributesList.UnknownAttributes' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.ExtAttributesList.UnknownAttributes',
            False, 
            [
            _MetaInfoClassMember('attribute-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                AttributeLength
                ''',
                'attribute_length',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('attribute-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                AttributeType
                ''',
                'attribute_type',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('attribute-value', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Atributevalue
                ''',
                'attribute_value',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'unknown-attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.ExtAttributesList' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.ExtAttributesList',
            False, 
            [
            _MetaInfoClassMember('aigp', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                AIGP
                ''',
                'aigp',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('cluster', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                ClusterList
                ''',
                'cluster',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('ext-community', REFERENCE_LIST, 'ExtCommunity' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.ExtAttributesList.ExtCommunity', 
                [], [], 
                '''                ExtendedCommunityArray
                ''',
                'ext_community',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('originator-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                OriginatorID
                ''',
                'originator_id',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('path-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                PathId
                ''',
                'path_id',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('unknown-attributes', REFERENCE_LIST, 'UnknownAttributes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.ExtAttributesList.UnknownAttributes', 
                [], [], 
                '''                UnknownAttributes
                ''',
                'unknown_attributes',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'ext-attributes-list',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.LastModifiedDate' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.LastModifiedDate',
            False, 
            [
            _MetaInfoClassMember('time-value', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                TimeValue
                ''',
                'time_value',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'last-modified-date',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.LastUpdateRecieved' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.LastUpdateRecieved',
            False, 
            [
            _MetaInfoClassMember('time-value', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                TimeValue
                ''',
                'time_value',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'last-update-recieved',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route',
            False, 
            [
            _MetaInfoClassMember('best-path', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                BestPath
                ''',
                'best_path',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('ext-attributes-list', REFERENCE_CLASS, 'ExtAttributesList' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.ExtAttributesList', 
                [], [], 
                '''                ExtAttributesList
                ''',
                'ext_attributes_list',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('invalid-reason', REFERENCE_ENUM_CLASS, 'BgpOcInvalidRouteReasonEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'BgpOcInvalidRouteReasonEnum', 
                [], [], 
                '''                IndentityRef
                ''',
                'invalid_reason',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('last-modified-date', REFERENCE_CLASS, 'LastModifiedDate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.LastModifiedDate', 
                [], [], 
                '''                LastModifiedDate
                ''',
                'last_modified_date',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('last-update-recieved', REFERENCE_CLASS, 'LastUpdateRecieved' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.LastUpdateRecieved', 
                [], [], 
                '''                LastUpdateRecieved
                ''',
                'last_update_recieved',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('neighbor-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Neighbor address
                ''',
                'neighbor_address',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False, [
                    _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Neighbor address
                        ''',
                        'neighbor_address',
                        'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
                    _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Neighbor address
                        ''',
                        'neighbor_address',
                        'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
                ]),
            _MetaInfoClassMember('path-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Path ID
                ''',
                'path_id',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('prefix-name', REFERENCE_CLASS, 'PrefixName' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.PrefixName', 
                [], [], 
                '''                Prefix
                ''',
                'prefix_name',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('route', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Network in prefix/length format
                ''',
                'route',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False, [
                    _MetaInfoClassMember('route', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                        '''                        Network in prefix/length format
                        ''',
                        'route',
                        'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
                    _MetaInfoClassMember('route', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                        '''                        Network in prefix/length format
                        ''',
                        'route',
                        'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
                ]),
            _MetaInfoClassMember('route-attr-list', REFERENCE_CLASS, 'RouteAttrList' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.RouteAttrList', 
                [], [], 
                '''                RouteAttributesList
                ''',
                'route_attr_list',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('valid-route', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                ValidRoute
                ''',
                'valid_route',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'route',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes',
            False, 
            [
            _MetaInfoClassMember('route', REFERENCE_LIST, 'Route' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route', 
                [], [], 
                '''                route entry
                ''',
                'route',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'routes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.NumRoutes' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.NumRoutes',
            False, 
            [
            _MetaInfoClassMember('num-routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                NumRoutes
                ''',
                'num_routes',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'num-routes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost',
            False, 
            [
            _MetaInfoClassMember('num-routes', REFERENCE_CLASS, 'NumRoutes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.NumRoutes', 
                [], [], 
                '''                Number of routes in adjacency rib out-bound
                post-policy table
                ''',
                'num_routes',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('routes', REFERENCE_CLASS, 'Routes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes', 
                [], [], 
                '''                routes table
                ''',
                'routes',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'adj-rib-out-post',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.PrefixName.Prefix' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.PrefixName.Prefix',
            False, 
            [
            _MetaInfoClassMember('afi', REFERENCE_ENUM_CLASS, 'BgpOcAfiEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'BgpOcAfiEnum', 
                [], [], 
                '''                AFI
                ''',
                'afi',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 Addr
                ''',
                'ipv4_address',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 Addr
                ''',
                'ipv6_address',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.PrefixName' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.PrefixName',
            False, 
            [
            _MetaInfoClassMember('prefix', REFERENCE_CLASS, 'Prefix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.PrefixName.Prefix', 
                [], [], 
                '''                Prefix
                ''',
                'prefix',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Prefix length
                ''',
                'prefix_length',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'prefix-name',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.RouteAttrList.NextHop' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.RouteAttrList.NextHop',
            False, 
            [
            _MetaInfoClassMember('afi', REFERENCE_ENUM_CLASS, 'BgpOcAfiEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'BgpOcAfiEnum', 
                [], [], 
                '''                AFI
                ''',
                'afi',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 Addr
                ''',
                'ipv4_address',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 Addr
                ''',
                'ipv6_address',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'next-hop',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.RouteAttrList.AggregratorAttributes' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.RouteAttrList.AggregratorAttributes',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address
                ''',
                'address',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('as4', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                AS4 number
                ''',
                'as4',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('as', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                AS number
                ''',
                'as_',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'aggregrator-attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.RouteAttrList.Community' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.RouteAttrList.Community',
            False, 
            [
            _MetaInfoClassMember('objects', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                BGP OC objects
                ''',
                'objects',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'community',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.RouteAttrList' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.RouteAttrList',
            False, 
            [
            _MetaInfoClassMember('aggregrator-attributes', REFERENCE_CLASS, 'AggregratorAttributes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.RouteAttrList.AggregratorAttributes', 
                [], [], 
                '''                AggregatorList
                ''',
                'aggregrator_attributes',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('as4-path', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                AS4 Path
                ''',
                'as4_path',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('as-path', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                AS Path
                ''',
                'as_path',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('atomic-aggr', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                AtomicAggr
                ''',
                'atomic_aggr',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('community', REFERENCE_LIST, 'Community' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.RouteAttrList.Community', 
                [], [], 
                '''                CommunityArray
                ''',
                'community',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('local-pref', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LocalPref
                ''',
                'local_pref',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('med', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Med
                ''',
                'med',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('next-hop', REFERENCE_CLASS, 'NextHop' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.RouteAttrList.NextHop', 
                [], [], 
                '''                NextHopAddress
                ''',
                'next_hop',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('origin-type', REFERENCE_ENUM_CLASS, 'BgpOcOriginAttrEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'BgpOcOriginAttrEnum', 
                [], [], 
                '''                Origin Attribute Type
                ''',
                'origin_type',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'route-attr-list',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.ExtAttributesList.ExtCommunity' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.ExtAttributesList.ExtCommunity',
            False, 
            [
            _MetaInfoClassMember('objects', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                BGP OC objects
                ''',
                'objects',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'ext-community',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.ExtAttributesList.UnknownAttributes' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.ExtAttributesList.UnknownAttributes',
            False, 
            [
            _MetaInfoClassMember('attribute-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                AttributeLength
                ''',
                'attribute_length',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('attribute-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                AttributeType
                ''',
                'attribute_type',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('attribute-value', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Atributevalue
                ''',
                'attribute_value',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'unknown-attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.ExtAttributesList' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.ExtAttributesList',
            False, 
            [
            _MetaInfoClassMember('aigp', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                AIGP
                ''',
                'aigp',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('cluster', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                ClusterList
                ''',
                'cluster',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('ext-community', REFERENCE_LIST, 'ExtCommunity' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.ExtAttributesList.ExtCommunity', 
                [], [], 
                '''                ExtendedCommunityArray
                ''',
                'ext_community',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('originator-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                OriginatorID
                ''',
                'originator_id',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('path-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                PathId
                ''',
                'path_id',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('unknown-attributes', REFERENCE_LIST, 'UnknownAttributes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.ExtAttributesList.UnknownAttributes', 
                [], [], 
                '''                UnknownAttributes
                ''',
                'unknown_attributes',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'ext-attributes-list',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.LastModifiedDate' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.LastModifiedDate',
            False, 
            [
            _MetaInfoClassMember('time-value', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                TimeValue
                ''',
                'time_value',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'last-modified-date',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.LastUpdateRecieved' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.LastUpdateRecieved',
            False, 
            [
            _MetaInfoClassMember('time-value', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                TimeValue
                ''',
                'time_value',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'last-update-recieved',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route',
            False, 
            [
            _MetaInfoClassMember('best-path', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                BestPath
                ''',
                'best_path',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('ext-attributes-list', REFERENCE_CLASS, 'ExtAttributesList' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.ExtAttributesList', 
                [], [], 
                '''                ExtAttributesList
                ''',
                'ext_attributes_list',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('invalid-reason', REFERENCE_ENUM_CLASS, 'BgpOcInvalidRouteReasonEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'BgpOcInvalidRouteReasonEnum', 
                [], [], 
                '''                IndentityRef
                ''',
                'invalid_reason',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('last-modified-date', REFERENCE_CLASS, 'LastModifiedDate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.LastModifiedDate', 
                [], [], 
                '''                LastModifiedDate
                ''',
                'last_modified_date',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('last-update-recieved', REFERENCE_CLASS, 'LastUpdateRecieved' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.LastUpdateRecieved', 
                [], [], 
                '''                LastUpdateRecieved
                ''',
                'last_update_recieved',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('neighbor-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Neighbor address
                ''',
                'neighbor_address',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False, [
                    _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Neighbor address
                        ''',
                        'neighbor_address',
                        'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
                    _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Neighbor address
                        ''',
                        'neighbor_address',
                        'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
                ]),
            _MetaInfoClassMember('path-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Path ID
                ''',
                'path_id',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('prefix-name', REFERENCE_CLASS, 'PrefixName' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.PrefixName', 
                [], [], 
                '''                Prefix
                ''',
                'prefix_name',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('route', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Network in prefix/length format
                ''',
                'route',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False, [
                    _MetaInfoClassMember('route', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                        '''                        Network in prefix/length format
                        ''',
                        'route',
                        'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
                    _MetaInfoClassMember('route', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                        '''                        Network in prefix/length format
                        ''',
                        'route',
                        'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
                ]),
            _MetaInfoClassMember('route-attr-list', REFERENCE_CLASS, 'RouteAttrList' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.RouteAttrList', 
                [], [], 
                '''                RouteAttributesList
                ''',
                'route_attr_list',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('valid-route', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                ValidRoute
                ''',
                'valid_route',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'route',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes',
            False, 
            [
            _MetaInfoClassMember('route', REFERENCE_LIST, 'Route' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route', 
                [], [], 
                '''                route entry
                ''',
                'route',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'routes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.NumRoutes' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.NumRoutes',
            False, 
            [
            _MetaInfoClassMember('num-routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                NumRoutes
                ''',
                'num_routes',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'num-routes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre',
            False, 
            [
            _MetaInfoClassMember('num-routes', REFERENCE_CLASS, 'NumRoutes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.NumRoutes', 
                [], [], 
                '''                Number of routes in adjacency rib out-bound
                post-policy table
                ''',
                'num_routes',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('routes', REFERENCE_CLASS, 'Routes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes', 
                [], [], 
                '''                routes table
                ''',
                'routes',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'adj-rib-out-pre',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.PrefixName.Prefix' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.PrefixName.Prefix',
            False, 
            [
            _MetaInfoClassMember('afi', REFERENCE_ENUM_CLASS, 'BgpOcAfiEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'BgpOcAfiEnum', 
                [], [], 
                '''                AFI
                ''',
                'afi',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 Addr
                ''',
                'ipv4_address',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 Addr
                ''',
                'ipv6_address',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.PrefixName' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.PrefixName',
            False, 
            [
            _MetaInfoClassMember('prefix', REFERENCE_CLASS, 'Prefix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.PrefixName.Prefix', 
                [], [], 
                '''                Prefix
                ''',
                'prefix',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Prefix length
                ''',
                'prefix_length',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'prefix-name',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.RouteAttrList.NextHop' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.RouteAttrList.NextHop',
            False, 
            [
            _MetaInfoClassMember('afi', REFERENCE_ENUM_CLASS, 'BgpOcAfiEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'BgpOcAfiEnum', 
                [], [], 
                '''                AFI
                ''',
                'afi',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 Addr
                ''',
                'ipv4_address',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 Addr
                ''',
                'ipv6_address',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'next-hop',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.RouteAttrList.AggregratorAttributes' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.RouteAttrList.AggregratorAttributes',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address
                ''',
                'address',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('as4', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                AS4 number
                ''',
                'as4',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('as', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                AS number
                ''',
                'as_',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'aggregrator-attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.RouteAttrList.Community' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.RouteAttrList.Community',
            False, 
            [
            _MetaInfoClassMember('objects', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                BGP OC objects
                ''',
                'objects',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'community',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.RouteAttrList' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.RouteAttrList',
            False, 
            [
            _MetaInfoClassMember('aggregrator-attributes', REFERENCE_CLASS, 'AggregratorAttributes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.RouteAttrList.AggregratorAttributes', 
                [], [], 
                '''                AggregatorList
                ''',
                'aggregrator_attributes',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('as4-path', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                AS4 Path
                ''',
                'as4_path',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('as-path', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                AS Path
                ''',
                'as_path',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('atomic-aggr', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                AtomicAggr
                ''',
                'atomic_aggr',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('community', REFERENCE_LIST, 'Community' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.RouteAttrList.Community', 
                [], [], 
                '''                CommunityArray
                ''',
                'community',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('local-pref', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LocalPref
                ''',
                'local_pref',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('med', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Med
                ''',
                'med',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('next-hop', REFERENCE_CLASS, 'NextHop' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.RouteAttrList.NextHop', 
                [], [], 
                '''                NextHopAddress
                ''',
                'next_hop',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('origin-type', REFERENCE_ENUM_CLASS, 'BgpOcOriginAttrEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'BgpOcOriginAttrEnum', 
                [], [], 
                '''                Origin Attribute Type
                ''',
                'origin_type',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'route-attr-list',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.ExtAttributesList.ExtCommunity' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.ExtAttributesList.ExtCommunity',
            False, 
            [
            _MetaInfoClassMember('objects', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                BGP OC objects
                ''',
                'objects',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'ext-community',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.ExtAttributesList.UnknownAttributes' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.ExtAttributesList.UnknownAttributes',
            False, 
            [
            _MetaInfoClassMember('attribute-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                AttributeLength
                ''',
                'attribute_length',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('attribute-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                AttributeType
                ''',
                'attribute_type',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('attribute-value', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Atributevalue
                ''',
                'attribute_value',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'unknown-attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.ExtAttributesList' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.ExtAttributesList',
            False, 
            [
            _MetaInfoClassMember('aigp', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                AIGP
                ''',
                'aigp',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('cluster', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                ClusterList
                ''',
                'cluster',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('ext-community', REFERENCE_LIST, 'ExtCommunity' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.ExtAttributesList.ExtCommunity', 
                [], [], 
                '''                ExtendedCommunityArray
                ''',
                'ext_community',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('originator-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                OriginatorID
                ''',
                'originator_id',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('path-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                PathId
                ''',
                'path_id',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('unknown-attributes', REFERENCE_LIST, 'UnknownAttributes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.ExtAttributesList.UnknownAttributes', 
                [], [], 
                '''                UnknownAttributes
                ''',
                'unknown_attributes',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'ext-attributes-list',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.LastModifiedDate' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.LastModifiedDate',
            False, 
            [
            _MetaInfoClassMember('time-value', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                TimeValue
                ''',
                'time_value',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'last-modified-date',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.LastUpdateRecieved' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.LastUpdateRecieved',
            False, 
            [
            _MetaInfoClassMember('time-value', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                TimeValue
                ''',
                'time_value',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'last-update-recieved',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route',
            False, 
            [
            _MetaInfoClassMember('best-path', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                BestPath
                ''',
                'best_path',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('ext-attributes-list', REFERENCE_CLASS, 'ExtAttributesList' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.ExtAttributesList', 
                [], [], 
                '''                ExtAttributesList
                ''',
                'ext_attributes_list',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('invalid-reason', REFERENCE_ENUM_CLASS, 'BgpOcInvalidRouteReasonEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'BgpOcInvalidRouteReasonEnum', 
                [], [], 
                '''                IndentityRef
                ''',
                'invalid_reason',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('last-modified-date', REFERENCE_CLASS, 'LastModifiedDate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.LastModifiedDate', 
                [], [], 
                '''                LastModifiedDate
                ''',
                'last_modified_date',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('last-update-recieved', REFERENCE_CLASS, 'LastUpdateRecieved' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.LastUpdateRecieved', 
                [], [], 
                '''                LastUpdateRecieved
                ''',
                'last_update_recieved',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('neighbor-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Neighbor address
                ''',
                'neighbor_address',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False, [
                    _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Neighbor address
                        ''',
                        'neighbor_address',
                        'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
                    _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Neighbor address
                        ''',
                        'neighbor_address',
                        'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
                ]),
            _MetaInfoClassMember('path-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Path ID
                ''',
                'path_id',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('prefix-name', REFERENCE_CLASS, 'PrefixName' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.PrefixName', 
                [], [], 
                '''                Prefix
                ''',
                'prefix_name',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('route', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Network in prefix/length format
                ''',
                'route',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False, [
                    _MetaInfoClassMember('route', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                        '''                        Network in prefix/length format
                        ''',
                        'route',
                        'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
                    _MetaInfoClassMember('route', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                        '''                        Network in prefix/length format
                        ''',
                        'route',
                        'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
                ]),
            _MetaInfoClassMember('route-attr-list', REFERENCE_CLASS, 'RouteAttrList' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.RouteAttrList', 
                [], [], 
                '''                RouteAttributesList
                ''',
                'route_attr_list',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('valid-route', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                ValidRoute
                ''',
                'valid_route',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'route',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes',
            False, 
            [
            _MetaInfoClassMember('route', REFERENCE_LIST, 'Route' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route', 
                [], [], 
                '''                route entry
                ''',
                'route',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'routes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.NumRoutes' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.NumRoutes',
            False, 
            [
            _MetaInfoClassMember('num-routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                NumRoutes
                ''',
                'num_routes',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'num-routes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre',
            False, 
            [
            _MetaInfoClassMember('num-routes', REFERENCE_CLASS, 'NumRoutes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.NumRoutes', 
                [], [], 
                '''                Number of routes in adjacency rib out-bound
                post-policy table
                ''',
                'num_routes',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('routes', REFERENCE_CLASS, 'Routes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes', 
                [], [], 
                '''                routes table
                ''',
                'routes',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'adj-rib-in-pre',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor',
            False, 
            [
            _MetaInfoClassMember('neighbor-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Neighbor Address
                ''',
                'neighbor_address',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', True, [
                    _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Neighbor Address
                        ''',
                        'neighbor_address',
                        'Cisco-IOS-XR-ipv4-bgp-oc-oper', True),
                    _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Neighbor Address
                        ''',
                        'neighbor_address',
                        'Cisco-IOS-XR-ipv4-bgp-oc-oper', True),
                ]),
            _MetaInfoClassMember('adj-rib-in-post', REFERENCE_CLASS, 'AdjRibInPost' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost', 
                [], [], 
                '''                Adjacency rib in-bound post-policy table
                ''',
                'adj_rib_in_post',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('adj-rib-in-pre', REFERENCE_CLASS, 'AdjRibInPre' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre', 
                [], [], 
                '''                Adjacency rib in-bound pre-policy table
                ''',
                'adj_rib_in_pre',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('adj-rib-out-post', REFERENCE_CLASS, 'AdjRibOutPost' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost', 
                [], [], 
                '''                Adjacency rib out-bound post-policy table
                ''',
                'adj_rib_out_post',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('adj-rib-out-pre', REFERENCE_CLASS, 'AdjRibOutPre' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre', 
                [], [], 
                '''                Adjacency rib out-bound pre-policy table
                ''',
                'adj_rib_out_pre',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'open-config-neighbor',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors',
            False, 
            [
            _MetaInfoClassMember('open-config-neighbor', REFERENCE_LIST, 'OpenConfigNeighbor' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor', 
                [], [], 
                '''                Neighbor name
                ''',
                'open_config_neighbor',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'open-config-neighbors',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast',
            False, 
            [
            _MetaInfoClassMember('loc-rib', REFERENCE_CLASS, 'LocRib' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib', 
                [], [], 
                '''                Local rib route table
                ''',
                'loc_rib',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('open-config-neighbors', REFERENCE_CLASS, 'OpenConfigNeighbors' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors', 
                [], [], 
                '''                Neighbor list
                ''',
                'open_config_neighbors',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'ipv6-unicast',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib.AfiSafiTable' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib.AfiSafiTable',
            False, 
            [
            _MetaInfoClassMember('ipv4-unicast', REFERENCE_CLASS, 'Ipv4Unicast' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast', 
                [], [], 
                '''                IPv4 Unicast
                ''',
                'ipv4_unicast',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            _MetaInfoClassMember('ipv6-unicast', REFERENCE_CLASS, 'Ipv6Unicast' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast', 
                [], [], 
                '''                IPv6 Unicast
                ''',
                'ipv6_unicast',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'afi-safi-table',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp.BgpRib' : {
        'meta_info' : _MetaInfoClass('OcBgp.BgpRib',
            False, 
            [
            _MetaInfoClassMember('afi-safi-table', REFERENCE_CLASS, 'AfiSafiTable' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib.AfiSafiTable', 
                [], [], 
                '''                AFI-SAFIs information
                ''',
                'afi_safi_table',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'bgp-rib',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
    'OcBgp' : {
        'meta_info' : _MetaInfoClass('OcBgp',
            False, 
            [
            _MetaInfoClassMember('bgp-rib', REFERENCE_CLASS, 'BgpRib' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper', 'OcBgp.BgpRib', 
                [], [], 
                '''                BGP-RIB operational data
                ''',
                'bgp_rib',
                'Cisco-IOS-XR-ipv4-bgp-oc-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-oc-oper',
            'oc-bgp',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-oc-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_oc_oper'
        ),
    },
}
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.PrefixName.Prefix']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.PrefixName']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.RouteAttrList.NextHop']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.RouteAttrList']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.RouteAttrList.AggregratorAttributes']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.RouteAttrList']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.RouteAttrList.Community']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.RouteAttrList']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.ExtAttributesList.ExtCommunity']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.ExtAttributesList']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.ExtAttributesList.UnknownAttributes']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.ExtAttributesList']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.PrefixName']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.RouteAttrList']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.ExtAttributesList']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.LastModifiedDate']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route.LastUpdateRecieved']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes.Route']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.Routes']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib.NumRoutes']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.PrefixName.Prefix']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.PrefixName']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.RouteAttrList.NextHop']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.RouteAttrList']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.RouteAttrList.AggregratorAttributes']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.RouteAttrList']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.RouteAttrList.Community']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.RouteAttrList']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.ExtAttributesList.ExtCommunity']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.ExtAttributesList']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.ExtAttributesList.UnknownAttributes']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.ExtAttributesList']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.PrefixName']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.RouteAttrList']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.ExtAttributesList']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.LastModifiedDate']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.LastUpdateRecieved']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.NumRoutes']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.PrefixName.Prefix']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.PrefixName']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.RouteAttrList.NextHop']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.RouteAttrList']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.RouteAttrList.AggregratorAttributes']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.RouteAttrList']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.RouteAttrList.Community']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.RouteAttrList']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.ExtAttributesList.ExtCommunity']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.ExtAttributesList']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.ExtAttributesList.UnknownAttributes']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.ExtAttributesList']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.PrefixName']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.RouteAttrList']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.ExtAttributesList']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.LastModifiedDate']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.LastUpdateRecieved']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.NumRoutes']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.PrefixName.Prefix']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.PrefixName']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.RouteAttrList.NextHop']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.RouteAttrList']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.RouteAttrList.AggregratorAttributes']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.RouteAttrList']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.RouteAttrList.Community']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.RouteAttrList']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.ExtAttributesList.ExtCommunity']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.ExtAttributesList']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.ExtAttributesList.UnknownAttributes']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.ExtAttributesList']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.PrefixName']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.RouteAttrList']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.ExtAttributesList']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.LastModifiedDate']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.LastUpdateRecieved']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.NumRoutes']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.PrefixName.Prefix']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.PrefixName']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.RouteAttrList.NextHop']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.RouteAttrList']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.RouteAttrList.AggregratorAttributes']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.RouteAttrList']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.RouteAttrList.Community']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.RouteAttrList']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.ExtAttributesList.ExtCommunity']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.ExtAttributesList']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.ExtAttributesList.UnknownAttributes']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.ExtAttributesList']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.PrefixName']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.RouteAttrList']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.ExtAttributesList']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.LastModifiedDate']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.LastUpdateRecieved']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.NumRoutes']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors.OpenConfigNeighbor']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.LocRib']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast.OpenConfigNeighbors']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.PrefixName.Prefix']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.PrefixName']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.RouteAttrList.NextHop']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.RouteAttrList']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.RouteAttrList.AggregratorAttributes']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.RouteAttrList']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.RouteAttrList.Community']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.RouteAttrList']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.ExtAttributesList.ExtCommunity']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.ExtAttributesList']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.ExtAttributesList.UnknownAttributes']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.ExtAttributesList']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.PrefixName']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.RouteAttrList']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.ExtAttributesList']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.LastModifiedDate']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route.LastUpdateRecieved']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes.Route']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.Routes']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib.NumRoutes']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.PrefixName.Prefix']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.PrefixName']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.RouteAttrList.NextHop']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.RouteAttrList']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.RouteAttrList.AggregratorAttributes']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.RouteAttrList']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.RouteAttrList.Community']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.RouteAttrList']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.ExtAttributesList.ExtCommunity']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.ExtAttributesList']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.ExtAttributesList.UnknownAttributes']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.ExtAttributesList']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.PrefixName']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.RouteAttrList']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.ExtAttributesList']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.LastModifiedDate']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route.LastUpdateRecieved']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes.Route']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.Routes']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost.NumRoutes']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.PrefixName.Prefix']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.PrefixName']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.RouteAttrList.NextHop']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.RouteAttrList']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.RouteAttrList.AggregratorAttributes']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.RouteAttrList']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.RouteAttrList.Community']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.RouteAttrList']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.ExtAttributesList.ExtCommunity']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.ExtAttributesList']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.ExtAttributesList.UnknownAttributes']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.ExtAttributesList']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.PrefixName']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.RouteAttrList']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.ExtAttributesList']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.LastModifiedDate']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route.LastUpdateRecieved']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes.Route']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.Routes']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost.NumRoutes']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.PrefixName.Prefix']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.PrefixName']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.RouteAttrList.NextHop']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.RouteAttrList']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.RouteAttrList.AggregratorAttributes']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.RouteAttrList']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.RouteAttrList.Community']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.RouteAttrList']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.ExtAttributesList.ExtCommunity']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.ExtAttributesList']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.ExtAttributesList.UnknownAttributes']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.ExtAttributesList']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.PrefixName']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.RouteAttrList']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.ExtAttributesList']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.LastModifiedDate']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route.LastUpdateRecieved']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes.Route']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.Routes']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre.NumRoutes']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.PrefixName.Prefix']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.PrefixName']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.RouteAttrList.NextHop']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.RouteAttrList']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.RouteAttrList.AggregratorAttributes']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.RouteAttrList']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.RouteAttrList.Community']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.RouteAttrList']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.ExtAttributesList.ExtCommunity']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.ExtAttributesList']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.ExtAttributesList.UnknownAttributes']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.ExtAttributesList']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.PrefixName']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.RouteAttrList']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.ExtAttributesList']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.LastModifiedDate']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route.LastUpdateRecieved']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes.Route']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.Routes']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre.NumRoutes']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPost']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPost']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibOutPre']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor.AdjRibInPre']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors.OpenConfigNeighbor']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.LocRib']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast.OpenConfigNeighbors']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv4Unicast']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable.Ipv6Unicast']['meta_info'].parent =_meta_table['OcBgp.BgpRib.AfiSafiTable']['meta_info']
_meta_table['OcBgp.BgpRib.AfiSafiTable']['meta_info'].parent =_meta_table['OcBgp.BgpRib']['meta_info']
_meta_table['OcBgp.BgpRib']['meta_info'].parent =_meta_table['OcBgp']['meta_info']
