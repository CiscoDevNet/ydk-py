


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns

_meta_table = {
    'Ipv4DhcpdFmtEnum' : _MetaInfoEnum('Ipv4DhcpdFmtEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg',
        {
            'no-format':'no_format',
            'format':'format',
        }, 'Cisco-IOS-XR-ipv4-dhcpd-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-cfg']),
    'Ipv4DhcpdFmtSpecifierEnum' : _MetaInfoEnum('Ipv4DhcpdFmtSpecifierEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg',
        {
            'physical-chassis':'physical_chassis',
            'physical-slot':'physical_slot',
            'physical-sub-slot':'physical_sub_slot',
            'physical-port':'physical_port',
            'physical-sub-port':'physical_sub_port',
            'inner-vlan-id':'inner_vlan_id',
            'outer-vlan-id':'outer_vlan_id',
            'l2-interface':'l2_interface',
        }, 'Cisco-IOS-XR-ipv4-dhcpd-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-cfg']),
    'Ipv4DhcpdRelayInfoOptionPolicyEnum' : _MetaInfoEnum('Ipv4DhcpdRelayInfoOptionPolicyEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg',
        {
            'replace':'replace',
            'keep':'keep',
            'drop':'drop',
            'encapsulate':'encapsulate',
        }, 'Cisco-IOS-XR-ipv4-dhcpd-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-cfg']),
    'Ipv4DhcpdBroadcastFlagPolicyEnum' : _MetaInfoEnum('Ipv4DhcpdBroadcastFlagPolicyEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg',
        {
            'ignore':'ignore',
            'check':'check',
            'unicast-always':'unicast_always',
        }, 'Cisco-IOS-XR-ipv4-dhcpd-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-cfg']),
    'Ipv4DhcpdModeEnum' : _MetaInfoEnum('Ipv4DhcpdModeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg',
        {
            'base':'base',
            'relay':'relay',
            'snoop':'snoop',
            'server':'server',
            'proxy':'proxy',
            'base2':'base2',
        }, 'Cisco-IOS-XR-ipv4-dhcpd-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-cfg']),
    'Ipv4DhcpdGiaddrPolicyEnum' : _MetaInfoEnum('Ipv4DhcpdGiaddrPolicyEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg',
        {
            'keep':'keep',
            'replace':'replace',
            'drop':'drop',
        }, 'Cisco-IOS-XR-ipv4-dhcpd-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-cfg']),
    'Ipv4DhcpdRelayInfoOptionvpnModeEnum' : _MetaInfoEnum('Ipv4DhcpdRelayInfoOptionvpnModeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg',
        {
            'rfc':'rfc',
            'cisco':'cisco',
        }, 'Cisco-IOS-XR-ipv4-dhcpd-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-cfg']),
    'Ipv4Dhcpd.Vrfs.Vrf.Profile' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Vrfs.Vrf.Profile',
            False, 
            [
            _MetaInfoClassMember('mode', REFERENCE_ENUM_CLASS, 'Ipv4DhcpdModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4DhcpdModeEnum', 
                [], [], 
                '''                Dhcp mode
                ''',
                'mode',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('vrf-profile-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Profile name
                ''',
                'vrf_profile_name',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-cfg',
            'profile',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg'
        ),
    },
    'Ipv4Dhcpd.Vrfs.Vrf' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Vrfs.Vrf',
            False, 
            [
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                VRF Name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', True),
            _MetaInfoClassMember('profile', REFERENCE_CLASS, 'Profile' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4Dhcpd.Vrfs.Vrf.Profile', 
                [], [], 
                '''                Profile name and mode
                ''',
                'profile',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-cfg',
            'vrf',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg'
        ),
    },
    'Ipv4Dhcpd.Vrfs' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Vrfs',
            False, 
            [
            _MetaInfoClassMember('vrf', REFERENCE_LIST, 'Vrf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4Dhcpd.Vrfs.Vrf', 
                [], [], 
                '''                VRF table
                ''',
                'vrf',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-cfg',
            'vrfs',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg'
        ),
    },
    'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server',
            False, 
            [
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-cfg',
            'server',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg'
        ),
    },
    'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.GiAddrPolicy' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.GiAddrPolicy',
            False, 
            [
            _MetaInfoClassMember('policy', REFERENCE_ENUM_CLASS, 'Ipv4DhcpdGiaddrPolicyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4DhcpdGiaddrPolicyEnum', 
                [], [], 
                '''                GIADDR policy
                ''',
                'policy',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-cfg',
            'gi-addr-policy',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg'
        ),
    },
    'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.Vrfs.Vrf.HelperAddresses.HelperAddress' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.Vrfs.Vrf.HelperAddresses.HelperAddress',
            False, 
            [
            _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPV4 Address
                ''',
                'ip_address',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', True),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable helper - deprecated
                ''',
                'enable',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('gateway-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                GatewayAddress
                ''',
                'gateway_address',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-cfg',
            'helper-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg'
        ),
    },
    'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.Vrfs.Vrf.HelperAddresses' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.Vrfs.Vrf.HelperAddresses',
            False, 
            [
            _MetaInfoClassMember('helper-address', REFERENCE_LIST, 'HelperAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.Vrfs.Vrf.HelperAddresses.HelperAddress', 
                [], [], 
                '''                Helper Address
                ''',
                'helper_address',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-cfg',
            'helper-addresses',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg'
        ),
    },
    'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.Vrfs.Vrf' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.Vrfs.Vrf',
            False, 
            [
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                VRF Name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', True),
            _MetaInfoClassMember('helper-addresses', REFERENCE_CLASS, 'HelperAddresses' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.Vrfs.Vrf.HelperAddresses', 
                [], [], 
                '''                Helper Addresses
                ''',
                'helper_addresses',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-cfg',
            'vrf',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg'
        ),
    },
    'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.Vrfs' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.Vrfs',
            False, 
            [
            _MetaInfoClassMember('vrf', REFERENCE_LIST, 'Vrf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.Vrfs.Vrf', 
                [], [], 
                '''                VRF Name
                ''',
                'vrf',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-cfg',
            'vrfs',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg'
        ),
    },
    'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.RelayInformationOption' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.RelayInformationOption',
            False, 
            [
            _MetaInfoClassMember('allow-untrusted', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Forward untrusted packets
                ''',
                'allow_untrusted',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('check', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Check Relay Agent Information Option in
                server reply
                ''',
                'check',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('insert', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Insert Relay Agent Information circuit ID
                and remote ID suboptions in client
                requests
                ''',
                'insert',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('policy', REFERENCE_ENUM_CLASS, 'Ipv4DhcpdRelayInfoOptionPolicyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4DhcpdRelayInfoOptionPolicyEnum', 
                [], [], 
                '''                Relay information option policy
                ''',
                'policy',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('subscriber-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Subscriber ID
                ''',
                'subscriber_id',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('vpn', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Insert VPN options
                ''',
                'vpn',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('vpn-mode', REFERENCE_ENUM_CLASS, 'Ipv4DhcpdRelayInfoOptionvpnModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4DhcpdRelayInfoOptionvpnModeEnum', 
                [], [], 
                '''                VPN Mode
                ''',
                'vpn_mode',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-cfg',
            'relay-information-option',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg'
        ),
    },
    'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.BroadcastPolicy' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.BroadcastPolicy',
            False, 
            [
            _MetaInfoClassMember('policy', REFERENCE_ENUM_CLASS, 'Ipv4DhcpdBroadcastFlagPolicyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4DhcpdBroadcastFlagPolicyEnum', 
                [], [], 
                '''                Broadcast flag policy
                ''',
                'policy',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-cfg',
            'broadcast-policy',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg'
        ),
    },
    'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay',
            False, 
            [
            _MetaInfoClassMember('broadcast-policy', REFERENCE_CLASS, 'BroadcastPolicy' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.BroadcastPolicy', 
                [], [], 
                '''                Broadcast Flag policy
                ''',
                'broadcast_policy',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('gi-addr-policy', REFERENCE_CLASS, 'GiAddrPolicy' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.GiAddrPolicy', 
                [], [], 
                '''                GIADDR policy
                ''',
                'gi_addr_policy',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('relay-information-option', REFERENCE_CLASS, 'RelayInformationOption' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.RelayInformationOption', 
                [], [], 
                '''                Relay agent information option
                ''',
                'relay_information_option',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('vrfs', REFERENCE_CLASS, 'Vrfs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.Vrfs', 
                [], [], 
                '''                VRF Helper Addresses
                ''',
                'vrfs',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-cfg',
            'relay',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg'
        ),
    },
    'Ipv4Dhcpd.Profiles.Profile.Modes.Mode' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Profiles.Profile.Modes.Mode',
            False, 
            [
            _MetaInfoClassMember('mode', REFERENCE_ENUM_CLASS, 'Ipv4DhcpdModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4DhcpdModeEnum', 
                [], [], 
                '''                DHCP IPV4 Profile mode
                ''',
                'mode',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', True),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable the DHCP IPV4 Profile mode
                ''',
                'enable',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('relay', REFERENCE_CLASS, 'Relay' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay', 
                [], [], 
                '''                DHCP Relay profile
                ''',
                'relay',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('server', REFERENCE_CLASS, 'Server' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server', 
                [], [], 
                '''                DHCP Server profile
                ''',
                'server',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-cfg',
            'mode',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg'
        ),
    },
    'Ipv4Dhcpd.Profiles.Profile.Modes' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Profiles.Profile.Modes',
            False, 
            [
            _MetaInfoClassMember('mode', REFERENCE_LIST, 'Mode' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4Dhcpd.Profiles.Profile.Modes.Mode', 
                [], [], 
                '''                DHCP IPV4 Profile mode
                ''',
                'mode',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-cfg',
            'modes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg'
        ),
    },
    'Ipv4Dhcpd.Profiles.Profile' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Profiles.Profile',
            False, 
            [
            _MetaInfoClassMember('profile-name', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Profile Name
                ''',
                'profile_name',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', True),
            _MetaInfoClassMember('modes', REFERENCE_CLASS, 'Modes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4Dhcpd.Profiles.Profile.Modes', 
                [], [], 
                '''                DHCP IPV4 Profile modes
                ''',
                'modes',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-cfg',
            'profile',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg'
        ),
    },
    'Ipv4Dhcpd.Profiles' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Profiles',
            False, 
            [
            _MetaInfoClassMember('profile', REFERENCE_LIST, 'Profile' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4Dhcpd.Profiles.Profile', 
                [], [], 
                '''                DHCP IPV4 Profile
                ''',
                'profile',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-cfg',
            'profiles',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg'
        ),
    },
    'Ipv4Dhcpd.Database' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Database',
            False, 
            [
            _MetaInfoClassMember('full-write-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '1440')], [], 
                '''                Full file write interval (default 10 minutes)
                ''',
                'full_write_interval',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('incremental-write-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '1440')], [], 
                '''                Incremental file write interval (default 1
                minutes)
                ''',
                'incremental_write_interval',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('proxy', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable DHCP proxy binding database storage to
                file system
                ''',
                'proxy',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('server', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable DHCP server binding database storage to
                file system
                ''',
                'server',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('snoop', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable DHCP snoop binding database storage to
                file system
                ''',
                'snoop',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-cfg',
            'database',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg'
        ),
    },
    'Ipv4Dhcpd.Interfaces.Interface.ProxyInterface.DhcpCircuitId' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Interfaces.Interface.ProxyInterface.DhcpCircuitId',
            False, 
            [
            _MetaInfoClassMember('argument1', REFERENCE_ENUM_CLASS, 'Ipv4DhcpdFmtSpecifierEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4DhcpdFmtSpecifierEnum', 
                [], [], 
                '''                Argument
                ''',
                'argument1',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('argument10', REFERENCE_ENUM_CLASS, 'Ipv4DhcpdFmtSpecifierEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4DhcpdFmtSpecifierEnum', 
                [], [], 
                '''                Argument
                ''',
                'argument10',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('argument11', REFERENCE_ENUM_CLASS, 'Ipv4DhcpdFmtSpecifierEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4DhcpdFmtSpecifierEnum', 
                [], [], 
                '''                Argument
                ''',
                'argument11',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('argument12', REFERENCE_ENUM_CLASS, 'Ipv4DhcpdFmtSpecifierEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4DhcpdFmtSpecifierEnum', 
                [], [], 
                '''                Argument
                ''',
                'argument12',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('argument13', REFERENCE_ENUM_CLASS, 'Ipv4DhcpdFmtSpecifierEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4DhcpdFmtSpecifierEnum', 
                [], [], 
                '''                Argument
                ''',
                'argument13',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('argument14', REFERENCE_ENUM_CLASS, 'Ipv4DhcpdFmtSpecifierEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4DhcpdFmtSpecifierEnum', 
                [], [], 
                '''                Argument
                ''',
                'argument14',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('argument15', REFERENCE_ENUM_CLASS, 'Ipv4DhcpdFmtSpecifierEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4DhcpdFmtSpecifierEnum', 
                [], [], 
                '''                Argument
                ''',
                'argument15',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('argument16', REFERENCE_ENUM_CLASS, 'Ipv4DhcpdFmtSpecifierEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4DhcpdFmtSpecifierEnum', 
                [], [], 
                '''                Argument
                ''',
                'argument16',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('argument2', REFERENCE_ENUM_CLASS, 'Ipv4DhcpdFmtSpecifierEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4DhcpdFmtSpecifierEnum', 
                [], [], 
                '''                Argument
                ''',
                'argument2',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('argument3', REFERENCE_ENUM_CLASS, 'Ipv4DhcpdFmtSpecifierEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4DhcpdFmtSpecifierEnum', 
                [], [], 
                '''                Argument
                ''',
                'argument3',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('argument4', REFERENCE_ENUM_CLASS, 'Ipv4DhcpdFmtSpecifierEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4DhcpdFmtSpecifierEnum', 
                [], [], 
                '''                Argument
                ''',
                'argument4',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('argument5', REFERENCE_ENUM_CLASS, 'Ipv4DhcpdFmtSpecifierEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4DhcpdFmtSpecifierEnum', 
                [], [], 
                '''                Argument
                ''',
                'argument5',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('argument6', REFERENCE_ENUM_CLASS, 'Ipv4DhcpdFmtSpecifierEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4DhcpdFmtSpecifierEnum', 
                [], [], 
                '''                Argument
                ''',
                'argument6',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('argument7', REFERENCE_ENUM_CLASS, 'Ipv4DhcpdFmtSpecifierEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4DhcpdFmtSpecifierEnum', 
                [], [], 
                '''                Argument
                ''',
                'argument7',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('argument8', REFERENCE_ENUM_CLASS, 'Ipv4DhcpdFmtSpecifierEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4DhcpdFmtSpecifierEnum', 
                [], [], 
                '''                Argument
                ''',
                'argument8',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('argument9', REFERENCE_ENUM_CLASS, 'Ipv4DhcpdFmtSpecifierEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4DhcpdFmtSpecifierEnum', 
                [], [], 
                '''                Argument
                ''',
                'argument9',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('circuit-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                DHCP IPv4 circuit ID value
                ''',
                'circuit_id',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('format', REFERENCE_ENUM_CLASS, 'Ipv4DhcpdFmtEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4DhcpdFmtEnum', 
                [], [], 
                '''                Format String
                ''',
                'format',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-cfg',
            'dhcp-circuit-id',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg'
        ),
    },
    'Ipv4Dhcpd.Interfaces.Interface.ProxyInterface' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Interfaces.Interface.ProxyInterface',
            False, 
            [
            _MetaInfoClassMember('dhcp-circuit-id', REFERENCE_CLASS, 'DhcpCircuitId' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4Dhcpd.Interfaces.Interface.ProxyInterface.DhcpCircuitId', 
                [], [], 
                '''                Circuit ID value
                ''',
                'dhcp_circuit_id',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('profile', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Interface profile name
                ''',
                'profile',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-cfg',
            'proxy-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg'
        ),
    },
    'Ipv4Dhcpd.Interfaces.Interface.BaseInterface' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Interfaces.Interface.BaseInterface',
            False, 
            [
            _MetaInfoClassMember('profile', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Interface profile name
                ''',
                'profile',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-cfg',
            'base-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg'
        ),
    },
    'Ipv4Dhcpd.Interfaces.Interface.RelayInterface.RelayDhcpCircuitId' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Interfaces.Interface.RelayInterface.RelayDhcpCircuitId',
            False, 
            [
            _MetaInfoClassMember('argument1', REFERENCE_ENUM_CLASS, 'Ipv4DhcpdFmtSpecifierEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4DhcpdFmtSpecifierEnum', 
                [], [], 
                '''                Argument
                ''',
                'argument1',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('argument10', REFERENCE_ENUM_CLASS, 'Ipv4DhcpdFmtSpecifierEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4DhcpdFmtSpecifierEnum', 
                [], [], 
                '''                Argument
                ''',
                'argument10',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('argument11', REFERENCE_ENUM_CLASS, 'Ipv4DhcpdFmtSpecifierEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4DhcpdFmtSpecifierEnum', 
                [], [], 
                '''                Argument
                ''',
                'argument11',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('argument12', REFERENCE_ENUM_CLASS, 'Ipv4DhcpdFmtSpecifierEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4DhcpdFmtSpecifierEnum', 
                [], [], 
                '''                Argument
                ''',
                'argument12',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('argument13', REFERENCE_ENUM_CLASS, 'Ipv4DhcpdFmtSpecifierEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4DhcpdFmtSpecifierEnum', 
                [], [], 
                '''                Argument
                ''',
                'argument13',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('argument14', REFERENCE_ENUM_CLASS, 'Ipv4DhcpdFmtSpecifierEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4DhcpdFmtSpecifierEnum', 
                [], [], 
                '''                Argument
                ''',
                'argument14',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('argument15', REFERENCE_ENUM_CLASS, 'Ipv4DhcpdFmtSpecifierEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4DhcpdFmtSpecifierEnum', 
                [], [], 
                '''                Argument
                ''',
                'argument15',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('argument16', REFERENCE_ENUM_CLASS, 'Ipv4DhcpdFmtSpecifierEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4DhcpdFmtSpecifierEnum', 
                [], [], 
                '''                Argument
                ''',
                'argument16',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('argument2', REFERENCE_ENUM_CLASS, 'Ipv4DhcpdFmtSpecifierEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4DhcpdFmtSpecifierEnum', 
                [], [], 
                '''                Argument
                ''',
                'argument2',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('argument3', REFERENCE_ENUM_CLASS, 'Ipv4DhcpdFmtSpecifierEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4DhcpdFmtSpecifierEnum', 
                [], [], 
                '''                Argument
                ''',
                'argument3',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('argument4', REFERENCE_ENUM_CLASS, 'Ipv4DhcpdFmtSpecifierEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4DhcpdFmtSpecifierEnum', 
                [], [], 
                '''                Argument
                ''',
                'argument4',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('argument5', REFERENCE_ENUM_CLASS, 'Ipv4DhcpdFmtSpecifierEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4DhcpdFmtSpecifierEnum', 
                [], [], 
                '''                Argument
                ''',
                'argument5',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('argument6', REFERENCE_ENUM_CLASS, 'Ipv4DhcpdFmtSpecifierEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4DhcpdFmtSpecifierEnum', 
                [], [], 
                '''                Argument
                ''',
                'argument6',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('argument7', REFERENCE_ENUM_CLASS, 'Ipv4DhcpdFmtSpecifierEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4DhcpdFmtSpecifierEnum', 
                [], [], 
                '''                Argument
                ''',
                'argument7',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('argument8', REFERENCE_ENUM_CLASS, 'Ipv4DhcpdFmtSpecifierEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4DhcpdFmtSpecifierEnum', 
                [], [], 
                '''                Argument
                ''',
                'argument8',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('argument9', REFERENCE_ENUM_CLASS, 'Ipv4DhcpdFmtSpecifierEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4DhcpdFmtSpecifierEnum', 
                [], [], 
                '''                Argument
                ''',
                'argument9',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('circuit-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                DHCP IPv4 circuit ID value
                ''',
                'circuit_id',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('format', REFERENCE_ENUM_CLASS, 'Ipv4DhcpdFmtEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4DhcpdFmtEnum', 
                [], [], 
                '''                Format String
                ''',
                'format',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-cfg',
            'relay-dhcp-circuit-id',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg'
        ),
    },
    'Ipv4Dhcpd.Interfaces.Interface.RelayInterface' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Interfaces.Interface.RelayInterface',
            False, 
            [
            _MetaInfoClassMember('relay-dhcp-circuit-id', REFERENCE_CLASS, 'RelayDhcpCircuitId' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4Dhcpd.Interfaces.Interface.RelayInterface.RelayDhcpCircuitId', 
                [], [], 
                '''                Circuit ID value
                ''',
                'relay_dhcp_circuit_id',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-cfg',
            'relay-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg'
        ),
    },
    'Ipv4Dhcpd.Interfaces.Interface.Profile' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Interfaces.Interface.Profile',
            False, 
            [
            _MetaInfoClassMember('mode', REFERENCE_ENUM_CLASS, 'Ipv4DhcpdModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4DhcpdModeEnum', 
                [], [], 
                '''                DHCP mode
                ''',
                'mode',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('profile-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Profile name
                ''',
                'profile_name',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-cfg',
            'profile',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg'
        ),
    },
    'Ipv4Dhcpd.Interfaces.Interface.ServerInterface' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Interfaces.Interface.ServerInterface',
            False, 
            [
            _MetaInfoClassMember('profile', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Interface profile name
                ''',
                'profile',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-cfg',
            'server-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg'
        ),
    },
    'Ipv4Dhcpd.Interfaces.Interface.SnoopInterface.SnoopCircuitId' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Interfaces.Interface.SnoopInterface.SnoopCircuitId',
            False, 
            [
            _MetaInfoClassMember('circuit-id-value', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Enter circuit-id value
                ''',
                'circuit_id_value',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('format-type', ATTRIBUTE, 'int' , None, None, 
                [('1', '2')], [], 
                '''                Format type, 1. Hex 2. ASCII
                ''',
                'format_type',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-cfg',
            'snoop-circuit-id',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg'
        ),
    },
    'Ipv4Dhcpd.Interfaces.Interface.SnoopInterface' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Interfaces.Interface.SnoopInterface',
            False, 
            [
            _MetaInfoClassMember('snoop-circuit-id', REFERENCE_CLASS, 'SnoopCircuitId' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4Dhcpd.Interfaces.Interface.SnoopInterface.SnoopCircuitId', 
                [], [], 
                '''                Configure circuit ID for snoop 1. Hex 2.
                ASCII
                ''',
                'snoop_circuit_id',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-cfg',
            'snoop-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg'
        ),
    },
    'Ipv4Dhcpd.Interfaces.Interface' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Interfaces.Interface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', True),
            _MetaInfoClassMember('base-interface', REFERENCE_CLASS, 'BaseInterface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4Dhcpd.Interfaces.Interface.BaseInterface', 
                [], [], 
                '''                DHCP IPv4 Base profile information
                ''',
                'base_interface',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('none', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                DHCP IPV4 disabled
                ''',
                'none',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('profile', REFERENCE_CLASS, 'Profile' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4Dhcpd.Interfaces.Interface.Profile', 
                [], [], 
                '''                Profile name and mode
                ''',
                'profile',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('proxy-interface', REFERENCE_CLASS, 'ProxyInterface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4Dhcpd.Interfaces.Interface.ProxyInterface', 
                [], [], 
                '''                DHCP IPv4 proxy information
                ''',
                'proxy_interface',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('relay-interface', REFERENCE_CLASS, 'RelayInterface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4Dhcpd.Interfaces.Interface.RelayInterface', 
                [], [], 
                '''                DHCP IPv4 relay information
                ''',
                'relay_interface',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('server-interface', REFERENCE_CLASS, 'ServerInterface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4Dhcpd.Interfaces.Interface.ServerInterface', 
                [], [], 
                '''                DHCP IPv4 Server information
                ''',
                'server_interface',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('snoop-interface', REFERENCE_CLASS, 'SnoopInterface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4Dhcpd.Interfaces.Interface.SnoopInterface', 
                [], [], 
                '''                DHCP IPv4 snoop information
                ''',
                'snoop_interface',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-cfg',
            'interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg'
        ),
    },
    'Ipv4Dhcpd.Interfaces' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Interfaces',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4Dhcpd.Interfaces.Interface', 
                [], [], 
                '''                DHCP IPV4 Interface
                ''',
                'interface',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-cfg',
            'interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg'
        ),
    },
    'Ipv4Dhcpd.DuplicateMacAllowed' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.DuplicateMacAllowed',
            False, 
            [
            _MetaInfoClassMember('duplicate-mac', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Duplicate mac is allowed
                ''',
                'duplicate_mac',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('exclude-vlan', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Exclude vlan
                ''',
                'exclude_vlan',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-cfg',
            'duplicate-mac-allowed',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg'
        ),
    },
    'Ipv4Dhcpd.RateLimit' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.RateLimit',
            False, 
            [
            _MetaInfoClassMember('num-discover', ATTRIBUTE, 'int' , None, None, 
                [('0', '1000')], [], 
                '''                Max DISCOVER packets per rate-limiter period
                (default 100)
                ''',
                'num_discover',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('num-period', ATTRIBUTE, 'int' , None, None, 
                [('1', '1000')], [], 
                '''                Rate limiter period in msec (default: 200 msec)
                ''',
                'num_period',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-cfg',
            'rate-limit',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg'
        ),
    },
    'Ipv4Dhcpd' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd',
            False, 
            [
            _MetaInfoClassMember('allow-client-id-change', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                For BNG session, allow client id change for a
                client MAC
                ''',
                'allow_client_id_change',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('database', REFERENCE_CLASS, 'Database' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4Dhcpd.Database', 
                [], [], 
                '''                Enable DHCP binding database storage to file
                system
                ''',
                'database',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('duplicate-mac-allowed', REFERENCE_CLASS, 'DuplicateMacAllowed' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4Dhcpd.DuplicateMacAllowed', 
                [], [], 
                '''                Allow Duplicate MAC Address
                ''',
                'duplicate_mac_allowed',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                DHCP IPV4 configuration
                ''',
                'enable',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4Dhcpd.Interfaces', 
                [], [], 
                '''                DHCP IPV4 Interface Table
                ''',
                'interfaces',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('profiles', REFERENCE_CLASS, 'Profiles' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4Dhcpd.Profiles', 
                [], [], 
                '''                DHCP IPV4 Profile Table
                ''',
                'profiles',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('rate-limit', REFERENCE_CLASS, 'RateLimit' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4Dhcpd.RateLimit', 
                [], [], 
                '''                Rate limit ingress packets
                ''',
                'rate_limit',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('vrfs', REFERENCE_CLASS, 'Vrfs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4Dhcpd.Vrfs', 
                [], [], 
                '''                VRF Table
                ''',
                'vrfs',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-cfg',
            'ipv4-dhcpd',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg'
        ),
    },
}
_meta_table['Ipv4Dhcpd.Vrfs.Vrf.Profile']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Vrfs.Vrf']['meta_info']
_meta_table['Ipv4Dhcpd.Vrfs.Vrf']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Vrfs']['meta_info']
_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.Vrfs.Vrf.HelperAddresses.HelperAddress']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.Vrfs.Vrf.HelperAddresses']['meta_info']
_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.Vrfs.Vrf.HelperAddresses']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.Vrfs.Vrf']['meta_info']
_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.Vrfs.Vrf']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.Vrfs']['meta_info']
_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.GiAddrPolicy']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay']['meta_info']
_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.Vrfs']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay']['meta_info']
_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.RelayInformationOption']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay']['meta_info']
_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.BroadcastPolicy']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay']['meta_info']
_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode']['meta_info']
_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode']['meta_info']
_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes']['meta_info']
_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Profiles.Profile']['meta_info']
_meta_table['Ipv4Dhcpd.Profiles.Profile']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Profiles']['meta_info']
_meta_table['Ipv4Dhcpd.Interfaces.Interface.ProxyInterface.DhcpCircuitId']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Interfaces.Interface.ProxyInterface']['meta_info']
_meta_table['Ipv4Dhcpd.Interfaces.Interface.RelayInterface.RelayDhcpCircuitId']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Interfaces.Interface.RelayInterface']['meta_info']
_meta_table['Ipv4Dhcpd.Interfaces.Interface.SnoopInterface.SnoopCircuitId']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Interfaces.Interface.SnoopInterface']['meta_info']
_meta_table['Ipv4Dhcpd.Interfaces.Interface.ProxyInterface']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Interfaces.Interface']['meta_info']
_meta_table['Ipv4Dhcpd.Interfaces.Interface.BaseInterface']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Interfaces.Interface']['meta_info']
_meta_table['Ipv4Dhcpd.Interfaces.Interface.RelayInterface']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Interfaces.Interface']['meta_info']
_meta_table['Ipv4Dhcpd.Interfaces.Interface.Profile']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Interfaces.Interface']['meta_info']
_meta_table['Ipv4Dhcpd.Interfaces.Interface.ServerInterface']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Interfaces.Interface']['meta_info']
_meta_table['Ipv4Dhcpd.Interfaces.Interface.SnoopInterface']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Interfaces.Interface']['meta_info']
_meta_table['Ipv4Dhcpd.Interfaces.Interface']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Interfaces']['meta_info']
_meta_table['Ipv4Dhcpd.Vrfs']['meta_info'].parent =_meta_table['Ipv4Dhcpd']['meta_info']
_meta_table['Ipv4Dhcpd.Profiles']['meta_info'].parent =_meta_table['Ipv4Dhcpd']['meta_info']
_meta_table['Ipv4Dhcpd.Database']['meta_info'].parent =_meta_table['Ipv4Dhcpd']['meta_info']
_meta_table['Ipv4Dhcpd.Interfaces']['meta_info'].parent =_meta_table['Ipv4Dhcpd']['meta_info']
_meta_table['Ipv4Dhcpd.DuplicateMacAllowed']['meta_info'].parent =_meta_table['Ipv4Dhcpd']['meta_info']
_meta_table['Ipv4Dhcpd.RateLimit']['meta_info'].parent =_meta_table['Ipv4Dhcpd']['meta_info']
