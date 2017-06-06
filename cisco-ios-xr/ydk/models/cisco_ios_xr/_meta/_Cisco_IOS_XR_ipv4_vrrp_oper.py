


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'VrrpVmacStateEnum' : _MetaInfoEnum('VrrpVmacStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper',
        {
            'stored':'stored',
            'reserved':'reserved',
            'active':'active',
            'reserving':'reserving',
        }, 'Cisco-IOS-XR-ipv4-vrrp-oper', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-vrrp-oper']),
    'VrrpProtAuthEnum' : _MetaInfoEnum('VrrpProtAuthEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper',
        {
            'authentication-none':'authentication_none',
            'authentication-text':'authentication_text',
            'authentication-ip':'authentication_ip',
        }, 'Cisco-IOS-XR-ipv4-vrrp-oper', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-vrrp-oper']),
    'VrrpBAfEnum' : _MetaInfoEnum('VrrpBAfEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper',
        {
            'address-family-ipv4':'address_family_ipv4',
            'address-family-ipv6':'address_family_ipv6',
            'vrrp-baf-count':'vrrp_baf_count',
        }, 'Cisco-IOS-XR-ipv4-vrrp-oper', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-vrrp-oper']),
    'VrrpBfdSessionStateEnum' : _MetaInfoEnum('VrrpBfdSessionStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper',
        {
            'bfd-state-none':'bfd_state_none',
            'bfd-state-inactive':'bfd_state_inactive',
            'bfd-state-up':'bfd_state_up',
            'bfd-state-down':'bfd_state_down',
        }, 'Cisco-IOS-XR-ipv4-vrrp-oper', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-vrrp-oper']),
    'VrrpBagProtocolStateEnum' : _MetaInfoEnum('VrrpBagProtocolStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper',
        {
            'state-initial':'state_initial',
            'state-backup':'state_backup',
            'state-master':'state_master',
        }, 'Cisco-IOS-XR-ipv4-vrrp-oper', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-vrrp-oper']),
    'VrrpStateChangeReasonEnum' : _MetaInfoEnum('VrrpStateChangeReasonEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper',
        {
            'state-change-bfd-down':'state_change_bfd_down',
            'state-change-virtual-ip-configured':'state_change_virtual_ip_configured',
            'state-change-interface-ip':'state_change_interface_ip',
            'state-change-delay-timer':'state_change_delay_timer',
            'state-change-startup':'state_change_startup',
            'state-change-interface-up':'state_change_interface_up',
            'state-change-interface-down':'state_change_interface_down',
            'state-change-master-down-timer':'state_change_master_down_timer',
            'state-change-higher-priority-master':'state_change_higher_priority_master',
            'state-change-fhrp-admin':'state_change_fhrp_admin',
            'state-change-mgo-parent':'state_change_mgo_parent',
            'state-change-chkpt-update':'state_change_chkpt_update',
            'state-change-issu-resync':'state_change_issu_resync',
        }, 'Cisco-IOS-XR-ipv4-vrrp-oper', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-vrrp-oper']),
    'VrrpVipStateEnum' : _MetaInfoEnum('VrrpVipStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper',
        {
            'virtual-ip-state-down':'virtual_ip_state_down',
            'virtual-ip-state-up':'virtual_ip_state_up',
        }, 'Cisco-IOS-XR-ipv4-vrrp-oper', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-vrrp-oper']),
    'Vrrp.Summary' : {
        'meta_info' : _MetaInfoClass('Vrrp.Summary',
            False, 
            [
            _MetaInfoClassMember('bfd-session-inactive', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of VRRP IPv4 BFD sessions in INACTIVE
                state
                ''',
                'bfd_session_inactive',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('bfd-sessions-down', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of VRRP IPv4 BFD sessions in DOWN state
                ''',
                'bfd_sessions_down',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('bfd-sessions-up', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of VRRP IPv4 BFD sessions in UP state
                ''',
                'bfd_sessions_up',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('interfaces-ipv4-state-down', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of VRRP interfaces with IPv4 caps in DOWN
                state
                ''',
                'interfaces_ipv4_state_down',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('interfaces-ipv4-state-up', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of VRRP interfaces with IPv4 caps in UP
                state
                ''',
                'interfaces_ipv4_state_up',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('interfaces-ipv6-state-down', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of VRRP interfaces with IPv6 caps in DOWN
                state
                ''',
                'interfaces_ipv6_state_down',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('interfaces-ipv6-state-up', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of VRRP interfaces with IPv6 caps in UP
                state
                ''',
                'interfaces_ipv6_state_up',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('ipv4-sessions-backup', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of IPv4 sessions in BACKUP state
                ''',
                'ipv4_sessions_backup',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('ipv4-sessions-init', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of IPv4 sessions in INIT state
                ''',
                'ipv4_sessions_init',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('ipv4-sessions-master', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of IPv4 sessions in MASTER state
                ''',
                'ipv4_sessions_master',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('ipv4-sessions-master-owner', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of IPv4 sessions in MASTER (owner) state
                ''',
                'ipv4_sessions_master_owner',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('ipv4-slaves-backup', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of IPv4 slaves in BACKUP state
                ''',
                'ipv4_slaves_backup',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('ipv4-slaves-init', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of IPv4 slaves in INIT state
                ''',
                'ipv4_slaves_init',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('ipv4-slaves-master', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of IPv4 slaves in MASTER state
                ''',
                'ipv4_slaves_master',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('ipv4-virtual-ip-addresses-backup-down', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of DOWN IPv4 Virtual IP Addresses on
                virtual routers in BACKUP state
                ''',
                'ipv4_virtual_ip_addresses_backup_down',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('ipv4-virtual-ip-addresses-backup-up', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of UP IPv4 Virtual IP Addresses on
                virtual routers in BACKUP state
                ''',
                'ipv4_virtual_ip_addresses_backup_up',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('ipv4-virtual-ip-addresses-init-down', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of DOWN IPv4 Virtual IP Addresses on
                virtual routers in INIT state
                ''',
                'ipv4_virtual_ip_addresses_init_down',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('ipv4-virtual-ip-addresses-init-up', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of UP IPv4 Virtual IP Addresses on
                virtual routers in INIT state
                ''',
                'ipv4_virtual_ip_addresses_init_up',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('ipv4-virtual-ip-addresses-master-down', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of DOWN IPv4 Virtual IP Addresses on
                virtual routers in MASTER state
                ''',
                'ipv4_virtual_ip_addresses_master_down',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('ipv4-virtual-ip-addresses-master-owner-down', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of DOWN IPv4 Virtual IP Addresses on
                virtual routers in MASTER (owner) state
                ''',
                'ipv4_virtual_ip_addresses_master_owner_down',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('ipv4-virtual-ip-addresses-master-owner-up', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of UP IPv4 Virtual IP Addresses on
                virtual routers in MASTER (owner) state
                ''',
                'ipv4_virtual_ip_addresses_master_owner_up',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('ipv4-virtual-ip-addresses-master-up', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of UP IPv4 Virtual IP Addresses on
                virtual routers in MASTER state
                ''',
                'ipv4_virtual_ip_addresses_master_up',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('ipv6-sessions-backup', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of IPv6 sessions in BACKUP state
                ''',
                'ipv6_sessions_backup',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('ipv6-sessions-init', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of IPv6 sessions in INIT state
                ''',
                'ipv6_sessions_init',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('ipv6-sessions-master', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of IPv6 sessions in MASTER state
                ''',
                'ipv6_sessions_master',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('ipv6-sessions-master-owner', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of IPv6 sessions in MASTER (owner) state
                ''',
                'ipv6_sessions_master_owner',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('ipv6-slaves-backup', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of IPv6 slaves in BACKUP state
                ''',
                'ipv6_slaves_backup',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('ipv6-slaves-init', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of IPv6 slaves in INIT state
                ''',
                'ipv6_slaves_init',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('ipv6-slaves-master', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of IPv6 slaves in MASTER state
                ''',
                'ipv6_slaves_master',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('ipv6-virtual-ip-addresses-backup-down', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of DOWN IPv6 Virtual IP Addresses on
                virtual routers in BACKUP state
                ''',
                'ipv6_virtual_ip_addresses_backup_down',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('ipv6-virtual-ip-addresses-backup-up', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of UP IPv6 Virtual IP Addresses on
                virtual routers in BACKUP state
                ''',
                'ipv6_virtual_ip_addresses_backup_up',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('ipv6-virtual-ip-addresses-init-down', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of DOWN IPv6 Virtual IP Addresses on
                virtual routers in INIT state
                ''',
                'ipv6_virtual_ip_addresses_init_down',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('ipv6-virtual-ip-addresses-init-up', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of UP IPv6 Virtual IP Addresses on
                virtual routers in INIT state
                ''',
                'ipv6_virtual_ip_addresses_init_up',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('ipv6-virtual-ip-addresses-master-down', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of DOWN IPv6 Virtual IP Addresses on
                virtual routers in MASTER state
                ''',
                'ipv6_virtual_ip_addresses_master_down',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('ipv6-virtual-ip-addresses-master-owner-down', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of DOWN IPv6 Virtual IP Addresses on
                virtual routers in MASTER (owner) state
                ''',
                'ipv6_virtual_ip_addresses_master_owner_down',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('ipv6-virtual-ip-addresses-master-owner-up', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of UP IPv6 Virtual IP Addresses on
                virtual routers in MASTER (owner) state
                ''',
                'ipv6_virtual_ip_addresses_master_owner_up',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('ipv6-virtual-ip-addresses-master-up', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of UP IPv6 Virtual IP Addresses on
                virtual routers in MASTER state
                ''',
                'ipv6_virtual_ip_addresses_master_up',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('ipv6bfd-session-inactive', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of VRRP IPv6 BFD sessions in INACTIVE
                state
                ''',
                'ipv6bfd_session_inactive',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('ipv6bfd-sessions-down', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of VRRP IPv6 BFD sessions in DOWN state
                ''',
                'ipv6bfd_sessions_down',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('ipv6bfd-sessions-up', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of VRRP IPv6 BFD sessions in UP state
                ''',
                'ipv6bfd_sessions_up',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('tracked-interfaces-ipv4-state-down', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of tracked interfaces with IPv4 caps in
                DOWN state
                ''',
                'tracked_interfaces_ipv4_state_down',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('tracked-interfaces-ipv4-state-up', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of tracked interfaces with IPv4 caps in
                UP state
                ''',
                'tracked_interfaces_ipv4_state_up',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('tracked-interfaces-ipv6-state-down', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of tracked interfaces with IPv6 caps in
                DOWN state
                ''',
                'tracked_interfaces_ipv6_state_down',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('tracked-interfaces-ipv6-state-up', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of tracked interfaces with IPv6 caps in
                UP state
                ''',
                'tracked_interfaces_ipv6_state_up',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('tracked-objects-state-down', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of tracked objects in DOWN state
                ''',
                'tracked_objects_state_down',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('tracked-objects-state-up', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of tracked objects in UP state
                ''',
                'tracked_objects_state_up',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-oper',
            'summary',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-vrrp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper'
        ),
    },
    'Vrrp.Ipv6.TrackItems.TrackItem' : {
        'meta_info' : _MetaInfoClass('Vrrp.Ipv6.TrackItems.TrackItem',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                The interface name to track
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-vrrp-oper', True),
            _MetaInfoClassMember('virtual-router-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The VRRP virtual router id
                ''',
                'virtual_router_id',
                'Cisco-IOS-XR-ipv4-vrrp-oper', True),
            _MetaInfoClassMember('tracked-interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                The name of the tracked interface
                ''',
                'tracked_interface_name',
                'Cisco-IOS-XR-ipv4-vrrp-oper', True),
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                IM Interface
                ''',
                'interface',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Priority weight of item
                ''',
                'priority',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('state', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                State of the tracked item
                ''',
                'state',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('tracked-item-index', ATTRIBUTE, 'str' , None, None, 
                [(0, 32)], [], 
                '''                Tracked item index
                ''',
                'tracked_item_index',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('tracked-item-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Type of tracked item
                ''',
                'tracked_item_type',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('virtual-router-id-xr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Virtual Router ID
                ''',
                'virtual_router_id_xr',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-oper',
            'track-item',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-vrrp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper'
        ),
    },
    'Vrrp.Ipv6.TrackItems' : {
        'meta_info' : _MetaInfoClass('Vrrp.Ipv6.TrackItems',
            False, 
            [
            _MetaInfoClassMember('track-item', REFERENCE_LIST, 'TrackItem' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper', 'Vrrp.Ipv6.TrackItems.TrackItem', 
                [], [], 
                '''                A configured VRRP IP address entry
                ''',
                'track_item',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-oper',
            'track-items',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-vrrp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper'
        ),
    },
    'Vrrp.Ipv6.VirtualRouters.VirtualRouter.ResignSentTime' : {
        'meta_info' : _MetaInfoClass('Vrrp.Ipv6.VirtualRouters.VirtualRouter.ResignSentTime',
            False, 
            [
            _MetaInfoClassMember('nanoseconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Nanoseconds
                ''',
                'nanoseconds',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Seconds
                ''',
                'seconds',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-oper',
            'resign-sent-time',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-vrrp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper'
        ),
    },
    'Vrrp.Ipv6.VirtualRouters.VirtualRouter.ResignReceivedTime' : {
        'meta_info' : _MetaInfoClass('Vrrp.Ipv6.VirtualRouters.VirtualRouter.ResignReceivedTime',
            False, 
            [
            _MetaInfoClassMember('nanoseconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Nanoseconds
                ''',
                'nanoseconds',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Seconds
                ''',
                'seconds',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-oper',
            'resign-received-time',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-vrrp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper'
        ),
    },
    'Vrrp.Ipv6.VirtualRouters.VirtualRouter.Ipv6OperationalAddress' : {
        'meta_info' : _MetaInfoClass('Vrrp.Ipv6.VirtualRouters.VirtualRouter.Ipv6OperationalAddress',
            False, 
            [
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPV6Address
                ''',
                'ipv6_address',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-oper',
            'ipv6-operational-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-vrrp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper'
        ),
    },
    'Vrrp.Ipv6.VirtualRouters.VirtualRouter.Ipv6ConfiguredDownAddress' : {
        'meta_info' : _MetaInfoClass('Vrrp.Ipv6.VirtualRouters.VirtualRouter.Ipv6ConfiguredDownAddress',
            False, 
            [
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPV6Address
                ''',
                'ipv6_address',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-oper',
            'ipv6-configured-down-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-vrrp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper'
        ),
    },
    'Vrrp.Ipv6.VirtualRouters.VirtualRouter.StateChangeHistory.Time' : {
        'meta_info' : _MetaInfoClass('Vrrp.Ipv6.VirtualRouters.VirtualRouter.StateChangeHistory.Time',
            False, 
            [
            _MetaInfoClassMember('nanoseconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Nanoseconds
                ''',
                'nanoseconds',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Seconds
                ''',
                'seconds',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-oper',
            'time',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-vrrp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper'
        ),
    },
    'Vrrp.Ipv6.VirtualRouters.VirtualRouter.StateChangeHistory' : {
        'meta_info' : _MetaInfoClass('Vrrp.Ipv6.VirtualRouters.VirtualRouter.StateChangeHistory',
            False, 
            [
            _MetaInfoClassMember('new-state', REFERENCE_ENUM_CLASS, 'VrrpBagProtocolStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper', 'VrrpBagProtocolStateEnum', 
                [], [], 
                '''                New State
                ''',
                'new_state',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('old-state', REFERENCE_ENUM_CLASS, 'VrrpBagProtocolStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper', 'VrrpBagProtocolStateEnum', 
                [], [], 
                '''                Old State
                ''',
                'old_state',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('reason', REFERENCE_ENUM_CLASS, 'VrrpStateChangeReasonEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper', 'VrrpStateChangeReasonEnum', 
                [], [], 
                '''                Reason for state change
                ''',
                'reason',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('time', REFERENCE_CLASS, 'Time' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper', 'Vrrp.Ipv6.VirtualRouters.VirtualRouter.StateChangeHistory.Time', 
                [], [], 
                '''                Time of state change
                ''',
                'time',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-oper',
            'state-change-history',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-vrrp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper'
        ),
    },
    'Vrrp.Ipv6.VirtualRouters.VirtualRouter' : {
        'meta_info' : _MetaInfoClass('Vrrp.Ipv6.VirtualRouters.VirtualRouter',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                The name of the interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-vrrp-oper', True),
            _MetaInfoClassMember('virtual-router-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The VRRP virtual router id
                ''',
                'virtual_router_id',
                'Cisco-IOS-XR-ipv4-vrrp-oper', True),
            _MetaInfoClassMember('address-family', REFERENCE_ENUM_CLASS, 'VrrpBAfEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper', 'VrrpBAfEnum', 
                [], [], 
                '''                Address family
                ''',
                'address_family',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('address-list-error-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Address list errors
                ''',
                'address_list_error_count',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('advert-interval-error-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Advertise interval errors
                ''',
                'advert_interval_error_count',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('adverts-received-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                No. of advertisements received
                ''',
                'adverts_received_count',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('adverts-sent-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                No. of advertisements sent
                ''',
                'adverts_sent_count',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('auth-type-mismatch-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Authentication type mismatches
                ''',
                'auth_type_mismatch_count',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('authentication-fail-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Authentication failures
                ''',
                'authentication_fail_count',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('authentication-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Text authentication configured flag
                ''',
                'authentication_flag',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('authentication-string', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Authentication data
                ''',
                'authentication_string',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('authentication-type', REFERENCE_ENUM_CLASS, 'VrrpProtAuthEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper', 'VrrpProtAuthEnum', 
                [], [], 
                '''                Authentication type
                ''',
                'authentication_type',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('bfd-cfg-remote-ip', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                BFD configured remote IP
                ''',
                'bfd_cfg_remote_ip',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('bfd-configured-remote-ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                BFD configured remote IPv6
                ''',
                'bfd_configured_remote_ipv6_address',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('bfd-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                BFD packet send interval
                ''',
                'bfd_interval',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('bfd-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                BFD multiplier
                ''',
                'bfd_multiplier',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('bfd-session-state', REFERENCE_ENUM_CLASS, 'VrrpBfdSessionStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper', 'VrrpBfdSessionStateEnum', 
                [], [], 
                '''                BFD session state
                ''',
                'bfd_session_state',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('configured-advertize-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Configured advertize time
                ''',
                'configured_advertize_time',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('configured-down-address-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                 Configured but Down VRRP address count
                ''',
                'configured_down_address_count',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('configured-priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Configured priority
                ''',
                'configured_priority',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('delay-timer-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Delay timer running flag
                ''',
                'delay_timer_flag',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('delay-timer-msecs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Delay timer running time msecs
                ''',
                'delay_timer_msecs',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('delay-timer-secs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Delay timer running time secs
                ''',
                'delay_timer_secs',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('followed-session-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 16)], [], 
                '''                Followed Session Name
                ''',
                'followed_session_name',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('force-timer-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Configured timers forced flag
                ''',
                'force_timer_flag',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('interface-ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The Interface Primary IPv4 address
                ''',
                'interface_ipv4_address',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('interface-ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                The Interface linklocal IPv6 address
                ''',
                'interface_ipv6_address',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('interface-name-xr', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                IM Interface Name
                ''',
                'interface_name_xr',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('invalid-auth-type-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Invalid authentication type
                ''',
                'invalid_auth_type_count',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('invalid-packet-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Invalid packets received
                ''',
                'invalid_packet_count',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('ip-address-owner-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                IP address owner flag
                ''',
                'ip_address_owner_flag',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('ipv4-configured-down-address', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 Configured but Down VRRP addresses
                ''',
                'ipv4_configured_down_address',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('ipv6-configured-down-address', REFERENCE_LIST, 'Ipv6ConfiguredDownAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper', 'Vrrp.Ipv6.VirtualRouters.VirtualRouter.Ipv6ConfiguredDownAddress', 
                [], [], 
                '''                IPv6 Configured but Down VRRP addresses
                ''',
                'ipv6_configured_down_address',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('ipv6-operational-address', REFERENCE_LIST, 'Ipv6OperationalAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper', 'Vrrp.Ipv6.VirtualRouters.VirtualRouter.Ipv6OperationalAddress', 
                [], [], 
                '''                IPv6 Operational VRRP addresses
                ''',
                'ipv6_operational_address',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('is-accept-mode', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is accept mode
                ''',
                'is_accept_mode',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('is-slave', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Group is a slave group
                ''',
                'is_slave',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('master-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                No. of times become Master
                ''',
                'master_count',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('master-ip-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Master router real IP address
                ''',
                'master_ip_address',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('master-ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                Master router real IPv6 address
                ''',
                'master_ipv6_address',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('master-priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Master router priority
                ''',
                'master_priority',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('min-delay-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Minimum delay time in msecs
                ''',
                'min_delay_time',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('oper-advertize-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Operational advertize time
                ''',
                'oper_advertize_time',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('operational-address', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Operational IPv4 VRRP addresses
                ''',
                'operational_address',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('operational-address-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Operational VRRP address count
                ''',
                'operational_address_count',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('operational-priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Operational priority
                ''',
                'operational_priority',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('pkt-length-errors-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Packet length errors
                ''',
                'pkt_length_errors_count',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('preempt-delay-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Preempt delay time
                ''',
                'preempt_delay_time',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('preempt-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Preempt configured flag
                ''',
                'preempt_flag',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('primary-state', REFERENCE_ENUM_CLASS, 'VrrpVipStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper', 'VrrpVipStateEnum', 
                [], [], 
                '''                State of primary IP address
                ''',
                'primary_state',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('primary-virtual-ip', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Configured IPv4 Primary address
                ''',
                'primary_virtual_ip',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('priority-decrement', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Priority decrement
                ''',
                'priority_decrement',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('priority-zero-received-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                No. priority 0 received
                ''',
                'priority_zero_received_count',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('priority-zero-sent-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                No. priority 0 sent
                ''',
                'priority_zero_sent_count',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('reload-delay-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Reload delay time in msecs
                ''',
                'reload_delay_time',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('resign-received-time', REFERENCE_CLASS, 'ResignReceivedTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper', 'Vrrp.Ipv6.VirtualRouters.VirtualRouter.ResignReceivedTime', 
                [], [], 
                '''                Time last resign was received
                ''',
                'resign_received_time',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('resign-sent-time', REFERENCE_CLASS, 'ResignSentTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper', 'Vrrp.Ipv6.VirtualRouters.VirtualRouter.ResignSentTime', 
                [], [], 
                '''                Time last resign was sent
                ''',
                'resign_sent_time',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('secondary-address-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Configured VRRP secondary address count
                ''',
                'secondary_address_count',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('session-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 16)], [], 
                '''                Session Name
                ''',
                'session_name',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('slaves', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of slaves following state
                ''',
                'slaves',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('state-change-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of state changes
                ''',
                'state_change_count',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('state-change-history', REFERENCE_LIST, 'StateChangeHistory' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper', 'Vrrp.Ipv6.VirtualRouters.VirtualRouter.StateChangeHistory', 
                [], [], 
                '''                State change history
                ''',
                'state_change_history',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('state-from-checkpoint', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Whether state recovered from checkpoint
                ''',
                'state_from_checkpoint',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('time-in-current-state', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Time in current state secs
                ''',
                'time_in_current_state',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('time-stats-discontinuity', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Time since a statistics discontinuity in ticks
                (10ns units)
                ''',
                'time_stats_discontinuity',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('time-vrouter-up', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Time vrouter is up in centiseconds
                ''',
                'time_vrouter_up',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('tracked-interface-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of items tracked
                ''',
                'tracked_interface_count',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('tracked-interface-up-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of tracked items up
                ''',
                'tracked_interface_up_count',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('tracked-item-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of tracked items
                ''',
                'tracked_item_count',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('tracked-item-up-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of tracked items in UP state
                ''',
                'tracked_item_up_count',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('ttl-error-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                TTL errors
                ''',
                'ttl_error_count',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                VRRP Protocol Version
                ''',
                'version',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('virtual-linklocal-ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                Virtual linklocal IPv6 address
                ''',
                'virtual_linklocal_ipv6_address',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('virtual-mac-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                Virtual mac address
                ''',
                'virtual_mac_address',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('virtual-mac-address-state', REFERENCE_ENUM_CLASS, 'VrrpVmacStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper', 'VrrpVmacStateEnum', 
                [], [], 
                '''                Virtual mac address state
                ''',
                'virtual_mac_address_state',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('virtual-router-id-xr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Virtual Router ID
                ''',
                'virtual_router_id_xr',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('vrrp-state', REFERENCE_ENUM_CLASS, 'VrrpBagProtocolStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper', 'VrrpBagProtocolStateEnum', 
                [], [], 
                '''                VRRP state
                ''',
                'vrrp_state',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-oper',
            'virtual-router',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-vrrp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper'
        ),
    },
    'Vrrp.Ipv6.VirtualRouters' : {
        'meta_info' : _MetaInfoClass('Vrrp.Ipv6.VirtualRouters',
            False, 
            [
            _MetaInfoClassMember('virtual-router', REFERENCE_LIST, 'VirtualRouter' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper', 'Vrrp.Ipv6.VirtualRouters.VirtualRouter', 
                [], [], 
                '''                A VRRP virtual router
                ''',
                'virtual_router',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-oper',
            'virtual-routers',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-vrrp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper'
        ),
    },
    'Vrrp.Ipv6.Interfaces.Interface' : {
        'meta_info' : _MetaInfoClass('Vrrp.Ipv6.Interfaces.Interface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                The name of the interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-vrrp-oper', True),
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                IM Interface
                ''',
                'interface',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('invalid-checksum-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Invalid checksum
                ''',
                'invalid_checksum_count',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('invalid-packet-length-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Bad packet lengths
                ''',
                'invalid_packet_length_count',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('invalid-version-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Unknown/unsupported version
                ''',
                'invalid_version_count',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('invalid-vrid-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Invalid vrID
                ''',
                'invalid_vrid_count',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-oper',
            'interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-vrrp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper'
        ),
    },
    'Vrrp.Ipv6.Interfaces' : {
        'meta_info' : _MetaInfoClass('Vrrp.Ipv6.Interfaces',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper', 'Vrrp.Ipv6.Interfaces.Interface', 
                [], [], 
                '''                A VRRP interface entry
                ''',
                'interface',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-oper',
            'interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-vrrp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper'
        ),
    },
    'Vrrp.Ipv6' : {
        'meta_info' : _MetaInfoClass('Vrrp.Ipv6',
            False, 
            [
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper', 'Vrrp.Ipv6.Interfaces', 
                [], [], 
                '''                The VRRP interface table
                ''',
                'interfaces',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('track-items', REFERENCE_CLASS, 'TrackItems' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper', 'Vrrp.Ipv6.TrackItems', 
                [], [], 
                '''                The VRRP tracked item table
                ''',
                'track_items',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('virtual-routers', REFERENCE_CLASS, 'VirtualRouters' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper', 'Vrrp.Ipv6.VirtualRouters', 
                [], [], 
                '''                The VRRP virtual router table
                ''',
                'virtual_routers',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-oper',
            'ipv6',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-vrrp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper'
        ),
    },
    'Vrrp.Ipv4.Interfaces.Interface' : {
        'meta_info' : _MetaInfoClass('Vrrp.Ipv4.Interfaces.Interface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                The name of the interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-vrrp-oper', True),
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                IM Interface
                ''',
                'interface',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('invalid-checksum-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Invalid checksum
                ''',
                'invalid_checksum_count',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('invalid-packet-length-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Bad packet lengths
                ''',
                'invalid_packet_length_count',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('invalid-version-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Unknown/unsupported version
                ''',
                'invalid_version_count',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('invalid-vrid-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Invalid vrID
                ''',
                'invalid_vrid_count',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-oper',
            'interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-vrrp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper'
        ),
    },
    'Vrrp.Ipv4.Interfaces' : {
        'meta_info' : _MetaInfoClass('Vrrp.Ipv4.Interfaces',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper', 'Vrrp.Ipv4.Interfaces.Interface', 
                [], [], 
                '''                A VRRP interface entry
                ''',
                'interface',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-oper',
            'interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-vrrp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper'
        ),
    },
    'Vrrp.Ipv4.TrackItems.TrackItem' : {
        'meta_info' : _MetaInfoClass('Vrrp.Ipv4.TrackItems.TrackItem',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                The interface name to track
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-vrrp-oper', True),
            _MetaInfoClassMember('virtual-router-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The VRRP virtual router id
                ''',
                'virtual_router_id',
                'Cisco-IOS-XR-ipv4-vrrp-oper', True),
            _MetaInfoClassMember('tracked-interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                The name of the tracked interface
                ''',
                'tracked_interface_name',
                'Cisco-IOS-XR-ipv4-vrrp-oper', True),
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                IM Interface
                ''',
                'interface',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Priority weight of item
                ''',
                'priority',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('state', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                State of the tracked item
                ''',
                'state',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('tracked-item-index', ATTRIBUTE, 'str' , None, None, 
                [(0, 32)], [], 
                '''                Tracked item index
                ''',
                'tracked_item_index',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('tracked-item-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Type of tracked item
                ''',
                'tracked_item_type',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('virtual-router-id-xr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Virtual Router ID
                ''',
                'virtual_router_id_xr',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-oper',
            'track-item',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-vrrp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper'
        ),
    },
    'Vrrp.Ipv4.TrackItems' : {
        'meta_info' : _MetaInfoClass('Vrrp.Ipv4.TrackItems',
            False, 
            [
            _MetaInfoClassMember('track-item', REFERENCE_LIST, 'TrackItem' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper', 'Vrrp.Ipv4.TrackItems.TrackItem', 
                [], [], 
                '''                A configured VRRP IP address entry
                ''',
                'track_item',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-oper',
            'track-items',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-vrrp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper'
        ),
    },
    'Vrrp.Ipv4.VirtualRouters.VirtualRouter.ResignSentTime' : {
        'meta_info' : _MetaInfoClass('Vrrp.Ipv4.VirtualRouters.VirtualRouter.ResignSentTime',
            False, 
            [
            _MetaInfoClassMember('nanoseconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Nanoseconds
                ''',
                'nanoseconds',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Seconds
                ''',
                'seconds',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-oper',
            'resign-sent-time',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-vrrp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper'
        ),
    },
    'Vrrp.Ipv4.VirtualRouters.VirtualRouter.ResignReceivedTime' : {
        'meta_info' : _MetaInfoClass('Vrrp.Ipv4.VirtualRouters.VirtualRouter.ResignReceivedTime',
            False, 
            [
            _MetaInfoClassMember('nanoseconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Nanoseconds
                ''',
                'nanoseconds',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Seconds
                ''',
                'seconds',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-oper',
            'resign-received-time',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-vrrp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper'
        ),
    },
    'Vrrp.Ipv4.VirtualRouters.VirtualRouter.Ipv6OperationalAddress' : {
        'meta_info' : _MetaInfoClass('Vrrp.Ipv4.VirtualRouters.VirtualRouter.Ipv6OperationalAddress',
            False, 
            [
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPV6Address
                ''',
                'ipv6_address',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-oper',
            'ipv6-operational-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-vrrp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper'
        ),
    },
    'Vrrp.Ipv4.VirtualRouters.VirtualRouter.Ipv6ConfiguredDownAddress' : {
        'meta_info' : _MetaInfoClass('Vrrp.Ipv4.VirtualRouters.VirtualRouter.Ipv6ConfiguredDownAddress',
            False, 
            [
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPV6Address
                ''',
                'ipv6_address',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-oper',
            'ipv6-configured-down-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-vrrp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper'
        ),
    },
    'Vrrp.Ipv4.VirtualRouters.VirtualRouter.StateChangeHistory.Time' : {
        'meta_info' : _MetaInfoClass('Vrrp.Ipv4.VirtualRouters.VirtualRouter.StateChangeHistory.Time',
            False, 
            [
            _MetaInfoClassMember('nanoseconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Nanoseconds
                ''',
                'nanoseconds',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Seconds
                ''',
                'seconds',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-oper',
            'time',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-vrrp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper'
        ),
    },
    'Vrrp.Ipv4.VirtualRouters.VirtualRouter.StateChangeHistory' : {
        'meta_info' : _MetaInfoClass('Vrrp.Ipv4.VirtualRouters.VirtualRouter.StateChangeHistory',
            False, 
            [
            _MetaInfoClassMember('new-state', REFERENCE_ENUM_CLASS, 'VrrpBagProtocolStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper', 'VrrpBagProtocolStateEnum', 
                [], [], 
                '''                New State
                ''',
                'new_state',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('old-state', REFERENCE_ENUM_CLASS, 'VrrpBagProtocolStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper', 'VrrpBagProtocolStateEnum', 
                [], [], 
                '''                Old State
                ''',
                'old_state',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('reason', REFERENCE_ENUM_CLASS, 'VrrpStateChangeReasonEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper', 'VrrpStateChangeReasonEnum', 
                [], [], 
                '''                Reason for state change
                ''',
                'reason',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('time', REFERENCE_CLASS, 'Time' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper', 'Vrrp.Ipv4.VirtualRouters.VirtualRouter.StateChangeHistory.Time', 
                [], [], 
                '''                Time of state change
                ''',
                'time',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-oper',
            'state-change-history',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-vrrp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper'
        ),
    },
    'Vrrp.Ipv4.VirtualRouters.VirtualRouter' : {
        'meta_info' : _MetaInfoClass('Vrrp.Ipv4.VirtualRouters.VirtualRouter',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                The name of the interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-vrrp-oper', True),
            _MetaInfoClassMember('virtual-router-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The VRRP virtual router id
                ''',
                'virtual_router_id',
                'Cisco-IOS-XR-ipv4-vrrp-oper', True),
            _MetaInfoClassMember('address-family', REFERENCE_ENUM_CLASS, 'VrrpBAfEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper', 'VrrpBAfEnum', 
                [], [], 
                '''                Address family
                ''',
                'address_family',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('address-list-error-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Address list errors
                ''',
                'address_list_error_count',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('advert-interval-error-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Advertise interval errors
                ''',
                'advert_interval_error_count',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('adverts-received-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                No. of advertisements received
                ''',
                'adverts_received_count',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('adverts-sent-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                No. of advertisements sent
                ''',
                'adverts_sent_count',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('auth-type-mismatch-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Authentication type mismatches
                ''',
                'auth_type_mismatch_count',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('authentication-fail-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Authentication failures
                ''',
                'authentication_fail_count',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('authentication-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Text authentication configured flag
                ''',
                'authentication_flag',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('authentication-string', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Authentication data
                ''',
                'authentication_string',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('authentication-type', REFERENCE_ENUM_CLASS, 'VrrpProtAuthEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper', 'VrrpProtAuthEnum', 
                [], [], 
                '''                Authentication type
                ''',
                'authentication_type',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('bfd-cfg-remote-ip', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                BFD configured remote IP
                ''',
                'bfd_cfg_remote_ip',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('bfd-configured-remote-ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                BFD configured remote IPv6
                ''',
                'bfd_configured_remote_ipv6_address',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('bfd-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                BFD packet send interval
                ''',
                'bfd_interval',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('bfd-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                BFD multiplier
                ''',
                'bfd_multiplier',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('bfd-session-state', REFERENCE_ENUM_CLASS, 'VrrpBfdSessionStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper', 'VrrpBfdSessionStateEnum', 
                [], [], 
                '''                BFD session state
                ''',
                'bfd_session_state',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('configured-advertize-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Configured advertize time
                ''',
                'configured_advertize_time',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('configured-down-address-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                 Configured but Down VRRP address count
                ''',
                'configured_down_address_count',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('configured-priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Configured priority
                ''',
                'configured_priority',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('delay-timer-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Delay timer running flag
                ''',
                'delay_timer_flag',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('delay-timer-msecs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Delay timer running time msecs
                ''',
                'delay_timer_msecs',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('delay-timer-secs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Delay timer running time secs
                ''',
                'delay_timer_secs',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('followed-session-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 16)], [], 
                '''                Followed Session Name
                ''',
                'followed_session_name',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('force-timer-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Configured timers forced flag
                ''',
                'force_timer_flag',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('interface-ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The Interface Primary IPv4 address
                ''',
                'interface_ipv4_address',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('interface-ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                The Interface linklocal IPv6 address
                ''',
                'interface_ipv6_address',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('interface-name-xr', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                IM Interface Name
                ''',
                'interface_name_xr',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('invalid-auth-type-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Invalid authentication type
                ''',
                'invalid_auth_type_count',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('invalid-packet-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Invalid packets received
                ''',
                'invalid_packet_count',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('ip-address-owner-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                IP address owner flag
                ''',
                'ip_address_owner_flag',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('ipv4-configured-down-address', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 Configured but Down VRRP addresses
                ''',
                'ipv4_configured_down_address',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('ipv6-configured-down-address', REFERENCE_LIST, 'Ipv6ConfiguredDownAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper', 'Vrrp.Ipv4.VirtualRouters.VirtualRouter.Ipv6ConfiguredDownAddress', 
                [], [], 
                '''                IPv6 Configured but Down VRRP addresses
                ''',
                'ipv6_configured_down_address',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('ipv6-operational-address', REFERENCE_LIST, 'Ipv6OperationalAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper', 'Vrrp.Ipv4.VirtualRouters.VirtualRouter.Ipv6OperationalAddress', 
                [], [], 
                '''                IPv6 Operational VRRP addresses
                ''',
                'ipv6_operational_address',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('is-accept-mode', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is accept mode
                ''',
                'is_accept_mode',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('is-slave', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Group is a slave group
                ''',
                'is_slave',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('master-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                No. of times become Master
                ''',
                'master_count',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('master-ip-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Master router real IP address
                ''',
                'master_ip_address',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('master-ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                Master router real IPv6 address
                ''',
                'master_ipv6_address',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('master-priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Master router priority
                ''',
                'master_priority',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('min-delay-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Minimum delay time in msecs
                ''',
                'min_delay_time',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('oper-advertize-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Operational advertize time
                ''',
                'oper_advertize_time',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('operational-address', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Operational IPv4 VRRP addresses
                ''',
                'operational_address',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('operational-address-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Operational VRRP address count
                ''',
                'operational_address_count',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('operational-priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Operational priority
                ''',
                'operational_priority',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('pkt-length-errors-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Packet length errors
                ''',
                'pkt_length_errors_count',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('preempt-delay-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Preempt delay time
                ''',
                'preempt_delay_time',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('preempt-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Preempt configured flag
                ''',
                'preempt_flag',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('primary-state', REFERENCE_ENUM_CLASS, 'VrrpVipStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper', 'VrrpVipStateEnum', 
                [], [], 
                '''                State of primary IP address
                ''',
                'primary_state',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('primary-virtual-ip', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Configured IPv4 Primary address
                ''',
                'primary_virtual_ip',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('priority-decrement', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Priority decrement
                ''',
                'priority_decrement',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('priority-zero-received-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                No. priority 0 received
                ''',
                'priority_zero_received_count',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('priority-zero-sent-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                No. priority 0 sent
                ''',
                'priority_zero_sent_count',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('reload-delay-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Reload delay time in msecs
                ''',
                'reload_delay_time',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('resign-received-time', REFERENCE_CLASS, 'ResignReceivedTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper', 'Vrrp.Ipv4.VirtualRouters.VirtualRouter.ResignReceivedTime', 
                [], [], 
                '''                Time last resign was received
                ''',
                'resign_received_time',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('resign-sent-time', REFERENCE_CLASS, 'ResignSentTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper', 'Vrrp.Ipv4.VirtualRouters.VirtualRouter.ResignSentTime', 
                [], [], 
                '''                Time last resign was sent
                ''',
                'resign_sent_time',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('secondary-address-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Configured VRRP secondary address count
                ''',
                'secondary_address_count',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('session-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 16)], [], 
                '''                Session Name
                ''',
                'session_name',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('slaves', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of slaves following state
                ''',
                'slaves',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('state-change-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of state changes
                ''',
                'state_change_count',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('state-change-history', REFERENCE_LIST, 'StateChangeHistory' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper', 'Vrrp.Ipv4.VirtualRouters.VirtualRouter.StateChangeHistory', 
                [], [], 
                '''                State change history
                ''',
                'state_change_history',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('state-from-checkpoint', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Whether state recovered from checkpoint
                ''',
                'state_from_checkpoint',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('time-in-current-state', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Time in current state secs
                ''',
                'time_in_current_state',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('time-stats-discontinuity', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Time since a statistics discontinuity in ticks
                (10ns units)
                ''',
                'time_stats_discontinuity',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('time-vrouter-up', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Time vrouter is up in centiseconds
                ''',
                'time_vrouter_up',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('tracked-interface-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of items tracked
                ''',
                'tracked_interface_count',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('tracked-interface-up-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of tracked items up
                ''',
                'tracked_interface_up_count',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('tracked-item-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of tracked items
                ''',
                'tracked_item_count',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('tracked-item-up-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of tracked items in UP state
                ''',
                'tracked_item_up_count',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('ttl-error-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                TTL errors
                ''',
                'ttl_error_count',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                VRRP Protocol Version
                ''',
                'version',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('virtual-linklocal-ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                Virtual linklocal IPv6 address
                ''',
                'virtual_linklocal_ipv6_address',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('virtual-mac-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                Virtual mac address
                ''',
                'virtual_mac_address',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('virtual-mac-address-state', REFERENCE_ENUM_CLASS, 'VrrpVmacStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper', 'VrrpVmacStateEnum', 
                [], [], 
                '''                Virtual mac address state
                ''',
                'virtual_mac_address_state',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('virtual-router-id-xr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Virtual Router ID
                ''',
                'virtual_router_id_xr',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('vrrp-state', REFERENCE_ENUM_CLASS, 'VrrpBagProtocolStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper', 'VrrpBagProtocolStateEnum', 
                [], [], 
                '''                VRRP state
                ''',
                'vrrp_state',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-oper',
            'virtual-router',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-vrrp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper'
        ),
    },
    'Vrrp.Ipv4.VirtualRouters' : {
        'meta_info' : _MetaInfoClass('Vrrp.Ipv4.VirtualRouters',
            False, 
            [
            _MetaInfoClassMember('virtual-router', REFERENCE_LIST, 'VirtualRouter' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper', 'Vrrp.Ipv4.VirtualRouters.VirtualRouter', 
                [], [], 
                '''                A VRRP virtual router
                ''',
                'virtual_router',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-oper',
            'virtual-routers',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-vrrp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper'
        ),
    },
    'Vrrp.Ipv4' : {
        'meta_info' : _MetaInfoClass('Vrrp.Ipv4',
            False, 
            [
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper', 'Vrrp.Ipv4.Interfaces', 
                [], [], 
                '''                The VRRP interface table
                ''',
                'interfaces',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('track-items', REFERENCE_CLASS, 'TrackItems' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper', 'Vrrp.Ipv4.TrackItems', 
                [], [], 
                '''                The VRRP tracked item table
                ''',
                'track_items',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('virtual-routers', REFERENCE_CLASS, 'VirtualRouters' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper', 'Vrrp.Ipv4.VirtualRouters', 
                [], [], 
                '''                The VRRP virtual router table
                ''',
                'virtual_routers',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-oper',
            'ipv4',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-vrrp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper'
        ),
    },
    'Vrrp.MgoSessions.MgoSession.Slave' : {
        'meta_info' : _MetaInfoClass('Vrrp.MgoSessions.MgoSession.Slave',
            False, 
            [
            _MetaInfoClassMember('slave-interface', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Interface of slave
                ''',
                'slave_interface',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('slave-virtual-router-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                VRID of slave
                ''',
                'slave_virtual_router_id',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-oper',
            'slave',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-vrrp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper'
        ),
    },
    'Vrrp.MgoSessions.MgoSession' : {
        'meta_info' : _MetaInfoClass('Vrrp.MgoSessions.MgoSession',
            False, 
            [
            _MetaInfoClassMember('session-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the session
                ''',
                'session_name',
                'Cisco-IOS-XR-ipv4-vrrp-oper', True),
            _MetaInfoClassMember('primary-af-name', REFERENCE_ENUM_CLASS, 'VrrpBAfEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper', 'VrrpBAfEnum', 
                [], [], 
                '''                Address family of primary session
                ''',
                'primary_af_name',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('primary-session-interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface of primary session
                ''',
                'primary_session_interface',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('primary-session-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 16)], [], 
                '''                Session Name
                ''',
                'primary_session_name',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('primary-session-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                VRID of primary session
                ''',
                'primary_session_number',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('primary-session-state', REFERENCE_ENUM_CLASS, 'VrrpBagProtocolStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper', 'VrrpBagProtocolStateEnum', 
                [], [], 
                '''                State of primary session
                ''',
                'primary_session_state',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('slave', REFERENCE_LIST, 'Slave' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper', 'Vrrp.MgoSessions.MgoSession.Slave', 
                [], [], 
                '''                List of slaves following this primary session
                ''',
                'slave',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-oper',
            'mgo-session',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-vrrp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper'
        ),
    },
    'Vrrp.MgoSessions' : {
        'meta_info' : _MetaInfoClass('Vrrp.MgoSessions',
            False, 
            [
            _MetaInfoClassMember('mgo-session', REFERENCE_LIST, 'MgoSession' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper', 'Vrrp.MgoSessions.MgoSession', 
                [], [], 
                '''                A VRRP MGO Session
                ''',
                'mgo_session',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-oper',
            'mgo-sessions',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-vrrp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper'
        ),
    },
    'Vrrp' : {
        'meta_info' : _MetaInfoClass('Vrrp',
            False, 
            [
            _MetaInfoClassMember('ipv4', REFERENCE_CLASS, 'Ipv4' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper', 'Vrrp.Ipv4', 
                [], [], 
                '''                IPv4 VRRP configuration
                ''',
                'ipv4',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('ipv6', REFERENCE_CLASS, 'Ipv6' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper', 'Vrrp.Ipv6', 
                [], [], 
                '''                IPv6 VRRP configuration
                ''',
                'ipv6',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('mgo-sessions', REFERENCE_CLASS, 'MgoSessions' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper', 'Vrrp.MgoSessions', 
                [], [], 
                '''                VRRP MGO Session information
                ''',
                'mgo_sessions',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            _MetaInfoClassMember('summary', REFERENCE_CLASS, 'Summary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper', 'Vrrp.Summary', 
                [], [], 
                '''                VRRP summary statistics
                ''',
                'summary',
                'Cisco-IOS-XR-ipv4-vrrp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-oper',
            'vrrp',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-vrrp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_vrrp_oper'
        ),
    },
}
_meta_table['Vrrp.Ipv6.TrackItems.TrackItem']['meta_info'].parent =_meta_table['Vrrp.Ipv6.TrackItems']['meta_info']
_meta_table['Vrrp.Ipv6.VirtualRouters.VirtualRouter.StateChangeHistory.Time']['meta_info'].parent =_meta_table['Vrrp.Ipv6.VirtualRouters.VirtualRouter.StateChangeHistory']['meta_info']
_meta_table['Vrrp.Ipv6.VirtualRouters.VirtualRouter.ResignSentTime']['meta_info'].parent =_meta_table['Vrrp.Ipv6.VirtualRouters.VirtualRouter']['meta_info']
_meta_table['Vrrp.Ipv6.VirtualRouters.VirtualRouter.ResignReceivedTime']['meta_info'].parent =_meta_table['Vrrp.Ipv6.VirtualRouters.VirtualRouter']['meta_info']
_meta_table['Vrrp.Ipv6.VirtualRouters.VirtualRouter.Ipv6OperationalAddress']['meta_info'].parent =_meta_table['Vrrp.Ipv6.VirtualRouters.VirtualRouter']['meta_info']
_meta_table['Vrrp.Ipv6.VirtualRouters.VirtualRouter.Ipv6ConfiguredDownAddress']['meta_info'].parent =_meta_table['Vrrp.Ipv6.VirtualRouters.VirtualRouter']['meta_info']
_meta_table['Vrrp.Ipv6.VirtualRouters.VirtualRouter.StateChangeHistory']['meta_info'].parent =_meta_table['Vrrp.Ipv6.VirtualRouters.VirtualRouter']['meta_info']
_meta_table['Vrrp.Ipv6.VirtualRouters.VirtualRouter']['meta_info'].parent =_meta_table['Vrrp.Ipv6.VirtualRouters']['meta_info']
_meta_table['Vrrp.Ipv6.Interfaces.Interface']['meta_info'].parent =_meta_table['Vrrp.Ipv6.Interfaces']['meta_info']
_meta_table['Vrrp.Ipv6.TrackItems']['meta_info'].parent =_meta_table['Vrrp.Ipv6']['meta_info']
_meta_table['Vrrp.Ipv6.VirtualRouters']['meta_info'].parent =_meta_table['Vrrp.Ipv6']['meta_info']
_meta_table['Vrrp.Ipv6.Interfaces']['meta_info'].parent =_meta_table['Vrrp.Ipv6']['meta_info']
_meta_table['Vrrp.Ipv4.Interfaces.Interface']['meta_info'].parent =_meta_table['Vrrp.Ipv4.Interfaces']['meta_info']
_meta_table['Vrrp.Ipv4.TrackItems.TrackItem']['meta_info'].parent =_meta_table['Vrrp.Ipv4.TrackItems']['meta_info']
_meta_table['Vrrp.Ipv4.VirtualRouters.VirtualRouter.StateChangeHistory.Time']['meta_info'].parent =_meta_table['Vrrp.Ipv4.VirtualRouters.VirtualRouter.StateChangeHistory']['meta_info']
_meta_table['Vrrp.Ipv4.VirtualRouters.VirtualRouter.ResignSentTime']['meta_info'].parent =_meta_table['Vrrp.Ipv4.VirtualRouters.VirtualRouter']['meta_info']
_meta_table['Vrrp.Ipv4.VirtualRouters.VirtualRouter.ResignReceivedTime']['meta_info'].parent =_meta_table['Vrrp.Ipv4.VirtualRouters.VirtualRouter']['meta_info']
_meta_table['Vrrp.Ipv4.VirtualRouters.VirtualRouter.Ipv6OperationalAddress']['meta_info'].parent =_meta_table['Vrrp.Ipv4.VirtualRouters.VirtualRouter']['meta_info']
_meta_table['Vrrp.Ipv4.VirtualRouters.VirtualRouter.Ipv6ConfiguredDownAddress']['meta_info'].parent =_meta_table['Vrrp.Ipv4.VirtualRouters.VirtualRouter']['meta_info']
_meta_table['Vrrp.Ipv4.VirtualRouters.VirtualRouter.StateChangeHistory']['meta_info'].parent =_meta_table['Vrrp.Ipv4.VirtualRouters.VirtualRouter']['meta_info']
_meta_table['Vrrp.Ipv4.VirtualRouters.VirtualRouter']['meta_info'].parent =_meta_table['Vrrp.Ipv4.VirtualRouters']['meta_info']
_meta_table['Vrrp.Ipv4.Interfaces']['meta_info'].parent =_meta_table['Vrrp.Ipv4']['meta_info']
_meta_table['Vrrp.Ipv4.TrackItems']['meta_info'].parent =_meta_table['Vrrp.Ipv4']['meta_info']
_meta_table['Vrrp.Ipv4.VirtualRouters']['meta_info'].parent =_meta_table['Vrrp.Ipv4']['meta_info']
_meta_table['Vrrp.MgoSessions.MgoSession.Slave']['meta_info'].parent =_meta_table['Vrrp.MgoSessions.MgoSession']['meta_info']
_meta_table['Vrrp.MgoSessions.MgoSession']['meta_info'].parent =_meta_table['Vrrp.MgoSessions']['meta_info']
_meta_table['Vrrp.Summary']['meta_info'].parent =_meta_table['Vrrp']['meta_info']
_meta_table['Vrrp.Ipv6']['meta_info'].parent =_meta_table['Vrrp']['meta_info']
_meta_table['Vrrp.Ipv4']['meta_info'].parent =_meta_table['Vrrp']['meta_info']
_meta_table['Vrrp.MgoSessions']['meta_info'].parent =_meta_table['Vrrp']['meta_info']
