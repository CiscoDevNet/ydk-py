


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'Ipv6NdShVrStateEnum' : _MetaInfoEnum('Ipv6NdShVrStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper',
        {
            'deleted':'deleted',
            'standby':'standby',
            'active':'active',
        }, 'Cisco-IOS-XR-ipv6-nd-oper', _yang_ns._namespaces['Cisco-IOS-XR-ipv6-nd-oper']),
    'Ipv6NdShStateEnum' : _MetaInfoEnum('Ipv6NdShStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper',
        {
            'incomplete':'incomplete',
            'reachable':'reachable',
            'stale':'stale',
            'glean':'glean',
            'delay':'delay',
            'probe':'probe',
            'delete':'delete',
        }, 'Cisco-IOS-XR-ipv6-nd-oper', _yang_ns._namespaces['Cisco-IOS-XR-ipv6-nd-oper']),
    'Ipv6NdMediaEncapEnum' : _MetaInfoEnum('Ipv6NdMediaEncapEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper',
        {
            'none':'none',
            'arpa':'arpa',
            'snap':'snap',
            'ieee802-1q':'ieee802_1q',
            'srp':'srp',
            'srpa':'srpa',
            'srpb':'srpb',
            'ppp':'ppp',
            'hdlc':'hdlc',
            'chdlc':'chdlc',
            'dot1q':'dot1q',
            'fr':'fr',
            'gre':'gre',
        }, 'Cisco-IOS-XR-ipv6-nd-oper', _yang_ns._namespaces['Cisco-IOS-XR-ipv6-nd-oper']),
    'Ipv6NdShVrFlagsEnum' : _MetaInfoEnum('Ipv6NdShVrFlagsEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper',
        {
            'no-flags':'no_flags',
            'final-ra':'final_ra',
        }, 'Cisco-IOS-XR-ipv6-nd-oper', _yang_ns._namespaces['Cisco-IOS-XR-ipv6-nd-oper']),
    'Ipv6NdNeighborOriginEnum' : _MetaInfoEnum('Ipv6NdNeighborOriginEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper',
        {
            'other':'other',
            'static':'static',
            'dynamic':'dynamic',
        }, 'Cisco-IOS-XR-ipv6-nd-oper', _yang_ns._namespaces['Cisco-IOS-XR-ipv6-nd-oper']),
    'Ipv6NdBndlStateEnum' : _MetaInfoEnum('Ipv6NdBndlStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper',
        {
            'run':'run',
            'error':'error',
            'wait':'wait',
        }, 'Cisco-IOS-XR-ipv6-nd-oper', _yang_ns._namespaces['Cisco-IOS-XR-ipv6-nd-oper']),
    'Ipv6NodeDiscovery.Nodes.Node.NeighborInterfaces.NeighborInterface.HostAddresses.HostAddress.LastReachedTime' : {
        'meta_info' : _MetaInfoClass('Ipv6NodeDiscovery.Nodes.Node.NeighborInterfaces.NeighborInterface.HostAddresses.HostAddress.LastReachedTime',
            False, 
            [
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of seconds
                ''',
                'seconds',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-nd-oper',
            'last-reached-time',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-nd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper'
        ),
    },
    'Ipv6NodeDiscovery.Nodes.Node.NeighborInterfaces.NeighborInterface.HostAddresses.HostAddress' : {
        'meta_info' : _MetaInfoClass('Ipv6NodeDiscovery.Nodes.Node.NeighborInterfaces.NeighborInterface.HostAddresses.HostAddress',
            False, 
            [
            _MetaInfoClassMember('host-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                Host Address
                ''',
                'host_address',
                'Cisco-IOS-XR-ipv6-nd-oper', True),
            _MetaInfoClassMember('encapsulation', REFERENCE_ENUM_CLASS, 'Ipv6NdMediaEncapEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper', 'Ipv6NdMediaEncapEnum', 
                [], [], 
                '''                Preferred media encap type
                ''',
                'encapsulation',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Interface name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            _MetaInfoClassMember('is-router', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                IsRouter
                ''',
                'is_router',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            _MetaInfoClassMember('last-reached-time', REFERENCE_CLASS, 'LastReachedTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper', 'Ipv6NodeDiscovery.Nodes.Node.NeighborInterfaces.NeighborInterface.HostAddresses.HostAddress.LastReachedTime', 
                [], [], 
                '''                Last time of reachability
                ''',
                'last_reached_time',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            _MetaInfoClassMember('link-layer-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                Link-Layer Address
                ''',
                'link_layer_address',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            _MetaInfoClassMember('location', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location where the neighbor entry exists
                ''',
                'location',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            _MetaInfoClassMember('origin-encapsulation', REFERENCE_ENUM_CLASS, 'Ipv6NdNeighborOriginEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper', 'Ipv6NdNeighborOriginEnum', 
                [], [], 
                '''                Neighbor origin
                ''',
                'origin_encapsulation',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            _MetaInfoClassMember('reachability-state', REFERENCE_ENUM_CLASS, 'Ipv6NdShStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper', 'Ipv6NdShStateEnum', 
                [], [], 
                '''                Current state
                ''',
                'reachability_state',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            _MetaInfoClassMember('selected-encapsulation', REFERENCE_ENUM_CLASS, 'Ipv6NdMediaEncapEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper', 'Ipv6NdMediaEncapEnum', 
                [], [], 
                '''                Selected media encap
                ''',
                'selected_encapsulation',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            _MetaInfoClassMember('serg-flags', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ND serg flags for this entry
                ''',
                'serg_flags',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-nd-oper',
            'host-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-nd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper'
        ),
    },
    'Ipv6NodeDiscovery.Nodes.Node.NeighborInterfaces.NeighborInterface.HostAddresses' : {
        'meta_info' : _MetaInfoClass('Ipv6NodeDiscovery.Nodes.Node.NeighborInterfaces.NeighborInterface.HostAddresses',
            False, 
            [
            _MetaInfoClassMember('host-address', REFERENCE_LIST, 'HostAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper', 'Ipv6NodeDiscovery.Nodes.Node.NeighborInterfaces.NeighborInterface.HostAddresses.HostAddress', 
                [], [], 
                '''                IPv6 Neighbor detailed information
                ''',
                'host_address',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-nd-oper',
            'host-addresses',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-nd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper'
        ),
    },
    'Ipv6NodeDiscovery.Nodes.Node.NeighborInterfaces.NeighborInterface' : {
        'meta_info' : _MetaInfoClass('Ipv6NodeDiscovery.Nodes.Node.NeighborInterfaces.NeighborInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv6-nd-oper', True),
            _MetaInfoClassMember('host-addresses', REFERENCE_CLASS, 'HostAddresses' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper', 'Ipv6NodeDiscovery.Nodes.Node.NeighborInterfaces.NeighborInterface.HostAddresses', 
                [], [], 
                '''                IPv6 node discovery list of neighbor host
                addresses
                ''',
                'host_addresses',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-nd-oper',
            'neighbor-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-nd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper'
        ),
    },
    'Ipv6NodeDiscovery.Nodes.Node.NeighborInterfaces' : {
        'meta_info' : _MetaInfoClass('Ipv6NodeDiscovery.Nodes.Node.NeighborInterfaces',
            False, 
            [
            _MetaInfoClassMember('neighbor-interface', REFERENCE_LIST, 'NeighborInterface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper', 'Ipv6NodeDiscovery.Nodes.Node.NeighborInterfaces.NeighborInterface', 
                [], [], 
                '''                IPv6 node discovery neighbor interface
                ''',
                'neighbor_interface',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-nd-oper',
            'neighbor-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-nd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper'
        ),
    },
    'Ipv6NodeDiscovery.Nodes.Node.NeighborSummary.Multicast' : {
        'meta_info' : _MetaInfoClass('Ipv6NodeDiscovery.Nodes.Node.NeighborSummary.Multicast',
            False, 
            [
            _MetaInfoClassMember('delayed-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total delayed entries
                ''',
                'delayed_entries',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            _MetaInfoClassMember('deleted-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total deleted entries
                ''',
                'deleted_entries',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            _MetaInfoClassMember('incomplete-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total incomplete entries
                ''',
                'incomplete_entries',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            _MetaInfoClassMember('probe-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total probe entries
                ''',
                'probe_entries',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            _MetaInfoClassMember('reachable-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total reachable entries
                ''',
                'reachable_entries',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            _MetaInfoClassMember('stale-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total stale entries
                ''',
                'stale_entries',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            _MetaInfoClassMember('subtotal-neighbor-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total number of entries
                ''',
                'subtotal_neighbor_entries',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-nd-oper',
            'multicast',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-nd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper'
        ),
    },
    'Ipv6NodeDiscovery.Nodes.Node.NeighborSummary.Static' : {
        'meta_info' : _MetaInfoClass('Ipv6NodeDiscovery.Nodes.Node.NeighborSummary.Static',
            False, 
            [
            _MetaInfoClassMember('delayed-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total delayed entries
                ''',
                'delayed_entries',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            _MetaInfoClassMember('deleted-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total deleted entries
                ''',
                'deleted_entries',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            _MetaInfoClassMember('incomplete-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total incomplete entries
                ''',
                'incomplete_entries',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            _MetaInfoClassMember('probe-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total probe entries
                ''',
                'probe_entries',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            _MetaInfoClassMember('reachable-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total reachable entries
                ''',
                'reachable_entries',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            _MetaInfoClassMember('stale-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total stale entries
                ''',
                'stale_entries',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            _MetaInfoClassMember('subtotal-neighbor-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total number of entries
                ''',
                'subtotal_neighbor_entries',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-nd-oper',
            'static',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-nd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper'
        ),
    },
    'Ipv6NodeDiscovery.Nodes.Node.NeighborSummary.Dynamic' : {
        'meta_info' : _MetaInfoClass('Ipv6NodeDiscovery.Nodes.Node.NeighborSummary.Dynamic',
            False, 
            [
            _MetaInfoClassMember('delayed-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total delayed entries
                ''',
                'delayed_entries',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            _MetaInfoClassMember('deleted-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total deleted entries
                ''',
                'deleted_entries',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            _MetaInfoClassMember('incomplete-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total incomplete entries
                ''',
                'incomplete_entries',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            _MetaInfoClassMember('probe-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total probe entries
                ''',
                'probe_entries',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            _MetaInfoClassMember('reachable-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total reachable entries
                ''',
                'reachable_entries',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            _MetaInfoClassMember('stale-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total stale entries
                ''',
                'stale_entries',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            _MetaInfoClassMember('subtotal-neighbor-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total number of entries
                ''',
                'subtotal_neighbor_entries',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-nd-oper',
            'dynamic',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-nd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper'
        ),
    },
    'Ipv6NodeDiscovery.Nodes.Node.NeighborSummary' : {
        'meta_info' : _MetaInfoClass('Ipv6NodeDiscovery.Nodes.Node.NeighborSummary',
            False, 
            [
            _MetaInfoClassMember('dynamic', REFERENCE_CLASS, 'Dynamic' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper', 'Ipv6NodeDiscovery.Nodes.Node.NeighborSummary.Dynamic', 
                [], [], 
                '''                Dynamic neighbor summary
                ''',
                'dynamic',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            _MetaInfoClassMember('multicast', REFERENCE_CLASS, 'Multicast' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper', 'Ipv6NodeDiscovery.Nodes.Node.NeighborSummary.Multicast', 
                [], [], 
                '''                Multicast neighbor summary
                ''',
                'multicast',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            _MetaInfoClassMember('static', REFERENCE_CLASS, 'Static' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper', 'Ipv6NodeDiscovery.Nodes.Node.NeighborSummary.Static', 
                [], [], 
                '''                Static neighbor summary
                ''',
                'static',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            _MetaInfoClassMember('total-neighbor-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total number of entries
                ''',
                'total_neighbor_entries',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-nd-oper',
            'neighbor-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-nd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper'
        ),
    },
    'Ipv6NodeDiscovery.Nodes.Node.BundleNodes.BundleNode.Age' : {
        'meta_info' : _MetaInfoClass('Ipv6NodeDiscovery.Nodes.Node.BundleNodes.BundleNode.Age',
            False, 
            [
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of seconds
                ''',
                'seconds',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-nd-oper',
            'age',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-nd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper'
        ),
    },
    'Ipv6NodeDiscovery.Nodes.Node.BundleNodes.BundleNode' : {
        'meta_info' : _MetaInfoClass('Ipv6NodeDiscovery.Nodes.Node.BundleNodes.BundleNode',
            False, 
            [
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                The bundle node name
                ''',
                'node_name',
                'Cisco-IOS-XR-ipv6-nd-oper', True),
            _MetaInfoClassMember('age', REFERENCE_CLASS, 'Age' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper', 'Ipv6NodeDiscovery.Nodes.Node.BundleNodes.BundleNode.Age', 
                [], [], 
                '''                Uptime of node (secs)
                ''',
                'age',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            _MetaInfoClassMember('group-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Group ID
                ''',
                'group_id',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            _MetaInfoClassMember('process-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Process Name
                ''',
                'process_name',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total packet receives
                ''',
                'received_packets',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            _MetaInfoClassMember('received-sequence-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Received sequence num
                ''',
                'received_sequence_number',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            _MetaInfoClassMember('sent-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total packet sends
                ''',
                'sent_packets',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            _MetaInfoClassMember('sent-sequence-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sent sequence num
                ''',
                'sent_sequence_number',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'Ipv6NdBndlStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper', 'Ipv6NdBndlStateEnum', 
                [], [], 
                '''                State
                ''',
                'state',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            _MetaInfoClassMember('state-changes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                State changes
                ''',
                'state_changes',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-nd-oper',
            'bundle-node',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-nd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper'
        ),
    },
    'Ipv6NodeDiscovery.Nodes.Node.BundleNodes' : {
        'meta_info' : _MetaInfoClass('Ipv6NodeDiscovery.Nodes.Node.BundleNodes',
            False, 
            [
            _MetaInfoClassMember('bundle-node', REFERENCE_LIST, 'BundleNode' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper', 'Ipv6NodeDiscovery.Nodes.Node.BundleNodes.BundleNode', 
                [], [], 
                '''                IPv6 ND operational data for a specific
                bundle node
                ''',
                'bundle_node',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-nd-oper',
            'bundle-nodes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-nd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper'
        ),
    },
    'Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces.BundleInterface.NdParameters' : {
        'meta_info' : _MetaInfoClass('Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces.BundleInterface.NdParameters',
            False, 
            [
            _MetaInfoClassMember('complete-glean-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Completed GLEAN entry count
                ''',
                'complete_glean_count',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            _MetaInfoClassMember('complete-protocol-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Completed PROTO entry Count
                ''',
                'complete_protocol_count',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            _MetaInfoClassMember('dad-attempts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                DAD attempt count
                ''',
                'dad_attempts',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            _MetaInfoClassMember('dropped-glean-req-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Dropped GLEAN entry lequest count
                ''',
                'dropped_glean_req_count',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            _MetaInfoClassMember('dropped-protocol-req-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Dropped PROTO entry request count
                ''',
                'dropped_protocol_req_count',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            _MetaInfoClassMember('incomplete-glean-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Incomplete GLEAN entry count
                ''',
                'incomplete_glean_count',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            _MetaInfoClassMember('incomplete-protocol-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Incomplete PROTO entry count
                ''',
                'incomplete_protocol_count',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            _MetaInfoClassMember('is-dad-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If true, DAD (D.. A.. D..) is enabled otherwise
                it is disabled
                ''',
                'is_dad_enabled',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            _MetaInfoClassMember('is-dhcp-managed', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Flag used for utilising DHCP
                ''',
                'is_dhcp_managed',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            _MetaInfoClassMember('is-icm-pv6-redirect', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                ICMP redirect flag
                ''',
                'is_icm_pv6_redirect',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            _MetaInfoClassMember('is-route-address-managed', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Flag used to manage routable address
                ''',
                'is_route_address_managed',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            _MetaInfoClassMember('is-suppressed', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Suppress flag
                ''',
                'is_suppressed',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            _MetaInfoClassMember('nd-advertisement-lifetime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ND router advertisement life time in sec
                ''',
                'nd_advertisement_lifetime',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            _MetaInfoClassMember('nd-cache-limit', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Completed adjacency limit per interface
                ''',
                'nd_cache_limit',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            _MetaInfoClassMember('nd-max-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ND router advertisement maximum transmit
                interval in sec
                ''',
                'nd_max_transmit_interval',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            _MetaInfoClassMember('nd-min-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ND router advertisement minimum transmit
                interval in sec
                ''',
                'nd_min_transmit_interval',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            _MetaInfoClassMember('nd-reachable-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Time to reach ND in msec
                ''',
                'nd_reachable_time',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            _MetaInfoClassMember('nd-retransmit-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ND retransmit interval in msec
                ''',
                'nd_retransmit_interval',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            _MetaInfoClassMember('send-unicast-ra', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                unicast RA send flag
                ''',
                'send_unicast_ra',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-nd-oper',
            'nd-parameters',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-nd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper'
        ),
    },
    'Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces.BundleInterface.LocalAddress' : {
        'meta_info' : _MetaInfoClass('Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces.BundleInterface.LocalAddress',
            False, 
            [
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address
                ''',
                'ipv6_address',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-nd-oper',
            'local-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-nd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper'
        ),
    },
    'Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces.BundleInterface.GlobalAddress' : {
        'meta_info' : _MetaInfoClass('Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces.BundleInterface.GlobalAddress',
            False, 
            [
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address
                ''',
                'ipv6_address',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-nd-oper',
            'global-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-nd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper'
        ),
    },
    'Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces.BundleInterface.MemberNode' : {
        'meta_info' : _MetaInfoClass('Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces.BundleInterface.MemberNode',
            False, 
            [
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Node Name
                ''',
                'node_name',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            _MetaInfoClassMember('total-links', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of links on the node
                ''',
                'total_links',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-nd-oper',
            'member-node',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-nd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper'
        ),
    },
    'Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces.BundleInterface' : {
        'meta_info' : _MetaInfoClass('Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces.BundleInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv6-nd-oper', True),
            _MetaInfoClassMember('etype', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                etype
                ''',
                'etype',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            _MetaInfoClassMember('global-address', REFERENCE_LIST, 'GlobalAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper', 'Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces.BundleInterface.GlobalAddress', 
                [], [], 
                '''                List of ND global addresses
                ''',
                'global_address',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            _MetaInfoClassMember('iftype', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Interface type
                ''',
                'iftype',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            _MetaInfoClassMember('is-interface-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If true, interface is enabled
                ''',
                'is_interface_enabled',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            _MetaInfoClassMember('is-ipv6-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If true, IPv6 is enabled
                ''',
                'is_ipv6_enabled',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            _MetaInfoClassMember('is-mpls-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If true, MPLS is enabled
                ''',
                'is_mpls_enabled',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            _MetaInfoClassMember('local-address', REFERENCE_CLASS, 'LocalAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper', 'Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces.BundleInterface.LocalAddress', 
                [], [], 
                '''                Link local address
                ''',
                'local_address',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            _MetaInfoClassMember('mac-addr', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                mac address
                ''',
                'mac_addr',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            _MetaInfoClassMember('mac-addr-size', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                mac address size
                ''',
                'mac_addr_size',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            _MetaInfoClassMember('member-link', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                List of member links
                ''',
                'member_link',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            _MetaInfoClassMember('member-node', REFERENCE_LIST, 'MemberNode' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper', 'Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces.BundleInterface.MemberNode', 
                [], [], 
                '''                List of member nodes
                ''',
                'member_node',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            _MetaInfoClassMember('mtu', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                MTU
                ''',
                'mtu',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            _MetaInfoClassMember('nd-parameters', REFERENCE_CLASS, 'NdParameters' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper', 'Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces.BundleInterface.NdParameters', 
                [], [], 
                '''                ND interface parameters
                ''',
                'nd_parameters',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            _MetaInfoClassMember('parent-interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Parent interface name
                ''',
                'parent_interface_name',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            _MetaInfoClassMember('vlan-tag', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                vlan tag/id/ucv
                ''',
                'vlan_tag',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-nd-oper',
            'bundle-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-nd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper'
        ),
    },
    'Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces' : {
        'meta_info' : _MetaInfoClass('Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces',
            False, 
            [
            _MetaInfoClassMember('bundle-interface', REFERENCE_LIST, 'BundleInterface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper', 'Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces.BundleInterface', 
                [], [], 
                '''                IPv6 ND operational data for a specific
                bundler interface
                ''',
                'bundle_interface',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-nd-oper',
            'bundle-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-nd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper'
        ),
    },
    'Ipv6NodeDiscovery.Nodes.Node.Interfaces.Interface' : {
        'meta_info' : _MetaInfoClass('Ipv6NodeDiscovery.Nodes.Node.Interfaces.Interface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv6-nd-oper', True),
            _MetaInfoClassMember('complete-glean-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Completed GLEAN entry count
                ''',
                'complete_glean_count',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            _MetaInfoClassMember('complete-protocol-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Completed PROTO entry Count
                ''',
                'complete_protocol_count',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            _MetaInfoClassMember('dad-attempts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                DAD attempt count
                ''',
                'dad_attempts',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            _MetaInfoClassMember('dropped-glean-req-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Dropped GLEAN entry lequest count
                ''',
                'dropped_glean_req_count',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            _MetaInfoClassMember('dropped-protocol-req-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Dropped PROTO entry request count
                ''',
                'dropped_protocol_req_count',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            _MetaInfoClassMember('incomplete-glean-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Incomplete GLEAN entry count
                ''',
                'incomplete_glean_count',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            _MetaInfoClassMember('incomplete-protocol-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Incomplete PROTO entry count
                ''',
                'incomplete_protocol_count',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            _MetaInfoClassMember('is-dad-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If true, DAD (D.. A.. D..) is enabled otherwise
                it is disabled
                ''',
                'is_dad_enabled',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            _MetaInfoClassMember('is-dhcp-managed', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Flag used for utilising DHCP
                ''',
                'is_dhcp_managed',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            _MetaInfoClassMember('is-icm-pv6-redirect', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                ICMP redirect flag
                ''',
                'is_icm_pv6_redirect',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            _MetaInfoClassMember('is-route-address-managed', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Flag used to manage routable address
                ''',
                'is_route_address_managed',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            _MetaInfoClassMember('is-suppressed', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Suppress flag
                ''',
                'is_suppressed',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            _MetaInfoClassMember('nd-advertisement-lifetime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ND router advertisement life time in sec
                ''',
                'nd_advertisement_lifetime',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            _MetaInfoClassMember('nd-cache-limit', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Completed adjacency limit per interface
                ''',
                'nd_cache_limit',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            _MetaInfoClassMember('nd-max-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ND router advertisement maximum transmit
                interval in sec
                ''',
                'nd_max_transmit_interval',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            _MetaInfoClassMember('nd-min-transmit-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ND router advertisement minimum transmit
                interval in sec
                ''',
                'nd_min_transmit_interval',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            _MetaInfoClassMember('nd-reachable-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Time to reach ND in msec
                ''',
                'nd_reachable_time',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            _MetaInfoClassMember('nd-retransmit-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ND retransmit interval in msec
                ''',
                'nd_retransmit_interval',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            _MetaInfoClassMember('send-unicast-ra', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                unicast RA send flag
                ''',
                'send_unicast_ra',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-nd-oper',
            'interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-nd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper'
        ),
    },
    'Ipv6NodeDiscovery.Nodes.Node.Interfaces' : {
        'meta_info' : _MetaInfoClass('Ipv6NodeDiscovery.Nodes.Node.Interfaces',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper', 'Ipv6NodeDiscovery.Nodes.Node.Interfaces.Interface', 
                [], [], 
                '''                IPv6  node discovery operational data for a
                specific node and interface
                ''',
                'interface',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-nd-oper',
            'interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-nd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper'
        ),
    },
    'Ipv6NodeDiscovery.Nodes.Node.NdVirtualRouters.NdVirtualRouter.LocalAddress' : {
        'meta_info' : _MetaInfoClass('Ipv6NodeDiscovery.Nodes.Node.NdVirtualRouters.NdVirtualRouter.LocalAddress',
            False, 
            [
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address
                ''',
                'ipv6_address',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-nd-oper',
            'local-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-nd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper'
        ),
    },
    'Ipv6NodeDiscovery.Nodes.Node.NdVirtualRouters.NdVirtualRouter.VrGlobalAddress' : {
        'meta_info' : _MetaInfoClass('Ipv6NodeDiscovery.Nodes.Node.NdVirtualRouters.NdVirtualRouter.VrGlobalAddress',
            False, 
            [
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address
                ''',
                'ipv6_address',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-nd-oper',
            'vr-global-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-nd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper'
        ),
    },
    'Ipv6NodeDiscovery.Nodes.Node.NdVirtualRouters.NdVirtualRouter' : {
        'meta_info' : _MetaInfoClass('Ipv6NodeDiscovery.Nodes.Node.NdVirtualRouters.NdVirtualRouter',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv6-nd-oper', True),
            _MetaInfoClassMember('context', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Virtual Router ID
                ''',
                'context',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            _MetaInfoClassMember('flags', REFERENCE_ENUM_CLASS, 'Ipv6NdShVrFlagsEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper', 'Ipv6NdShVrFlagsEnum', 
                [], [], 
                '''                VR Flags
                ''',
                'flags',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            _MetaInfoClassMember('link-layer-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                Link-Layer Address
                ''',
                'link_layer_address',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            _MetaInfoClassMember('local-address', REFERENCE_CLASS, 'LocalAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper', 'Ipv6NodeDiscovery.Nodes.Node.NdVirtualRouters.NdVirtualRouter.LocalAddress', 
                [], [], 
                '''                Link local address
                ''',
                'local_address',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'Ipv6NdShVrStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper', 'Ipv6NdShVrStateEnum', 
                [], [], 
                '''                VR state
                ''',
                'state',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            _MetaInfoClassMember('vr-gl-addr-ct', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Virtual Global Address Count
                ''',
                'vr_gl_addr_ct',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            _MetaInfoClassMember('vr-global-address', REFERENCE_LIST, 'VrGlobalAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper', 'Ipv6NodeDiscovery.Nodes.Node.NdVirtualRouters.NdVirtualRouter.VrGlobalAddress', 
                [], [], 
                '''                List of ND global addresses
                ''',
                'vr_global_address',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-nd-oper',
            'nd-virtual-router',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-nd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper'
        ),
    },
    'Ipv6NodeDiscovery.Nodes.Node.NdVirtualRouters' : {
        'meta_info' : _MetaInfoClass('Ipv6NodeDiscovery.Nodes.Node.NdVirtualRouters',
            False, 
            [
            _MetaInfoClassMember('nd-virtual-router', REFERENCE_LIST, 'NdVirtualRouter' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper', 'Ipv6NodeDiscovery.Nodes.Node.NdVirtualRouters.NdVirtualRouter', 
                [], [], 
                '''                IPv6 ND virtual  router operational data for
                a specific interface
                ''',
                'nd_virtual_router',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-nd-oper',
            'nd-virtual-routers',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-nd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper'
        ),
    },
    'Ipv6NodeDiscovery.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('Ipv6NodeDiscovery.Nodes.Node',
            False, 
            [
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                The node name
                ''',
                'node_name',
                'Cisco-IOS-XR-ipv6-nd-oper', True),
            _MetaInfoClassMember('bundle-interfaces', REFERENCE_CLASS, 'BundleInterfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper', 'Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces', 
                [], [], 
                '''                IPv6 ND list of bundle interfaces for a
                specific node
                ''',
                'bundle_interfaces',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            _MetaInfoClassMember('bundle-nodes', REFERENCE_CLASS, 'BundleNodes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper', 'Ipv6NodeDiscovery.Nodes.Node.BundleNodes', 
                [], [], 
                '''                IPv6 ND list of bundle nodes for a specific
                node
                ''',
                'bundle_nodes',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper', 'Ipv6NodeDiscovery.Nodes.Node.Interfaces', 
                [], [], 
                '''                IPv6 node discovery list of interfaces for a
                specific node
                ''',
                'interfaces',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            _MetaInfoClassMember('nd-virtual-routers', REFERENCE_CLASS, 'NdVirtualRouters' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper', 'Ipv6NodeDiscovery.Nodes.Node.NdVirtualRouters', 
                [], [], 
                '''                IPv6 ND virtual router information for a
                specific interface
                ''',
                'nd_virtual_routers',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            _MetaInfoClassMember('neighbor-interfaces', REFERENCE_CLASS, 'NeighborInterfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper', 'Ipv6NodeDiscovery.Nodes.Node.NeighborInterfaces', 
                [], [], 
                '''                IPv6 node discovery list of neighbor
                interfaces
                ''',
                'neighbor_interfaces',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            _MetaInfoClassMember('neighbor-summary', REFERENCE_CLASS, 'NeighborSummary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper', 'Ipv6NodeDiscovery.Nodes.Node.NeighborSummary', 
                [], [], 
                '''                IPv6 Neighbor summary
                ''',
                'neighbor_summary',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-nd-oper',
            'node',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-nd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper'
        ),
    },
    'Ipv6NodeDiscovery.Nodes' : {
        'meta_info' : _MetaInfoClass('Ipv6NodeDiscovery.Nodes',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper', 'Ipv6NodeDiscovery.Nodes.Node', 
                [], [], 
                '''                IPv6 node discovery operational data for a
                particular node
                ''',
                'node',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-nd-oper',
            'nodes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-nd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper'
        ),
    },
    'Ipv6NodeDiscovery' : {
        'meta_info' : _MetaInfoClass('Ipv6NodeDiscovery',
            False, 
            [
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper', 'Ipv6NodeDiscovery.Nodes', 
                [], [], 
                '''                IPv6 node discovery list of nodes
                ''',
                'nodes',
                'Cisco-IOS-XR-ipv6-nd-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-nd-oper',
            'ipv6-node-discovery',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-nd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_oper'
        ),
    },
}
_meta_table['Ipv6NodeDiscovery.Nodes.Node.NeighborInterfaces.NeighborInterface.HostAddresses.HostAddress.LastReachedTime']['meta_info'].parent =_meta_table['Ipv6NodeDiscovery.Nodes.Node.NeighborInterfaces.NeighborInterface.HostAddresses.HostAddress']['meta_info']
_meta_table['Ipv6NodeDiscovery.Nodes.Node.NeighborInterfaces.NeighborInterface.HostAddresses.HostAddress']['meta_info'].parent =_meta_table['Ipv6NodeDiscovery.Nodes.Node.NeighborInterfaces.NeighborInterface.HostAddresses']['meta_info']
_meta_table['Ipv6NodeDiscovery.Nodes.Node.NeighborInterfaces.NeighborInterface.HostAddresses']['meta_info'].parent =_meta_table['Ipv6NodeDiscovery.Nodes.Node.NeighborInterfaces.NeighborInterface']['meta_info']
_meta_table['Ipv6NodeDiscovery.Nodes.Node.NeighborInterfaces.NeighborInterface']['meta_info'].parent =_meta_table['Ipv6NodeDiscovery.Nodes.Node.NeighborInterfaces']['meta_info']
_meta_table['Ipv6NodeDiscovery.Nodes.Node.NeighborSummary.Multicast']['meta_info'].parent =_meta_table['Ipv6NodeDiscovery.Nodes.Node.NeighborSummary']['meta_info']
_meta_table['Ipv6NodeDiscovery.Nodes.Node.NeighborSummary.Static']['meta_info'].parent =_meta_table['Ipv6NodeDiscovery.Nodes.Node.NeighborSummary']['meta_info']
_meta_table['Ipv6NodeDiscovery.Nodes.Node.NeighborSummary.Dynamic']['meta_info'].parent =_meta_table['Ipv6NodeDiscovery.Nodes.Node.NeighborSummary']['meta_info']
_meta_table['Ipv6NodeDiscovery.Nodes.Node.BundleNodes.BundleNode.Age']['meta_info'].parent =_meta_table['Ipv6NodeDiscovery.Nodes.Node.BundleNodes.BundleNode']['meta_info']
_meta_table['Ipv6NodeDiscovery.Nodes.Node.BundleNodes.BundleNode']['meta_info'].parent =_meta_table['Ipv6NodeDiscovery.Nodes.Node.BundleNodes']['meta_info']
_meta_table['Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces.BundleInterface.NdParameters']['meta_info'].parent =_meta_table['Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces.BundleInterface']['meta_info']
_meta_table['Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces.BundleInterface.LocalAddress']['meta_info'].parent =_meta_table['Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces.BundleInterface']['meta_info']
_meta_table['Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces.BundleInterface.GlobalAddress']['meta_info'].parent =_meta_table['Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces.BundleInterface']['meta_info']
_meta_table['Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces.BundleInterface.MemberNode']['meta_info'].parent =_meta_table['Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces.BundleInterface']['meta_info']
_meta_table['Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces.BundleInterface']['meta_info'].parent =_meta_table['Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces']['meta_info']
_meta_table['Ipv6NodeDiscovery.Nodes.Node.Interfaces.Interface']['meta_info'].parent =_meta_table['Ipv6NodeDiscovery.Nodes.Node.Interfaces']['meta_info']
_meta_table['Ipv6NodeDiscovery.Nodes.Node.NdVirtualRouters.NdVirtualRouter.LocalAddress']['meta_info'].parent =_meta_table['Ipv6NodeDiscovery.Nodes.Node.NdVirtualRouters.NdVirtualRouter']['meta_info']
_meta_table['Ipv6NodeDiscovery.Nodes.Node.NdVirtualRouters.NdVirtualRouter.VrGlobalAddress']['meta_info'].parent =_meta_table['Ipv6NodeDiscovery.Nodes.Node.NdVirtualRouters.NdVirtualRouter']['meta_info']
_meta_table['Ipv6NodeDiscovery.Nodes.Node.NdVirtualRouters.NdVirtualRouter']['meta_info'].parent =_meta_table['Ipv6NodeDiscovery.Nodes.Node.NdVirtualRouters']['meta_info']
_meta_table['Ipv6NodeDiscovery.Nodes.Node.NeighborInterfaces']['meta_info'].parent =_meta_table['Ipv6NodeDiscovery.Nodes.Node']['meta_info']
_meta_table['Ipv6NodeDiscovery.Nodes.Node.NeighborSummary']['meta_info'].parent =_meta_table['Ipv6NodeDiscovery.Nodes.Node']['meta_info']
_meta_table['Ipv6NodeDiscovery.Nodes.Node.BundleNodes']['meta_info'].parent =_meta_table['Ipv6NodeDiscovery.Nodes.Node']['meta_info']
_meta_table['Ipv6NodeDiscovery.Nodes.Node.BundleInterfaces']['meta_info'].parent =_meta_table['Ipv6NodeDiscovery.Nodes.Node']['meta_info']
_meta_table['Ipv6NodeDiscovery.Nodes.Node.Interfaces']['meta_info'].parent =_meta_table['Ipv6NodeDiscovery.Nodes.Node']['meta_info']
_meta_table['Ipv6NodeDiscovery.Nodes.Node.NdVirtualRouters']['meta_info'].parent =_meta_table['Ipv6NodeDiscovery.Nodes.Node']['meta_info']
_meta_table['Ipv6NodeDiscovery.Nodes.Node']['meta_info'].parent =_meta_table['Ipv6NodeDiscovery.Nodes']['meta_info']
_meta_table['Ipv6NodeDiscovery.Nodes']['meta_info'].parent =_meta_table['Ipv6NodeDiscovery']['meta_info']
