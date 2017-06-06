


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'BagDhcpv6DIaIdEnum' : _MetaInfoEnum('BagDhcpv6DIaIdEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper',
        {
            'iana':'iana',
            'iapd':'iapd',
            'iata':'iata',
        }, 'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper']),
    'Dhcpv6IssuVersionEnum' : _MetaInfoEnum('Dhcpv6IssuVersionEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper',
        {
            'version1':'version1',
            'version2':'version2',
        }, 'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper']),
    'BagDhcpv6DFsmStateEnum' : _MetaInfoEnum('BagDhcpv6DFsmStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper',
        {
            'server-initializing':'server_initializing',
            'server-waiting-dpm':'server_waiting_dpm',
            'server-waiting-daps':'server_waiting_daps',
            'server-waiting-client':'server_waiting_client',
            'server-waiting-subscriber':'server_waiting_subscriber',
            'server-waiting-rib':'server_waiting_rib',
            'server-bound-client':'server_bound_client',
            'proxy-initializing':'proxy_initializing',
            'proxy-waiting-dpm':'proxy_waiting_dpm',
            'proxy-waiting-daps':'proxy_waiting_daps',
            'proxy-waiting-client-server':'proxy_waiting_client_server',
            'proxy-waiting-subscriber':'proxy_waiting_subscriber',
            'proxy-waiting-rib':'proxy_waiting_rib',
            'proxy-bound-client':'proxy_bound_client',
        }, 'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper']),
    'DhcpIssuPhaseEnum' : _MetaInfoEnum('DhcpIssuPhaseEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper',
        {
            'phase-not-started':'phase_not_started',
            'phase-load':'phase_load',
            'phase-run':'phase_run',
            'phase-completed':'phase_completed',
            'phase-aborted':'phase_aborted',
        }, 'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper']),
    'BagDhcpv6DIntfSergRoleEnum' : _MetaInfoEnum('BagDhcpv6DIntfSergRoleEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper',
        {
            'none':'none',
            'master':'master',
            'slave':'slave',
        }, 'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper']),
    'BagDhcpv6DIntfSrgRoleEnum' : _MetaInfoEnum('BagDhcpv6DIntfSrgRoleEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper',
        {
            'none':'none',
            'master':'master',
            'slave':'slave',
        }, 'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper']),
    'LeaseLimitEnum' : _MetaInfoEnum('LeaseLimitEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper',
        {
            'none':'none',
            'interface':'interface',
            'circuit-id':'circuit_id',
            'remote-id':'remote_id',
        }, 'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper']),
    'BagDhcpv6DSubModeEnum' : _MetaInfoEnum('BagDhcpv6DSubModeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper',
        {
            'base':'base',
            'server':'server',
            'proxy':'proxy',
        }, 'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper']),
    'Dhcpv6IssuRoleEnum' : _MetaInfoEnum('Dhcpv6IssuRoleEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper',
        {
            'role-primary':'role_primary',
            'role-secondary':'role_secondary',
        }, 'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper']),
    'Dhcpv6.IssuStatus' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.IssuStatus',
            False, 
            [
            _MetaInfoClassMember('big-bang-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Timestamp for the Big Bang notification time in
                nanoseconds since Epoch, i.e. since 00:00:00 UTC
                , January 1, 1970
                ''',
                'big_bang_time',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('issu-ready-issu-mgr-connection', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Whether or not DHCP is currently connected to
                ISSU Manager during the ISSU Load Phase
                ''',
                'issu_ready_issu_mgr_connection',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('issu-ready-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Timestamp for the ISSU ready declaration in
                nanoseconds since Epoch, i.e. since 00:00:00 UTC
                , January 1, 1970
                ''',
                'issu_ready_time',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('issu-sync-complete-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Timestamp for the ISSU sync complete in
                nanoseconds since Epoch, i.e. since 00:00:00 UTC
                , January 1, 1970
                ''',
                'issu_sync_complete_time',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('issu-sync-start-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Timestamp for the ISSU sync start in nanoseconds
                since Epoch, i.e. since 00:00:00 UTC, January 1,
                1970
                ''',
                'issu_sync_start_time',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('phase', REFERENCE_ENUM_CLASS, 'DhcpIssuPhaseEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'DhcpIssuPhaseEnum', 
                [], [], 
                '''                The current ISSU phase of the DHCP process
                ''',
                'phase',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('primary-role-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Timestamp for the change to Primary role
                notification time in nanoseconds since Epoch, i
                .e. since 00:00:00 UTC, January 1, 1970
                ''',
                'primary_role_time',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('process-start-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Timestamp for the process start time in
                nanoseconds since Epoch, i.e. since 00:00:00 UTC
                , January 1, 1970
                ''',
                'process_start_time',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('role', REFERENCE_ENUM_CLASS, 'Dhcpv6IssuRoleEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6IssuRoleEnum', 
                [], [], 
                '''                The current role of the DHCP process
                ''',
                'role',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('version', REFERENCE_ENUM_CLASS, 'Dhcpv6IssuVersionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6IssuVersionEnum', 
                [], [], 
                '''                The current version of the DHCP process in the
                context of an ISSU
                ''',
                'version',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'issu-status',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Solicit' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Solicit',
            False, 
            [
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped packets
                ''',
                'dropped_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('transmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmitted packets
                ''',
                'transmitted_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'solicit',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Advertise' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Advertise',
            False, 
            [
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped packets
                ''',
                'dropped_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('transmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmitted packets
                ''',
                'transmitted_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'advertise',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Request' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Request',
            False, 
            [
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped packets
                ''',
                'dropped_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('transmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmitted packets
                ''',
                'transmitted_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'request',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Reply' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Reply',
            False, 
            [
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped packets
                ''',
                'dropped_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('transmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmitted packets
                ''',
                'transmitted_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'reply',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Confirm' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Confirm',
            False, 
            [
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped packets
                ''',
                'dropped_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('transmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmitted packets
                ''',
                'transmitted_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'confirm',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Decline' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Decline',
            False, 
            [
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped packets
                ''',
                'dropped_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('transmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmitted packets
                ''',
                'transmitted_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'decline',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Renew' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Renew',
            False, 
            [
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped packets
                ''',
                'dropped_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('transmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmitted packets
                ''',
                'transmitted_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'renew',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Rebind' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Rebind',
            False, 
            [
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped packets
                ''',
                'dropped_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('transmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmitted packets
                ''',
                'transmitted_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'rebind',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Release' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Release',
            False, 
            [
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped packets
                ''',
                'dropped_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('transmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmitted packets
                ''',
                'transmitted_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'release',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Reconfig' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Reconfig',
            False, 
            [
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped packets
                ''',
                'dropped_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('transmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmitted packets
                ''',
                'transmitted_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'reconfig',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Inform' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Inform',
            False, 
            [
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped packets
                ''',
                'dropped_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('transmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmitted packets
                ''',
                'transmitted_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'inform',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.RelayForward' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.RelayForward',
            False, 
            [
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped packets
                ''',
                'dropped_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('transmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmitted packets
                ''',
                'transmitted_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'relay-forward',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.RelayReply' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.RelayReply',
            False, 
            [
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped packets
                ''',
                'dropped_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('transmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmitted packets
                ''',
                'transmitted_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'relay-reply',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.LeaseQuery' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.LeaseQuery',
            False, 
            [
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped packets
                ''',
                'dropped_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('transmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmitted packets
                ''',
                'transmitted_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'lease-query',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.LeaseQueryReply' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.LeaseQueryReply',
            False, 
            [
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped packets
                ''',
                'dropped_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('transmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmitted packets
                ''',
                'transmitted_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'lease-query-reply',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.LeaseQueryDone' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.LeaseQueryDone',
            False, 
            [
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped packets
                ''',
                'dropped_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('transmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmitted packets
                ''',
                'transmitted_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'lease-query-done',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.LeaseQueryData' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.LeaseQueryData',
            False, 
            [
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped packets
                ''',
                'dropped_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('transmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmitted packets
                ''',
                'transmitted_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'lease-query-data',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics',
            False, 
            [
            _MetaInfoClassMember('advertise', REFERENCE_CLASS, 'Advertise' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Advertise', 
                [], [], 
                '''                DHCPV6 advertise packets
                ''',
                'advertise',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('confirm', REFERENCE_CLASS, 'Confirm' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Confirm', 
                [], [], 
                '''                DHCPV6 confirm packets
                ''',
                'confirm',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('decline', REFERENCE_CLASS, 'Decline' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Decline', 
                [], [], 
                '''                DHCPV6 decline packets
                ''',
                'decline',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('inform', REFERENCE_CLASS, 'Inform' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Inform', 
                [], [], 
                '''                DHCPV6 inform packets
                ''',
                'inform',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('lease-query', REFERENCE_CLASS, 'LeaseQuery' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.LeaseQuery', 
                [], [], 
                '''                DHCPV6 lease query packets
                ''',
                'lease_query',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('lease-query-data', REFERENCE_CLASS, 'LeaseQueryData' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.LeaseQueryData', 
                [], [], 
                '''                DHCPV6 lease query data packets
                ''',
                'lease_query_data',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('lease-query-done', REFERENCE_CLASS, 'LeaseQueryDone' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.LeaseQueryDone', 
                [], [], 
                '''                DHCPV6 lease query done packets
                ''',
                'lease_query_done',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('lease-query-reply', REFERENCE_CLASS, 'LeaseQueryReply' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.LeaseQueryReply', 
                [], [], 
                '''                DHCPV6 lease query reply packets
                ''',
                'lease_query_reply',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('rebind', REFERENCE_CLASS, 'Rebind' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Rebind', 
                [], [], 
                '''                DHCPV6 rebind packets
                ''',
                'rebind',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('reconfig', REFERENCE_CLASS, 'Reconfig' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Reconfig', 
                [], [], 
                '''                DHCPV6 reconfig packets
                ''',
                'reconfig',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('relay-forward', REFERENCE_CLASS, 'RelayForward' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.RelayForward', 
                [], [], 
                '''                DHCPV6 relay forward packets
                ''',
                'relay_forward',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('relay-reply', REFERENCE_CLASS, 'RelayReply' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.RelayReply', 
                [], [], 
                '''                DHCPV6 relay reply packets
                ''',
                'relay_reply',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('release', REFERENCE_CLASS, 'Release' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Release', 
                [], [], 
                '''                DHCPV6 release packets
                ''',
                'release',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('renew', REFERENCE_CLASS, 'Renew' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Renew', 
                [], [], 
                '''                DHCPV6 renew packets
                ''',
                'renew',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('reply', REFERENCE_CLASS, 'Reply' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Reply', 
                [], [], 
                '''                DHCPV6 reply packets
                ''',
                'reply',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('request', REFERENCE_CLASS, 'Request' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Request', 
                [], [], 
                '''                DHCPV6 request packets
                ''',
                'request',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('solicit', REFERENCE_CLASS, 'Solicit' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Solicit', 
                [], [], 
                '''                DHCPV6 solicit packets
                ''',
                'solicit',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf',
            False, 
            [
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', True),
            _MetaInfoClassMember('statistics', REFERENCE_CLASS, 'Statistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics', 
                [], [], 
                '''                IPv6 DHCP proxy statistics
                ''',
                'statistics',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'vrf',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Proxy.Vrfs' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Proxy.Vrfs',
            False, 
            [
            _MetaInfoClassMember('vrf', REFERENCE_LIST, 'Vrf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf', 
                [], [], 
                '''                IPv6 DHCP proxy VRF name
                ''',
                'vrf',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'vrfs',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.ThrottleInfos.ThrottleInfo' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.ThrottleInfos.ThrottleInfo',
            False, 
            [
            _MetaInfoClassMember('mac-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                MAC address
                ''',
                'mac_address',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', True),
            _MetaInfoClassMember('binding-chaddr', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Client MAC address
                ''',
                'binding_chaddr',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('ifname', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                DHCP access interface
                ''',
                'ifname',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('state', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                State of entry
                ''',
                'state',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('time-left', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Time Left in secs
                ''',
                'time_left',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'throttle-info',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.ThrottleInfos' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.ThrottleInfos',
            False, 
            [
            _MetaInfoClassMember('throttle-info', REFERENCE_LIST, 'ThrottleInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.ThrottleInfos.ThrottleInfo', 
                [], [], 
                '''                IPv6 DHCP proxy profile Throttle Info
                ''',
                'throttle_info',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'throttle-infos',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.Info.InterfaceIdReferences.Ipv6Dhcpv6DProxyIidReference' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.Info.InterfaceIdReferences.Ipv6Dhcpv6DProxyIidReference',
            False, 
            [
            _MetaInfoClassMember('proxy-iid-interface-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                Interface name for interface id
                ''',
                'proxy_iid_interface_name',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('proxy-interface-id', ATTRIBUTE, 'str' , None, None, 
                [(0, 257)], [], 
                '''                Interface id
                ''',
                'proxy_interface_id',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'ipv6-dhcpv6d-proxy-iid-reference',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.Info.InterfaceIdReferences' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.Info.InterfaceIdReferences',
            False, 
            [
            _MetaInfoClassMember('ipv6-dhcpv6d-proxy-iid-reference', REFERENCE_LIST, 'Ipv6Dhcpv6DProxyIidReference' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.Info.InterfaceIdReferences.Ipv6Dhcpv6DProxyIidReference', 
                [], [], 
                '''                ipv6 dhcpv6d proxy iid reference
                ''',
                'ipv6_dhcpv6d_proxy_iid_reference',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'interface-id-references',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.Info.VrfReferences.Ipv6Dhcpv6DProxyVrfReference' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.Info.VrfReferences.Ipv6Dhcpv6DProxyVrfReference',
            False, 
            [
            _MetaInfoClassMember('proxy-reference-vrf-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 33)], [], 
                '''                VRF name
                ''',
                'proxy_reference_vrf_name',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'ipv6-dhcpv6d-proxy-vrf-reference',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.Info.VrfReferences' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.Info.VrfReferences',
            False, 
            [
            _MetaInfoClassMember('ipv6-dhcpv6d-proxy-vrf-reference', REFERENCE_LIST, 'Ipv6Dhcpv6DProxyVrfReference' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.Info.VrfReferences.Ipv6Dhcpv6DProxyVrfReference', 
                [], [], 
                '''                ipv6 dhcpv6d proxy vrf reference
                ''',
                'ipv6_dhcpv6d_proxy_vrf_reference',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'vrf-references',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.Info.InterfaceReferences.Ipv6Dhcpv6DProxyInterfaceReference' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.Info.InterfaceReferences.Ipv6Dhcpv6DProxyInterfaceReference',
            False, 
            [
            _MetaInfoClassMember('proxy-reference-interface-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                Interface name
                ''',
                'proxy_reference_interface_name',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'ipv6-dhcpv6d-proxy-interface-reference',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.Info.InterfaceReferences' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.Info.InterfaceReferences',
            False, 
            [
            _MetaInfoClassMember('ipv6-dhcpv6d-proxy-interface-reference', REFERENCE_LIST, 'Ipv6Dhcpv6DProxyInterfaceReference' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.Info.InterfaceReferences.Ipv6Dhcpv6DProxyInterfaceReference', 
                [], [], 
                '''                ipv6 dhcpv6d proxy interface reference
                ''',
                'ipv6_dhcpv6d_proxy_interface_reference',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'interface-references',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.Info' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.Info',
            False, 
            [
            _MetaInfoClassMember('interface-id-references', REFERENCE_CLASS, 'InterfaceIdReferences' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.Info.InterfaceIdReferences', 
                [], [], 
                '''                Interface id references
                ''',
                'interface_id_references',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('interface-name', REFERENCE_LEAFLIST, 'str' , None, None, 
                [(0, 65)], [], 
                '''                Interface names
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False, max_elements=8),
            _MetaInfoClassMember('interface-references', REFERENCE_CLASS, 'InterfaceReferences' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.Info.InterfaceReferences', 
                [], [], 
                '''                Interface references
                ''',
                'interface_references',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('profile-helper-address', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                Helper addresses
                ''',
                'profile_helper_address',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False, max_elements=8),
            _MetaInfoClassMember('profile-link-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                Link address
                ''',
                'profile_link_address',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('profile-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                Proxy profile name
                ''',
                'profile_name',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('remote-id', ATTRIBUTE, 'str' , None, None, 
                [(0, 257)], [], 
                '''                Remote id
                ''',
                'remote_id',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('vrf-name', REFERENCE_LEAFLIST, 'str' , None, None, 
                [(0, 33)], [], 
                '''                VRF names
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False, max_elements=8),
            _MetaInfoClassMember('vrf-references', REFERENCE_CLASS, 'VrfReferences' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.Info.VrfReferences', 
                [], [], 
                '''                VRF references
                ''',
                'vrf_references',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'info',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Proxy.Profiles.Profile' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Proxy.Profiles.Profile',
            False, 
            [
            _MetaInfoClassMember('profile-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Profile name
                ''',
                'profile_name',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', True),
            _MetaInfoClassMember('info', REFERENCE_CLASS, 'Info' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.Info', 
                [], [], 
                '''                IPv6 DHCP proxy profile Info
                ''',
                'info',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('throttle-infos', REFERENCE_CLASS, 'ThrottleInfos' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.ThrottleInfos', 
                [], [], 
                '''                DHCPV6 throttle table
                ''',
                'throttle_infos',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'profile',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Proxy.Profiles' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Proxy.Profiles',
            False, 
            [
            _MetaInfoClassMember('profile', REFERENCE_LIST, 'Profile' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Proxy.Profiles.Profile', 
                [], [], 
                '''                IPv6 DHCP proxy profile
                ''',
                'profile',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'profiles',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Proxy.Interfaces.Interface' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Proxy.Interfaces.Interface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', True),
            _MetaInfoClassMember('is-proxy-interface-ambiguous', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Is interface ambiguous
                ''',
                'is_proxy_interface_ambiguous',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('mac-throttle', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Mac Throttle Status
                ''',
                'mac_throttle',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('proxy-interface-lease-limit-type', REFERENCE_ENUM_CLASS, 'LeaseLimitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'LeaseLimitEnum', 
                [], [], 
                '''                Lease limit type on interface
                ''',
                'proxy_interface_lease_limit_type',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('proxy-interface-lease-limits', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Lease limit count on interface
                ''',
                'proxy_interface_lease_limits',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('proxy-interface-mode', REFERENCE_ENUM_CLASS, 'BagDhcpv6DSubModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'BagDhcpv6DSubModeEnum', 
                [], [], 
                '''                Mode of interface
                ''',
                'proxy_interface_mode',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('proxy-interface-profile-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                Name of profile attached to the interface
                ''',
                'proxy_interface_profile_name',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('proxy-vrf-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 33)], [], 
                '''                VRF name
                ''',
                'proxy_vrf_name',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('serg-role', REFERENCE_ENUM_CLASS, 'BagDhcpv6DIntfSergRoleEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'BagDhcpv6DIntfSergRoleEnum', 
                [], [], 
                '''                DHCPv6 Interface SERG role
                ''',
                'serg_role',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('srg-role', REFERENCE_ENUM_CLASS, 'BagDhcpv6DIntfSrgRoleEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'BagDhcpv6DIntfSrgRoleEnum', 
                [], [], 
                '''                DHCPv6 Interface SRG role
                ''',
                'srg_role',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('srg-vrf-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 33)], [], 
                '''                SRG VRF name
                ''',
                'srg_vrf_name',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('srgp2p', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                SRG P2P Status
                ''',
                'srgp2p',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Proxy.Interfaces' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Proxy.Interfaces',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Proxy.Interfaces.Interface', 
                [], [], 
                '''                IPv6 DHCP proxy interface
                ''',
                'interface',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Proxy.Statistics.Ipv6Dhcpv6DProxyStat.Statistics_' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Proxy.Statistics.Ipv6Dhcpv6DProxyStat.Statistics_',
            False, 
            [
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped packets
                ''',
                'dropped_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('transmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmitted packets
                ''',
                'transmitted_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Proxy.Statistics.Ipv6Dhcpv6DProxyStat' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Proxy.Statistics.Ipv6Dhcpv6DProxyStat',
            False, 
            [
            _MetaInfoClassMember('statistics', REFERENCE_CLASS, 'Statistics_' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Proxy.Statistics.Ipv6Dhcpv6DProxyStat.Statistics_', 
                [], [], 
                '''                Proxy statistics
                ''',
                'statistics',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 33)], [], 
                '''                DHCPv6 L3 VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'ipv6-dhcpv6d-proxy-stat',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Proxy.Statistics' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Proxy.Statistics',
            False, 
            [
            _MetaInfoClassMember('ipv6-dhcpv6d-proxy-stat', REFERENCE_LIST, 'Ipv6Dhcpv6DProxyStat' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Proxy.Statistics.Ipv6Dhcpv6DProxyStat', 
                [], [], 
                '''                ipv6 dhcpv6d proxy stat
                ''',
                'ipv6_dhcpv6d_proxy_stat',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Proxy.Binding.Clients.Client.IaIdPd.BagDhcpv6DIaIdPdInfo.Addresses.BagDhcpv6DAddrAttrb' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Proxy.Binding.Clients.Client.IaIdPd.BagDhcpv6DIaIdPdInfo.Addresses.BagDhcpv6DAddrAttrb',
            False, 
            [
            _MetaInfoClassMember('lease-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Lease time in seconds
                ''',
                'lease_time',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 prefix
                ''',
                'prefix',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Prefix length
                ''',
                'prefix_length',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('remaining-lease-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Remaining lease time in seconds
                ''',
                'remaining_lease_time',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'bag-dhcpv6d-addr-attrb',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Proxy.Binding.Clients.Client.IaIdPd.BagDhcpv6DIaIdPdInfo.Addresses' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Proxy.Binding.Clients.Client.IaIdPd.BagDhcpv6DIaIdPdInfo.Addresses',
            False, 
            [
            _MetaInfoClassMember('bag-dhcpv6d-addr-attrb', REFERENCE_LIST, 'BagDhcpv6DAddrAttrb' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Proxy.Binding.Clients.Client.IaIdPd.BagDhcpv6DIaIdPdInfo.Addresses.BagDhcpv6DAddrAttrb', 
                [], [], 
                '''                bag dhcpv6d addr attrb
                ''',
                'bag_dhcpv6d_addr_attrb',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'addresses',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Proxy.Binding.Clients.Client.IaIdPd.BagDhcpv6DIaIdPdInfo' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Proxy.Binding.Clients.Client.IaIdPd.BagDhcpv6DIaIdPdInfo',
            False, 
            [
            _MetaInfoClassMember('addresses', REFERENCE_CLASS, 'Addresses' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Proxy.Binding.Clients.Client.IaIdPd.BagDhcpv6DIaIdPdInfo.Addresses', 
                [], [], 
                '''                List of addresses in this IA
                ''',
                'addresses',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('flags', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                FSM Flag for this IA
                ''',
                'flags',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('ia-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IA_ID of this IA
                ''',
                'ia_id',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('ia-type', REFERENCE_ENUM_CLASS, 'BagDhcpv6DIaIdEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'BagDhcpv6DIaIdEnum', 
                [], [], 
                '''                IA type
                ''',
                'ia_type',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'BagDhcpv6DFsmStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'BagDhcpv6DFsmStateEnum', 
                [], [], 
                '''                State
                ''',
                'state',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('total-address', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Total address in this IA
                ''',
                'total_address',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'bag-dhcpv6d-ia-id-pd-info',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Proxy.Binding.Clients.Client.IaIdPd' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Proxy.Binding.Clients.Client.IaIdPd',
            False, 
            [
            _MetaInfoClassMember('bag-dhcpv6d-ia-id-pd-info', REFERENCE_LIST, 'BagDhcpv6DIaIdPdInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Proxy.Binding.Clients.Client.IaIdPd.BagDhcpv6DIaIdPdInfo', 
                [], [], 
                '''                bag dhcpv6d ia id pd info
                ''',
                'bag_dhcpv6d_ia_id_pd_info',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'ia-id-pd',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Proxy.Binding.Clients.Client' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Proxy.Binding.Clients.Client',
            False, 
            [
            _MetaInfoClassMember('client-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Client ID
                ''',
                'client_id',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', True),
            _MetaInfoClassMember('access-vrf-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 33)], [], 
                '''                DHCPV6 access VRF name to client
                ''',
                'access_vrf_name',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('class-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                DHCPV6 class name
                ''',
                'class_name',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('client-flag', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                DHCPV6 client flag
                ''',
                'client_flag',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('duid', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Client DUID
                ''',
                'duid',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('framed-ipv6-prefix', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                DHCPV6 framed ipv6 addess used by ND
                ''',
                'framed_ipv6_prefix',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('framed-prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                DHCPV6 framed ipv6 prefix length used by ND
                ''',
                'framed_prefix_length',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('ia-id-p-ds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of ia_id/pd
                ''',
                'ia_id_p_ds',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('ia-id-pd', REFERENCE_CLASS, 'IaIdPd' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Proxy.Binding.Clients.Client.IaIdPd', 
                [], [], 
                '''                List of DHCPv6 IA_ID/PDs
                ''',
                'ia_id_pd',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                DHCPV6 access interface to client
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('is-nak-next-renew', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is true if DHCP next renew from client will be
                NAK'd
                ''',
                'is_nak_next_renew',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('mac-address', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Client MAC address
                ''',
                'mac_address',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('pool-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                DHCPV6 pool name
                ''',
                'pool_name',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('profile-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                DHCPV6 profile name
                ''',
                'profile_name',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('proxy-binding-inner-tag', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                DHCPV6 VLAN Inner VLAN
                ''',
                'proxy_binding_inner_tag',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('proxy-binding-outer-tag', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                DHCPV6 VLAN Outer VLAN
                ''',
                'proxy_binding_outer_tag',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('proxy-binding-tags', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                DHCPV6 VLAN tag count
                ''',
                'proxy_binding_tags',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('rx-interface-id', ATTRIBUTE, 'str' , None, None, 
                [(0, 771)], [], 
                '''                DHCPV6 received Interface ID
                ''',
                'rx_interface_id',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('rx-remote-id', ATTRIBUTE, 'str' , None, None, 
                [(0, 771)], [], 
                '''                DHCPV6 received Remote ID
                ''',
                'rx_remote_id',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('serg-intf-role', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                DHCPV6 SERG Intf Role
                ''',
                'serg_intf_role',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('serg-state', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                DHCPV6 SERG state
                ''',
                'serg_state',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('server-ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                DHCPV6 server IPv6 address
                ''',
                'server_ipv6_address',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('srg-intf-role', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                DHCPV6 SRG Intf Role
                ''',
                'srg_intf_role',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('srg-state', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                DHCPV6 SRG state
                ''',
                'srg_state',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('srg-vrf-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 33)], [], 
                '''                DHCPV6 SRG VRF NAME
                ''',
                'srg_vrf_name',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('srgp2p', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                SRG P2P Status
                ''',
                'srgp2p',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('subscriber-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                DHCPV6 subscriber label
                ''',
                'subscriber_label',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('tx-interface-id', ATTRIBUTE, 'str' , None, None, 
                [(0, 771)], [], 
                '''                DHCPV6 transmitted Interface ID
                ''',
                'tx_interface_id',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('tx-remote-id', ATTRIBUTE, 'str' , None, None, 
                [(0, 771)], [], 
                '''                DHCPV6 transmitted Remote ID
                ''',
                'tx_remote_id',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 33)], [], 
                '''                DHCPVV6 client/subscriber VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'client',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Proxy.Binding.Clients' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Proxy.Binding.Clients',
            False, 
            [
            _MetaInfoClassMember('client', REFERENCE_LIST, 'Client' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Proxy.Binding.Clients.Client', 
                [], [], 
                '''                Single DHCPV6 proxy binding
                ''',
                'client',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'clients',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Proxy.Binding.Summary.Iana' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Proxy.Binding.Summary.Iana',
            False, 
            [
            _MetaInfoClassMember('bound-clients', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of clients in bound state
                ''',
                'bound_clients',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('daps-waiting-clients', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of clients waiting on DAPS to assign/free
                prefix(ND)
                ''',
                'daps_waiting_clients',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('dpm-waiting-clients', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of clients waiting on DPM to validate
                subscriber
                ''',
                'dpm_waiting_clients',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('iedge-waiting-clients', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of clients waiting on iedge to subscriber
                session
                ''',
                'iedge_waiting_clients',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('initializing-clients', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of clients in init state
                ''',
                'initializing_clients',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('msg-waiting-clients', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of clients waiting for a message from the
                client/server
                ''',
                'msg_waiting_clients',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('rib-waiting-clients', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of clients in waiting on RIB response
                ''',
                'rib_waiting_clients',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'iana',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Proxy.Binding.Summary.Iapd' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Proxy.Binding.Summary.Iapd',
            False, 
            [
            _MetaInfoClassMember('bound-clients', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of clients in bound state
                ''',
                'bound_clients',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('daps-waiting-clients', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of clients waiting on DAPS to assign/free
                prefix(ND)
                ''',
                'daps_waiting_clients',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('dpm-waiting-clients', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of clients waiting on DPM to validate
                subscriber
                ''',
                'dpm_waiting_clients',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('iedge-waiting-clients', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of clients waiting on iedge to subscriber
                session
                ''',
                'iedge_waiting_clients',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('initializing-clients', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of clients in init state
                ''',
                'initializing_clients',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('msg-waiting-clients', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of clients waiting for a message from the
                client/server
                ''',
                'msg_waiting_clients',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('rib-waiting-clients', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of clients in waiting on RIB response
                ''',
                'rib_waiting_clients',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'iapd',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Proxy.Binding.Summary' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Proxy.Binding.Summary',
            False, 
            [
            _MetaInfoClassMember('clients', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total number of clients
                ''',
                'clients',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('iana', REFERENCE_CLASS, 'Iana' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Proxy.Binding.Summary.Iana', 
                [], [], 
                '''                IANA proxy binding summary
                ''',
                'iana',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('iapd', REFERENCE_CLASS, 'Iapd' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Proxy.Binding.Summary.Iapd', 
                [], [], 
                '''                IAPD proxy binding summary
                ''',
                'iapd',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'summary',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Proxy.Binding' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Proxy.Binding',
            False, 
            [
            _MetaInfoClassMember('clients', REFERENCE_CLASS, 'Clients' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Proxy.Binding.Clients', 
                [], [], 
                '''                DHCPV6 proxy client bindings
                ''',
                'clients',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('summary', REFERENCE_CLASS, 'Summary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Proxy.Binding.Summary', 
                [], [], 
                '''                DHCPV6 proxy binding summary
                ''',
                'summary',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'binding',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Proxy' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Proxy',
            False, 
            [
            _MetaInfoClassMember('binding', REFERENCE_CLASS, 'Binding' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Proxy.Binding', 
                [], [], 
                '''                DHCPV6 proxy bindings
                ''',
                'binding',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Proxy.Interfaces', 
                [], [], 
                '''                DHCPV6 proxy interface
                ''',
                'interfaces',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('profiles', REFERENCE_CLASS, 'Profiles' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Proxy.Profiles', 
                [], [], 
                '''                IPv6 DHCP proxy profile
                ''',
                'profiles',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('statistics', REFERENCE_CLASS, 'Statistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Proxy.Statistics', 
                [], [], 
                '''                DHCPv6 proxy statistics
                ''',
                'statistics',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('vrfs', REFERENCE_CLASS, 'Vrfs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Proxy.Vrfs', 
                [], [], 
                '''                DHCPV6 proxy list of VRF names
                ''',
                'vrfs',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'proxy',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Base.Database' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Base.Database',
            False, 
            [
            _MetaInfoClassMember('configured', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Database feature configured
                ''',
                'configured',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('failed-full-file-write-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Failed full file write count
                ''',
                'failed_full_file_write_count',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('failed-incremental-file-write-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Failed incremental file write count
                ''',
                'failed_incremental_file_write_count',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('full-file-record-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Full file record count
                ''',
                'full_file_record_count',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('full-file-write-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Full file write count
                ''',
                'full_file_write_count',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('full-file-write-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Full file write interval in minutes
                ''',
                'full_file_write_interval',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('incremental-file-record-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Incremental file record count
                ''',
                'incremental_file_record_count',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('incremental-file-write-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Incremental file write count
                ''',
                'incremental_file_write_count',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('incremental-file-write-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Incremental file write interval in minutes
                ''',
                'incremental_file_write_interval',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('last-full-file-write-error-timestamp', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Last full file write error timestamp since epoch
                ''',
                'last_full_file_write_error_timestamp',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('last-full-write-file-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Last full write file name
                ''',
                'last_full_write_file_name',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('last-full-write-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Last full write time since epoch
                ''',
                'last_full_write_time',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('last-incremental-file-write-error-timestamp', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Last incremental file write error timestamp
                since epoch
                ''',
                'last_incremental_file_write_error_timestamp',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('last-incremental-write-file-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Last incremental write file name
                ''',
                'last_incremental_write_file_name',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('last-incremental-write-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Last incremental write time since epoch
                ''',
                'last_incremental_write_time',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Current file version
                ''',
                'version',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'database',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Base.AddrBindings.AddrBinding' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Base.AddrBindings.AddrBinding',
            False, 
            [
            _MetaInfoClassMember('addr-string', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Address String
                ''',
                'addr_string',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', True),
            _MetaInfoClassMember('access-vrf-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 33)], [], 
                '''                DHCPV6 access interface VRF name
                ''',
                'access_vrf_name',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('base-binding-inner-tag', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                DHCPV6 VLAN Inner VLAN
                ''',
                'base_binding_inner_tag',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('base-binding-outer-tag', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                DHCPV6 VLAN Outer VLAN
                ''',
                'base_binding_outer_tag',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('base-binding-tags', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                DHCPV6 VLAN tag count
                ''',
                'base_binding_tags',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                DHCPV6 access interface to client
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                DHCPV6 IPv6 address
                ''',
                'ipv6_address',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('is-nak-next-renew', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is true if DHCPV6 next renew from client will be
                NAK'd
                ''',
                'is_nak_next_renew',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('lease-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Lease time in seconds
                ''',
                'lease_time',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('mac-address', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                DHCPV6 client MAC address
                ''',
                'mac_address',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('old-subscriber-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                DHCPV6 old subscriber label
                ''',
                'old_subscriber_label',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('profile-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                DHCPV6 profile name
                ''',
                'profile_name',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('remaining-lease-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Remaining lease time in seconds
                ''',
                'remaining_lease_time',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('reply-server-ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                DHCPV6 reply server IPv6 address
                ''',
                'reply_server_ipv6_address',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('rx-client-duid', ATTRIBUTE, 'str' , None, None, 
                [(0, 771)], [], 
                '''                DHCPV6 received client DUID
                ''',
                'rx_client_duid',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('rx-interface-id', ATTRIBUTE, 'str' , None, None, 
                [(0, 771)], [], 
                '''                DHCPV6 received Interface ID
                ''',
                'rx_interface_id',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('rx-remote-id', ATTRIBUTE, 'str' , None, None, 
                [(0, 771)], [], 
                '''                DHCPV6 received Remote ID
                ''',
                'rx_remote_id',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('server-ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                DHCPV6 server IPv6 address
                ''',
                'server_ipv6_address',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('server-vrf-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 33)], [], 
                '''                DHCPV6 server VRF name
                ''',
                'server_vrf_name',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'BagDhcpv6DFsmStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'BagDhcpv6DFsmStateEnum', 
                [], [], 
                '''                DHCPV6 client state
                ''',
                'state',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('subscriber-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                DHCPV6 subscriber label
                ''',
                'subscriber_label',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('tx-client-uid', ATTRIBUTE, 'str' , None, None, 
                [(0, 771)], [], 
                '''                DHCPV6 transmitted client DUID
                ''',
                'tx_client_uid',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('tx-interface-id', ATTRIBUTE, 'str' , None, None, 
                [(0, 771)], [], 
                '''                DHCPV6 transmitted Interface ID
                ''',
                'tx_interface_id',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('tx-remote-id', ATTRIBUTE, 'str' , None, None, 
                [(0, 771)], [], 
                '''                DHCPV6 transmitted Remote ID
                ''',
                'tx_remote_id',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 33)], [], 
                '''                DHCPV6 client/subscriber VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'addr-binding',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Base.AddrBindings' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Base.AddrBindings',
            False, 
            [
            _MetaInfoClassMember('addr-binding', REFERENCE_LIST, 'AddrBinding' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Base.AddrBindings.AddrBinding', 
                [], [], 
                '''                DHCPv6 base stats debug
                ''',
                'addr_binding',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'addr-bindings',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Base' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Base',
            False, 
            [
            _MetaInfoClassMember('addr-bindings', REFERENCE_CLASS, 'AddrBindings' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Base.AddrBindings', 
                [], [], 
                '''                IPv6 DHCP Base Binding
                ''',
                'addr_bindings',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('database', REFERENCE_CLASS, 'Database' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Base.Database', 
                [], [], 
                '''                DHCP database
                ''',
                'database',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'base',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Server.Binding.Summary.Iana' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Server.Binding.Summary.Iana',
            False, 
            [
            _MetaInfoClassMember('bound-clients', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of clients in bound state
                ''',
                'bound_clients',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('daps-waiting-clients', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of clients waiting on DAPS to assign/free
                addr/prefix
                ''',
                'daps_waiting_clients',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('dpm-waiting-clients', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of clients waiting on DPM to validate
                subscriber
                ''',
                'dpm_waiting_clients',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('iedge-waiting-clients', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of clients waiting for iedge for the
                session
                ''',
                'iedge_waiting_clients',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('initializing-clients', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of clients in init state
                ''',
                'initializing_clients',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('request-waiting-clients', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of clients waiting for a request from the
                client
                ''',
                'request_waiting_clients',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('rib-waiting-clients', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of clients in waiting for RIB response
                ''',
                'rib_waiting_clients',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'iana',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Server.Binding.Summary.Iapd' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Server.Binding.Summary.Iapd',
            False, 
            [
            _MetaInfoClassMember('bound-clients', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of clients in bound state
                ''',
                'bound_clients',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('daps-waiting-clients', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of clients waiting on DAPS to assign/free
                addr/prefix
                ''',
                'daps_waiting_clients',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('dpm-waiting-clients', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of clients waiting on DPM to validate
                subscriber
                ''',
                'dpm_waiting_clients',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('iedge-waiting-clients', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of clients waiting for iedge for the
                session
                ''',
                'iedge_waiting_clients',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('initializing-clients', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of clients in init state
                ''',
                'initializing_clients',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('request-waiting-clients', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of clients waiting for a request from the
                client
                ''',
                'request_waiting_clients',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('rib-waiting-clients', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of clients in waiting for RIB response
                ''',
                'rib_waiting_clients',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'iapd',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Server.Binding.Summary' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Server.Binding.Summary',
            False, 
            [
            _MetaInfoClassMember('clients', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total number of clients
                ''',
                'clients',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('iana', REFERENCE_CLASS, 'Iana' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Server.Binding.Summary.Iana', 
                [], [], 
                '''                IANA server binding summary
                ''',
                'iana',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('iapd', REFERENCE_CLASS, 'Iapd' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Server.Binding.Summary.Iapd', 
                [], [], 
                '''                IAPD server binding summary
                ''',
                'iapd',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'summary',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Server.Binding.Clients.Client.IaIdPd.BagDhcpv6DIaIdPdInfo.Addresses.BagDhcpv6DAddrAttrb' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Server.Binding.Clients.Client.IaIdPd.BagDhcpv6DIaIdPdInfo.Addresses.BagDhcpv6DAddrAttrb',
            False, 
            [
            _MetaInfoClassMember('lease-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Lease time in seconds
                ''',
                'lease_time',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 prefix
                ''',
                'prefix',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Prefix length
                ''',
                'prefix_length',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('remaining-lease-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Remaining lease time in seconds
                ''',
                'remaining_lease_time',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'bag-dhcpv6d-addr-attrb',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Server.Binding.Clients.Client.IaIdPd.BagDhcpv6DIaIdPdInfo.Addresses' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Server.Binding.Clients.Client.IaIdPd.BagDhcpv6DIaIdPdInfo.Addresses',
            False, 
            [
            _MetaInfoClassMember('bag-dhcpv6d-addr-attrb', REFERENCE_LIST, 'BagDhcpv6DAddrAttrb' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Server.Binding.Clients.Client.IaIdPd.BagDhcpv6DIaIdPdInfo.Addresses.BagDhcpv6DAddrAttrb', 
                [], [], 
                '''                bag dhcpv6d addr attrb
                ''',
                'bag_dhcpv6d_addr_attrb',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'addresses',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Server.Binding.Clients.Client.IaIdPd.BagDhcpv6DIaIdPdInfo' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Server.Binding.Clients.Client.IaIdPd.BagDhcpv6DIaIdPdInfo',
            False, 
            [
            _MetaInfoClassMember('addresses', REFERENCE_CLASS, 'Addresses' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Server.Binding.Clients.Client.IaIdPd.BagDhcpv6DIaIdPdInfo.Addresses', 
                [], [], 
                '''                List of addresses in this IA
                ''',
                'addresses',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('flags', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                FSM Flag for this IA
                ''',
                'flags',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('ia-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IA_ID of this IA
                ''',
                'ia_id',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('ia-type', REFERENCE_ENUM_CLASS, 'BagDhcpv6DIaIdEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'BagDhcpv6DIaIdEnum', 
                [], [], 
                '''                IA type
                ''',
                'ia_type',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'BagDhcpv6DFsmStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'BagDhcpv6DFsmStateEnum', 
                [], [], 
                '''                State
                ''',
                'state',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('total-address', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Total address in this IA
                ''',
                'total_address',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'bag-dhcpv6d-ia-id-pd-info',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Server.Binding.Clients.Client.IaIdPd' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Server.Binding.Clients.Client.IaIdPd',
            False, 
            [
            _MetaInfoClassMember('bag-dhcpv6d-ia-id-pd-info', REFERENCE_LIST, 'BagDhcpv6DIaIdPdInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Server.Binding.Clients.Client.IaIdPd.BagDhcpv6DIaIdPdInfo', 
                [], [], 
                '''                bag dhcpv6d ia id pd info
                ''',
                'bag_dhcpv6d_ia_id_pd_info',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'ia-id-pd',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Server.Binding.Clients.Client' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Server.Binding.Clients.Client',
            False, 
            [
            _MetaInfoClassMember('client-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Client ID
                ''',
                'client_id',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', True),
            _MetaInfoClassMember('access-vrf-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 33)], [], 
                '''                DHCPV6 access VRF name to client
                ''',
                'access_vrf_name',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('address-pool-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                DHCPV6 server address pool name
                ''',
                'address_pool_name',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('class-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                DHCPV6 class name
                ''',
                'class_name',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('client-flag', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                DHCPV6 client flag
                ''',
                'client_flag',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('client-id-xr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Client unique identifier
                ''',
                'client_id_xr',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('dns-server-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                DNS server count
                ''',
                'dns_server_count',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('duid', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Client DUID
                ''',
                'duid',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('framed-ipv6-prefix', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                DHCPV6 framed ipv6 addess used by ND
                ''',
                'framed_ipv6_prefix',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('framed-prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                DHCPV6 framed ipv6 prefix length used by ND
                ''',
                'framed_prefix_length',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('ia-id-p-ds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of ia_id/pd
                ''',
                'ia_id_p_ds',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('ia-id-pd', REFERENCE_CLASS, 'IaIdPd' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Server.Binding.Clients.Client.IaIdPd', 
                [], [], 
                '''                List of DHCPv6 IA_ID/PDs
                ''',
                'ia_id_pd',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                DHCPV6 access interface to client
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('is-nak-next-renew', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is true if DHCPv6 next renew from client will be
                NAK'd
                ''',
                'is_nak_next_renew',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('link-local-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                DHCPV6 IPv6 client link local address
                ''',
                'link_local_address',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('mac-address', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Client MAC address
                ''',
                'mac_address',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('pool-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                DHCPV6 pool name
                ''',
                'pool_name',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('prefix-pool-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                DHCPV6 server prefix pool name
                ''',
                'prefix_pool_name',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('profile-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                DHCPV6 profile name
                ''',
                'profile_name',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('rx-interface-id', ATTRIBUTE, 'str' , None, None, 
                [(0, 771)], [], 
                '''                DHCPV6 received Interface ID
                ''',
                'rx_interface_id',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('rx-remote-id', ATTRIBUTE, 'str' , None, None, 
                [(0, 771)], [], 
                '''                DHCPV6 received Remote ID
                ''',
                'rx_remote_id',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('serg-intf-role', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                DHCPV6 SERG Intf Role
                ''',
                'serg_intf_role',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('server-binding-inner-tag', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                DHCPV6 VLAN Inner VLAN
                ''',
                'server_binding_inner_tag',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('server-binding-outer-tag', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                DHCPV6 VLAN Outer VLAN
                ''',
                'server_binding_outer_tag',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('server-binding-tags', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                DHCPV6 VLAN tag count
                ''',
                'server_binding_tags',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('sesrg-state', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                DHCPV6 SERG state
                ''',
                'sesrg_state',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('srg-intf-role', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                DHCPV6 SRG Intf Role
                ''',
                'srg_intf_role',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('srg-state', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                DHCPV6 SRG state
                ''',
                'srg_state',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('srg-vrf-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 33)], [], 
                '''                DHCPV6 SRG VRF NAME
                ''',
                'srg_vrf_name',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('srgp2p', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                SRG P2P Status
                ''',
                'srgp2p',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('subscriber-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                DHCPV6 subscriber label
                ''',
                'subscriber_label',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 33)], [], 
                '''                DHCPVV6 client/subscriber VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'client',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Server.Binding.Clients' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Server.Binding.Clients',
            False, 
            [
            _MetaInfoClassMember('client', REFERENCE_LIST, 'Client' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Server.Binding.Clients.Client', 
                [], [], 
                '''                Single DHCPV6 server binding
                ''',
                'client',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'clients',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Server.Binding' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Server.Binding',
            False, 
            [
            _MetaInfoClassMember('clients', REFERENCE_CLASS, 'Clients' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Server.Binding.Clients', 
                [], [], 
                '''                DHCPV6 server client bindings
                ''',
                'clients',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('summary', REFERENCE_CLASS, 'Summary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Server.Binding.Summary', 
                [], [], 
                '''                DHCPV6 server binding summary
                ''',
                'summary',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'binding',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Solicit' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Solicit',
            False, 
            [
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped packets
                ''',
                'dropped_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('transmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmitted packets
                ''',
                'transmitted_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'solicit',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Advertise' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Advertise',
            False, 
            [
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped packets
                ''',
                'dropped_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('transmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmitted packets
                ''',
                'transmitted_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'advertise',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Request' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Request',
            False, 
            [
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped packets
                ''',
                'dropped_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('transmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmitted packets
                ''',
                'transmitted_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'request',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Reply' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Reply',
            False, 
            [
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped packets
                ''',
                'dropped_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('transmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmitted packets
                ''',
                'transmitted_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'reply',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Confirm' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Confirm',
            False, 
            [
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped packets
                ''',
                'dropped_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('transmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmitted packets
                ''',
                'transmitted_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'confirm',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Decline' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Decline',
            False, 
            [
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped packets
                ''',
                'dropped_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('transmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmitted packets
                ''',
                'transmitted_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'decline',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Renew' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Renew',
            False, 
            [
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped packets
                ''',
                'dropped_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('transmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmitted packets
                ''',
                'transmitted_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'renew',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Rebind' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Rebind',
            False, 
            [
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped packets
                ''',
                'dropped_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('transmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmitted packets
                ''',
                'transmitted_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'rebind',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Release' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Release',
            False, 
            [
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped packets
                ''',
                'dropped_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('transmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmitted packets
                ''',
                'transmitted_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'release',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Reconfig' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Reconfig',
            False, 
            [
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped packets
                ''',
                'dropped_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('transmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmitted packets
                ''',
                'transmitted_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'reconfig',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Inform' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Inform',
            False, 
            [
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped packets
                ''',
                'dropped_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('transmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmitted packets
                ''',
                'transmitted_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'inform',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.RelayForward' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.RelayForward',
            False, 
            [
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped packets
                ''',
                'dropped_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('transmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmitted packets
                ''',
                'transmitted_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'relay-forward',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.RelayReply' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.RelayReply',
            False, 
            [
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped packets
                ''',
                'dropped_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('transmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmitted packets
                ''',
                'transmitted_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'relay-reply',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.LeaseQuery' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.LeaseQuery',
            False, 
            [
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped packets
                ''',
                'dropped_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('transmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmitted packets
                ''',
                'transmitted_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'lease-query',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.LeaseQueryReply' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.LeaseQueryReply',
            False, 
            [
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped packets
                ''',
                'dropped_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('transmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmitted packets
                ''',
                'transmitted_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'lease-query-reply',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.LeaseQueryDone' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.LeaseQueryDone',
            False, 
            [
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped packets
                ''',
                'dropped_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('transmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmitted packets
                ''',
                'transmitted_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'lease-query-done',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.LeaseQueryData' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.LeaseQueryData',
            False, 
            [
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped packets
                ''',
                'dropped_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('transmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmitted packets
                ''',
                'transmitted_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'lease-query-data',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics',
            False, 
            [
            _MetaInfoClassMember('advertise', REFERENCE_CLASS, 'Advertise' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Advertise', 
                [], [], 
                '''                DHCPV6 advertise packets
                ''',
                'advertise',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('confirm', REFERENCE_CLASS, 'Confirm' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Confirm', 
                [], [], 
                '''                DHCPV6 confirm packets
                ''',
                'confirm',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('decline', REFERENCE_CLASS, 'Decline' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Decline', 
                [], [], 
                '''                DHCPV6 decline packets
                ''',
                'decline',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('inform', REFERENCE_CLASS, 'Inform' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Inform', 
                [], [], 
                '''                DHCPV6 inform packets
                ''',
                'inform',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('lease-query', REFERENCE_CLASS, 'LeaseQuery' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.LeaseQuery', 
                [], [], 
                '''                DHCPV6 lease query packets
                ''',
                'lease_query',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('lease-query-data', REFERENCE_CLASS, 'LeaseQueryData' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.LeaseQueryData', 
                [], [], 
                '''                DHCPV6 lease query data packets
                ''',
                'lease_query_data',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('lease-query-done', REFERENCE_CLASS, 'LeaseQueryDone' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.LeaseQueryDone', 
                [], [], 
                '''                DHCPV6 lease query done packets
                ''',
                'lease_query_done',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('lease-query-reply', REFERENCE_CLASS, 'LeaseQueryReply' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.LeaseQueryReply', 
                [], [], 
                '''                DHCPV6 lease query reply packets
                ''',
                'lease_query_reply',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('rebind', REFERENCE_CLASS, 'Rebind' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Rebind', 
                [], [], 
                '''                DHCPV6 rebind packets
                ''',
                'rebind',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('reconfig', REFERENCE_CLASS, 'Reconfig' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Reconfig', 
                [], [], 
                '''                DHCPV6 reconfig packets
                ''',
                'reconfig',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('relay-forward', REFERENCE_CLASS, 'RelayForward' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.RelayForward', 
                [], [], 
                '''                DHCPV6 relay forward packets
                ''',
                'relay_forward',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('relay-reply', REFERENCE_CLASS, 'RelayReply' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.RelayReply', 
                [], [], 
                '''                DHCPV6 relay reply packets
                ''',
                'relay_reply',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('release', REFERENCE_CLASS, 'Release' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Release', 
                [], [], 
                '''                DHCPV6 release packets
                ''',
                'release',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('renew', REFERENCE_CLASS, 'Renew' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Renew', 
                [], [], 
                '''                DHCPV6 renew packets
                ''',
                'renew',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('reply', REFERENCE_CLASS, 'Reply' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Reply', 
                [], [], 
                '''                DHCPV6 reply packets
                ''',
                'reply',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('request', REFERENCE_CLASS, 'Request' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Request', 
                [], [], 
                '''                DHCPV6 request packets
                ''',
                'request',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('solicit', REFERENCE_CLASS, 'Solicit' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Solicit', 
                [], [], 
                '''                DHCPV6 solicit packets
                ''',
                'solicit',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Server.Vrfs.Vrf' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Server.Vrfs.Vrf',
            False, 
            [
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', True),
            _MetaInfoClassMember('statistics', REFERENCE_CLASS, 'Statistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics', 
                [], [], 
                '''                IPv6 DHCP server statistics
                ''',
                'statistics',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'vrf',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Server.Vrfs' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Server.Vrfs',
            False, 
            [
            _MetaInfoClassMember('vrf', REFERENCE_LIST, 'Vrf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Server.Vrfs.Vrf', 
                [], [], 
                '''                IPv6 DHCP server VRF name
                ''',
                'vrf',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'vrfs',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Server.Profiles.Profile.Info.Lease' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Server.Profiles.Profile.Info.Lease',
            False, 
            [
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                DHCPV6 client lease in seconds
                ''',
                'seconds',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('time', ATTRIBUTE, 'str' , None, None, 
                [(0, 10)], [], 
                '''                Time in format HH:MM:SS
                ''',
                'time',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'lease',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Server.Profiles.Profile.Info.InterfaceReferences.Ipv6Dhcpv6DServerInterfaceReference' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Server.Profiles.Profile.Info.InterfaceReferences.Ipv6Dhcpv6DServerInterfaceReference',
            False, 
            [
            _MetaInfoClassMember('server-reference-interface-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                Interface name
                ''',
                'server_reference_interface_name',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'ipv6-dhcpv6d-server-interface-reference',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Server.Profiles.Profile.Info.InterfaceReferences' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Server.Profiles.Profile.Info.InterfaceReferences',
            False, 
            [
            _MetaInfoClassMember('ipv6-dhcpv6d-server-interface-reference', REFERENCE_LIST, 'Ipv6Dhcpv6DServerInterfaceReference' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Server.Profiles.Profile.Info.InterfaceReferences.Ipv6Dhcpv6DServerInterfaceReference', 
                [], [], 
                '''                ipv6 dhcpv6d server interface reference
                ''',
                'ipv6_dhcpv6d_server_interface_reference',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'interface-references',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Server.Profiles.Profile.Info' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Server.Profiles.Profile.Info',
            False, 
            [
            _MetaInfoClassMember('aftr-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                Server aftr name
                ''',
                'aftr_name',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('delegated-prefix-pool-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                Server delegated prefix pool name
                ''',
                'delegated_prefix_pool_name',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('domain-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                Server domain name
                ''',
                'domain_name',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('framed-addr-pool-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                Server framed address pool name
                ''',
                'framed_addr_pool_name',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('interface-references', REFERENCE_CLASS, 'InterfaceReferences' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Server.Profiles.Profile.Info.InterfaceReferences', 
                [], [], 
                '''                Interface references
                ''',
                'interface_references',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('lease', REFERENCE_CLASS, 'Lease' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Server.Profiles.Profile.Info.Lease', 
                [], [], 
                '''                Server lease time
                ''',
                'lease',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('profile-dns', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                DNS address count
                ''',
                'profile_dns',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('profile-dns-address', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                DNS addresses
                ''',
                'profile_dns_address',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False, max_elements=8),
            _MetaInfoClassMember('profile-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                Server profile name
                ''',
                'profile_name',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('rapid-commit', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Rapid Commit
                ''',
                'rapid_commit',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'info',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Server.Profiles.Profile.ThrottleInfos.ThrottleInfo' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Server.Profiles.Profile.ThrottleInfos.ThrottleInfo',
            False, 
            [
            _MetaInfoClassMember('mac-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                MAC address
                ''',
                'mac_address',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', True),
            _MetaInfoClassMember('binding-chaddr', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Client MAC address
                ''',
                'binding_chaddr',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('ifname', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                DHCP access interface
                ''',
                'ifname',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('state', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                State of entry
                ''',
                'state',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('time-left', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Time Left in secs
                ''',
                'time_left',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'throttle-info',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Server.Profiles.Profile.ThrottleInfos' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Server.Profiles.Profile.ThrottleInfos',
            False, 
            [
            _MetaInfoClassMember('throttle-info', REFERENCE_LIST, 'ThrottleInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Server.Profiles.Profile.ThrottleInfos.ThrottleInfo', 
                [], [], 
                '''                IPv6 DHCP server profile Throttle Info
                ''',
                'throttle_info',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'throttle-infos',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Server.Profiles.Profile' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Server.Profiles.Profile',
            False, 
            [
            _MetaInfoClassMember('profile-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Profile name
                ''',
                'profile_name',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', True),
            _MetaInfoClassMember('info', REFERENCE_CLASS, 'Info' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Server.Profiles.Profile.Info', 
                [], [], 
                '''                IPv6 DHCP server profile Info
                ''',
                'info',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('throttle-infos', REFERENCE_CLASS, 'ThrottleInfos' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Server.Profiles.Profile.ThrottleInfos', 
                [], [], 
                '''                DHCPV6 throttle table
                ''',
                'throttle_infos',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'profile',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Server.Profiles' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Server.Profiles',
            False, 
            [
            _MetaInfoClassMember('profile', REFERENCE_LIST, 'Profile' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Server.Profiles.Profile', 
                [], [], 
                '''                IPv6 DHCP server profile
                ''',
                'profile',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'profiles',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Server.Interfaces.Interface' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Server.Interfaces.Interface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', True),
            _MetaInfoClassMember('is-server-interface-ambiguous', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Is interface ambiguous
                ''',
                'is_server_interface_ambiguous',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('mac-throttle', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Mac Throttle Status
                ''',
                'mac_throttle',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('serg-role', REFERENCE_ENUM_CLASS, 'BagDhcpv6DIntfSergRoleEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'BagDhcpv6DIntfSergRoleEnum', 
                [], [], 
                '''                DHCPv6 Interface SERG role
                ''',
                'serg_role',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('server-interface-lease-limit-type', REFERENCE_ENUM_CLASS, 'LeaseLimitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'LeaseLimitEnum', 
                [], [], 
                '''                Lease limit type on interface
                ''',
                'server_interface_lease_limit_type',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('server-interface-lease-limits', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Lease limit count on interface
                ''',
                'server_interface_lease_limits',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('server-interface-mode', REFERENCE_ENUM_CLASS, 'BagDhcpv6DSubModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'BagDhcpv6DSubModeEnum', 
                [], [], 
                '''                Mode of interface
                ''',
                'server_interface_mode',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('server-interface-profile-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                Name of profile attached to the interface
                ''',
                'server_interface_profile_name',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('server-vrf-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 33)], [], 
                '''                VRF name
                ''',
                'server_vrf_name',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('srg-role', REFERENCE_ENUM_CLASS, 'BagDhcpv6DIntfSrgRoleEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'BagDhcpv6DIntfSrgRoleEnum', 
                [], [], 
                '''                DHCPv6 Interface SRG role
                ''',
                'srg_role',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('srg-vrf-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 33)], [], 
                '''                SRG VRF name
                ''',
                'srg_vrf_name',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('srgp2p', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                SRG P2P Status
                ''',
                'srgp2p',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Server.Interfaces' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Server.Interfaces',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Server.Interfaces.Interface', 
                [], [], 
                '''                IPv6 DHCP server interface
                ''',
                'interface',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Server.Statistics.Ipv6Dhcpv6DServerStat.Statistics_' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Server.Statistics.Ipv6Dhcpv6DServerStat.Statistics_',
            False, 
            [
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped packets
                ''',
                'dropped_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('transmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmitted packets
                ''',
                'transmitted_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Server.Statistics.Ipv6Dhcpv6DServerStat' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Server.Statistics.Ipv6Dhcpv6DServerStat',
            False, 
            [
            _MetaInfoClassMember('statistics', REFERENCE_CLASS, 'Statistics_' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Server.Statistics.Ipv6Dhcpv6DServerStat.Statistics_', 
                [], [], 
                '''                Server statistics
                ''',
                'statistics',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 33)], [], 
                '''                DHCPv6 L3 VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'ipv6-dhcpv6d-server-stat',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Server.Statistics' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Server.Statistics',
            False, 
            [
            _MetaInfoClassMember('ipv6-dhcpv6d-server-stat', REFERENCE_LIST, 'Ipv6Dhcpv6DServerStat' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Server.Statistics.Ipv6Dhcpv6DServerStat', 
                [], [], 
                '''                ipv6 dhcpv6d server stat
                ''',
                'ipv6_dhcpv6d_server_stat',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Server.BindingOptions.MacBindOptions.MacBindOption' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Server.BindingOptions.MacBindOptions.MacBindOption',
            False, 
            [
            _MetaInfoClassMember('mac-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                MAC address
                ''',
                'mac_address',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', True),
            _MetaInfoClassMember('dns-address', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                DNS addresses
                ''',
                'dns_address',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False, max_elements=8),
            _MetaInfoClassMember('dns-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                DNS address count
                ''',
                'dns_count',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('duid-xr', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Client DUID
                ''',
                'duid_xr',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('mac-address-xr', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Client MAC address
                ''',
                'mac_address_xr',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('opt17', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Client Option 17 value
                ''',
                'opt17',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'mac-bind-option',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Server.BindingOptions.MacBindOptions' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Server.BindingOptions.MacBindOptions',
            False, 
            [
            _MetaInfoClassMember('mac-bind-option', REFERENCE_LIST, 'MacBindOption' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Server.BindingOptions.MacBindOptions.MacBindOption', 
                [], [], 
                '''                DHCPv6 server binding with options
                ''',
                'mac_bind_option',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'mac-bind-options',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Server.BindingOptions.DuidBindOptions.DuidBindOption' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Server.BindingOptions.DuidBindOptions.DuidBindOption',
            False, 
            [
            _MetaInfoClassMember('duid', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                DUID of Binding
                ''',
                'duid',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', True),
            _MetaInfoClassMember('dns-address', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                DNS addresses
                ''',
                'dns_address',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False, max_elements=8),
            _MetaInfoClassMember('dns-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                DNS address count
                ''',
                'dns_count',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('duid-xr', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Client DUID
                ''',
                'duid_xr',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('mac-address-xr', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Client MAC address
                ''',
                'mac_address_xr',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('opt17', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Client Option 17 value
                ''',
                'opt17',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'duid-bind-option',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Server.BindingOptions.DuidBindOptions' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Server.BindingOptions.DuidBindOptions',
            False, 
            [
            _MetaInfoClassMember('duid-bind-option', REFERENCE_LIST, 'DuidBindOption' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Server.BindingOptions.DuidBindOptions.DuidBindOption', 
                [], [], 
                '''                DHCPv6 server binding with options
                ''',
                'duid_bind_option',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'duid-bind-options',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Server.BindingOptions' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Server.BindingOptions',
            False, 
            [
            _MetaInfoClassMember('duid-bind-options', REFERENCE_CLASS, 'DuidBindOptions' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Server.BindingOptions.DuidBindOptions', 
                [], [], 
                '''                DHCPv6 server binding from DUID
                ''',
                'duid_bind_options',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('mac-bind-options', REFERENCE_CLASS, 'MacBindOptions' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Server.BindingOptions.MacBindOptions', 
                [], [], 
                '''                DHCPv6 server binding from MAC address
                ''',
                'mac_bind_options',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'binding-options',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Server' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Server',
            False, 
            [
            _MetaInfoClassMember('binding', REFERENCE_CLASS, 'Binding' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Server.Binding', 
                [], [], 
                '''                DHCPV6 server bindings
                ''',
                'binding',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('binding-options', REFERENCE_CLASS, 'BindingOptions' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Server.BindingOptions', 
                [], [], 
                '''                DHCPv6 server binding with options
                ''',
                'binding_options',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Server.Interfaces', 
                [], [], 
                '''                DHCPV6 server interface
                ''',
                'interfaces',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('profiles', REFERENCE_CLASS, 'Profiles' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Server.Profiles', 
                [], [], 
                '''                IPv6 DHCP server profile
                ''',
                'profiles',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('statistics', REFERENCE_CLASS, 'Statistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Server.Statistics', 
                [], [], 
                '''                DHCPv6 server statistics
                ''',
                'statistics',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('vrfs', REFERENCE_CLASS, 'Vrfs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Server.Vrfs', 
                [], [], 
                '''                DHCPV6 server list of VRF names
                ''',
                'vrfs',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'server',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Relay.Statistics.Ipv6Dhcpv6DRelayStat.Statistics_' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Relay.Statistics.Ipv6Dhcpv6DRelayStat.Statistics_',
            False, 
            [
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped packets
                ''',
                'dropped_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('transmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmitted packets
                ''',
                'transmitted_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Relay.Statistics.Ipv6Dhcpv6DRelayStat' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Relay.Statistics.Ipv6Dhcpv6DRelayStat',
            False, 
            [
            _MetaInfoClassMember('statistics', REFERENCE_CLASS, 'Statistics_' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Relay.Statistics.Ipv6Dhcpv6DRelayStat.Statistics_', 
                [], [], 
                '''                Relay statistics
                ''',
                'statistics',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 33)], [], 
                '''                DHCPv6 L3 VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'ipv6-dhcpv6d-relay-stat',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Relay.Statistics' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Relay.Statistics',
            False, 
            [
            _MetaInfoClassMember('ipv6-dhcpv6d-relay-stat', REFERENCE_LIST, 'Ipv6Dhcpv6DRelayStat' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Relay.Statistics.Ipv6Dhcpv6DRelayStat', 
                [], [], 
                '''                ipv6 dhcpv6d relay stat
                ''',
                'ipv6_dhcpv6d_relay_stat',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Relay.Binding.Summary' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Relay.Binding.Summary',
            False, 
            [
            _MetaInfoClassMember('clients', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total number of clients
                ''',
                'clients',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'summary',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Relay.Binding.Clients.Client' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Relay.Binding.Clients.Client',
            False, 
            [
            _MetaInfoClassMember('client-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Client ID
                ''',
                'client_id',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', True),
            _MetaInfoClassMember('client-id-xr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Client unique identifier
                ''',
                'client_id_xr',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('duid', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Client DUID
                ''',
                'duid',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('ia-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IA_ID of this IA
                ''',
                'ia_id',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                Interface name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('lifetime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Client route lifetime
                ''',
                'lifetime',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('next-hop-addr', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                Next hop is our address
                ''',
                'next_hop_addr',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                DHCPV6 IPv6 Prefix allotted to client
                ''',
                'prefix',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                length of prefix
                ''',
                'prefix_length',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('relay-profile-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                Relay Profile name
                ''',
                'relay_profile_name',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('rem-life-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Client route remaining lifetime
                ''',
                'rem_life_time',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 33)], [], 
                '''                DHCPv6 client/subscriber Vrf name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'client',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Relay.Binding.Clients' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Relay.Binding.Clients',
            False, 
            [
            _MetaInfoClassMember('client', REFERENCE_LIST, 'Client' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Relay.Binding.Clients.Client', 
                [], [], 
                '''                Single DHCPV6 relay binding
                ''',
                'client',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'clients',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Relay.Binding' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Relay.Binding',
            False, 
            [
            _MetaInfoClassMember('clients', REFERENCE_CLASS, 'Clients' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Relay.Binding.Clients', 
                [], [], 
                '''                DHCPV6 relay client bindings
                ''',
                'clients',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('summary', REFERENCE_CLASS, 'Summary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Relay.Binding.Summary', 
                [], [], 
                '''                DHCPV6 relay binding summary
                ''',
                'summary',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'binding',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Solicit' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Solicit',
            False, 
            [
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped packets
                ''',
                'dropped_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('transmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmitted packets
                ''',
                'transmitted_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'solicit',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Advertise' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Advertise',
            False, 
            [
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped packets
                ''',
                'dropped_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('transmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmitted packets
                ''',
                'transmitted_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'advertise',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Request' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Request',
            False, 
            [
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped packets
                ''',
                'dropped_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('transmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmitted packets
                ''',
                'transmitted_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'request',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Reply' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Reply',
            False, 
            [
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped packets
                ''',
                'dropped_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('transmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmitted packets
                ''',
                'transmitted_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'reply',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Confirm' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Confirm',
            False, 
            [
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped packets
                ''',
                'dropped_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('transmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmitted packets
                ''',
                'transmitted_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'confirm',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Decline' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Decline',
            False, 
            [
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped packets
                ''',
                'dropped_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('transmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmitted packets
                ''',
                'transmitted_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'decline',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Renew' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Renew',
            False, 
            [
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped packets
                ''',
                'dropped_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('transmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmitted packets
                ''',
                'transmitted_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'renew',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Rebind' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Rebind',
            False, 
            [
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped packets
                ''',
                'dropped_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('transmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmitted packets
                ''',
                'transmitted_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'rebind',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Release' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Release',
            False, 
            [
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped packets
                ''',
                'dropped_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('transmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmitted packets
                ''',
                'transmitted_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'release',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Reconfig' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Reconfig',
            False, 
            [
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped packets
                ''',
                'dropped_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('transmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmitted packets
                ''',
                'transmitted_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'reconfig',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Inform' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Inform',
            False, 
            [
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped packets
                ''',
                'dropped_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('transmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmitted packets
                ''',
                'transmitted_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'inform',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.RelayForward' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.RelayForward',
            False, 
            [
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped packets
                ''',
                'dropped_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('transmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmitted packets
                ''',
                'transmitted_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'relay-forward',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.RelayReply' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.RelayReply',
            False, 
            [
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped packets
                ''',
                'dropped_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('transmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmitted packets
                ''',
                'transmitted_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'relay-reply',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.LeaseQuery' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.LeaseQuery',
            False, 
            [
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped packets
                ''',
                'dropped_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('transmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmitted packets
                ''',
                'transmitted_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'lease-query',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.LeaseQueryReply' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.LeaseQueryReply',
            False, 
            [
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped packets
                ''',
                'dropped_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('transmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmitted packets
                ''',
                'transmitted_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'lease-query-reply',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.LeaseQueryDone' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.LeaseQueryDone',
            False, 
            [
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped packets
                ''',
                'dropped_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('transmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmitted packets
                ''',
                'transmitted_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'lease-query-done',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.LeaseQueryData' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.LeaseQueryData',
            False, 
            [
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped packets
                ''',
                'dropped_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('transmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmitted packets
                ''',
                'transmitted_packets',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'lease-query-data',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics',
            False, 
            [
            _MetaInfoClassMember('advertise', REFERENCE_CLASS, 'Advertise' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Advertise', 
                [], [], 
                '''                DHCPV6 advertise packets
                ''',
                'advertise',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('confirm', REFERENCE_CLASS, 'Confirm' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Confirm', 
                [], [], 
                '''                DHCPV6 confirm packets
                ''',
                'confirm',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('decline', REFERENCE_CLASS, 'Decline' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Decline', 
                [], [], 
                '''                DHCPV6 decline packets
                ''',
                'decline',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('inform', REFERENCE_CLASS, 'Inform' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Inform', 
                [], [], 
                '''                DHCPV6 inform packets
                ''',
                'inform',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('lease-query', REFERENCE_CLASS, 'LeaseQuery' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.LeaseQuery', 
                [], [], 
                '''                DHCPV6 lease query packets
                ''',
                'lease_query',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('lease-query-data', REFERENCE_CLASS, 'LeaseQueryData' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.LeaseQueryData', 
                [], [], 
                '''                DHCPV6 lease query data packets
                ''',
                'lease_query_data',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('lease-query-done', REFERENCE_CLASS, 'LeaseQueryDone' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.LeaseQueryDone', 
                [], [], 
                '''                DHCPV6 lease query done packets
                ''',
                'lease_query_done',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('lease-query-reply', REFERENCE_CLASS, 'LeaseQueryReply' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.LeaseQueryReply', 
                [], [], 
                '''                DHCPV6 lease query reply packets
                ''',
                'lease_query_reply',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('rebind', REFERENCE_CLASS, 'Rebind' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Rebind', 
                [], [], 
                '''                DHCPV6 rebind packets
                ''',
                'rebind',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('reconfig', REFERENCE_CLASS, 'Reconfig' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Reconfig', 
                [], [], 
                '''                DHCPV6 reconfig packets
                ''',
                'reconfig',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('relay-forward', REFERENCE_CLASS, 'RelayForward' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.RelayForward', 
                [], [], 
                '''                DHCPV6 relay forward packets
                ''',
                'relay_forward',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('relay-reply', REFERENCE_CLASS, 'RelayReply' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.RelayReply', 
                [], [], 
                '''                DHCPV6 relay reply packets
                ''',
                'relay_reply',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('release', REFERENCE_CLASS, 'Release' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Release', 
                [], [], 
                '''                DHCPV6 release packets
                ''',
                'release',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('renew', REFERENCE_CLASS, 'Renew' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Renew', 
                [], [], 
                '''                DHCPV6 renew packets
                ''',
                'renew',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('reply', REFERENCE_CLASS, 'Reply' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Reply', 
                [], [], 
                '''                DHCPV6 reply packets
                ''',
                'reply',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('request', REFERENCE_CLASS, 'Request' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Request', 
                [], [], 
                '''                DHCPV6 request packets
                ''',
                'request',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('solicit', REFERENCE_CLASS, 'Solicit' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Solicit', 
                [], [], 
                '''                DHCPV6 solicit packets
                ''',
                'solicit',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf',
            False, 
            [
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', True),
            _MetaInfoClassMember('statistics', REFERENCE_CLASS, 'Statistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics', 
                [], [], 
                '''                IPv6 DHCP relay statistics
                ''',
                'statistics',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'vrf',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Relay.Vrfs' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Relay.Vrfs',
            False, 
            [
            _MetaInfoClassMember('vrf', REFERENCE_LIST, 'Vrf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf', 
                [], [], 
                '''                IPv6 DHCP relay VRF name
                ''',
                'vrf',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'vrfs',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node.Relay' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node.Relay',
            False, 
            [
            _MetaInfoClassMember('binding', REFERENCE_CLASS, 'Binding' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Relay.Binding', 
                [], [], 
                '''                DHCPV6 relay bindings
                ''',
                'binding',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('statistics', REFERENCE_CLASS, 'Statistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Relay.Statistics', 
                [], [], 
                '''                DHCPv6 relay statistics
                ''',
                'statistics',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('vrfs', REFERENCE_CLASS, 'Vrfs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Relay.Vrfs', 
                [], [], 
                '''                DHCPV6 relay list of VRF names
                ''',
                'vrfs',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'relay',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes.Node',
            False, 
            [
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Node name
                ''',
                'node_name',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', True),
            _MetaInfoClassMember('base', REFERENCE_CLASS, 'Base' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Base', 
                [], [], 
                '''                IPv6 DHCP Base
                ''',
                'base',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('proxy', REFERENCE_CLASS, 'Proxy' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Proxy', 
                [], [], 
                '''                IPv6 DHCP proxy operational data
                ''',
                'proxy',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('relay', REFERENCE_CLASS, 'Relay' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Relay', 
                [], [], 
                '''                IPv6 DHCP relay operational data
                ''',
                'relay',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('server', REFERENCE_CLASS, 'Server' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node.Server', 
                [], [], 
                '''                IPv6 DHCP server operational data
                ''',
                'server',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'node',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6.Nodes' : {
        'meta_info' : _MetaInfoClass('Dhcpv6.Nodes',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes.Node', 
                [], [], 
                '''                IPv6 DHCP particular node name
                ''',
                'node',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'nodes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
    'Dhcpv6' : {
        'meta_info' : _MetaInfoClass('Dhcpv6',
            False, 
            [
            _MetaInfoClassMember('issu-status', REFERENCE_CLASS, 'IssuStatus' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.IssuStatus', 
                [], [], 
                '''                DHCP IssuStatus
                ''',
                'issu_status',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper', 'Dhcpv6.Nodes', 
                [], [], 
                '''                IPv6 DHCP list of nodes
                ''',
                'nodes',
                'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-new-dhcpv6d-oper',
            'dhcpv6',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-new-dhcpv6d-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_new_dhcpv6d_oper'
        ),
    },
}
_meta_table['Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Solicit']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Advertise']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Request']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Reply']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Confirm']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Decline']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Renew']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Rebind']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Release']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Reconfig']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Inform']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.RelayForward']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.RelayReply']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.LeaseQuery']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.LeaseQueryReply']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.LeaseQueryDone']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.LeaseQueryData']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf.Statistics']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Proxy.Vrfs.Vrf']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Proxy.Vrfs']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.ThrottleInfos.ThrottleInfo']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.ThrottleInfos']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.Info.InterfaceIdReferences.Ipv6Dhcpv6DProxyIidReference']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.Info.InterfaceIdReferences']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.Info.VrfReferences.Ipv6Dhcpv6DProxyVrfReference']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.Info.VrfReferences']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.Info.InterfaceReferences.Ipv6Dhcpv6DProxyInterfaceReference']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.Info.InterfaceReferences']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.Info.InterfaceIdReferences']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.Info']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.Info.VrfReferences']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.Info']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.Info.InterfaceReferences']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.Info']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.ThrottleInfos']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Proxy.Profiles.Profile']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Proxy.Profiles.Profile.Info']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Proxy.Profiles.Profile']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Proxy.Profiles.Profile']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Proxy.Profiles']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Proxy.Interfaces.Interface']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Proxy.Interfaces']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Proxy.Statistics.Ipv6Dhcpv6DProxyStat.Statistics_']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Proxy.Statistics.Ipv6Dhcpv6DProxyStat']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Proxy.Statistics.Ipv6Dhcpv6DProxyStat']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Proxy.Statistics']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Proxy.Binding.Clients.Client.IaIdPd.BagDhcpv6DIaIdPdInfo.Addresses.BagDhcpv6DAddrAttrb']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Proxy.Binding.Clients.Client.IaIdPd.BagDhcpv6DIaIdPdInfo.Addresses']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Proxy.Binding.Clients.Client.IaIdPd.BagDhcpv6DIaIdPdInfo.Addresses']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Proxy.Binding.Clients.Client.IaIdPd.BagDhcpv6DIaIdPdInfo']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Proxy.Binding.Clients.Client.IaIdPd.BagDhcpv6DIaIdPdInfo']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Proxy.Binding.Clients.Client.IaIdPd']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Proxy.Binding.Clients.Client.IaIdPd']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Proxy.Binding.Clients.Client']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Proxy.Binding.Clients.Client']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Proxy.Binding.Clients']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Proxy.Binding.Summary.Iana']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Proxy.Binding.Summary']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Proxy.Binding.Summary.Iapd']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Proxy.Binding.Summary']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Proxy.Binding.Clients']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Proxy.Binding']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Proxy.Binding.Summary']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Proxy.Binding']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Proxy.Vrfs']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Proxy']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Proxy.Profiles']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Proxy']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Proxy.Interfaces']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Proxy']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Proxy.Statistics']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Proxy']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Proxy.Binding']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Proxy']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Base.AddrBindings.AddrBinding']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Base.AddrBindings']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Base.Database']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Base']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Base.AddrBindings']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Base']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Server.Binding.Summary.Iana']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Server.Binding.Summary']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Server.Binding.Summary.Iapd']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Server.Binding.Summary']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Server.Binding.Clients.Client.IaIdPd.BagDhcpv6DIaIdPdInfo.Addresses.BagDhcpv6DAddrAttrb']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Server.Binding.Clients.Client.IaIdPd.BagDhcpv6DIaIdPdInfo.Addresses']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Server.Binding.Clients.Client.IaIdPd.BagDhcpv6DIaIdPdInfo.Addresses']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Server.Binding.Clients.Client.IaIdPd.BagDhcpv6DIaIdPdInfo']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Server.Binding.Clients.Client.IaIdPd.BagDhcpv6DIaIdPdInfo']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Server.Binding.Clients.Client.IaIdPd']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Server.Binding.Clients.Client.IaIdPd']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Server.Binding.Clients.Client']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Server.Binding.Clients.Client']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Server.Binding.Clients']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Server.Binding.Summary']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Server.Binding']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Server.Binding.Clients']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Server.Binding']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Solicit']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Advertise']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Request']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Reply']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Confirm']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Decline']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Renew']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Rebind']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Release']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Reconfig']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.Inform']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.RelayForward']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.RelayReply']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.LeaseQuery']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.LeaseQueryReply']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.LeaseQueryDone']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics.LeaseQueryData']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Server.Vrfs.Vrf.Statistics']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Server.Vrfs.Vrf']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Server.Vrfs.Vrf']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Server.Vrfs']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Server.Profiles.Profile.Info.InterfaceReferences.Ipv6Dhcpv6DServerInterfaceReference']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Server.Profiles.Profile.Info.InterfaceReferences']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Server.Profiles.Profile.Info.Lease']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Server.Profiles.Profile.Info']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Server.Profiles.Profile.Info.InterfaceReferences']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Server.Profiles.Profile.Info']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Server.Profiles.Profile.ThrottleInfos.ThrottleInfo']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Server.Profiles.Profile.ThrottleInfos']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Server.Profiles.Profile.Info']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Server.Profiles.Profile']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Server.Profiles.Profile.ThrottleInfos']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Server.Profiles.Profile']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Server.Profiles.Profile']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Server.Profiles']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Server.Interfaces.Interface']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Server.Interfaces']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Server.Statistics.Ipv6Dhcpv6DServerStat.Statistics_']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Server.Statistics.Ipv6Dhcpv6DServerStat']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Server.Statistics.Ipv6Dhcpv6DServerStat']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Server.Statistics']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Server.BindingOptions.MacBindOptions.MacBindOption']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Server.BindingOptions.MacBindOptions']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Server.BindingOptions.DuidBindOptions.DuidBindOption']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Server.BindingOptions.DuidBindOptions']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Server.BindingOptions.MacBindOptions']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Server.BindingOptions']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Server.BindingOptions.DuidBindOptions']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Server.BindingOptions']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Server.Binding']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Server']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Server.Vrfs']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Server']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Server.Profiles']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Server']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Server.Interfaces']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Server']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Server.Statistics']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Server']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Server.BindingOptions']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Server']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Relay.Statistics.Ipv6Dhcpv6DRelayStat.Statistics_']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Relay.Statistics.Ipv6Dhcpv6DRelayStat']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Relay.Statistics.Ipv6Dhcpv6DRelayStat']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Relay.Statistics']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Relay.Binding.Clients.Client']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Relay.Binding.Clients']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Relay.Binding.Summary']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Relay.Binding']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Relay.Binding.Clients']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Relay.Binding']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Solicit']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Advertise']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Request']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Reply']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Confirm']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Decline']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Renew']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Rebind']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Release']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Reconfig']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.Inform']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.RelayForward']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.RelayReply']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.LeaseQuery']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.LeaseQueryReply']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.LeaseQueryDone']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics.LeaseQueryData']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf.Statistics']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Relay.Vrfs.Vrf']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Relay.Vrfs']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Relay.Statistics']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Relay']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Relay.Binding']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Relay']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Relay.Vrfs']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node.Relay']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Proxy']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Base']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Server']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node']['meta_info']
_meta_table['Dhcpv6.Nodes.Node.Relay']['meta_info'].parent =_meta_table['Dhcpv6.Nodes.Node']['meta_info']
_meta_table['Dhcpv6.Nodes.Node']['meta_info'].parent =_meta_table['Dhcpv6.Nodes']['meta_info']
_meta_table['Dhcpv6.IssuStatus']['meta_info'].parent =_meta_table['Dhcpv6']['meta_info']
_meta_table['Dhcpv6.Nodes']['meta_info'].parent =_meta_table['Dhcpv6']['meta_info']
