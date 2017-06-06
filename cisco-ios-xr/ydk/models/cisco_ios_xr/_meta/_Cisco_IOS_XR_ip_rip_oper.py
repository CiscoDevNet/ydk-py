


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'InterfaceStateEnum' : _MetaInfoEnum('InterfaceStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper',
        {
            'interface-none':'interface_none',
            'interface-down':'interface_down',
            'interface-up':'interface_up',
            'interface-unknown':'interface_unknown',
        }, 'Cisco-IOS-XR-ip-rip-oper', _yang_ns._namespaces['Cisco-IOS-XR-ip-rip-oper']),
    'RipRouteOriginEnum' : _MetaInfoEnum('RipRouteOriginEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper',
        {
            'rip-rt-org-runover':'rip_rt_org_runover',
            'rip-rt-org-redist':'rip_rt_org_redist',
            'rip-rt-org-auto-summary':'rip_rt_org_auto_summary',
            'rip-rt-org-rip':'rip_rt_org_rip',
            'rip-rt-org-intsummary':'rip_rt_org_intsummary',
            'rip-rt-org-unused':'rip_rt_org_unused',
        }, 'Cisco-IOS-XR-ip-rip-oper', _yang_ns._namespaces['Cisco-IOS-XR-ip-rip-oper']),
    'Rip.Vrfs.Vrf.Routes.Route.Paths' : {
        'meta_info' : _MetaInfoClass('Rip.Vrfs.Vrf.Routes.Route.Paths',
            False, 
            [
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('is-permanent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Permanent indicator
                ''',
                'is_permanent',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('metric', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Metric
                ''',
                'metric',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('next-hop-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Next hop address
                ''',
                'next_hop_address',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Source address
                ''',
                'source_address',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('tag', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Tag
                ''',
                'tag',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('uptime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Up time
                ''',
                'uptime',
                'Cisco-IOS-XR-ip-rip-oper', False),
            ],
            'Cisco-IOS-XR-ip-rip-oper',
            'paths',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rip-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper'
        ),
    },
    'Rip.Vrfs.Vrf.Routes.Route' : {
        'meta_info' : _MetaInfoClass('Rip.Vrfs.Vrf.Routes.Route',
            False, 
            [
            _MetaInfoClassMember('active', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Active route indicator
                ''',
                'active',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('attributes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                RIB supplied route attributes
                ''',
                'attributes',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('bgp-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Hop count for this route
                ''',
                'bgp_count',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('destination-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Destination IP Address for this route
                ''',
                'destination_address',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('distance', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Route administrative distance
                ''',
                'distance',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('hold-down', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicates whether route is in holddown
                ''',
                'hold_down',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('path-origin', REFERENCE_ENUM_CLASS, 'RipRouteOriginEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper', 'RipRouteOriginEnum', 
                [], [], 
                '''                Where this route was learnt
                ''',
                'path_origin',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('paths', REFERENCE_LIST, 'Paths' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper', 'Rip.Vrfs.Vrf.Routes.Route.Paths', 
                [], [], 
                '''                The paths for this route
                ''',
                'paths',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Network prefix
                ''',
                'prefix',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '32')], [], 
                '''                Prefix length
                ''',
                'prefix_length',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('prefix-length-xr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Prefix length of IP address
                ''',
                'prefix_length_xr',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('route-summary', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Summary route placeholder indicator
                ''',
                'route_summary',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('route-tag', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Generic route information
                ''',
                'route_tag',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('route-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Type of this route
                ''',
                'route_type',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                RIB supplied version number
                ''',
                'version',
                'Cisco-IOS-XR-ip-rip-oper', False),
            ],
            'Cisco-IOS-XR-ip-rip-oper',
            'route',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rip-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper'
        ),
    },
    'Rip.Vrfs.Vrf.Routes' : {
        'meta_info' : _MetaInfoClass('Rip.Vrfs.Vrf.Routes',
            False, 
            [
            _MetaInfoClassMember('route', REFERENCE_LIST, 'Route' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper', 'Rip.Vrfs.Vrf.Routes.Route', 
                [], [], 
                '''                A route in the RIP database
                ''',
                'route',
                'Cisco-IOS-XR-ip-rip-oper', False),
            ],
            'Cisco-IOS-XR-ip-rip-oper',
            'routes',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rip-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper'
        ),
    },
    'Rip.Vrfs.Vrf.Configuration' : {
        'meta_info' : _MetaInfoClass('Rip.Vrfs.Vrf.Configuration',
            False, 
            [
            _MetaInfoClassMember('active', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                VRF active indicator
                ''',
                'active',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('auto-summarize', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Auto-summarization indicator
                ''',
                'auto_summarize',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('default-metric', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Default metric for RIP routes
                ''',
                'default_metric',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('flash-threshold', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Flash update threshold
                ''',
                'flash_threshold',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('flush-timer', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Flush timer
                ''',
                'flush_timer',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('hold-down-timer', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Holddown timer
                ''',
                'hold_down_timer',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('input-q-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Length of the input queue
                ''',
                'input_q_length',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('invalid-timer', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Invalid timer
                ''',
                'invalid_timer',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('maximum-paths', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Maximum number of paths a route can have
                ''',
                'maximum_paths',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('multicast-address', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Use broadcast/multicast address indicator
                ''',
                'multicast_address',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('next-update-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Time left for next update
                ''',
                'next_update_time',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('nsf-life-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                NSF life time
                ''',
                'nsf_life_time',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('nsf-status', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                NSF Enable status
                ''',
                'nsf_status',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('oom-flags', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Out-of-memory status flags
                ''',
                'oom_flags',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('rip-version', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Version of RIP configured
                ''',
                'rip_version',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('triggered-rip', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Triggered RIP enabled indicator
                ''',
                'triggered_rip',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('update-timer', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Update timer
                ''',
                'update_timer',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('validation-indicator', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Incoming packet source validation indicator
                ''',
                'validation_indicator',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('vr-fised-socket', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                VRF added to socket indicator
                ''',
                'vr_fised_socket',
                'Cisco-IOS-XR-ip-rip-oper', False),
            ],
            'Cisco-IOS-XR-ip-rip-oper',
            'configuration',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rip-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper'
        ),
    },
    'Rip.Vrfs.Vrf.Statistics' : {
        'meta_info' : _MetaInfoClass('Rip.Vrfs.Vrf.Statistics',
            False, 
            [
            _MetaInfoClassMember('discarded-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total discarded packets
                ''',
                'discarded_packets',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('discarded-routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total discarded routes
                ''',
                'discarded_routes',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('path-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of paths allocated
                ''',
                'path_count',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('path-malloc-failures', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of failures to allocate memory for a path
                ''',
                'path_malloc_failures',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('periodic-updates', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of periodic RIP updates
                ''',
                'periodic_updates',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('query-responses', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of RIP queries responded to
                ''',
                'query_responses',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total packets received
                ''',
                'received_packets',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('rib-updates', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of route updates to RIB made by RIP
                ''',
                'rib_updates',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('route-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of routes allocated
                ''',
                'route_count',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('route-malloc-failures', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of failures to allocate memory for a
                route
                ''',
                'route_malloc_failures',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('sent-message-failures', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of message send failures
                ''',
                'sent_message_failures',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('sent-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of messages sent
                ''',
                'sent_messages',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('standby-packets-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Packets rx in SRP
                ''',
                'standby_packets_received',
                'Cisco-IOS-XR-ip-rip-oper', False),
            ],
            'Cisco-IOS-XR-ip-rip-oper',
            'statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rip-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper'
        ),
    },
    'Rip.Vrfs.Vrf.Interfaces.Interface.RipSummary' : {
        'meta_info' : _MetaInfoClass('Rip.Vrfs.Vrf.Interfaces.Interface.RipSummary',
            False, 
            [
            _MetaInfoClassMember('metric', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Summary metric
                ''',
                'metric',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('next-hop-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Summary address next hop
                ''',
                'next_hop_address',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Summary address prefix
                ''',
                'prefix',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Summary address prefix length
                ''',
                'prefix_length',
                'Cisco-IOS-XR-ip-rip-oper', False),
            ],
            'Cisco-IOS-XR-ip-rip-oper',
            'rip-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rip-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper'
        ),
    },
    'Rip.Vrfs.Vrf.Interfaces.Interface.RipPeer' : {
        'meta_info' : _MetaInfoClass('Rip.Vrfs.Vrf.Interfaces.Interface.RipPeer',
            False, 
            [
            _MetaInfoClassMember('discarded-peer-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Discarded packets from this peer
                ''',
                'discarded_peer_packets',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('discarded-peer-routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Discarded routes from this peer
                ''',
                'discarded_peer_routes',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('peer-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IP Address of this peer
                ''',
                'peer_address',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('peer-uptime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Uptime of this peer
                ''',
                'peer_uptime',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('peer-version', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                RIP version for this peer
                ''',
                'peer_version',
                'Cisco-IOS-XR-ip-rip-oper', False),
            ],
            'Cisco-IOS-XR-ip-rip-oper',
            'rip-peer',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rip-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper'
        ),
    },
    'Rip.Vrfs.Vrf.Interfaces.Interface' : {
        'meta_info' : _MetaInfoClass('Rip.Vrfs.Vrf.Interfaces.Interface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ip-rip-oper', True),
            _MetaInfoClassMember('accept-metric', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Accept routes of metric 0 indicator
                ''',
                'accept_metric',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('auth-key-md5', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Authentication key programmed with MD5 algorithm
                ''',
                'auth_key_md5',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('auth-key-send-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Current active Send Authentication Key Id
                ''',
                'auth_key_send_id',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('auth-keychain', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Authentication Keychain Name
                ''',
                'auth_keychain',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('auth-mode', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Authentication Mode
                ''',
                'auth_mode',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('destination-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IP Address of this interface
                ''',
                'destination_address',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('if-handle', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface handle
                ''',
                'if_handle',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Interface name
                ''',
                'interface',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('is-passive-interface', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Passive interface indicator
                ''',
                'is_passive_interface',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('join-status', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Multicast group join status
                ''',
                'join_status',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('lpts-state', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                LPTSState
                ''',
                'lpts_state',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('metric-cost', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Cost added to routes through this interface
                ''',
                'metric_cost',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('multicast-address', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Use broadcast address for v2 packets
                ''',
                'multicast_address',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Interface's triggered RIP neighbor
                ''',
                'neighbor_address',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('oom-flags', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Out-of-memory status flags
                ''',
                'oom_flags',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('pkt-accepted-valid-auth', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Packets accepted with valid authentication data
                ''',
                'pkt_accepted_valid_auth',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('pkt-drop-invalid-auth', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Packets dropped due to invalid authentication
                data
                ''',
                'pkt_drop_invalid_auth',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('pkt-drop-no-auth', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Packets dropped due to missing authentication
                data
                ''',
                'pkt_drop_no_auth',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('pkt-drop-wrong-kc', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Packets dropped due to wrong keychain configured
                ''',
                'pkt_drop_wrong_kc',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('poison-horizon', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Poisoned reverse enabled indicator
                ''',
                'poison_horizon',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Prefix length of the IP address
                ''',
                'prefix_length',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('receive-version', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Versions that the interface will recieve
                ''',
                'receive_version',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('rip-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Whether RIP is enabled on this interface
                ''',
                'rip_enabled',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('rip-peer', REFERENCE_LIST, 'RipPeer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper', 'Rip.Vrfs.Vrf.Interfaces.Interface.RipPeer', 
                [], [], 
                '''                Neighbors on this interface
                ''',
                'rip_peer',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('rip-summary', REFERENCE_LIST, 'RipSummary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper', 'Rip.Vrfs.Vrf.Interfaces.Interface.RipSummary', 
                [], [], 
                '''                User defined summary addresses
                ''',
                'rip_summary',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('send-auth-key-exists', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Authentication send key exists
                ''',
                'send_auth_key_exists',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('send-version', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Versions that the interface is sending
                ''',
                'send_version',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('split-horizon', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Split horizon enabled indicator
                ''',
                'split_horizon',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'InterfaceStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper', 'InterfaceStateEnum', 
                [], [], 
                '''                Current state of the interface
                ''',
                'state',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('total-pkt-recvd', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total packets received
                ''',
                'total_pkt_recvd',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('triggered-rip', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Triggered RIP enabled indicator
                ''',
                'triggered_rip',
                'Cisco-IOS-XR-ip-rip-oper', False),
            ],
            'Cisco-IOS-XR-ip-rip-oper',
            'interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rip-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper'
        ),
    },
    'Rip.Vrfs.Vrf.Interfaces' : {
        'meta_info' : _MetaInfoClass('Rip.Vrfs.Vrf.Interfaces',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper', 'Rip.Vrfs.Vrf.Interfaces.Interface', 
                [], [], 
                '''                Information about a particular RIP interface
                ''',
                'interface',
                'Cisco-IOS-XR-ip-rip-oper', False),
            ],
            'Cisco-IOS-XR-ip-rip-oper',
            'interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rip-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper'
        ),
    },
    'Rip.Vrfs.Vrf.Global_.VrfSummary' : {
        'meta_info' : _MetaInfoClass('Rip.Vrfs.Vrf.Global_.VrfSummary',
            False, 
            [
            _MetaInfoClassMember('active', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                VRF Active indicator
                ''',
                'active',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('active-interface-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of active interfaces
                ''',
                'active_interface_count',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('flush-timer', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Flush timer
                ''',
                'flush_timer',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('hold-down-timer', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Holddown timer
                ''',
                'hold_down_timer',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('interface-configured-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of interfaces configured
                ''',
                'interface_configured_count',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('invalid-timer', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Invalid timer
                ''',
                'invalid_timer',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('next-update-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Time left for next update
                ''',
                'next_update_time',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('oom-flags', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Current OOM flags
                ''',
                'oom_flags',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('path-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of paths allocated
                ''',
                'path_count',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('route-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of routes allocated
                ''',
                'route_count',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('update-timer', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Update timer
                ''',
                'update_timer',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                VRF Name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ip-rip-oper', False),
            ],
            'Cisco-IOS-XR-ip-rip-oper',
            'vrf-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rip-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper'
        ),
    },
    'Rip.Vrfs.Vrf.Global_.InterfaceSummary' : {
        'meta_info' : _MetaInfoClass('Rip.Vrfs.Vrf.Global_.InterfaceSummary',
            False, 
            [
            _MetaInfoClassMember('destination-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IP address
                ''',
                'destination_address',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                RIP enabled indicator
                ''',
                'enabled',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Interface name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('neighbor-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of neighbors seen
                ''',
                'neighbor_count',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('oom-flags', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Current OOM flags
                ''',
                'oom_flags',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Prefix length of IP address
                ''',
                'prefix_length',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('receive-version', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                RIP versions this interface will receive
                ''',
                'receive_version',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('send-version', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                RIP versions this interface sends out
                ''',
                'send_version',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'InterfaceStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper', 'InterfaceStateEnum', 
                [], [], 
                '''                Interface state
                ''',
                'state',
                'Cisco-IOS-XR-ip-rip-oper', False),
            ],
            'Cisco-IOS-XR-ip-rip-oper',
            'interface-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rip-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper'
        ),
    },
    'Rip.Vrfs.Vrf.Global_' : {
        'meta_info' : _MetaInfoClass('Rip.Vrfs.Vrf.Global_',
            False, 
            [
            _MetaInfoClassMember('interface-summary', REFERENCE_LIST, 'InterfaceSummary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper', 'Rip.Vrfs.Vrf.Global_.InterfaceSummary', 
                [], [], 
                '''                List of Interfaces configured
                ''',
                'interface_summary',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('vrf-summary', REFERENCE_CLASS, 'VrfSummary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper', 'Rip.Vrfs.Vrf.Global_.VrfSummary', 
                [], [], 
                '''                VRF summary data
                ''',
                'vrf_summary',
                'Cisco-IOS-XR-ip-rip-oper', False),
            ],
            'Cisco-IOS-XR-ip-rip-oper',
            'global',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rip-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper'
        ),
    },
    'Rip.Vrfs.Vrf' : {
        'meta_info' : _MetaInfoClass('Rip.Vrfs.Vrf',
            False, 
            [
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Name of the VRF
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ip-rip-oper', True),
            _MetaInfoClassMember('configuration', REFERENCE_CLASS, 'Configuration' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper', 'Rip.Vrfs.Vrf.Configuration', 
                [], [], 
                '''                RIP global configuration
                ''',
                'configuration',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('global', REFERENCE_CLASS, 'Global_' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper', 'Rip.Vrfs.Vrf.Global_', 
                [], [], 
                '''                Global Information 
                ''',
                'global_',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper', 'Rip.Vrfs.Vrf.Interfaces', 
                [], [], 
                '''                RIP interfaces
                ''',
                'interfaces',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('routes', REFERENCE_CLASS, 'Routes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper', 'Rip.Vrfs.Vrf.Routes', 
                [], [], 
                '''                RIP route database
                ''',
                'routes',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('statistics', REFERENCE_CLASS, 'Statistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper', 'Rip.Vrfs.Vrf.Statistics', 
                [], [], 
                '''                RIP statistics information
                ''',
                'statistics',
                'Cisco-IOS-XR-ip-rip-oper', False),
            ],
            'Cisco-IOS-XR-ip-rip-oper',
            'vrf',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rip-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper'
        ),
    },
    'Rip.Vrfs' : {
        'meta_info' : _MetaInfoClass('Rip.Vrfs',
            False, 
            [
            _MetaInfoClassMember('vrf', REFERENCE_LIST, 'Vrf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper', 'Rip.Vrfs.Vrf', 
                [], [], 
                '''                Operational data for a particular VRF
                ''',
                'vrf',
                'Cisco-IOS-XR-ip-rip-oper', False),
            ],
            'Cisco-IOS-XR-ip-rip-oper',
            'vrfs',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rip-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper'
        ),
    },
    'Rip.Protocol.Process.VrfSummary' : {
        'meta_info' : _MetaInfoClass('Rip.Protocol.Process.VrfSummary',
            False, 
            [
            _MetaInfoClassMember('active', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                VRF Active indicator
                ''',
                'active',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('active-interface-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of active interfaces
                ''',
                'active_interface_count',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('flush-timer', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Flush timer
                ''',
                'flush_timer',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('hold-down-timer', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Holddown timer
                ''',
                'hold_down_timer',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('interface-configured-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of interfaces configured
                ''',
                'interface_configured_count',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('invalid-timer', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Invalid timer
                ''',
                'invalid_timer',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('next-update-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Time left for next update
                ''',
                'next_update_time',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('oom-flags', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Current OOM flags
                ''',
                'oom_flags',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('path-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of paths allocated
                ''',
                'path_count',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('route-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of routes allocated
                ''',
                'route_count',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('update-timer', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Update timer
                ''',
                'update_timer',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                VRF Name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ip-rip-oper', False),
            ],
            'Cisco-IOS-XR-ip-rip-oper',
            'vrf-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rip-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper'
        ),
    },
    'Rip.Protocol.Process' : {
        'meta_info' : _MetaInfoClass('Rip.Protocol.Process',
            False, 
            [
            _MetaInfoClassMember('current-oom-state', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Current OOM state
                ''',
                'current_oom_state',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('path-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of paths allocated
                ''',
                'path_count',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('route-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of routes allocated
                ''',
                'route_count',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('socket-descriptor', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Socket descriptior
                ''',
                'socket_descriptor',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('vrf-active-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of active VRFs
                ''',
                'vrf_active_count',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('vrf-config-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of VRFs configured
                ''',
                'vrf_config_count',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('vrf-summary', REFERENCE_LIST, 'VrfSummary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper', 'Rip.Protocol.Process.VrfSummary', 
                [], [], 
                '''                List of VRFs configured
                ''',
                'vrf_summary',
                'Cisco-IOS-XR-ip-rip-oper', False),
            ],
            'Cisco-IOS-XR-ip-rip-oper',
            'process',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rip-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper'
        ),
    },
    'Rip.Protocol.DefaultVrf.Routes.Route.Paths' : {
        'meta_info' : _MetaInfoClass('Rip.Protocol.DefaultVrf.Routes.Route.Paths',
            False, 
            [
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('is-permanent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Permanent indicator
                ''',
                'is_permanent',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('metric', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Metric
                ''',
                'metric',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('next-hop-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Next hop address
                ''',
                'next_hop_address',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Source address
                ''',
                'source_address',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('tag', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Tag
                ''',
                'tag',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('uptime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Up time
                ''',
                'uptime',
                'Cisco-IOS-XR-ip-rip-oper', False),
            ],
            'Cisco-IOS-XR-ip-rip-oper',
            'paths',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rip-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper'
        ),
    },
    'Rip.Protocol.DefaultVrf.Routes.Route' : {
        'meta_info' : _MetaInfoClass('Rip.Protocol.DefaultVrf.Routes.Route',
            False, 
            [
            _MetaInfoClassMember('active', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Active route indicator
                ''',
                'active',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('attributes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                RIB supplied route attributes
                ''',
                'attributes',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('bgp-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Hop count for this route
                ''',
                'bgp_count',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('destination-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Destination IP Address for this route
                ''',
                'destination_address',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('distance', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Route administrative distance
                ''',
                'distance',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('hold-down', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicates whether route is in holddown
                ''',
                'hold_down',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('path-origin', REFERENCE_ENUM_CLASS, 'RipRouteOriginEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper', 'RipRouteOriginEnum', 
                [], [], 
                '''                Where this route was learnt
                ''',
                'path_origin',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('paths', REFERENCE_LIST, 'Paths' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper', 'Rip.Protocol.DefaultVrf.Routes.Route.Paths', 
                [], [], 
                '''                The paths for this route
                ''',
                'paths',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Network prefix
                ''',
                'prefix',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '32')], [], 
                '''                Prefix length
                ''',
                'prefix_length',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('prefix-length-xr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Prefix length of IP address
                ''',
                'prefix_length_xr',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('route-summary', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Summary route placeholder indicator
                ''',
                'route_summary',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('route-tag', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Generic route information
                ''',
                'route_tag',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('route-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Type of this route
                ''',
                'route_type',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                RIB supplied version number
                ''',
                'version',
                'Cisco-IOS-XR-ip-rip-oper', False),
            ],
            'Cisco-IOS-XR-ip-rip-oper',
            'route',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rip-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper'
        ),
    },
    'Rip.Protocol.DefaultVrf.Routes' : {
        'meta_info' : _MetaInfoClass('Rip.Protocol.DefaultVrf.Routes',
            False, 
            [
            _MetaInfoClassMember('route', REFERENCE_LIST, 'Route' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper', 'Rip.Protocol.DefaultVrf.Routes.Route', 
                [], [], 
                '''                A route in the RIP database
                ''',
                'route',
                'Cisco-IOS-XR-ip-rip-oper', False),
            ],
            'Cisco-IOS-XR-ip-rip-oper',
            'routes',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rip-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper'
        ),
    },
    'Rip.Protocol.DefaultVrf.Configuration' : {
        'meta_info' : _MetaInfoClass('Rip.Protocol.DefaultVrf.Configuration',
            False, 
            [
            _MetaInfoClassMember('active', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                VRF active indicator
                ''',
                'active',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('auto-summarize', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Auto-summarization indicator
                ''',
                'auto_summarize',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('default-metric', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Default metric for RIP routes
                ''',
                'default_metric',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('flash-threshold', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Flash update threshold
                ''',
                'flash_threshold',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('flush-timer', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Flush timer
                ''',
                'flush_timer',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('hold-down-timer', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Holddown timer
                ''',
                'hold_down_timer',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('input-q-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Length of the input queue
                ''',
                'input_q_length',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('invalid-timer', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Invalid timer
                ''',
                'invalid_timer',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('maximum-paths', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Maximum number of paths a route can have
                ''',
                'maximum_paths',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('multicast-address', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Use broadcast/multicast address indicator
                ''',
                'multicast_address',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('next-update-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Time left for next update
                ''',
                'next_update_time',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('nsf-life-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                NSF life time
                ''',
                'nsf_life_time',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('nsf-status', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                NSF Enable status
                ''',
                'nsf_status',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('oom-flags', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Out-of-memory status flags
                ''',
                'oom_flags',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('rip-version', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Version of RIP configured
                ''',
                'rip_version',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('triggered-rip', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Triggered RIP enabled indicator
                ''',
                'triggered_rip',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('update-timer', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Update timer
                ''',
                'update_timer',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('validation-indicator', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Incoming packet source validation indicator
                ''',
                'validation_indicator',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('vr-fised-socket', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                VRF added to socket indicator
                ''',
                'vr_fised_socket',
                'Cisco-IOS-XR-ip-rip-oper', False),
            ],
            'Cisco-IOS-XR-ip-rip-oper',
            'configuration',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rip-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper'
        ),
    },
    'Rip.Protocol.DefaultVrf.Statistics' : {
        'meta_info' : _MetaInfoClass('Rip.Protocol.DefaultVrf.Statistics',
            False, 
            [
            _MetaInfoClassMember('discarded-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total discarded packets
                ''',
                'discarded_packets',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('discarded-routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total discarded routes
                ''',
                'discarded_routes',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('path-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of paths allocated
                ''',
                'path_count',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('path-malloc-failures', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of failures to allocate memory for a path
                ''',
                'path_malloc_failures',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('periodic-updates', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of periodic RIP updates
                ''',
                'periodic_updates',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('query-responses', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of RIP queries responded to
                ''',
                'query_responses',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total packets received
                ''',
                'received_packets',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('rib-updates', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of route updates to RIB made by RIP
                ''',
                'rib_updates',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('route-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of routes allocated
                ''',
                'route_count',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('route-malloc-failures', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of failures to allocate memory for a
                route
                ''',
                'route_malloc_failures',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('sent-message-failures', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of message send failures
                ''',
                'sent_message_failures',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('sent-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of messages sent
                ''',
                'sent_messages',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('standby-packets-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Packets rx in SRP
                ''',
                'standby_packets_received',
                'Cisco-IOS-XR-ip-rip-oper', False),
            ],
            'Cisco-IOS-XR-ip-rip-oper',
            'statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rip-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper'
        ),
    },
    'Rip.Protocol.DefaultVrf.Interfaces.Interface.RipSummary' : {
        'meta_info' : _MetaInfoClass('Rip.Protocol.DefaultVrf.Interfaces.Interface.RipSummary',
            False, 
            [
            _MetaInfoClassMember('metric', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Summary metric
                ''',
                'metric',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('next-hop-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Summary address next hop
                ''',
                'next_hop_address',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Summary address prefix
                ''',
                'prefix',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Summary address prefix length
                ''',
                'prefix_length',
                'Cisco-IOS-XR-ip-rip-oper', False),
            ],
            'Cisco-IOS-XR-ip-rip-oper',
            'rip-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rip-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper'
        ),
    },
    'Rip.Protocol.DefaultVrf.Interfaces.Interface.RipPeer' : {
        'meta_info' : _MetaInfoClass('Rip.Protocol.DefaultVrf.Interfaces.Interface.RipPeer',
            False, 
            [
            _MetaInfoClassMember('discarded-peer-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Discarded packets from this peer
                ''',
                'discarded_peer_packets',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('discarded-peer-routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Discarded routes from this peer
                ''',
                'discarded_peer_routes',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('peer-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IP Address of this peer
                ''',
                'peer_address',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('peer-uptime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Uptime of this peer
                ''',
                'peer_uptime',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('peer-version', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                RIP version for this peer
                ''',
                'peer_version',
                'Cisco-IOS-XR-ip-rip-oper', False),
            ],
            'Cisco-IOS-XR-ip-rip-oper',
            'rip-peer',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rip-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper'
        ),
    },
    'Rip.Protocol.DefaultVrf.Interfaces.Interface' : {
        'meta_info' : _MetaInfoClass('Rip.Protocol.DefaultVrf.Interfaces.Interface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ip-rip-oper', True),
            _MetaInfoClassMember('accept-metric', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Accept routes of metric 0 indicator
                ''',
                'accept_metric',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('auth-key-md5', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Authentication key programmed with MD5 algorithm
                ''',
                'auth_key_md5',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('auth-key-send-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Current active Send Authentication Key Id
                ''',
                'auth_key_send_id',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('auth-keychain', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Authentication Keychain Name
                ''',
                'auth_keychain',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('auth-mode', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Authentication Mode
                ''',
                'auth_mode',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('destination-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IP Address of this interface
                ''',
                'destination_address',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('if-handle', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface handle
                ''',
                'if_handle',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Interface name
                ''',
                'interface',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('is-passive-interface', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Passive interface indicator
                ''',
                'is_passive_interface',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('join-status', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Multicast group join status
                ''',
                'join_status',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('lpts-state', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                LPTSState
                ''',
                'lpts_state',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('metric-cost', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Cost added to routes through this interface
                ''',
                'metric_cost',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('multicast-address', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Use broadcast address for v2 packets
                ''',
                'multicast_address',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Interface's triggered RIP neighbor
                ''',
                'neighbor_address',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('oom-flags', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Out-of-memory status flags
                ''',
                'oom_flags',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('pkt-accepted-valid-auth', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Packets accepted with valid authentication data
                ''',
                'pkt_accepted_valid_auth',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('pkt-drop-invalid-auth', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Packets dropped due to invalid authentication
                data
                ''',
                'pkt_drop_invalid_auth',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('pkt-drop-no-auth', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Packets dropped due to missing authentication
                data
                ''',
                'pkt_drop_no_auth',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('pkt-drop-wrong-kc', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Packets dropped due to wrong keychain configured
                ''',
                'pkt_drop_wrong_kc',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('poison-horizon', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Poisoned reverse enabled indicator
                ''',
                'poison_horizon',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Prefix length of the IP address
                ''',
                'prefix_length',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('receive-version', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Versions that the interface will recieve
                ''',
                'receive_version',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('rip-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Whether RIP is enabled on this interface
                ''',
                'rip_enabled',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('rip-peer', REFERENCE_LIST, 'RipPeer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper', 'Rip.Protocol.DefaultVrf.Interfaces.Interface.RipPeer', 
                [], [], 
                '''                Neighbors on this interface
                ''',
                'rip_peer',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('rip-summary', REFERENCE_LIST, 'RipSummary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper', 'Rip.Protocol.DefaultVrf.Interfaces.Interface.RipSummary', 
                [], [], 
                '''                User defined summary addresses
                ''',
                'rip_summary',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('send-auth-key-exists', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Authentication send key exists
                ''',
                'send_auth_key_exists',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('send-version', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Versions that the interface is sending
                ''',
                'send_version',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('split-horizon', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Split horizon enabled indicator
                ''',
                'split_horizon',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'InterfaceStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper', 'InterfaceStateEnum', 
                [], [], 
                '''                Current state of the interface
                ''',
                'state',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('total-pkt-recvd', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total packets received
                ''',
                'total_pkt_recvd',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('triggered-rip', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Triggered RIP enabled indicator
                ''',
                'triggered_rip',
                'Cisco-IOS-XR-ip-rip-oper', False),
            ],
            'Cisco-IOS-XR-ip-rip-oper',
            'interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rip-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper'
        ),
    },
    'Rip.Protocol.DefaultVrf.Interfaces' : {
        'meta_info' : _MetaInfoClass('Rip.Protocol.DefaultVrf.Interfaces',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper', 'Rip.Protocol.DefaultVrf.Interfaces.Interface', 
                [], [], 
                '''                Information about a particular RIP interface
                ''',
                'interface',
                'Cisco-IOS-XR-ip-rip-oper', False),
            ],
            'Cisco-IOS-XR-ip-rip-oper',
            'interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rip-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper'
        ),
    },
    'Rip.Protocol.DefaultVrf.Global_.VrfSummary' : {
        'meta_info' : _MetaInfoClass('Rip.Protocol.DefaultVrf.Global_.VrfSummary',
            False, 
            [
            _MetaInfoClassMember('active', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                VRF Active indicator
                ''',
                'active',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('active-interface-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of active interfaces
                ''',
                'active_interface_count',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('flush-timer', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Flush timer
                ''',
                'flush_timer',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('hold-down-timer', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Holddown timer
                ''',
                'hold_down_timer',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('interface-configured-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of interfaces configured
                ''',
                'interface_configured_count',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('invalid-timer', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Invalid timer
                ''',
                'invalid_timer',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('next-update-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Time left for next update
                ''',
                'next_update_time',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('oom-flags', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Current OOM flags
                ''',
                'oom_flags',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('path-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of paths allocated
                ''',
                'path_count',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('route-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of routes allocated
                ''',
                'route_count',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('update-timer', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Update timer
                ''',
                'update_timer',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                VRF Name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ip-rip-oper', False),
            ],
            'Cisco-IOS-XR-ip-rip-oper',
            'vrf-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rip-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper'
        ),
    },
    'Rip.Protocol.DefaultVrf.Global_.InterfaceSummary' : {
        'meta_info' : _MetaInfoClass('Rip.Protocol.DefaultVrf.Global_.InterfaceSummary',
            False, 
            [
            _MetaInfoClassMember('destination-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IP address
                ''',
                'destination_address',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                RIP enabled indicator
                ''',
                'enabled',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Interface name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('neighbor-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of neighbors seen
                ''',
                'neighbor_count',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('oom-flags', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Current OOM flags
                ''',
                'oom_flags',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Prefix length of IP address
                ''',
                'prefix_length',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('receive-version', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                RIP versions this interface will receive
                ''',
                'receive_version',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('send-version', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                RIP versions this interface sends out
                ''',
                'send_version',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'InterfaceStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper', 'InterfaceStateEnum', 
                [], [], 
                '''                Interface state
                ''',
                'state',
                'Cisco-IOS-XR-ip-rip-oper', False),
            ],
            'Cisco-IOS-XR-ip-rip-oper',
            'interface-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rip-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper'
        ),
    },
    'Rip.Protocol.DefaultVrf.Global_' : {
        'meta_info' : _MetaInfoClass('Rip.Protocol.DefaultVrf.Global_',
            False, 
            [
            _MetaInfoClassMember('interface-summary', REFERENCE_LIST, 'InterfaceSummary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper', 'Rip.Protocol.DefaultVrf.Global_.InterfaceSummary', 
                [], [], 
                '''                List of Interfaces configured
                ''',
                'interface_summary',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('vrf-summary', REFERENCE_CLASS, 'VrfSummary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper', 'Rip.Protocol.DefaultVrf.Global_.VrfSummary', 
                [], [], 
                '''                VRF summary data
                ''',
                'vrf_summary',
                'Cisco-IOS-XR-ip-rip-oper', False),
            ],
            'Cisco-IOS-XR-ip-rip-oper',
            'global',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rip-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper'
        ),
    },
    'Rip.Protocol.DefaultVrf' : {
        'meta_info' : _MetaInfoClass('Rip.Protocol.DefaultVrf',
            False, 
            [
            _MetaInfoClassMember('configuration', REFERENCE_CLASS, 'Configuration' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper', 'Rip.Protocol.DefaultVrf.Configuration', 
                [], [], 
                '''                RIP global configuration
                ''',
                'configuration',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('global', REFERENCE_CLASS, 'Global_' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper', 'Rip.Protocol.DefaultVrf.Global_', 
                [], [], 
                '''                Global Information 
                ''',
                'global_',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper', 'Rip.Protocol.DefaultVrf.Interfaces', 
                [], [], 
                '''                RIP interfaces
                ''',
                'interfaces',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('routes', REFERENCE_CLASS, 'Routes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper', 'Rip.Protocol.DefaultVrf.Routes', 
                [], [], 
                '''                RIP route database
                ''',
                'routes',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('statistics', REFERENCE_CLASS, 'Statistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper', 'Rip.Protocol.DefaultVrf.Statistics', 
                [], [], 
                '''                RIP statistics information
                ''',
                'statistics',
                'Cisco-IOS-XR-ip-rip-oper', False),
            ],
            'Cisco-IOS-XR-ip-rip-oper',
            'default-vrf',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rip-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper'
        ),
    },
    'Rip.Protocol' : {
        'meta_info' : _MetaInfoClass('Rip.Protocol',
            False, 
            [
            _MetaInfoClassMember('default-vrf', REFERENCE_CLASS, 'DefaultVrf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper', 'Rip.Protocol.DefaultVrf', 
                [], [], 
                '''                RIP operational data for Default VRF
                ''',
                'default_vrf',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('process', REFERENCE_CLASS, 'Process' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper', 'Rip.Protocol.Process', 
                [], [], 
                '''                RIP global process 
                ''',
                'process',
                'Cisco-IOS-XR-ip-rip-oper', False),
            ],
            'Cisco-IOS-XR-ip-rip-oper',
            'protocol',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rip-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper'
        ),
    },
    'Rip.DefaultVrf.Routes.Route.Paths' : {
        'meta_info' : _MetaInfoClass('Rip.DefaultVrf.Routes.Route.Paths',
            False, 
            [
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('is-permanent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Permanent indicator
                ''',
                'is_permanent',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('metric', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Metric
                ''',
                'metric',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('next-hop-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Next hop address
                ''',
                'next_hop_address',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Source address
                ''',
                'source_address',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('tag', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Tag
                ''',
                'tag',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('uptime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Up time
                ''',
                'uptime',
                'Cisco-IOS-XR-ip-rip-oper', False),
            ],
            'Cisco-IOS-XR-ip-rip-oper',
            'paths',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rip-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper'
        ),
    },
    'Rip.DefaultVrf.Routes.Route' : {
        'meta_info' : _MetaInfoClass('Rip.DefaultVrf.Routes.Route',
            False, 
            [
            _MetaInfoClassMember('active', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Active route indicator
                ''',
                'active',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('attributes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                RIB supplied route attributes
                ''',
                'attributes',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('bgp-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Hop count for this route
                ''',
                'bgp_count',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('destination-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Destination IP Address for this route
                ''',
                'destination_address',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('distance', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Route administrative distance
                ''',
                'distance',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('hold-down', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicates whether route is in holddown
                ''',
                'hold_down',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('path-origin', REFERENCE_ENUM_CLASS, 'RipRouteOriginEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper', 'RipRouteOriginEnum', 
                [], [], 
                '''                Where this route was learnt
                ''',
                'path_origin',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('paths', REFERENCE_LIST, 'Paths' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper', 'Rip.DefaultVrf.Routes.Route.Paths', 
                [], [], 
                '''                The paths for this route
                ''',
                'paths',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Network prefix
                ''',
                'prefix',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '32')], [], 
                '''                Prefix length
                ''',
                'prefix_length',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('prefix-length-xr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Prefix length of IP address
                ''',
                'prefix_length_xr',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('route-summary', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Summary route placeholder indicator
                ''',
                'route_summary',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('route-tag', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Generic route information
                ''',
                'route_tag',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('route-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Type of this route
                ''',
                'route_type',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                RIB supplied version number
                ''',
                'version',
                'Cisco-IOS-XR-ip-rip-oper', False),
            ],
            'Cisco-IOS-XR-ip-rip-oper',
            'route',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rip-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper'
        ),
    },
    'Rip.DefaultVrf.Routes' : {
        'meta_info' : _MetaInfoClass('Rip.DefaultVrf.Routes',
            False, 
            [
            _MetaInfoClassMember('route', REFERENCE_LIST, 'Route' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper', 'Rip.DefaultVrf.Routes.Route', 
                [], [], 
                '''                A route in the RIP database
                ''',
                'route',
                'Cisco-IOS-XR-ip-rip-oper', False),
            ],
            'Cisco-IOS-XR-ip-rip-oper',
            'routes',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rip-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper'
        ),
    },
    'Rip.DefaultVrf.Configuration' : {
        'meta_info' : _MetaInfoClass('Rip.DefaultVrf.Configuration',
            False, 
            [
            _MetaInfoClassMember('active', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                VRF active indicator
                ''',
                'active',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('auto-summarize', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Auto-summarization indicator
                ''',
                'auto_summarize',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('default-metric', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Default metric for RIP routes
                ''',
                'default_metric',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('flash-threshold', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Flash update threshold
                ''',
                'flash_threshold',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('flush-timer', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Flush timer
                ''',
                'flush_timer',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('hold-down-timer', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Holddown timer
                ''',
                'hold_down_timer',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('input-q-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Length of the input queue
                ''',
                'input_q_length',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('invalid-timer', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Invalid timer
                ''',
                'invalid_timer',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('maximum-paths', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Maximum number of paths a route can have
                ''',
                'maximum_paths',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('multicast-address', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Use broadcast/multicast address indicator
                ''',
                'multicast_address',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('next-update-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Time left for next update
                ''',
                'next_update_time',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('nsf-life-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                NSF life time
                ''',
                'nsf_life_time',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('nsf-status', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                NSF Enable status
                ''',
                'nsf_status',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('oom-flags', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Out-of-memory status flags
                ''',
                'oom_flags',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('rip-version', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Version of RIP configured
                ''',
                'rip_version',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('triggered-rip', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Triggered RIP enabled indicator
                ''',
                'triggered_rip',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('update-timer', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Update timer
                ''',
                'update_timer',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('validation-indicator', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Incoming packet source validation indicator
                ''',
                'validation_indicator',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('vr-fised-socket', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                VRF added to socket indicator
                ''',
                'vr_fised_socket',
                'Cisco-IOS-XR-ip-rip-oper', False),
            ],
            'Cisco-IOS-XR-ip-rip-oper',
            'configuration',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rip-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper'
        ),
    },
    'Rip.DefaultVrf.Statistics' : {
        'meta_info' : _MetaInfoClass('Rip.DefaultVrf.Statistics',
            False, 
            [
            _MetaInfoClassMember('discarded-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total discarded packets
                ''',
                'discarded_packets',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('discarded-routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total discarded routes
                ''',
                'discarded_routes',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('path-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of paths allocated
                ''',
                'path_count',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('path-malloc-failures', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of failures to allocate memory for a path
                ''',
                'path_malloc_failures',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('periodic-updates', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of periodic RIP updates
                ''',
                'periodic_updates',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('query-responses', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of RIP queries responded to
                ''',
                'query_responses',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total packets received
                ''',
                'received_packets',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('rib-updates', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of route updates to RIB made by RIP
                ''',
                'rib_updates',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('route-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of routes allocated
                ''',
                'route_count',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('route-malloc-failures', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of failures to allocate memory for a
                route
                ''',
                'route_malloc_failures',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('sent-message-failures', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of message send failures
                ''',
                'sent_message_failures',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('sent-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of messages sent
                ''',
                'sent_messages',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('standby-packets-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Packets rx in SRP
                ''',
                'standby_packets_received',
                'Cisco-IOS-XR-ip-rip-oper', False),
            ],
            'Cisco-IOS-XR-ip-rip-oper',
            'statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rip-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper'
        ),
    },
    'Rip.DefaultVrf.Interfaces.Interface.RipSummary' : {
        'meta_info' : _MetaInfoClass('Rip.DefaultVrf.Interfaces.Interface.RipSummary',
            False, 
            [
            _MetaInfoClassMember('metric', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Summary metric
                ''',
                'metric',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('next-hop-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Summary address next hop
                ''',
                'next_hop_address',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Summary address prefix
                ''',
                'prefix',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Summary address prefix length
                ''',
                'prefix_length',
                'Cisco-IOS-XR-ip-rip-oper', False),
            ],
            'Cisco-IOS-XR-ip-rip-oper',
            'rip-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rip-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper'
        ),
    },
    'Rip.DefaultVrf.Interfaces.Interface.RipPeer' : {
        'meta_info' : _MetaInfoClass('Rip.DefaultVrf.Interfaces.Interface.RipPeer',
            False, 
            [
            _MetaInfoClassMember('discarded-peer-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Discarded packets from this peer
                ''',
                'discarded_peer_packets',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('discarded-peer-routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Discarded routes from this peer
                ''',
                'discarded_peer_routes',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('peer-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IP Address of this peer
                ''',
                'peer_address',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('peer-uptime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Uptime of this peer
                ''',
                'peer_uptime',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('peer-version', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                RIP version for this peer
                ''',
                'peer_version',
                'Cisco-IOS-XR-ip-rip-oper', False),
            ],
            'Cisco-IOS-XR-ip-rip-oper',
            'rip-peer',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rip-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper'
        ),
    },
    'Rip.DefaultVrf.Interfaces.Interface' : {
        'meta_info' : _MetaInfoClass('Rip.DefaultVrf.Interfaces.Interface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ip-rip-oper', True),
            _MetaInfoClassMember('accept-metric', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Accept routes of metric 0 indicator
                ''',
                'accept_metric',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('auth-key-md5', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Authentication key programmed with MD5 algorithm
                ''',
                'auth_key_md5',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('auth-key-send-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Current active Send Authentication Key Id
                ''',
                'auth_key_send_id',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('auth-keychain', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Authentication Keychain Name
                ''',
                'auth_keychain',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('auth-mode', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Authentication Mode
                ''',
                'auth_mode',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('destination-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IP Address of this interface
                ''',
                'destination_address',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('if-handle', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface handle
                ''',
                'if_handle',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Interface name
                ''',
                'interface',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('is-passive-interface', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Passive interface indicator
                ''',
                'is_passive_interface',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('join-status', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Multicast group join status
                ''',
                'join_status',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('lpts-state', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                LPTSState
                ''',
                'lpts_state',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('metric-cost', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Cost added to routes through this interface
                ''',
                'metric_cost',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('multicast-address', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Use broadcast address for v2 packets
                ''',
                'multicast_address',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Interface's triggered RIP neighbor
                ''',
                'neighbor_address',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('oom-flags', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Out-of-memory status flags
                ''',
                'oom_flags',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('pkt-accepted-valid-auth', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Packets accepted with valid authentication data
                ''',
                'pkt_accepted_valid_auth',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('pkt-drop-invalid-auth', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Packets dropped due to invalid authentication
                data
                ''',
                'pkt_drop_invalid_auth',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('pkt-drop-no-auth', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Packets dropped due to missing authentication
                data
                ''',
                'pkt_drop_no_auth',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('pkt-drop-wrong-kc', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Packets dropped due to wrong keychain configured
                ''',
                'pkt_drop_wrong_kc',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('poison-horizon', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Poisoned reverse enabled indicator
                ''',
                'poison_horizon',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Prefix length of the IP address
                ''',
                'prefix_length',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('receive-version', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Versions that the interface will recieve
                ''',
                'receive_version',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('rip-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Whether RIP is enabled on this interface
                ''',
                'rip_enabled',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('rip-peer', REFERENCE_LIST, 'RipPeer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper', 'Rip.DefaultVrf.Interfaces.Interface.RipPeer', 
                [], [], 
                '''                Neighbors on this interface
                ''',
                'rip_peer',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('rip-summary', REFERENCE_LIST, 'RipSummary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper', 'Rip.DefaultVrf.Interfaces.Interface.RipSummary', 
                [], [], 
                '''                User defined summary addresses
                ''',
                'rip_summary',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('send-auth-key-exists', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Authentication send key exists
                ''',
                'send_auth_key_exists',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('send-version', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Versions that the interface is sending
                ''',
                'send_version',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('split-horizon', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Split horizon enabled indicator
                ''',
                'split_horizon',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'InterfaceStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper', 'InterfaceStateEnum', 
                [], [], 
                '''                Current state of the interface
                ''',
                'state',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('total-pkt-recvd', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total packets received
                ''',
                'total_pkt_recvd',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('triggered-rip', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Triggered RIP enabled indicator
                ''',
                'triggered_rip',
                'Cisco-IOS-XR-ip-rip-oper', False),
            ],
            'Cisco-IOS-XR-ip-rip-oper',
            'interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rip-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper'
        ),
    },
    'Rip.DefaultVrf.Interfaces' : {
        'meta_info' : _MetaInfoClass('Rip.DefaultVrf.Interfaces',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper', 'Rip.DefaultVrf.Interfaces.Interface', 
                [], [], 
                '''                Information about a particular RIP interface
                ''',
                'interface',
                'Cisco-IOS-XR-ip-rip-oper', False),
            ],
            'Cisco-IOS-XR-ip-rip-oper',
            'interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rip-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper'
        ),
    },
    'Rip.DefaultVrf.Global_.VrfSummary' : {
        'meta_info' : _MetaInfoClass('Rip.DefaultVrf.Global_.VrfSummary',
            False, 
            [
            _MetaInfoClassMember('active', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                VRF Active indicator
                ''',
                'active',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('active-interface-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of active interfaces
                ''',
                'active_interface_count',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('flush-timer', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Flush timer
                ''',
                'flush_timer',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('hold-down-timer', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Holddown timer
                ''',
                'hold_down_timer',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('interface-configured-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of interfaces configured
                ''',
                'interface_configured_count',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('invalid-timer', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Invalid timer
                ''',
                'invalid_timer',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('next-update-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Time left for next update
                ''',
                'next_update_time',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('oom-flags', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Current OOM flags
                ''',
                'oom_flags',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('path-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of paths allocated
                ''',
                'path_count',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('route-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of routes allocated
                ''',
                'route_count',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('update-timer', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Update timer
                ''',
                'update_timer',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                VRF Name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ip-rip-oper', False),
            ],
            'Cisco-IOS-XR-ip-rip-oper',
            'vrf-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rip-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper'
        ),
    },
    'Rip.DefaultVrf.Global_.InterfaceSummary' : {
        'meta_info' : _MetaInfoClass('Rip.DefaultVrf.Global_.InterfaceSummary',
            False, 
            [
            _MetaInfoClassMember('destination-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IP address
                ''',
                'destination_address',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                RIP enabled indicator
                ''',
                'enabled',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Interface name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('neighbor-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of neighbors seen
                ''',
                'neighbor_count',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('oom-flags', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Current OOM flags
                ''',
                'oom_flags',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Prefix length of IP address
                ''',
                'prefix_length',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('receive-version', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                RIP versions this interface will receive
                ''',
                'receive_version',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('send-version', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                RIP versions this interface sends out
                ''',
                'send_version',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'InterfaceStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper', 'InterfaceStateEnum', 
                [], [], 
                '''                Interface state
                ''',
                'state',
                'Cisco-IOS-XR-ip-rip-oper', False),
            ],
            'Cisco-IOS-XR-ip-rip-oper',
            'interface-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rip-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper'
        ),
    },
    'Rip.DefaultVrf.Global_' : {
        'meta_info' : _MetaInfoClass('Rip.DefaultVrf.Global_',
            False, 
            [
            _MetaInfoClassMember('interface-summary', REFERENCE_LIST, 'InterfaceSummary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper', 'Rip.DefaultVrf.Global_.InterfaceSummary', 
                [], [], 
                '''                List of Interfaces configured
                ''',
                'interface_summary',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('vrf-summary', REFERENCE_CLASS, 'VrfSummary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper', 'Rip.DefaultVrf.Global_.VrfSummary', 
                [], [], 
                '''                VRF summary data
                ''',
                'vrf_summary',
                'Cisco-IOS-XR-ip-rip-oper', False),
            ],
            'Cisco-IOS-XR-ip-rip-oper',
            'global',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rip-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper'
        ),
    },
    'Rip.DefaultVrf' : {
        'meta_info' : _MetaInfoClass('Rip.DefaultVrf',
            False, 
            [
            _MetaInfoClassMember('configuration', REFERENCE_CLASS, 'Configuration' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper', 'Rip.DefaultVrf.Configuration', 
                [], [], 
                '''                RIP global configuration
                ''',
                'configuration',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('global', REFERENCE_CLASS, 'Global_' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper', 'Rip.DefaultVrf.Global_', 
                [], [], 
                '''                Global Information 
                ''',
                'global_',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper', 'Rip.DefaultVrf.Interfaces', 
                [], [], 
                '''                RIP interfaces
                ''',
                'interfaces',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('routes', REFERENCE_CLASS, 'Routes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper', 'Rip.DefaultVrf.Routes', 
                [], [], 
                '''                RIP route database
                ''',
                'routes',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('statistics', REFERENCE_CLASS, 'Statistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper', 'Rip.DefaultVrf.Statistics', 
                [], [], 
                '''                RIP statistics information
                ''',
                'statistics',
                'Cisco-IOS-XR-ip-rip-oper', False),
            ],
            'Cisco-IOS-XR-ip-rip-oper',
            'default-vrf',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rip-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper'
        ),
    },
    'Rip' : {
        'meta_info' : _MetaInfoClass('Rip',
            False, 
            [
            _MetaInfoClassMember('default-vrf', REFERENCE_CLASS, 'DefaultVrf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper', 'Rip.DefaultVrf', 
                [], [], 
                '''                RIP operational data for Default VRF
                ''',
                'default_vrf',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('protocol', REFERENCE_CLASS, 'Protocol' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper', 'Rip.Protocol', 
                [], [], 
                '''                Protocol operational data
                ''',
                'protocol',
                'Cisco-IOS-XR-ip-rip-oper', False),
            _MetaInfoClassMember('vrfs', REFERENCE_CLASS, 'Vrfs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper', 'Rip.Vrfs', 
                [], [], 
                '''                VRF related operational data
                ''',
                'vrfs',
                'Cisco-IOS-XR-ip-rip-oper', False),
            ],
            'Cisco-IOS-XR-ip-rip-oper',
            'rip',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rip-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_rip_oper'
        ),
    },
}
_meta_table['Rip.Vrfs.Vrf.Routes.Route.Paths']['meta_info'].parent =_meta_table['Rip.Vrfs.Vrf.Routes.Route']['meta_info']
_meta_table['Rip.Vrfs.Vrf.Routes.Route']['meta_info'].parent =_meta_table['Rip.Vrfs.Vrf.Routes']['meta_info']
_meta_table['Rip.Vrfs.Vrf.Interfaces.Interface.RipSummary']['meta_info'].parent =_meta_table['Rip.Vrfs.Vrf.Interfaces.Interface']['meta_info']
_meta_table['Rip.Vrfs.Vrf.Interfaces.Interface.RipPeer']['meta_info'].parent =_meta_table['Rip.Vrfs.Vrf.Interfaces.Interface']['meta_info']
_meta_table['Rip.Vrfs.Vrf.Interfaces.Interface']['meta_info'].parent =_meta_table['Rip.Vrfs.Vrf.Interfaces']['meta_info']
_meta_table['Rip.Vrfs.Vrf.Global_.VrfSummary']['meta_info'].parent =_meta_table['Rip.Vrfs.Vrf.Global_']['meta_info']
_meta_table['Rip.Vrfs.Vrf.Global_.InterfaceSummary']['meta_info'].parent =_meta_table['Rip.Vrfs.Vrf.Global_']['meta_info']
_meta_table['Rip.Vrfs.Vrf.Routes']['meta_info'].parent =_meta_table['Rip.Vrfs.Vrf']['meta_info']
_meta_table['Rip.Vrfs.Vrf.Configuration']['meta_info'].parent =_meta_table['Rip.Vrfs.Vrf']['meta_info']
_meta_table['Rip.Vrfs.Vrf.Statistics']['meta_info'].parent =_meta_table['Rip.Vrfs.Vrf']['meta_info']
_meta_table['Rip.Vrfs.Vrf.Interfaces']['meta_info'].parent =_meta_table['Rip.Vrfs.Vrf']['meta_info']
_meta_table['Rip.Vrfs.Vrf.Global_']['meta_info'].parent =_meta_table['Rip.Vrfs.Vrf']['meta_info']
_meta_table['Rip.Vrfs.Vrf']['meta_info'].parent =_meta_table['Rip.Vrfs']['meta_info']
_meta_table['Rip.Protocol.Process.VrfSummary']['meta_info'].parent =_meta_table['Rip.Protocol.Process']['meta_info']
_meta_table['Rip.Protocol.DefaultVrf.Routes.Route.Paths']['meta_info'].parent =_meta_table['Rip.Protocol.DefaultVrf.Routes.Route']['meta_info']
_meta_table['Rip.Protocol.DefaultVrf.Routes.Route']['meta_info'].parent =_meta_table['Rip.Protocol.DefaultVrf.Routes']['meta_info']
_meta_table['Rip.Protocol.DefaultVrf.Interfaces.Interface.RipSummary']['meta_info'].parent =_meta_table['Rip.Protocol.DefaultVrf.Interfaces.Interface']['meta_info']
_meta_table['Rip.Protocol.DefaultVrf.Interfaces.Interface.RipPeer']['meta_info'].parent =_meta_table['Rip.Protocol.DefaultVrf.Interfaces.Interface']['meta_info']
_meta_table['Rip.Protocol.DefaultVrf.Interfaces.Interface']['meta_info'].parent =_meta_table['Rip.Protocol.DefaultVrf.Interfaces']['meta_info']
_meta_table['Rip.Protocol.DefaultVrf.Global_.VrfSummary']['meta_info'].parent =_meta_table['Rip.Protocol.DefaultVrf.Global_']['meta_info']
_meta_table['Rip.Protocol.DefaultVrf.Global_.InterfaceSummary']['meta_info'].parent =_meta_table['Rip.Protocol.DefaultVrf.Global_']['meta_info']
_meta_table['Rip.Protocol.DefaultVrf.Routes']['meta_info'].parent =_meta_table['Rip.Protocol.DefaultVrf']['meta_info']
_meta_table['Rip.Protocol.DefaultVrf.Configuration']['meta_info'].parent =_meta_table['Rip.Protocol.DefaultVrf']['meta_info']
_meta_table['Rip.Protocol.DefaultVrf.Statistics']['meta_info'].parent =_meta_table['Rip.Protocol.DefaultVrf']['meta_info']
_meta_table['Rip.Protocol.DefaultVrf.Interfaces']['meta_info'].parent =_meta_table['Rip.Protocol.DefaultVrf']['meta_info']
_meta_table['Rip.Protocol.DefaultVrf.Global_']['meta_info'].parent =_meta_table['Rip.Protocol.DefaultVrf']['meta_info']
_meta_table['Rip.Protocol.Process']['meta_info'].parent =_meta_table['Rip.Protocol']['meta_info']
_meta_table['Rip.Protocol.DefaultVrf']['meta_info'].parent =_meta_table['Rip.Protocol']['meta_info']
_meta_table['Rip.DefaultVrf.Routes.Route.Paths']['meta_info'].parent =_meta_table['Rip.DefaultVrf.Routes.Route']['meta_info']
_meta_table['Rip.DefaultVrf.Routes.Route']['meta_info'].parent =_meta_table['Rip.DefaultVrf.Routes']['meta_info']
_meta_table['Rip.DefaultVrf.Interfaces.Interface.RipSummary']['meta_info'].parent =_meta_table['Rip.DefaultVrf.Interfaces.Interface']['meta_info']
_meta_table['Rip.DefaultVrf.Interfaces.Interface.RipPeer']['meta_info'].parent =_meta_table['Rip.DefaultVrf.Interfaces.Interface']['meta_info']
_meta_table['Rip.DefaultVrf.Interfaces.Interface']['meta_info'].parent =_meta_table['Rip.DefaultVrf.Interfaces']['meta_info']
_meta_table['Rip.DefaultVrf.Global_.VrfSummary']['meta_info'].parent =_meta_table['Rip.DefaultVrf.Global_']['meta_info']
_meta_table['Rip.DefaultVrf.Global_.InterfaceSummary']['meta_info'].parent =_meta_table['Rip.DefaultVrf.Global_']['meta_info']
_meta_table['Rip.DefaultVrf.Routes']['meta_info'].parent =_meta_table['Rip.DefaultVrf']['meta_info']
_meta_table['Rip.DefaultVrf.Configuration']['meta_info'].parent =_meta_table['Rip.DefaultVrf']['meta_info']
_meta_table['Rip.DefaultVrf.Statistics']['meta_info'].parent =_meta_table['Rip.DefaultVrf']['meta_info']
_meta_table['Rip.DefaultVrf.Interfaces']['meta_info'].parent =_meta_table['Rip.DefaultVrf']['meta_info']
_meta_table['Rip.DefaultVrf.Global_']['meta_info'].parent =_meta_table['Rip.DefaultVrf']['meta_info']
_meta_table['Rip.Vrfs']['meta_info'].parent =_meta_table['Rip']['meta_info']
_meta_table['Rip.Protocol']['meta_info'].parent =_meta_table['Rip']['meta_info']
_meta_table['Rip.DefaultVrf']['meta_info'].parent =_meta_table['Rip']['meta_info']
