


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'FibFrrProtocolShowEnum' : _MetaInfoEnum('FibFrrProtocolShowEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper',
        {
            'frr-protocol-ipv4':'frr_protocol_ipv4',
            'frr-protocol-ipv6':'frr_protocol_ipv6',
            'frr-protocol-mpls':'frr_protocol_mpls',
        }, 'Cisco-IOS-XR-fib-common-oper', _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper']),
    'FibLinkEnum' : _MetaInfoEnum('FibLinkEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper',
        {
            'link-ipv4':'link_ipv4',
            'link-ipv6':'link_ipv6',
            'link-mpls':'link_mpls',
        }, 'Cisco-IOS-XR-fib-common-oper', _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper']),
    'FibAdjacencyShowEnum' : _MetaInfoEnum('FibAdjacencyShowEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper',
        {
            'fib-adjacency-normal':'fib_adjacency_normal',
            'fib-adjacency-null':'fib_adjacency_null',
            'fib-adjacency-punt':'fib_adjacency_punt',
            'fib-adjacency-drop':'fib_adjacency_drop',
            'fib-adjacency-glean':'fib_adjacency_glean',
            'fib-adjacency-discard':'fib_adjacency_discard',
            'fib-adjacency-broadcast':'fib_adjacency_broadcast',
            'fib-adjacency-external':'fib_adjacency_external',
            'fib-adjacency-lisp':'fib_adjacency_lisp',
            'fib-adjacency-unknown':'fib_adjacency_unknown',
        }, 'Cisco-IOS-XR-fib-common-oper', _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper']),
    'FibRpfModeEnum' : _MetaInfoEnum('FibRpfModeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper',
        {
            'fib-rpf-mode-strict':'fib_rpf_mode_strict',
            'fib-rpf-mode-loose':'fib_rpf_mode_loose',
            'fib-rpf-mode-unknown':'fib_rpf_mode_unknown',
        }, 'Cisco-IOS-XR-fib-common-oper', _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper']),
    'SsLbaStateEnum' : _MetaInfoEnum('SsLbaStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper',
        {
            'l3':'l3',
            'l4':'l4',
        }, 'Cisco-IOS-XR-fib-common-oper', _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper']),
    'FibllcEntryEnum' : _MetaInfoEnum('FibllcEntryEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper',
        {
            'xc':'xc',
            'pfx':'pfx',
        }, 'Cisco-IOS-XR-fib-common-oper', _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper']),
    'FibShTblFibExtBagEnum' : _MetaInfoEnum('FibShTblFibExtBagEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper',
        {
            'leaf-extension':'leaf_extension',
        }, 'Cisco-IOS-XR-fib-common-oper', _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper']),
    'FibMplsLlcEntryBagEnum' : _MetaInfoEnum('FibMplsLlcEntryBagEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper',
        {
            'fib-mpls-llc-bag-type-xc':'fib_mpls_llc_bag_type_xc',
            'fib-mpls-llc-bag-type-pfx':'fib_mpls_llc_bag_type_pfx',
            'fib-mpls-llc-bag-type-lsm':'fib_mpls_llc_bag_type_lsm',
            'fib-mpls-llc-bag-type-max':'fib_mpls_llc_bag_type_max',
        }, 'Cisco-IOS-XR-fib-common-oper', _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper']),
    'FibidbOperEnum' : _MetaInfoEnum('FibidbOperEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper',
        {
            'fibidb-none':'fibidb_none',
            'fibidb-create':'fibidb_create',
            'fibidb-delete':'fibidb_delete',
            'fibidb-modify':'fibidb_modify',
            'fibidb-max':'fibidb_max',
        }, 'Cisco-IOS-XR-fib-common-oper', _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper']),
    'FibProtocolEnum' : _MetaInfoEnum('FibProtocolEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper',
        {
            'ipv4':'ipv4',
            'ipv6':'ipv6',
            'mpls':'mpls',
        }, 'Cisco-IOS-XR-fib-common-oper', _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper']),
    'FibNehEnum' : _MetaInfoEnum('FibNehEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper',
        {
            'nh-local':'nh_local',
            'nh-remote':'nh_remote',
            'nh-special':'nh_special',
        }, 'Cisco-IOS-XR-fib-common-oper', _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper']),
    'MplseosEnum' : _MetaInfoEnum('MplseosEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper',
        {
            'eos0':'eos0',
            'eos1':'eos1',
        }, 'Cisco-IOS-XR-fib-common-oper', _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper']),
    'FibUpdatePathLfaProtectionEnum' : _MetaInfoEnum('FibUpdatePathLfaProtectionEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper',
        {
            'not-lfa-protected':'not_lfa_protected',
            'local-lfa-protected':'local_lfa_protected',
            'remote-lfa-protected':'remote_lfa_protected',
            'ti-lfa-protected':'ti_lfa_protected',
        }, 'Cisco-IOS-XR-fib-common-oper', _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper']),
    'NextHopEnum' : _MetaInfoEnum('NextHopEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper',
        {
            'tx':'tx',
            'rx':'rx',
            'special':'special',
        }, 'Cisco-IOS-XR-fib-common-oper', _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper']),
    'FibNehSpecialEnum' : _MetaInfoEnum('FibNehSpecialEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper',
        {
            'nh-not-found':'nh_not_found',
            'nh-null0':'nh_null0',
            'nh-punt':'nh_punt',
            'nh-drop':'nh_drop',
            'nh-glean':'nh_glean',
            'nh-receive':'nh_receive',
            'nh-broadcast':'nh_broadcast',
            'nh-external':'nh_external',
            'nh-lisp':'nh_lisp',
            'nh-lookup':'nh_lookup',
            'nh-max-type':'nh_max_type',
        }, 'Cisco-IOS-XR-fib-common-oper', _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper']),
    'MgmtFibMplsLspRoleEnum' : _MetaInfoEnum('MgmtFibMplsLspRoleEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper',
        {
            'head':'head',
            'midpoint':'midpoint',
        }, 'Cisco-IOS-XR-fib-common-oper', _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper']),
    'FibafiProtoEnum' : _MetaInfoEnum('FibafiProtoEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper',
        {
            'ipv4':'ipv4',
            'ipv4-mpls':'ipv4_mpls',
            'ipv6':'ipv6',
            'ipv6-mpls':'ipv6_mpls',
        }, 'Cisco-IOS-XR-fib-common-oper', _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper']),
    'MgmtFibMplsFrrStateEnum' : _MetaInfoEnum('MgmtFibMplsFrrStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper',
        {
            'partial':'partial',
            'active':'active',
            'ready':'ready',
            'complete':'complete',
            'any':'any',
        }, 'Cisco-IOS-XR-fib-common-oper', _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper']),
    'ProtoEnum' : _MetaInfoEnum('ProtoEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper',
        {
            'ipv4':'ipv4',
            'ipv6':'ipv6',
            'mpls':'mpls',
        }, 'Cisco-IOS-XR-fib-common-oper', _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper']),
    'FibRouteSourceEnum' : _MetaInfoEnum('FibRouteSourceEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper',
        {
            'lsd':'lsd',
            'rib':'rib',
            'mrib':'mrib',
        }, 'Cisco-IOS-XR-fib-common-oper', _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper']),
    'FibLoadshareShowEnum' : _MetaInfoEnum('FibLoadshareShowEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper',
        {
            'fib-load-share-none':'fib_load_share_none',
            'fib-load-share-per-packet':'fib_load_share_per_packet',
            'fib-load-share-dest-sharing':'fib_load_share_dest_sharing',
        }, 'Cisco-IOS-XR-fib-common-oper', _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper']),
    'FibShIpencapHdrEnum' : _MetaInfoEnum('FibShIpencapHdrEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper',
        {
            'fib-sh-ip-encap-none':'fib_sh_ip_encap_none',
            'fib-sh-ip-encap-ip4':'fib_sh_ip_encap_ip4',
            'fib-sh-ip-encap-ip6':'fib_sh_ip_encap_ip6',
            'fib-sh-ip-encap-udp':'fib_sh_ip_encap_udp',
            'fib-sh-ip-encap-lisp':'fib_sh_ip_encap_lisp',
        }, 'Cisco-IOS-XR-fib-common-oper', _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper']),
    'FibStatistics.Nodes.Node.Drops' : {
        'meta_info' : _MetaInfoClass('FibStatistics.Nodes.Node.Drops',
            False, 
            [
            _MetaInfoClassMember('acl-in-rpf-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                ACL in RPF pkt
                ''',
                'acl_in_rpf_packets',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('checksum-error-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                checksum error pkt
                ''',
                'checksum_error_packets',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('df-unreachable-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                DF unreachable pkt
                ''',
                'df_unreachable_packets',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('discard-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                discard pkt
                ''',
                'discard_packets',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('encapsulation-failure-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                encapsulation failure pkt
                ''',
                'encapsulation_failure_packets',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fragmenation-consumed-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                frag consumed packet pkt
                ''',
                'fragmenation_consumed_packets',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fragmenation-failure-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                fragmenation failure pkt
                ''',
                'fragmenation_failure_packets',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('gre-error-drop', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                GRE processing errors
                ''',
                'gre_error_drop',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('gre-lookup-failed-drop', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                GRE tunnel lookup failed drop pkt
                ''',
                'gre_lookup_failed_drop',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('incomplete-adjacency-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                incomplete adjacency pkt
                ''',
                'incomplete_adjacency_packets',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('lisp-decap-error-drops', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Lisp decap error drops
                ''',
                'lisp_decap_error_drops',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('lisp-encap-error-drops', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Lisp encap error drops
                ''',
                'lisp_encap_error_drops',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('lisp-punt-drops', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                LISP Punt drops
                ''',
                'lisp_punt_drops',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('mpls-disabled-interface', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                mpls disabled in interface
                ''',
                'mpls_disabled_interface',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('multi-label-drops', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Drops for the packets with multi[le labels
                ''',
                'multi_label_drops',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('no-route-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                no route pkt
                ''',
                'no_route_packets',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('null-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                null0 pkt
                ''',
                'null_packets',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('punt-unreachable-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Punt generate unreach pkt
                ''',
                'punt_unreachable_packets',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('rp-destination-drop-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                rp dest drop pkt
                ''',
                'rp_destination_drop_packets',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('rpf-check-failure-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                RPF check failures pkt
                ''',
                'rpf_check_failure_packets',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('total-number-of-drop-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                the total number of drop pkt
                ''',
                'total_number_of_drop_packets',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('unresolved-prefix-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                unresolved prefix pkt
                ''',
                'unresolved_prefix_packets',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('unsupported-feature-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                unsupported feature pkt
                ''',
                'unsupported_feature_packets',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'drops',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'FibStatistics.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('FibStatistics.Nodes.Node',
            False, 
            [
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Node name
                ''',
                'node_name',
                'Cisco-IOS-XR-fib-common-oper', True),
            _MetaInfoClassMember('drops', REFERENCE_CLASS, 'Drops' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'FibStatistics.Nodes.Node.Drops', 
                [], [], 
                '''                Specific node drops
                ''',
                'drops',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'node',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'FibStatistics.Nodes' : {
        'meta_info' : _MetaInfoClass('FibStatistics.Nodes',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'FibStatistics.Nodes.Node', 
                [], [], 
                '''                Specific node operational data
                ''',
                'node',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'nodes',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'FibStatistics' : {
        'meta_info' : _MetaInfoClass('FibStatistics',
            False, 
            [
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'FibStatistics.Nodes', 
                [], [], 
                '''                List of nodes
                ''',
                'nodes',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'fib-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Global_.Summary.Total.CommonInfo' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Global_.Summary.Total.CommonInfo',
            False, 
            [
            _MetaInfoClassMember('count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Placeholder for common info counts
                ''',
                'count',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'common-info',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Global_.Summary.Total.TotalCounters.ArrayNumberOfRetry' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Global_.Summary.Total.TotalCounters.ArrayNumberOfRetry',
            False, 
            [
            _MetaInfoClassMember('num-retries', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                number of elements for this obj type in retry db
                ''',
                'num_retries',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('retry-object-type', ATTRIBUTE, 'str' , None, None, 
                [(0, 30)], [], 
                '''                retry object
                ''',
                'retry_object_type',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'array-number-of-retry',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Global_.Summary.Total.TotalCounters.ArrayNumberOfObject' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Global_.Summary.Total.TotalCounters.ArrayNumberOfObject',
            False, 
            [
            _MetaInfoClassMember('num-objects', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                number of elements for this obj type
                ''',
                'num_objects',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('object-type', ATTRIBUTE, 'str' , None, None, 
                [(0, 30)], [], 
                '''                object
                ''',
                'object_type',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'array-number-of-object',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Global_.Summary.Total.TotalCounters' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Global_.Summary.Total.TotalCounters',
            False, 
            [
            _MetaInfoClassMember('array-number-of-object', REFERENCE_LIST, 'ArrayNumberOfObject' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Global_.Summary.Total.TotalCounters.ArrayNumberOfObject', 
                [], [], 
                '''                total number of objects
                ''',
                'array_number_of_object',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('array-number-of-retry', REFERENCE_LIST, 'ArrayNumberOfRetry' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Global_.Summary.Total.TotalCounters.ArrayNumberOfRetry', 
                [], [], 
                '''                number of objects in retry db
                ''',
                'array_number_of_retry',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('num-retry-ojbects', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                number of elements in retry db
                ''',
                'num_retry_ojbects',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('num-retry-timeouts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                number of retry timeouts
                ''',
                'num_retry_timeouts',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'total-counters',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Global_.Summary.Total' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Global_.Summary.Total',
            False, 
            [
            _MetaInfoClassMember('common-info', REFERENCE_CLASS, 'CommonInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Global_.Summary.Total.CommonInfo', 
                [], [], 
                '''                Common info
                ''',
                'common_info',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('total-counters', REFERENCE_CLASS, 'TotalCounters' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Global_.Summary.Total.TotalCounters', 
                [], [], 
                '''                Aggregate counters of all protocols
                ''',
                'total_counters',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'total',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Global_.Summary.Protos.Proto.CommonInfo' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Global_.Summary.Protos.Proto.CommonInfo',
            False, 
            [
            _MetaInfoClassMember('count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Placeholder for common info counts
                ''',
                'count',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'common-info',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Global_.Summary.Protos.Proto.Summary_.BaseObject' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Global_.Summary.Protos.Proto.Summary_.BaseObject',
            False, 
            [
            _MetaInfoClassMember('protocol', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                protocol
                ''',
                'protocol',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'base-object',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Global_.Summary.Protos.Proto.Summary_.SummaryCounts.ArrayNumberOfRetry' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Global_.Summary.Protos.Proto.Summary_.SummaryCounts.ArrayNumberOfRetry',
            False, 
            [
            _MetaInfoClassMember('num-retries', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                number of elements for this obj type in retry db
                ''',
                'num_retries',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('retry-object-type', ATTRIBUTE, 'str' , None, None, 
                [(0, 30)], [], 
                '''                retry object
                ''',
                'retry_object_type',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'array-number-of-retry',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Global_.Summary.Protos.Proto.Summary_.SummaryCounts.ArrayNumberOfObject' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Global_.Summary.Protos.Proto.Summary_.SummaryCounts.ArrayNumberOfObject',
            False, 
            [
            _MetaInfoClassMember('num-objects', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                number of elements for this obj type
                ''',
                'num_objects',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('object-type', ATTRIBUTE, 'str' , None, None, 
                [(0, 30)], [], 
                '''                object
                ''',
                'object_type',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'array-number-of-object',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Global_.Summary.Protos.Proto.Summary_.SummaryCounts' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Global_.Summary.Protos.Proto.Summary_.SummaryCounts',
            False, 
            [
            _MetaInfoClassMember('array-number-of-object', REFERENCE_LIST, 'ArrayNumberOfObject' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Global_.Summary.Protos.Proto.Summary_.SummaryCounts.ArrayNumberOfObject', 
                [], [], 
                '''                total number of objects
                ''',
                'array_number_of_object',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('array-number-of-retry', REFERENCE_LIST, 'ArrayNumberOfRetry' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Global_.Summary.Protos.Proto.Summary_.SummaryCounts.ArrayNumberOfRetry', 
                [], [], 
                '''                number of objects in retry db
                ''',
                'array_number_of_retry',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('num-retry-ojbects', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                number of elements in retry db
                ''',
                'num_retry_ojbects',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('num-retry-timeouts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                number of retry timeouts
                ''',
                'num_retry_timeouts',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'summary-counts',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Global_.Summary.Protos.Proto.Summary_.Health' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Global_.Summary.Protos.Proto.Summary_.Health',
            False, 
            [
            _MetaInfoClassMember('is-retry-db-empty', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is the retry db empty?
                ''',
                'is_retry_db_empty',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'health',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Global_.Summary.Protos.Proto.Summary_' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Global_.Summary.Protos.Proto.Summary_',
            False, 
            [
            _MetaInfoClassMember('base-object', REFERENCE_CLASS, 'BaseObject' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Global_.Summary.Protos.Proto.Summary_.BaseObject', 
                [], [], 
                '''                Base object
                ''',
                'base_object',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('health', REFERENCE_CLASS, 'Health' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Global_.Summary.Protos.Proto.Summary_.Health', 
                [], [], 
                '''                Global summary health
                ''',
                'health',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('summary-counts', REFERENCE_CLASS, 'SummaryCounts' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Global_.Summary.Protos.Proto.Summary_.SummaryCounts', 
                [], [], 
                '''                Global Summary counts
                ''',
                'summary_counts',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'summary',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Global_.Summary.Protos.Proto' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Global_.Summary.Protos.Proto',
            False, 
            [
            _MetaInfoClassMember('protocol-name', REFERENCE_ENUM_CLASS, 'FibafiProtoEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'FibafiProtoEnum', 
                [], [], 
                '''                Protocol Name
                ''',
                'protocol_name',
                'Cisco-IOS-XR-fib-common-oper', True),
            _MetaInfoClassMember('common-info', REFERENCE_CLASS, 'CommonInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Global_.Summary.Protos.Proto.CommonInfo', 
                [], [], 
                '''                Common Info
                ''',
                'common_info',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('summary', REFERENCE_CLASS, 'Summary_' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Global_.Summary.Protos.Proto.Summary_', 
                [], [], 
                '''                Global summary
                ''',
                'summary',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'proto',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Global_.Summary.Protos' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Global_.Summary.Protos',
            False, 
            [
            _MetaInfoClassMember('proto', REFERENCE_LIST, 'Proto' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Global_.Summary.Protos.Proto', 
                [], [], 
                '''                Proto Table entry
                ''',
                'proto',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'protos',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Global_.Summary' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Global_.Summary',
            False, 
            [
            _MetaInfoClassMember('protos', REFERENCE_CLASS, 'Protos' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Global_.Summary.Protos', 
                [], [], 
                '''                Proto Table
                ''',
                'protos',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('total', REFERENCE_CLASS, 'Total' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Global_.Summary.Total', 
                [], [], 
                '''                Display total counters and common info
                ''',
                'total',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'summary',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Global_.ObjectHistory.ObjHistoryProtos.ObjHistoryProto.BaseObject' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Global_.ObjectHistory.ObjHistoryProtos.ObjHistoryProto.BaseObject',
            False, 
            [
            _MetaInfoClassMember('protocol', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                protocol
                ''',
                'protocol',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'base-object',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Global_.ObjectHistory.ObjHistoryProtos.ObjHistoryProto.ObjectHistory_' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Global_.ObjectHistory.ObjHistoryProtos.ObjHistoryProto.ObjectHistory_',
            False, 
            [
            _MetaInfoClassMember('count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Placeholder for obj history counts
                ''',
                'count',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'object-history',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Global_.ObjectHistory.ObjHistoryProtos.ObjHistoryProto' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Global_.ObjectHistory.ObjHistoryProtos.ObjHistoryProto',
            False, 
            [
            _MetaInfoClassMember('protocol-name', REFERENCE_ENUM_CLASS, 'FibafiProtoEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'FibafiProtoEnum', 
                [], [], 
                '''                Protocol Name
                ''',
                'protocol_name',
                'Cisco-IOS-XR-fib-common-oper', True),
            _MetaInfoClassMember('base-object', REFERENCE_CLASS, 'BaseObject' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Global_.ObjectHistory.ObjHistoryProtos.ObjHistoryProto.BaseObject', 
                [], [], 
                '''                Base object
                ''',
                'base_object',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('object-history', REFERENCE_CLASS, 'ObjectHistory_' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Global_.ObjectHistory.ObjHistoryProtos.ObjHistoryProto.ObjectHistory_', 
                [], [], 
                '''                Obj History
                ''',
                'object_history',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'obj-history-proto',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Global_.ObjectHistory.ObjHistoryProtos' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Global_.ObjectHistory.ObjHistoryProtos',
            False, 
            [
            _MetaInfoClassMember('obj-history-proto', REFERENCE_LIST, 'ObjHistoryProto' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Global_.ObjectHistory.ObjHistoryProtos.ObjHistoryProto', 
                [], [], 
                '''                Protocol Table entry
                ''',
                'obj_history_proto',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'obj-history-protos',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Global_.ObjectHistory' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Global_.ObjectHistory',
            False, 
            [
            _MetaInfoClassMember('obj-history-protos', REFERENCE_CLASS, 'ObjHistoryProtos' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Global_.ObjectHistory.ObjHistoryProtos', 
                [], [], 
                '''                Proto Table
                ''',
                'obj_history_protos',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'object-history',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Global_' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Global_',
            False, 
            [
            _MetaInfoClassMember('object-history', REFERENCE_CLASS, 'ObjectHistory' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Global_.ObjectHistory', 
                [], [], 
                '''                Object History
                ''',
                'object_history',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('summary', REFERENCE_CLASS, 'Summary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Global_.Summary', 
                [], [], 
                '''                Global Summary
                ''',
                'summary',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'global',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Protocols.Protocol.IssuState.FisProtoState' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Protocols.Protocol.IssuState.FisProtoState',
            False, 
            [
            _MetaInfoClassMember('aib-eod-time-stamp', ATTRIBUTE, 'str' , None, None, 
                [(0, 33)], [], 
                '''                AIB EODTimeStamp
                ''',
                'aib_eod_time_stamp',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('bcdl-tables', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of BCDL tables
                ''',
                'bcdl_tables',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('converged-tables', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of tables converged
                ''',
                'converged_tables',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('lmrib-eod-time-stamp', ATTRIBUTE, 'str' , None, None, 
                [(0, 33)], [], 
                '''                LMRIB EOD received timestamp
                ''',
                'lmrib_eod_time_stamp',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('lmrib-eod-valid', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                LMRIB EOD expected/valid
                ''',
                'lmrib_eod_valid',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('lsd-eod-time-stamp', ATTRIBUTE, 'str' , None, None, 
                [(0, 33)], [], 
                '''                LSD EOD received timestamp
                ''',
                'lsd_eod_time_stamp',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('lsd-eod-valid', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                LSD EOD expected/valid
                ''',
                'lsd_eod_valid',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('protocol-eod-time-stamp', ATTRIBUTE, 'str' , None, None, 
                [(0, 33)], [], 
                '''                Protocol EOD sent timestamp
                ''',
                'protocol_eod_time_stamp',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('protocol-eod-valid', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Protocol EOD expected/valid
                ''',
                'protocol_eod_valid',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('protocol-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 6)], [], 
                '''                Protocol name
                ''',
                'protocol_name',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('rib-info-valid', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                RIB table info valid
                ''',
                'rib_info_valid',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('rib-tables-converged-time-stamp', ATTRIBUTE, 'str' , None, None, 
                [(0, 33)], [], 
                '''                All RIB tables converged timestamp
                ''',
                'rib_tables_converged_time_stamp',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('rsi-eod-time-stamp', ATTRIBUTE, 'str' , None, None, 
                [(0, 33)], [], 
                '''                RSI EOD received timestamp
                ''',
                'rsi_eod_time_stamp',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('rsi-eod-valid', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                RSI EOD expected/valid
                ''',
                'rsi_eod_valid',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'fis-proto-state',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Protocols.Protocol.IssuState' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Protocols.Protocol.IssuState',
            False, 
            [
            _MetaInfoClassMember('eoc-received-imdr-time-stamp', ATTRIBUTE, 'str' , None, None, 
                [(0, 33)], [], 
                '''                End-of-config received from IMDR timestamp
                ''',
                'eoc_received_imdr_time_stamp',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('eoc-received-slc-time-stamp', ATTRIBUTE, 'str' , None, None, 
                [(0, 33)], [], 
                '''                End-of-config received from SLC timestamp
                ''',
                'eoc_received_slc_time_stamp',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('eod-received-im-time-stamp', ATTRIBUTE, 'str' , None, None, 
                [(0, 33)], [], 
                '''                End-of-download received from IM timestamp
                ''',
                'eod_received_im_time_stamp',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('eod-sent-imdr-time-stamp', ATTRIBUTE, 'str' , None, None, 
                [(0, 33)], [], 
                '''                End-of-download send to IMDR timestamp
                ''',
                'eod_sent_imdr_time_stamp',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('eod-sent-slc-time-stamp', ATTRIBUTE, 'str' , None, None, 
                [(0, 33)], [], 
                '''                End-of-download send to SLC timestamp
                ''',
                'eod_sent_slc_time_stamp',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fis-issu-error-ts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                ISSU error sent to ISSUMGR timetstamp
                ''',
                'fis_issu_error_ts',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fis-issu-restart', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                ISSU restart
                ''',
                'fis_issu_restart',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fis-proto-state', REFERENCE_LIST, 'FisProtoState' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Protocols.Protocol.IssuState.FisProtoState', 
                [], [], 
                '''                IMDR state for the protocols
                ''',
                'fis_proto_state',
                'Cisco-IOS-XR-fib-common-oper', False, max_elements=3),
            _MetaInfoClassMember('imdr-eoc-implicit', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                IMDR End-of-config implicit
                ''',
                'imdr_eoc_implicit',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('imdr-support', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                IMDR supported
                ''',
                'imdr_support',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('slc-eoc-implicit', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                SLC End-of-config implicit
                ''',
                'slc_eoc_implicit',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('slc-support', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                SLC supported
                ''',
                'slc_support',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'issu-state',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Protocols.Protocol.Resource.ResourceDetailInfo.SrShmState' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Protocols.Protocol.Resource.ResourceDetailInfo.SrShmState',
            False, 
            [
            _MetaInfoClassMember('srs-avg-avail', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Average number of bytes available
                ''',
                'srs_avg_avail',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('srs-curr-mode', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                OOR mode for this shared memory window
                ''',
                'srs_curr_mode',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('srs-max-avail', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Maximum bytes available
                ''',
                'srs_max_avail',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'sr-shm-state',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Protocols.Protocol.Resource.ResourceDetailInfo' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Protocols.Protocol.Resource.ResourceDetailInfo',
            False, 
            [
            _MetaInfoClassMember('sr-curr-mode', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Current overall oor mode
                ''',
                'sr_curr_mode',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('sr-hw-oor-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                sr hw oor count
                ''',
                'sr_hw_oor_count',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('sr-hwrsrc-info', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Opaque hardware rsrc state info
                ''',
                'sr_hwrsrc_info',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('sr-hwrsrc-mode', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Hardware resource mode
                ''',
                'sr_hwrsrc_mode',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('sr-in-oor-ts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                sr in oor ts
                ''',
                'sr_in_oor_ts',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('sr-out-oor-ts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                sr out oor ts
                ''',
                'sr_out_oor_ts',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('sr-shm-state', REFERENCE_LIST, 'SrShmState' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Protocols.Protocol.Resource.ResourceDetailInfo.SrShmState', 
                [], [], 
                '''                Current status of shared memories
                ''',
                'sr_shm_state',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('sr-shmwin-oor-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                sr shmwin oor count
                ''',
                'sr_shmwin_oor_count',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'resource-detail-info',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Protocols.Protocol.Resource.ResourceHardwareIngressInfo.SrShmState' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Protocols.Protocol.Resource.ResourceHardwareIngressInfo.SrShmState',
            False, 
            [
            _MetaInfoClassMember('srs-avg-avail', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Average number of bytes available
                ''',
                'srs_avg_avail',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('srs-curr-mode', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                OOR mode for this shared memory window
                ''',
                'srs_curr_mode',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('srs-max-avail', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Maximum bytes available
                ''',
                'srs_max_avail',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'sr-shm-state',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Protocols.Protocol.Resource.ResourceHardwareIngressInfo' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Protocols.Protocol.Resource.ResourceHardwareIngressInfo',
            False, 
            [
            _MetaInfoClassMember('sr-curr-mode', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Current overall oor mode
                ''',
                'sr_curr_mode',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('sr-hw-oor-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                sr hw oor count
                ''',
                'sr_hw_oor_count',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('sr-hwrsrc-info', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Opaque hardware rsrc state info
                ''',
                'sr_hwrsrc_info',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('sr-hwrsrc-mode', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Hardware resource mode
                ''',
                'sr_hwrsrc_mode',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('sr-in-oor-ts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                sr in oor ts
                ''',
                'sr_in_oor_ts',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('sr-out-oor-ts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                sr out oor ts
                ''',
                'sr_out_oor_ts',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('sr-shm-state', REFERENCE_LIST, 'SrShmState' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Protocols.Protocol.Resource.ResourceHardwareIngressInfo.SrShmState', 
                [], [], 
                '''                Current status of shared memories
                ''',
                'sr_shm_state',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('sr-shmwin-oor-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                sr shmwin oor count
                ''',
                'sr_shmwin_oor_count',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'resource-hardware-ingress-info',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Protocols.Protocol.Resource.ResourceHardwareEgressInfo.SrShmState' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Protocols.Protocol.Resource.ResourceHardwareEgressInfo.SrShmState',
            False, 
            [
            _MetaInfoClassMember('srs-avg-avail', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Average number of bytes available
                ''',
                'srs_avg_avail',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('srs-curr-mode', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                OOR mode for this shared memory window
                ''',
                'srs_curr_mode',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('srs-max-avail', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Maximum bytes available
                ''',
                'srs_max_avail',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'sr-shm-state',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Protocols.Protocol.Resource.ResourceHardwareEgressInfo' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Protocols.Protocol.Resource.ResourceHardwareEgressInfo',
            False, 
            [
            _MetaInfoClassMember('sr-curr-mode', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Current overall oor mode
                ''',
                'sr_curr_mode',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('sr-hw-oor-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                sr hw oor count
                ''',
                'sr_hw_oor_count',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('sr-hwrsrc-info', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Opaque hardware rsrc state info
                ''',
                'sr_hwrsrc_info',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('sr-hwrsrc-mode', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Hardware resource mode
                ''',
                'sr_hwrsrc_mode',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('sr-in-oor-ts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                sr in oor ts
                ''',
                'sr_in_oor_ts',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('sr-out-oor-ts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                sr out oor ts
                ''',
                'sr_out_oor_ts',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('sr-shm-state', REFERENCE_LIST, 'SrShmState' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Protocols.Protocol.Resource.ResourceHardwareEgressInfo.SrShmState', 
                [], [], 
                '''                Current status of shared memories
                ''',
                'sr_shm_state',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('sr-shmwin-oor-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                sr shmwin oor count
                ''',
                'sr_shmwin_oor_count',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'resource-hardware-egress-info',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Protocols.Protocol.Resource.ResourceSummaryInfo.SrShmState' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Protocols.Protocol.Resource.ResourceSummaryInfo.SrShmState',
            False, 
            [
            _MetaInfoClassMember('srs-avg-avail', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Average number of bytes available
                ''',
                'srs_avg_avail',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('srs-curr-mode', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                OOR mode for this shared memory window
                ''',
                'srs_curr_mode',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('srs-max-avail', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Maximum bytes available
                ''',
                'srs_max_avail',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'sr-shm-state',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Protocols.Protocol.Resource.ResourceSummaryInfo' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Protocols.Protocol.Resource.ResourceSummaryInfo',
            False, 
            [
            _MetaInfoClassMember('sr-curr-mode', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Current overall oor mode
                ''',
                'sr_curr_mode',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('sr-hw-oor-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                sr hw oor count
                ''',
                'sr_hw_oor_count',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('sr-hwrsrc-info', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Opaque hardware rsrc state info
                ''',
                'sr_hwrsrc_info',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('sr-hwrsrc-mode', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Hardware resource mode
                ''',
                'sr_hwrsrc_mode',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('sr-in-oor-ts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                sr in oor ts
                ''',
                'sr_in_oor_ts',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('sr-out-oor-ts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                sr out oor ts
                ''',
                'sr_out_oor_ts',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('sr-shm-state', REFERENCE_LIST, 'SrShmState' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Protocols.Protocol.Resource.ResourceSummaryInfo.SrShmState', 
                [], [], 
                '''                Current status of shared memories
                ''',
                'sr_shm_state',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('sr-shmwin-oor-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                sr shmwin oor count
                ''',
                'sr_shmwin_oor_count',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'resource-summary-info',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Protocols.Protocol.Resource' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Protocols.Protocol.Resource',
            False, 
            [
            _MetaInfoClassMember('resource-detail-info', REFERENCE_CLASS, 'ResourceDetailInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Protocols.Protocol.Resource.ResourceDetailInfo', 
                [], [], 
                '''                Detailed info
                ''',
                'resource_detail_info',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('resource-hardware-egress-info', REFERENCE_CLASS, 'ResourceHardwareEgressInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Protocols.Protocol.Resource.ResourceHardwareEgressInfo', 
                [], [], 
                '''                Detailed info with egress hardware info
                ''',
                'resource_hardware_egress_info',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('resource-hardware-ingress-info', REFERENCE_CLASS, 'ResourceHardwareIngressInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Protocols.Protocol.Resource.ResourceHardwareIngressInfo', 
                [], [], 
                '''                Detailed info with ingress hardware info
                ''',
                'resource_hardware_ingress_info',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('resource-summary-info', REFERENCE_CLASS, 'ResourceSummaryInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Protocols.Protocol.Resource.ResourceSummaryInfo', 
                [], [], 
                '''                Summary info
                ''',
                'resource_summary_info',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'resource',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Protocols.Protocol.FibSummaries.FibSummary.ExclusiveLoadSharingElement' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Protocols.Protocol.FibSummaries.FibSummary.ExclusiveLoadSharingElement',
            False, 
            [
            _MetaInfoClassMember('platform-shared-load-info-elements', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Count of platform shared Loadinfo elements
                ''',
                'platform_shared_load_info_elements',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('platform-shared-path-list-elements', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Count of platform shared Pathlist elements
                ''',
                'platform_shared_path_list_elements',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('recursive-load-info-elements', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Count of recursive Loadinfo elements
                ''',
                'recursive_load_info_elements',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('recursive-path-list-elements', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Count of recursive Pathlist elements
                ''',
                'recursive_path_list_elements',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('retry-path-list-elements', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Count of Pathlist elements in retry
                ''',
                'retry_path_list_elements',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('total-load-info-elements', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total count of Loadinfo elements
                ''',
                'total_load_info_elements',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('total-load-sharing-element-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total memory used by load sharing elements in
                bytes
                ''',
                'total_load_sharing_element_bytes',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('total-load-sharing-element-references', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total count of references to load sharing
                elements
                ''',
                'total_load_sharing_element_references',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('total-path-list-elements', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total count of Pathlist elements
                ''',
                'total_path_list_elements',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'exclusive-load-sharing-element',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Protocols.Protocol.FibSummaries.FibSummary.SharedLoadSharingElement' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Protocols.Protocol.FibSummaries.FibSummary.SharedLoadSharingElement',
            False, 
            [
            _MetaInfoClassMember('platform-shared-load-info-elements', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Count of platform shared Loadinfo elements
                ''',
                'platform_shared_load_info_elements',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('platform-shared-path-list-elements', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Count of platform shared Pathlist elements
                ''',
                'platform_shared_path_list_elements',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('recursive-load-info-elements', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Count of recursive Loadinfo elements
                ''',
                'recursive_load_info_elements',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('recursive-path-list-elements', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Count of recursive Pathlist elements
                ''',
                'recursive_path_list_elements',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('retry-path-list-elements', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Count of Pathlist elements in retry
                ''',
                'retry_path_list_elements',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('total-load-info-elements', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total count of Loadinfo elements
                ''',
                'total_load_info_elements',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('total-load-sharing-element-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total memory used by load sharing elements in
                bytes
                ''',
                'total_load_sharing_element_bytes',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('total-load-sharing-element-references', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total count of references to load sharing
                elements
                ''',
                'total_load_sharing_element_references',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('total-path-list-elements', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total count of Pathlist elements
                ''',
                'total_path_list_elements',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'shared-load-sharing-element',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Protocols.Protocol.FibSummaries.FibSummary.CrossSharedLoadSharingElement' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Protocols.Protocol.FibSummaries.FibSummary.CrossSharedLoadSharingElement',
            False, 
            [
            _MetaInfoClassMember('platform-shared-load-info-elements', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Count of platform shared Loadinfo elements
                ''',
                'platform_shared_load_info_elements',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('platform-shared-path-list-elements', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Count of platform shared Pathlist elements
                ''',
                'platform_shared_path_list_elements',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('recursive-load-info-elements', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Count of recursive Loadinfo elements
                ''',
                'recursive_load_info_elements',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('recursive-path-list-elements', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Count of recursive Pathlist elements
                ''',
                'recursive_path_list_elements',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('retry-path-list-elements', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Count of Pathlist elements in retry
                ''',
                'retry_path_list_elements',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('total-load-info-elements', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total count of Loadinfo elements
                ''',
                'total_load_info_elements',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('total-load-sharing-element-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total memory used by load sharing elements in
                bytes
                ''',
                'total_load_sharing_element_bytes',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('total-load-sharing-element-references', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total count of references to load sharing
                elements
                ''',
                'total_load_sharing_element_references',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('total-path-list-elements', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total count of Pathlist elements
                ''',
                'total_path_list_elements',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'cross-shared-load-sharing-element',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Protocols.Protocol.FibSummaries.FibSummary.LabelSharedLoadSharingElement' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Protocols.Protocol.FibSummaries.FibSummary.LabelSharedLoadSharingElement',
            False, 
            [
            _MetaInfoClassMember('platform-shared-load-info-elements', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Count of platform shared Loadinfo elements
                ''',
                'platform_shared_load_info_elements',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('platform-shared-path-list-elements', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Count of platform shared Pathlist elements
                ''',
                'platform_shared_path_list_elements',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('recursive-load-info-elements', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Count of recursive Loadinfo elements
                ''',
                'recursive_load_info_elements',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('recursive-path-list-elements', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Count of recursive Pathlist elements
                ''',
                'recursive_path_list_elements',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('retry-path-list-elements', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Count of Pathlist elements in retry
                ''',
                'retry_path_list_elements',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('total-load-info-elements', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total count of Loadinfo elements
                ''',
                'total_load_info_elements',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('total-load-sharing-element-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total memory used by load sharing elements in
                bytes
                ''',
                'total_load_sharing_element_bytes',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('total-load-sharing-element-references', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total count of references to load sharing
                elements
                ''',
                'total_load_sharing_element_references',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('total-path-list-elements', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total count of Pathlist elements
                ''',
                'total_path_list_elements',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'label-shared-load-sharing-element',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Protocols.Protocol.FibSummaries.FibSummary' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Protocols.Protocol.FibSummaries.FibSummary',
            False, 
            [
            _MetaInfoClassMember('cef-route-drops', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of routes dropped by CEF
                ''',
                'cef_route_drops',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('cef-version-mismatch-route-drops', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                the number of routes dropped due to version
                mismatch
                ''',
                'cef_version_mismatch_route_drops',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('cefl-bl-recycled-routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of routes updates with recycled label
                handled
                ''',
                'cefl_bl_recycled_routes',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('cross-shared-load-sharing-element', REFERENCE_CLASS, 'CrossSharedLoadSharingElement' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Protocols.Protocol.FibSummaries.FibSummary.CrossSharedLoadSharingElement', 
                [], [], 
                '''                Cross-table shared load sharing element
                ''',
                'cross_shared_load_sharing_element',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('delete-cache-num-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of entries in the route delete cache
                ''',
                'delete_cache_num_entries',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('exclusive-load-sharing-element', REFERENCE_CLASS, 'ExclusiveLoadSharingElement' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Protocols.Protocol.FibSummaries.FibSummary.ExclusiveLoadSharingElement', 
                [], [], 
                '''                Exclusive load sharing element
                ''',
                'exclusive_load_sharing_element',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('existing-leaves-revisions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of entries present on addition
                ''',
                'existing_leaves_revisions',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('extended-prefixes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of prefixes with extended path-list
                ''',
                'extended_prefixes',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fib-default-prefix', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Default prefix
                ''',
                'fib_default_prefix',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fib-default-prefix-mask-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Default prefix mask length
                ''',
                'fib_default_prefix_mask_length',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('forwarding-elements', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of forwarding elements linked to the
                table
                ''',
                'forwarding_elements',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('imposition-prefixes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of prefixes with imposition LDI
                ''',
                'imposition_prefixes',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('incomplete-next-hops', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of incomplete NHINFOS
                ''',
                'incomplete_next_hops',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('label-shared-load-sharing-element', REFERENCE_CLASS, 'LabelSharedLoadSharingElement' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Protocols.Protocol.FibSummaries.FibSummary.LabelSharedLoadSharingElement', 
                [], [], 
                '''                Label-shared load sharing element
                ''',
                'label_shared_load_sharing_element',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('ldi-backwalks', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                pd backwalks on LDI modify with backup path
                ''',
                'ldi_backwalks',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('leaves-used-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total memory used by leaves
                ''',
                'leaves_used_bytes',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('lisp-eid-prefixes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of lisp eid prefixes associated with
                table
                ''',
                'lisp_eid_prefixes',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('lisp-eid-valid-prefixes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of lisp eid prefixes eligible for
                forwarding
                ''',
                'lisp_eid_valid_prefixes',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('lisp-rloc-objects', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of lisp rloc objects associated with
                table
                ''',
                'lisp_rloc_objects',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('load-balancing', REFERENCE_ENUM_CLASS, 'SsLbaStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'SsLbaStateEnum', 
                [], [], 
                '''                LBA configuration state
                ''',
                'load_balancing',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('load-sharing-elements', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Count of load sharing elements
                ''',
                'load_sharing_elements',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('load-sharing-references', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Count of load sharing references
                ''',
                'load_sharing_references',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('max-resolution-timer', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IP CEF max resolution time in seconds
                ''',
                'max_resolution_timer',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('new-unresolve-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of new unresolved entries
                ''',
                'new_unresolve_entries',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('next-hops', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of NHINFOS
                ''',
                'next_hops',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('old-unresolve-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of old unresolved entries
                ''',
                'old_unresolve_entries',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                The router-id
                ''',
                'prefix',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('prefix-in-place-modifications', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of inplace modifications
                ''',
                'prefix_in_place_modifications',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('reresolve-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of reresolved entries
                ''',
                'reresolve_entries',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('resolution-timer', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IP CEF resolution timer in seconds
                ''',
                'resolution_timer',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of routes
                ''',
                'routes',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('shared-load-sharing-element', REFERENCE_CLASS, 'SharedLoadSharingElement' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Protocols.Protocol.FibSummaries.FibSummary.SharedLoadSharingElement', 
                [], [], 
                '''                Shared load sharing element
                ''',
                'shared_load_sharing_element',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('slow-process-timer', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IP CEF slow processing time in seconds
                ''',
                'slow_process_timer',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('ss-drop-pl-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of dropped pathlists
                ''',
                'ss_drop_pl_count',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('ss-prot-route-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of routes with FRR protection
                ''',
                'ss_prot_route_count',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('ss-tbl-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Table Id
                ''',
                'ss_tbl_id',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('ss-tbl-id-ptr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Table Id Ptr
                ''',
                'ss_tbl_id_ptr',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('ss-vr-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Virtual router instance Id
                ''',
                'ss_vr_id',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('ss-vrf-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Virtual routing forwarding instance Id
                ''',
                'ss_vrf_id',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('ss-vxlan-ltep-ifh', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                VXLAN local Interface handle
                ''',
                'ss_vxlan_ltep_ifh',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('stale-prefix-deletes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of deleted stale leafs
                ''',
                'stale_prefix_deletes',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('table-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                FIB table id
                ''',
                'table_id',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('total-load-share-element-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total memory used by load sharing elements
                ''',
                'total_load_share_element_bytes',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('unresolve-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of total unresolved entries
                ''',
                'unresolve_entries',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                VRF Name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'fib-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Protocols.Protocol.FibSummaries' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Protocols.Protocol.FibSummaries',
            False, 
            [
            _MetaInfoClassMember('fib-summary', REFERENCE_LIST, 'FibSummary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Protocols.Protocol.FibSummaries.FibSummary', 
                [], [], 
                '''                Summary for the requested fib table
                ''',
                'fib_summary',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'fib-summaries',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Protocols.Protocol.ExternalSummaryAll.SesaPlSum' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Protocols.Protocol.ExternalSummaryAll.SesaPlSum',
            False, 
            [
            _MetaInfoClassMember('sep-num-ecd-pathlist', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of ECD pathlists
                ''',
                'sep_num_ecd_pathlist',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('sep-num-ecd-pl-per-interest', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of ECD pathlists per interest
                ''',
                'sep_num_ecd_pl_per_interest',
                'Cisco-IOS-XR-fib-common-oper', False, max_elements=10),
            _MetaInfoClassMember('sep-num-ecd-pl-unresolved', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of ECD pathlists unresolved
                ''',
                'sep_num_ecd_pl_unresolved',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'sesa-pl-sum',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Protocols.Protocol.ExternalSummaryAll' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Protocols.Protocol.ExternalSummaryAll',
            False, 
            [
            _MetaInfoClassMember('sesa-num-client', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Client information
                ''',
                'sesa_num_client',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('sesa-pl-sum', REFERENCE_CLASS, 'SesaPlSum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Protocols.Protocol.ExternalSummaryAll.SesaPlSum', 
                [], [], 
                '''                External pathlist summary
                ''',
                'sesa_pl_sum',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'external-summary-all',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Protocols.Protocol.FrrLog.FrrInterfaces.FrrInterface.Logs.Log.FrrTimestamp' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Protocols.Protocol.FrrLog.FrrInterfaces.FrrInterface.Logs.Log.FrrTimestamp',
            False, 
            [
            _MetaInfoClassMember('nano-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                NanoSeconds
                ''',
                'nano_seconds',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Seconds
                ''',
                'seconds',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'frr-timestamp',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Protocols.Protocol.FrrLog.FrrInterfaces.FrrInterface.Logs.Log' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Protocols.Protocol.FrrLog.FrrInterfaces.FrrInterface.Logs.Log',
            False, 
            [
            _MetaInfoClassMember('log-index', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                FRR Log Index
                ''',
                'log_index',
                'Cisco-IOS-XR-fib-common-oper', True),
            _MetaInfoClassMember('bundle-member-interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                bundle member
                ''',
                'bundle_member_interface_name',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('frr-interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface assoc w frr nh
                ''',
                'frr_interface_name',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('frr-prefix', ATTRIBUTE, 'str' , None, None, 
                [(0, 52)], [], 
                '''                nh prefix
                ''',
                'frr_prefix',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('frr-protocol-type', REFERENCE_ENUM_CLASS, 'FibFrrProtocolShowEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'FibFrrProtocolShowEnum', 
                [], [], 
                '''                FIB Protocol Type
                ''',
                'frr_protocol_type',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('frr-switching-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                frr switching time
                ''',
                'frr_switching_time',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('frr-timestamp', REFERENCE_CLASS, 'FrrTimestamp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Protocols.Protocol.FrrLog.FrrInterfaces.FrrInterface.Logs.Log.FrrTimestamp', 
                [], [], 
                '''                frr timestamp
                ''',
                'frr_timestamp',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'log',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Protocols.Protocol.FrrLog.FrrInterfaces.FrrInterface.Logs' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Protocols.Protocol.FrrLog.FrrInterfaces.FrrInterface.Logs',
            False, 
            [
            _MetaInfoClassMember('log', REFERENCE_LIST, 'Log' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Protocols.Protocol.FrrLog.FrrInterfaces.FrrInterface.Logs.Log', 
                [], [], 
                '''                Specify index into frr log table
                ''',
                'log',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'logs',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Protocols.Protocol.FrrLog.FrrInterfaces.FrrInterface' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Protocols.Protocol.FrrLog.FrrInterfaces.FrrInterface',
            False, 
            [
            _MetaInfoClassMember('frr-interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface Name
                ''',
                'frr_interface_name',
                'Cisco-IOS-XR-fib-common-oper', True),
            _MetaInfoClassMember('logs', REFERENCE_CLASS, 'Logs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Protocols.Protocol.FrrLog.FrrInterfaces.FrrInterface.Logs', 
                [], [], 
                '''                FRR log table
                ''',
                'logs',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'frr-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Protocols.Protocol.FrrLog.FrrInterfaces' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Protocols.Protocol.FrrLog.FrrInterfaces',
            False, 
            [
            _MetaInfoClassMember('frr-interface', REFERENCE_LIST, 'FrrInterface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Protocols.Protocol.FrrLog.FrrInterfaces.FrrInterface', 
                [], [], 
                '''                Specify FRR Interface Name
                ''',
                'frr_interface',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'frr-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Protocols.Protocol.FrrLog' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Protocols.Protocol.FrrLog',
            False, 
            [
            _MetaInfoClassMember('frr-interfaces', REFERENCE_CLASS, 'FrrInterfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Protocols.Protocol.FrrLog.FrrInterfaces', 
                [], [], 
                '''                FRR Interface Table
                ''',
                'frr_interfaces',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'frr-log',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixDetails.IpPrefixDetail.DetailFibEntryInformation.LoadshareInformation.LoadInformtionInternalData.AdjacencyAddress' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixDetails.IpPrefixDetail.DetailFibEntryInformation.LoadshareInformation.LoadInformtionInternalData.AdjacencyAddress',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [(0, 60)], [], 
                '''                address
                ''',
                'address',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'adjacency-address',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixDetails.IpPrefixDetail.DetailFibEntryInformation.LoadshareInformation.LoadInformtionInternalData.PbtsClassIsFallbackMapped' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixDetails.IpPrefixDetail.DetailFibEntryInformation.LoadshareInformation.LoadInformtionInternalData.PbtsClassIsFallbackMapped',
            False, 
            [
            _MetaInfoClassMember('entry', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Array entry.
                ''',
                'entry',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'pbts-class-is-fallback-mapped',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixDetails.IpPrefixDetail.DetailFibEntryInformation.LoadshareInformation.LoadInformtionInternalData.PbtsFallbackToDrop' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixDetails.IpPrefixDetail.DetailFibEntryInformation.LoadshareInformation.LoadInformtionInternalData.PbtsFallbackToDrop',
            False, 
            [
            _MetaInfoClassMember('entry', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Array entry.
                ''',
                'entry',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'pbts-fallback-to-drop',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixDetails.IpPrefixDetail.DetailFibEntryInformation.LoadshareInformation.LoadInformtionInternalData.TunnelIsForwardClass' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixDetails.IpPrefixDetail.DetailFibEntryInformation.LoadshareInformation.LoadInformtionInternalData.TunnelIsForwardClass',
            False, 
            [
            _MetaInfoClassMember('entry', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Array entry.
                ''',
                'entry',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'tunnel-is-forward-class',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixDetails.IpPrefixDetail.DetailFibEntryInformation.LoadshareInformation.LoadInformtionInternalData' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixDetails.IpPrefixDetail.DetailFibEntryInformation.LoadshareInformation.LoadInformtionInternalData',
            False, 
            [
            _MetaInfoClassMember('adjacency-address', REFERENCE_LIST, 'AdjacencyAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixDetails.IpPrefixDetail.DetailFibEntryInformation.LoadshareInformation.LoadInformtionInternalData.AdjacencyAddress', 
                [], [], 
                '''                Adjacency address
                ''',
                'adjacency_address',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('interface-handle', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface handle
                ''',
                'interface_handle',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('is-pbts-info-valid', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                PBTS info valid flag
                ''',
                'is_pbts_info_valid',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('ldi-next-hop-buckets', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Number of LDI next hop buckets
                ''',
                'ldi_next_hop_buckets',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('level-ofldis', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                level of ldis
                ''',
                'level_ofldis',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('maximum-index-arrays', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum index of the arrays
                ''',
                'maximum_index_arrays',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('maximum-slots', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum slots
                ''',
                'maximum_slots',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('normalized-weights', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Normalized weights
                ''',
                'normalized_weights',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('number-of-ldis', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                no. of ldis
                ''',
                'number_of_ldis',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('path-indices', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Path indices
                ''',
                'path_indices',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('path-ldi-numbers', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Path indices
                ''',
                'path_ldi_numbers',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('pbts-class-is-fallback-mapped', REFERENCE_LIST, 'PbtsClassIsFallbackMapped' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixDetails.IpPrefixDetail.DetailFibEntryInformation.LoadshareInformation.LoadInformtionInternalData.PbtsClassIsFallbackMapped', 
                [], [], 
                '''                Does PBTS class fall back to drop or any class
                ''',
                'pbts_class_is_fallback_mapped',
                'Cisco-IOS-XR-fib-common-oper', False, max_elements=9, min_elements=9),
            _MetaInfoClassMember('pbts-class-num-paths', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                PBTS class num paths
                ''',
                'pbts_class_num_paths',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('pbts-class-offset', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                PBTS class offset
                ''',
                'pbts_class_offset',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('pbts-fallback-mapped-class', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                PBTS class falls back to class
                ''',
                'pbts_fallback_mapped_class',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('pbts-fallback-to-drop', REFERENCE_LIST, 'PbtsFallbackToDrop' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixDetails.IpPrefixDetail.DetailFibEntryInformation.LoadshareInformation.LoadInformtionInternalData.PbtsFallbackToDrop', 
                [], [], 
                '''                PBTS class falls back to drop
                ''',
                'pbts_fallback_to_drop',
                'Cisco-IOS-XR-fib-common-oper', False, max_elements=9, min_elements=9),
            _MetaInfoClassMember('platform-hardware-information', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Platform Hardware info
                ''',
                'platform_hardware_information',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('round-robin-disable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Round Robin Disable
                ''',
                'round_robin_disable',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('sanity-flag', REFERENCE_LEAFLIST, 'bool' , None, None, 
                [], [], 
                '''                Sanity flag
                ''',
                'sanity_flag',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('tunnel-class-value', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Tunnel class value
                ''',
                'tunnel_class_value',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('tunnel-is-forward-class', REFERENCE_LIST, 'TunnelIsForwardClass' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixDetails.IpPrefixDetail.DetailFibEntryInformation.LoadshareInformation.LoadInformtionInternalData.TunnelIsForwardClass', 
                [], [], 
                '''                Tunnel is forward class
                ''',
                'tunnel_is_forward_class',
                'Cisco-IOS-XR-fib-common-oper', False, max_elements=128, min_elements=128),
            _MetaInfoClassMember('weights-of-path', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Weights of paths
                ''',
                'weights_of_path',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'load-informtion-internal-data',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixDetails.IpPrefixDetail.DetailFibEntryInformation.LoadshareInformation' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixDetails.IpPrefixDetail.DetailFibEntryInformation.LoadshareInformation',
            False, 
            [
            _MetaInfoClassMember('bytes-through-load-information', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Bytes through this loadinfo
                ''',
                'bytes_through_load_information',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('is-owner', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Owner flag
                ''',
                'is_owner',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('load-information-owner-deleted-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Loadinfo owner deleted flag
                ''',
                'load_information_owner_deleted_flag',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('load-information-reference-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Loadinfo reference count
                ''',
                'load_information_reference_count',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('load-informtion-internal-data', REFERENCE_CLASS, 'LoadInformtionInternalData' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixDetails.IpPrefixDetail.DetailFibEntryInformation.LoadshareInformation.LoadInformtionInternalData', 
                [], [], 
                '''                Loadinfo internal data
                ''',
                'load_informtion_internal_data',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('loadinfo-sanity-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Loadinfo sanity flag
                ''',
                'loadinfo_sanity_flag',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('mask-length-of-owner', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Mask length of the owner
                ''',
                'mask_length_of_owner',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('packets-through-load-information', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Packets through this loadinfo
                ''',
                'packets_through_load_information',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('per-dest-load-sharing-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Per destination load sharing flag
                ''',
                'per_dest_load_sharing_flag',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('prefix-of-owner', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Prefix of the owner
                ''',
                'prefix_of_owner',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('total-bytes-through-load-information', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total bytes through this loadinfo
                ''',
                'total_bytes_through_load_information',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('total-packets-through-load-information', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total packets through this loadinfo
                ''',
                'total_packets_through_load_information',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'loadshare-information',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixDetails.IpPrefixDetail.DetailFibEntryInformation' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixDetails.IpPrefixDetail.DetailFibEntryInformation',
            False, 
            [
            _MetaInfoClassMember('adjacency-address-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ADJ ADDR LEN
                ''',
                'adjacency_address_length',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('adjacency-interface', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ADJ IFH
                ''',
                'adjacency_interface',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('afi-fib-protocol-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                AFI FIB protocol type
                ''',
                'afi_fib_protocol_type',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('aib-l3-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                AIB L3 Address
                ''',
                'aib_l3_address',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('bgp-attribute-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                BGP attribute id
                ''',
                'bgp_attribute_id',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('bgp-attribute-next-hop-as', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                BGP attribute next hop as
                ''',
                'bgp_attribute_next_hop_as',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('bgp-attribute-origin-as', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                BGP attribute origin as
                ''',
                'bgp_attribute_origin_as',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('bgp-local-attribute-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                BGP local attribute id
                ''',
                'bgp_local_attribute_id',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('bytes-through-fib-entry', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Bytes through this FIB entry
                ''',
                'bytes_through_fib_entry',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('com-string', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                com st
                ''',
                'com_string',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('detailed-prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Prefix length
                ''',
                'detailed_prefix_length',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('extcom-string', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                extcom st
                ''',
                'extcom_string',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('extended-community', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                extended community
                ''',
                'extended_community',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fast-adjacency-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Fast adjacency flag
                ''',
                'fast_adjacency_flag',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fib-entry-adjacency-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                FIB entry adj address
                ''',
                'fib_entry_adjacency_address',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fib-entry-adjacency-interface', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                FIB entry adjacency interface
                ''',
                'fib_entry_adjacency_interface',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fib-entry-adjacency-type', REFERENCE_ENUM_CLASS, 'FibAdjacencyShowEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'FibAdjacencyShowEnum', 
                [], [], 
                '''                FIB entry adjacency type
                ''',
                'fib_entry_adjacency_type',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fib-entry-version', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                FIB entry version number
                ''',
                'fib_entry_version',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fib-protocol-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                FIB Protocol type
                ''',
                'fib_protocol_type',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fib-special-nh-information-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                FIB Special NHINFO Type
                ''',
                'fib_special_nh_information_type',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('flow-tag', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                PBR flow-tag
                ''',
                'flow_tag',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('forward-class', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                SPP forwarding class ID
                ''',
                'forward_class',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('illegal-fast-adjacency-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Illegal fast adjacency flag
                ''',
                'illegal_fast_adjacency_flag',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('ldi-time-of-last-update-in-msec', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The time of last update for LDI in msec
                ''',
                'ldi_time_of_last_update_in_msec',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('load-sharing-type', REFERENCE_ENUM_CLASS, 'FibLoadshareShowEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'FibLoadshareShowEnum', 
                [], [], 
                '''                Load sharing type
                ''',
                'load_sharing_type',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('loadshare-information', REFERENCE_CLASS, 'LoadshareInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixDetails.IpPrefixDetail.DetailFibEntryInformation.LoadshareInformation', 
                [], [], 
                '''                Detailed Loadshare info
                ''',
                'loadshare_information',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('lwldi-time-of-last-update-in-msec', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The time of last update for LW-LDI in msec
                ''',
                'lwldi_time_of_last_update_in_msec',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('mpls-fec', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                mpls fec
                ''',
                'mpls_fec',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('packets-through-fib-entry', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Packets through this FIB entry
                ''',
                'packets_through_fib_entry',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('path-string', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                As path string
                ''',
                'path_string',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('per-prefix-accounting', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Per Prefix Accounting
                ''',
                'per_prefix_accounting',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('pl-time-of-last-update-in-msec', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The time of last update for PL in msec
                ''',
                'pl_time_of_last_update_in_msec',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('pl-time-stamp-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The type of time-stamp on PL
                ''',
                'pl_time_stamp_type',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('precedence-forpackets', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Precedence for packets to this entry
                ''',
                'precedence_forpackets',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('prefix-protocol', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Prefix protocol
                ''',
                'prefix_protocol',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('qos-group', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                qos group
                ''',
                'qos_group',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('qppb-qos-group-and-ip-precedence', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                qppb QOS group and IP precedence
                ''',
                'qppb_qos_group_and_ip_precedence',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('remote-adjacency-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Remote adjacency flag
                ''',
                'remote_adjacency_flag',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('switch-compontent-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Switch function compontent ID
                ''',
                'switch_compontent_id',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('traffic-index-for-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Traffic index for packets to this entry
                ''',
                'traffic_index_for_packets',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'detail-fib-entry-information',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixDetails.IpPrefixDetail.FibEntryPath.FibShTblPath.MoreDetailAboutPath.SpdIpencap.IpEncapHdr' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixDetails.IpPrefixDetail.FibEntryPath.FibShTblPath.MoreDetailAboutPath.SpdIpencap.IpEncapHdr',
            False, 
            [
            _MetaInfoClassMember('ip-encap-hdr-dyn', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Dynamic Header Fields
                ''',
                'ip_encap_hdr_dyn',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('ip-encap-hdr-type', REFERENCE_ENUM_CLASS, 'FibShIpencapHdrEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'FibShIpencapHdrEnum', 
                [], [], 
                '''                Header Type
                ''',
                'ip_encap_hdr_type',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('ip-encap-hdrp', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Static Header
                ''',
                'ip_encap_hdrp',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'ip-encap-hdr',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixDetails.IpPrefixDetail.FibEntryPath.FibShTblPath.MoreDetailAboutPath.SpdIpencap' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixDetails.IpPrefixDetail.FibEntryPath.FibShTblPath.MoreDetailAboutPath.SpdIpencap',
            False, 
            [
            _MetaInfoClassMember('ip-encap-hdr', REFERENCE_LIST, 'IpEncapHdr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixDetails.IpPrefixDetail.FibEntryPath.FibShTblPath.MoreDetailAboutPath.SpdIpencap.IpEncapHdr', 
                [], [], 
                '''                Headers
                ''',
                'ip_encap_hdr',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('ip-encap-hdr-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Header Count
                ''',
                'ip_encap_hdr_count',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('ip-encap-locks', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IPEncap Object Locks
                ''',
                'ip_encap_locks',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('ip-encap-parent', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Pointer to parent
                ''',
                'ip_encap_parent',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('ip-encap-parent-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Parent type enumeration
                ''',
                'ip_encap_parent_type',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('ip-encap-payload-af', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Payload AF
                ''',
                'ip_encap_payload_af',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('ip-encap-payload-mtu', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Payload MTU
                ''',
                'ip_encap_payload_mtu',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('ip-encap-transport-af', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Transport AF
                ''',
                'ip_encap_transport_af',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('ip-encap-transport-tbl', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Transport Table
                ''',
                'ip_encap_transport_tbl',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('ipe-transport-vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Transport VRF name
                ''',
                'ipe_transport_vrf_name',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'spd-ipencap',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixDetails.IpPrefixDetail.FibEntryPath.FibShTblPath.MoreDetailAboutPath' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixDetails.IpPrefixDetail.FibEntryPath.FibShTblPath.MoreDetailAboutPath',
            False, 
            [
            _MetaInfoClassMember('current-path-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Current path flag
                ''',
                'current_path_flag',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('detail-fib-adjacency-type', REFERENCE_ENUM_CLASS, 'FibAdjacencyShowEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'FibAdjacencyShowEnum', 
                [], [], 
                '''                FIB entry adjacency type
                ''',
                'detail_fib_adjacency_type',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('detail-next-hop-prefix', ATTRIBUTE, 'str' , None, None, 
                [(0, 52)], [], 
                '''                Next hop prefix
                ''',
                'detail_next_hop_prefix',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('external-adjacency', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Path is an external adjacency
                ''',
                'external_adjacency',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fib-path-nh-information-type', REFERENCE_ENUM_CLASS, 'FibNehEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'FibNehEnum', 
                [], [], 
                '''                FIB Nhinfo type
                ''',
                'fib_path_nh_information_type',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fib-path-nh-information-type-special', REFERENCE_ENUM_CLASS, 'FibNehSpecialEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'FibNehSpecialEnum', 
                [], [], 
                '''                FIB Nhinfo type special
                ''',
                'fib_path_nh_information_type_special',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('interface-associated-path', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface associated with this path
                ''',
                'interface_associated_path',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('ip-address-to-recurse', ATTRIBUTE, 'str' , None, None, 
                [(0, 52)], [], 
                '''                IP address to recurse to
                ''',
                'ip_address_to_recurse',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('label-to-recurse', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Local label to recurse over
                ''',
                'label_to_recurse',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('lisprlocid', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LISP RLOC ID
                ''',
                'lisprlocid',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('next-hop-interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Next hop interface
                ''',
                'next_hop_interface',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('next-hop-mask-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Next hop mask length
                ''',
                'next_hop_mask_length',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('next-hop-vrf', ATTRIBUTE, 'str' , None, None, 
                [(0, 33)], [], 
                '''                Next hop VRF
                ''',
                'next_hop_vrf',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('next-prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Next prefix length
                ''',
                'next_prefix_length',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('next-prefix-length2', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Next prefix2 length
                ''',
                'next_prefix_length2',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('next-prefix-recursion', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Next prefix recursion in the path
                ''',
                'next_prefix_recursion',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('next-prefix-recursion2', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Next prefix2 recursion in the path
                ''',
                'next_prefix_recursion2',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('number-of-dependencies-this-path', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                No. of dependents for this path
                ''',
                'number_of_dependencies_this_path',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('recurse-prefix-object', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is recursion object a leaf?
                ''',
                'recurse_prefix_object',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('recurse-prefix-object2', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Recursion has two leaves (e.g. implicit-null
                path)
                ''',
                'recurse_prefix_object2',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('recursive-path-information', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Recursive path information is available
                ''',
                'recursive_path_information',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('robin-reset-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Round robin reset value
                ''',
                'robin_reset_value',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('spd-ipencap', REFERENCE_LIST, 'SpdIpencap' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixDetails.IpPrefixDetail.FibEntryPath.FibShTblPath.MoreDetailAboutPath.SpdIpencap', 
                [], [], 
                '''                IP Encap
                ''',
                'spd_ipencap',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('tunnel-class', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Tunnel class of the path
                ''',
                'tunnel_class',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('tunnel-is-forward-class', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Tunnel is forward class
                ''',
                'tunnel_is_forward_class',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('tunnle-endpoint-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Tunnel endpoint id
                ''',
                'tunnle_endpoint_id',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('weight-of-path', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Weight of the path
                ''',
                'weight_of_path',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'more-detail-about-path',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixDetails.IpPrefixDetail.FibEntryPath.FibShTblPath.MplsInformationForPath.IgpLabelStackArray' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixDetails.IpPrefixDetail.FibEntryPath.FibShTblPath.MplsInformationForPath.IgpLabelStackArray',
            False, 
            [
            _MetaInfoClassMember('lstack', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                lstack
                ''',
                'lstack',
                'Cisco-IOS-XR-fib-common-oper', False, max_elements=14),
            _MetaInfoClassMember('nh-address', ATTRIBUTE, 'str' , None, None, 
                [(0, 52)], [], 
                '''                NHAddress
                ''',
                'nh_address',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('number-of-labels', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                NumberOfLabels
                ''',
                'number_of_labels',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('out-interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                OutInterface
                ''',
                'out_interface',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'igp-label-stack-array',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixDetails.IpPrefixDetail.FibEntryPath.FibShTblPath.MplsInformationForPath' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixDetails.IpPrefixDetail.FibEntryPath.FibShTblPath.MplsInformationForPath',
            False, 
            [
            _MetaInfoClassMember('igp-label-stack-array', REFERENCE_LIST, 'IgpLabelStackArray' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixDetails.IpPrefixDetail.FibEntryPath.FibShTblPath.MplsInformationForPath.IgpLabelStackArray', 
                [], [], 
                '''                igp label stack array
                ''',
                'igp_label_stack_array',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('local-lable', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LocalLable
                ''',
                'local_lable',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('number-of-igp-paths', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                NumberOfIGPPaths
                ''',
                'number_of_igp_paths',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('recursive-fwd-chain', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                RecursiveFwdChain
                ''',
                'recursive_fwd_chain',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('recursive-out-label-valid', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                RecursiveOutLabelValid
                ''',
                'recursive_out_label_valid',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('recursive-out-lable', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                RecursiveOutLable
                ''',
                'recursive_out_lable',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('remote-backup', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                RemoteBackupPath
                ''',
                'remote_backup',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'mpls-information-for-path',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixDetails.IpPrefixDetail.FibEntryPath.FibShTblPath' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixDetails.IpPrefixDetail.FibEntryPath.FibShTblPath',
            False, 
            [
            _MetaInfoClassMember('attached-path', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Attached path
                ''',
                'attached_path',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('backup-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Backup path index
                ''',
                'backup_index',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('backup-path', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Backup path
                ''',
                'backup_path',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('best-external-path', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Best external path
                ''',
                'best_external_path',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('brief-interface-handle', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface handle
                ''',
                'brief_interface_handle',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('brief-lfa-protection-type', REFERENCE_ENUM_CLASS, 'FibUpdatePathLfaProtectionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'FibUpdatePathLfaProtectionEnum', 
                [], [], 
                '''                LFA protection type
                ''',
                'brief_lfa_protection_type',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('brief-next-hop-prefix', ATTRIBUTE, 'str' , None, None, 
                [(0, 52)], [], 
                '''                Next hop prefix
                ''',
                'brief_next_hop_prefix',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('brief-pnode-address', ATTRIBUTE, 'str' , None, None, 
                [(0, 52)], [], 
                '''                P-node address
                ''',
                'brief_pnode_address',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('brief-qnode-address', ATTRIBUTE, 'str' , None, None, 
                [(0, 52)], [], 
                '''                Q-node address
                ''',
                'brief_qnode_address',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('hardware-information', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Hardware info
                ''',
                'hardware_information',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('more-detail-about-path', REFERENCE_CLASS, 'MoreDetailAboutPath' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixDetails.IpPrefixDetail.FibEntryPath.FibShTblPath.MoreDetailAboutPath', 
                [], [], 
                '''                More detail about this path entry
                ''',
                'more_detail_about_path',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('mpls-information-for-path', REFERENCE_CLASS, 'MplsInformationForPath' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixDetails.IpPrefixDetail.FibEntryPath.FibShTblPath.MplsInformationForPath', 
                [], [], 
                '''                mpls info for this path entry
                ''',
                'mpls_information_for_path',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('next-hop-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Next Hop Index
                ''',
                'next_hop_index',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('packets-received-path', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Packets received on this path
                ''',
                'packets_received_path',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('parent-interface-handle', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Parent Interface Handle
                ''',
                'parent_interface_handle',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('path-dlb', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is this the path used for DLB
                ''',
                'path_dlb',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('path-flags', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Path flags
                ''',
                'path_flags',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('path-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Path index
                ''',
                'path_index',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('path-info-flags', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Path Info flags
                ''',
                'path_info_flags',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('protect-ignore', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is protection ignored
                ''',
                'protect_ignore',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('recursionvia-len', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                recursion via /N constraint
                ''',
                'recursionvia_len',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('recursive-path', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Recursive path
                ''',
                'recursive_path',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('resolved-path', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Resolved path
                ''',
                'resolved_path',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('via-label-to-recurse', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Local label to recurse over
                ''',
                'via_label_to_recurse',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'fib-sh-tbl-path',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixDetails.IpPrefixDetail.FibEntryPath' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixDetails.IpPrefixDetail.FibEntryPath',
            False, 
            [
            _MetaInfoClassMember('fib-sh-tbl-path', REFERENCE_LIST, 'FibShTblPath' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixDetails.IpPrefixDetail.FibEntryPath.FibShTblPath', 
                [], [], 
                '''                fib sh tbl path
                ''',
                'fib_sh_tbl_path',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'fib-entry-path',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixDetails.IpPrefixDetail.Srv6Information.Srv6Statistics' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixDetails.IpPrefixDetail.Srv6Information.Srv6Statistics',
            False, 
            [
            _MetaInfoClassMember('srv6-packets-dropped', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                SRv6 Packets dropped for a prefix
                ''',
                'srv6_packets_dropped',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('srv6-packets-forwarded', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                SRv6 packets forwarded for a prefix
                ''',
                'srv6_packets_forwarded',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'srv6-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixDetails.IpPrefixDetail.Srv6Information' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixDetails.IpPrefixDetail.Srv6Information',
            False, 
            [
            _MetaInfoClassMember('route-is-sripv6-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Route is an IPv6 Segment-Routing prefix
                ''',
                'route_is_sripv6_flag',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('sripv6-stats-valid-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Statistics are valid for this prefix
                ''',
                'sripv6_stats_valid_flag',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('srv6-pfx-resolved-via-policy-label', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Route is a SRv6 prefix resolved via Policy label
                ''',
                'srv6_pfx_resolved_via_policy_label',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('srv6-statistics', REFERENCE_CLASS, 'Srv6Statistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixDetails.IpPrefixDetail.Srv6Information.Srv6Statistics', 
                [], [], 
                '''                Statistics for a IPv6 SR prefix
                ''',
                'srv6_statistics',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'srv6-information',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixDetails.IpPrefixDetail.ExtensionObject.SfecdLe' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixDetails.IpPrefixDetail.ExtensionObject.SfecdLe',
            False, 
            [
            _MetaInfoClassMember('context-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Context Label
                ''',
                'context_label',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('context-label-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Context Label Exist
                ''',
                'context_label_flag',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'sfecd-le',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixDetails.IpPrefixDetail.ExtensionObject' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixDetails.IpPrefixDetail.ExtensionObject',
            False, 
            [
            _MetaInfoClassMember('sfecd-le', REFERENCE_CLASS, 'SfecdLe' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixDetails.IpPrefixDetail.ExtensionObject.SfecdLe', 
                [], [], 
                '''                sfecd le
                ''',
                'sfecd_le',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'FibShTblFibExtBagEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'FibShTblFibExtBagEnum', 
                [], [], 
                '''                type
                ''',
                'type',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'extension-object',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixDetails.IpPrefixDetail' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixDetails.IpPrefixDetail',
            False, 
            [
            _MetaInfoClassMember('broadcast-forward-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Broadcast forward flag
                ''',
                'broadcast_forward_flag',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('broadcast-recive-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Broadcast receive flag
                ''',
                'broadcast_recive_flag',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('detail-fib-entry-information', REFERENCE_CLASS, 'DetailFibEntryInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixDetails.IpPrefixDetail.DetailFibEntryInformation', 
                [], [], 
                '''                Detailed FIB entry information
                ''',
                'detail_fib_entry_information',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('dummy-real-zero-route', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Dummy real zero route
                ''',
                'dummy_real_zero_route',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('exact-route-result', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                exact-route result
                ''',
                'exact_route_result',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('extension-object', REFERENCE_LIST, 'ExtensionObject' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixDetails.IpPrefixDetail.ExtensionObject', 
                [], [], 
                '''                Leaf Extension Object List
                ''',
                'extension_object',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('external-switch-triggered', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                External switch function triggered
                ''',
                'external_switch_triggered',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fib-entry-path', REFERENCE_CLASS, 'FibEntryPath' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixDetails.IpPrefixDetail.FibEntryPath', 
                [], [], 
                '''                FIB entry path details
                ''',
                'fib_entry_path',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fib-route-download-priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Priority at which the route was downloaded
                ''',
                'fib_route_download_priority',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('flags-external-ldi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The flags of ext assocaited with LDI 
                ''',
                'flags_external_ldi',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('l2-subscriber-ip-protocol', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IP protocol associated with L2 subscriber
                ''',
                'l2_subscriber_ip_protocol',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('l2-subscriber-route', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is L2 Subscriber route
                ''',
                'l2_subscriber_route',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('l2-subscriber-xconnect-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                XConnect-id associated with L2 subscriber
                ''',
                'l2_subscriber_xconnect_id',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('l2tpv3-cookie-length-bits', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                L2TPv3 cookie length for L2 subscriber
                ''',
                'l2tpv3_cookie_length_bits',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('ldi-flags', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The LDI flags
                ''',
                'ldi_flags',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('ldi-lw-flag', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The LDI LW flags
                ''',
                'ldi_lw_flag',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('lspa-flags', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The LSPA flags
                ''',
                'lspa_flags',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('number-of-referances-to-ldi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of references to the LDI
                ''',
                'number_of_referances_to_ldi',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('number-of-referances-to-path-list', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of references to the pathlist
                ''',
                'number_of_referances_to_path_list',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('packet-should-recieve', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Packet should always be received
                ''',
                'packet_should_recieve',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('path-list-flags', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The pathlist flags
                ''',
                'path_list_flags',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('path-list-source', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The pathlist source
                ''',
                'path_list_source',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('platform-hardware', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Platform Hardware info
                ''',
                'platform_hardware',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('prefix', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Destination IP address
                ''',
                'prefix',
                'Cisco-IOS-XR-fib-common-oper', False, [
                    _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Destination IP address
                        ''',
                        'prefix',
                        'Cisco-IOS-XR-fib-common-oper', False),
                    _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Destination IP address
                        ''',
                        'prefix',
                        'Cisco-IOS-XR-fib-common-oper', False),
                ]),
            _MetaInfoClassMember('prefix-connected', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Prefix is connected
                ''',
                'prefix_connected',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('prefix-for-adjancency', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Prefix is for an adjacency
                ''',
                'prefix_for_adjancency',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('prefix-for-pic-next-hop', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Prefix is for a PIC nexthop
                ''',
                'prefix_for_pic_next_hop',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('prefix-is-static-or-connected', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Prefix is static or connected
                ''',
                'prefix_is_static_or_connected',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '128')], [], 
                '''                IP prefix length
                ''',
                'prefix_length',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('protocol-type-fib-entry', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Proto type for this entry
                ''',
                'protocol_type_fib_entry',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('purgable-after-purge-interval', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Purgable after the purge interval
                ''',
                'purgable_after_purge_interval',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('ref-counter-of-ldi-lw-ldi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The refcounter of LDI LW LDI
                ''',
                'ref_counter_of_ldi_lw_ldi',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('route-attribute-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Route attributes summary flag
                ''',
                'route_attribute_flag',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('route-for-external-reach-linecard-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Route destined for Line Card that support
                External Reach only
                ''',
                'route_for_external_reach_linecard_flag',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('route-is-sr-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Route is a MPLS Segment-Routing prefix
                ''',
                'route_is_sr_flag',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('srv6-information', REFERENCE_CLASS, 'Srv6Information' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixDetails.IpPrefixDetail.Srv6Information', 
                [], [], 
                '''                Information about IPv6 SR prefix
                ''',
                'srv6_information',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('time-of-last-update-in-msec', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The time of last update in msec
                ''',
                'time_of_last_update_in_msec',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('type-of-ldi-lw-ldi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The type of LDI LW LDI
                ''',
                'type_of_ldi_lw_ldi',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('version-of-route', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The version of the route
                ''',
                'version_of_route',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('zero-by-zero-route-as-default', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                0/0 route added as default route
                ''',
                'zero_by_zero_route_as_default',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'ip-prefix-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixDetails' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixDetails',
            False, 
            [
            _MetaInfoClassMember('ip-prefix-detail', REFERENCE_LIST, 'IpPrefixDetail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixDetails.IpPrefixDetail', 
                [], [], 
                '''                IP FIB prefix detail table entry
                ''',
                'ip_prefix_detail',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'ip-prefix-details',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.Summary.ExclusiveLoadSharingElement' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.Summary.ExclusiveLoadSharingElement',
            False, 
            [
            _MetaInfoClassMember('platform-shared-load-info-elements', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Count of platform shared Loadinfo elements
                ''',
                'platform_shared_load_info_elements',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('platform-shared-path-list-elements', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Count of platform shared Pathlist elements
                ''',
                'platform_shared_path_list_elements',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('recursive-load-info-elements', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Count of recursive Loadinfo elements
                ''',
                'recursive_load_info_elements',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('recursive-path-list-elements', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Count of recursive Pathlist elements
                ''',
                'recursive_path_list_elements',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('retry-path-list-elements', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Count of Pathlist elements in retry
                ''',
                'retry_path_list_elements',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('total-load-info-elements', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total count of Loadinfo elements
                ''',
                'total_load_info_elements',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('total-load-sharing-element-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total memory used by load sharing elements in
                bytes
                ''',
                'total_load_sharing_element_bytes',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('total-load-sharing-element-references', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total count of references to load sharing
                elements
                ''',
                'total_load_sharing_element_references',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('total-path-list-elements', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total count of Pathlist elements
                ''',
                'total_path_list_elements',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'exclusive-load-sharing-element',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.Summary.SharedLoadSharingElement' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.Summary.SharedLoadSharingElement',
            False, 
            [
            _MetaInfoClassMember('platform-shared-load-info-elements', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Count of platform shared Loadinfo elements
                ''',
                'platform_shared_load_info_elements',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('platform-shared-path-list-elements', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Count of platform shared Pathlist elements
                ''',
                'platform_shared_path_list_elements',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('recursive-load-info-elements', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Count of recursive Loadinfo elements
                ''',
                'recursive_load_info_elements',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('recursive-path-list-elements', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Count of recursive Pathlist elements
                ''',
                'recursive_path_list_elements',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('retry-path-list-elements', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Count of Pathlist elements in retry
                ''',
                'retry_path_list_elements',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('total-load-info-elements', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total count of Loadinfo elements
                ''',
                'total_load_info_elements',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('total-load-sharing-element-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total memory used by load sharing elements in
                bytes
                ''',
                'total_load_sharing_element_bytes',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('total-load-sharing-element-references', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total count of references to load sharing
                elements
                ''',
                'total_load_sharing_element_references',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('total-path-list-elements', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total count of Pathlist elements
                ''',
                'total_path_list_elements',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'shared-load-sharing-element',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.Summary.CrossSharedLoadSharingElement' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.Summary.CrossSharedLoadSharingElement',
            False, 
            [
            _MetaInfoClassMember('platform-shared-load-info-elements', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Count of platform shared Loadinfo elements
                ''',
                'platform_shared_load_info_elements',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('platform-shared-path-list-elements', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Count of platform shared Pathlist elements
                ''',
                'platform_shared_path_list_elements',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('recursive-load-info-elements', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Count of recursive Loadinfo elements
                ''',
                'recursive_load_info_elements',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('recursive-path-list-elements', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Count of recursive Pathlist elements
                ''',
                'recursive_path_list_elements',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('retry-path-list-elements', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Count of Pathlist elements in retry
                ''',
                'retry_path_list_elements',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('total-load-info-elements', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total count of Loadinfo elements
                ''',
                'total_load_info_elements',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('total-load-sharing-element-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total memory used by load sharing elements in
                bytes
                ''',
                'total_load_sharing_element_bytes',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('total-load-sharing-element-references', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total count of references to load sharing
                elements
                ''',
                'total_load_sharing_element_references',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('total-path-list-elements', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total count of Pathlist elements
                ''',
                'total_path_list_elements',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'cross-shared-load-sharing-element',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.Summary.LabelSharedLoadSharingElement' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.Summary.LabelSharedLoadSharingElement',
            False, 
            [
            _MetaInfoClassMember('platform-shared-load-info-elements', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Count of platform shared Loadinfo elements
                ''',
                'platform_shared_load_info_elements',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('platform-shared-path-list-elements', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Count of platform shared Pathlist elements
                ''',
                'platform_shared_path_list_elements',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('recursive-load-info-elements', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Count of recursive Loadinfo elements
                ''',
                'recursive_load_info_elements',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('recursive-path-list-elements', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Count of recursive Pathlist elements
                ''',
                'recursive_path_list_elements',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('retry-path-list-elements', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Count of Pathlist elements in retry
                ''',
                'retry_path_list_elements',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('total-load-info-elements', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total count of Loadinfo elements
                ''',
                'total_load_info_elements',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('total-load-sharing-element-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total memory used by load sharing elements in
                bytes
                ''',
                'total_load_sharing_element_bytes',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('total-load-sharing-element-references', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total count of references to load sharing
                elements
                ''',
                'total_load_sharing_element_references',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('total-path-list-elements', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total count of Pathlist elements
                ''',
                'total_path_list_elements',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'label-shared-load-sharing-element',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.Summary' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.Summary',
            False, 
            [
            _MetaInfoClassMember('cef-route-drops', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of routes dropped by CEF
                ''',
                'cef_route_drops',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('cef-version-mismatch-route-drops', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                the number of routes dropped due to version
                mismatch
                ''',
                'cef_version_mismatch_route_drops',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('cefl-bl-recycled-routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of routes updates with recycled label
                handled
                ''',
                'cefl_bl_recycled_routes',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('cross-shared-load-sharing-element', REFERENCE_CLASS, 'CrossSharedLoadSharingElement' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.Summary.CrossSharedLoadSharingElement', 
                [], [], 
                '''                Cross-table shared load sharing element
                ''',
                'cross_shared_load_sharing_element',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('delete-cache-num-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of entries in the route delete cache
                ''',
                'delete_cache_num_entries',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('exclusive-load-sharing-element', REFERENCE_CLASS, 'ExclusiveLoadSharingElement' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.Summary.ExclusiveLoadSharingElement', 
                [], [], 
                '''                Exclusive load sharing element
                ''',
                'exclusive_load_sharing_element',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('existing-leaves-revisions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of entries present on addition
                ''',
                'existing_leaves_revisions',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('extended-prefixes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of prefixes with extended path-list
                ''',
                'extended_prefixes',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fib-default-prefix', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Default prefix
                ''',
                'fib_default_prefix',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fib-default-prefix-mask-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Default prefix mask length
                ''',
                'fib_default_prefix_mask_length',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('forwarding-elements', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of forwarding elements linked to the
                table
                ''',
                'forwarding_elements',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('imposition-prefixes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of prefixes with imposition LDI
                ''',
                'imposition_prefixes',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('incomplete-next-hops', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of incomplete NHINFOS
                ''',
                'incomplete_next_hops',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('label-shared-load-sharing-element', REFERENCE_CLASS, 'LabelSharedLoadSharingElement' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.Summary.LabelSharedLoadSharingElement', 
                [], [], 
                '''                Label-shared load sharing element
                ''',
                'label_shared_load_sharing_element',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('ldi-backwalks', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                pd backwalks on LDI modify with backup path
                ''',
                'ldi_backwalks',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('leaves-used-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total memory used by leaves
                ''',
                'leaves_used_bytes',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('lisp-eid-prefixes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of lisp eid prefixes associated with
                table
                ''',
                'lisp_eid_prefixes',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('lisp-eid-valid-prefixes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of lisp eid prefixes eligible for
                forwarding
                ''',
                'lisp_eid_valid_prefixes',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('lisp-rloc-objects', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of lisp rloc objects associated with
                table
                ''',
                'lisp_rloc_objects',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('load-balancing', REFERENCE_ENUM_CLASS, 'SsLbaStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'SsLbaStateEnum', 
                [], [], 
                '''                LBA configuration state
                ''',
                'load_balancing',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('load-sharing-elements', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Count of load sharing elements
                ''',
                'load_sharing_elements',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('load-sharing-references', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Count of load sharing references
                ''',
                'load_sharing_references',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('max-resolution-timer', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IP CEF max resolution time in seconds
                ''',
                'max_resolution_timer',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('new-unresolve-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of new unresolved entries
                ''',
                'new_unresolve_entries',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('next-hops', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of NHINFOS
                ''',
                'next_hops',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('old-unresolve-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of old unresolved entries
                ''',
                'old_unresolve_entries',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                The router-id
                ''',
                'prefix',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('prefix-in-place-modifications', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of inplace modifications
                ''',
                'prefix_in_place_modifications',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('reresolve-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of reresolved entries
                ''',
                'reresolve_entries',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('resolution-timer', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IP CEF resolution timer in seconds
                ''',
                'resolution_timer',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of routes
                ''',
                'routes',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('shared-load-sharing-element', REFERENCE_CLASS, 'SharedLoadSharingElement' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.Summary.SharedLoadSharingElement', 
                [], [], 
                '''                Shared load sharing element
                ''',
                'shared_load_sharing_element',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('slow-process-timer', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IP CEF slow processing time in seconds
                ''',
                'slow_process_timer',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('ss-drop-pl-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of dropped pathlists
                ''',
                'ss_drop_pl_count',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('ss-prot-route-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of routes with FRR protection
                ''',
                'ss_prot_route_count',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('ss-tbl-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Table Id
                ''',
                'ss_tbl_id',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('ss-tbl-id-ptr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Table Id Ptr
                ''',
                'ss_tbl_id_ptr',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('ss-vr-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Virtual router instance Id
                ''',
                'ss_vr_id',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('ss-vrf-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Virtual routing forwarding instance Id
                ''',
                'ss_vrf_id',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('ss-vxlan-ltep-ifh', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                VXLAN local Interface handle
                ''',
                'ss_vxlan_ltep_ifh',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('stale-prefix-deletes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of deleted stale leafs
                ''',
                'stale_prefix_deletes',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('total-load-share-element-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total memory used by load sharing elements
                ''',
                'total_load_share_element_bytes',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('unresolve-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of total unresolved entries
                ''',
                'unresolve_entries',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'summary',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.InterfaceInfos.InterfaceInfo.Interfaces.Interface.DetailFibIntInformation' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.InterfaceInfos.InterfaceInfo.Interfaces.Interface.DetailFibIntInformation',
            False, 
            [
            _MetaInfoClassMember('bgp-pa-input-configured-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                BGP PA configured flag
                ''',
                'bgp_pa_input_configured_flag',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('bgp-pa-output-configured-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                BGP PA configured flag
                ''',
                'bgp_pa_output_configured_flag',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('default-route-with-rpf', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Allow default route with RPF
                ''',
                'default_route_with_rpf',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('destination-bgp-pa-input-configured-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                dst BGP PA configured flag
                ''',
                'destination_bgp_pa_input_configured_flag',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('destination-bgp-pa-output-configured-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                dst BGP PA configured flag
                ''',
                'destination_bgp_pa_output_configured_flag',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('forwarding-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Forwarding enabled/disabled flag
                ''',
                'forwarding_flag',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('icmp-flag', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ICMP  configured flag
                ''',
                'icmp_flag',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('interface-mtu', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Interface Protocol MTU
                ''',
                'interface_mtu',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('multi-label-drop-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Drop packets with multiple-label-stack if set
                ''',
                'multi_label_drop_flag',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('rpf-configured-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                RPF configured flag
                ''',
                'rpf_configured_flag',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('rpf-mode', REFERENCE_ENUM_CLASS, 'FibRpfModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'FibRpfModeEnum', 
                [], [], 
                '''                RPF mode
                ''',
                'rpf_mode',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('self-ping-with-rpf', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Allow selfping with RPF
                ''',
                'self_ping_with_rpf',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('source-bgp-pa-input-configured-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                src BGP PA configured flag
                ''',
                'source_bgp_pa_input_configured_flag',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('source-bgp-pa-output-configured-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                src BGP PA configured flag
                ''',
                'source_bgp_pa_output_configured_flag',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'detail-fib-int-information',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.InterfaceInfos.InterfaceInfo.Interfaces.Interface.SiInternal.FibIdbHist.EvtEntry' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.InterfaceInfos.InterfaceInfo.Interfaces.Interface.SiInternal.FibIdbHist.EvtEntry',
            False, 
            [
            _MetaInfoClassMember('evt-data', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Optional data
                ''',
                'evt_data',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('evt-many', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Multiple instance flag
                ''',
                'evt_many',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('evt-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Event name
                ''',
                'evt_name',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('evt-sticky', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Sticky flag
                ''',
                'evt_sticky',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('evt-timestamp', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The timestamp of the event
                ''',
                'evt_timestamp',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('evt-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Event type
                ''',
                'evt_type',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'evt-entry',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.InterfaceInfos.InterfaceInfo.Interfaces.Interface.SiInternal.FibIdbHist' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.InterfaceInfos.InterfaceInfo.Interfaces.Interface.SiInternal.FibIdbHist',
            False, 
            [
            _MetaInfoClassMember('evt-class-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Class name string
                ''',
                'evt_class_name',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('evt-entry', REFERENCE_LIST, 'EvtEntry' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.InterfaceInfos.InterfaceInfo.Interfaces.Interface.SiInternal.FibIdbHist.EvtEntry', 
                [], [], 
                '''                Array of event entries
                ''',
                'evt_entry',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'fib-idb-hist',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.InterfaceInfos.InterfaceInfo.Interfaces.Interface.SiInternal.FibSrteHeadHist.EvtEntry' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.InterfaceInfos.InterfaceInfo.Interfaces.Interface.SiInternal.FibSrteHeadHist.EvtEntry',
            False, 
            [
            _MetaInfoClassMember('evt-data', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Optional data
                ''',
                'evt_data',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('evt-many', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Multiple instance flag
                ''',
                'evt_many',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('evt-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Event name
                ''',
                'evt_name',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('evt-sticky', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Sticky flag
                ''',
                'evt_sticky',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('evt-timestamp', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The timestamp of the event
                ''',
                'evt_timestamp',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('evt-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Event type
                ''',
                'evt_type',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'evt-entry',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.InterfaceInfos.InterfaceInfo.Interfaces.Interface.SiInternal.FibSrteHeadHist' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.InterfaceInfos.InterfaceInfo.Interfaces.Interface.SiInternal.FibSrteHeadHist',
            False, 
            [
            _MetaInfoClassMember('evt-class-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Class name string
                ''',
                'evt_class_name',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('evt-entry', REFERENCE_LIST, 'EvtEntry' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.InterfaceInfos.InterfaceInfo.Interfaces.Interface.SiInternal.FibSrteHeadHist.EvtEntry', 
                [], [], 
                '''                Array of event entries
                ''',
                'evt_entry',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'fib-srte-head-hist',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.InterfaceInfos.InterfaceInfo.Interfaces.Interface.SiInternal' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.InterfaceInfos.InterfaceInfo.Interfaces.Interface.SiInternal',
            False, 
            [
            _MetaInfoClassMember('fib-idb-hist', REFERENCE_CLASS, 'FibIdbHist' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.InterfaceInfos.InterfaceInfo.Interfaces.Interface.SiInternal.FibIdbHist', 
                [], [], 
                '''                Event History for IDB
                ''',
                'fib_idb_hist',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fib-srte-head-hist', REFERENCE_CLASS, 'FibSrteHeadHist' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.InterfaceInfos.InterfaceInfo.Interfaces.Interface.SiInternal.FibSrteHeadHist', 
                [], [], 
                '''                Event History for Srtehead
                ''',
                'fib_srte_head_hist',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'si-internal',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.InterfaceInfos.InterfaceInfo.Interfaces.Interface' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.InterfaceInfos.InterfaceInfo.Interfaces.Interface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-fib-common-oper', True),
            _MetaInfoClassMember('detail-fib-int-information', REFERENCE_CLASS, 'DetailFibIntInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.InterfaceInfos.InterfaceInfo.Interfaces.Interface.DetailFibIntInformation', 
                [], [], 
                '''                Detailed FIB interface information
                ''',
                'detail_fib_int_information',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('drop-packets-while-fib-switching-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Drop packets while FIB switching flag
                ''',
                'drop_packets_while_fib_switching_flag',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fib-id-extension-flags', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Flags on fibidb extension
                ''',
                'fib_id_extension_flags',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fib-id-extension-pointer', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Pointer to fibidb extension
                ''',
                'fib_id_extension_pointer',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fib-id-flags', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Flags on fibidb
                ''',
                'fib_id_flags',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fib-id-pointer', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Pointer to fibidb
                ''',
                'fib_id_pointer',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fib-interface-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                FIB Interface type
                ''',
                'fib_interface_type',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('gre-tunnel-interface-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                GRE Tunnel interface flag
                ''',
                'gre_tunnel_interface_flag',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('interface-up-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Interface up flag
                ''',
                'interface_up_flag',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('last-modified-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Time last modified
                ''',
                'last_modified_time',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('last-operation', REFERENCE_ENUM_CLASS, 'FibidbOperEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'FibidbOperEnum', 
                [], [], 
                '''                Last Oper
                ''',
                'last_operation',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('loopback-interface-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Loopback interface flag
                ''',
                'loopback_interface_flag',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('null-interface-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Null interface flag
                ''',
                'null_interface_flag',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('number-of-dependent-next-hop-information', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of dependent nhinfo's
                ''',
                'number_of_dependent_next_hop_information',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('number-of-input-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of input bytes
                ''',
                'number_of_input_bytes',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('number-of-input-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of input packets
                ''',
                'number_of_input_packets',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('number-of-output-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of output bytes
                ''',
                'number_of_output_bytes',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('number-of-output-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of output packets
                ''',
                'number_of_output_packets',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('p2p-interface-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                P2P interface flag
                ''',
                'p2p_interface_flag',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('per-interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface handle
                ''',
                'per_interface',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('per-packet-load-balancing-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Per packet loadbalancing flag
                ''',
                'per_packet_load_balancing_flag',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('primary-ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [(0, 52)], [], 
                '''                Pimary local v4 address for the interface
                ''',
                'primary_ipv4_address',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('primary-ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [(0, 52)], [], 
                '''                Pimary local v6 address for the interface
                ''',
                'primary_ipv6_address',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('protocol-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is the protocol configured?
                ''',
                'protocol_enabled',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('punt-packets-from-fib-switching-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Punt packets from FIB switching flag
                ''',
                'punt_packets_from_fib_switching_flag',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('punt-packets-from-linecard-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Punt packets from linecard flag
                ''',
                'punt_packets_from_linecard_flag',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('referance-count-for-protocol', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Reference count for the protocol
                ''',
                'referance_count_for_protocol',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('reference-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Reference count
                ''',
                'reference_count',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('si-internal', REFERENCE_CLASS, 'SiInternal' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.InterfaceInfos.InterfaceInfo.Interfaces.Interface.SiInternal', 
                [], [], 
                '''                Internal Information
                ''',
                'si_internal',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('tunnel-interface-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Tunnel interface flag
                ''',
                'tunnel_interface_flag',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('vrf-local-cef-information-pointer', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Vrf local cef info ptr
                ''',
                'vrf_local_cef_information_pointer',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'interface',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.InterfaceInfos.InterfaceInfo.Interfaces' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.InterfaceInfos.InterfaceInfo.Interfaces',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.InterfaceInfos.InterfaceInfo.Interfaces.Interface', 
                [], [], 
                '''                Specify Interface name
                ''',
                'interface',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.InterfaceInfos.InterfaceInfo' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.InterfaceInfos.InterfaceInfo',
            False, 
            [
            _MetaInfoClassMember('link-type', REFERENCE_ENUM_CLASS, 'FibLinkEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'FibLinkEnum', 
                [], [], 
                '''                Link type
                ''',
                'link_type',
                'Cisco-IOS-XR-fib-common-oper', True),
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.InterfaceInfos.InterfaceInfo.Interfaces', 
                [], [], 
                '''                Table of interfaces
                ''',
                'interfaces',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'interface-info',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.InterfaceInfos' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.InterfaceInfos',
            False, 
            [
            _MetaInfoClassMember('interface-info', REFERENCE_LIST, 'InterfaceInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.InterfaceInfos.InterfaceInfo', 
                [], [], 
                '''                Specify link type
                ''',
                'interface_info',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'interface-infos',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixBriefs.IpPrefixBrief.DetailFibEntryInformation.LoadshareInformation.LoadInformtionInternalData.AdjacencyAddress' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixBriefs.IpPrefixBrief.DetailFibEntryInformation.LoadshareInformation.LoadInformtionInternalData.AdjacencyAddress',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [(0, 60)], [], 
                '''                address
                ''',
                'address',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'adjacency-address',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixBriefs.IpPrefixBrief.DetailFibEntryInformation.LoadshareInformation.LoadInformtionInternalData.PbtsClassIsFallbackMapped' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixBriefs.IpPrefixBrief.DetailFibEntryInformation.LoadshareInformation.LoadInformtionInternalData.PbtsClassIsFallbackMapped',
            False, 
            [
            _MetaInfoClassMember('entry', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Array entry.
                ''',
                'entry',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'pbts-class-is-fallback-mapped',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixBriefs.IpPrefixBrief.DetailFibEntryInformation.LoadshareInformation.LoadInformtionInternalData.PbtsFallbackToDrop' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixBriefs.IpPrefixBrief.DetailFibEntryInformation.LoadshareInformation.LoadInformtionInternalData.PbtsFallbackToDrop',
            False, 
            [
            _MetaInfoClassMember('entry', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Array entry.
                ''',
                'entry',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'pbts-fallback-to-drop',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixBriefs.IpPrefixBrief.DetailFibEntryInformation.LoadshareInformation.LoadInformtionInternalData.TunnelIsForwardClass' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixBriefs.IpPrefixBrief.DetailFibEntryInformation.LoadshareInformation.LoadInformtionInternalData.TunnelIsForwardClass',
            False, 
            [
            _MetaInfoClassMember('entry', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Array entry.
                ''',
                'entry',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'tunnel-is-forward-class',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixBriefs.IpPrefixBrief.DetailFibEntryInformation.LoadshareInformation.LoadInformtionInternalData' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixBriefs.IpPrefixBrief.DetailFibEntryInformation.LoadshareInformation.LoadInformtionInternalData',
            False, 
            [
            _MetaInfoClassMember('adjacency-address', REFERENCE_LIST, 'AdjacencyAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixBriefs.IpPrefixBrief.DetailFibEntryInformation.LoadshareInformation.LoadInformtionInternalData.AdjacencyAddress', 
                [], [], 
                '''                Adjacency address
                ''',
                'adjacency_address',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('interface-handle', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface handle
                ''',
                'interface_handle',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('is-pbts-info-valid', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                PBTS info valid flag
                ''',
                'is_pbts_info_valid',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('ldi-next-hop-buckets', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Number of LDI next hop buckets
                ''',
                'ldi_next_hop_buckets',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('level-ofldis', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                level of ldis
                ''',
                'level_ofldis',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('maximum-index-arrays', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum index of the arrays
                ''',
                'maximum_index_arrays',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('maximum-slots', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum slots
                ''',
                'maximum_slots',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('normalized-weights', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Normalized weights
                ''',
                'normalized_weights',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('number-of-ldis', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                no. of ldis
                ''',
                'number_of_ldis',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('path-indices', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Path indices
                ''',
                'path_indices',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('path-ldi-numbers', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Path indices
                ''',
                'path_ldi_numbers',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('pbts-class-is-fallback-mapped', REFERENCE_LIST, 'PbtsClassIsFallbackMapped' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixBriefs.IpPrefixBrief.DetailFibEntryInformation.LoadshareInformation.LoadInformtionInternalData.PbtsClassIsFallbackMapped', 
                [], [], 
                '''                Does PBTS class fall back to drop or any class
                ''',
                'pbts_class_is_fallback_mapped',
                'Cisco-IOS-XR-fib-common-oper', False, max_elements=9, min_elements=9),
            _MetaInfoClassMember('pbts-class-num-paths', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                PBTS class num paths
                ''',
                'pbts_class_num_paths',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('pbts-class-offset', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                PBTS class offset
                ''',
                'pbts_class_offset',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('pbts-fallback-mapped-class', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                PBTS class falls back to class
                ''',
                'pbts_fallback_mapped_class',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('pbts-fallback-to-drop', REFERENCE_LIST, 'PbtsFallbackToDrop' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixBriefs.IpPrefixBrief.DetailFibEntryInformation.LoadshareInformation.LoadInformtionInternalData.PbtsFallbackToDrop', 
                [], [], 
                '''                PBTS class falls back to drop
                ''',
                'pbts_fallback_to_drop',
                'Cisco-IOS-XR-fib-common-oper', False, max_elements=9, min_elements=9),
            _MetaInfoClassMember('platform-hardware-information', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Platform Hardware info
                ''',
                'platform_hardware_information',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('round-robin-disable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Round Robin Disable
                ''',
                'round_robin_disable',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('sanity-flag', REFERENCE_LEAFLIST, 'bool' , None, None, 
                [], [], 
                '''                Sanity flag
                ''',
                'sanity_flag',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('tunnel-class-value', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Tunnel class value
                ''',
                'tunnel_class_value',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('tunnel-is-forward-class', REFERENCE_LIST, 'TunnelIsForwardClass' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixBriefs.IpPrefixBrief.DetailFibEntryInformation.LoadshareInformation.LoadInformtionInternalData.TunnelIsForwardClass', 
                [], [], 
                '''                Tunnel is forward class
                ''',
                'tunnel_is_forward_class',
                'Cisco-IOS-XR-fib-common-oper', False, max_elements=128, min_elements=128),
            _MetaInfoClassMember('weights-of-path', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Weights of paths
                ''',
                'weights_of_path',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'load-informtion-internal-data',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixBriefs.IpPrefixBrief.DetailFibEntryInformation.LoadshareInformation' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixBriefs.IpPrefixBrief.DetailFibEntryInformation.LoadshareInformation',
            False, 
            [
            _MetaInfoClassMember('bytes-through-load-information', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Bytes through this loadinfo
                ''',
                'bytes_through_load_information',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('is-owner', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Owner flag
                ''',
                'is_owner',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('load-information-owner-deleted-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Loadinfo owner deleted flag
                ''',
                'load_information_owner_deleted_flag',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('load-information-reference-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Loadinfo reference count
                ''',
                'load_information_reference_count',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('load-informtion-internal-data', REFERENCE_CLASS, 'LoadInformtionInternalData' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixBriefs.IpPrefixBrief.DetailFibEntryInformation.LoadshareInformation.LoadInformtionInternalData', 
                [], [], 
                '''                Loadinfo internal data
                ''',
                'load_informtion_internal_data',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('loadinfo-sanity-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Loadinfo sanity flag
                ''',
                'loadinfo_sanity_flag',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('mask-length-of-owner', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Mask length of the owner
                ''',
                'mask_length_of_owner',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('packets-through-load-information', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Packets through this loadinfo
                ''',
                'packets_through_load_information',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('per-dest-load-sharing-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Per destination load sharing flag
                ''',
                'per_dest_load_sharing_flag',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('prefix-of-owner', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Prefix of the owner
                ''',
                'prefix_of_owner',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('total-bytes-through-load-information', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total bytes through this loadinfo
                ''',
                'total_bytes_through_load_information',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('total-packets-through-load-information', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total packets through this loadinfo
                ''',
                'total_packets_through_load_information',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'loadshare-information',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixBriefs.IpPrefixBrief.DetailFibEntryInformation' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixBriefs.IpPrefixBrief.DetailFibEntryInformation',
            False, 
            [
            _MetaInfoClassMember('adjacency-address-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ADJ ADDR LEN
                ''',
                'adjacency_address_length',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('adjacency-interface', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ADJ IFH
                ''',
                'adjacency_interface',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('afi-fib-protocol-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                AFI FIB protocol type
                ''',
                'afi_fib_protocol_type',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('aib-l3-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                AIB L3 Address
                ''',
                'aib_l3_address',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('bgp-attribute-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                BGP attribute id
                ''',
                'bgp_attribute_id',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('bgp-attribute-next-hop-as', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                BGP attribute next hop as
                ''',
                'bgp_attribute_next_hop_as',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('bgp-attribute-origin-as', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                BGP attribute origin as
                ''',
                'bgp_attribute_origin_as',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('bgp-local-attribute-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                BGP local attribute id
                ''',
                'bgp_local_attribute_id',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('bytes-through-fib-entry', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Bytes through this FIB entry
                ''',
                'bytes_through_fib_entry',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('com-string', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                com st
                ''',
                'com_string',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('detailed-prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Prefix length
                ''',
                'detailed_prefix_length',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('extcom-string', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                extcom st
                ''',
                'extcom_string',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('extended-community', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                extended community
                ''',
                'extended_community',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fast-adjacency-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Fast adjacency flag
                ''',
                'fast_adjacency_flag',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fib-entry-adjacency-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                FIB entry adj address
                ''',
                'fib_entry_adjacency_address',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fib-entry-adjacency-interface', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                FIB entry adjacency interface
                ''',
                'fib_entry_adjacency_interface',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fib-entry-adjacency-type', REFERENCE_ENUM_CLASS, 'FibAdjacencyShowEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'FibAdjacencyShowEnum', 
                [], [], 
                '''                FIB entry adjacency type
                ''',
                'fib_entry_adjacency_type',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fib-entry-version', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                FIB entry version number
                ''',
                'fib_entry_version',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fib-protocol-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                FIB Protocol type
                ''',
                'fib_protocol_type',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fib-special-nh-information-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                FIB Special NHINFO Type
                ''',
                'fib_special_nh_information_type',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('flow-tag', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                PBR flow-tag
                ''',
                'flow_tag',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('forward-class', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                SPP forwarding class ID
                ''',
                'forward_class',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('illegal-fast-adjacency-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Illegal fast adjacency flag
                ''',
                'illegal_fast_adjacency_flag',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('ldi-time-of-last-update-in-msec', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The time of last update for LDI in msec
                ''',
                'ldi_time_of_last_update_in_msec',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('load-sharing-type', REFERENCE_ENUM_CLASS, 'FibLoadshareShowEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'FibLoadshareShowEnum', 
                [], [], 
                '''                Load sharing type
                ''',
                'load_sharing_type',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('loadshare-information', REFERENCE_CLASS, 'LoadshareInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixBriefs.IpPrefixBrief.DetailFibEntryInformation.LoadshareInformation', 
                [], [], 
                '''                Detailed Loadshare info
                ''',
                'loadshare_information',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('lwldi-time-of-last-update-in-msec', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The time of last update for LW-LDI in msec
                ''',
                'lwldi_time_of_last_update_in_msec',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('mpls-fec', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                mpls fec
                ''',
                'mpls_fec',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('packets-through-fib-entry', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Packets through this FIB entry
                ''',
                'packets_through_fib_entry',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('path-string', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                As path string
                ''',
                'path_string',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('per-prefix-accounting', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Per Prefix Accounting
                ''',
                'per_prefix_accounting',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('pl-time-of-last-update-in-msec', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The time of last update for PL in msec
                ''',
                'pl_time_of_last_update_in_msec',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('pl-time-stamp-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The type of time-stamp on PL
                ''',
                'pl_time_stamp_type',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('precedence-forpackets', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Precedence for packets to this entry
                ''',
                'precedence_forpackets',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('prefix-protocol', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Prefix protocol
                ''',
                'prefix_protocol',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('qos-group', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                qos group
                ''',
                'qos_group',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('qppb-qos-group-and-ip-precedence', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                qppb QOS group and IP precedence
                ''',
                'qppb_qos_group_and_ip_precedence',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('remote-adjacency-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Remote adjacency flag
                ''',
                'remote_adjacency_flag',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('switch-compontent-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Switch function compontent ID
                ''',
                'switch_compontent_id',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('traffic-index-for-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Traffic index for packets to this entry
                ''',
                'traffic_index_for_packets',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'detail-fib-entry-information',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixBriefs.IpPrefixBrief.FibEntryPath.FibShTblPath.MoreDetailAboutPath.SpdIpencap.IpEncapHdr' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixBriefs.IpPrefixBrief.FibEntryPath.FibShTblPath.MoreDetailAboutPath.SpdIpencap.IpEncapHdr',
            False, 
            [
            _MetaInfoClassMember('ip-encap-hdr-dyn', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Dynamic Header Fields
                ''',
                'ip_encap_hdr_dyn',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('ip-encap-hdr-type', REFERENCE_ENUM_CLASS, 'FibShIpencapHdrEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'FibShIpencapHdrEnum', 
                [], [], 
                '''                Header Type
                ''',
                'ip_encap_hdr_type',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('ip-encap-hdrp', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Static Header
                ''',
                'ip_encap_hdrp',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'ip-encap-hdr',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixBriefs.IpPrefixBrief.FibEntryPath.FibShTblPath.MoreDetailAboutPath.SpdIpencap' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixBriefs.IpPrefixBrief.FibEntryPath.FibShTblPath.MoreDetailAboutPath.SpdIpencap',
            False, 
            [
            _MetaInfoClassMember('ip-encap-hdr', REFERENCE_LIST, 'IpEncapHdr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixBriefs.IpPrefixBrief.FibEntryPath.FibShTblPath.MoreDetailAboutPath.SpdIpencap.IpEncapHdr', 
                [], [], 
                '''                Headers
                ''',
                'ip_encap_hdr',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('ip-encap-hdr-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Header Count
                ''',
                'ip_encap_hdr_count',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('ip-encap-locks', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IPEncap Object Locks
                ''',
                'ip_encap_locks',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('ip-encap-parent', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Pointer to parent
                ''',
                'ip_encap_parent',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('ip-encap-parent-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Parent type enumeration
                ''',
                'ip_encap_parent_type',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('ip-encap-payload-af', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Payload AF
                ''',
                'ip_encap_payload_af',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('ip-encap-payload-mtu', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Payload MTU
                ''',
                'ip_encap_payload_mtu',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('ip-encap-transport-af', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Transport AF
                ''',
                'ip_encap_transport_af',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('ip-encap-transport-tbl', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Transport Table
                ''',
                'ip_encap_transport_tbl',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('ipe-transport-vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Transport VRF name
                ''',
                'ipe_transport_vrf_name',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'spd-ipencap',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixBriefs.IpPrefixBrief.FibEntryPath.FibShTblPath.MoreDetailAboutPath' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixBriefs.IpPrefixBrief.FibEntryPath.FibShTblPath.MoreDetailAboutPath',
            False, 
            [
            _MetaInfoClassMember('current-path-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Current path flag
                ''',
                'current_path_flag',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('detail-fib-adjacency-type', REFERENCE_ENUM_CLASS, 'FibAdjacencyShowEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'FibAdjacencyShowEnum', 
                [], [], 
                '''                FIB entry adjacency type
                ''',
                'detail_fib_adjacency_type',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('detail-next-hop-prefix', ATTRIBUTE, 'str' , None, None, 
                [(0, 52)], [], 
                '''                Next hop prefix
                ''',
                'detail_next_hop_prefix',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('external-adjacency', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Path is an external adjacency
                ''',
                'external_adjacency',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fib-path-nh-information-type', REFERENCE_ENUM_CLASS, 'FibNehEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'FibNehEnum', 
                [], [], 
                '''                FIB Nhinfo type
                ''',
                'fib_path_nh_information_type',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fib-path-nh-information-type-special', REFERENCE_ENUM_CLASS, 'FibNehSpecialEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'FibNehSpecialEnum', 
                [], [], 
                '''                FIB Nhinfo type special
                ''',
                'fib_path_nh_information_type_special',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('interface-associated-path', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface associated with this path
                ''',
                'interface_associated_path',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('ip-address-to-recurse', ATTRIBUTE, 'str' , None, None, 
                [(0, 52)], [], 
                '''                IP address to recurse to
                ''',
                'ip_address_to_recurse',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('label-to-recurse', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Local label to recurse over
                ''',
                'label_to_recurse',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('lisprlocid', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LISP RLOC ID
                ''',
                'lisprlocid',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('next-hop-interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Next hop interface
                ''',
                'next_hop_interface',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('next-hop-mask-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Next hop mask length
                ''',
                'next_hop_mask_length',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('next-hop-vrf', ATTRIBUTE, 'str' , None, None, 
                [(0, 33)], [], 
                '''                Next hop VRF
                ''',
                'next_hop_vrf',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('next-prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Next prefix length
                ''',
                'next_prefix_length',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('next-prefix-length2', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Next prefix2 length
                ''',
                'next_prefix_length2',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('next-prefix-recursion', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Next prefix recursion in the path
                ''',
                'next_prefix_recursion',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('next-prefix-recursion2', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Next prefix2 recursion in the path
                ''',
                'next_prefix_recursion2',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('number-of-dependencies-this-path', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                No. of dependents for this path
                ''',
                'number_of_dependencies_this_path',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('recurse-prefix-object', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is recursion object a leaf?
                ''',
                'recurse_prefix_object',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('recurse-prefix-object2', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Recursion has two leaves (e.g. implicit-null
                path)
                ''',
                'recurse_prefix_object2',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('recursive-path-information', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Recursive path information is available
                ''',
                'recursive_path_information',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('robin-reset-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Round robin reset value
                ''',
                'robin_reset_value',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('spd-ipencap', REFERENCE_LIST, 'SpdIpencap' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixBriefs.IpPrefixBrief.FibEntryPath.FibShTblPath.MoreDetailAboutPath.SpdIpencap', 
                [], [], 
                '''                IP Encap
                ''',
                'spd_ipencap',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('tunnel-class', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Tunnel class of the path
                ''',
                'tunnel_class',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('tunnel-is-forward-class', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Tunnel is forward class
                ''',
                'tunnel_is_forward_class',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('tunnle-endpoint-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Tunnel endpoint id
                ''',
                'tunnle_endpoint_id',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('weight-of-path', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Weight of the path
                ''',
                'weight_of_path',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'more-detail-about-path',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixBriefs.IpPrefixBrief.FibEntryPath.FibShTblPath.MplsInformationForPath.IgpLabelStackArray' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixBriefs.IpPrefixBrief.FibEntryPath.FibShTblPath.MplsInformationForPath.IgpLabelStackArray',
            False, 
            [
            _MetaInfoClassMember('lstack', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                lstack
                ''',
                'lstack',
                'Cisco-IOS-XR-fib-common-oper', False, max_elements=14),
            _MetaInfoClassMember('nh-address', ATTRIBUTE, 'str' , None, None, 
                [(0, 52)], [], 
                '''                NHAddress
                ''',
                'nh_address',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('number-of-labels', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                NumberOfLabels
                ''',
                'number_of_labels',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('out-interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                OutInterface
                ''',
                'out_interface',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'igp-label-stack-array',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixBriefs.IpPrefixBrief.FibEntryPath.FibShTblPath.MplsInformationForPath' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixBriefs.IpPrefixBrief.FibEntryPath.FibShTblPath.MplsInformationForPath',
            False, 
            [
            _MetaInfoClassMember('igp-label-stack-array', REFERENCE_LIST, 'IgpLabelStackArray' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixBriefs.IpPrefixBrief.FibEntryPath.FibShTblPath.MplsInformationForPath.IgpLabelStackArray', 
                [], [], 
                '''                igp label stack array
                ''',
                'igp_label_stack_array',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('local-lable', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LocalLable
                ''',
                'local_lable',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('number-of-igp-paths', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                NumberOfIGPPaths
                ''',
                'number_of_igp_paths',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('recursive-fwd-chain', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                RecursiveFwdChain
                ''',
                'recursive_fwd_chain',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('recursive-out-label-valid', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                RecursiveOutLabelValid
                ''',
                'recursive_out_label_valid',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('recursive-out-lable', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                RecursiveOutLable
                ''',
                'recursive_out_lable',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('remote-backup', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                RemoteBackupPath
                ''',
                'remote_backup',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'mpls-information-for-path',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixBriefs.IpPrefixBrief.FibEntryPath.FibShTblPath' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixBriefs.IpPrefixBrief.FibEntryPath.FibShTblPath',
            False, 
            [
            _MetaInfoClassMember('attached-path', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Attached path
                ''',
                'attached_path',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('backup-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Backup path index
                ''',
                'backup_index',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('backup-path', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Backup path
                ''',
                'backup_path',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('best-external-path', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Best external path
                ''',
                'best_external_path',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('brief-interface-handle', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface handle
                ''',
                'brief_interface_handle',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('brief-lfa-protection-type', REFERENCE_ENUM_CLASS, 'FibUpdatePathLfaProtectionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'FibUpdatePathLfaProtectionEnum', 
                [], [], 
                '''                LFA protection type
                ''',
                'brief_lfa_protection_type',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('brief-next-hop-prefix', ATTRIBUTE, 'str' , None, None, 
                [(0, 52)], [], 
                '''                Next hop prefix
                ''',
                'brief_next_hop_prefix',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('brief-pnode-address', ATTRIBUTE, 'str' , None, None, 
                [(0, 52)], [], 
                '''                P-node address
                ''',
                'brief_pnode_address',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('brief-qnode-address', ATTRIBUTE, 'str' , None, None, 
                [(0, 52)], [], 
                '''                Q-node address
                ''',
                'brief_qnode_address',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('hardware-information', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Hardware info
                ''',
                'hardware_information',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('more-detail-about-path', REFERENCE_CLASS, 'MoreDetailAboutPath' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixBriefs.IpPrefixBrief.FibEntryPath.FibShTblPath.MoreDetailAboutPath', 
                [], [], 
                '''                More detail about this path entry
                ''',
                'more_detail_about_path',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('mpls-information-for-path', REFERENCE_CLASS, 'MplsInformationForPath' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixBriefs.IpPrefixBrief.FibEntryPath.FibShTblPath.MplsInformationForPath', 
                [], [], 
                '''                mpls info for this path entry
                ''',
                'mpls_information_for_path',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('next-hop-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Next Hop Index
                ''',
                'next_hop_index',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('packets-received-path', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Packets received on this path
                ''',
                'packets_received_path',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('parent-interface-handle', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Parent Interface Handle
                ''',
                'parent_interface_handle',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('path-dlb', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is this the path used for DLB
                ''',
                'path_dlb',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('path-flags', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Path flags
                ''',
                'path_flags',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('path-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Path index
                ''',
                'path_index',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('path-info-flags', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Path Info flags
                ''',
                'path_info_flags',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('protect-ignore', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is protection ignored
                ''',
                'protect_ignore',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('recursionvia-len', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                recursion via /N constraint
                ''',
                'recursionvia_len',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('recursive-path', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Recursive path
                ''',
                'recursive_path',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('resolved-path', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Resolved path
                ''',
                'resolved_path',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('via-label-to-recurse', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Local label to recurse over
                ''',
                'via_label_to_recurse',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'fib-sh-tbl-path',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixBriefs.IpPrefixBrief.FibEntryPath' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixBriefs.IpPrefixBrief.FibEntryPath',
            False, 
            [
            _MetaInfoClassMember('fib-sh-tbl-path', REFERENCE_LIST, 'FibShTblPath' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixBriefs.IpPrefixBrief.FibEntryPath.FibShTblPath', 
                [], [], 
                '''                fib sh tbl path
                ''',
                'fib_sh_tbl_path',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'fib-entry-path',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixBriefs.IpPrefixBrief.Srv6Information.Srv6Statistics' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixBriefs.IpPrefixBrief.Srv6Information.Srv6Statistics',
            False, 
            [
            _MetaInfoClassMember('srv6-packets-dropped', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                SRv6 Packets dropped for a prefix
                ''',
                'srv6_packets_dropped',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('srv6-packets-forwarded', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                SRv6 packets forwarded for a prefix
                ''',
                'srv6_packets_forwarded',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'srv6-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixBriefs.IpPrefixBrief.Srv6Information' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixBriefs.IpPrefixBrief.Srv6Information',
            False, 
            [
            _MetaInfoClassMember('route-is-sripv6-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Route is an IPv6 Segment-Routing prefix
                ''',
                'route_is_sripv6_flag',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('sripv6-stats-valid-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Statistics are valid for this prefix
                ''',
                'sripv6_stats_valid_flag',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('srv6-pfx-resolved-via-policy-label', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Route is a SRv6 prefix resolved via Policy label
                ''',
                'srv6_pfx_resolved_via_policy_label',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('srv6-statistics', REFERENCE_CLASS, 'Srv6Statistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixBriefs.IpPrefixBrief.Srv6Information.Srv6Statistics', 
                [], [], 
                '''                Statistics for a IPv6 SR prefix
                ''',
                'srv6_statistics',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'srv6-information',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixBriefs.IpPrefixBrief.ExtensionObject.SfecdLe' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixBriefs.IpPrefixBrief.ExtensionObject.SfecdLe',
            False, 
            [
            _MetaInfoClassMember('context-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Context Label
                ''',
                'context_label',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('context-label-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Context Label Exist
                ''',
                'context_label_flag',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'sfecd-le',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixBriefs.IpPrefixBrief.ExtensionObject' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixBriefs.IpPrefixBrief.ExtensionObject',
            False, 
            [
            _MetaInfoClassMember('sfecd-le', REFERENCE_CLASS, 'SfecdLe' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixBriefs.IpPrefixBrief.ExtensionObject.SfecdLe', 
                [], [], 
                '''                sfecd le
                ''',
                'sfecd_le',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'FibShTblFibExtBagEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'FibShTblFibExtBagEnum', 
                [], [], 
                '''                type
                ''',
                'type',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'extension-object',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixBriefs.IpPrefixBrief' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixBriefs.IpPrefixBrief',
            False, 
            [
            _MetaInfoClassMember('broadcast-forward-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Broadcast forward flag
                ''',
                'broadcast_forward_flag',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('broadcast-recive-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Broadcast receive flag
                ''',
                'broadcast_recive_flag',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('detail-fib-entry-information', REFERENCE_CLASS, 'DetailFibEntryInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixBriefs.IpPrefixBrief.DetailFibEntryInformation', 
                [], [], 
                '''                Detailed FIB entry information
                ''',
                'detail_fib_entry_information',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('dummy-real-zero-route', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Dummy real zero route
                ''',
                'dummy_real_zero_route',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('exact-route-result', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                exact-route result
                ''',
                'exact_route_result',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('extension-object', REFERENCE_LIST, 'ExtensionObject' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixBriefs.IpPrefixBrief.ExtensionObject', 
                [], [], 
                '''                Leaf Extension Object List
                ''',
                'extension_object',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('external-switch-triggered', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                External switch function triggered
                ''',
                'external_switch_triggered',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fib-entry-path', REFERENCE_CLASS, 'FibEntryPath' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixBriefs.IpPrefixBrief.FibEntryPath', 
                [], [], 
                '''                FIB entry path details
                ''',
                'fib_entry_path',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fib-route-download-priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Priority at which the route was downloaded
                ''',
                'fib_route_download_priority',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('flags-external-ldi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The flags of ext assocaited with LDI 
                ''',
                'flags_external_ldi',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('l2-subscriber-ip-protocol', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IP protocol associated with L2 subscriber
                ''',
                'l2_subscriber_ip_protocol',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('l2-subscriber-route', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is L2 Subscriber route
                ''',
                'l2_subscriber_route',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('l2-subscriber-xconnect-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                XConnect-id associated with L2 subscriber
                ''',
                'l2_subscriber_xconnect_id',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('l2tpv3-cookie-length-bits', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                L2TPv3 cookie length for L2 subscriber
                ''',
                'l2tpv3_cookie_length_bits',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('ldi-flags', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The LDI flags
                ''',
                'ldi_flags',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('ldi-lw-flag', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The LDI LW flags
                ''',
                'ldi_lw_flag',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('lspa-flags', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The LSPA flags
                ''',
                'lspa_flags',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('number-of-referances-to-ldi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of references to the LDI
                ''',
                'number_of_referances_to_ldi',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('number-of-referances-to-path-list', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of references to the pathlist
                ''',
                'number_of_referances_to_path_list',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('packet-should-recieve', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Packet should always be received
                ''',
                'packet_should_recieve',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('path-list-flags', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The pathlist flags
                ''',
                'path_list_flags',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('path-list-source', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The pathlist source
                ''',
                'path_list_source',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('platform-hardware', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Platform Hardware info
                ''',
                'platform_hardware',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('prefix', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Destination IP address
                ''',
                'prefix',
                'Cisco-IOS-XR-fib-common-oper', False, [
                    _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Destination IP address
                        ''',
                        'prefix',
                        'Cisco-IOS-XR-fib-common-oper', False),
                    _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Destination IP address
                        ''',
                        'prefix',
                        'Cisco-IOS-XR-fib-common-oper', False),
                ]),
            _MetaInfoClassMember('prefix-connected', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Prefix is connected
                ''',
                'prefix_connected',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('prefix-for-adjancency', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Prefix is for an adjacency
                ''',
                'prefix_for_adjancency',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('prefix-for-pic-next-hop', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Prefix is for a PIC nexthop
                ''',
                'prefix_for_pic_next_hop',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('prefix-is-static-or-connected', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Prefix is static or connected
                ''',
                'prefix_is_static_or_connected',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '128')], [], 
                '''                IP prefix length
                ''',
                'prefix_length',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('protocol-type-fib-entry', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Proto type for this entry
                ''',
                'protocol_type_fib_entry',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('purgable-after-purge-interval', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Purgable after the purge interval
                ''',
                'purgable_after_purge_interval',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('ref-counter-of-ldi-lw-ldi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The refcounter of LDI LW LDI
                ''',
                'ref_counter_of_ldi_lw_ldi',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('route-attribute-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Route attributes summary flag
                ''',
                'route_attribute_flag',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('route-for-external-reach-linecard-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Route destined for Line Card that support
                External Reach only
                ''',
                'route_for_external_reach_linecard_flag',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('route-is-sr-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Route is a MPLS Segment-Routing prefix
                ''',
                'route_is_sr_flag',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('srv6-information', REFERENCE_CLASS, 'Srv6Information' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixBriefs.IpPrefixBrief.Srv6Information', 
                [], [], 
                '''                Information about IPv6 SR prefix
                ''',
                'srv6_information',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('time-of-last-update-in-msec', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The time of last update in msec
                ''',
                'time_of_last_update_in_msec',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('type-of-ldi-lw-ldi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The type of LDI LW LDI
                ''',
                'type_of_ldi_lw_ldi',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('version-of-route', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The version of the route
                ''',
                'version_of_route',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('zero-by-zero-route-as-default', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                0/0 route added as default route
                ''',
                'zero_by_zero_route_as_default',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'ip-prefix-brief',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixBriefs' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixBriefs',
            False, 
            [
            _MetaInfoClassMember('ip-prefix-brief', REFERENCE_LIST, 'IpPrefixBrief' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixBriefs.IpPrefixBrief', 
                [], [], 
                '''                IP FIB prefix brief table entry
                ''',
                'ip_prefix_brief',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'ip-prefix-briefs',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf',
            False, 
            [
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                VRF Name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-fib-common-oper', True),
            _MetaInfoClassMember('interface-infos', REFERENCE_CLASS, 'InterfaceInfos' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.InterfaceInfos', 
                [], [], 
                '''                Table of InterfaceInfo
                ''',
                'interface_infos',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('ip-prefix-briefs', REFERENCE_CLASS, 'IpPrefixBriefs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixBriefs', 
                [], [], 
                '''                IP FIB prefix brief table
                ''',
                'ip_prefix_briefs',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('ip-prefix-details', REFERENCE_CLASS, 'IpPrefixDetails' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixDetails', 
                [], [], 
                '''                IP FIB prefix detail table
                ''',
                'ip_prefix_details',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('summary', REFERENCE_CLASS, 'Summary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.Summary', 
                [], [], 
                '''                Operational data for FIB Tablee
                ''',
                'summary',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'vrf',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Protocols.Protocol.Vrfs' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Protocols.Protocol.Vrfs',
            False, 
            [
            _MetaInfoClassMember('vrf', REFERENCE_LIST, 'Vrf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf', 
                [], [], 
                '''                VRF table entry
                ''',
                'vrf',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'vrfs',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Protocols.Protocol.NhIds.NhId' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Protocols.Protocol.NhIds.NhId',
            False, 
            [
            _MetaInfoClassMember('nh-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Next-hop address in string format (e.g., 1
                .2.3.4)
                ''',
                'nh_address',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('nh-address-xr', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Next-hop address
                ''',
                'nh_address_xr',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('nh-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                NHID value
                ''',
                'nh_id',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('nh-id-value', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                NexthopId Value
                ''',
                'nh_id_value',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('nh-interf-handle', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Next-hop interface
                ''',
                'nh_interf_handle',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('nh-interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface Name
                ''',
                'nh_interface_name',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('nh-link-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Payload linktype
                ''',
                'nh_link_type',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('nh-protocol', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Next-hop address protocol, IPv4/IPv6
                ''',
                'nh_protocol',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('nh-table-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Table-ID entry notified for
                ''',
                'nh_table_id',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('time-of-last-update-in-msec', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The time of last update in msec
                ''',
                'time_of_last_update_in_msec',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                RIB version
                ''',
                'version',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'nh-id',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Protocols.Protocol.NhIds' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Protocols.Protocol.NhIds',
            False, 
            [
            _MetaInfoClassMember('nh-id', REFERENCE_LIST, 'NhId' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Protocols.Protocol.NhIds.NhId', 
                [], [], 
                '''                NextHopeId table entry
                ''',
                'nh_id',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'nh-ids',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Protocols.Protocol.ExternalClientSummaries.ExternalClientSummary.SesPlSum' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Protocols.Protocol.ExternalClientSummaries.ExternalClientSummary.SesPlSum',
            False, 
            [
            _MetaInfoClassMember('sep-num-ecd-pathlist', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of ECD pathlists
                ''',
                'sep_num_ecd_pathlist',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('sep-num-ecd-pl-per-interest', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of ECD pathlists per interest
                ''',
                'sep_num_ecd_pl_per_interest',
                'Cisco-IOS-XR-fib-common-oper', False, max_elements=10),
            _MetaInfoClassMember('sep-num-ecd-pl-unresolved', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of ECD pathlists unresolved
                ''',
                'sep_num_ecd_pl_unresolved',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'ses-pl-sum',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Protocols.Protocol.ExternalClientSummaries.ExternalClientSummary' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Protocols.Protocol.ExternalClientSummaries.ExternalClientSummary',
            False, 
            [
            _MetaInfoClassMember('ecd-ver', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Ecd Version
                ''',
                'ecd_ver',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                ID of the client: ECDv1 is component id,
                ECDv2 is client id
                ''',
                'id',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('ses-client-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                External client name
                ''',
                'ses_client_name',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('ses-client-pulsed-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Client pulsed timestamp
                ''',
                'ses_client_pulsed_time',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('ses-comp-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                component-id of the client
                ''',
                'ses_comp_id',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('ses-ecd-version', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ECD version
                ''',
                'ses_ecd_version',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('ses-feci-fib-proto', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Registration proto
                ''',
                'ses_feci_fib_proto',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('ses-num-pending', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of pending notifs
                ''',
                'ses_num_pending',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('ses-num-regs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of registrations
                ''',
                'ses_num_regs',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('ses-pl-sum', REFERENCE_CLASS, 'SesPlSum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Protocols.Protocol.ExternalClientSummaries.ExternalClientSummary.SesPlSum', 
                [], [], 
                '''                ECD pathlist summary
                ''',
                'ses_pl_sum',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'external-client-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Protocols.Protocol.ExternalClientSummaries' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Protocols.Protocol.ExternalClientSummaries',
            False, 
            [
            _MetaInfoClassMember('external-client-summary', REFERENCE_LIST, 'ExternalClientSummary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Protocols.Protocol.ExternalClientSummaries.ExternalClientSummary', 
                [], [], 
                '''                Summary of the external clients
                ''',
                'external_client_summary',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'external-client-summaries',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Protocols.Protocol.Misc.MiIssuState.FisProtoState' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Protocols.Protocol.Misc.MiIssuState.FisProtoState',
            False, 
            [
            _MetaInfoClassMember('aib-eod-time-stamp', ATTRIBUTE, 'str' , None, None, 
                [(0, 33)], [], 
                '''                AIB EODTimeStamp
                ''',
                'aib_eod_time_stamp',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('bcdl-tables', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of BCDL tables
                ''',
                'bcdl_tables',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('converged-tables', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of tables converged
                ''',
                'converged_tables',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('lmrib-eod-time-stamp', ATTRIBUTE, 'str' , None, None, 
                [(0, 33)], [], 
                '''                LMRIB EOD received timestamp
                ''',
                'lmrib_eod_time_stamp',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('lmrib-eod-valid', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                LMRIB EOD expected/valid
                ''',
                'lmrib_eod_valid',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('lsd-eod-time-stamp', ATTRIBUTE, 'str' , None, None, 
                [(0, 33)], [], 
                '''                LSD EOD received timestamp
                ''',
                'lsd_eod_time_stamp',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('lsd-eod-valid', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                LSD EOD expected/valid
                ''',
                'lsd_eod_valid',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('protocol-eod-time-stamp', ATTRIBUTE, 'str' , None, None, 
                [(0, 33)], [], 
                '''                Protocol EOD sent timestamp
                ''',
                'protocol_eod_time_stamp',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('protocol-eod-valid', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Protocol EOD expected/valid
                ''',
                'protocol_eod_valid',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('protocol-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 6)], [], 
                '''                Protocol name
                ''',
                'protocol_name',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('rib-info-valid', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                RIB table info valid
                ''',
                'rib_info_valid',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('rib-tables-converged-time-stamp', ATTRIBUTE, 'str' , None, None, 
                [(0, 33)], [], 
                '''                All RIB tables converged timestamp
                ''',
                'rib_tables_converged_time_stamp',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('rsi-eod-time-stamp', ATTRIBUTE, 'str' , None, None, 
                [(0, 33)], [], 
                '''                RSI EOD received timestamp
                ''',
                'rsi_eod_time_stamp',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('rsi-eod-valid', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                RSI EOD expected/valid
                ''',
                'rsi_eod_valid',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'fis-proto-state',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Protocols.Protocol.Misc.MiIssuState' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Protocols.Protocol.Misc.MiIssuState',
            False, 
            [
            _MetaInfoClassMember('eoc-received-imdr-time-stamp', ATTRIBUTE, 'str' , None, None, 
                [(0, 33)], [], 
                '''                End-of-config received from IMDR timestamp
                ''',
                'eoc_received_imdr_time_stamp',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('eoc-received-slc-time-stamp', ATTRIBUTE, 'str' , None, None, 
                [(0, 33)], [], 
                '''                End-of-config received from SLC timestamp
                ''',
                'eoc_received_slc_time_stamp',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('eod-received-im-time-stamp', ATTRIBUTE, 'str' , None, None, 
                [(0, 33)], [], 
                '''                End-of-download received from IM timestamp
                ''',
                'eod_received_im_time_stamp',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('eod-sent-imdr-time-stamp', ATTRIBUTE, 'str' , None, None, 
                [(0, 33)], [], 
                '''                End-of-download send to IMDR timestamp
                ''',
                'eod_sent_imdr_time_stamp',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('eod-sent-slc-time-stamp', ATTRIBUTE, 'str' , None, None, 
                [(0, 33)], [], 
                '''                End-of-download send to SLC timestamp
                ''',
                'eod_sent_slc_time_stamp',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fis-issu-error-ts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                ISSU error sent to ISSUMGR timetstamp
                ''',
                'fis_issu_error_ts',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fis-issu-restart', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                ISSU restart
                ''',
                'fis_issu_restart',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fis-proto-state', REFERENCE_LIST, 'FisProtoState' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Protocols.Protocol.Misc.MiIssuState.FisProtoState', 
                [], [], 
                '''                IMDR state for the protocols
                ''',
                'fis_proto_state',
                'Cisco-IOS-XR-fib-common-oper', False, max_elements=3),
            _MetaInfoClassMember('imdr-eoc-implicit', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                IMDR End-of-config implicit
                ''',
                'imdr_eoc_implicit',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('imdr-support', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                IMDR supported
                ''',
                'imdr_support',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('slc-eoc-implicit', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                SLC End-of-config implicit
                ''',
                'slc_eoc_implicit',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('slc-support', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                SLC supported
                ''',
                'slc_support',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'mi-issu-state',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Protocols.Protocol.Misc.MiPlatCapabilities.FpcLispDecapOverV4' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Protocols.Protocol.Misc.MiPlatCapabilities.FpcLispDecapOverV4',
            False, 
            [
            _MetaInfoClassMember('entry', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Array entry.
                ''',
                'entry',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'fpc-lisp-decap-over-v4',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Protocols.Protocol.Misc.MiPlatCapabilities.FpcLispDecapOverV6' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Protocols.Protocol.Misc.MiPlatCapabilities.FpcLispDecapOverV6',
            False, 
            [
            _MetaInfoClassMember('entry', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Array entry.
                ''',
                'entry',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'fpc-lisp-decap-over-v6',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Protocols.Protocol.Misc.MiPlatCapabilities.FpcLispUcmp' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Protocols.Protocol.Misc.MiPlatCapabilities.FpcLispUcmp',
            False, 
            [
            _MetaInfoClassMember('entry', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Array entry.
                ''',
                'entry',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'fpc-lisp-ucmp',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Protocols.Protocol.Misc.MiPlatCapabilities.FpcResolveViaTable' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Protocols.Protocol.Misc.MiPlatCapabilities.FpcResolveViaTable',
            False, 
            [
            _MetaInfoClassMember('entry', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Array entry.
                ''',
                'entry',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'fpc-resolve-via-table',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Protocols.Protocol.Misc.MiPlatCapabilities' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Protocols.Protocol.Misc.MiPlatCapabilities',
            False, 
            [
            _MetaInfoClassMember('fpc-dlb-support', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Per-destination load-balancing support
                ''',
                'fpc_dlb_support',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fpc-exclude-deag-bkup', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Exclude Deag backup Paths
                ''',
                'fpc_exclude_deag_bkup',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fpc-lba-tuples-default', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LBA tuples
                ''',
                'fpc_lba_tuples_default',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fpc-link-mpls-nhinfo-in-ipv6-thread-support', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Link MPLS IPv6 NH support
                ''',
                'fpc_link_mpls_nhinfo_in_ipv6_thread_support',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fpc-lisp-decap-over-v4', REFERENCE_LIST, 'FpcLispDecapOverV4' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Protocols.Protocol.Misc.MiPlatCapabilities.FpcLispDecapOverV4', 
                [], [], 
                '''                LISP Decap over 4
                ''',
                'fpc_lisp_decap_over_v4',
                'Cisco-IOS-XR-fib-common-oper', False, max_elements=3, min_elements=3),
            _MetaInfoClassMember('fpc-lisp-decap-over-v6', REFERENCE_LIST, 'FpcLispDecapOverV6' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Protocols.Protocol.Misc.MiPlatCapabilities.FpcLispDecapOverV6', 
                [], [], 
                '''                LISP Decap over 6
                ''',
                'fpc_lisp_decap_over_v6',
                'Cisco-IOS-XR-fib-common-oper', False, max_elements=3, min_elements=3),
            _MetaInfoClassMember('fpc-lisp-ucmp', REFERENCE_LIST, 'FpcLispUcmp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Protocols.Protocol.Misc.MiPlatCapabilities.FpcLispUcmp', 
                [], [], 
                '''                LISP UCMP support
                ''',
                'fpc_lisp_ucmp',
                'Cisco-IOS-XR-fib-common-oper', False, max_elements=3, min_elements=3),
            _MetaInfoClassMember('fpc-loadinfo-filter-support', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                loadinfo filter support
                ''',
                'fpc_loadinfo_filter_support',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fpc-local-label-split', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Label split
                ''',
                'fpc_local_label_split',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fpc-mraps-support', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                MRAPS support
                ''',
                'fpc_mraps_support',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fpc-nhid', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                NHID support
                ''',
                'fpc_nhid',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fpc-num-fwding-stages', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Forwarding stages
                ''',
                'fpc_num_fwding_stages',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fpc-num-l3-lbl-levels', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                L3 LBL levels
                ''',
                'fpc_num_l3_lbl_levels',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fpc-num-l3-lbl-paths', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                L3 Hash buckets
                ''',
                'fpc_num_l3_lbl_paths',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fpc-num-l3-lbl-rec-paths', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                L3 Recursive Hash buckets
                ''',
                'fpc_num_l3_lbl_rec_paths',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fpc-num-l3-ucmp-paths', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                L3 Unequal cost hash buckets
                ''',
                'fpc_num_l3_ucmp_paths',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fpc-num-paths-per-pbts-class', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Path per tunnel class
                ''',
                'fpc_num_paths_per_pbts_class',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fpc-pbts-defclass-support', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                PBTS default class support
                ''',
                'fpc_pbts_defclass_support',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fpc-platf-ready-cb-wait', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Plat ready cb register
                ''',
                'fpc_platf_ready_cb_wait',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fpc-platf-temp-back-walk-reqd', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Backwalk dependents is required
                ''',
                'fpc_platf_temp_back_walk_reqd',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fpc-platf-v4-upd-disable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                V4 update disable
                ''',
                'fpc_platf_v4_upd_disable',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fpc-platf-v6-upd-disable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                V6 update disable
                ''',
                'fpc_platf_v6_upd_disable',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fpc-prefix-filter-support', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Prefix filter level of support
                ''',
                'fpc_prefix_filter_support',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fpc-resolve-via-table', REFERENCE_LIST, 'FpcResolveViaTable' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Protocols.Protocol.Misc.MiPlatCapabilities.FpcResolveViaTable', 
                [], [], 
                '''                Fallback VRF support
                ''',
                'fpc_resolve_via_table',
                'Cisco-IOS-XR-fib-common-oper', False, max_elements=3, min_elements=3),
            _MetaInfoClassMember('fpc-slowpath-ingress-inject-reqd', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Slowpath ingress inject required
                ''',
                'fpc_slowpath_ingress_inject_reqd',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fpc-stats-support', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Statistics support
                ''',
                'fpc_stats_support',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'mi-plat-capabilities',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Protocols.Protocol.Misc.MiProtoDbgStat.FpdPlatfUpdStats.FpusObjStat.FosObjActStat' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Protocols.Protocol.Misc.MiProtoDbgStat.FpdPlatfUpdStats.FpusObjStat.FosObjActStat',
            False, 
            [
            _MetaInfoClassMember('foas-max-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Time for the update
                ''',
                'foas_max_time',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('foas-max-tstamp', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Time stamp of max update
                ''',
                'foas_max_tstamp',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('foas-num-failure', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total number of failed updates
                ''',
                'foas_num_failure',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('foas-num-success', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total number of successful updates
                ''',
                'foas_num_success',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('foas-tot-upd-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total time for updates
                ''',
                'foas_tot_upd_time',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('foas-tot-updates', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total number of updates
                ''',
                'foas_tot_updates',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('foas-tot-updates-zero', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total number of updates that took zero time
                ''',
                'foas_tot_updates_zero',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'fos-obj-act-stat',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Protocols.Protocol.Misc.MiProtoDbgStat.FpdPlatfUpdStats.FpusObjStat' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Protocols.Protocol.Misc.MiProtoDbgStat.FpdPlatfUpdStats.FpusObjStat',
            False, 
            [
            _MetaInfoClassMember('fos-obj-act-stat', REFERENCE_LIST, 'FosObjActStat' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Protocols.Protocol.Misc.MiProtoDbgStat.FpdPlatfUpdStats.FpusObjStat.FosObjActStat', 
                [], [], 
                '''                Array of max time info indexed by action type
                ''',
                'fos_obj_act_stat',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fos-tot-upd-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total time for updates
                ''',
                'fos_tot_upd_time',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fos-tot-updates', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total number of updates
                ''',
                'fos_tot_updates',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'fpus-obj-stat',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Protocols.Protocol.Misc.MiProtoDbgStat.FpdPlatfUpdStats' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Protocols.Protocol.Misc.MiProtoDbgStat.FpdPlatfUpdStats',
            False, 
            [
            _MetaInfoClassMember('fpus-num-failure', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of unsuccessful updates
                ''',
                'fpus_num_failure',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fpus-num-success', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of successful updates
                ''',
                'fpus_num_success',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fpus-obj-stat', REFERENCE_LIST, 'FpusObjStat' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Protocols.Protocol.Misc.MiProtoDbgStat.FpdPlatfUpdStats.FpusObjStat', 
                [], [], 
                '''                Array of max time info indexed by object type
                ''',
                'fpus_obj_stat',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fpus-upd-total-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total time for all pd updates
                ''',
                'fpus_upd_total_time',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'fpd-platf-upd-stats',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Protocols.Protocol.Misc.MiProtoDbgStat.FpdGtrieTiming.FgtGtrieFnTiming' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Protocols.Protocol.Misc.MiProtoDbgStat.FpdGtrieTiming.FgtGtrieFnTiming',
            False, 
            [
            _MetaInfoClassMember('fgft-fn', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Gtrie operation
                ''',
                'fgft_fn',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fgft-max-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Time for the update
                ''',
                'fgft_max_time',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fgft-max-tstamp', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Time stamp of max update
                ''',
                'fgft_max_tstamp',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fgft-tot-upd-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total time for updates
                ''',
                'fgft_tot_upd_time',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fgft-tot-updates', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total number of updates
                ''',
                'fgft_tot_updates',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fgft-tot-updates-zero', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total number of updates with zero timing (due to
                timestamp granularity)
                ''',
                'fgft_tot_updates_zero',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'fgt-gtrie-fn-timing',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Protocols.Protocol.Misc.MiProtoDbgStat.FpdGtrieTiming' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Protocols.Protocol.Misc.MiProtoDbgStat.FpdGtrieTiming',
            False, 
            [
            _MetaInfoClassMember('fgt-gtrie-fn-timing', REFERENCE_LIST, 'FgtGtrieFnTiming' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Protocols.Protocol.Misc.MiProtoDbgStat.FpdGtrieTiming.FgtGtrieFnTiming', 
                [], [], 
                '''                Array of max time info indexed by gtrie function
                ''',
                'fgt_gtrie_fn_timing',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fgt-num-failure', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of unsuccessful updates
                ''',
                'fgt_num_failure',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fgt-num-success', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of successful updates
                ''',
                'fgt_num_success',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fgt-upd-total-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total time for all pd updates
                ''',
                'fgt_upd_total_time',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'fpd-gtrie-timing',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Protocols.Protocol.Misc.MiProtoDbgStat' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Protocols.Protocol.Misc.MiProtoDbgStat',
            False, 
            [
            _MetaInfoClassMember('fpd-adj-del', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                the number of adjacency deletes
                ''',
                'fpd_adj_del',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fpd-adj-drops', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                 number of adj updates dropped because of OOR
                ''',
                'fpd_adj_drops',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fpd-adj-msg', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                number of AIB messages
                ''',
                'fpd_adj_msg',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fpd-adj-tx-retry-nh-found', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                number of TX adj retries that found or created
                NH
                ''',
                'fpd_adj_tx_retry_nh_found',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fpd-adj-tx-retry-obj-reinit', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                number of times TX NH retry objects updated
                ''',
                'fpd_adj_tx_retry_obj_reinit',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fpd-adj-upd', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                the number of adjacency updates
                ''',
                'fpd_adj_upd',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fpd-adj-upd-tx', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                number of TX adjacency updates from AIB
                ''',
                'fpd_adj_upd_tx',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fpd-adj-upd-tx-nh-found', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                number of TX adjacency updates that found or
                created NH
                ''',
                'fpd_adj_upd_tx_nh_found',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fpd-adj-upd-tx-retry-created', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                number of TX adjacency updates that went to
                retry
                ''',
                'fpd_adj_upd_tx_retry_created',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fpd-bcdl-msgs', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                the number of bcdl msgs
                ''',
                'fpd_bcdl_msgs',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fpd-gbltbl-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                the number of fib entries in global tbl
                ''',
                'fpd_gbltbl_entries',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fpd-gbltbl-rej-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                the number of fib entries in global retry tbl
                ''',
                'fpd_gbltbl_rej_entries',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fpd-gbltbl-src-entry', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of global routes from                    
                each route source
                ''',
                'fpd_gbltbl_src_entry',
                'Cisco-IOS-XR-fib-common-oper', False, max_elements=14),
            _MetaInfoClassMember('fpd-gtrie-timing', REFERENCE_CLASS, 'FpdGtrieTiming' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Protocols.Protocol.Misc.MiProtoDbgStat.FpdGtrieTiming', 
                [], [], 
                '''                Gtrie timing statistics
                ''',
                'fpd_gtrie_timing',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fpd-lbl-recycled', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                the number of routes handled with recycled label
                ''',
                'fpd_lbl_recycled',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fpd-ldi-avg-backup-activate-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                avg ldi mod time for backup activation
                ''',
                'fpd_ldi_avg_backup_activate_time',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fpd-ldi-backup-activate-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                number of ldi backup path activications
                ''',
                'fpd_ldi_backup_activate_count',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fpd-ldi-last-backup-activate-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                ldi mod time for last backup activation
                ''',
                'fpd_ldi_last_backup_activate_time',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fpd-ldi-max-backup-activate-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                max ldi mod time for backup activation
                ''',
                'fpd_ldi_max_backup_activate_time',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fpd-ldi-min-backup-activate-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                min ldi mod time for backup activation
                ''',
                'fpd_ldi_min_backup_activate_time',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fpd-ldi-num-correct-fixup', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                the number of corrected fixup LDIs
                ''',
                'fpd_ldi_num_correct_fixup',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fpd-ldi-num-del-refcnt', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                the number of deleted with non-zero refcount
                ''',
                'fpd_ldi_num_del_refcnt',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fpd-ldi-num-fixedup', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                the number of fixup LDIs
                ''',
                'fpd_ldi_num_fixedup',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fpd-ldi-total-backup-activate-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                total ldi mod time for backup activation
                ''',
                'fpd_ldi_total_backup_activate_time',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fpd-num-allocs', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                the number of allocs for this proto
                ''',
                'fpd_num_allocs',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fpd-num-frees', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                the number of frees for this proto
                ''',
                'fpd_num_frees',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fpd-num-retry', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                the number of retries of each type
                ''',
                'fpd_num_retry',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fpd-num-retry-touts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                the number of retry timeouts
                ''',
                'fpd_num_retry_touts',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fpd-num-tbls', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                the number of tables in table set
                ''',
                'fpd_num_tbls',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fpd-pl-backup-disable-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                 number of PLs unmarked to include backup path
                ''',
                'fpd_pl_backup_disable_count',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fpd-pl-backup-enable-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                number of PLs marked to include backup path
                ''',
                'fpd_pl_backup_enable_count',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fpd-pl-fast-nfn-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                number of PLs visited on fast notification
                ''',
                'fpd_pl_fast_nfn_count',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fpd-pl-inline-res-q', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                the number of PLs linked to resolving tables for
                inline res
                ''',
                'fpd_pl_inline_res_q',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fpd-pl-num-correct-fixup', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                the number of corrected fixup PLs
                ''',
                'fpd_pl_num_correct_fixup',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fpd-pl-num-queued-fixedup', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                the number of PL queued for fixup
                ''',
                'fpd_pl_num_queued_fixedup',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fpd-pl-retry-add-exist', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                the number PLs added to retry while already in
                retry
                ''',
                'fpd_pl_retry_add_exist',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fpd-pl-with-backup-create-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                number of pl creates with backu path
                ''',
                'fpd_pl_with_backup_create_count',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fpd-pl-with-backup-del-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                number of pl deletes with backup path
                ''',
                'fpd_pl_with_backup_del_count',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fpd-platf-upd-stats', REFERENCE_CLASS, 'FpdPlatfUpdStats' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Protocols.Protocol.Misc.MiProtoDbgStat.FpdPlatfUpdStats', 
                [], [], 
                '''                platform update statistics
                ''',
                'fpd_platf_upd_stats',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fpd-recursion-constraint-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                number of resolution failures because of
                recursion constraint
                ''',
                'fpd_recursion_constraint_count',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fpd-retryq-size', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                the number of elements in retryq
                ''',
                'fpd_retryq_size',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fpd-route-del', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                the number of route deletes
                ''',
                'fpd_route_del',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fpd-route-drops', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                the number of routes dropped
                ''',
                'fpd_route_drops',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fpd-route-rcv', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                the number of routes received
                ''',
                'fpd_route_rcv',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fpd-route-upd', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                the number of route updates
                ''',
                'fpd_route_upd',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fpd-te-rcv', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                the number of TE upds received
                ''',
                'fpd_te_rcv',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fpd-te-version-mismatch-drops', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                the number of TE upds dropped because of version
                mismatch
                ''',
                'fpd_te_version_mismatch_drops',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fpd-version-mismatch-drops', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                the number of routes dropped because of version
                mismatch
                ''',
                'fpd_version_mismatch_drops',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fpd-vrftbl-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                the number of fib entries in vrf tbls
                ''',
                'fpd_vrftbl_entries',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fpd-vrftbl-rej-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                the number of fib entries in vrf retry tbls
                ''',
                'fpd_vrftbl_rej_entries',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fpd-vrftbl-src-entry', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of vrf routes from                       
                each route source
                ''',
                'fpd_vrftbl_src_entry',
                'Cisco-IOS-XR-fib-common-oper', False, max_elements=14),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'mi-proto-dbg-stat',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Protocols.Protocol.Misc.MiIdbPurgeCntr' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Protocols.Protocol.Misc.MiIdbPurgeCntr',
            False, 
            [
            _MetaInfoClassMember('fpp-cntr', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                the number of frees for this proto
                ''',
                'fpp_cntr',
                'Cisco-IOS-XR-fib-common-oper', False, max_elements=3),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'mi-idb-purge-cntr',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Protocols.Protocol.Misc.MiDel' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Protocols.Protocol.Misc.MiDel',
            False, 
            [
            _MetaInfoClassMember('msec-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                msec time
                ''',
                'msec_time',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('prfx', ATTRIBUTE, 'str' , None, None, 
                [(0, 16)], [], 
                '''                prfx
                ''',
                'prfx',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('prfx-len', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                prfx len
                ''',
                'prfx_len',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('prfx-proto', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                prfx proto
                ''',
                'prfx_proto',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('tableid', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                tableid
                ''',
                'tableid',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'mi-del',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Protocols.Protocol.Misc.MiFrrStat' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Protocols.Protocol.Misc.MiFrrStat',
            False, 
            [
            _MetaInfoClassMember('mi-num-bfd-down', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                number of NH down FRR events frm BFD
                ''',
                'mi_num_bfd_down',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('mi-num-bkup-frr-objects', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                total number of backup FRR objects
                ''',
                'mi_num_bkup_frr_objects',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('mi-num-frr-logs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                frr log size
                ''',
                'mi_num_frr_logs',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('mi-num-frr-proto-events', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                number of frr events received in proto thread
                ''',
                'mi_num_frr_proto_events',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('mi-num-frr-reset', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                number of frr resets
                ''',
                'mi_num_frr_reset',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('mi-num-frr-reset-queue-adds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                number of frr reset queue adds
                ''',
                'mi_num_frr_reset_queue_adds',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('mi-num-frr-reset-queue-remove', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                number of frr reset queue deletes
                ''',
                'mi_num_frr_reset_queue_remove',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('mi-num-intf-frr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                number of FRR events sent on nh interface down
                ''',
                'mi_num_intf_frr',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('mi-num-parent-intf-frr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                number of FRR events sent on nh parent interface
                down
                ''',
                'mi_num_parent_intf_frr',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('mi-num-pfi-intf-down', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                number of interface down FRR events from PFI
                ''',
                'mi_num_pfi_intf_down',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('mi-num-prot-frr-objects', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                total number of prot FRR objects
                ''',
                'mi_num_prot_frr_objects',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('mi-num-tunid-alloc-failures', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                total number of FRR tunnel ID allocation
                failures
                ''',
                'mi_num_tunid_alloc_failures',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('mi-num-tunid-allocs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                total number of successful FRR tunnel ID
                allocations
                ''',
                'mi_num_tunid_allocs',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('mi-num-tunid-free-failures', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                total number of FRR tunnel ID free failures
                ''',
                'mi_num_tunid_free_failures',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('mi-num-tunid-frees', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                total number of successful FRR tunnel ID frees
                ''',
                'mi_num_tunid_frees',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'mi-frr-stat',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Protocols.Protocol.Misc' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Protocols.Protocol.Misc',
            False, 
            [
            _MetaInfoClassMember('mi-clock-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                clock download time
                ''',
                'mi_clock_time',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('mi-cpu-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                CPU download time
                ''',
                'mi_cpu_time',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('mi-cpuless-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                count of cpuless line cards
                ''',
                'mi_cpuless_count',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('mi-cpuless-init', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                cpuless node list init
                ''',
                'mi_cpuless_init',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('mi-cpuless-node', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                list of cpuless line cards
                ''',
                'mi_cpuless_node',
                'Cisco-IOS-XR-fib-common-oper', False, max_elements=20),
            _MetaInfoClassMember('mi-del', REFERENCE_LIST, 'MiDel' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Protocols.Protocol.Misc.MiDel', 
                [], [], 
                '''                Timestamps of deleted routes
                ''',
                'mi_del',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('mi-frr-stat', REFERENCE_LIST, 'MiFrrStat' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Protocols.Protocol.Misc.MiFrrStat', 
                [], [], 
                '''                FRR statistics
                ''',
                'mi_frr_stat',
                'Cisco-IOS-XR-fib-common-oper', False, max_elements=3),
            _MetaInfoClassMember('mi-idb-ext-cleanup-failed-count', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of recycled idb extensions that failed
                cleanup
                ''',
                'mi_idb_ext_cleanup_failed_count',
                'Cisco-IOS-XR-fib-common-oper', False, max_elements=3),
            _MetaInfoClassMember('mi-idb-lsec-enabled-num', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of interfaces having label security
                enabled
                ''',
                'mi_idb_lsec_enabled_num',
                'Cisco-IOS-XR-fib-common-oper', False, max_elements=3),
            _MetaInfoClassMember('mi-idb-purge-cntr', REFERENCE_LIST, 'MiIdbPurgeCntr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Protocols.Protocol.Misc.MiIdbPurgeCntr', 
                [], [], 
                '''                the number of counters used for purge counter
                stats
                ''',
                'mi_idb_purge_cntr',
                'Cisco-IOS-XR-fib-common-oper', False, max_elements=3),
            _MetaInfoClassMember('mi-idb-recycle-cleanup-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of idb cleaned up after hitting ifh
                recycle
                ''',
                'mi_idb_recycle_cleanup_count',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('mi-idb-recycle-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of idbs that hit ifh recycle
                ''',
                'mi_idb_recycle_count',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('mi-issu-state', REFERENCE_CLASS, 'MiIssuState' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Protocols.Protocol.Misc.MiIssuState', 
                [], [], 
                '''                FIB ISSU state
                ''',
                'mi_issu_state',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('mi-lrpf-num', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Per protocol number of label RPFs
                ''',
                'mi_lrpf_num',
                'Cisco-IOS-XR-fib-common-oper', False, max_elements=3),
            _MetaInfoClassMember('mi-lrpf-stats-act', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Per protocol actions stats for label RPF
                ''',
                'mi_lrpf_stats_act',
                'Cisco-IOS-XR-fib-common-oper', False, max_elements=24),
            _MetaInfoClassMember('mi-lrpf-stats-fail', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Per protocol Failure stats for label RPF
                ''',
                'mi_lrpf_stats_fail',
                'Cisco-IOS-XR-fib-common-oper', False, max_elements=9),
            _MetaInfoClassMember('mi-num-lisp-eid', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                number of LISP EID prefixes
                ''',
                'mi_num_lisp_eid',
                'Cisco-IOS-XR-fib-common-oper', False, max_elements=3),
            _MetaInfoClassMember('mi-num-lisp-valid-eid', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                number of LISP EID prefixes eligible for
                forwarding
                ''',
                'mi_num_lisp_valid_eid',
                'Cisco-IOS-XR-fib-common-oper', False, max_elements=3),
            _MetaInfoClassMember('mi-num-mgmt-list', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of management interfaces
                ''',
                'mi_num_mgmt_list',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('mi-num-virtual-ll-addresses-added', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                mi num virtual ll addresses added
                ''',
                'mi_num_virtual_ll_addresses_added',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('mi-num-virtual-ll-addresses-cached', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                mi num virtual ll addresses cached
                ''',
                'mi_num_virtual_ll_addresses_cached',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('mi-num-virtual-ll-addresses-deleted', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                mi num virtual ll addresses deleted
                ''',
                'mi_num_virtual_ll_addresses_deleted',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('mi-num-virtual-ll-addresses-dropped', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                mi num virtual ll addresses dropped
                ''',
                'mi_num_virtual_ll_addresses_dropped',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('mi-pfi-ifh-del', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                number of pfi ifh delete notif
                ''',
                'mi_pfi_ifh_del',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('mi-pfi-ifh-stale', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                number of stale ifh removed
                ''',
                'mi_pfi_ifh_stale',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('mi-pfi-ifh-upd', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                number of pfi ifh create notif
                ''',
                'mi_pfi_ifh_upd',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('mi-plat-capabilities', REFERENCE_CLASS, 'MiPlatCapabilities' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Protocols.Protocol.Misc.MiPlatCapabilities', 
                [], [], 
                '''                FIB platform capabilities
                ''',
                'mi_plat_capabilities',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('mi-prefer-aib-routes-over-rib-cfg', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Prefer AIB routes over RIB/LSD configured state
                ''',
                'mi_prefer_aib_routes_over_rib_cfg',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('mi-prefer-aib-routes-over-rib-oper', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Prefer AIB routes over RIB/LSD operational state
                ''',
                'mi_prefer_aib_routes_over_rib_oper',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('mi-proto-dbg-stat', REFERENCE_LIST, 'MiProtoDbgStat' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Protocols.Protocol.Misc.MiProtoDbgStat', 
                [], [], 
                '''                Per protocol debug stats
                ''',
                'mi_proto_dbg_stat',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('mi-shm-reset-ts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Last FIB shared memory reset time stamp
                ''',
                'mi_shm_reset_ts',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('mi-tot-dnld-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                total download time
                ''',
                'mi_tot_dnld_time',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('mi-tot-gtrie-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                total time spent in gtrie operations
                ''',
                'mi_tot_gtrie_time',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('mi-tot-plat-upd-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                total platform update time
                ''',
                'mi_tot_plat_upd_time',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'misc',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Protocols.Protocol.LocalLabel.Conflicts.Conflict.Ext.Pfx' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Protocols.Protocol.LocalLabel.Conflicts.Conflict.Ext.Pfx',
            False, 
            [
            _MetaInfoClassMember('pfx', ATTRIBUTE, 'str' , None, None, 
                [(0, 52)], [], 
                '''                pfx
                ''',
                'pfx',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('tbl-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                tbl id
                ''',
                'tbl_id',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'pfx',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Protocols.Protocol.LocalLabel.Conflicts.Conflict.Ext.Lsm' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Protocols.Protocol.LocalLabel.Conflicts.Conflict.Ext.Lsm',
            False, 
            [
            _MetaInfoClassMember('mcast-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                mcast id
                ''',
                'mcast_id',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('nh', ATTRIBUTE, 'str' , None, None, 
                [(0, 52)], [], 
                '''                nh
                ''',
                'nh',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'lsm',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Protocols.Protocol.LocalLabel.Conflicts.Conflict.Ext' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Protocols.Protocol.LocalLabel.Conflicts.Conflict.Ext',
            False, 
            [
            _MetaInfoClassMember('lsm', REFERENCE_CLASS, 'Lsm' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Protocols.Protocol.LocalLabel.Conflicts.Conflict.Ext.Lsm', 
                [], [], 
                '''                lsm
                ''',
                'lsm',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('pfx', REFERENCE_CLASS, 'Pfx' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Protocols.Protocol.LocalLabel.Conflicts.Conflict.Ext.Pfx', 
                [], [], 
                '''                pfx
                ''',
                'pfx',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'FibMplsLlcEntryBagEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'FibMplsLlcEntryBagEnum', 
                [], [], 
                '''                type
                ''',
                'type',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'ext',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Protocols.Protocol.LocalLabel.Conflicts.Conflict' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Protocols.Protocol.LocalLabel.Conflicts.Conflict',
            False, 
            [
            _MetaInfoClassMember('ext', REFERENCE_CLASS, 'Ext' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Protocols.Protocol.LocalLabel.Conflicts.Conflict.Ext', 
                [], [], 
                '''                ext
                ''',
                'ext',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('label', ATTRIBUTE, 'int' , None, None, 
                [('16', '1048575')], [], 
                '''                Local label
                ''',
                'label',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('ll-ctype', REFERENCE_ENUM_CLASS, 'FibllcEntryEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'FibllcEntryEnum', 
                [], [], 
                '''                Type of entry
                ''',
                'll_ctype',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('local-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                local label
                ''',
                'local_label',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('num-retries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                num retries
                ''',
                'num_retries',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('pfx-tbl-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Table ID of IP prefix
                ''',
                'pfx_tbl_id',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                IP Prefix
                ''',
                'prefix',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('prefix-len', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Length of IP Prefix
                ''',
                'prefix_len',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('retry-ts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                retry ts
                ''',
                'retry_ts',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('source', REFERENCE_ENUM_CLASS, 'FibRouteSourceEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'FibRouteSourceEnum', 
                [], [], 
                '''                Route source
                ''',
                'source',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('source-xr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                source xr
                ''',
                'source_xr',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('update-ts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                update ts
                ''',
                'update_ts',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'conflict',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Protocols.Protocol.LocalLabel.Conflicts' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Protocols.Protocol.LocalLabel.Conflicts',
            False, 
            [
            _MetaInfoClassMember('conflict', REFERENCE_LIST, 'Conflict' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Protocols.Protocol.LocalLabel.Conflicts.Conflict', 
                [], [], 
                '''                CEF Local-label conflicts entry
                ''',
                'conflict',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'conflicts',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Protocols.Protocol.LocalLabel' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Protocols.Protocol.LocalLabel',
            False, 
            [
            _MetaInfoClassMember('conflicts', REFERENCE_CLASS, 'Conflicts' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Protocols.Protocol.LocalLabel.Conflicts', 
                [], [], 
                '''                FIB Local-label conflicts database
                ''',
                'conflicts',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'local-label',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Protocols.Protocol' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Protocols.Protocol',
            False, 
            [
            _MetaInfoClassMember('protocol-name', REFERENCE_ENUM_CLASS, 'FibProtocolEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'FibProtocolEnum', 
                [], [], 
                '''                Protocol Name 
                ''',
                'protocol_name',
                'Cisco-IOS-XR-fib-common-oper', True),
            _MetaInfoClassMember('external-client-summaries', REFERENCE_CLASS, 'ExternalClientSummaries' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Protocols.Protocol.ExternalClientSummaries', 
                [], [], 
                '''                External Client Summary Table
                ''',
                'external_client_summaries',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('external-summary-all', REFERENCE_CLASS, 'ExternalSummaryAll' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Protocols.Protocol.ExternalSummaryAll', 
                [], [], 
                '''                Summary for all external clients
                ''',
                'external_summary_all',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('fib-summaries', REFERENCE_CLASS, 'FibSummaries' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Protocols.Protocol.FibSummaries', 
                [], [], 
                '''                Summary for FIB tables
                ''',
                'fib_summaries',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('frr-log', REFERENCE_CLASS, 'FrrLog' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Protocols.Protocol.FrrLog', 
                [], [], 
                '''                Table of Fast Reroute activation logs
                ''',
                'frr_log',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('issu-state', REFERENCE_CLASS, 'IssuState' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Protocols.Protocol.IssuState', 
                [], [], 
                '''                CEF ISSU State
                ''',
                'issu_state',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('local-label', REFERENCE_CLASS, 'LocalLabel' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Protocols.Protocol.LocalLabel', 
                [], [], 
                '''                Local label
                ''',
                'local_label',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('misc', REFERENCE_CLASS, 'Misc' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Protocols.Protocol.Misc', 
                [], [], 
                '''                CEF misc hidden data
                ''',
                'misc',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('nh-ids', REFERENCE_CLASS, 'NhIds' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Protocols.Protocol.NhIds', 
                [], [], 
                '''                NHIdTable is accessed by two keys;
                {NHIdValue} and/or {NHInterface,NHAddress
                ''',
                'nh_ids',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('resource', REFERENCE_CLASS, 'Resource' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Protocols.Protocol.Resource', 
                [], [], 
                '''                Resource information
                ''',
                'resource',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('vrfs', REFERENCE_CLASS, 'Vrfs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Protocols.Protocol.Vrfs', 
                [], [], 
                '''                VRF table
                ''',
                'vrfs',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'protocol',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node.Protocols' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node.Protocols',
            False, 
            [
            _MetaInfoClassMember('protocol', REFERENCE_LIST, 'Protocol' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Protocols.Protocol', 
                [], [], 
                '''                Protocol table entry
                ''',
                'protocol',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'protocols',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes.Node',
            False, 
            [
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Node name
                ''',
                'node_name',
                'Cisco-IOS-XR-fib-common-oper', True),
            _MetaInfoClassMember('global', REFERENCE_CLASS, 'Global_' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Global_', 
                [], [], 
                '''                FIB Global info
                ''',
                'global_',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('protocols', REFERENCE_CLASS, 'Protocols' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node.Protocols', 
                [], [], 
                '''                Protocol table
                ''',
                'protocols',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'node',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib.Nodes' : {
        'meta_info' : _MetaInfoClass('Fib.Nodes',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes.Node', 
                [], [], 
                '''                Operational data for a specific Node
                ''',
                'node',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'nodes',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'Fib' : {
        'meta_info' : _MetaInfoClass('Fib',
            False, 
            [
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'Fib.Nodes', 
                [], [], 
                '''                Table of nodes
                ''',
                'nodes',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'fib',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'MplsForwarding.Nodes.Node.ForwardingSummary' : {
        'meta_info' : _MetaInfoClass('MplsForwarding.Nodes.Node.ForwardingSummary',
            False, 
            [
            _MetaInfoClassMember('deleted-stale-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of delete stale label entries
                ''',
                'deleted_stale_entries',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('global-dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of global FIB packets dropped
                ''',
                'global_dropped_packets',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('global-failed-lookups', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of global failed lookups
                ''',
                'global_failed_lookups',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('global-fragmented-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of global FIB packets fragmented
                ''',
                'global_fragmented_packets',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('highest-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Highest Label in use
                ''',
                'highest_label',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('ignore-protect', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of TE tunnels treated as non-protected
                ''',
                'ignore_protect',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('ipv4-imposition-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of IPv4 imposition entries
                ''',
                'ipv4_imposition_entries',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('label-switched-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of label swap/disposition entries
                ''',
                'label_switched_entries',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('lowest-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Lowest label in use
                ''',
                'lowest_label',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('lrpf-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of labels with RPF
                ''',
                'lrpf_entries',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('mte-head-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of MTE tunnel head entries
                ''',
                'mte_head_entries',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('mte-ll-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of MTE local entries
                ''',
                'mte_ll_entries',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('mte-midpoint-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of MTE midpoint entries
                ''',
                'mte_midpoint_entries',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('reserved-label-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of reserved label entries
                ''',
                'reserved_label_entries',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('te-frr-head-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of TE FRR tunnel head imposition entries
                ''',
                'te_frr_head_entries',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('te-frr-interface-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of TE FRR protected interface entries
                ''',
                'te_frr_interface_entries',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('te-frr-internal-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of TE internal forwarding entries
                ''',
                'te_frr_internal_entries',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('te-frr-mid-points-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of TE FRR MidPoints forwarding entries
                ''',
                'te_frr_mid_points_entries',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('te-frr-next-hop-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of TE FRR protected next-hop entries
                ''',
                'te_frr_next_hop_entries',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('te-head-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of TE tunnel head imposition entries
                ''',
                'te_head_entries',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('te-internal-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of TE internal forwarding entries
                ''',
                'te_internal_entries',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('te-mid-points-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of TE MidPoints forwarding entries
                ''',
                'te_mid_points_entries',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('total-forwarding-update-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total forwarding update messages from LSD to
                LFDs
                ''',
                'total_forwarding_update_messages',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('total-forwarding-updates', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total forwarding updates from LSD to LFDs
                ''',
                'total_forwarding_updates',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('total-p2mp-forwarding-added-or-modify-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total p2mp forwarding add/modify messages from
                MRIB to LFDs
                ''',
                'total_p2mp_forwarding_added_or_modify_messages',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('total-p2mp-forwarding-delete-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total p2mp forwarding del messages from MRIB to
                LFDs
                ''',
                'total_p2mp_forwarding_delete_messages',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('total-p2mp-forwarding-drop-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total p2mp forwarding messages dropped from MRIB
                to LFDs
                ''',
                'total_p2mp_forwarding_drop_messages',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('total-p2mp-forwarding-updates', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total forwarding updates from MRIB to LFDs
                ''',
                'total_p2mp_forwarding_updates',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('total-p2mp-iir-forwarding-drop-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total IIR triggered p2mp forwarding MRIB
                messages dropped
                ''',
                'total_p2mp_iir_forwarding_drop_messages',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'forwarding-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'MplsForwarding.Nodes.Node.FrrLogs.FrrLog.StartTime' : {
        'meta_info' : _MetaInfoClass('MplsForwarding.Nodes.Node.FrrLogs.FrrLog.StartTime',
            False, 
            [
            _MetaInfoClassMember('nanoseconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Nanoseconds part of time value
                ''',
                'nanoseconds',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Seconds part of time valueiin UTC
                ''',
                'seconds',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'start-time',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'MplsForwarding.Nodes.Node.FrrLogs.FrrLog' : {
        'meta_info' : _MetaInfoClass('MplsForwarding.Nodes.Node.FrrLogs.FrrLog',
            False, 
            [
            _MetaInfoClassMember('event-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Event ID
                ''',
                'event_id',
                'Cisco-IOS-XR-fib-common-oper', True),
            _MetaInfoClassMember('fast-bundle-member-down-interface', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Fast Bundle Member Down Interface
                ''',
                'fast_bundle_member_down_interface',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('frr-event-node-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Node on which the FRR event happened
                ''',
                'frr_event_node_id',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('main-processing', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Main Processing for FRR
                ''',
                'main_processing',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('next-hop', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Next Hop
                ''',
                'next_hop',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('number-of-rewrites-affected', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of rewrites affected
                ''',
                'number_of_rewrites_affected',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('protected-frr-interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'protected_frr_interface_name',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('start-time', REFERENCE_CLASS, 'StartTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'MplsForwarding.Nodes.Node.FrrLogs.FrrLog.StartTime', 
                [], [], 
                '''                Time of FRR event processing start, Seconds in
                UTC, and Nano Seconds
                ''',
                'start_time',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('switching-time-nsecs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Time to switch rewrites [nsecs]
                ''',
                'switching_time_nsecs',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'frr-log',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'MplsForwarding.Nodes.Node.FrrLogs' : {
        'meta_info' : _MetaInfoClass('MplsForwarding.Nodes.Node.FrrLogs',
            False, 
            [
            _MetaInfoClassMember('frr-log', REFERENCE_LIST, 'FrrLog' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'MplsForwarding.Nodes.Node.FrrLogs.FrrLog', 
                [], [], 
                '''                FRR Log information
                ''',
                'frr_log',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'frr-logs',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'MplsForwarding.Nodes.Node.LabelFib.ForwardingDetails.ForwardingDetail.LdiInformation' : {
        'meta_info' : _MetaInfoClass('MplsForwarding.Nodes.Node.LabelFib.ForwardingDetails.ForwardingDetail.LdiInformation',
            False, 
            [
            _MetaInfoClassMember('ldi-hardware-information', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Hardware info
                ''',
                'ldi_hardware_information',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'ldi-information',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'MplsForwarding.Nodes.Node.LabelFib.ForwardingDetails.ForwardingDetail.MulticastInformation' : {
        'meta_info' : _MetaInfoClass('MplsForwarding.Nodes.Node.LabelFib.ForwardingDetails.ForwardingDetail.MulticastInformation',
            False, 
            [
            _MetaInfoClassMember('multicast-encap-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The multicast ENCAP-ID 
                ''',
                'multicast_encap_id',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('multicast-mol-base-flags', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                MOL base flags
                ''',
                'multicast_mol_base_flags',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('multicast-mol-flags', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                MOL flags
                ''',
                'multicast_mol_flags',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('multicast-mol-referance-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                MOL refcount
                ''',
                'multicast_mol_referance_count',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('multicast-mpls-local-output-paths', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                num multicast mpls local output paths
                ''',
                'multicast_mpls_local_output_paths',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('multicast-mpls-output-paths', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                num multicast mpls output paths 
                ''',
                'multicast_mpls_output_paths',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('multicast-mpls-protocol-output-paths', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                num multicast mpls prot output paths 
                ''',
                'multicast_mpls_protocol_output_paths',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('multicast-platform-data', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                The multicast platform data
                ''',
                'multicast_platform_data',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('multicast-platform-data-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The multicast platform data len
                ''',
                'multicast_platform_data_length',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('multicast-rpf-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The multicast RPF-ID 
                ''',
                'multicast_rpf_id',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('multicast-tunnel-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                multicast mpls P2MP-TE tunnel id or MLDP Tunnel
                LSMID on all nodes
                ''',
                'multicast_tunnel_id',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('multicast-tunnel-interface-handler', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                multicast mpls tunnel
                ''',
                'multicast_tunnel_interface_handler',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('multicast-tunnel-lspvif', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                multicast LSPVIF for MLDP Tunnels
                ''',
                'multicast_tunnel_lspvif',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('multicast-tunnel-next-hop-information', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                multicast nhinfo for p2mp TE Head
                ''',
                'multicast_tunnel_next_hop_information',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'multicast-information',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'MplsForwarding.Nodes.Node.LabelFib.ForwardingDetails.ForwardingDetail.LabelInformation.LabelInformationDetail' : {
        'meta_info' : _MetaInfoClass('MplsForwarding.Nodes.Node.LabelFib.ForwardingDetails.ForwardingDetail.LabelInformation.LabelInformationDetail',
            False, 
            [
            _MetaInfoClassMember('l3-mtu', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                L3 MTU
                ''',
                'l3_mtu',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('label-stack', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Label stack
                ''',
                'label_stack',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('mac-size', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Length of L2 encapsulation
                ''',
                'mac_size',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('next-hop-interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Next hop interface
                ''',
                'next_hop_interface',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('next-hop-protocol', REFERENCE_ENUM_CLASS, 'ProtoEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'ProtoEnum', 
                [], [], 
                '''                The address family (V4/V6) 
                ''',
                'next_hop_protocol',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('next-hop-string', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Next hop address in string format
                ''',
                'next_hop_string',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('status', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Status
                ''',
                'status',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('total-encapsulation-size', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total encapsulation size: L2 + MPLS
                ''',
                'total_encapsulation_size',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('transmit-number-of-bytes-switched', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of Bytes switched
                ''',
                'transmit_number_of_bytes_switched',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('transmit-number-of-packets-switched', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of packets switched
                ''',
                'transmit_number_of_packets_switched',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'label-information-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'MplsForwarding.Nodes.Node.LabelFib.ForwardingDetails.ForwardingDetail.LabelInformation' : {
        'meta_info' : _MetaInfoClass('MplsForwarding.Nodes.Node.LabelFib.ForwardingDetails.ForwardingDetail.LabelInformation',
            False, 
            [
            _MetaInfoClassMember('label-information-detail', REFERENCE_CLASS, 'LabelInformationDetail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'MplsForwarding.Nodes.Node.LabelFib.ForwardingDetails.ForwardingDetail.LabelInformation.LabelInformationDetail', 
                [], [], 
                '''                Detail label info
                ''',
                'label_information_detail',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('label-information-next-hop-protocol', REFERENCE_ENUM_CLASS, 'ProtoEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'ProtoEnum', 
                [], [], 
                '''                The address family (v4/v6) 
                ''',
                'label_information_next_hop_protocol',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('label-information-next-hop-string', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Next hop address in string format
                ''',
                'label_information_next_hop_string',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('label-information-next-hop-type', REFERENCE_ENUM_CLASS, 'NextHopEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'NextHopEnum', 
                [], [], 
                '''                NHinfo Type
                ''',
                'label_information_next_hop_type',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('label-information-path-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LabelInformationPathIndex
                ''',
                'label_information_path_index',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('label-information-route-version', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The version of the route
                ''',
                'label_information_route_version',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('label-information-time-in-milli-seconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The time of last update in msec
                ''',
                'label_information_time_in_milli_seconds',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('label-information-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Label-Info type
                ''',
                'label_information_type',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('local-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Local label
                ''',
                'local_label',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('mpls-adjacency-flags', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                MPLS Adjacency flags
                ''',
                'mpls_adjacency_flags',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('outgoing-interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Outgoing interface
                ''',
                'outgoing_interface',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('outgoing-interface-string', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Output Interface in string format
                ''',
                'outgoing_interface_string',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('outgoing-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Outgoing label
                ''',
                'outgoing_label',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('outgoing-label-string', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Output Label in string format
                ''',
                'outgoing_label_string',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('outgoing-physical-interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Outgoing Physical Interface
                ''',
                'outgoing_physical_interface',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('prefix-or-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Prefix Or ID
                ''',
                'prefix_or_id',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('tunnel-id-present', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Tunnel id present?
                ''',
                'tunnel_id_present',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('tunnel-interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Tunnel Interface
                ''',
                'tunnel_interface',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('tx-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Bytes transmitted per LSP
                ''',
                'tx_bytes',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('tx-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Packets transmitted per LSP
                ''',
                'tx_packets',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'label-information',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'MplsForwarding.Nodes.Node.LabelFib.ForwardingDetails.ForwardingDetail' : {
        'meta_info' : _MetaInfoClass('MplsForwarding.Nodes.Node.LabelFib.ForwardingDetails.ForwardingDetail',
            False, 
            [
            _MetaInfoClassMember('afi-table-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The AFI table ID
                ''',
                'afi_table_id',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('eos', REFERENCE_ENUM_CLASS, 'MplseosEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'MplseosEnum', 
                [], [], 
                '''                End of stack flag
                ''',
                'eos',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('eos-bit', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                EOS bit
                ''',
                'eos_bit',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('hardware-information', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Hardware info
                ''',
                'hardware_information',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('label-information', REFERENCE_LIST, 'LabelInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'MplsForwarding.Nodes.Node.LabelFib.ForwardingDetails.ForwardingDetail.LabelInformation', 
                [], [], 
                '''                Label-infos in FIB leaf
                ''',
                'label_information',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('label-value', ATTRIBUTE, 'int' , None, None, 
                [('16', '1048575')], [], 
                '''                Local label value
                ''',
                'label_value',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('ldi-flags', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The LDI flags
                ''',
                'ldi_flags',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('ldi-information', REFERENCE_CLASS, 'LdiInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'MplsForwarding.Nodes.Node.LabelFib.ForwardingDetails.ForwardingDetail.LdiInformation', 
                [], [], 
                '''                LDI-info in FIB leaf
                ''',
                'ldi_information',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('ldi-pointer', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The pointer to the LDI
                ''',
                'ldi_pointer',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('ldi-referance-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of references to the LDI
                ''',
                'ldi_referance_count',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('ldi-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The LDI type
                ''',
                'ldi_type',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('leaf-flags', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The leaf flags
                ''',
                'leaf_flags',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('leaf-local-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Local label
                ''',
                'leaf_local_label',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('leaf-referance-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of references to the leaf
                ''',
                'leaf_referance_count',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('leaf-time-in-milli-seconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The time of last update in msec
                ''',
                'leaf_time_in_milli_seconds',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('lspa-flags', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The LSPA flags
                ''',
                'lspa_flags',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('lw-ldi-pointer', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The pointer to the LW-LDI
                ''',
                'lw_ldi_pointer',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('lw-ldi-refernace-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The LW-LDI refcounter
                ''',
                'lw_ldi_refernace_count',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('lw-ldi-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The LW-LDI type
                ''',
                'lw_ldi_type',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('lw-shared-ldi-pointer', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The pointer to the shared LDI in LW-LDI
                ''',
                'lw_shared_ldi_pointer',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('multicast-information', REFERENCE_CLASS, 'MulticastInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'MplsForwarding.Nodes.Node.LabelFib.ForwardingDetails.ForwardingDetail.MulticastInformation', 
                [], [], 
                '''                The multicast info
                ''',
                'multicast_information',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('multicast-label', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                The unicast or multicast label
                ''',
                'multicast_label',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('path-list-flags', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The pathlist flags
                ''',
                'path_list_flags',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('path-list-referance-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of references to the pathlist
                ''',
                'path_list_referance_count',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'forwarding-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'MplsForwarding.Nodes.Node.LabelFib.ForwardingDetails' : {
        'meta_info' : _MetaInfoClass('MplsForwarding.Nodes.Node.LabelFib.ForwardingDetails',
            False, 
            [
            _MetaInfoClassMember('forwarding-detail', REFERENCE_LIST, 'ForwardingDetail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'MplsForwarding.Nodes.Node.LabelFib.ForwardingDetails.ForwardingDetail', 
                [], [], 
                '''                MPLS forwarding details
                ''',
                'forwarding_detail',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'forwarding-details',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'MplsForwarding.Nodes.Node.LabelFib.Informations.Information.LdiInformation' : {
        'meta_info' : _MetaInfoClass('MplsForwarding.Nodes.Node.LabelFib.Informations.Information.LdiInformation',
            False, 
            [
            _MetaInfoClassMember('ldi-hardware-information', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Hardware info
                ''',
                'ldi_hardware_information',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'ldi-information',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'MplsForwarding.Nodes.Node.LabelFib.Informations.Information.MulticastInformation' : {
        'meta_info' : _MetaInfoClass('MplsForwarding.Nodes.Node.LabelFib.Informations.Information.MulticastInformation',
            False, 
            [
            _MetaInfoClassMember('multicast-encap-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The multicast ENCAP-ID 
                ''',
                'multicast_encap_id',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('multicast-mol-base-flags', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                MOL base flags
                ''',
                'multicast_mol_base_flags',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('multicast-mol-flags', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                MOL flags
                ''',
                'multicast_mol_flags',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('multicast-mol-referance-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                MOL refcount
                ''',
                'multicast_mol_referance_count',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('multicast-mpls-local-output-paths', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                num multicast mpls local output paths
                ''',
                'multicast_mpls_local_output_paths',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('multicast-mpls-output-paths', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                num multicast mpls output paths 
                ''',
                'multicast_mpls_output_paths',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('multicast-mpls-protocol-output-paths', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                num multicast mpls prot output paths 
                ''',
                'multicast_mpls_protocol_output_paths',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('multicast-platform-data', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                The multicast platform data
                ''',
                'multicast_platform_data',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('multicast-platform-data-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The multicast platform data len
                ''',
                'multicast_platform_data_length',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('multicast-rpf-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The multicast RPF-ID 
                ''',
                'multicast_rpf_id',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('multicast-tunnel-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                multicast mpls P2MP-TE tunnel id or MLDP Tunnel
                LSMID on all nodes
                ''',
                'multicast_tunnel_id',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('multicast-tunnel-interface-handler', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                multicast mpls tunnel
                ''',
                'multicast_tunnel_interface_handler',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('multicast-tunnel-lspvif', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                multicast LSPVIF for MLDP Tunnels
                ''',
                'multicast_tunnel_lspvif',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('multicast-tunnel-next-hop-information', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                multicast nhinfo for p2mp TE Head
                ''',
                'multicast_tunnel_next_hop_information',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'multicast-information',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'MplsForwarding.Nodes.Node.LabelFib.Informations.Information.LabelInformation.LabelInformationDetail' : {
        'meta_info' : _MetaInfoClass('MplsForwarding.Nodes.Node.LabelFib.Informations.Information.LabelInformation.LabelInformationDetail',
            False, 
            [
            _MetaInfoClassMember('l3-mtu', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                L3 MTU
                ''',
                'l3_mtu',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('label-stack', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Label stack
                ''',
                'label_stack',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('mac-size', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Length of L2 encapsulation
                ''',
                'mac_size',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('next-hop-interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Next hop interface
                ''',
                'next_hop_interface',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('next-hop-protocol', REFERENCE_ENUM_CLASS, 'ProtoEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'ProtoEnum', 
                [], [], 
                '''                The address family (V4/V6) 
                ''',
                'next_hop_protocol',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('next-hop-string', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Next hop address in string format
                ''',
                'next_hop_string',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('status', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Status
                ''',
                'status',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('total-encapsulation-size', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total encapsulation size: L2 + MPLS
                ''',
                'total_encapsulation_size',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('transmit-number-of-bytes-switched', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of Bytes switched
                ''',
                'transmit_number_of_bytes_switched',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('transmit-number-of-packets-switched', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of packets switched
                ''',
                'transmit_number_of_packets_switched',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'label-information-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'MplsForwarding.Nodes.Node.LabelFib.Informations.Information.LabelInformation' : {
        'meta_info' : _MetaInfoClass('MplsForwarding.Nodes.Node.LabelFib.Informations.Information.LabelInformation',
            False, 
            [
            _MetaInfoClassMember('label-information-detail', REFERENCE_CLASS, 'LabelInformationDetail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'MplsForwarding.Nodes.Node.LabelFib.Informations.Information.LabelInformation.LabelInformationDetail', 
                [], [], 
                '''                Detail label info
                ''',
                'label_information_detail',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('label-information-next-hop-protocol', REFERENCE_ENUM_CLASS, 'ProtoEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'ProtoEnum', 
                [], [], 
                '''                The address family (v4/v6) 
                ''',
                'label_information_next_hop_protocol',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('label-information-next-hop-string', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Next hop address in string format
                ''',
                'label_information_next_hop_string',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('label-information-next-hop-type', REFERENCE_ENUM_CLASS, 'NextHopEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'NextHopEnum', 
                [], [], 
                '''                NHinfo Type
                ''',
                'label_information_next_hop_type',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('label-information-path-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LabelInformationPathIndex
                ''',
                'label_information_path_index',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('label-information-route-version', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The version of the route
                ''',
                'label_information_route_version',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('label-information-time-in-milli-seconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The time of last update in msec
                ''',
                'label_information_time_in_milli_seconds',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('label-information-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Label-Info type
                ''',
                'label_information_type',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('local-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Local label
                ''',
                'local_label',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('mpls-adjacency-flags', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                MPLS Adjacency flags
                ''',
                'mpls_adjacency_flags',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('outgoing-interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Outgoing interface
                ''',
                'outgoing_interface',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('outgoing-interface-string', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Output Interface in string format
                ''',
                'outgoing_interface_string',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('outgoing-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Outgoing label
                ''',
                'outgoing_label',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('outgoing-label-string', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Output Label in string format
                ''',
                'outgoing_label_string',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('outgoing-physical-interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Outgoing Physical Interface
                ''',
                'outgoing_physical_interface',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('prefix-or-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Prefix Or ID
                ''',
                'prefix_or_id',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('tunnel-id-present', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Tunnel id present?
                ''',
                'tunnel_id_present',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('tunnel-interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Tunnel Interface
                ''',
                'tunnel_interface',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('tx-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Bytes transmitted per LSP
                ''',
                'tx_bytes',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('tx-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Packets transmitted per LSP
                ''',
                'tx_packets',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'label-information',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'MplsForwarding.Nodes.Node.LabelFib.Informations.Information' : {
        'meta_info' : _MetaInfoClass('MplsForwarding.Nodes.Node.LabelFib.Informations.Information',
            False, 
            [
            _MetaInfoClassMember('afi-table-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The AFI table ID
                ''',
                'afi_table_id',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('eos', REFERENCE_ENUM_CLASS, 'MplseosEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'MplseosEnum', 
                [], [], 
                '''                End of stack flag
                ''',
                'eos',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('eos-bit', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                EOS bit
                ''',
                'eos_bit',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('hardware-information', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Hardware info
                ''',
                'hardware_information',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('label-information', REFERENCE_LIST, 'LabelInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'MplsForwarding.Nodes.Node.LabelFib.Informations.Information.LabelInformation', 
                [], [], 
                '''                Label-infos in FIB leaf
                ''',
                'label_information',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('label-value', ATTRIBUTE, 'int' , None, None, 
                [('16', '1048575')], [], 
                '''                Local label value
                ''',
                'label_value',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('ldi-flags', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The LDI flags
                ''',
                'ldi_flags',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('ldi-information', REFERENCE_CLASS, 'LdiInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'MplsForwarding.Nodes.Node.LabelFib.Informations.Information.LdiInformation', 
                [], [], 
                '''                LDI-info in FIB leaf
                ''',
                'ldi_information',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('ldi-pointer', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The pointer to the LDI
                ''',
                'ldi_pointer',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('ldi-referance-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of references to the LDI
                ''',
                'ldi_referance_count',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('ldi-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The LDI type
                ''',
                'ldi_type',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('leaf-flags', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The leaf flags
                ''',
                'leaf_flags',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('leaf-local-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Local label
                ''',
                'leaf_local_label',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('leaf-referance-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of references to the leaf
                ''',
                'leaf_referance_count',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('leaf-time-in-milli-seconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The time of last update in msec
                ''',
                'leaf_time_in_milli_seconds',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('lspa-flags', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The LSPA flags
                ''',
                'lspa_flags',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('lw-ldi-pointer', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The pointer to the LW-LDI
                ''',
                'lw_ldi_pointer',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('lw-ldi-refernace-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The LW-LDI refcounter
                ''',
                'lw_ldi_refernace_count',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('lw-ldi-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The LW-LDI type
                ''',
                'lw_ldi_type',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('lw-shared-ldi-pointer', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The pointer to the shared LDI in LW-LDI
                ''',
                'lw_shared_ldi_pointer',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('multicast-information', REFERENCE_CLASS, 'MulticastInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'MplsForwarding.Nodes.Node.LabelFib.Informations.Information.MulticastInformation', 
                [], [], 
                '''                The multicast info
                ''',
                'multicast_information',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('multicast-label', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                The unicast or multicast label
                ''',
                'multicast_label',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('path-list-flags', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The pathlist flags
                ''',
                'path_list_flags',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('path-list-referance-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of references to the pathlist
                ''',
                'path_list_referance_count',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'information',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'MplsForwarding.Nodes.Node.LabelFib.Informations' : {
        'meta_info' : _MetaInfoClass('MplsForwarding.Nodes.Node.LabelFib.Informations',
            False, 
            [
            _MetaInfoClassMember('information', REFERENCE_LIST, 'Information' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'MplsForwarding.Nodes.Node.LabelFib.Informations.Information', 
                [], [], 
                '''                MPLS forwarding information
                ''',
                'information',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'informations',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'MplsForwarding.Nodes.Node.LabelFib.LabelSecurity.Interfaces.Interface' : {
        'meta_info' : _MetaInfoClass('MplsForwarding.Nodes.Node.LabelFib.LabelSecurity.Interfaces.Interface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-fib-common-oper', True),
            _MetaInfoClassMember('mld-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Multi-label drop is enabled on interface
                ''',
                'mld_enabled',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('mld-supported', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Multi-label drop counters are supported per
                interface
                ''',
                'mld_supported',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('multi-label-drops', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Multi-label drops
                ''',
                'multi_label_drops',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('rpf-drops', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                RPF drops
                ''',
                'rpf_drops',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('rpf-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                RPF is enabled on interface
                ''',
                'rpf_enabled',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('rpf-supported', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                RPF stats supported per interface
                ''',
                'rpf_supported',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('rpfifh', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                RPF interface handle
                ''',
                'rpfifh',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'interface',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'MplsForwarding.Nodes.Node.LabelFib.LabelSecurity.Interfaces' : {
        'meta_info' : _MetaInfoClass('MplsForwarding.Nodes.Node.LabelFib.LabelSecurity.Interfaces',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'MplsForwarding.Nodes.Node.LabelFib.LabelSecurity.Interfaces.Interface', 
                [], [], 
                '''                Specify interface Name
                ''',
                'interface',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'MplsForwarding.Nodes.Node.LabelFib.LabelSecurity.Summary' : {
        'meta_info' : _MetaInfoClass('MplsForwarding.Nodes.Node.LabelFib.LabelSecurity.Summary',
            False, 
            [
            _MetaInfoClassMember('multi-label-drops', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Multi-label drops
                ''',
                'multi_label_drops',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('rpf-drops', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                RPF drops
                ''',
                'rpf_drops',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'summary',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'MplsForwarding.Nodes.Node.LabelFib.LabelSecurity' : {
        'meta_info' : _MetaInfoClass('MplsForwarding.Nodes.Node.LabelFib.LabelSecurity',
            False, 
            [
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'MplsForwarding.Nodes.Node.LabelFib.LabelSecurity.Interfaces', 
                [], [], 
                '''                MPLS label security interface table
                ''',
                'interfaces',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('summary', REFERENCE_CLASS, 'Summary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'MplsForwarding.Nodes.Node.LabelFib.LabelSecurity.Summary', 
                [], [], 
                '''                MPLS label security summary
                ''',
                'summary',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'label-security',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'MplsForwarding.Nodes.Node.LabelFib' : {
        'meta_info' : _MetaInfoClass('MplsForwarding.Nodes.Node.LabelFib',
            False, 
            [
            _MetaInfoClassMember('forwarding-details', REFERENCE_CLASS, 'ForwardingDetails' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'MplsForwarding.Nodes.Node.LabelFib.ForwardingDetails', 
                [], [], 
                '''                MPLS Forwarding Detail table
                ''',
                'forwarding_details',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('informations', REFERENCE_CLASS, 'Informations' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'MplsForwarding.Nodes.Node.LabelFib.Informations', 
                [], [], 
                '''                Forwarding filtering details
                ''',
                'informations',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('label-security', REFERENCE_CLASS, 'LabelSecurity' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'MplsForwarding.Nodes.Node.LabelFib.LabelSecurity', 
                [], [], 
                '''                MPLS label security
                ''',
                'label_security',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'label-fib',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'MplsForwarding.Nodes.Node.Tunnel.ForwardingTunnels.ForwardingTunnel.TunnelInfo' : {
        'meta_info' : _MetaInfoClass('MplsForwarding.Nodes.Node.Tunnel.ForwardingTunnels.ForwardingTunnel.TunnelInfo',
            False, 
            [
            _MetaInfoClassMember('tli-flags', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Tunnel LI flags
                ''',
                'tli_flags',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('tli-flags-extended', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Tunnel LI extended flags
                ''',
                'tli_flags_extended',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('tli-pointer', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The pointer to the Tun LI object
                ''',
                'tli_pointer',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('tli-reference-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The Tunnel LI object refcounter
                ''',
                'tli_reference_count',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('tli-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Th tunnel LI type
                ''',
                'tli_type',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('tunnel-fwd-class', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Tunnel Forward Class
                ''',
                'tunnel_fwd_class',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('tunnel-interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Tunnel interface
                ''',
                'tunnel_interface_name',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('tunnel-is-programmed-to-drop', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is Tunnel programmed as drop
                ''',
                'tunnel_is_programmed_to_drop',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('tunnel-is-srte', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is Tunnel SRTE
                ''',
                'tunnel_is_srte',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('tunnel-load-metric', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                 Tunnel Load Metric
                ''',
                'tunnel_load_metric',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('tunnel-local-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Tunnel Local label
                ''',
                'tunnel_local_label',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('tunnel-resolution-incomplete', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Tunnel head resolution is incomplete
                ''',
                'tunnel_resolution_incomplete',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('tunnel-resolution-inconsistent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Tunnel head resolition is inconsitent b/w TEhead
                and Local label
                ''',
                'tunnel_resolution_inconsistent',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'tunnel-info',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'MplsForwarding.Nodes.Node.Tunnel.ForwardingTunnels.ForwardingTunnel.Fwdg.LdiInformation' : {
        'meta_info' : _MetaInfoClass('MplsForwarding.Nodes.Node.Tunnel.ForwardingTunnels.ForwardingTunnel.Fwdg.LdiInformation',
            False, 
            [
            _MetaInfoClassMember('ldi-hardware-information', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Hardware info
                ''',
                'ldi_hardware_information',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'ldi-information',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'MplsForwarding.Nodes.Node.Tunnel.ForwardingTunnels.ForwardingTunnel.Fwdg.MulticastInformation' : {
        'meta_info' : _MetaInfoClass('MplsForwarding.Nodes.Node.Tunnel.ForwardingTunnels.ForwardingTunnel.Fwdg.MulticastInformation',
            False, 
            [
            _MetaInfoClassMember('multicast-encap-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The multicast ENCAP-ID 
                ''',
                'multicast_encap_id',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('multicast-mol-base-flags', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                MOL base flags
                ''',
                'multicast_mol_base_flags',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('multicast-mol-flags', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                MOL flags
                ''',
                'multicast_mol_flags',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('multicast-mol-referance-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                MOL refcount
                ''',
                'multicast_mol_referance_count',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('multicast-mpls-local-output-paths', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                num multicast mpls local output paths
                ''',
                'multicast_mpls_local_output_paths',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('multicast-mpls-output-paths', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                num multicast mpls output paths 
                ''',
                'multicast_mpls_output_paths',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('multicast-mpls-protocol-output-paths', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                num multicast mpls prot output paths 
                ''',
                'multicast_mpls_protocol_output_paths',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('multicast-platform-data', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                The multicast platform data
                ''',
                'multicast_platform_data',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('multicast-platform-data-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The multicast platform data len
                ''',
                'multicast_platform_data_length',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('multicast-rpf-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The multicast RPF-ID 
                ''',
                'multicast_rpf_id',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('multicast-tunnel-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                multicast mpls P2MP-TE tunnel id or MLDP Tunnel
                LSMID on all nodes
                ''',
                'multicast_tunnel_id',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('multicast-tunnel-interface-handler', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                multicast mpls tunnel
                ''',
                'multicast_tunnel_interface_handler',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('multicast-tunnel-lspvif', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                multicast LSPVIF for MLDP Tunnels
                ''',
                'multicast_tunnel_lspvif',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('multicast-tunnel-next-hop-information', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                multicast nhinfo for p2mp TE Head
                ''',
                'multicast_tunnel_next_hop_information',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'multicast-information',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'MplsForwarding.Nodes.Node.Tunnel.ForwardingTunnels.ForwardingTunnel.Fwdg.LabelInformation.LabelInformationDetail' : {
        'meta_info' : _MetaInfoClass('MplsForwarding.Nodes.Node.Tunnel.ForwardingTunnels.ForwardingTunnel.Fwdg.LabelInformation.LabelInformationDetail',
            False, 
            [
            _MetaInfoClassMember('l3-mtu', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                L3 MTU
                ''',
                'l3_mtu',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('label-stack', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Label stack
                ''',
                'label_stack',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('mac-size', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Length of L2 encapsulation
                ''',
                'mac_size',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('next-hop-interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Next hop interface
                ''',
                'next_hop_interface',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('next-hop-protocol', REFERENCE_ENUM_CLASS, 'ProtoEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'ProtoEnum', 
                [], [], 
                '''                The address family (V4/V6) 
                ''',
                'next_hop_protocol',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('next-hop-string', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Next hop address in string format
                ''',
                'next_hop_string',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('status', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Status
                ''',
                'status',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('total-encapsulation-size', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total encapsulation size: L2 + MPLS
                ''',
                'total_encapsulation_size',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('transmit-number-of-bytes-switched', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of Bytes switched
                ''',
                'transmit_number_of_bytes_switched',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('transmit-number-of-packets-switched', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of packets switched
                ''',
                'transmit_number_of_packets_switched',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'label-information-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'MplsForwarding.Nodes.Node.Tunnel.ForwardingTunnels.ForwardingTunnel.Fwdg.LabelInformation' : {
        'meta_info' : _MetaInfoClass('MplsForwarding.Nodes.Node.Tunnel.ForwardingTunnels.ForwardingTunnel.Fwdg.LabelInformation',
            False, 
            [
            _MetaInfoClassMember('label-information-detail', REFERENCE_CLASS, 'LabelInformationDetail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'MplsForwarding.Nodes.Node.Tunnel.ForwardingTunnels.ForwardingTunnel.Fwdg.LabelInformation.LabelInformationDetail', 
                [], [], 
                '''                Detail label info
                ''',
                'label_information_detail',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('label-information-next-hop-protocol', REFERENCE_ENUM_CLASS, 'ProtoEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'ProtoEnum', 
                [], [], 
                '''                The address family (v4/v6) 
                ''',
                'label_information_next_hop_protocol',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('label-information-next-hop-string', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Next hop address in string format
                ''',
                'label_information_next_hop_string',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('label-information-next-hop-type', REFERENCE_ENUM_CLASS, 'NextHopEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'NextHopEnum', 
                [], [], 
                '''                NHinfo Type
                ''',
                'label_information_next_hop_type',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('label-information-path-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LabelInformationPathIndex
                ''',
                'label_information_path_index',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('label-information-route-version', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The version of the route
                ''',
                'label_information_route_version',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('label-information-time-in-milli-seconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The time of last update in msec
                ''',
                'label_information_time_in_milli_seconds',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('label-information-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Label-Info type
                ''',
                'label_information_type',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('local-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Local label
                ''',
                'local_label',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('mpls-adjacency-flags', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                MPLS Adjacency flags
                ''',
                'mpls_adjacency_flags',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('outgoing-interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Outgoing interface
                ''',
                'outgoing_interface',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('outgoing-interface-string', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Output Interface in string format
                ''',
                'outgoing_interface_string',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('outgoing-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Outgoing label
                ''',
                'outgoing_label',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('outgoing-label-string', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Output Label in string format
                ''',
                'outgoing_label_string',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('outgoing-physical-interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Outgoing Physical Interface
                ''',
                'outgoing_physical_interface',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('prefix-or-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Prefix Or ID
                ''',
                'prefix_or_id',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('tunnel-id-present', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Tunnel id present?
                ''',
                'tunnel_id_present',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('tunnel-interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Tunnel Interface
                ''',
                'tunnel_interface',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('tx-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Bytes transmitted per LSP
                ''',
                'tx_bytes',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('tx-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Packets transmitted per LSP
                ''',
                'tx_packets',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'label-information',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'MplsForwarding.Nodes.Node.Tunnel.ForwardingTunnels.ForwardingTunnel.Fwdg' : {
        'meta_info' : _MetaInfoClass('MplsForwarding.Nodes.Node.Tunnel.ForwardingTunnels.ForwardingTunnel.Fwdg',
            False, 
            [
            _MetaInfoClassMember('afi-table-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The AFI table ID
                ''',
                'afi_table_id',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('eos-bit', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                EOS bit
                ''',
                'eos_bit',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('hardware-information', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Hardware info
                ''',
                'hardware_information',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('label-information', REFERENCE_LIST, 'LabelInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'MplsForwarding.Nodes.Node.Tunnel.ForwardingTunnels.ForwardingTunnel.Fwdg.LabelInformation', 
                [], [], 
                '''                Label-infos in FIB leaf
                ''',
                'label_information',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('ldi-flags', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The LDI flags
                ''',
                'ldi_flags',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('ldi-information', REFERENCE_CLASS, 'LdiInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'MplsForwarding.Nodes.Node.Tunnel.ForwardingTunnels.ForwardingTunnel.Fwdg.LdiInformation', 
                [], [], 
                '''                LDI-info in FIB leaf
                ''',
                'ldi_information',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('ldi-pointer', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The pointer to the LDI
                ''',
                'ldi_pointer',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('ldi-referance-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of references to the LDI
                ''',
                'ldi_referance_count',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('ldi-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The LDI type
                ''',
                'ldi_type',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('leaf-flags', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The leaf flags
                ''',
                'leaf_flags',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('leaf-local-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Local label
                ''',
                'leaf_local_label',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('leaf-referance-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of references to the leaf
                ''',
                'leaf_referance_count',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('leaf-time-in-milli-seconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The time of last update in msec
                ''',
                'leaf_time_in_milli_seconds',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('lspa-flags', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The LSPA flags
                ''',
                'lspa_flags',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('lw-ldi-pointer', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The pointer to the LW-LDI
                ''',
                'lw_ldi_pointer',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('lw-ldi-refernace-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The LW-LDI refcounter
                ''',
                'lw_ldi_refernace_count',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('lw-ldi-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The LW-LDI type
                ''',
                'lw_ldi_type',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('lw-shared-ldi-pointer', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The pointer to the shared LDI in LW-LDI
                ''',
                'lw_shared_ldi_pointer',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('multicast-information', REFERENCE_CLASS, 'MulticastInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'MplsForwarding.Nodes.Node.Tunnel.ForwardingTunnels.ForwardingTunnel.Fwdg.MulticastInformation', 
                [], [], 
                '''                The multicast info
                ''',
                'multicast_information',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('multicast-label', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                The unicast or multicast label
                ''',
                'multicast_label',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('path-list-flags', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The pathlist flags
                ''',
                'path_list_flags',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('path-list-referance-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of references to the pathlist
                ''',
                'path_list_referance_count',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'fwdg',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'MplsForwarding.Nodes.Node.Tunnel.ForwardingTunnels.ForwardingTunnel' : {
        'meta_info' : _MetaInfoClass('MplsForwarding.Nodes.Node.Tunnel.ForwardingTunnels.ForwardingTunnel',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-fib-common-oper', True),
            _MetaInfoClassMember('fwdg', REFERENCE_CLASS, 'Fwdg' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'MplsForwarding.Nodes.Node.Tunnel.ForwardingTunnels.ForwardingTunnel.Fwdg', 
                [], [], 
                '''                Tunnel forwarding information
                ''',
                'fwdg',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('tunnel-info', REFERENCE_CLASS, 'TunnelInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'MplsForwarding.Nodes.Node.Tunnel.ForwardingTunnels.ForwardingTunnel.TunnelInfo', 
                [], [], 
                '''                Tunnel head information
                ''',
                'tunnel_info',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'forwarding-tunnel',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'MplsForwarding.Nodes.Node.Tunnel.ForwardingTunnels' : {
        'meta_info' : _MetaInfoClass('MplsForwarding.Nodes.Node.Tunnel.ForwardingTunnels',
            False, 
            [
            _MetaInfoClassMember('forwarding-tunnel', REFERENCE_LIST, 'ForwardingTunnel' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'MplsForwarding.Nodes.Node.Tunnel.ForwardingTunnels.ForwardingTunnel', 
                [], [], 
                '''                Forwarding information for the TE tunnel
                ''',
                'forwarding_tunnel',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'forwarding-tunnels',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'MplsForwarding.Nodes.Node.Tunnel' : {
        'meta_info' : _MetaInfoClass('MplsForwarding.Nodes.Node.Tunnel',
            False, 
            [
            _MetaInfoClassMember('forwarding-tunnels', REFERENCE_CLASS, 'ForwardingTunnels' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'MplsForwarding.Nodes.Node.Tunnel.ForwardingTunnels', 
                [], [], 
                '''                Forwarding details for TE tunnels
                ''',
                'forwarding_tunnels',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'tunnel',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'MplsForwarding.Nodes.Node.FrrDatabase.FrrdbSummary' : {
        'meta_info' : _MetaInfoClass('MplsForwarding.Nodes.Node.FrrDatabase.FrrdbSummary',
            False, 
            [
            _MetaInfoClassMember('active', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of FRR rewrites in Active state
                ''',
                'active',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('other', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of FRR rewrites in an unrecognized state
                ''',
                'other',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('partial', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of FRR rewrites in Partial state
                ''',
                'partial',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('ready', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of FRR rewrites in Ready state
                ''',
                'ready',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'frrdb-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'MplsForwarding.Nodes.Node.FrrDatabase.FrrdbProtectedInterfaceTableSummaries.FrrdbProtectedInterfaceTableSummary' : {
        'meta_info' : _MetaInfoClass('MplsForwarding.Nodes.Node.FrrDatabase.FrrdbProtectedInterfaceTableSummaries.FrrdbProtectedInterfaceTableSummary',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-fib-common-oper', True),
            _MetaInfoClassMember('active', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of FRR rewrites in Active state
                ''',
                'active',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('other', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of FRR rewrites in an unrecognized state
                ''',
                'other',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('partial', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of FRR rewrites in Partial state
                ''',
                'partial',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('ready', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of FRR rewrites in Ready state
                ''',
                'ready',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'frrdb-protected-interface-table-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'MplsForwarding.Nodes.Node.FrrDatabase.FrrdbProtectedInterfaceTableSummaries' : {
        'meta_info' : _MetaInfoClass('MplsForwarding.Nodes.Node.FrrDatabase.FrrdbProtectedInterfaceTableSummaries',
            False, 
            [
            _MetaInfoClassMember('frrdb-protected-interface-table-summary', REFERENCE_LIST, 'FrrdbProtectedInterfaceTableSummary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'MplsForwarding.Nodes.Node.FrrDatabase.FrrdbProtectedInterfaceTableSummaries.FrrdbProtectedInterfaceTableSummary', 
                [], [], 
                '''                MPLS forwarding FRR Database Protected
                Interface Summary
                ''',
                'frrdb_protected_interface_table_summary',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'frrdb-protected-interface-table-summaries',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'MplsForwarding.Nodes.Node.FrrDatabase.FrrdbTunnelMidpointSummary' : {
        'meta_info' : _MetaInfoClass('MplsForwarding.Nodes.Node.FrrDatabase.FrrdbTunnelMidpointSummary',
            False, 
            [
            _MetaInfoClassMember('active', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of FRR rewrites in Active state
                ''',
                'active',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('other', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of FRR rewrites in an unrecognized state
                ''',
                'other',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('partial', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of FRR rewrites in Partial state
                ''',
                'partial',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('ready', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of FRR rewrites in Ready state
                ''',
                'ready',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'frrdb-tunnel-midpoint-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'MplsForwarding.Nodes.Node.FrrDatabase.FrrdbTunnelMidpoints.FrrdbTunnelMidpoint.FrrDb.FrrEntryId.Head' : {
        'meta_info' : _MetaInfoClass('MplsForwarding.Nodes.Node.FrrDatabase.FrrdbTunnelMidpoints.FrrdbTunnelMidpoint.FrrDb.FrrEntryId.Head',
            False, 
            [
            _MetaInfoClassMember('destination-prefix', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Destination prefix
                ''',
                'destination_prefix',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('destination-prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Destination prefix length
                ''',
                'destination_prefix_length',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'head',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'MplsForwarding.Nodes.Node.FrrDatabase.FrrdbTunnelMidpoints.FrrdbTunnelMidpoint.FrrDb.FrrEntryId.Midpoint' : {
        'meta_info' : _MetaInfoClass('MplsForwarding.Nodes.Node.FrrDatabase.FrrdbTunnelMidpoints.FrrdbTunnelMidpoint.FrrDb.FrrEntryId.Midpoint',
            False, 
            [
            _MetaInfoClassMember('lspid', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LSP ID
                ''',
                'lspid',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Source IPv4 address
                ''',
                'source_address',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('tunnel-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Tunnel ID
                ''',
                'tunnel_id',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'midpoint',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'MplsForwarding.Nodes.Node.FrrDatabase.FrrdbTunnelMidpoints.FrrdbTunnelMidpoint.FrrDb.FrrEntryId' : {
        'meta_info' : _MetaInfoClass('MplsForwarding.Nodes.Node.FrrDatabase.FrrdbTunnelMidpoints.FrrdbTunnelMidpoint.FrrDb.FrrEntryId',
            False, 
            [
            _MetaInfoClassMember('head', REFERENCE_CLASS, 'Head' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'MplsForwarding.Nodes.Node.FrrDatabase.FrrdbTunnelMidpoints.FrrdbTunnelMidpoint.FrrDb.FrrEntryId.Head', 
                [], [], 
                '''                head
                ''',
                'head',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('midpoint', REFERENCE_CLASS, 'Midpoint' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'MplsForwarding.Nodes.Node.FrrDatabase.FrrdbTunnelMidpoints.FrrdbTunnelMidpoint.FrrDb.FrrEntryId.Midpoint', 
                [], [], 
                '''                midpoint
                ''',
                'midpoint',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('role', REFERENCE_ENUM_CLASS, 'MgmtFibMplsLspRoleEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'MgmtFibMplsLspRoleEnum', 
                [], [], 
                '''                Role
                ''',
                'role',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'frr-entry-id',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'MplsForwarding.Nodes.Node.FrrDatabase.FrrdbTunnelMidpoints.FrrdbTunnelMidpoint.FrrDb.MulticastLeg.FrrEntryId.Head' : {
        'meta_info' : _MetaInfoClass('MplsForwarding.Nodes.Node.FrrDatabase.FrrdbTunnelMidpoints.FrrdbTunnelMidpoint.FrrDb.MulticastLeg.FrrEntryId.Head',
            False, 
            [
            _MetaInfoClassMember('destination-prefix', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Destination prefix
                ''',
                'destination_prefix',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('destination-prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Destination prefix length
                ''',
                'destination_prefix_length',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'head',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'MplsForwarding.Nodes.Node.FrrDatabase.FrrdbTunnelMidpoints.FrrdbTunnelMidpoint.FrrDb.MulticastLeg.FrrEntryId.Midpoint' : {
        'meta_info' : _MetaInfoClass('MplsForwarding.Nodes.Node.FrrDatabase.FrrdbTunnelMidpoints.FrrdbTunnelMidpoint.FrrDb.MulticastLeg.FrrEntryId.Midpoint',
            False, 
            [
            _MetaInfoClassMember('lspid', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LSP ID
                ''',
                'lspid',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Source IPv4 address
                ''',
                'source_address',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('tunnel-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Tunnel ID
                ''',
                'tunnel_id',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'midpoint',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'MplsForwarding.Nodes.Node.FrrDatabase.FrrdbTunnelMidpoints.FrrdbTunnelMidpoint.FrrDb.MulticastLeg.FrrEntryId' : {
        'meta_info' : _MetaInfoClass('MplsForwarding.Nodes.Node.FrrDatabase.FrrdbTunnelMidpoints.FrrdbTunnelMidpoint.FrrDb.MulticastLeg.FrrEntryId',
            False, 
            [
            _MetaInfoClassMember('head', REFERENCE_CLASS, 'Head' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'MplsForwarding.Nodes.Node.FrrDatabase.FrrdbTunnelMidpoints.FrrdbTunnelMidpoint.FrrDb.MulticastLeg.FrrEntryId.Head', 
                [], [], 
                '''                head
                ''',
                'head',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('midpoint', REFERENCE_CLASS, 'Midpoint' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'MplsForwarding.Nodes.Node.FrrDatabase.FrrdbTunnelMidpoints.FrrdbTunnelMidpoint.FrrDb.MulticastLeg.FrrEntryId.Midpoint', 
                [], [], 
                '''                midpoint
                ''',
                'midpoint',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('role', REFERENCE_ENUM_CLASS, 'MgmtFibMplsLspRoleEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'MgmtFibMplsLspRoleEnum', 
                [], [], 
                '''                Role
                ''',
                'role',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'frr-entry-id',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'MplsForwarding.Nodes.Node.FrrDatabase.FrrdbTunnelMidpoints.FrrdbTunnelMidpoint.FrrDb.MulticastLeg' : {
        'meta_info' : _MetaInfoClass('MplsForwarding.Nodes.Node.FrrDatabase.FrrdbTunnelMidpoints.FrrdbTunnelMidpoint.FrrDb.MulticastLeg',
            False, 
            [
            _MetaInfoClassMember('entry-frr-state', REFERENCE_ENUM_CLASS, 'MgmtFibMplsFrrStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'MgmtFibMplsFrrStateEnum', 
                [], [], 
                '''                MPLS FRR entry state
                ''',
                'entry_frr_state',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('frr-entry-id', REFERENCE_CLASS, 'FrrEntryId' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'MplsForwarding.Nodes.Node.FrrDatabase.FrrdbTunnelMidpoints.FrrdbTunnelMidpoint.FrrDb.MulticastLeg.FrrEntryId', 
                [], [], 
                '''                FRR entry ID
                ''',
                'frr_entry_id',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('frr-interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                FRR interface
                ''',
                'frr_interface_name',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('frr-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                FRR output label
                ''',
                'frr_label',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('frr-next-hop-ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Next hop IPv4 address
                ''',
                'frr_next_hop_ipv4_address',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('input-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Input label
                ''',
                'input_label',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('is-mldp-lsp', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                MLDP or P2MP-TE
                ''',
                'is_mldp_lsp',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('outgoing-interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Outgoing interface
                ''',
                'outgoing_interface',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('outgoing-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Outgoing label
                ''',
                'outgoing_label',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('tunnel-interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Tunnel interface
                ''',
                'tunnel_interface_name',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'multicast-leg',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'MplsForwarding.Nodes.Node.FrrDatabase.FrrdbTunnelMidpoints.FrrdbTunnelMidpoint.FrrDb' : {
        'meta_info' : _MetaInfoClass('MplsForwarding.Nodes.Node.FrrDatabase.FrrdbTunnelMidpoints.FrrdbTunnelMidpoint.FrrDb',
            False, 
            [
            _MetaInfoClassMember('entry-frr-state', REFERENCE_ENUM_CLASS, 'MgmtFibMplsFrrStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'MgmtFibMplsFrrStateEnum', 
                [], [], 
                '''                MPLS FRR entry state
                ''',
                'entry_frr_state',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('frr-entry-id', REFERENCE_CLASS, 'FrrEntryId' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'MplsForwarding.Nodes.Node.FrrDatabase.FrrdbTunnelMidpoints.FrrdbTunnelMidpoint.FrrDb.FrrEntryId', 
                [], [], 
                '''                FRR entry ID
                ''',
                'frr_entry_id',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('frr-interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                FRR interface
                ''',
                'frr_interface_name',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('frr-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                FRR output label
                ''',
                'frr_label',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('frr-next-hop-ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Next hop IPv4 address
                ''',
                'frr_next_hop_ipv4_address',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('input-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Input label
                ''',
                'input_label',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('is-mldp-lsp', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                MLDP or P2MP-TE
                ''',
                'is_mldp_lsp',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('is-multicast-tunnel', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Multicast tunnel
                ''',
                'is_multicast_tunnel',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('multicast-leg', REFERENCE_LIST, 'MulticastLeg' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'MplsForwarding.Nodes.Node.FrrDatabase.FrrdbTunnelMidpoints.FrrdbTunnelMidpoint.FrrDb.MulticastLeg', 
                [], [], 
                '''                MCAST legs
                ''',
                'multicast_leg',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('multicast-tunnel-legs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of legs in MCAST tunnel
                ''',
                'multicast_tunnel_legs',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('outgoing-interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Outgoing interface
                ''',
                'outgoing_interface',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('outgoing-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Outgoing label
                ''',
                'outgoing_label',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('tunnel-interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Tunnel interface
                ''',
                'tunnel_interface_name',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'frr-db',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'MplsForwarding.Nodes.Node.FrrDatabase.FrrdbTunnelMidpoints.FrrdbTunnelMidpoint' : {
        'meta_info' : _MetaInfoClass('MplsForwarding.Nodes.Node.FrrDatabase.FrrdbTunnelMidpoints.FrrdbTunnelMidpoint',
            False, 
            [
            _MetaInfoClassMember('local-label', ATTRIBUTE, 'int' , None, None, 
                [('16', '1048575')], [], 
                '''                Local label value
                ''',
                'local_label',
                'Cisco-IOS-XR-fib-common-oper', True),
            _MetaInfoClassMember('frr-db', REFERENCE_CLASS, 'FrrDb' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'MplsForwarding.Nodes.Node.FrrDatabase.FrrdbTunnelMidpoints.FrrdbTunnelMidpoint.FrrDb', 
                [], [], 
                '''                FRR DB
                ''',
                'frr_db',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('frr-lable-string', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                FRR label in string format
                ''',
                'frr_lable_string',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('outgoing-lable-string', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Output label in string format
                ''',
                'outgoing_lable_string',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'frrdb-tunnel-midpoint',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'MplsForwarding.Nodes.Node.FrrDatabase.FrrdbTunnelMidpoints' : {
        'meta_info' : _MetaInfoClass('MplsForwarding.Nodes.Node.FrrDatabase.FrrdbTunnelMidpoints',
            False, 
            [
            _MetaInfoClassMember('frrdb-tunnel-midpoint', REFERENCE_LIST, 'FrrdbTunnelMidpoint' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'MplsForwarding.Nodes.Node.FrrDatabase.FrrdbTunnelMidpoints.FrrdbTunnelMidpoint', 
                [], [], 
                '''                MPLS forwarding FRR Database Tunnel Midpoint
                Entry
                ''',
                'frrdb_tunnel_midpoint',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'frrdb-tunnel-midpoints',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'MplsForwarding.Nodes.Node.FrrDatabase.FrrdbTunnelHeads.FrrdbTunnelHead.FrrDb.FrrEntryId.Head' : {
        'meta_info' : _MetaInfoClass('MplsForwarding.Nodes.Node.FrrDatabase.FrrdbTunnelHeads.FrrdbTunnelHead.FrrDb.FrrEntryId.Head',
            False, 
            [
            _MetaInfoClassMember('destination-prefix', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Destination prefix
                ''',
                'destination_prefix',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('destination-prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Destination prefix length
                ''',
                'destination_prefix_length',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'head',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'MplsForwarding.Nodes.Node.FrrDatabase.FrrdbTunnelHeads.FrrdbTunnelHead.FrrDb.FrrEntryId.Midpoint' : {
        'meta_info' : _MetaInfoClass('MplsForwarding.Nodes.Node.FrrDatabase.FrrdbTunnelHeads.FrrdbTunnelHead.FrrDb.FrrEntryId.Midpoint',
            False, 
            [
            _MetaInfoClassMember('lspid', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LSP ID
                ''',
                'lspid',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Source IPv4 address
                ''',
                'source_address',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('tunnel-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Tunnel ID
                ''',
                'tunnel_id',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'midpoint',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'MplsForwarding.Nodes.Node.FrrDatabase.FrrdbTunnelHeads.FrrdbTunnelHead.FrrDb.FrrEntryId' : {
        'meta_info' : _MetaInfoClass('MplsForwarding.Nodes.Node.FrrDatabase.FrrdbTunnelHeads.FrrdbTunnelHead.FrrDb.FrrEntryId',
            False, 
            [
            _MetaInfoClassMember('head', REFERENCE_CLASS, 'Head' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'MplsForwarding.Nodes.Node.FrrDatabase.FrrdbTunnelHeads.FrrdbTunnelHead.FrrDb.FrrEntryId.Head', 
                [], [], 
                '''                head
                ''',
                'head',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('midpoint', REFERENCE_CLASS, 'Midpoint' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'MplsForwarding.Nodes.Node.FrrDatabase.FrrdbTunnelHeads.FrrdbTunnelHead.FrrDb.FrrEntryId.Midpoint', 
                [], [], 
                '''                midpoint
                ''',
                'midpoint',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('role', REFERENCE_ENUM_CLASS, 'MgmtFibMplsLspRoleEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'MgmtFibMplsLspRoleEnum', 
                [], [], 
                '''                Role
                ''',
                'role',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'frr-entry-id',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'MplsForwarding.Nodes.Node.FrrDatabase.FrrdbTunnelHeads.FrrdbTunnelHead.FrrDb.MulticastLeg.FrrEntryId.Head' : {
        'meta_info' : _MetaInfoClass('MplsForwarding.Nodes.Node.FrrDatabase.FrrdbTunnelHeads.FrrdbTunnelHead.FrrDb.MulticastLeg.FrrEntryId.Head',
            False, 
            [
            _MetaInfoClassMember('destination-prefix', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Destination prefix
                ''',
                'destination_prefix',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('destination-prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Destination prefix length
                ''',
                'destination_prefix_length',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'head',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'MplsForwarding.Nodes.Node.FrrDatabase.FrrdbTunnelHeads.FrrdbTunnelHead.FrrDb.MulticastLeg.FrrEntryId.Midpoint' : {
        'meta_info' : _MetaInfoClass('MplsForwarding.Nodes.Node.FrrDatabase.FrrdbTunnelHeads.FrrdbTunnelHead.FrrDb.MulticastLeg.FrrEntryId.Midpoint',
            False, 
            [
            _MetaInfoClassMember('lspid', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LSP ID
                ''',
                'lspid',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Source IPv4 address
                ''',
                'source_address',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('tunnel-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Tunnel ID
                ''',
                'tunnel_id',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'midpoint',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'MplsForwarding.Nodes.Node.FrrDatabase.FrrdbTunnelHeads.FrrdbTunnelHead.FrrDb.MulticastLeg.FrrEntryId' : {
        'meta_info' : _MetaInfoClass('MplsForwarding.Nodes.Node.FrrDatabase.FrrdbTunnelHeads.FrrdbTunnelHead.FrrDb.MulticastLeg.FrrEntryId',
            False, 
            [
            _MetaInfoClassMember('head', REFERENCE_CLASS, 'Head' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'MplsForwarding.Nodes.Node.FrrDatabase.FrrdbTunnelHeads.FrrdbTunnelHead.FrrDb.MulticastLeg.FrrEntryId.Head', 
                [], [], 
                '''                head
                ''',
                'head',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('midpoint', REFERENCE_CLASS, 'Midpoint' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'MplsForwarding.Nodes.Node.FrrDatabase.FrrdbTunnelHeads.FrrdbTunnelHead.FrrDb.MulticastLeg.FrrEntryId.Midpoint', 
                [], [], 
                '''                midpoint
                ''',
                'midpoint',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('role', REFERENCE_ENUM_CLASS, 'MgmtFibMplsLspRoleEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'MgmtFibMplsLspRoleEnum', 
                [], [], 
                '''                Role
                ''',
                'role',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'frr-entry-id',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'MplsForwarding.Nodes.Node.FrrDatabase.FrrdbTunnelHeads.FrrdbTunnelHead.FrrDb.MulticastLeg' : {
        'meta_info' : _MetaInfoClass('MplsForwarding.Nodes.Node.FrrDatabase.FrrdbTunnelHeads.FrrdbTunnelHead.FrrDb.MulticastLeg',
            False, 
            [
            _MetaInfoClassMember('entry-frr-state', REFERENCE_ENUM_CLASS, 'MgmtFibMplsFrrStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'MgmtFibMplsFrrStateEnum', 
                [], [], 
                '''                MPLS FRR entry state
                ''',
                'entry_frr_state',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('frr-entry-id', REFERENCE_CLASS, 'FrrEntryId' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'MplsForwarding.Nodes.Node.FrrDatabase.FrrdbTunnelHeads.FrrdbTunnelHead.FrrDb.MulticastLeg.FrrEntryId', 
                [], [], 
                '''                FRR entry ID
                ''',
                'frr_entry_id',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('frr-interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                FRR interface
                ''',
                'frr_interface_name',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('frr-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                FRR output label
                ''',
                'frr_label',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('frr-next-hop-ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Next hop IPv4 address
                ''',
                'frr_next_hop_ipv4_address',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('input-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Input label
                ''',
                'input_label',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('is-mldp-lsp', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                MLDP or P2MP-TE
                ''',
                'is_mldp_lsp',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('outgoing-interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Outgoing interface
                ''',
                'outgoing_interface',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('outgoing-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Outgoing label
                ''',
                'outgoing_label',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('tunnel-interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Tunnel interface
                ''',
                'tunnel_interface_name',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'multicast-leg',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'MplsForwarding.Nodes.Node.FrrDatabase.FrrdbTunnelHeads.FrrdbTunnelHead.FrrDb' : {
        'meta_info' : _MetaInfoClass('MplsForwarding.Nodes.Node.FrrDatabase.FrrdbTunnelHeads.FrrdbTunnelHead.FrrDb',
            False, 
            [
            _MetaInfoClassMember('entry-frr-state', REFERENCE_ENUM_CLASS, 'MgmtFibMplsFrrStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'MgmtFibMplsFrrStateEnum', 
                [], [], 
                '''                MPLS FRR entry state
                ''',
                'entry_frr_state',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('frr-entry-id', REFERENCE_CLASS, 'FrrEntryId' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'MplsForwarding.Nodes.Node.FrrDatabase.FrrdbTunnelHeads.FrrdbTunnelHead.FrrDb.FrrEntryId', 
                [], [], 
                '''                FRR entry ID
                ''',
                'frr_entry_id',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('frr-interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                FRR interface
                ''',
                'frr_interface_name',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('frr-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                FRR output label
                ''',
                'frr_label',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('frr-next-hop-ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Next hop IPv4 address
                ''',
                'frr_next_hop_ipv4_address',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('input-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Input label
                ''',
                'input_label',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('is-mldp-lsp', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                MLDP or P2MP-TE
                ''',
                'is_mldp_lsp',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('is-multicast-tunnel', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Multicast tunnel
                ''',
                'is_multicast_tunnel',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('multicast-leg', REFERENCE_LIST, 'MulticastLeg' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'MplsForwarding.Nodes.Node.FrrDatabase.FrrdbTunnelHeads.FrrdbTunnelHead.FrrDb.MulticastLeg', 
                [], [], 
                '''                MCAST legs
                ''',
                'multicast_leg',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('multicast-tunnel-legs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of legs in MCAST tunnel
                ''',
                'multicast_tunnel_legs',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('outgoing-interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Outgoing interface
                ''',
                'outgoing_interface',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('outgoing-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Outgoing label
                ''',
                'outgoing_label',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('tunnel-interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Tunnel interface
                ''',
                'tunnel_interface_name',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'frr-db',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'MplsForwarding.Nodes.Node.FrrDatabase.FrrdbTunnelHeads.FrrdbTunnelHead' : {
        'meta_info' : _MetaInfoClass('MplsForwarding.Nodes.Node.FrrDatabase.FrrdbTunnelHeads.FrrdbTunnelHead',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-fib-common-oper', True),
            _MetaInfoClassMember('frr-db', REFERENCE_CLASS, 'FrrDb' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'MplsForwarding.Nodes.Node.FrrDatabase.FrrdbTunnelHeads.FrrdbTunnelHead.FrrDb', 
                [], [], 
                '''                FRR DB
                ''',
                'frr_db',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('frr-lable-string', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                FRR label in string format
                ''',
                'frr_lable_string',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('outgoing-lable-string', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Output label in string format
                ''',
                'outgoing_lable_string',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'frrdb-tunnel-head',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'MplsForwarding.Nodes.Node.FrrDatabase.FrrdbTunnelHeads' : {
        'meta_info' : _MetaInfoClass('MplsForwarding.Nodes.Node.FrrDatabase.FrrdbTunnelHeads',
            False, 
            [
            _MetaInfoClassMember('frrdb-tunnel-head', REFERENCE_LIST, 'FrrdbTunnelHead' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'MplsForwarding.Nodes.Node.FrrDatabase.FrrdbTunnelHeads.FrrdbTunnelHead', 
                [], [], 
                '''                MPLS forwarding FRR Database Tunnel Head
                Entry
                ''',
                'frrdb_tunnel_head',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'frrdb-tunnel-heads',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'MplsForwarding.Nodes.Node.FrrDatabase.FrrdbTunnelHeadSummary' : {
        'meta_info' : _MetaInfoClass('MplsForwarding.Nodes.Node.FrrDatabase.FrrdbTunnelHeadSummary',
            False, 
            [
            _MetaInfoClassMember('active', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of FRR rewrites in Active state
                ''',
                'active',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('other', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of FRR rewrites in an unrecognized state
                ''',
                'other',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('partial', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of FRR rewrites in Partial state
                ''',
                'partial',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('ready', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of FRR rewrites in Ready state
                ''',
                'ready',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'frrdb-tunnel-head-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'MplsForwarding.Nodes.Node.FrrDatabase.FrrdbBackupInterfaceSummaries.FrrdbBackupInterfaceSummary' : {
        'meta_info' : _MetaInfoClass('MplsForwarding.Nodes.Node.FrrDatabase.FrrdbBackupInterfaceSummaries.FrrdbBackupInterfaceSummary',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-fib-common-oper', True),
            _MetaInfoClassMember('active', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of FRR rewrites in Active state
                ''',
                'active',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('other', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of FRR rewrites in an unrecognized state
                ''',
                'other',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('partial', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of FRR rewrites in Partial state
                ''',
                'partial',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('ready', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of FRR rewrites in Ready state
                ''',
                'ready',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'frrdb-backup-interface-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'MplsForwarding.Nodes.Node.FrrDatabase.FrrdbBackupInterfaceSummaries' : {
        'meta_info' : _MetaInfoClass('MplsForwarding.Nodes.Node.FrrDatabase.FrrdbBackupInterfaceSummaries',
            False, 
            [
            _MetaInfoClassMember('frrdb-backup-interface-summary', REFERENCE_LIST, 'FrrdbBackupInterfaceSummary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'MplsForwarding.Nodes.Node.FrrDatabase.FrrdbBackupInterfaceSummaries.FrrdbBackupInterfaceSummary', 
                [], [], 
                '''                MPLS forwarding FRR Database Backup
                Interface Summary
                ''',
                'frrdb_backup_interface_summary',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'frrdb-backup-interface-summaries',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'MplsForwarding.Nodes.Node.FrrDatabase' : {
        'meta_info' : _MetaInfoClass('MplsForwarding.Nodes.Node.FrrDatabase',
            False, 
            [
            _MetaInfoClassMember('frrdb-backup-interface-summaries', REFERENCE_CLASS, 'FrrdbBackupInterfaceSummaries' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'MplsForwarding.Nodes.Node.FrrDatabase.FrrdbBackupInterfaceSummaries', 
                [], [], 
                '''                MPLS forwarding FRR Database Backup Interface
                Summary Table
                ''',
                'frrdb_backup_interface_summaries',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('frrdb-protected-interface-table-summaries', REFERENCE_CLASS, 'FrrdbProtectedInterfaceTableSummaries' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'MplsForwarding.Nodes.Node.FrrDatabase.FrrdbProtectedInterfaceTableSummaries', 
                [], [], 
                '''                MPLS forwarding FRR Database Protected
                Interface Summary Table
                ''',
                'frrdb_protected_interface_table_summaries',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('frrdb-summary', REFERENCE_CLASS, 'FrrdbSummary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'MplsForwarding.Nodes.Node.FrrDatabase.FrrdbSummary', 
                [], [], 
                '''                MPLS forwarding FRR Database Summary
                ''',
                'frrdb_summary',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('frrdb-tunnel-head-summary', REFERENCE_CLASS, 'FrrdbTunnelHeadSummary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'MplsForwarding.Nodes.Node.FrrDatabase.FrrdbTunnelHeadSummary', 
                [], [], 
                '''                MPLS forwarding FRR Database Tunnel Head
                Summary
                ''',
                'frrdb_tunnel_head_summary',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('frrdb-tunnel-heads', REFERENCE_CLASS, 'FrrdbTunnelHeads' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'MplsForwarding.Nodes.Node.FrrDatabase.FrrdbTunnelHeads', 
                [], [], 
                '''                MPLS forwarding FRR Database Tunnel Head
                Table
                ''',
                'frrdb_tunnel_heads',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('frrdb-tunnel-midpoint-summary', REFERENCE_CLASS, 'FrrdbTunnelMidpointSummary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'MplsForwarding.Nodes.Node.FrrDatabase.FrrdbTunnelMidpointSummary', 
                [], [], 
                '''                MPLS forwarding FRR Database Tunnel Midpoint
                Summary
                ''',
                'frrdb_tunnel_midpoint_summary',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('frrdb-tunnel-midpoints', REFERENCE_CLASS, 'FrrdbTunnelMidpoints' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'MplsForwarding.Nodes.Node.FrrDatabase.FrrdbTunnelMidpoints', 
                [], [], 
                '''                MPLS forwarding FRR Database Tunnel Midpoint
                Table
                ''',
                'frrdb_tunnel_midpoints',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'frr-database',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'MplsForwarding.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('MplsForwarding.Nodes.Node',
            False, 
            [
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Node ID
                ''',
                'node_name',
                'Cisco-IOS-XR-fib-common-oper', True),
            _MetaInfoClassMember('forwarding-summary', REFERENCE_CLASS, 'ForwardingSummary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'MplsForwarding.Nodes.Node.ForwardingSummary', 
                [], [], 
                '''                MPLS forwarding summary
                ''',
                'forwarding_summary',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('frr-database', REFERENCE_CLASS, 'FrrDatabase' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'MplsForwarding.Nodes.Node.FrrDatabase', 
                [], [], 
                '''                MPLS forwarding FRR Database
                ''',
                'frr_database',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('frr-logs', REFERENCE_CLASS, 'FrrLogs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'MplsForwarding.Nodes.Node.FrrLogs', 
                [], [], 
                '''                FRR Log Table
                ''',
                'frr_logs',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('label-fib', REFERENCE_CLASS, 'LabelFib' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'MplsForwarding.Nodes.Node.LabelFib', 
                [], [], 
                '''                Labels For FIB
                ''',
                'label_fib',
                'Cisco-IOS-XR-fib-common-oper', False),
            _MetaInfoClassMember('tunnel', REFERENCE_CLASS, 'Tunnel' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'MplsForwarding.Nodes.Node.Tunnel', 
                [], [], 
                '''                TE Tunnel information
                ''',
                'tunnel',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'node',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'MplsForwarding.Nodes' : {
        'meta_info' : _MetaInfoClass('MplsForwarding.Nodes',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'MplsForwarding.Nodes.Node', 
                [], [], 
                '''                Operational data for a specific Node
                ''',
                'node',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'nodes',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
    'MplsForwarding' : {
        'meta_info' : _MetaInfoClass('MplsForwarding',
            False, 
            [
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper', 'MplsForwarding.Nodes', 
                [], [], 
                '''                Table of Nodes
                ''',
                'nodes',
                'Cisco-IOS-XR-fib-common-oper', False),
            ],
            'Cisco-IOS-XR-fib-common-oper',
            'mpls-forwarding',
            _yang_ns._namespaces['Cisco-IOS-XR-fib-common-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fib_common_oper'
        ),
    },
}
_meta_table['FibStatistics.Nodes.Node.Drops']['meta_info'].parent =_meta_table['FibStatistics.Nodes.Node']['meta_info']
_meta_table['FibStatistics.Nodes.Node']['meta_info'].parent =_meta_table['FibStatistics.Nodes']['meta_info']
_meta_table['FibStatistics.Nodes']['meta_info'].parent =_meta_table['FibStatistics']['meta_info']
_meta_table['Fib.Nodes.Node.Global_.Summary.Total.TotalCounters.ArrayNumberOfRetry']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Global_.Summary.Total.TotalCounters']['meta_info']
_meta_table['Fib.Nodes.Node.Global_.Summary.Total.TotalCounters.ArrayNumberOfObject']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Global_.Summary.Total.TotalCounters']['meta_info']
_meta_table['Fib.Nodes.Node.Global_.Summary.Total.CommonInfo']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Global_.Summary.Total']['meta_info']
_meta_table['Fib.Nodes.Node.Global_.Summary.Total.TotalCounters']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Global_.Summary.Total']['meta_info']
_meta_table['Fib.Nodes.Node.Global_.Summary.Protos.Proto.Summary_.SummaryCounts.ArrayNumberOfRetry']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Global_.Summary.Protos.Proto.Summary_.SummaryCounts']['meta_info']
_meta_table['Fib.Nodes.Node.Global_.Summary.Protos.Proto.Summary_.SummaryCounts.ArrayNumberOfObject']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Global_.Summary.Protos.Proto.Summary_.SummaryCounts']['meta_info']
_meta_table['Fib.Nodes.Node.Global_.Summary.Protos.Proto.Summary_.BaseObject']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Global_.Summary.Protos.Proto.Summary_']['meta_info']
_meta_table['Fib.Nodes.Node.Global_.Summary.Protos.Proto.Summary_.SummaryCounts']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Global_.Summary.Protos.Proto.Summary_']['meta_info']
_meta_table['Fib.Nodes.Node.Global_.Summary.Protos.Proto.Summary_.Health']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Global_.Summary.Protos.Proto.Summary_']['meta_info']
_meta_table['Fib.Nodes.Node.Global_.Summary.Protos.Proto.CommonInfo']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Global_.Summary.Protos.Proto']['meta_info']
_meta_table['Fib.Nodes.Node.Global_.Summary.Protos.Proto.Summary_']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Global_.Summary.Protos.Proto']['meta_info']
_meta_table['Fib.Nodes.Node.Global_.Summary.Protos.Proto']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Global_.Summary.Protos']['meta_info']
_meta_table['Fib.Nodes.Node.Global_.Summary.Total']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Global_.Summary']['meta_info']
_meta_table['Fib.Nodes.Node.Global_.Summary.Protos']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Global_.Summary']['meta_info']
_meta_table['Fib.Nodes.Node.Global_.ObjectHistory.ObjHistoryProtos.ObjHistoryProto.BaseObject']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Global_.ObjectHistory.ObjHistoryProtos.ObjHistoryProto']['meta_info']
_meta_table['Fib.Nodes.Node.Global_.ObjectHistory.ObjHistoryProtos.ObjHistoryProto.ObjectHistory_']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Global_.ObjectHistory.ObjHistoryProtos.ObjHistoryProto']['meta_info']
_meta_table['Fib.Nodes.Node.Global_.ObjectHistory.ObjHistoryProtos.ObjHistoryProto']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Global_.ObjectHistory.ObjHistoryProtos']['meta_info']
_meta_table['Fib.Nodes.Node.Global_.ObjectHistory.ObjHistoryProtos']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Global_.ObjectHistory']['meta_info']
_meta_table['Fib.Nodes.Node.Global_.Summary']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Global_']['meta_info']
_meta_table['Fib.Nodes.Node.Global_.ObjectHistory']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Global_']['meta_info']
_meta_table['Fib.Nodes.Node.Protocols.Protocol.IssuState.FisProtoState']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Protocols.Protocol.IssuState']['meta_info']
_meta_table['Fib.Nodes.Node.Protocols.Protocol.Resource.ResourceDetailInfo.SrShmState']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Protocols.Protocol.Resource.ResourceDetailInfo']['meta_info']
_meta_table['Fib.Nodes.Node.Protocols.Protocol.Resource.ResourceHardwareIngressInfo.SrShmState']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Protocols.Protocol.Resource.ResourceHardwareIngressInfo']['meta_info']
_meta_table['Fib.Nodes.Node.Protocols.Protocol.Resource.ResourceHardwareEgressInfo.SrShmState']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Protocols.Protocol.Resource.ResourceHardwareEgressInfo']['meta_info']
_meta_table['Fib.Nodes.Node.Protocols.Protocol.Resource.ResourceSummaryInfo.SrShmState']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Protocols.Protocol.Resource.ResourceSummaryInfo']['meta_info']
_meta_table['Fib.Nodes.Node.Protocols.Protocol.Resource.ResourceDetailInfo']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Protocols.Protocol.Resource']['meta_info']
_meta_table['Fib.Nodes.Node.Protocols.Protocol.Resource.ResourceHardwareIngressInfo']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Protocols.Protocol.Resource']['meta_info']
_meta_table['Fib.Nodes.Node.Protocols.Protocol.Resource.ResourceHardwareEgressInfo']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Protocols.Protocol.Resource']['meta_info']
_meta_table['Fib.Nodes.Node.Protocols.Protocol.Resource.ResourceSummaryInfo']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Protocols.Protocol.Resource']['meta_info']
_meta_table['Fib.Nodes.Node.Protocols.Protocol.FibSummaries.FibSummary.ExclusiveLoadSharingElement']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Protocols.Protocol.FibSummaries.FibSummary']['meta_info']
_meta_table['Fib.Nodes.Node.Protocols.Protocol.FibSummaries.FibSummary.SharedLoadSharingElement']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Protocols.Protocol.FibSummaries.FibSummary']['meta_info']
_meta_table['Fib.Nodes.Node.Protocols.Protocol.FibSummaries.FibSummary.CrossSharedLoadSharingElement']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Protocols.Protocol.FibSummaries.FibSummary']['meta_info']
_meta_table['Fib.Nodes.Node.Protocols.Protocol.FibSummaries.FibSummary.LabelSharedLoadSharingElement']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Protocols.Protocol.FibSummaries.FibSummary']['meta_info']
_meta_table['Fib.Nodes.Node.Protocols.Protocol.FibSummaries.FibSummary']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Protocols.Protocol.FibSummaries']['meta_info']
_meta_table['Fib.Nodes.Node.Protocols.Protocol.ExternalSummaryAll.SesaPlSum']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Protocols.Protocol.ExternalSummaryAll']['meta_info']
_meta_table['Fib.Nodes.Node.Protocols.Protocol.FrrLog.FrrInterfaces.FrrInterface.Logs.Log.FrrTimestamp']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Protocols.Protocol.FrrLog.FrrInterfaces.FrrInterface.Logs.Log']['meta_info']
_meta_table['Fib.Nodes.Node.Protocols.Protocol.FrrLog.FrrInterfaces.FrrInterface.Logs.Log']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Protocols.Protocol.FrrLog.FrrInterfaces.FrrInterface.Logs']['meta_info']
_meta_table['Fib.Nodes.Node.Protocols.Protocol.FrrLog.FrrInterfaces.FrrInterface.Logs']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Protocols.Protocol.FrrLog.FrrInterfaces.FrrInterface']['meta_info']
_meta_table['Fib.Nodes.Node.Protocols.Protocol.FrrLog.FrrInterfaces.FrrInterface']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Protocols.Protocol.FrrLog.FrrInterfaces']['meta_info']
_meta_table['Fib.Nodes.Node.Protocols.Protocol.FrrLog.FrrInterfaces']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Protocols.Protocol.FrrLog']['meta_info']
_meta_table['Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixDetails.IpPrefixDetail.DetailFibEntryInformation.LoadshareInformation.LoadInformtionInternalData.AdjacencyAddress']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixDetails.IpPrefixDetail.DetailFibEntryInformation.LoadshareInformation.LoadInformtionInternalData']['meta_info']
_meta_table['Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixDetails.IpPrefixDetail.DetailFibEntryInformation.LoadshareInformation.LoadInformtionInternalData.PbtsClassIsFallbackMapped']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixDetails.IpPrefixDetail.DetailFibEntryInformation.LoadshareInformation.LoadInformtionInternalData']['meta_info']
_meta_table['Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixDetails.IpPrefixDetail.DetailFibEntryInformation.LoadshareInformation.LoadInformtionInternalData.PbtsFallbackToDrop']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixDetails.IpPrefixDetail.DetailFibEntryInformation.LoadshareInformation.LoadInformtionInternalData']['meta_info']
_meta_table['Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixDetails.IpPrefixDetail.DetailFibEntryInformation.LoadshareInformation.LoadInformtionInternalData.TunnelIsForwardClass']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixDetails.IpPrefixDetail.DetailFibEntryInformation.LoadshareInformation.LoadInformtionInternalData']['meta_info']
_meta_table['Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixDetails.IpPrefixDetail.DetailFibEntryInformation.LoadshareInformation.LoadInformtionInternalData']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixDetails.IpPrefixDetail.DetailFibEntryInformation.LoadshareInformation']['meta_info']
_meta_table['Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixDetails.IpPrefixDetail.DetailFibEntryInformation.LoadshareInformation']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixDetails.IpPrefixDetail.DetailFibEntryInformation']['meta_info']
_meta_table['Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixDetails.IpPrefixDetail.FibEntryPath.FibShTblPath.MoreDetailAboutPath.SpdIpencap.IpEncapHdr']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixDetails.IpPrefixDetail.FibEntryPath.FibShTblPath.MoreDetailAboutPath.SpdIpencap']['meta_info']
_meta_table['Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixDetails.IpPrefixDetail.FibEntryPath.FibShTblPath.MoreDetailAboutPath.SpdIpencap']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixDetails.IpPrefixDetail.FibEntryPath.FibShTblPath.MoreDetailAboutPath']['meta_info']
_meta_table['Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixDetails.IpPrefixDetail.FibEntryPath.FibShTblPath.MplsInformationForPath.IgpLabelStackArray']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixDetails.IpPrefixDetail.FibEntryPath.FibShTblPath.MplsInformationForPath']['meta_info']
_meta_table['Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixDetails.IpPrefixDetail.FibEntryPath.FibShTblPath.MoreDetailAboutPath']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixDetails.IpPrefixDetail.FibEntryPath.FibShTblPath']['meta_info']
_meta_table['Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixDetails.IpPrefixDetail.FibEntryPath.FibShTblPath.MplsInformationForPath']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixDetails.IpPrefixDetail.FibEntryPath.FibShTblPath']['meta_info']
_meta_table['Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixDetails.IpPrefixDetail.FibEntryPath.FibShTblPath']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixDetails.IpPrefixDetail.FibEntryPath']['meta_info']
_meta_table['Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixDetails.IpPrefixDetail.Srv6Information.Srv6Statistics']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixDetails.IpPrefixDetail.Srv6Information']['meta_info']
_meta_table['Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixDetails.IpPrefixDetail.ExtensionObject.SfecdLe']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixDetails.IpPrefixDetail.ExtensionObject']['meta_info']
_meta_table['Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixDetails.IpPrefixDetail.DetailFibEntryInformation']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixDetails.IpPrefixDetail']['meta_info']
_meta_table['Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixDetails.IpPrefixDetail.FibEntryPath']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixDetails.IpPrefixDetail']['meta_info']
_meta_table['Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixDetails.IpPrefixDetail.Srv6Information']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixDetails.IpPrefixDetail']['meta_info']
_meta_table['Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixDetails.IpPrefixDetail.ExtensionObject']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixDetails.IpPrefixDetail']['meta_info']
_meta_table['Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixDetails.IpPrefixDetail']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixDetails']['meta_info']
_meta_table['Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.Summary.ExclusiveLoadSharingElement']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.Summary']['meta_info']
_meta_table['Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.Summary.SharedLoadSharingElement']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.Summary']['meta_info']
_meta_table['Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.Summary.CrossSharedLoadSharingElement']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.Summary']['meta_info']
_meta_table['Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.Summary.LabelSharedLoadSharingElement']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.Summary']['meta_info']
_meta_table['Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.InterfaceInfos.InterfaceInfo.Interfaces.Interface.SiInternal.FibIdbHist.EvtEntry']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.InterfaceInfos.InterfaceInfo.Interfaces.Interface.SiInternal.FibIdbHist']['meta_info']
_meta_table['Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.InterfaceInfos.InterfaceInfo.Interfaces.Interface.SiInternal.FibSrteHeadHist.EvtEntry']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.InterfaceInfos.InterfaceInfo.Interfaces.Interface.SiInternal.FibSrteHeadHist']['meta_info']
_meta_table['Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.InterfaceInfos.InterfaceInfo.Interfaces.Interface.SiInternal.FibIdbHist']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.InterfaceInfos.InterfaceInfo.Interfaces.Interface.SiInternal']['meta_info']
_meta_table['Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.InterfaceInfos.InterfaceInfo.Interfaces.Interface.SiInternal.FibSrteHeadHist']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.InterfaceInfos.InterfaceInfo.Interfaces.Interface.SiInternal']['meta_info']
_meta_table['Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.InterfaceInfos.InterfaceInfo.Interfaces.Interface.DetailFibIntInformation']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.InterfaceInfos.InterfaceInfo.Interfaces.Interface']['meta_info']
_meta_table['Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.InterfaceInfos.InterfaceInfo.Interfaces.Interface.SiInternal']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.InterfaceInfos.InterfaceInfo.Interfaces.Interface']['meta_info']
_meta_table['Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.InterfaceInfos.InterfaceInfo.Interfaces.Interface']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.InterfaceInfos.InterfaceInfo.Interfaces']['meta_info']
_meta_table['Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.InterfaceInfos.InterfaceInfo.Interfaces']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.InterfaceInfos.InterfaceInfo']['meta_info']
_meta_table['Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.InterfaceInfos.InterfaceInfo']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.InterfaceInfos']['meta_info']
_meta_table['Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixBriefs.IpPrefixBrief.DetailFibEntryInformation.LoadshareInformation.LoadInformtionInternalData.AdjacencyAddress']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixBriefs.IpPrefixBrief.DetailFibEntryInformation.LoadshareInformation.LoadInformtionInternalData']['meta_info']
_meta_table['Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixBriefs.IpPrefixBrief.DetailFibEntryInformation.LoadshareInformation.LoadInformtionInternalData.PbtsClassIsFallbackMapped']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixBriefs.IpPrefixBrief.DetailFibEntryInformation.LoadshareInformation.LoadInformtionInternalData']['meta_info']
_meta_table['Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixBriefs.IpPrefixBrief.DetailFibEntryInformation.LoadshareInformation.LoadInformtionInternalData.PbtsFallbackToDrop']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixBriefs.IpPrefixBrief.DetailFibEntryInformation.LoadshareInformation.LoadInformtionInternalData']['meta_info']
_meta_table['Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixBriefs.IpPrefixBrief.DetailFibEntryInformation.LoadshareInformation.LoadInformtionInternalData.TunnelIsForwardClass']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixBriefs.IpPrefixBrief.DetailFibEntryInformation.LoadshareInformation.LoadInformtionInternalData']['meta_info']
_meta_table['Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixBriefs.IpPrefixBrief.DetailFibEntryInformation.LoadshareInformation.LoadInformtionInternalData']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixBriefs.IpPrefixBrief.DetailFibEntryInformation.LoadshareInformation']['meta_info']
_meta_table['Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixBriefs.IpPrefixBrief.DetailFibEntryInformation.LoadshareInformation']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixBriefs.IpPrefixBrief.DetailFibEntryInformation']['meta_info']
_meta_table['Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixBriefs.IpPrefixBrief.FibEntryPath.FibShTblPath.MoreDetailAboutPath.SpdIpencap.IpEncapHdr']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixBriefs.IpPrefixBrief.FibEntryPath.FibShTblPath.MoreDetailAboutPath.SpdIpencap']['meta_info']
_meta_table['Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixBriefs.IpPrefixBrief.FibEntryPath.FibShTblPath.MoreDetailAboutPath.SpdIpencap']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixBriefs.IpPrefixBrief.FibEntryPath.FibShTblPath.MoreDetailAboutPath']['meta_info']
_meta_table['Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixBriefs.IpPrefixBrief.FibEntryPath.FibShTblPath.MplsInformationForPath.IgpLabelStackArray']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixBriefs.IpPrefixBrief.FibEntryPath.FibShTblPath.MplsInformationForPath']['meta_info']
_meta_table['Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixBriefs.IpPrefixBrief.FibEntryPath.FibShTblPath.MoreDetailAboutPath']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixBriefs.IpPrefixBrief.FibEntryPath.FibShTblPath']['meta_info']
_meta_table['Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixBriefs.IpPrefixBrief.FibEntryPath.FibShTblPath.MplsInformationForPath']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixBriefs.IpPrefixBrief.FibEntryPath.FibShTblPath']['meta_info']
_meta_table['Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixBriefs.IpPrefixBrief.FibEntryPath.FibShTblPath']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixBriefs.IpPrefixBrief.FibEntryPath']['meta_info']
_meta_table['Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixBriefs.IpPrefixBrief.Srv6Information.Srv6Statistics']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixBriefs.IpPrefixBrief.Srv6Information']['meta_info']
_meta_table['Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixBriefs.IpPrefixBrief.ExtensionObject.SfecdLe']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixBriefs.IpPrefixBrief.ExtensionObject']['meta_info']
_meta_table['Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixBriefs.IpPrefixBrief.DetailFibEntryInformation']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixBriefs.IpPrefixBrief']['meta_info']
_meta_table['Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixBriefs.IpPrefixBrief.FibEntryPath']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixBriefs.IpPrefixBrief']['meta_info']
_meta_table['Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixBriefs.IpPrefixBrief.Srv6Information']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixBriefs.IpPrefixBrief']['meta_info']
_meta_table['Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixBriefs.IpPrefixBrief.ExtensionObject']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixBriefs.IpPrefixBrief']['meta_info']
_meta_table['Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixBriefs.IpPrefixBrief']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixBriefs']['meta_info']
_meta_table['Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixDetails']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf']['meta_info']
_meta_table['Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.Summary']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf']['meta_info']
_meta_table['Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.InterfaceInfos']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf']['meta_info']
_meta_table['Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf.IpPrefixBriefs']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf']['meta_info']
_meta_table['Fib.Nodes.Node.Protocols.Protocol.Vrfs.Vrf']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Protocols.Protocol.Vrfs']['meta_info']
_meta_table['Fib.Nodes.Node.Protocols.Protocol.NhIds.NhId']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Protocols.Protocol.NhIds']['meta_info']
_meta_table['Fib.Nodes.Node.Protocols.Protocol.ExternalClientSummaries.ExternalClientSummary.SesPlSum']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Protocols.Protocol.ExternalClientSummaries.ExternalClientSummary']['meta_info']
_meta_table['Fib.Nodes.Node.Protocols.Protocol.ExternalClientSummaries.ExternalClientSummary']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Protocols.Protocol.ExternalClientSummaries']['meta_info']
_meta_table['Fib.Nodes.Node.Protocols.Protocol.Misc.MiIssuState.FisProtoState']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Protocols.Protocol.Misc.MiIssuState']['meta_info']
_meta_table['Fib.Nodes.Node.Protocols.Protocol.Misc.MiPlatCapabilities.FpcLispDecapOverV4']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Protocols.Protocol.Misc.MiPlatCapabilities']['meta_info']
_meta_table['Fib.Nodes.Node.Protocols.Protocol.Misc.MiPlatCapabilities.FpcLispDecapOverV6']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Protocols.Protocol.Misc.MiPlatCapabilities']['meta_info']
_meta_table['Fib.Nodes.Node.Protocols.Protocol.Misc.MiPlatCapabilities.FpcLispUcmp']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Protocols.Protocol.Misc.MiPlatCapabilities']['meta_info']
_meta_table['Fib.Nodes.Node.Protocols.Protocol.Misc.MiPlatCapabilities.FpcResolveViaTable']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Protocols.Protocol.Misc.MiPlatCapabilities']['meta_info']
_meta_table['Fib.Nodes.Node.Protocols.Protocol.Misc.MiProtoDbgStat.FpdPlatfUpdStats.FpusObjStat.FosObjActStat']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Protocols.Protocol.Misc.MiProtoDbgStat.FpdPlatfUpdStats.FpusObjStat']['meta_info']
_meta_table['Fib.Nodes.Node.Protocols.Protocol.Misc.MiProtoDbgStat.FpdPlatfUpdStats.FpusObjStat']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Protocols.Protocol.Misc.MiProtoDbgStat.FpdPlatfUpdStats']['meta_info']
_meta_table['Fib.Nodes.Node.Protocols.Protocol.Misc.MiProtoDbgStat.FpdGtrieTiming.FgtGtrieFnTiming']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Protocols.Protocol.Misc.MiProtoDbgStat.FpdGtrieTiming']['meta_info']
_meta_table['Fib.Nodes.Node.Protocols.Protocol.Misc.MiProtoDbgStat.FpdPlatfUpdStats']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Protocols.Protocol.Misc.MiProtoDbgStat']['meta_info']
_meta_table['Fib.Nodes.Node.Protocols.Protocol.Misc.MiProtoDbgStat.FpdGtrieTiming']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Protocols.Protocol.Misc.MiProtoDbgStat']['meta_info']
_meta_table['Fib.Nodes.Node.Protocols.Protocol.Misc.MiIssuState']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Protocols.Protocol.Misc']['meta_info']
_meta_table['Fib.Nodes.Node.Protocols.Protocol.Misc.MiPlatCapabilities']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Protocols.Protocol.Misc']['meta_info']
_meta_table['Fib.Nodes.Node.Protocols.Protocol.Misc.MiProtoDbgStat']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Protocols.Protocol.Misc']['meta_info']
_meta_table['Fib.Nodes.Node.Protocols.Protocol.Misc.MiIdbPurgeCntr']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Protocols.Protocol.Misc']['meta_info']
_meta_table['Fib.Nodes.Node.Protocols.Protocol.Misc.MiDel']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Protocols.Protocol.Misc']['meta_info']
_meta_table['Fib.Nodes.Node.Protocols.Protocol.Misc.MiFrrStat']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Protocols.Protocol.Misc']['meta_info']
_meta_table['Fib.Nodes.Node.Protocols.Protocol.LocalLabel.Conflicts.Conflict.Ext.Pfx']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Protocols.Protocol.LocalLabel.Conflicts.Conflict.Ext']['meta_info']
_meta_table['Fib.Nodes.Node.Protocols.Protocol.LocalLabel.Conflicts.Conflict.Ext.Lsm']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Protocols.Protocol.LocalLabel.Conflicts.Conflict.Ext']['meta_info']
_meta_table['Fib.Nodes.Node.Protocols.Protocol.LocalLabel.Conflicts.Conflict.Ext']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Protocols.Protocol.LocalLabel.Conflicts.Conflict']['meta_info']
_meta_table['Fib.Nodes.Node.Protocols.Protocol.LocalLabel.Conflicts.Conflict']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Protocols.Protocol.LocalLabel.Conflicts']['meta_info']
_meta_table['Fib.Nodes.Node.Protocols.Protocol.LocalLabel.Conflicts']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Protocols.Protocol.LocalLabel']['meta_info']
_meta_table['Fib.Nodes.Node.Protocols.Protocol.IssuState']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Protocols.Protocol']['meta_info']
_meta_table['Fib.Nodes.Node.Protocols.Protocol.Resource']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Protocols.Protocol']['meta_info']
_meta_table['Fib.Nodes.Node.Protocols.Protocol.FibSummaries']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Protocols.Protocol']['meta_info']
_meta_table['Fib.Nodes.Node.Protocols.Protocol.ExternalSummaryAll']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Protocols.Protocol']['meta_info']
_meta_table['Fib.Nodes.Node.Protocols.Protocol.FrrLog']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Protocols.Protocol']['meta_info']
_meta_table['Fib.Nodes.Node.Protocols.Protocol.Vrfs']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Protocols.Protocol']['meta_info']
_meta_table['Fib.Nodes.Node.Protocols.Protocol.NhIds']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Protocols.Protocol']['meta_info']
_meta_table['Fib.Nodes.Node.Protocols.Protocol.ExternalClientSummaries']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Protocols.Protocol']['meta_info']
_meta_table['Fib.Nodes.Node.Protocols.Protocol.Misc']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Protocols.Protocol']['meta_info']
_meta_table['Fib.Nodes.Node.Protocols.Protocol.LocalLabel']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Protocols.Protocol']['meta_info']
_meta_table['Fib.Nodes.Node.Protocols.Protocol']['meta_info'].parent =_meta_table['Fib.Nodes.Node.Protocols']['meta_info']
_meta_table['Fib.Nodes.Node.Global_']['meta_info'].parent =_meta_table['Fib.Nodes.Node']['meta_info']
_meta_table['Fib.Nodes.Node.Protocols']['meta_info'].parent =_meta_table['Fib.Nodes.Node']['meta_info']
_meta_table['Fib.Nodes.Node']['meta_info'].parent =_meta_table['Fib.Nodes']['meta_info']
_meta_table['Fib.Nodes']['meta_info'].parent =_meta_table['Fib']['meta_info']
_meta_table['MplsForwarding.Nodes.Node.FrrLogs.FrrLog.StartTime']['meta_info'].parent =_meta_table['MplsForwarding.Nodes.Node.FrrLogs.FrrLog']['meta_info']
_meta_table['MplsForwarding.Nodes.Node.FrrLogs.FrrLog']['meta_info'].parent =_meta_table['MplsForwarding.Nodes.Node.FrrLogs']['meta_info']
_meta_table['MplsForwarding.Nodes.Node.LabelFib.ForwardingDetails.ForwardingDetail.LabelInformation.LabelInformationDetail']['meta_info'].parent =_meta_table['MplsForwarding.Nodes.Node.LabelFib.ForwardingDetails.ForwardingDetail.LabelInformation']['meta_info']
_meta_table['MplsForwarding.Nodes.Node.LabelFib.ForwardingDetails.ForwardingDetail.LdiInformation']['meta_info'].parent =_meta_table['MplsForwarding.Nodes.Node.LabelFib.ForwardingDetails.ForwardingDetail']['meta_info']
_meta_table['MplsForwarding.Nodes.Node.LabelFib.ForwardingDetails.ForwardingDetail.MulticastInformation']['meta_info'].parent =_meta_table['MplsForwarding.Nodes.Node.LabelFib.ForwardingDetails.ForwardingDetail']['meta_info']
_meta_table['MplsForwarding.Nodes.Node.LabelFib.ForwardingDetails.ForwardingDetail.LabelInformation']['meta_info'].parent =_meta_table['MplsForwarding.Nodes.Node.LabelFib.ForwardingDetails.ForwardingDetail']['meta_info']
_meta_table['MplsForwarding.Nodes.Node.LabelFib.ForwardingDetails.ForwardingDetail']['meta_info'].parent =_meta_table['MplsForwarding.Nodes.Node.LabelFib.ForwardingDetails']['meta_info']
_meta_table['MplsForwarding.Nodes.Node.LabelFib.Informations.Information.LabelInformation.LabelInformationDetail']['meta_info'].parent =_meta_table['MplsForwarding.Nodes.Node.LabelFib.Informations.Information.LabelInformation']['meta_info']
_meta_table['MplsForwarding.Nodes.Node.LabelFib.Informations.Information.LdiInformation']['meta_info'].parent =_meta_table['MplsForwarding.Nodes.Node.LabelFib.Informations.Information']['meta_info']
_meta_table['MplsForwarding.Nodes.Node.LabelFib.Informations.Information.MulticastInformation']['meta_info'].parent =_meta_table['MplsForwarding.Nodes.Node.LabelFib.Informations.Information']['meta_info']
_meta_table['MplsForwarding.Nodes.Node.LabelFib.Informations.Information.LabelInformation']['meta_info'].parent =_meta_table['MplsForwarding.Nodes.Node.LabelFib.Informations.Information']['meta_info']
_meta_table['MplsForwarding.Nodes.Node.LabelFib.Informations.Information']['meta_info'].parent =_meta_table['MplsForwarding.Nodes.Node.LabelFib.Informations']['meta_info']
_meta_table['MplsForwarding.Nodes.Node.LabelFib.LabelSecurity.Interfaces.Interface']['meta_info'].parent =_meta_table['MplsForwarding.Nodes.Node.LabelFib.LabelSecurity.Interfaces']['meta_info']
_meta_table['MplsForwarding.Nodes.Node.LabelFib.LabelSecurity.Interfaces']['meta_info'].parent =_meta_table['MplsForwarding.Nodes.Node.LabelFib.LabelSecurity']['meta_info']
_meta_table['MplsForwarding.Nodes.Node.LabelFib.LabelSecurity.Summary']['meta_info'].parent =_meta_table['MplsForwarding.Nodes.Node.LabelFib.LabelSecurity']['meta_info']
_meta_table['MplsForwarding.Nodes.Node.LabelFib.ForwardingDetails']['meta_info'].parent =_meta_table['MplsForwarding.Nodes.Node.LabelFib']['meta_info']
_meta_table['MplsForwarding.Nodes.Node.LabelFib.Informations']['meta_info'].parent =_meta_table['MplsForwarding.Nodes.Node.LabelFib']['meta_info']
_meta_table['MplsForwarding.Nodes.Node.LabelFib.LabelSecurity']['meta_info'].parent =_meta_table['MplsForwarding.Nodes.Node.LabelFib']['meta_info']
_meta_table['MplsForwarding.Nodes.Node.Tunnel.ForwardingTunnels.ForwardingTunnel.Fwdg.LabelInformation.LabelInformationDetail']['meta_info'].parent =_meta_table['MplsForwarding.Nodes.Node.Tunnel.ForwardingTunnels.ForwardingTunnel.Fwdg.LabelInformation']['meta_info']
_meta_table['MplsForwarding.Nodes.Node.Tunnel.ForwardingTunnels.ForwardingTunnel.Fwdg.LdiInformation']['meta_info'].parent =_meta_table['MplsForwarding.Nodes.Node.Tunnel.ForwardingTunnels.ForwardingTunnel.Fwdg']['meta_info']
_meta_table['MplsForwarding.Nodes.Node.Tunnel.ForwardingTunnels.ForwardingTunnel.Fwdg.MulticastInformation']['meta_info'].parent =_meta_table['MplsForwarding.Nodes.Node.Tunnel.ForwardingTunnels.ForwardingTunnel.Fwdg']['meta_info']
_meta_table['MplsForwarding.Nodes.Node.Tunnel.ForwardingTunnels.ForwardingTunnel.Fwdg.LabelInformation']['meta_info'].parent =_meta_table['MplsForwarding.Nodes.Node.Tunnel.ForwardingTunnels.ForwardingTunnel.Fwdg']['meta_info']
_meta_table['MplsForwarding.Nodes.Node.Tunnel.ForwardingTunnels.ForwardingTunnel.TunnelInfo']['meta_info'].parent =_meta_table['MplsForwarding.Nodes.Node.Tunnel.ForwardingTunnels.ForwardingTunnel']['meta_info']
_meta_table['MplsForwarding.Nodes.Node.Tunnel.ForwardingTunnels.ForwardingTunnel.Fwdg']['meta_info'].parent =_meta_table['MplsForwarding.Nodes.Node.Tunnel.ForwardingTunnels.ForwardingTunnel']['meta_info']
_meta_table['MplsForwarding.Nodes.Node.Tunnel.ForwardingTunnels.ForwardingTunnel']['meta_info'].parent =_meta_table['MplsForwarding.Nodes.Node.Tunnel.ForwardingTunnels']['meta_info']
_meta_table['MplsForwarding.Nodes.Node.Tunnel.ForwardingTunnels']['meta_info'].parent =_meta_table['MplsForwarding.Nodes.Node.Tunnel']['meta_info']
_meta_table['MplsForwarding.Nodes.Node.FrrDatabase.FrrdbProtectedInterfaceTableSummaries.FrrdbProtectedInterfaceTableSummary']['meta_info'].parent =_meta_table['MplsForwarding.Nodes.Node.FrrDatabase.FrrdbProtectedInterfaceTableSummaries']['meta_info']
_meta_table['MplsForwarding.Nodes.Node.FrrDatabase.FrrdbTunnelMidpoints.FrrdbTunnelMidpoint.FrrDb.FrrEntryId.Head']['meta_info'].parent =_meta_table['MplsForwarding.Nodes.Node.FrrDatabase.FrrdbTunnelMidpoints.FrrdbTunnelMidpoint.FrrDb.FrrEntryId']['meta_info']
_meta_table['MplsForwarding.Nodes.Node.FrrDatabase.FrrdbTunnelMidpoints.FrrdbTunnelMidpoint.FrrDb.FrrEntryId.Midpoint']['meta_info'].parent =_meta_table['MplsForwarding.Nodes.Node.FrrDatabase.FrrdbTunnelMidpoints.FrrdbTunnelMidpoint.FrrDb.FrrEntryId']['meta_info']
_meta_table['MplsForwarding.Nodes.Node.FrrDatabase.FrrdbTunnelMidpoints.FrrdbTunnelMidpoint.FrrDb.MulticastLeg.FrrEntryId.Head']['meta_info'].parent =_meta_table['MplsForwarding.Nodes.Node.FrrDatabase.FrrdbTunnelMidpoints.FrrdbTunnelMidpoint.FrrDb.MulticastLeg.FrrEntryId']['meta_info']
_meta_table['MplsForwarding.Nodes.Node.FrrDatabase.FrrdbTunnelMidpoints.FrrdbTunnelMidpoint.FrrDb.MulticastLeg.FrrEntryId.Midpoint']['meta_info'].parent =_meta_table['MplsForwarding.Nodes.Node.FrrDatabase.FrrdbTunnelMidpoints.FrrdbTunnelMidpoint.FrrDb.MulticastLeg.FrrEntryId']['meta_info']
_meta_table['MplsForwarding.Nodes.Node.FrrDatabase.FrrdbTunnelMidpoints.FrrdbTunnelMidpoint.FrrDb.MulticastLeg.FrrEntryId']['meta_info'].parent =_meta_table['MplsForwarding.Nodes.Node.FrrDatabase.FrrdbTunnelMidpoints.FrrdbTunnelMidpoint.FrrDb.MulticastLeg']['meta_info']
_meta_table['MplsForwarding.Nodes.Node.FrrDatabase.FrrdbTunnelMidpoints.FrrdbTunnelMidpoint.FrrDb.FrrEntryId']['meta_info'].parent =_meta_table['MplsForwarding.Nodes.Node.FrrDatabase.FrrdbTunnelMidpoints.FrrdbTunnelMidpoint.FrrDb']['meta_info']
_meta_table['MplsForwarding.Nodes.Node.FrrDatabase.FrrdbTunnelMidpoints.FrrdbTunnelMidpoint.FrrDb.MulticastLeg']['meta_info'].parent =_meta_table['MplsForwarding.Nodes.Node.FrrDatabase.FrrdbTunnelMidpoints.FrrdbTunnelMidpoint.FrrDb']['meta_info']
_meta_table['MplsForwarding.Nodes.Node.FrrDatabase.FrrdbTunnelMidpoints.FrrdbTunnelMidpoint.FrrDb']['meta_info'].parent =_meta_table['MplsForwarding.Nodes.Node.FrrDatabase.FrrdbTunnelMidpoints.FrrdbTunnelMidpoint']['meta_info']
_meta_table['MplsForwarding.Nodes.Node.FrrDatabase.FrrdbTunnelMidpoints.FrrdbTunnelMidpoint']['meta_info'].parent =_meta_table['MplsForwarding.Nodes.Node.FrrDatabase.FrrdbTunnelMidpoints']['meta_info']
_meta_table['MplsForwarding.Nodes.Node.FrrDatabase.FrrdbTunnelHeads.FrrdbTunnelHead.FrrDb.FrrEntryId.Head']['meta_info'].parent =_meta_table['MplsForwarding.Nodes.Node.FrrDatabase.FrrdbTunnelHeads.FrrdbTunnelHead.FrrDb.FrrEntryId']['meta_info']
_meta_table['MplsForwarding.Nodes.Node.FrrDatabase.FrrdbTunnelHeads.FrrdbTunnelHead.FrrDb.FrrEntryId.Midpoint']['meta_info'].parent =_meta_table['MplsForwarding.Nodes.Node.FrrDatabase.FrrdbTunnelHeads.FrrdbTunnelHead.FrrDb.FrrEntryId']['meta_info']
_meta_table['MplsForwarding.Nodes.Node.FrrDatabase.FrrdbTunnelHeads.FrrdbTunnelHead.FrrDb.MulticastLeg.FrrEntryId.Head']['meta_info'].parent =_meta_table['MplsForwarding.Nodes.Node.FrrDatabase.FrrdbTunnelHeads.FrrdbTunnelHead.FrrDb.MulticastLeg.FrrEntryId']['meta_info']
_meta_table['MplsForwarding.Nodes.Node.FrrDatabase.FrrdbTunnelHeads.FrrdbTunnelHead.FrrDb.MulticastLeg.FrrEntryId.Midpoint']['meta_info'].parent =_meta_table['MplsForwarding.Nodes.Node.FrrDatabase.FrrdbTunnelHeads.FrrdbTunnelHead.FrrDb.MulticastLeg.FrrEntryId']['meta_info']
_meta_table['MplsForwarding.Nodes.Node.FrrDatabase.FrrdbTunnelHeads.FrrdbTunnelHead.FrrDb.MulticastLeg.FrrEntryId']['meta_info'].parent =_meta_table['MplsForwarding.Nodes.Node.FrrDatabase.FrrdbTunnelHeads.FrrdbTunnelHead.FrrDb.MulticastLeg']['meta_info']
_meta_table['MplsForwarding.Nodes.Node.FrrDatabase.FrrdbTunnelHeads.FrrdbTunnelHead.FrrDb.FrrEntryId']['meta_info'].parent =_meta_table['MplsForwarding.Nodes.Node.FrrDatabase.FrrdbTunnelHeads.FrrdbTunnelHead.FrrDb']['meta_info']
_meta_table['MplsForwarding.Nodes.Node.FrrDatabase.FrrdbTunnelHeads.FrrdbTunnelHead.FrrDb.MulticastLeg']['meta_info'].parent =_meta_table['MplsForwarding.Nodes.Node.FrrDatabase.FrrdbTunnelHeads.FrrdbTunnelHead.FrrDb']['meta_info']
_meta_table['MplsForwarding.Nodes.Node.FrrDatabase.FrrdbTunnelHeads.FrrdbTunnelHead.FrrDb']['meta_info'].parent =_meta_table['MplsForwarding.Nodes.Node.FrrDatabase.FrrdbTunnelHeads.FrrdbTunnelHead']['meta_info']
_meta_table['MplsForwarding.Nodes.Node.FrrDatabase.FrrdbTunnelHeads.FrrdbTunnelHead']['meta_info'].parent =_meta_table['MplsForwarding.Nodes.Node.FrrDatabase.FrrdbTunnelHeads']['meta_info']
_meta_table['MplsForwarding.Nodes.Node.FrrDatabase.FrrdbBackupInterfaceSummaries.FrrdbBackupInterfaceSummary']['meta_info'].parent =_meta_table['MplsForwarding.Nodes.Node.FrrDatabase.FrrdbBackupInterfaceSummaries']['meta_info']
_meta_table['MplsForwarding.Nodes.Node.FrrDatabase.FrrdbSummary']['meta_info'].parent =_meta_table['MplsForwarding.Nodes.Node.FrrDatabase']['meta_info']
_meta_table['MplsForwarding.Nodes.Node.FrrDatabase.FrrdbProtectedInterfaceTableSummaries']['meta_info'].parent =_meta_table['MplsForwarding.Nodes.Node.FrrDatabase']['meta_info']
_meta_table['MplsForwarding.Nodes.Node.FrrDatabase.FrrdbTunnelMidpointSummary']['meta_info'].parent =_meta_table['MplsForwarding.Nodes.Node.FrrDatabase']['meta_info']
_meta_table['MplsForwarding.Nodes.Node.FrrDatabase.FrrdbTunnelMidpoints']['meta_info'].parent =_meta_table['MplsForwarding.Nodes.Node.FrrDatabase']['meta_info']
_meta_table['MplsForwarding.Nodes.Node.FrrDatabase.FrrdbTunnelHeads']['meta_info'].parent =_meta_table['MplsForwarding.Nodes.Node.FrrDatabase']['meta_info']
_meta_table['MplsForwarding.Nodes.Node.FrrDatabase.FrrdbTunnelHeadSummary']['meta_info'].parent =_meta_table['MplsForwarding.Nodes.Node.FrrDatabase']['meta_info']
_meta_table['MplsForwarding.Nodes.Node.FrrDatabase.FrrdbBackupInterfaceSummaries']['meta_info'].parent =_meta_table['MplsForwarding.Nodes.Node.FrrDatabase']['meta_info']
_meta_table['MplsForwarding.Nodes.Node.ForwardingSummary']['meta_info'].parent =_meta_table['MplsForwarding.Nodes.Node']['meta_info']
_meta_table['MplsForwarding.Nodes.Node.FrrLogs']['meta_info'].parent =_meta_table['MplsForwarding.Nodes.Node']['meta_info']
_meta_table['MplsForwarding.Nodes.Node.LabelFib']['meta_info'].parent =_meta_table['MplsForwarding.Nodes.Node']['meta_info']
_meta_table['MplsForwarding.Nodes.Node.Tunnel']['meta_info'].parent =_meta_table['MplsForwarding.Nodes.Node']['meta_info']
_meta_table['MplsForwarding.Nodes.Node.FrrDatabase']['meta_info'].parent =_meta_table['MplsForwarding.Nodes.Node']['meta_info']
_meta_table['MplsForwarding.Nodes.Node']['meta_info'].parent =_meta_table['MplsForwarding.Nodes']['meta_info']
_meta_table['MplsForwarding.Nodes']['meta_info'].parent =_meta_table['MplsForwarding']['meta_info']
