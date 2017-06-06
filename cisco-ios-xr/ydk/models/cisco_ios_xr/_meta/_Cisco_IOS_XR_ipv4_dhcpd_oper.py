


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'DhcpIssuPhaseEnum' : _MetaInfoEnum('DhcpIssuPhaseEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper',
        {
            'phase-not-started':'phase_not_started',
            'phase-load':'phase_load',
            'phase-run':'phase_run',
            'phase-completed':'phase_completed',
            'phase-aborted':'phase_aborted',
        }, 'Cisco-IOS-XR-ipv4-dhcpd-oper', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper']),
    'DhcpIssuVersionEnum' : _MetaInfoEnum('DhcpIssuVersionEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper',
        {
            'version1':'version1',
            'version2':'version2',
        }, 'Cisco-IOS-XR-ipv4-dhcpd-oper', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper']),
    'BagDhcpdProxyStateEnum' : _MetaInfoEnum('BagDhcpdProxyStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper',
        {
            'initializing':'initializing',
            'selecting':'selecting',
            'requesting':'requesting',
            'bound':'bound',
            'renewing':'renewing',
            'informing':'informing',
            'deleting':'deleting',
            'create-dpm':'create_dpm',
            'offer-sent':'offer_sent',
            'update-dpm':'update_dpm',
            'route-install':'route_install',
            'disc-dpm':'disc_dpm',
            'renew-new-intf':'renew_new_intf',
            'other-intf-dpm':'other_intf_dpm',
            'request-dpm':'request_dpm',
            'change-addr-dpm':'change_addr_dpm',
            'max':'max',
        }, 'Cisco-IOS-XR-ipv4-dhcpd-oper', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper']),
    'RelayInfoAuthenticateEnum' : _MetaInfoEnum('RelayInfoAuthenticateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper',
        {
            'received':'received',
            'inserted':'inserted',
        }, 'Cisco-IOS-XR-ipv4-dhcpd-oper', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper']),
    'RelayInfoPolicyEnum' : _MetaInfoEnum('RelayInfoPolicyEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper',
        {
            'replace':'replace',
            'keep':'keep',
            'drop':'drop',
            'encapsulate':'encapsulate',
        }, 'Cisco-IOS-XR-ipv4-dhcpd-oper', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper']),
    'DhcpIssuRoleEnum' : _MetaInfoEnum('DhcpIssuRoleEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper',
        {
            'role-primary':'role_primary',
            'role-secondary':'role_secondary',
        }, 'Cisco-IOS-XR-ipv4-dhcpd-oper', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper']),
    'RelayInfoVpnModeEnum' : _MetaInfoEnum('RelayInfoVpnModeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper',
        {
            'rfc':'rfc',
            'cisco':'cisco',
        }, 'Cisco-IOS-XR-ipv4-dhcpd-oper', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper']),
    'BroadcastFlagEnum' : _MetaInfoEnum('BroadcastFlagEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper',
        {
            'ignore':'ignore',
            'check':'check',
            'unicast-always':'unicast_always',
        }, 'Cisco-IOS-XR-ipv4-dhcpd-oper', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper']),
    'DhcpcIpv4StateEnum' : _MetaInfoEnum('DhcpcIpv4StateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper',
        {
            'init':'init',
            'init-reboot':'init_reboot',
            'rebooting':'rebooting',
            'selecting':'selecting',
            'requesting':'requesting',
            'bound':'bound',
            'renewing':'renewing',
            'rebinding':'rebinding',
            'invalid':'invalid',
        }, 'Cisco-IOS-XR-ipv4-dhcpd-oper', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper']),
    'ProxyLeaseLimitEnum' : _MetaInfoEnum('ProxyLeaseLimitEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper',
        {
            'none':'none',
            'interface':'interface',
            'circuit-id':'circuit_id',
            'remote-id':'remote_id',
            'remote-id-circuit-id':'remote_id_circuit_id',
        }, 'Cisco-IOS-XR-ipv4-dhcpd-oper', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper']),
    'BagDhcpdIntfSrgRoleEnum' : _MetaInfoEnum('BagDhcpdIntfSrgRoleEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper',
        {
            'none':'none',
            'master':'master',
            'slave':'slave',
        }, 'Cisco-IOS-XR-ipv4-dhcpd-oper', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper']),
    'DhcpClient.Nodes.Node.ClientStats.ClientStat' : {
        'meta_info' : _MetaInfoClass('DhcpClient.Nodes.Node.ClientStats.ClientStat',
            False, 
            [
            _MetaInfoClassMember('client-ifhandle', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Client Ifhandle
                ''',
                'client_ifhandle',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', True),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                Dhcp Client interface name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('num-broadcast-failed', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of broadcast packet send failed
                ''',
                'num_broadcast_failed',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('num-broadcast-packet-sent-success', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of broadcast packet sent successfully
                ''',
                'num_broadcast_packet_sent_success',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('num-create-event-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of create client event received
                ''',
                'num_create_event_received',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('num-declines-failed', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of decline send failed
                ''',
                'num_declines_failed',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('num-declines-sent-successfully', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of declines sent successfully
                ''',
                'num_declines_sent_successfully',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('num-delete-event-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of delete client event received
                ''',
                'num_delete_event_received',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('num-discovers-failed', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of discover send failed
                ''',
                'num_discovers_failed',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('num-discovers-sent-successfully', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of discovers sent successfully
                ''',
                'num_discovers_sent_successfully',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('num-events-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of events received
                ''',
                'num_events_received',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('num-init-timer-eventi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of init timer event
                ''',
                'num_init_timer_eventi',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('num-init-timer-start', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of init timer starts
                ''',
                'num_init_timer_start',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('num-init-timer-stop', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of init timer stops
                ''',
                'num_init_timer_stop',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('num-invalid-acks', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of invalid acks received
                ''',
                'num_invalid_acks',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('num-invalid-events', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of invalid events received
                ''',
                'num_invalid_events',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('num-invalid-nacks', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of invalid nacks received
                ''',
                'num_invalid_nacks',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('num-invalid-offers', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of invalid offers received
                ''',
                'num_invalid_offers',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('num-invalid-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of invalid packets dropped
                ''',
                'num_invalid_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('num-lease-timer-event', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Lease timer event
                ''',
                'num_lease_timer_event',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('num-lease-timer-start', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Lease timer starts
                ''',
                'num_lease_timer_start',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('num-lease-timer-stop', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Lease timer stops
                ''',
                'num_lease_timer_stop',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('num-packet-event-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of packet event received
                ''',
                'num_packet_event_received',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('num-rebinds-failed', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of rebind send failed
                ''',
                'num_rebinds_failed',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('num-rebinds-sent-successfully', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of rebinds sent successfully
                ''',
                'num_rebinds_sent_successfully',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('num-reboot-event-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of client rebooted event received
                ''',
                'num_reboot_event_received',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('num-reinit-event-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of reinit client event received
                ''',
                'num_reinit_event_received',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('num-releases-failed', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of release send failed
                ''',
                'num_releases_failed',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('num-releases-sent-successfully', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of releases sent successfully
                ''',
                'num_releases_sent_successfully',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('num-renews-failed', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of renew send failed
                ''',
                'num_renews_failed',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('num-renews-sent-successfully', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of renews sent successfully
                ''',
                'num_renews_sent_successfully',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('num-request-after-reboot-failed', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of requests sent after reboot failed
                ''',
                'num_request_after_reboot_failed',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('num-request-after-reboot-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of requests sent after reboot
                ''',
                'num_request_after_reboot_sent',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('num-requests-failed', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of request send failed
                ''',
                'num_requests_failed',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('num-requests-sent-successfully', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of requests sent successfully
                ''',
                'num_requests_sent_successfully',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('num-t1-timer-event', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of T1 timer event
                ''',
                'num_t1_timer_event',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('num-t1-timer-start', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of T1 timer starts
                ''',
                'num_t1_timer_start',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('num-t1-timer-stop', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of T1 timer stops
                ''',
                'num_t1_timer_stop',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('num-t2-timer-event', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of T2 timer event
                ''',
                'num_t2_timer_event',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('num-t2-timer-start', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of T2 timer starts
                ''',
                'num_t2_timer_start',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('num-t2-timer-stop', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of T2 timer stops
                ''',
                'num_t2_timer_stop',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('num-unicast-failed', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of unicast packet send failed
                ''',
                'num_unicast_failed',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('num-unicast-packet-sent-successfully', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of unicast packet sent successfully
                ''',
                'num_unicast_packet_sent_successfully',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('num-valid-acks-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of valid acks received
                ''',
                'num_valid_acks_received',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('num-valid-nacks-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of valid nacks received
                ''',
                'num_valid_nacks_received',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('num-valid-offers-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of valid offers received
                ''',
                'num_valid_offers_received',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('num-xid-mismatch', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of XID mismatch packets received
                ''',
                'num_xid_mismatch',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'client-stat',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'DhcpClient.Nodes.Node.ClientStats' : {
        'meta_info' : _MetaInfoClass('DhcpClient.Nodes.Node.ClientStats',
            False, 
            [
            _MetaInfoClassMember('client-stat', REFERENCE_LIST, 'ClientStat' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'DhcpClient.Nodes.Node.ClientStats.ClientStat', 
                [], [], 
                '''                DHCP client binding statistics
                ''',
                'client_stat',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'client-stats',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'DhcpClient.Nodes.Node.Clients.Client' : {
        'meta_info' : _MetaInfoClass('DhcpClient.Nodes.Node.Clients.Client',
            False, 
            [
            _MetaInfoClassMember('client-ifhandle', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Client Ifhandle
                ''',
                'client_ifhandle',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', True),
            _MetaInfoClassMember('client-id', ATTRIBUTE, 'str' , None, None, 
                [(0, 256)], [], 
                '''                Dhcp Client ID
                ''',
                'client_id',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('client-mac-address', ATTRIBUTE, 'str' , None, None, 
                [(0, 17)], [], 
                '''                Dhcp Client Interface MAC address
                ''',
                'client_mac_address',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                Dhcp Client interface name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Dhcp Client IP Address
                ''',
                'ipv4_address',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('ipv4-address-configured', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Dhcp Client IPV4 address configured in interface
                ''',
                'ipv4_address_configured',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('ipv4-client-state', REFERENCE_ENUM_CLASS, 'DhcpcIpv4StateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'DhcpcIpv4StateEnum', 
                [], [], 
                '''                Dhcp Client State
                ''',
                'ipv4_client_state',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('ipv4-lease-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Dhcp Client Lease time
                ''',
                'ipv4_lease_time',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('ipv4-rebind-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Dhcp Client Rebind time
                ''',
                'ipv4_rebind_time',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('ipv4-renew-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Dhcp Client Renew time
                ''',
                'ipv4_renew_time',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('ipv4-server-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Dhcp Client selected server IP Address
                ''',
                'ipv4_server_address',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('ipv4-subnet-mask', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Dhcp Client IP Address mask
                ''',
                'ipv4_subnet_mask',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('next-hop-ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Dhcp Client next hop IP Address
                ''',
                'next_hop_ipv4_address',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'client',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'DhcpClient.Nodes.Node.Clients' : {
        'meta_info' : _MetaInfoClass('DhcpClient.Nodes.Node.Clients',
            False, 
            [
            _MetaInfoClassMember('client', REFERENCE_LIST, 'Client' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'DhcpClient.Nodes.Node.Clients.Client', 
                [], [], 
                '''                Single DHCP client binding
                ''',
                'client',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'clients',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'DhcpClient.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('DhcpClient.Nodes.Node',
            False, 
            [
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Node name
                ''',
                'node_name',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', True),
            _MetaInfoClassMember('client-stats', REFERENCE_CLASS, 'ClientStats' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'DhcpClient.Nodes.Node.ClientStats', 
                [], [], 
                '''                IPv4 DHCP client statistics table
                ''',
                'client_stats',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('clients', REFERENCE_CLASS, 'Clients' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'DhcpClient.Nodes.Node.Clients', 
                [], [], 
                '''                IPv4 DHCP client table
                ''',
                'clients',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'node',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'DhcpClient.Nodes' : {
        'meta_info' : _MetaInfoClass('DhcpClient.Nodes',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'DhcpClient.Nodes.Node', 
                [], [], 
                '''                DHCP client particular node name
                ''',
                'node',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'nodes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'DhcpClient' : {
        'meta_info' : _MetaInfoClass('DhcpClient',
            False, 
            [
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'DhcpClient.Nodes', 
                [], [], 
                '''                DHCP client list of nodes
                ''',
                'nodes',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'dhcp-client',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Snoop.Bindings.Binding' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Snoop.Bindings.Binding',
            False, 
            [
            _MetaInfoClassMember('client-uid', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Client opaque handle
                ''',
                'client_uid',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', True),
            _MetaInfoClassMember('snoop-binding-bridge-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 74)], [], 
                '''                DHCP L2 bridge name
                ''',
                'snoop_binding_bridge_name',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('snoop-binding-ch-addr', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                DHCP client MAC address
                ''',
                'snoop_binding_ch_addr',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('snoop-binding-ch-addr-len', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                DHCP client MAC address length
                ''',
                'snoop_binding_ch_addr_len',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('snoop-binding-client-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                DHCP client id
                ''',
                'snoop_binding_client_id',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('snoop-binding-client-id-len', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                DHCP client id len
                ''',
                'snoop_binding_client_id_len',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('snoop-binding-i-addr', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                DHCP iaddr
                ''',
                'snoop_binding_i_addr',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('snoop-binding-lease', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                DHCP lease time
                ''',
                'snoop_binding_lease',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('snoop-binding-lease-start-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                DHCP lease start time
                ''',
                'snoop_binding_lease_start_time',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('snoop-binding-profile-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                DHCP profile name
                ''',
                'snoop_binding_profile_name',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('snoop-binding-state', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                DHCP sm state
                ''',
                'snoop_binding_state',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('snoop-bindng-interface-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 321)], [], 
                '''                DHCP interface to client
                ''',
                'snoop_bindng_interface_name',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'binding',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Snoop.Bindings' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Snoop.Bindings',
            False, 
            [
            _MetaInfoClassMember('binding', REFERENCE_LIST, 'Binding' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Snoop.Bindings.Binding', 
                [], [], 
                '''                DHCP Snoop binding
                ''',
                'binding',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'bindings',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Snoop.BindingStatistics' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Snoop.BindingStatistics',
            False, 
            [
            _MetaInfoClassMember('snoop-binding-timestamp', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Snoop binding timestamp
                ''',
                'snoop_binding_timestamp',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('snoop-binding-total', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total number of snoop bindings
                ''',
                'snoop_binding_total',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'binding-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Snoop.StatisticsInfo' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Snoop.StatisticsInfo',
            False, 
            [
            _MetaInfoClassMember('snoop-stats-timestamp', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Snoop Stats timestamp
                ''',
                'snoop_stats_timestamp',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'statistics-info',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Snoop.Profiles.Profile' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Snoop.Profiles.Profile',
            False, 
            [
            _MetaInfoClassMember('profile-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Profile name
                ''',
                'profile_name',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', True),
            _MetaInfoClassMember('snoop-profile-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                Profile Name
                ''',
                'snoop_profile_name',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('snoop-profile-relay-info-allow-untrusted', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Allow untrusted relay info
                ''',
                'snoop_profile_relay_info_allow_untrusted',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('snoop-profile-relay-info-option', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Relay info option
                ''',
                'snoop_profile_relay_info_option',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('snoop-profile-relay-info-policy', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Relay info policy
                ''',
                'snoop_profile_relay_info_policy',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('snoop-profile-trusted', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Trust
                ''',
                'snoop_profile_trusted',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('snoop-profile-uid', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Profile unique ID
                ''',
                'snoop_profile_uid',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'profile',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Snoop.Profiles' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Snoop.Profiles',
            False, 
            [
            _MetaInfoClassMember('profile', REFERENCE_LIST, 'Profile' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Snoop.Profiles.Profile', 
                [], [], 
                '''                DHCP Snoop profile
                ''',
                'profile',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'profiles',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Snoop.Statistics.Statistic' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Snoop.Statistics.Statistic',
            False, 
            [
            _MetaInfoClassMember('bridge-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Bridge domain name
                ''',
                'bridge_name',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', True),
            _MetaInfoClassMember('snoop-statistic', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Public snoop statistics
                ''',
                'snoop_statistic',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False, max_elements=45),
            _MetaInfoClassMember('snoop-statistics-bridge-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 74)], [], 
                '''                DHCP L2 bridge name
                ''',
                'snoop_statistics_bridge_name',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'statistic',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Snoop.Statistics' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Snoop.Statistics',
            False, 
            [
            _MetaInfoClassMember('statistic', REFERENCE_LIST, 'Statistic' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Snoop.Statistics.Statistic', 
                [], [], 
                '''                DHCP Snoop bridge domain statistics
                ''',
                'statistic',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Snoop' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Snoop',
            False, 
            [
            _MetaInfoClassMember('binding-statistics', REFERENCE_CLASS, 'BindingStatistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Snoop.BindingStatistics', 
                [], [], 
                '''                DHCP snoop binding statistics
                ''',
                'binding_statistics',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('bindings', REFERENCE_CLASS, 'Bindings' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Snoop.Bindings', 
                [], [], 
                '''                DHCP Snoop Bindings
                ''',
                'bindings',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('profiles', REFERENCE_CLASS, 'Profiles' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Snoop.Profiles', 
                [], [], 
                '''                DHCP Snoop Profile
                ''',
                'profiles',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('statistics', REFERENCE_CLASS, 'Statistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Snoop.Statistics', 
                [], [], 
                '''                DHCP Snoop Statistics
                ''',
                'statistics',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('statistics-info', REFERENCE_CLASS, 'StatisticsInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Snoop.StatisticsInfo', 
                [], [], 
                '''                DHCP snoop statistics info
                ''',
                'statistics_info',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'snoop',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes.Node.Proxy.StatisticsInfo' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes.Node.Proxy.StatisticsInfo',
            False, 
            [
            _MetaInfoClassMember('proxy-stats-timestamp', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Proxy Stats timestamp
                ''',
                'proxy_stats_timestamp',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'statistics-info',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Discover' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Discover',
            False, 
            [
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped packets
                ''',
                'dropped_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('transmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmitted packets
                ''',
                'transmitted_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'discover',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Offer' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Offer',
            False, 
            [
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped packets
                ''',
                'dropped_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('transmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmitted packets
                ''',
                'transmitted_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'offer',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Request' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Request',
            False, 
            [
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped packets
                ''',
                'dropped_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('transmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmitted packets
                ''',
                'transmitted_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'request',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Decline' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Decline',
            False, 
            [
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped packets
                ''',
                'dropped_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('transmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmitted packets
                ''',
                'transmitted_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'decline',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Ack' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Ack',
            False, 
            [
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped packets
                ''',
                'dropped_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('transmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmitted packets
                ''',
                'transmitted_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'ack',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Nak' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Nak',
            False, 
            [
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped packets
                ''',
                'dropped_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('transmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmitted packets
                ''',
                'transmitted_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'nak',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Release' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Release',
            False, 
            [
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped packets
                ''',
                'dropped_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('transmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmitted packets
                ''',
                'transmitted_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'release',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Inform' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Inform',
            False, 
            [
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped packets
                ''',
                'dropped_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('transmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmitted packets
                ''',
                'transmitted_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'inform',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.LeaseQuery' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.LeaseQuery',
            False, 
            [
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped packets
                ''',
                'dropped_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('transmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmitted packets
                ''',
                'transmitted_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'lease-query',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.LeaseNotAssigned' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.LeaseNotAssigned',
            False, 
            [
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped packets
                ''',
                'dropped_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('transmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmitted packets
                ''',
                'transmitted_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'lease-not-assigned',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.LeaseUnknown' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.LeaseUnknown',
            False, 
            [
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped packets
                ''',
                'dropped_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('transmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmitted packets
                ''',
                'transmitted_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'lease-unknown',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.LeaseActive' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.LeaseActive',
            False, 
            [
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped packets
                ''',
                'dropped_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('transmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmitted packets
                ''',
                'transmitted_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'lease-active',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.BootpRequest' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.BootpRequest',
            False, 
            [
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped packets
                ''',
                'dropped_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('transmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmitted packets
                ''',
                'transmitted_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'bootp-request',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.BootpReply' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.BootpReply',
            False, 
            [
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped packets
                ''',
                'dropped_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('transmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmitted packets
                ''',
                'transmitted_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'bootp-reply',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics',
            False, 
            [
            _MetaInfoClassMember('ack', REFERENCE_CLASS, 'Ack' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Ack', 
                [], [], 
                '''                DHCP ack packets
                ''',
                'ack',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('bootp-reply', REFERENCE_CLASS, 'BootpReply' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.BootpReply', 
                [], [], 
                '''                DHCP BOOTP reply
                ''',
                'bootp_reply',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('bootp-request', REFERENCE_CLASS, 'BootpRequest' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.BootpRequest', 
                [], [], 
                '''                DHCP BOOTP request
                ''',
                'bootp_request',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('decline', REFERENCE_CLASS, 'Decline' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Decline', 
                [], [], 
                '''                DHCP decline packets
                ''',
                'decline',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('discover', REFERENCE_CLASS, 'Discover' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Discover', 
                [], [], 
                '''                DHCP discover packets
                ''',
                'discover',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('inform', REFERENCE_CLASS, 'Inform' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Inform', 
                [], [], 
                '''                DHCP inform packets
                ''',
                'inform',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('lease-active', REFERENCE_CLASS, 'LeaseActive' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.LeaseActive', 
                [], [], 
                '''                DHCP lease active
                ''',
                'lease_active',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('lease-not-assigned', REFERENCE_CLASS, 'LeaseNotAssigned' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.LeaseNotAssigned', 
                [], [], 
                '''                DHCP lease not assigned
                ''',
                'lease_not_assigned',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('lease-query', REFERENCE_CLASS, 'LeaseQuery' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.LeaseQuery', 
                [], [], 
                '''                DHCP lease query packets
                ''',
                'lease_query',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('lease-unknown', REFERENCE_CLASS, 'LeaseUnknown' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.LeaseUnknown', 
                [], [], 
                '''                DHCP lease unknown
                ''',
                'lease_unknown',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('nak', REFERENCE_CLASS, 'Nak' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Nak', 
                [], [], 
                '''                DHCP nak packets
                ''',
                'nak',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('offer', REFERENCE_CLASS, 'Offer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Offer', 
                [], [], 
                '''                DHCP offer packets
                ''',
                'offer',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('release', REFERENCE_CLASS, 'Release' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Release', 
                [], [], 
                '''                DHCP release packets
                ''',
                'release',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('request', REFERENCE_CLASS, 'Request' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Request', 
                [], [], 
                '''                DHCP request packets
                ''',
                'request',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf',
            False, 
            [
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', True),
            _MetaInfoClassMember('statistics', REFERENCE_CLASS, 'Statistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics', 
                [], [], 
                '''                IPv4 DHCP proxy statistics
                ''',
                'statistics',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'vrf',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs',
            False, 
            [
            _MetaInfoClassMember('vrf', REFERENCE_LIST, 'Vrf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf', 
                [], [], 
                '''                IPv4 DHCP proxy VRF name
                ''',
                'vrf',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'vrfs',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes.Node.Proxy.Profiles.Profile.VrfReferences.Ipv4DhcpdProxyVrfReference' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes.Node.Proxy.Profiles.Profile.VrfReferences.Ipv4DhcpdProxyVrfReference',
            False, 
            [
            _MetaInfoClassMember('proxy-reference-vrf-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 33)], [], 
                '''                VRF name
                ''',
                'proxy_reference_vrf_name',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'ipv4-dhcpd-proxy-vrf-reference',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes.Node.Proxy.Profiles.Profile.VrfReferences' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes.Node.Proxy.Profiles.Profile.VrfReferences',
            False, 
            [
            _MetaInfoClassMember('ipv4-dhcpd-proxy-vrf-reference', REFERENCE_LIST, 'Ipv4DhcpdProxyVrfReference' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes.Node.Proxy.Profiles.Profile.VrfReferences.Ipv4DhcpdProxyVrfReference', 
                [], [], 
                '''                ipv4 dhcpd proxy vrf reference
                ''',
                'ipv4_dhcpd_proxy_vrf_reference',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'vrf-references',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes.Node.Proxy.Profiles.Profile.InterfaceReferences.Ipv4DhcpdProxyInterfaceReference' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes.Node.Proxy.Profiles.Profile.InterfaceReferences.Ipv4DhcpdProxyInterfaceReference',
            False, 
            [
            _MetaInfoClassMember('proxy-reference-interface-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                Interface name
                ''',
                'proxy_reference_interface_name',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'ipv4-dhcpd-proxy-interface-reference',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes.Node.Proxy.Profiles.Profile.InterfaceReferences' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes.Node.Proxy.Profiles.Profile.InterfaceReferences',
            False, 
            [
            _MetaInfoClassMember('ipv4-dhcpd-proxy-interface-reference', REFERENCE_LIST, 'Ipv4DhcpdProxyInterfaceReference' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes.Node.Proxy.Profiles.Profile.InterfaceReferences.Ipv4DhcpdProxyInterfaceReference', 
                [], [], 
                '''                ipv4 dhcpd proxy interface reference
                ''',
                'ipv4_dhcpd_proxy_interface_reference',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'interface-references',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes.Node.Proxy.Profiles.Profile' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes.Node.Proxy.Profiles.Profile',
            False, 
            [
            _MetaInfoClassMember('profile-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Profile name
                ''',
                'profile_name',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', True),
            _MetaInfoClassMember('gi-addr', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Gateway addresses
                ''',
                'gi_addr',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False, max_elements=8),
            _MetaInfoClassMember('interface-references', REFERENCE_CLASS, 'InterfaceReferences' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes.Node.Proxy.Profiles.Profile.InterfaceReferences', 
                [], [], 
                '''                Interface references
                ''',
                'interface_references',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('is-move-allowed', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is true if dhcp subscriber is allowed to move
                ''',
                'is_move_allowed',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('is-relay-allow-untrusted-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is true if relay untrusted is enabled
                ''',
                'is_relay_allow_untrusted_enabled',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('is-relay-check', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is true if relay check enabled
                ''',
                'is_relay_check',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('is-relay-option-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is true if relay option is enabled
                ''',
                'is_relay_option_enabled',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('is-relay-optionvpn-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is true if relay VPN enabled
                ''',
                'is_relay_optionvpn_enabled',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('profile-helper-address', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Helper addresses
                ''',
                'profile_helper_address',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False, max_elements=8),
            _MetaInfoClassMember('proxy-broadcast-flag-policy', REFERENCE_ENUM_CLASS, 'BroadcastFlagEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'BroadcastFlagEnum', 
                [], [], 
                '''                Broadcast policy
                ''',
                'proxy_broadcast_flag_policy',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('proxy-lease-limit-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Lease limit count
                ''',
                'proxy_lease_limit_count',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('proxy-lease-limit-type', REFERENCE_ENUM_CLASS, 'ProxyLeaseLimitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'ProxyLeaseLimitEnum', 
                [], [], 
                '''                Lease limit type
                ''',
                'proxy_lease_limit_type',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('proxy-profile-client-lease-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Client lease time in seconds
                ''',
                'proxy_profile_client_lease_time',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('relay-authenticate', REFERENCE_ENUM_CLASS, 'RelayInfoAuthenticateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'RelayInfoAuthenticateEnum', 
                [], [], 
                '''                Relay authenticate
                ''',
                'relay_authenticate',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('relay-optionvpn-enabled-mode', REFERENCE_ENUM_CLASS, 'RelayInfoVpnModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'RelayInfoVpnModeEnum', 
                [], [], 
                '''                Relay VPN RFC/Cisco mode
                ''',
                'relay_optionvpn_enabled_mode',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('relay-policy', REFERENCE_ENUM_CLASS, 'RelayInfoPolicyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'RelayInfoPolicyEnum', 
                [], [], 
                '''                Relay policy
                ''',
                'relay_policy',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('vrf-name', REFERENCE_LEAFLIST, 'str' , None, None, 
                [(0, 33)], [], 
                '''                VRF names
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False, max_elements=8),
            _MetaInfoClassMember('vrf-references', REFERENCE_CLASS, 'VrfReferences' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes.Node.Proxy.Profiles.Profile.VrfReferences', 
                [], [], 
                '''                VRF references
                ''',
                'vrf_references',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'profile',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes.Node.Proxy.Profiles' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes.Node.Proxy.Profiles',
            False, 
            [
            _MetaInfoClassMember('profile', REFERENCE_LIST, 'Profile' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes.Node.Proxy.Profiles.Profile', 
                [], [], 
                '''                IPv4 DHCP proxy profile
                ''',
                'profile',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'profiles',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes.Node.Proxy.Statistics.Ipv4DhcpdProxyStat.Statistics_' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes.Node.Proxy.Statistics.Ipv4DhcpdProxyStat.Statistics_',
            False, 
            [
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped packets
                ''',
                'dropped_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('transmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmitted packets
                ''',
                'transmitted_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes.Node.Proxy.Statistics.Ipv4DhcpdProxyStat' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes.Node.Proxy.Statistics.Ipv4DhcpdProxyStat',
            False, 
            [
            _MetaInfoClassMember('statistics', REFERENCE_CLASS, 'Statistics_' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes.Node.Proxy.Statistics.Ipv4DhcpdProxyStat.Statistics_', 
                [], [], 
                '''                Proxy statistics
                ''',
                'statistics',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 33)], [], 
                '''                DHCP L3 VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'ipv4-dhcpd-proxy-stat',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes.Node.Proxy.Statistics' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes.Node.Proxy.Statistics',
            False, 
            [
            _MetaInfoClassMember('ipv4-dhcpd-proxy-stat', REFERENCE_LIST, 'Ipv4DhcpdProxyStat' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes.Node.Proxy.Statistics.Ipv4DhcpdProxyStat', 
                [], [], 
                '''                ipv4 dhcpd proxy stat
                ''',
                'ipv4_dhcpd_proxy_stat',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes.Node.Proxy.Binding.Clients.Client' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes.Node.Proxy.Binding.Clients.Client',
            False, 
            [
            _MetaInfoClassMember('client-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Client ID
                ''',
                'client_id',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', True),
            _MetaInfoClassMember('access-vrf-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 33)], [], 
                '''                DHCP access interface VRF name
                ''',
                'access_vrf_name',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('client-gi-addr', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                DHCP client GIADDR
                ''',
                'client_gi_addr',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('client-id-xr', ATTRIBUTE, 'str' , None, None, 
                [(0, 1275)], [], 
                '''                DHCP client identifier
                ''',
                'client_id_xr',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('event-history', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                event history
                ''',
                'event_history',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False, max_elements=20),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                DHCP access interface to client
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                DHCP IP address
                ''',
                'ip_address',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('is-auth-received', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is true if authentication is on received
                option82
                ''',
                'is_auth_received',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('is-mbl-subscriber', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is true if DHCP subscriber is Mobile
                ''',
                'is_mbl_subscriber',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('is-nak-next-renew', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is true if DHCP next renew from client will be
                NAK'd
                ''',
                'is_nak_next_renew',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('lease-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Lease time in seconds
                ''',
                'lease_time',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('mac-address', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                DHCP client MAC address
                ''',
                'mac_address',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('old-subscriber-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                DHCP old subscriber label
                ''',
                'old_subscriber_label',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('param-request', ATTRIBUTE, 'str' , None, None, 
                [(0, 513)], [], 
                '''                DHCP parameter request option
                ''',
                'param_request',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('param-response', ATTRIBUTE, 'str' , None, None, 
                [(0, 2051)], [], 
                '''                DHCP saved options
                ''',
                'param_response',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('profile-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                DHCP profile name
                ''',
                'profile_name',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('proxy-binding-inner-tag', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                DHCP VLAN inner VLAN
                ''',
                'proxy_binding_inner_tag',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('proxy-binding-outer-tag', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                DHCP VLAN outer VLAN
                ''',
                'proxy_binding_outer_tag',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('remaining-lease-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Remaining lease time in seconds
                ''',
                'remaining_lease_time',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('reply-server-ip-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                DHCP reply server IP address
                ''',
                'reply_server_ip_address',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('rx-circuit-id', ATTRIBUTE, 'str' , None, None, 
                [(0, 768)], [], 
                '''                DHCP received circuit ID
                ''',
                'rx_circuit_id',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('rx-remote-id', ATTRIBUTE, 'str' , None, None, 
                [(0, 768)], [], 
                '''                DHCP received Remote ID
                ''',
                'rx_remote_id',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('rx-vsiso', ATTRIBUTE, 'str' , None, None, 
                [(0, 768)], [], 
                '''                DHCP received VSISO
                ''',
                'rx_vsiso',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('server-ip-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                DHCP server IP address
                ''',
                'server_ip_address',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('server-vrf-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 33)], [], 
                '''                DHCP server VRF name
                ''',
                'server_vrf_name',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('session-start-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                session start time
                ''',
                'session_start_time',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('srg-state', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                DHCPV4 SRG state
                ''',
                'srg_state',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'BagDhcpdProxyStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'BagDhcpdProxyStateEnum', 
                [], [], 
                '''                DHCP client state
                ''',
                'state',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('subscriber-interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                DHCP subscriber interface
                ''',
                'subscriber_interface_name',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('subscriber-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                DHCP subscriber label
                ''',
                'subscriber_label',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('to-server-gi-addr', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                DHCP to server GIADDR
                ''',
                'to_server_gi_addr',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('tx-circuit-id', ATTRIBUTE, 'str' , None, None, 
                [(0, 768)], [], 
                '''                DHCP transmitted circuit ID
                ''',
                'tx_circuit_id',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('tx-remote-id', ATTRIBUTE, 'str' , None, None, 
                [(0, 768)], [], 
                '''                DHCP transmitted Remote ID
                ''',
                'tx_remote_id',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('tx-vsiso', ATTRIBUTE, 'str' , None, None, 
                [(0, 768)], [], 
                '''                DHCP transmitted VSISO
                ''',
                'tx_vsiso',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 33)], [], 
                '''                DHCP client/subscriber VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'client',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes.Node.Proxy.Binding.Clients' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes.Node.Proxy.Binding.Clients',
            False, 
            [
            _MetaInfoClassMember('client', REFERENCE_LIST, 'Client' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes.Node.Proxy.Binding.Clients.Client', 
                [], [], 
                '''                Single DHCP proxy binding
                ''',
                'client',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'clients',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes.Node.Proxy.Binding.Summary' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes.Node.Proxy.Binding.Summary',
            False, 
            [
            _MetaInfoClassMember('ack-waiting-for-dpm', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of clients in Waiting for DPM with ACK
                ''',
                'ack_waiting_for_dpm',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('bound-clients', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of clients in bound state
                ''',
                'bound_clients',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('clients', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total number of clients
                ''',
                'clients',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('deleting-clients-d', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of clients in deleting state
                ''',
                'deleting_clients_d',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('disconnected-clients', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of clients in disconnected state
                ''',
                'disconnected_clients',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('informing-clients', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of clients in informing state
                ''',
                'informing_clients',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('initializing-clients', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of clients in init state
                ''',
                'initializing_clients',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('offer-sent-for-client', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of clients in Offer sent state
                ''',
                'offer_sent_for_client',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('reauthorizing-clients', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of clients in reauth state
                ''',
                'reauthorizing_clients',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('renewing-clients', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of clients in renewing state
                ''',
                'renewing_clients',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('request-waiting-for-dpm', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of clients in Waiting for DPM with
                Request
                ''',
                'request_waiting_for_dpm',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('requesting-clients', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of clients in requesting state
                ''',
                'requesting_clients',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('restarting-clients', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of clients in restarting state
                ''',
                'restarting_clients',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('selecting-clients', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of clients in selecting state
                ''',
                'selecting_clients',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('waiting-for-daps-init', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of clients in Init DAPS wait state
                ''',
                'waiting_for_daps_init',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('waiting-for-dpm-addr-change', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of clients in Waiting for DPM after addr
                change
                ''',
                'waiting_for_dpm_addr_change',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('waiting-for-dpm-disconnect', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of clients in waiting for DPM disconnect
                state
                ''',
                'waiting_for_dpm_disconnect',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('waiting-for-dpm-init', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of clients in Init DPM wait state
                ''',
                'waiting_for_dpm_init',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'summary',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes.Node.Proxy.Binding' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes.Node.Proxy.Binding',
            False, 
            [
            _MetaInfoClassMember('clients', REFERENCE_CLASS, 'Clients' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes.Node.Proxy.Binding.Clients', 
                [], [], 
                '''                DHCP proxy client bindings
                ''',
                'clients',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('summary', REFERENCE_CLASS, 'Summary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes.Node.Proxy.Binding.Summary', 
                [], [], 
                '''                DHCP proxy binding summary
                ''',
                'summary',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'binding',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes.Node.Proxy' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes.Node.Proxy',
            False, 
            [
            _MetaInfoClassMember('binding', REFERENCE_CLASS, 'Binding' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes.Node.Proxy.Binding', 
                [], [], 
                '''                DHCP proxy bindings
                ''',
                'binding',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('profiles', REFERENCE_CLASS, 'Profiles' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes.Node.Proxy.Profiles', 
                [], [], 
                '''                IPv4 DHCP proxy profile
                ''',
                'profiles',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('statistics', REFERENCE_CLASS, 'Statistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes.Node.Proxy.Statistics', 
                [], [], 
                '''                DHCP proxy statistics
                ''',
                'statistics',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('statistics-info', REFERENCE_CLASS, 'StatisticsInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes.Node.Proxy.StatisticsInfo', 
                [], [], 
                '''                DHCP proxy stats info
                ''',
                'statistics_info',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('vrfs', REFERENCE_CLASS, 'Vrfs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs', 
                [], [], 
                '''                DHCP proxy list of VRF names
                ''',
                'vrfs',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'proxy',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes.Node.Interfaces.Interface' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes.Node.Interfaces.Interface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', True),
            _MetaInfoClassMember('intf-ifhandle', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Ifhandle of the interface
                ''',
                'intf_ifhandle',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('intf-is-ambiguous', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Is interface ambiguous
                ''',
                'intf_is_ambiguous',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('intf-lease-limit-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Lease limit count on interface
                ''',
                'intf_lease_limit_count',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('intf-lease-limit-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Lease limit type on interface
                ''',
                'intf_lease_limit_type',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('intf-mode', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Mode of interface
                ''',
                'intf_mode',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('intf-profile-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                Name of profile attached to the interface
                ''',
                'intf_profile_name',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('mac-throttle', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Mac Throttle Status
                ''',
                'mac_throttle',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('srg-role', REFERENCE_ENUM_CLASS, 'BagDhcpdIntfSrgRoleEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'BagDhcpdIntfSrgRoleEnum', 
                [], [], 
                '''                DHCPv6 Interface SRG role
                ''',
                'srg_role',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 33)], [], 
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes.Node.Interfaces' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes.Node.Interfaces',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes.Node.Interfaces.Interface', 
                [], [], 
                '''                IPv4 DHCP proxy/server interface info
                ''',
                'interface',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes.Node.Base.Statistics.Ipv4DhcpdProxyStat.Statistics_' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes.Node.Base.Statistics.Ipv4DhcpdProxyStat.Statistics_',
            False, 
            [
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped packets
                ''',
                'dropped_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('transmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmitted packets
                ''',
                'transmitted_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes.Node.Base.Statistics.Ipv4DhcpdProxyStat' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes.Node.Base.Statistics.Ipv4DhcpdProxyStat',
            False, 
            [
            _MetaInfoClassMember('statistics', REFERENCE_CLASS, 'Statistics_' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes.Node.Base.Statistics.Ipv4DhcpdProxyStat.Statistics_', 
                [], [], 
                '''                Proxy statistics
                ''',
                'statistics',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 33)], [], 
                '''                DHCP L3 VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'ipv4-dhcpd-proxy-stat',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes.Node.Base.Statistics' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes.Node.Base.Statistics',
            False, 
            [
            _MetaInfoClassMember('ipv4-dhcpd-proxy-stat', REFERENCE_LIST, 'Ipv4DhcpdProxyStat' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes.Node.Base.Statistics.Ipv4DhcpdProxyStat', 
                [], [], 
                '''                ipv4 dhcpd proxy stat
                ''',
                'ipv4_dhcpd_proxy_stat',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes.Node.Base.IssuStatus' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes.Node.Base.IssuStatus',
            False, 
            [
            _MetaInfoClassMember('big-bang-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Timestamp for the Big Bang notification time in
                nanoseconds since Epoch, i.e. since 00:00:00 UTC
                , January 1, 1970
                ''',
                'big_bang_time',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('issu-ready-entries-replicate', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Whether or not DHCP has received all replicated
                entries during the ISSU Load Phase
                ''',
                'issu_ready_entries_replicate',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('issu-ready-issu-mgr-connection', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Whether or not DHCP is currently connected to
                ISSU Manager during the ISSU Load Phase
                ''',
                'issu_ready_issu_mgr_connection',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('issu-ready-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Timestamp for the ISSU ready declaration in
                nanoseconds since Epoch, i.e. since 00:00:00 UTC
                , January 1, 1970
                ''',
                'issu_ready_time',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('issu-sync-complete-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Timestamp for the ISSU sync complete in
                nanoseconds since Epoch, i.e. since 00:00:00 UTC
                , January 1, 1970
                ''',
                'issu_sync_complete_time',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('issu-sync-start-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Timestamp for the ISSU sync start in nanoseconds
                since Epoch, i.e. since 00:00:00 UTC, January 1,
                1970
                ''',
                'issu_sync_start_time',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('phase', REFERENCE_ENUM_CLASS, 'DhcpIssuPhaseEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'DhcpIssuPhaseEnum', 
                [], [], 
                '''                The current ISSU phase of the DHCP process
                ''',
                'phase',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('primary-role-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Timestamp for the change to Primary role
                notification time in nanoseconds since Epoch, i
                .e. since 00:00:00 UTC, January 1, 1970
                ''',
                'primary_role_time',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('role', REFERENCE_ENUM_CLASS, 'DhcpIssuRoleEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'DhcpIssuRoleEnum', 
                [], [], 
                '''                The current role of the DHCP process
                ''',
                'role',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('version', REFERENCE_ENUM_CLASS, 'DhcpIssuVersionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'DhcpIssuVersionEnum', 
                [], [], 
                '''                The current version of the DHCP process in the
                context of an ISSU
                ''',
                'version',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'issu-status',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.Discover' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.Discover',
            False, 
            [
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped packets
                ''',
                'dropped_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('transmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmitted packets
                ''',
                'transmitted_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'discover',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.Offer' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.Offer',
            False, 
            [
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped packets
                ''',
                'dropped_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('transmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmitted packets
                ''',
                'transmitted_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'offer',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.Request' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.Request',
            False, 
            [
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped packets
                ''',
                'dropped_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('transmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmitted packets
                ''',
                'transmitted_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'request',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.Decline' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.Decline',
            False, 
            [
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped packets
                ''',
                'dropped_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('transmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmitted packets
                ''',
                'transmitted_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'decline',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.Ack' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.Ack',
            False, 
            [
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped packets
                ''',
                'dropped_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('transmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmitted packets
                ''',
                'transmitted_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'ack',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.Nak' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.Nak',
            False, 
            [
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped packets
                ''',
                'dropped_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('transmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmitted packets
                ''',
                'transmitted_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'nak',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.Release' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.Release',
            False, 
            [
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped packets
                ''',
                'dropped_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('transmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmitted packets
                ''',
                'transmitted_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'release',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.Inform' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.Inform',
            False, 
            [
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped packets
                ''',
                'dropped_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('transmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmitted packets
                ''',
                'transmitted_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'inform',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.LeaseQuery' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.LeaseQuery',
            False, 
            [
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped packets
                ''',
                'dropped_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('transmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmitted packets
                ''',
                'transmitted_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'lease-query',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.LeaseNotAssigned' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.LeaseNotAssigned',
            False, 
            [
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped packets
                ''',
                'dropped_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('transmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmitted packets
                ''',
                'transmitted_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'lease-not-assigned',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.LeaseUnknown' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.LeaseUnknown',
            False, 
            [
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped packets
                ''',
                'dropped_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('transmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmitted packets
                ''',
                'transmitted_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'lease-unknown',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.LeaseActive' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.LeaseActive',
            False, 
            [
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped packets
                ''',
                'dropped_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('transmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmitted packets
                ''',
                'transmitted_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'lease-active',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.BootpRequest' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.BootpRequest',
            False, 
            [
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped packets
                ''',
                'dropped_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('transmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmitted packets
                ''',
                'transmitted_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'bootp-request',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.BootpReply' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.BootpReply',
            False, 
            [
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped packets
                ''',
                'dropped_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('transmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmitted packets
                ''',
                'transmitted_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'bootp-reply',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics',
            False, 
            [
            _MetaInfoClassMember('ack', REFERENCE_CLASS, 'Ack' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.Ack', 
                [], [], 
                '''                DHCP ack packets
                ''',
                'ack',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('bootp-reply', REFERENCE_CLASS, 'BootpReply' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.BootpReply', 
                [], [], 
                '''                DHCP BOOTP reply
                ''',
                'bootp_reply',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('bootp-request', REFERENCE_CLASS, 'BootpRequest' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.BootpRequest', 
                [], [], 
                '''                DHCP BOOTP request
                ''',
                'bootp_request',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('decline', REFERENCE_CLASS, 'Decline' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.Decline', 
                [], [], 
                '''                DHCP decline packets
                ''',
                'decline',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('discover', REFERENCE_CLASS, 'Discover' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.Discover', 
                [], [], 
                '''                DHCP discover packets
                ''',
                'discover',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('inform', REFERENCE_CLASS, 'Inform' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.Inform', 
                [], [], 
                '''                DHCP inform packets
                ''',
                'inform',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('lease-active', REFERENCE_CLASS, 'LeaseActive' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.LeaseActive', 
                [], [], 
                '''                DHCP lease active
                ''',
                'lease_active',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('lease-not-assigned', REFERENCE_CLASS, 'LeaseNotAssigned' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.LeaseNotAssigned', 
                [], [], 
                '''                DHCP lease not assigned
                ''',
                'lease_not_assigned',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('lease-query', REFERENCE_CLASS, 'LeaseQuery' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.LeaseQuery', 
                [], [], 
                '''                DHCP lease query packets
                ''',
                'lease_query',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('lease-unknown', REFERENCE_CLASS, 'LeaseUnknown' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.LeaseUnknown', 
                [], [], 
                '''                DHCP lease unknown
                ''',
                'lease_unknown',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('nak', REFERENCE_CLASS, 'Nak' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.Nak', 
                [], [], 
                '''                DHCP nak packets
                ''',
                'nak',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('offer', REFERENCE_CLASS, 'Offer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.Offer', 
                [], [], 
                '''                DHCP offer packets
                ''',
                'offer',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('release', REFERENCE_CLASS, 'Release' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.Release', 
                [], [], 
                '''                DHCP release packets
                ''',
                'release',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('request', REFERENCE_CLASS, 'Request' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.Request', 
                [], [], 
                '''                DHCP request packets
                ''',
                'request',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf',
            False, 
            [
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', True),
            _MetaInfoClassMember('statistics', REFERENCE_CLASS, 'Statistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics', 
                [], [], 
                '''                IPv4 DHCP base statistics
                ''',
                'statistics',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'vrf',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes.Node.Base.Vrfs' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes.Node.Base.Vrfs',
            False, 
            [
            _MetaInfoClassMember('vrf', REFERENCE_LIST, 'Vrf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf', 
                [], [], 
                '''                IPv4 DHCP base VRF name
                ''',
                'vrf',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'vrfs',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes.Node.Base.Profiles.Profile.InterfaceReferences.Ipv4DhcpdBaseInterfaceReference' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes.Node.Base.Profiles.Profile.InterfaceReferences.Ipv4DhcpdBaseInterfaceReference',
            False, 
            [
            _MetaInfoClassMember('base-reference-interface-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                Interface name
                ''',
                'base_reference_interface_name',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'ipv4-dhcpd-base-interface-reference',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes.Node.Base.Profiles.Profile.InterfaceReferences' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes.Node.Base.Profiles.Profile.InterfaceReferences',
            False, 
            [
            _MetaInfoClassMember('ipv4-dhcpd-base-interface-reference', REFERENCE_LIST, 'Ipv4DhcpdBaseInterfaceReference' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes.Node.Base.Profiles.Profile.InterfaceReferences.Ipv4DhcpdBaseInterfaceReference', 
                [], [], 
                '''                ipv4 dhcpd base interface reference
                ''',
                'ipv4_dhcpd_base_interface_reference',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'interface-references',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes.Node.Base.Profiles.Profile.ChildProfileInfo.Ipv4DhcpdBaseChildProfileInfo' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes.Node.Base.Profiles.Profile.ChildProfileInfo.Ipv4DhcpdBaseChildProfileInfo',
            False, 
            [
            _MetaInfoClassMember('base-child-profile-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                Base Child Profile name
                ''',
                'base_child_profile_name',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('matched-option-code', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Matched option code
                ''',
                'matched_option_code',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('matched-option-len', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Matched option len
                ''',
                'matched_option_len',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('mode', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Profile mode
                ''',
                'mode',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('option-data', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Matched option data
                ''',
                'option_data',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'ipv4-dhcpd-base-child-profile-info',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes.Node.Base.Profiles.Profile.ChildProfileInfo' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes.Node.Base.Profiles.Profile.ChildProfileInfo',
            False, 
            [
            _MetaInfoClassMember('ipv4-dhcpd-base-child-profile-info', REFERENCE_LIST, 'Ipv4DhcpdBaseChildProfileInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes.Node.Base.Profiles.Profile.ChildProfileInfo.Ipv4DhcpdBaseChildProfileInfo', 
                [], [], 
                '''                ipv4 dhcpd base child profile info
                ''',
                'ipv4_dhcpd_base_child_profile_info',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'child-profile-info',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes.Node.Base.Profiles.Profile' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes.Node.Base.Profiles.Profile',
            False, 
            [
            _MetaInfoClassMember('profile-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Profile name
                ''',
                'profile_name',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', True),
            _MetaInfoClassMember('base-default-profile-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                Base Default Profile name
                ''',
                'base_default_profile_name',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('child-profile-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Child profile count
                ''',
                'child_profile_count',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('child-profile-info', REFERENCE_CLASS, 'ChildProfileInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes.Node.Base.Profiles.Profile.ChildProfileInfo', 
                [], [], 
                '''                child profile info
                ''',
                'child_profile_info',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('default-profile-mode', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Default Profile mode
                ''',
                'default_profile_mode',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('interface-references', REFERENCE_CLASS, 'InterfaceReferences' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes.Node.Base.Profiles.Profile.InterfaceReferences', 
                [], [], 
                '''                Interface references
                ''',
                'interface_references',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('intf-ref-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Interface reference count
                ''',
                'intf_ref_count',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('relay-authenticate', REFERENCE_ENUM_CLASS, 'RelayInfoAuthenticateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'RelayInfoAuthenticateEnum', 
                [], [], 
                '''                Relay authenticate
                ''',
                'relay_authenticate',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('remote-id', ATTRIBUTE, 'str' , None, None, 
                [(0, 768)], [], 
                '''                DHCP configured Remote ID
                ''',
                'remote_id',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'profile',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes.Node.Base.Profiles' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes.Node.Base.Profiles',
            False, 
            [
            _MetaInfoClassMember('profile', REFERENCE_LIST, 'Profile' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes.Node.Base.Profiles.Profile', 
                [], [], 
                '''                IPv4 DHCP base profile
                ''',
                'profile',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'profiles',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes.Node.Base.Database' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes.Node.Base.Database',
            False, 
            [
            _MetaInfoClassMember('configured', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Database feature configured
                ''',
                'configured',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('failed-full-file-write-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Failed full file write count
                ''',
                'failed_full_file_write_count',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('failed-incremental-file-write-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Failed incremental file write count
                ''',
                'failed_incremental_file_write_count',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('full-file-record-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Full file record count
                ''',
                'full_file_record_count',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('full-file-write-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Full file write count
                ''',
                'full_file_write_count',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('full-file-write-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Full file write interval in minutes
                ''',
                'full_file_write_interval',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('incremental-file-record-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Incremental file record count
                ''',
                'incremental_file_record_count',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('incremental-file-write-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Incremental file write count
                ''',
                'incremental_file_write_count',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('incremental-file-write-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Incremental file write interval in minutes
                ''',
                'incremental_file_write_interval',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('last-full-file-write-error-timestamp', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Last full file write error timestamp since epoch
                ''',
                'last_full_file_write_error_timestamp',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('last-full-write-file-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Last full write file name
                ''',
                'last_full_write_file_name',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('last-full-write-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Last full write time since epoch
                ''',
                'last_full_write_time',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('last-incremental-file-write-error-timestamp', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Last incremental file write error timestamp
                since epoch
                ''',
                'last_incremental_file_write_error_timestamp',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('last-incremental-write-file-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Last incremental write file name
                ''',
                'last_incremental_write_file_name',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('last-incremental-write-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Last incremental write time since epoch
                ''',
                'last_incremental_write_time',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Current file version
                ''',
                'version',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'database',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes.Node.Base' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes.Node.Base',
            False, 
            [
            _MetaInfoClassMember('database', REFERENCE_CLASS, 'Database' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes.Node.Base.Database', 
                [], [], 
                '''                IPv4 DHCP database
                ''',
                'database',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('issu-status', REFERENCE_CLASS, 'IssuStatus' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes.Node.Base.IssuStatus', 
                [], [], 
                '''                IPv4 DHCP ISSU status
                ''',
                'issu_status',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('profiles', REFERENCE_CLASS, 'Profiles' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes.Node.Base.Profiles', 
                [], [], 
                '''                IPv4 DHCP Base profile
                ''',
                'profiles',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('statistics', REFERENCE_CLASS, 'Statistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes.Node.Base.Statistics', 
                [], [], 
                '''                DHCP base statistics
                ''',
                'statistics',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('vrfs', REFERENCE_CLASS, 'Vrfs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes.Node.Base.Vrfs', 
                [], [], 
                '''                DHCP base list of VRF names
                ''',
                'vrfs',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'base',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes.Node.Server.Profiles.Profile' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes.Node.Server.Profiles.Profile',
            False, 
            [
            _MetaInfoClassMember('server-profile-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Profile name
                ''',
                'server_profile_name',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', True),
            _MetaInfoClassMember('bcast-policy', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Bcast Policy
                ''',
                'bcast_policy',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('duplicate-ip-address-check', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Duplicate IP Address Check
                ''',
                'duplicate_ip_address_check',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('duplicate-mac-address-check', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Duplicate MAC Address Check
                ''',
                'duplicate_mac_address_check',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('giaddr-policy', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Giaddr Policy
                ''',
                'giaddr_policy',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('is-move-allowed', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is true if dhcp subscriber is allowed to move
                ''',
                'is_move_allowed',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('lease-limit-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Lease Limit Count
                ''',
                'lease_limit_count',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('lease-limit-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Lease Limit Type
                ''',
                'lease_limit_type',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('requested-address-check', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Requested Address Check
                ''',
                'requested_address_check',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('secure-arp', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Secure ARP
                ''',
                'secure_arp',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('server-bootfile-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 256)], [], 
                '''                Server Bootfile name
                ''',
                'server_bootfile_name',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('server-domain-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 256)], [], 
                '''                Server Domain name
                ''',
                'server_domain_name',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('server-id-check', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Server ID Check
                ''',
                'server_id_check',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('server-pool-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                Pool Name
                ''',
                'server_pool_name',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('server-profile-default-router', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Server default addresses
                ''',
                'server_profile_default_router',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False, max_elements=9),
            _MetaInfoClassMember('server-profile-dns', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Server DNS addresses
                ''',
                'server_profile_dns',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False, max_elements=9),
            _MetaInfoClassMember('server-profile-lease', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Lease
                ''',
                'server_profile_lease',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('server-profile-name-xr', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                Profile Name
                ''',
                'server_profile_name_xr',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('server-profile-netbios-name-svr-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Server netbios svr count 
                ''',
                'server_profile_netbios_name_svr_count',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('server-profile-netbios-node-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Server netbios node type
                ''',
                'server_profile_netbios_node_type',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('server-profile-netbious-name-server', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Server netbios addresses
                ''',
                'server_profile_netbious_name_server',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False, max_elements=9),
            _MetaInfoClassMember('server-profile-server-dns-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Server DNS Count
                ''',
                'server_profile_server_dns_count',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('server-profile-time-server', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Server Time addresses
                ''',
                'server_profile_time_server',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False, max_elements=9),
            _MetaInfoClassMember('server-profile-time-svr-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Server time svr count 
                ''',
                'server_profile_time_svr_count',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('server-profiledefault-router-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Server default count 
                ''',
                'server_profiledefault_router_count',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('server-profileiedge-check', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Server iEdge Check
                ''',
                'server_profileiedge_check',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('subnet-mask', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Subnet Mask
                ''',
                'subnet_mask',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'profile',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes.Node.Server.Profiles' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes.Node.Server.Profiles',
            False, 
            [
            _MetaInfoClassMember('profile', REFERENCE_LIST, 'Profile' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes.Node.Server.Profiles.Profile', 
                [], [], 
                '''                IPv4 DHCP server profile
                ''',
                'profile',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'profiles',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes.Node.Server.Statistics.Ipv4DhcpdProxyStat.Statistics_' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes.Node.Server.Statistics.Ipv4DhcpdProxyStat.Statistics_',
            False, 
            [
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped packets
                ''',
                'dropped_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('transmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmitted packets
                ''',
                'transmitted_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes.Node.Server.Statistics.Ipv4DhcpdProxyStat' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes.Node.Server.Statistics.Ipv4DhcpdProxyStat',
            False, 
            [
            _MetaInfoClassMember('statistics', REFERENCE_CLASS, 'Statistics_' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes.Node.Server.Statistics.Ipv4DhcpdProxyStat.Statistics_', 
                [], [], 
                '''                Proxy statistics
                ''',
                'statistics',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 33)], [], 
                '''                DHCP L3 VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'ipv4-dhcpd-proxy-stat',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes.Node.Server.Statistics' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes.Node.Server.Statistics',
            False, 
            [
            _MetaInfoClassMember('ipv4-dhcpd-proxy-stat', REFERENCE_LIST, 'Ipv4DhcpdProxyStat' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes.Node.Server.Statistics.Ipv4DhcpdProxyStat', 
                [], [], 
                '''                ipv4 dhcpd proxy stat
                ''',
                'ipv4_dhcpd_proxy_stat',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes.Node.Server.Binding.Summary' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes.Node.Server.Binding.Summary',
            False, 
            [
            _MetaInfoClassMember('ack-waiting-for-dpm', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of clients in Waiting for DPM with ACK
                ''',
                'ack_waiting_for_dpm',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('bound-clients', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of clients in bound state
                ''',
                'bound_clients',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('clients', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total number of clients
                ''',
                'clients',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('deleting-clients-d', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of clients in deleting state
                ''',
                'deleting_clients_d',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('disconnected-clients', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of clients in disconnected state
                ''',
                'disconnected_clients',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('informing-clients', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of clients in informing state
                ''',
                'informing_clients',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('initializing-clients', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of clients in init state
                ''',
                'initializing_clients',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('offer-sent-for-client', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of clients in Offer sent state
                ''',
                'offer_sent_for_client',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('reauthorizing-clients', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of clients in reauth state
                ''',
                'reauthorizing_clients',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('renewing-clients', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of clients in renewing state
                ''',
                'renewing_clients',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('request-waiting-for-dpm', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of clients in Waiting for DPM with
                Request
                ''',
                'request_waiting_for_dpm',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('requesting-clients', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of clients in requesting state
                ''',
                'requesting_clients',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('restarting-clients', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of clients in restarting state
                ''',
                'restarting_clients',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('selecting-clients', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of clients in selecting state
                ''',
                'selecting_clients',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('waiting-for-daps-init', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of clients in Init DAPS wait state
                ''',
                'waiting_for_daps_init',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('waiting-for-dpm-addr-change', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of clients in Waiting for DPM after addr
                change
                ''',
                'waiting_for_dpm_addr_change',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('waiting-for-dpm-disconnect', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of clients in waiting for DPM disconnect
                state
                ''',
                'waiting_for_dpm_disconnect',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('waiting-for-dpm-init', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of clients in Init DPM wait state
                ''',
                'waiting_for_dpm_init',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'summary',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes.Node.Server.Binding.Clients.Client' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes.Node.Server.Binding.Clients.Client',
            False, 
            [
            _MetaInfoClassMember('client-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Client ID
                ''',
                'client_id',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', True),
            _MetaInfoClassMember('access-vrf-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 33)], [], 
                '''                DHCP access interface VRF name
                ''',
                'access_vrf_name',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('client-gi-addr', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                DHCP client GIADDR
                ''',
                'client_gi_addr',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('client-id-xr', ATTRIBUTE, 'str' , None, None, 
                [(0, 1275)], [], 
                '''                DHCP client identifier
                ''',
                'client_id_xr',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('event-history', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                event history
                ''',
                'event_history',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False, max_elements=20),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                DHCP access interface to client
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                DHCP IP address
                ''',
                'ip_address',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('is-auth-received', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is true if authentication is on received
                option82
                ''',
                'is_auth_received',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('is-mbl-subscriber', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is true if DHCP subscriber is Mobile
                ''',
                'is_mbl_subscriber',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('is-nak-next-renew', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is true if DHCP next renew from client will be
                NAK'd
                ''',
                'is_nak_next_renew',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('lease-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Lease time in seconds
                ''',
                'lease_time',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('mac-address', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                DHCP client MAC address
                ''',
                'mac_address',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('old-subscriber-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                DHCP old subscriber label
                ''',
                'old_subscriber_label',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('param-request', ATTRIBUTE, 'str' , None, None, 
                [(0, 513)], [], 
                '''                DHCP parameter request option
                ''',
                'param_request',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('param-response', ATTRIBUTE, 'str' , None, None, 
                [(0, 2051)], [], 
                '''                DHCP saved options
                ''',
                'param_response',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('profile-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                DHCP profile name
                ''',
                'profile_name',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('proxy-binding-inner-tag', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                DHCP VLAN inner VLAN
                ''',
                'proxy_binding_inner_tag',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('proxy-binding-outer-tag', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                DHCP VLAN outer VLAN
                ''',
                'proxy_binding_outer_tag',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('remaining-lease-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Remaining lease time in seconds
                ''',
                'remaining_lease_time',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('reply-server-ip-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                DHCP reply server IP address
                ''',
                'reply_server_ip_address',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('rx-circuit-id', ATTRIBUTE, 'str' , None, None, 
                [(0, 768)], [], 
                '''                DHCP received circuit ID
                ''',
                'rx_circuit_id',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('rx-remote-id', ATTRIBUTE, 'str' , None, None, 
                [(0, 768)], [], 
                '''                DHCP received Remote ID
                ''',
                'rx_remote_id',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('rx-vsiso', ATTRIBUTE, 'str' , None, None, 
                [(0, 768)], [], 
                '''                DHCP received VSISO
                ''',
                'rx_vsiso',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('server-ip-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                DHCP server IP address
                ''',
                'server_ip_address',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('server-vrf-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 33)], [], 
                '''                DHCP server VRF name
                ''',
                'server_vrf_name',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('session-start-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                session start time
                ''',
                'session_start_time',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('srg-state', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                DHCPV4 SRG state
                ''',
                'srg_state',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'BagDhcpdProxyStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'BagDhcpdProxyStateEnum', 
                [], [], 
                '''                DHCP client state
                ''',
                'state',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('subscriber-interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                DHCP subscriber interface
                ''',
                'subscriber_interface_name',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('subscriber-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                DHCP subscriber label
                ''',
                'subscriber_label',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('to-server-gi-addr', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                DHCP to server GIADDR
                ''',
                'to_server_gi_addr',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('tx-circuit-id', ATTRIBUTE, 'str' , None, None, 
                [(0, 768)], [], 
                '''                DHCP transmitted circuit ID
                ''',
                'tx_circuit_id',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('tx-remote-id', ATTRIBUTE, 'str' , None, None, 
                [(0, 768)], [], 
                '''                DHCP transmitted Remote ID
                ''',
                'tx_remote_id',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('tx-vsiso', ATTRIBUTE, 'str' , None, None, 
                [(0, 768)], [], 
                '''                DHCP transmitted VSISO
                ''',
                'tx_vsiso',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 33)], [], 
                '''                DHCP client/subscriber VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'client',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes.Node.Server.Binding.Clients' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes.Node.Server.Binding.Clients',
            False, 
            [
            _MetaInfoClassMember('client', REFERENCE_LIST, 'Client' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes.Node.Server.Binding.Clients.Client', 
                [], [], 
                '''                Single DHCP Server binding
                ''',
                'client',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'clients',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes.Node.Server.Binding' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes.Node.Server.Binding',
            False, 
            [
            _MetaInfoClassMember('clients', REFERENCE_CLASS, 'Clients' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes.Node.Server.Binding.Clients', 
                [], [], 
                '''                DHCP server client bindings
                ''',
                'clients',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('summary', REFERENCE_CLASS, 'Summary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes.Node.Server.Binding.Summary', 
                [], [], 
                '''                DHCP server binding summary
                ''',
                'summary',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'binding',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes.Node.Server.StatisticsInfo' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes.Node.Server.StatisticsInfo',
            False, 
            [
            _MetaInfoClassMember('proxy-stats-timestamp', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Proxy Stats timestamp
                ''',
                'proxy_stats_timestamp',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'statistics-info',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.Discover' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.Discover',
            False, 
            [
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped packets
                ''',
                'dropped_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('transmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmitted packets
                ''',
                'transmitted_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'discover',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.Offer' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.Offer',
            False, 
            [
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped packets
                ''',
                'dropped_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('transmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmitted packets
                ''',
                'transmitted_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'offer',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.Request' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.Request',
            False, 
            [
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped packets
                ''',
                'dropped_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('transmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmitted packets
                ''',
                'transmitted_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'request',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.Decline' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.Decline',
            False, 
            [
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped packets
                ''',
                'dropped_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('transmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmitted packets
                ''',
                'transmitted_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'decline',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.Ack' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.Ack',
            False, 
            [
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped packets
                ''',
                'dropped_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('transmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmitted packets
                ''',
                'transmitted_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'ack',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.Nak' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.Nak',
            False, 
            [
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped packets
                ''',
                'dropped_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('transmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmitted packets
                ''',
                'transmitted_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'nak',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.Release' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.Release',
            False, 
            [
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped packets
                ''',
                'dropped_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('transmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmitted packets
                ''',
                'transmitted_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'release',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.Inform' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.Inform',
            False, 
            [
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped packets
                ''',
                'dropped_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('transmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmitted packets
                ''',
                'transmitted_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'inform',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.LeaseQuery' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.LeaseQuery',
            False, 
            [
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped packets
                ''',
                'dropped_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('transmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmitted packets
                ''',
                'transmitted_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'lease-query',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.LeaseNotAssigned' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.LeaseNotAssigned',
            False, 
            [
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped packets
                ''',
                'dropped_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('transmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmitted packets
                ''',
                'transmitted_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'lease-not-assigned',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.LeaseUnknown' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.LeaseUnknown',
            False, 
            [
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped packets
                ''',
                'dropped_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('transmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmitted packets
                ''',
                'transmitted_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'lease-unknown',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.LeaseActive' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.LeaseActive',
            False, 
            [
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped packets
                ''',
                'dropped_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('transmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmitted packets
                ''',
                'transmitted_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'lease-active',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.BootpRequest' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.BootpRequest',
            False, 
            [
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped packets
                ''',
                'dropped_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('transmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmitted packets
                ''',
                'transmitted_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'bootp-request',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.BootpReply' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.BootpReply',
            False, 
            [
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped packets
                ''',
                'dropped_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('transmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmitted packets
                ''',
                'transmitted_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'bootp-reply',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics',
            False, 
            [
            _MetaInfoClassMember('ack', REFERENCE_CLASS, 'Ack' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.Ack', 
                [], [], 
                '''                DHCP ack packets
                ''',
                'ack',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('bootp-reply', REFERENCE_CLASS, 'BootpReply' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.BootpReply', 
                [], [], 
                '''                DHCP BOOTP reply
                ''',
                'bootp_reply',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('bootp-request', REFERENCE_CLASS, 'BootpRequest' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.BootpRequest', 
                [], [], 
                '''                DHCP BOOTP request
                ''',
                'bootp_request',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('decline', REFERENCE_CLASS, 'Decline' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.Decline', 
                [], [], 
                '''                DHCP decline packets
                ''',
                'decline',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('discover', REFERENCE_CLASS, 'Discover' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.Discover', 
                [], [], 
                '''                DHCP discover packets
                ''',
                'discover',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('inform', REFERENCE_CLASS, 'Inform' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.Inform', 
                [], [], 
                '''                DHCP inform packets
                ''',
                'inform',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('lease-active', REFERENCE_CLASS, 'LeaseActive' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.LeaseActive', 
                [], [], 
                '''                DHCP lease active
                ''',
                'lease_active',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('lease-not-assigned', REFERENCE_CLASS, 'LeaseNotAssigned' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.LeaseNotAssigned', 
                [], [], 
                '''                DHCP lease not assigned
                ''',
                'lease_not_assigned',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('lease-query', REFERENCE_CLASS, 'LeaseQuery' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.LeaseQuery', 
                [], [], 
                '''                DHCP lease query packets
                ''',
                'lease_query',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('lease-unknown', REFERENCE_CLASS, 'LeaseUnknown' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.LeaseUnknown', 
                [], [], 
                '''                DHCP lease unknown
                ''',
                'lease_unknown',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('nak', REFERENCE_CLASS, 'Nak' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.Nak', 
                [], [], 
                '''                DHCP nak packets
                ''',
                'nak',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('offer', REFERENCE_CLASS, 'Offer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.Offer', 
                [], [], 
                '''                DHCP offer packets
                ''',
                'offer',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('release', REFERENCE_CLASS, 'Release' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.Release', 
                [], [], 
                '''                DHCP release packets
                ''',
                'release',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('request', REFERENCE_CLASS, 'Request' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.Request', 
                [], [], 
                '''                DHCP request packets
                ''',
                'request',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf',
            False, 
            [
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', True),
            _MetaInfoClassMember('statistics', REFERENCE_CLASS, 'Statistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics', 
                [], [], 
                '''                IPv4 DHCP server statistics
                ''',
                'statistics',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'vrf',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes.Node.Server.Vrfs' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes.Node.Server.Vrfs',
            False, 
            [
            _MetaInfoClassMember('vrf', REFERENCE_LIST, 'Vrf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf', 
                [], [], 
                '''                IPv4 DHCP server VRF name
                ''',
                'vrf',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'vrfs',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes.Node.Server' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes.Node.Server',
            False, 
            [
            _MetaInfoClassMember('binding', REFERENCE_CLASS, 'Binding' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes.Node.Server.Binding', 
                [], [], 
                '''                DHCP server bindings
                ''',
                'binding',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('profiles', REFERENCE_CLASS, 'Profiles' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes.Node.Server.Profiles', 
                [], [], 
                '''                IPv4 DHCP Server profile
                ''',
                'profiles',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('statistics', REFERENCE_CLASS, 'Statistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes.Node.Server.Statistics', 
                [], [], 
                '''                DHCP Server statistics
                ''',
                'statistics',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('statistics-info', REFERENCE_CLASS, 'StatisticsInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes.Node.Server.StatisticsInfo', 
                [], [], 
                '''                DHCP proxy stats info
                ''',
                'statistics_info',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('vrfs', REFERENCE_CLASS, 'Vrfs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes.Node.Server.Vrfs', 
                [], [], 
                '''                DHCP Server list of VRF names
                ''',
                'vrfs',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'server',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes.Node.Relay.Profiles.Profile' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes.Node.Relay.Profiles.Profile',
            False, 
            [
            _MetaInfoClassMember('profile-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Profile name
                ''',
                'profile_name',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', True),
            _MetaInfoClassMember('relay-profile-broadcast-flag-policy', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Broadcast policy
                ''',
                'relay_profile_broadcast_flag_policy',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('relay-profile-gi-addr', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Gateway addresses
                ''',
                'relay_profile_gi_addr',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False, max_elements=32),
            _MetaInfoClassMember('relay-profile-gi-addr-policy', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                GIADDR policy
                ''',
                'relay_profile_gi_addr_policy',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('relay-profile-helper-address', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Helper addresses
                ''',
                'relay_profile_helper_address',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False, max_elements=32),
            _MetaInfoClassMember('relay-profile-helper-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Helper address count
                ''',
                'relay_profile_helper_count',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('relay-profile-helper-vrf', REFERENCE_LEAFLIST, 'str' , None, None, 
                [(0, 33)], [], 
                '''                Helper address vrfs
                ''',
                'relay_profile_helper_vrf',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False, max_elements=32),
            _MetaInfoClassMember('relay-profile-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                Profile Name
                ''',
                'relay_profile_name',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('relay-profile-relay-info-allow-untrusted', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Relay info untrusted
                ''',
                'relay_profile_relay_info_allow_untrusted',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('relay-profile-relay-info-check', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Relay info check
                ''',
                'relay_profile_relay_info_check',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('relay-profile-relay-info-option', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Relay info option
                ''',
                'relay_profile_relay_info_option',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('relay-profile-relay-info-optionvpn', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Relay info option vpn
                ''',
                'relay_profile_relay_info_optionvpn',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('relay-profile-relay-info-optionvpn-mode', REFERENCE_ENUM_CLASS, 'RelayInfoVpnModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'RelayInfoVpnModeEnum', 
                [], [], 
                '''                Relay info option vpn-mode
                ''',
                'relay_profile_relay_info_optionvpn_mode',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('relay-profile-relay-info-policy', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Relay info policy
                ''',
                'relay_profile_relay_info_policy',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('relay-profile-uid', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Profile UID
                ''',
                'relay_profile_uid',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'profile',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes.Node.Relay.Profiles' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes.Node.Relay.Profiles',
            False, 
            [
            _MetaInfoClassMember('profile', REFERENCE_LIST, 'Profile' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes.Node.Relay.Profiles.Profile', 
                [], [], 
                '''                DHCP Relay profile
                ''',
                'profile',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'profiles',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes.Node.Relay.StatisticsInfo' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes.Node.Relay.StatisticsInfo',
            False, 
            [
            _MetaInfoClassMember('relay-stats-timestamp', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Relay Stats timestamp
                ''',
                'relay_stats_timestamp',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'statistics-info',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes.Node.Relay.Statistics.Ipv4DhcpdRelayStat.Statistics_' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes.Node.Relay.Statistics.Ipv4DhcpdRelayStat.Statistics_',
            False, 
            [
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped packets
                ''',
                'dropped_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('transmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmitted packets
                ''',
                'transmitted_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes.Node.Relay.Statistics.Ipv4DhcpdRelayStat' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes.Node.Relay.Statistics.Ipv4DhcpdRelayStat',
            False, 
            [
            _MetaInfoClassMember('relay-statistics-vrf-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 33)], [], 
                '''                DHCP L3 VRF Name
                ''',
                'relay_statistics_vrf_name',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('statistics', REFERENCE_CLASS, 'Statistics_' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes.Node.Relay.Statistics.Ipv4DhcpdRelayStat.Statistics_', 
                [], [], 
                '''                Public relay statistics
                ''',
                'statistics',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'ipv4-dhcpd-relay-stat',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes.Node.Relay.Statistics' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes.Node.Relay.Statistics',
            False, 
            [
            _MetaInfoClassMember('ipv4-dhcpd-relay-stat', REFERENCE_LIST, 'Ipv4DhcpdRelayStat' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes.Node.Relay.Statistics.Ipv4DhcpdRelayStat', 
                [], [], 
                '''                ipv4 dhcpd relay stat
                ''',
                'ipv4_dhcpd_relay_stat',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.Discover' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.Discover',
            False, 
            [
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped packets
                ''',
                'dropped_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('transmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmitted packets
                ''',
                'transmitted_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'discover',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.Offer' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.Offer',
            False, 
            [
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped packets
                ''',
                'dropped_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('transmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmitted packets
                ''',
                'transmitted_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'offer',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.Request' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.Request',
            False, 
            [
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped packets
                ''',
                'dropped_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('transmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmitted packets
                ''',
                'transmitted_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'request',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.Decline' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.Decline',
            False, 
            [
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped packets
                ''',
                'dropped_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('transmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmitted packets
                ''',
                'transmitted_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'decline',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.Ack' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.Ack',
            False, 
            [
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped packets
                ''',
                'dropped_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('transmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmitted packets
                ''',
                'transmitted_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'ack',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.Nak' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.Nak',
            False, 
            [
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped packets
                ''',
                'dropped_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('transmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmitted packets
                ''',
                'transmitted_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'nak',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.Release' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.Release',
            False, 
            [
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped packets
                ''',
                'dropped_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('transmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmitted packets
                ''',
                'transmitted_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'release',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.Inform' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.Inform',
            False, 
            [
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped packets
                ''',
                'dropped_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('transmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmitted packets
                ''',
                'transmitted_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'inform',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.LeaseQuery' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.LeaseQuery',
            False, 
            [
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped packets
                ''',
                'dropped_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('transmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmitted packets
                ''',
                'transmitted_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'lease-query',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.LeaseNotAssigned' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.LeaseNotAssigned',
            False, 
            [
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped packets
                ''',
                'dropped_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('transmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmitted packets
                ''',
                'transmitted_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'lease-not-assigned',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.LeaseUnknown' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.LeaseUnknown',
            False, 
            [
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped packets
                ''',
                'dropped_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('transmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmitted packets
                ''',
                'transmitted_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'lease-unknown',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.LeaseActive' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.LeaseActive',
            False, 
            [
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped packets
                ''',
                'dropped_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('transmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmitted packets
                ''',
                'transmitted_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'lease-active',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.BootpRequest' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.BootpRequest',
            False, 
            [
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped packets
                ''',
                'dropped_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('transmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmitted packets
                ''',
                'transmitted_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'bootp-request',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.BootpReply' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.BootpReply',
            False, 
            [
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped packets
                ''',
                'dropped_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('transmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmitted packets
                ''',
                'transmitted_packets',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'bootp-reply',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics',
            False, 
            [
            _MetaInfoClassMember('ack', REFERENCE_CLASS, 'Ack' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.Ack', 
                [], [], 
                '''                DHCP ack packets
                ''',
                'ack',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('bootp-reply', REFERENCE_CLASS, 'BootpReply' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.BootpReply', 
                [], [], 
                '''                DHCP BOOTP reply
                ''',
                'bootp_reply',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('bootp-request', REFERENCE_CLASS, 'BootpRequest' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.BootpRequest', 
                [], [], 
                '''                DHCP BOOTP request
                ''',
                'bootp_request',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('decline', REFERENCE_CLASS, 'Decline' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.Decline', 
                [], [], 
                '''                DHCP decline packets
                ''',
                'decline',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('discover', REFERENCE_CLASS, 'Discover' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.Discover', 
                [], [], 
                '''                DHCP discover packets
                ''',
                'discover',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('inform', REFERENCE_CLASS, 'Inform' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.Inform', 
                [], [], 
                '''                DHCP inform packets
                ''',
                'inform',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('lease-active', REFERENCE_CLASS, 'LeaseActive' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.LeaseActive', 
                [], [], 
                '''                DHCP lease active
                ''',
                'lease_active',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('lease-not-assigned', REFERENCE_CLASS, 'LeaseNotAssigned' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.LeaseNotAssigned', 
                [], [], 
                '''                DHCP lease not assigned
                ''',
                'lease_not_assigned',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('lease-query', REFERENCE_CLASS, 'LeaseQuery' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.LeaseQuery', 
                [], [], 
                '''                DHCP lease query packets
                ''',
                'lease_query',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('lease-unknown', REFERENCE_CLASS, 'LeaseUnknown' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.LeaseUnknown', 
                [], [], 
                '''                DHCP lease unknown
                ''',
                'lease_unknown',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('nak', REFERENCE_CLASS, 'Nak' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.Nak', 
                [], [], 
                '''                DHCP nak packets
                ''',
                'nak',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('offer', REFERENCE_CLASS, 'Offer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.Offer', 
                [], [], 
                '''                DHCP offer packets
                ''',
                'offer',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('release', REFERENCE_CLASS, 'Release' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.Release', 
                [], [], 
                '''                DHCP release packets
                ''',
                'release',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('request', REFERENCE_CLASS, 'Request' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.Request', 
                [], [], 
                '''                DHCP request packets
                ''',
                'request',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'vrf-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf',
            False, 
            [
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', True),
            _MetaInfoClassMember('vrf-statistics', REFERENCE_CLASS, 'VrfStatistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics', 
                [], [], 
                '''                IPv4 DHCP relay statistics
                ''',
                'vrf_statistics',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'vrf',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes.Node.Relay.Vrfs' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes.Node.Relay.Vrfs',
            False, 
            [
            _MetaInfoClassMember('vrf', REFERENCE_LIST, 'Vrf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf', 
                [], [], 
                '''                IPv4 DHCP relay VRF name
                ''',
                'vrf',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'vrfs',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes.Node.Relay' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes.Node.Relay',
            False, 
            [
            _MetaInfoClassMember('profiles', REFERENCE_CLASS, 'Profiles' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes.Node.Relay.Profiles', 
                [], [], 
                '''                DHCP Relay Profiles
                ''',
                'profiles',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('statistics', REFERENCE_CLASS, 'Statistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes.Node.Relay.Statistics', 
                [], [], 
                '''                DHCP Relay VRF statistics
                ''',
                'statistics',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('statistics-info', REFERENCE_CLASS, 'StatisticsInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes.Node.Relay.StatisticsInfo', 
                [], [], 
                '''                DHCP relay statistics info
                ''',
                'statistics_info',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('vrfs', REFERENCE_CLASS, 'Vrfs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes.Node.Relay.Vrfs', 
                [], [], 
                '''                DHCP relay list of VRF names
                ''',
                'vrfs',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'relay',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes.Node',
            False, 
            [
            _MetaInfoClassMember('nodeid', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                The node id to filter on. For eg., 0/1/CPU0
                ''',
                'nodeid',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', True),
            _MetaInfoClassMember('base', REFERENCE_CLASS, 'Base' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes.Node.Base', 
                [], [], 
                '''                IPv4 DHCP base operational data
                ''',
                'base',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes.Node.Interfaces', 
                [], [], 
                '''                IPv4 DHCP proxy/server Interface
                ''',
                'interfaces',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('proxy', REFERENCE_CLASS, 'Proxy' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes.Node.Proxy', 
                [], [], 
                '''                IPv4 DHCP proxy operational data
                ''',
                'proxy',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('relay', REFERENCE_CLASS, 'Relay' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes.Node.Relay', 
                [], [], 
                '''                IPv4 DHCPD Relay operational data
                ''',
                'relay',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('server', REFERENCE_CLASS, 'Server' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes.Node.Server', 
                [], [], 
                '''                IPv4 DHCP Server operational data
                ''',
                'server',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'node',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd.Nodes' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Nodes',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes.Node', 
                [], [], 
                '''                Location. For eg., 0/1/CPU0
                ''',
                'node',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'nodes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
    'Ipv4Dhcpd' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd',
            False, 
            [
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Nodes', 
                [], [], 
                '''                IPv4 DHCPD operational data for a particular
                location
                ''',
                'nodes',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            _MetaInfoClassMember('snoop', REFERENCE_CLASS, 'Snoop' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper', 'Ipv4Dhcpd.Snoop', 
                [], [], 
                '''                DHCP Snoop operational data
                ''',
                'snoop',
                'Cisco-IOS-XR-ipv4-dhcpd-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-oper',
            'ipv4-dhcpd',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_oper'
        ),
    },
}
_meta_table['DhcpClient.Nodes.Node.ClientStats.ClientStat']['meta_info'].parent =_meta_table['DhcpClient.Nodes.Node.ClientStats']['meta_info']
_meta_table['DhcpClient.Nodes.Node.Clients.Client']['meta_info'].parent =_meta_table['DhcpClient.Nodes.Node.Clients']['meta_info']
_meta_table['DhcpClient.Nodes.Node.ClientStats']['meta_info'].parent =_meta_table['DhcpClient.Nodes.Node']['meta_info']
_meta_table['DhcpClient.Nodes.Node.Clients']['meta_info'].parent =_meta_table['DhcpClient.Nodes.Node']['meta_info']
_meta_table['DhcpClient.Nodes.Node']['meta_info'].parent =_meta_table['DhcpClient.Nodes']['meta_info']
_meta_table['DhcpClient.Nodes']['meta_info'].parent =_meta_table['DhcpClient']['meta_info']
_meta_table['Ipv4Dhcpd.Snoop.Bindings.Binding']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Snoop.Bindings']['meta_info']
_meta_table['Ipv4Dhcpd.Snoop.Profiles.Profile']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Snoop.Profiles']['meta_info']
_meta_table['Ipv4Dhcpd.Snoop.Statistics.Statistic']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Snoop.Statistics']['meta_info']
_meta_table['Ipv4Dhcpd.Snoop.Bindings']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Snoop']['meta_info']
_meta_table['Ipv4Dhcpd.Snoop.BindingStatistics']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Snoop']['meta_info']
_meta_table['Ipv4Dhcpd.Snoop.StatisticsInfo']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Snoop']['meta_info']
_meta_table['Ipv4Dhcpd.Snoop.Profiles']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Snoop']['meta_info']
_meta_table['Ipv4Dhcpd.Snoop.Statistics']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Snoop']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Discover']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Offer']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Request']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Decline']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Ack']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Nak']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Release']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.Inform']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.LeaseQuery']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.LeaseNotAssigned']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.LeaseUnknown']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.LeaseActive']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.BootpRequest']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics.BootpReply']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf.Statistics']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs.Vrf']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes.Node.Proxy.Profiles.Profile.VrfReferences.Ipv4DhcpdProxyVrfReference']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Nodes.Node.Proxy.Profiles.Profile.VrfReferences']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes.Node.Proxy.Profiles.Profile.InterfaceReferences.Ipv4DhcpdProxyInterfaceReference']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Nodes.Node.Proxy.Profiles.Profile.InterfaceReferences']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes.Node.Proxy.Profiles.Profile.VrfReferences']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Nodes.Node.Proxy.Profiles.Profile']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes.Node.Proxy.Profiles.Profile.InterfaceReferences']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Nodes.Node.Proxy.Profiles.Profile']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes.Node.Proxy.Profiles.Profile']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Nodes.Node.Proxy.Profiles']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes.Node.Proxy.Statistics.Ipv4DhcpdProxyStat.Statistics_']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Nodes.Node.Proxy.Statistics.Ipv4DhcpdProxyStat']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes.Node.Proxy.Statistics.Ipv4DhcpdProxyStat']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Nodes.Node.Proxy.Statistics']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes.Node.Proxy.Binding.Clients.Client']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Nodes.Node.Proxy.Binding.Clients']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes.Node.Proxy.Binding.Clients']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Nodes.Node.Proxy.Binding']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes.Node.Proxy.Binding.Summary']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Nodes.Node.Proxy.Binding']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes.Node.Proxy.StatisticsInfo']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Nodes.Node.Proxy']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes.Node.Proxy.Vrfs']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Nodes.Node.Proxy']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes.Node.Proxy.Profiles']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Nodes.Node.Proxy']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes.Node.Proxy.Statistics']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Nodes.Node.Proxy']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes.Node.Proxy.Binding']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Nodes.Node.Proxy']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes.Node.Interfaces.Interface']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Nodes.Node.Interfaces']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes.Node.Base.Statistics.Ipv4DhcpdProxyStat.Statistics_']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Nodes.Node.Base.Statistics.Ipv4DhcpdProxyStat']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes.Node.Base.Statistics.Ipv4DhcpdProxyStat']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Nodes.Node.Base.Statistics']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.Discover']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.Offer']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.Request']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.Decline']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.Ack']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.Nak']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.Release']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.Inform']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.LeaseQuery']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.LeaseNotAssigned']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.LeaseUnknown']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.LeaseActive']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.BootpRequest']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics.BootpReply']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf.Statistics']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes.Node.Base.Vrfs.Vrf']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Nodes.Node.Base.Vrfs']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes.Node.Base.Profiles.Profile.InterfaceReferences.Ipv4DhcpdBaseInterfaceReference']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Nodes.Node.Base.Profiles.Profile.InterfaceReferences']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes.Node.Base.Profiles.Profile.ChildProfileInfo.Ipv4DhcpdBaseChildProfileInfo']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Nodes.Node.Base.Profiles.Profile.ChildProfileInfo']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes.Node.Base.Profiles.Profile.InterfaceReferences']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Nodes.Node.Base.Profiles.Profile']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes.Node.Base.Profiles.Profile.ChildProfileInfo']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Nodes.Node.Base.Profiles.Profile']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes.Node.Base.Profiles.Profile']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Nodes.Node.Base.Profiles']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes.Node.Base.Statistics']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Nodes.Node.Base']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes.Node.Base.IssuStatus']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Nodes.Node.Base']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes.Node.Base.Vrfs']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Nodes.Node.Base']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes.Node.Base.Profiles']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Nodes.Node.Base']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes.Node.Base.Database']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Nodes.Node.Base']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes.Node.Server.Profiles.Profile']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Nodes.Node.Server.Profiles']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes.Node.Server.Statistics.Ipv4DhcpdProxyStat.Statistics_']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Nodes.Node.Server.Statistics.Ipv4DhcpdProxyStat']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes.Node.Server.Statistics.Ipv4DhcpdProxyStat']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Nodes.Node.Server.Statistics']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes.Node.Server.Binding.Clients.Client']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Nodes.Node.Server.Binding.Clients']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes.Node.Server.Binding.Summary']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Nodes.Node.Server.Binding']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes.Node.Server.Binding.Clients']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Nodes.Node.Server.Binding']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.Discover']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.Offer']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.Request']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.Decline']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.Ack']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.Nak']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.Release']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.Inform']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.LeaseQuery']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.LeaseNotAssigned']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.LeaseUnknown']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.LeaseActive']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.BootpRequest']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics.BootpReply']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf.Statistics']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes.Node.Server.Vrfs.Vrf']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Nodes.Node.Server.Vrfs']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes.Node.Server.Profiles']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Nodes.Node.Server']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes.Node.Server.Statistics']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Nodes.Node.Server']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes.Node.Server.Binding']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Nodes.Node.Server']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes.Node.Server.StatisticsInfo']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Nodes.Node.Server']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes.Node.Server.Vrfs']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Nodes.Node.Server']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes.Node.Relay.Profiles.Profile']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Nodes.Node.Relay.Profiles']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes.Node.Relay.Statistics.Ipv4DhcpdRelayStat.Statistics_']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Nodes.Node.Relay.Statistics.Ipv4DhcpdRelayStat']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes.Node.Relay.Statistics.Ipv4DhcpdRelayStat']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Nodes.Node.Relay.Statistics']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.Discover']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.Offer']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.Request']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.Decline']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.Ack']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.Nak']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.Release']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.Inform']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.LeaseQuery']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.LeaseNotAssigned']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.LeaseUnknown']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.LeaseActive']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.BootpRequest']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics.BootpReply']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf.VrfStatistics']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes.Node.Relay.Vrfs.Vrf']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Nodes.Node.Relay.Vrfs']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes.Node.Relay.Profiles']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Nodes.Node.Relay']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes.Node.Relay.StatisticsInfo']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Nodes.Node.Relay']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes.Node.Relay.Statistics']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Nodes.Node.Relay']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes.Node.Relay.Vrfs']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Nodes.Node.Relay']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes.Node.Proxy']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Nodes.Node']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes.Node.Interfaces']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Nodes.Node']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes.Node.Base']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Nodes.Node']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes.Node.Server']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Nodes.Node']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes.Node.Relay']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Nodes.Node']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes.Node']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Nodes']['meta_info']
_meta_table['Ipv4Dhcpd.Snoop']['meta_info'].parent =_meta_table['Ipv4Dhcpd']['meta_info']
_meta_table['Ipv4Dhcpd.Nodes']['meta_info'].parent =_meta_table['Ipv4Dhcpd']['meta_info']
