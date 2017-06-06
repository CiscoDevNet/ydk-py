


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'Dhcpv4MatchOptionEnum' : _MetaInfoEnum('Dhcpv4MatchOptionEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg',
        {
            '60/60':'Y_60__FWD_SLASH__60',
            '77/77':'Y_77__FWD_SLASH__77',
            '124/124':'Y_124__FWD_SLASH__124',
            '125/125':'Y_125__FWD_SLASH__125',
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
    'Ipv4DhcpdBroadcastFlagPolicyEnum' : _MetaInfoEnum('Ipv4DhcpdBroadcastFlagPolicyEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg',
        {
            'ignore':'ignore',
            'check':'check',
            'unicast-always':'unicast_always',
        }, 'Cisco-IOS-XR-ipv4-dhcpd-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-cfg']),
    'Ipv4DhcpdRelayInfoOptionAuthenticateEnum' : _MetaInfoEnum('Ipv4DhcpdRelayInfoOptionAuthenticateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg',
        {
            'received':'received',
            'inserted':'inserted',
        }, 'Cisco-IOS-XR-ipv4-dhcpd-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-cfg']),
    'MatchactionEnum' : _MetaInfoEnum('MatchactionEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg',
        {
            'allow':'allow',
            'drop':'drop',
        }, 'Cisco-IOS-XR-ipv4-dhcpd-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-cfg']),
    'Dhcpv4LimitLease1Enum' : _MetaInfoEnum('Dhcpv4LimitLease1Enum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg',
        {
            'interface':'interface',
            'circuit-id':'circuit_id',
            'remote-id':'remote_id',
            'circuit-id-remote-id':'circuit_id_remote_id',
        }, 'Cisco-IOS-XR-ipv4-dhcpd-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-cfg']),
    'Ipv4DhcpdLayerEnum' : _MetaInfoEnum('Ipv4DhcpdLayerEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg',
        {
            'layer2':'layer2',
            'layer3':'layer3',
        }, 'Cisco-IOS-XR-ipv4-dhcpd-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-cfg']),
    'PolicyEnum' : _MetaInfoEnum('PolicyEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg',
        {
            'ignore':'ignore',
            'check':'check',
            'unicastalways':'unicastalways',
        }, 'Cisco-IOS-XR-ipv4-dhcpd-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-cfg']),
    'BaseActionEnum' : _MetaInfoEnum('BaseActionEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg',
        {
            'allow':'allow',
            'drop':'drop',
        }, 'Cisco-IOS-XR-ipv4-dhcpd-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-cfg']),
    'MatchoptionEnum' : _MetaInfoEnum('MatchoptionEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg',
        {
            'circuitid':'circuitid',
            'remoteid':'remoteid',
            '60':'Y_60',
            '77':'Y_77',
            '124':'Y_124',
            '125':'Y_125',
        }, 'Cisco-IOS-XR-ipv4-dhcpd-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-cfg']),
    'Ipv4DhcpdRelayInfoOptionPolicyEnum' : _MetaInfoEnum('Ipv4DhcpdRelayInfoOptionPolicyEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg',
        {
            'replace':'replace',
            'keep':'keep',
            'drop':'drop',
            'encapsulate':'encapsulate',
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
    'ProxyActionEnum' : _MetaInfoEnum('ProxyActionEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg',
        {
            'allow':'allow',
            'drop':'drop',
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
    'LeaseLimitValueEnum' : _MetaInfoEnum('LeaseLimitValueEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg',
        {
            'per-interface':'per_interface',
            'per-circuit-id':'per_circuit_id',
            'per-remote-id':'per_remote_id',
        }, 'Cisco-IOS-XR-ipv4-dhcpd-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-cfg']),
    'Ipv4DhcpdFmtEnum' : _MetaInfoEnum('Ipv4DhcpdFmtEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg',
        {
            'no-format':'no_format',
            'format':'format',
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
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
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
    'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Snoop.RelayInformationOption.RemoteId' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Snoop.RelayInformationOption.RemoteId',
            False, 
            [
            _MetaInfoClassMember('format-type', ATTRIBUTE, 'int' , None, None, 
                [('1', '2')], [], 
                '''                Format type, 1. Hex 2. ASCII
                ''',
                'format_type',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('remote-id-value', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Enter remote-id value
                ''',
                'remote_id_value',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-cfg',
            'remote-id',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg'
        ),
    },
    'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Snoop.RelayInformationOption' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Snoop.RelayInformationOption',
            False, 
            [
            _MetaInfoClassMember('allow-untrusted', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Forward untrusted packets
                ''',
                'allow_untrusted',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('insert', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Insert Relay Agent Information circuit ID
                and remote ID suboptions in client request
                ''',
                'insert',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('policy', REFERENCE_ENUM_CLASS, 'Ipv4DhcpdRelayInfoOptionPolicyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4DhcpdRelayInfoOptionPolicyEnum', 
                [], [], 
                '''                Relay information option policy
                ''',
                'policy',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('remote-id', REFERENCE_CLASS, 'RemoteId' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Snoop.RelayInformationOption.RemoteId', 
                [], [], 
                '''                Enter remote-id value
                ''',
                'remote_id',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-cfg',
            'relay-information-option',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg'
        ),
    },
    'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Snoop' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Snoop',
            False, 
            [
            _MetaInfoClassMember('relay-information-option', REFERENCE_CLASS, 'RelayInformationOption' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Snoop.RelayInformationOption', 
                [], [], 
                '''                DHCP Snoop profile
                ''',
                'relay_information_option',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('trusted', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Trusted sources
                ''',
                'trusted',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-cfg',
            'snoop',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg'
        ),
    },
    'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.DefaultProfile' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.DefaultProfile',
            False, 
            [
            _MetaInfoClassMember('profile-mode', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                none
                ''',
                'profile_mode',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('profile-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Profile name
                ''',
                'profile_name',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-cfg',
            'default-profile',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg'
        ),
    },
    'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.Match.OptionFilters.OptionFilter' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.Match.OptionFilters.OptionFilter',
            False, 
            [
            _MetaInfoClassMember('matchoption', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Match option 60
                ''',
                'matchoption',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', True),
            _MetaInfoClassMember('pattern', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Enter hex pattern string
                ''',
                'pattern',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', True),
            _MetaInfoClassMember('format', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Set constant integer
                ''',
                'format',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', True),
            _MetaInfoClassMember('option-action', REFERENCE_ENUM_CLASS, 'BaseActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'BaseActionEnum', 
                [], [], 
                '''                Vendor action
                ''',
                'option_action',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-cfg',
            'option-filter',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg'
        ),
    },
    'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.Match.OptionFilters' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.Match.OptionFilters',
            False, 
            [
            _MetaInfoClassMember('option-filter', REFERENCE_LIST, 'OptionFilter' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.Match.OptionFilters.OptionFilter', 
                [], [], 
                '''                Specify match option
                ''',
                'option_filter',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-cfg',
            'option-filters',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg'
        ),
    },
    'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.Match.DefOptions.DefOption' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.Match.DefOptions.DefOption',
            False, 
            [
            _MetaInfoClassMember('def-matchoption', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Match option 60
                ''',
                'def_matchoption',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', True),
            _MetaInfoClassMember('def-matchaction', REFERENCE_ENUM_CLASS, 'BaseActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'BaseActionEnum', 
                [], [], 
                '''                Vendor action
                ''',
                'def_matchaction',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-cfg',
            'def-option',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg'
        ),
    },
    'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.Match.DefOptions' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.Match.DefOptions',
            False, 
            [
            _MetaInfoClassMember('def-option', REFERENCE_LIST, 'DefOption' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.Match.DefOptions.DefOption', 
                [], [], 
                '''                Specify match option
                ''',
                'def_option',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-cfg',
            'def-options',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg'
        ),
    },
    'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.Match' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.Match',
            False, 
            [
            _MetaInfoClassMember('def-options', REFERENCE_CLASS, 'DefOptions' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.Match.DefOptions', 
                [], [], 
                '''                Table of Option
                ''',
                'def_options',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('option-filters', REFERENCE_CLASS, 'OptionFilters' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.Match.OptionFilters', 
                [], [], 
                '''                Table of Option
                ''',
                'option_filters',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-cfg',
            'match',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg'
        ),
    },
    'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.BaseRelayOpt' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.BaseRelayOpt',
            False, 
            [
            _MetaInfoClassMember('authenticate', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Specify Relay Agent Information Option
                authenticate
                ''',
                'authenticate',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('remote-id', ATTRIBUTE, 'str' , None, None, 
                [(1, 256)], [], 
                '''                Enter remote-id value
                ''',
                'remote_id',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-cfg',
            'base-relay-opt',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg'
        ),
    },
    'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.BaseMatch.Options.Option.OptionProfile' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.BaseMatch.Options.Option.OptionProfile',
            False, 
            [
            _MetaInfoClassMember('profile-mode', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                none
                ''',
                'profile_mode',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('profile-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Profile name
                ''',
                'profile_name',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-cfg',
            'option-profile',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg'
        ),
    },
    'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.BaseMatch.Options.Option' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.BaseMatch.Options.Option',
            False, 
            [
            _MetaInfoClassMember('opt60', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                none
                ''',
                'opt60',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', True),
            _MetaInfoClassMember('opt60-hex-str', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Enter hex pattern string
                ''',
                'opt60_hex_str',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', True),
            _MetaInfoClassMember('format', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Set constant integer
                ''',
                'format',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', True),
            _MetaInfoClassMember('option-profile', REFERENCE_CLASS, 'OptionProfile' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.BaseMatch.Options.Option.OptionProfile', 
                [], [], 
                '''                Enter a profile
                ''',
                'option_profile',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-cfg',
            'option',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg'
        ),
    },
    'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.BaseMatch.Options' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.BaseMatch.Options',
            False, 
            [
            _MetaInfoClassMember('option', REFERENCE_LIST, 'Option' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.BaseMatch.Options.Option', 
                [], [], 
                '''                none
                ''',
                'option',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-cfg',
            'options',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg'
        ),
    },
    'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.BaseMatch' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.BaseMatch',
            False, 
            [
            _MetaInfoClassMember('options', REFERENCE_CLASS, 'Options' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.BaseMatch.Options', 
                [], [], 
                '''                Specify match option
                ''',
                'options',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-cfg',
            'base-match',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg'
        ),
    },
    'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base',
            False, 
            [
            _MetaInfoClassMember('base-match', REFERENCE_CLASS, 'BaseMatch' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.BaseMatch', 
                [], [], 
                '''                Insert match keyword
                ''',
                'base_match',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('base-relay-opt', REFERENCE_CLASS, 'BaseRelayOpt' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.BaseRelayOpt', 
                [], [], 
                '''                Insert Relay Agent Information circuit ID
                and remote ID suboptions in client request
                ''',
                'base_relay_opt',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('default-profile', REFERENCE_CLASS, 'DefaultProfile' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.DefaultProfile', 
                [], [], 
                '''                Enable the default profile
                ''',
                'default_profile',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable the DHCP IPv4 Base Profile
                ''',
                'enable',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('match', REFERENCE_CLASS, 'Match' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.Match', 
                [], [], 
                '''                Insert match keyword
                ''',
                'match',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-cfg',
            'base',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg'
        ),
    },
    'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.ServerIdCheck' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.ServerIdCheck',
            False, 
            [
            _MetaInfoClassMember('check', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                specify server-id-check disable
                ''',
                'check',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-cfg',
            'server-id-check',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg'
        ),
    },
    'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.LeaseLimit' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.LeaseLimit',
            False, 
            [
            _MetaInfoClassMember('lease-limit-value', REFERENCE_ENUM_CLASS, 'LeaseLimitValueEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'LeaseLimitValueEnum', 
                [], [], 
                '''                Configure Lease limit value
                ''',
                'lease_limit_value',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('range', ATTRIBUTE, 'int' , None, None, 
                [('1', '240000')], [], 
                '''                Value of limit lease count in Decimal
                ''',
                'range',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-cfg',
            'lease-limit',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg'
        ),
    },
    'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.RequestedIpAddress' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.RequestedIpAddress',
            False, 
            [
            _MetaInfoClassMember('check', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                specify requested-ip-address-check disable
                ''',
                'check',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-cfg',
            'requested-ip-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg'
        ),
    },
    'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.DefaultRouters' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.DefaultRouters',
            False, 
            [
            _MetaInfoClassMember('default-router', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Router's IP address
                ''',
                'default_router',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False, max_elements=8),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-cfg',
            'default-routers',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg'
        ),
    },
    'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.NetBiosNameServers' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.NetBiosNameServers',
            False, 
            [
            _MetaInfoClassMember('net-bios-name-server', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                NetBIOSNameServer's IP address
                ''',
                'net_bios_name_server',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False, max_elements=8),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-cfg',
            'net-bios-name-servers',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg'
        ),
    },
    'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Match.OptionDefaults.OptionDefault' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Match.OptionDefaults.OptionDefault',
            False, 
            [
            _MetaInfoClassMember('matchoption', REFERENCE_ENUM_CLASS, 'MatchoptionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'MatchoptionEnum', 
                [], [], 
                '''                Match option 60
                ''',
                'matchoption',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', True),
            _MetaInfoClassMember('matchaction', REFERENCE_ENUM_CLASS, 'MatchactionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'MatchactionEnum', 
                [], [], 
                '''                Vendor action
                ''',
                'matchaction',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-cfg',
            'option-default',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg'
        ),
    },
    'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Match.OptionDefaults' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Match.OptionDefaults',
            False, 
            [
            _MetaInfoClassMember('option-default', REFERENCE_LIST, 'OptionDefault' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Match.OptionDefaults.OptionDefault', 
                [], [], 
                '''                Specify match option
                ''',
                'option_default',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-cfg',
            'option-defaults',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg'
        ),
    },
    'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Match.Options.Option' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Match.Options.Option',
            False, 
            [
            _MetaInfoClassMember('matchoption', REFERENCE_ENUM_CLASS, 'MatchoptionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'MatchoptionEnum', 
                [], [], 
                '''                Match option 60
                ''',
                'matchoption',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', True),
            _MetaInfoClassMember('pattern', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Enter hex pattern string
                ''',
                'pattern',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', True),
            _MetaInfoClassMember('format', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Set constant integer
                ''',
                'format',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', True),
            _MetaInfoClassMember('matchaction', REFERENCE_ENUM_CLASS, 'MatchactionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'MatchactionEnum', 
                [], [], 
                '''                Vendor action
                ''',
                'matchaction',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-cfg',
            'option',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg'
        ),
    },
    'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Match.Options' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Match.Options',
            False, 
            [
            _MetaInfoClassMember('option', REFERENCE_LIST, 'Option' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Match.Options.Option', 
                [], [], 
                '''                Specify match option
                ''',
                'option',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-cfg',
            'options',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg'
        ),
    },
    'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Match' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Match',
            False, 
            [
            _MetaInfoClassMember('option-defaults', REFERENCE_CLASS, 'OptionDefaults' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Match.OptionDefaults', 
                [], [], 
                '''                Table of OptionDefault
                ''',
                'option_defaults',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('options', REFERENCE_CLASS, 'Options' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Match.Options', 
                [], [], 
                '''                Table of Option
                ''',
                'options',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-cfg',
            'match',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg'
        ),
    },
    'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.BroadcastFlag' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.BroadcastFlag',
            False, 
            [
            _MetaInfoClassMember('policy', REFERENCE_ENUM_CLASS, 'PolicyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'PolicyEnum', 
                [], [], 
                '''                Specify broadcast flag policy
                ''',
                'policy',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-cfg',
            'broadcast-flag',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg'
        ),
    },
    'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Session.ThrottleType.MacThrottle' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Session.ThrottleType.MacThrottle',
            False, 
            [
            _MetaInfoClassMember('num-block', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Throttle blocking period (in secs)
                ''',
                'num_block',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('num-discover', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Number of discovers at which to throttle
                ''',
                'num_discover',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('num-request', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Throttle request period (in secs)
                ''',
                'num_request',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-cfg',
            'mac-throttle',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg'
        ),
    },
    'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Session.ThrottleType' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Session.ThrottleType',
            False, 
            [
            _MetaInfoClassMember('mac-throttle', REFERENCE_CLASS, 'MacThrottle' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Session.ThrottleType.MacThrottle', 
                [], [], 
                '''                Throttle DHCP sessions from any one MAC
                address
                ''',
                'mac_throttle',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-cfg',
            'throttle-type',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg'
        ),
    },
    'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Session' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Session',
            False, 
            [
            _MetaInfoClassMember('throttle-type', REFERENCE_CLASS, 'ThrottleType' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Session.ThrottleType', 
                [], [], 
                '''                Throttle DHCP sessions based on MAC
                address
                ''',
                'throttle_type',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-cfg',
            'session',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg'
        ),
    },
    'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.DefaultRouters' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.DefaultRouters',
            False, 
            [
            _MetaInfoClassMember('default-router', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Router's IP address
                ''',
                'default_router',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False, max_elements=8),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-cfg',
            'default-routers',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg'
        ),
    },
    'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.NetBiosNameServers' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.NetBiosNameServers',
            False, 
            [
            _MetaInfoClassMember('net-bios-name-server', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                NetBIOSNameServer's IP address
                ''',
                'net_bios_name_server',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False, max_elements=8),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-cfg',
            'net-bios-name-servers',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg'
        ),
    },
    'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.ClassMatch.ClassOptions.ClassOption' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.ClassMatch.ClassOptions.ClassOption',
            False, 
            [
            _MetaInfoClassMember('matchoption', REFERENCE_ENUM_CLASS, 'MatchoptionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'MatchoptionEnum', 
                [], [], 
                '''                Match options
                ''',
                'matchoption',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', True),
            _MetaInfoClassMember('bit-mask', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Enter bit mask pattern string
                ''',
                'bit_mask',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('pattern', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Enter hex pattern string
                ''',
                'pattern',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-cfg',
            'class-option',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg'
        ),
    },
    'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.ClassMatch.ClassOptions' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.ClassMatch.ClassOptions',
            False, 
            [
            _MetaInfoClassMember('class-option', REFERENCE_LIST, 'ClassOption' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.ClassMatch.ClassOptions.ClassOption', 
                [], [], 
                '''                Specify match option
                ''',
                'class_option',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-cfg',
            'class-options',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg'
        ),
    },
    'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.ClassMatch' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.ClassMatch',
            False, 
            [
            _MetaInfoClassMember('class-options', REFERENCE_CLASS, 'ClassOptions' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.ClassMatch.ClassOptions', 
                [], [], 
                '''                Table of Class-Option
                ''',
                'class_options',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('l2-interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Specify match l2-interface
                ''',
                'l2_interface',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('vrf', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Specify match VRF
                ''',
                'vrf',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-cfg',
            'class-match',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg'
        ),
    },
    'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.Lease' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.Lease',
            False, 
            [
            _MetaInfoClassMember('days', ATTRIBUTE, 'int' , None, None, 
                [('0', '365')], [], 
                '''                Days
                ''',
                'days',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('hours', ATTRIBUTE, 'int' , None, None, 
                [('0', '23')], [], 
                '''                Hours
                ''',
                'hours',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('infinite', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Set string
                ''',
                'infinite',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('minutes', ATTRIBUTE, 'int' , None, None, 
                [('0', '59')], [], 
                '''                Minutes
                ''',
                'minutes',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-cfg',
            'lease',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg'
        ),
    },
    'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.NetbiosNodeType' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.NetbiosNodeType',
            False, 
            [
            _MetaInfoClassMember('broadcast-node', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Set string
                ''',
                'broadcast_node',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('hexadecimal', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{1,8}'], 
                '''                Hexadecimal number
                ''',
                'hexadecimal',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('hybrid-node', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Set string
                ''',
                'hybrid_node',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('mixed-node', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Set string
                ''',
                'mixed_node',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('peer-to-peer-node', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Set string
                ''',
                'peer_to_peer_node',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-cfg',
            'netbios-node-type',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg'
        ),
    },
    'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.DnsServers' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.DnsServers',
            False, 
            [
            _MetaInfoClassMember('dns-server', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                DNS Server's IP address
                ''',
                'dns_server',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False, max_elements=8),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-cfg',
            'dns-servers',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg'
        ),
    },
    'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.OptionCodes.OptionCode' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.OptionCodes.OptionCode',
            False, 
            [
            _MetaInfoClassMember('option-code', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                DHCP option code
                ''',
                'option_code',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', True),
            _MetaInfoClassMember('ascii-string', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ASCII string
                ''',
                'ascii_string',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('force-insert', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Set constant integer
                ''',
                'force_insert',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('hex-string', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Hexadecimal string
                ''',
                'hex_string',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('ip-address', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Server's IP address
                ''',
                'ip_address',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False, max_elements=8),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-cfg',
            'option-code',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg'
        ),
    },
    'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.OptionCodes' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.OptionCodes',
            False, 
            [
            _MetaInfoClassMember('option-code', REFERENCE_LIST, 'OptionCode' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.OptionCodes.OptionCode', 
                [], [], 
                '''                DHCP option code
                ''',
                'option_code',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-cfg',
            'option-codes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg'
        ),
    },
    'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_',
            False, 
            [
            _MetaInfoClassMember('class-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 128)], [], 
                '''                class name
                ''',
                'class_name',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', True),
            _MetaInfoClassMember('boot-filename', ATTRIBUTE, 'str' , None, None, 
                [(1, 128)], [], 
                '''                Boot Filename
                ''',
                'boot_filename',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('class-match', REFERENCE_CLASS, 'ClassMatch' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.ClassMatch', 
                [], [], 
                '''                Insert match keyword
                ''',
                'class_match',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('default-routers', REFERENCE_CLASS, 'DefaultRouters' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.DefaultRouters', 
                [], [], 
                '''                default routers
                ''',
                'default_routers',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('dns-servers', REFERENCE_CLASS, 'DnsServers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.DnsServers', 
                [], [], 
                '''                DNS servers
                ''',
                'dns_servers',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('domain-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 256)], [], 
                '''                Domain name
                ''',
                'domain_name',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable Create or enter server profile
                class. Deletion of this object also
                causes deletion of all associated objects
                under Class.
                ''',
                'enable',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('infinite-lease', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Infinite lease
                ''',
                'infinite_lease',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('lease', REFERENCE_CLASS, 'Lease' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.Lease', 
                [], [], 
                '''                lease
                ''',
                'lease',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('net-bios-name-servers', REFERENCE_CLASS, 'NetBiosNameServers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.NetBiosNameServers', 
                [], [], 
                '''                NetBIOS name servers
                ''',
                'net_bios_name_servers',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('netbios-node-type', REFERENCE_CLASS, 'NetbiosNodeType' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.NetbiosNodeType', 
                [], [], 
                '''                NetBIOS node type
                ''',
                'netbios_node_type',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('next-server', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Configure the tftp-server IP to be used
                by the client
                ''',
                'next_server',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('option-codes', REFERENCE_CLASS, 'OptionCodes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.OptionCodes', 
                [], [], 
                '''                Table of OptionCode
                ''',
                'option_codes',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('pool', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Specify the pool
                ''',
                'pool',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('subnet-mask', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Configure Subnet Mask
                ''',
                'subnet_mask',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-cfg',
            'class',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg'
        ),
    },
    'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes',
            False, 
            [
            _MetaInfoClassMember('class', REFERENCE_LIST, 'Class_' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_', 
                [], [], 
                '''                Create or enter server profile class
                ''',
                'class_',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-cfg',
            'classes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg'
        ),
    },
    'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Relay' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Relay',
            False, 
            [
            _MetaInfoClassMember('authenticate', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Specify Relay Agent Information Option
                authenticate
                ''',
                'authenticate',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-cfg',
            'relay',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg'
        ),
    },
    'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Lease' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Lease',
            False, 
            [
            _MetaInfoClassMember('days', ATTRIBUTE, 'int' , None, None, 
                [('0', '365')], [], 
                '''                Days
                ''',
                'days',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('hours', ATTRIBUTE, 'int' , None, None, 
                [('0', '23')], [], 
                '''                Hours
                ''',
                'hours',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('infinite', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Set string
                ''',
                'infinite',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('minutes', ATTRIBUTE, 'int' , None, None, 
                [('0', '59')], [], 
                '''                Minutes
                ''',
                'minutes',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-cfg',
            'lease',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg'
        ),
    },
    'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.NetbiosNodeType' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.NetbiosNodeType',
            False, 
            [
            _MetaInfoClassMember('broadcast-node', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Set string
                ''',
                'broadcast_node',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('hexadecimal', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{1,8}'], 
                '''                Hexadecimal number
                ''',
                'hexadecimal',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('hybrid-node', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Set string
                ''',
                'hybrid_node',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('mixed-node', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Set string
                ''',
                'mixed_node',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('peer-to-peer-node', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Set string
                ''',
                'peer_to_peer_node',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-cfg',
            'netbios-node-type',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg'
        ),
    },
    'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Aaa.DhcpOption' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Aaa.DhcpOption',
            False, 
            [
            _MetaInfoClassMember('force-insert', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable aaa dhcp option force-insert
                ''',
                'force_insert',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-cfg',
            'dhcp-option',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg'
        ),
    },
    'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Aaa' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Aaa',
            False, 
            [
            _MetaInfoClassMember('dhcp-option', REFERENCE_CLASS, 'DhcpOption' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Aaa.DhcpOption', 
                [], [], 
                '''                Enable aaa dhcp option force-insert
                ''',
                'dhcp_option',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-cfg',
            'aaa',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg'
        ),
    },
    'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.DnsServers' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.DnsServers',
            False, 
            [
            _MetaInfoClassMember('dns-server', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                DNS Server's IP address
                ''',
                'dns_server',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False, max_elements=8),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-cfg',
            'dns-servers',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg'
        ),
    },
    'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.OptionCodes.OptionCode' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.OptionCodes.OptionCode',
            False, 
            [
            _MetaInfoClassMember('option-code', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                DHCP option code
                ''',
                'option_code',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', True),
            _MetaInfoClassMember('ascii-string', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ASCII string
                ''',
                'ascii_string',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('force-insert', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Set constant integer
                ''',
                'force_insert',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('hex-string', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Hexadecimal string
                ''',
                'hex_string',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('ip-address', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Server's IP address
                ''',
                'ip_address',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False, max_elements=8),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-cfg',
            'option-code',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg'
        ),
    },
    'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.OptionCodes' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.OptionCodes',
            False, 
            [
            _MetaInfoClassMember('option-code', REFERENCE_LIST, 'OptionCode' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.OptionCodes.OptionCode', 
                [], [], 
                '''                DHCP option code
                ''',
                'option_code',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-cfg',
            'option-codes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg'
        ),
    },
    'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server',
            False, 
            [
            _MetaInfoClassMember('aaa', REFERENCE_CLASS, 'Aaa' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Aaa', 
                [], [], 
                '''                Enable aaa dhcp option force-insert
                ''',
                'aaa',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('boot-filename', ATTRIBUTE, 'str' , None, None, 
                [(1, 128)], [], 
                '''                Boot Filename
                ''',
                'boot_filename',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('broadcast-flag', REFERENCE_CLASS, 'BroadcastFlag' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.BroadcastFlag', 
                [], [], 
                '''                None
                ''',
                'broadcast_flag',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('classes', REFERENCE_CLASS, 'Classes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes', 
                [], [], 
                '''                Table of Class
                ''',
                'classes',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('default-routers', REFERENCE_CLASS, 'DefaultRouters' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.DefaultRouters', 
                [], [], 
                '''                default routers
                ''',
                'default_routers',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('dns-servers', REFERENCE_CLASS, 'DnsServers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.DnsServers', 
                [], [], 
                '''                DNS servers
                ''',
                'dns_servers',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('domain-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 256)], [], 
                '''                Domain name
                ''',
                'domain_name',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('infinite-lease', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Infinite lease
                ''',
                'infinite_lease',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('lease', REFERENCE_CLASS, 'Lease' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Lease', 
                [], [], 
                '''                lease
                ''',
                'lease',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('lease-limit', REFERENCE_CLASS, 'LeaseLimit' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.LeaseLimit', 
                [], [], 
                '''                Specify limit lease
                ''',
                'lease_limit',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('match', REFERENCE_CLASS, 'Match' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Match', 
                [], [], 
                '''                Insert match keyword
                ''',
                'match',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('net-bios-name-servers', REFERENCE_CLASS, 'NetBiosNameServers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.NetBiosNameServers', 
                [], [], 
                '''                NetBIOS name servers
                ''',
                'net_bios_name_servers',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('netbios-node-type', REFERENCE_CLASS, 'NetbiosNodeType' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.NetbiosNodeType', 
                [], [], 
                '''                NetBIOS node type
                ''',
                'netbios_node_type',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('next-server', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Configure the tftp-server IP to be used by
                the client
                ''',
                'next_server',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('option-codes', REFERENCE_CLASS, 'OptionCodes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.OptionCodes', 
                [], [], 
                '''                Table of OptionCode
                ''',
                'option_codes',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('pool', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Specify the Pool name
                ''',
                'pool',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('relay', REFERENCE_CLASS, 'Relay' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Relay', 
                [], [], 
                '''                Specify Relay Agent Information Option
                configuration
                ''',
                'relay',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('requested-ip-address', REFERENCE_CLASS, 'RequestedIpAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.RequestedIpAddress', 
                [], [], 
                '''                Validate Requested IP Address
                ''',
                'requested_ip_address',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('secure-arp', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable Secure Arp
                ''',
                'secure_arp',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('server-allow-move', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Allow dhcp subscriber move
                ''',
                'server_allow_move',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('server-id-check', REFERENCE_CLASS, 'ServerIdCheck' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.ServerIdCheck', 
                [], [], 
                '''                Validate server ID check
                ''',
                'server_id_check',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('session', REFERENCE_CLASS, 'Session' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Session', 
                [], [], 
                '''                Change sessions configuration
                ''',
                'session',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('subnet-mask', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Configure Subnet Mask
                ''',
                'subnet_mask',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
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
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
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
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
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
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
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
    'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_.Match.Option' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_.Match.Option',
            False, 
            [
            _MetaInfoClassMember('bit-mask', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Bit mask pattern
                ''',
                'bit_mask',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('option-type', REFERENCE_ENUM_CLASS, 'Dhcpv4MatchOptionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Dhcpv4MatchOptionEnum', 
                [], [], 
                '''                Match option
                ''',
                'option_type',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('pattern', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Hex pattern string
                ''',
                'pattern',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-cfg',
            'option',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg'
        ),
    },
    'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_.Match' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_.Match',
            False, 
            [
            _MetaInfoClassMember('option', REFERENCE_CLASS, 'Option' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_.Match.Option', 
                [], [], 
                '''                Match option
                ''',
                'option',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('vrf', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Match VRF name
                ''',
                'vrf',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-cfg',
            'match',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg'
        ),
    },
    'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_.Vrfs.Vrf.HelperAddresses.HelperAddress' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_.Vrfs.Vrf.HelperAddresses.HelperAddress',
            False, 
            [
            _MetaInfoClassMember('server-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address
                ''',
                'server_address',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', True),
            _MetaInfoClassMember('gateway-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Gateway address
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
    'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_.Vrfs.Vrf.HelperAddresses' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_.Vrfs.Vrf.HelperAddresses',
            False, 
            [
            _MetaInfoClassMember('helper-address', REFERENCE_LIST, 'HelperAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_.Vrfs.Vrf.HelperAddresses.HelperAddress', 
                [], [], 
                '''                Helper address
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
    'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_.Vrfs.Vrf' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_.Vrfs.Vrf',
            False, 
            [
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', True),
            _MetaInfoClassMember('helper-addresses', REFERENCE_CLASS, 'HelperAddresses' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_.Vrfs.Vrf.HelperAddresses', 
                [], [], 
                '''                Helper addresses
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
    'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_.Vrfs' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_.Vrfs',
            False, 
            [
            _MetaInfoClassMember('vrf', REFERENCE_LIST, 'Vrf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_.Vrfs.Vrf', 
                [], [], 
                '''                VRF name
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
    'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_',
            False, 
            [
            _MetaInfoClassMember('class-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Class name
                ''',
                'class_name',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', True),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable the DHCP IPV4 proxy class
                ''',
                'enable',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('match', REFERENCE_CLASS, 'Match' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_.Match', 
                [], [], 
                '''                Match option
                ''',
                'match',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('vrfs', REFERENCE_CLASS, 'Vrfs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_.Vrfs', 
                [], [], 
                '''                List of VRFs
                ''',
                'vrfs',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-cfg',
            'class',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg'
        ),
    },
    'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes',
            False, 
            [
            _MetaInfoClassMember('class', REFERENCE_LIST, 'Class_' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_', 
                [], [], 
                '''                DHCP class
                ''',
                'class_',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-cfg',
            'classes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg'
        ),
    },
    'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.RelayInformation' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.RelayInformation',
            False, 
            [
            _MetaInfoClassMember('allow-untrusted', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Forward untrusted packets
                ''',
                'allow_untrusted',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('authenticate', REFERENCE_ENUM_CLASS, 'Ipv4DhcpdRelayInfoOptionAuthenticateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4DhcpdRelayInfoOptionAuthenticateEnum', 
                [], [], 
                '''                Relay information option authenticate
                ''',
                'authenticate',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('check', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Check relay agent information option in
                server reply
                ''',
                'check',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('circuit-id', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Insert Circuit-id sub-option
                ''',
                'circuit_id',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('option', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Insert relay rgent information circuit ID
                and remote ID suboptions in client
                requests
                ''',
                'option',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('policy', REFERENCE_ENUM_CLASS, 'Ipv4DhcpdRelayInfoOptionPolicyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4DhcpdRelayInfoOptionPolicyEnum', 
                [], [], 
                '''                Relay information option policy
                ''',
                'policy',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('remote-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Remote ID
                ''',
                'remote_id',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('remote-id-suppress', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Suppress Remote ID
                ''',
                'remote_id_suppress',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('remote-id-xr', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Insert Remote-id sub-option
                ''',
                'remote_id_xr',
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
            'relay-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg'
        ),
    },
    'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Vrfs.Vrf.HelperAddresses.HelperAddress' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Vrfs.Vrf.HelperAddresses.HelperAddress',
            False, 
            [
            _MetaInfoClassMember('server-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address
                ''',
                'server_address',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', True),
            _MetaInfoClassMember('gateway-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Gateway address
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
    'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Vrfs.Vrf.HelperAddresses' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Vrfs.Vrf.HelperAddresses',
            False, 
            [
            _MetaInfoClassMember('helper-address', REFERENCE_LIST, 'HelperAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Vrfs.Vrf.HelperAddresses.HelperAddress', 
                [], [], 
                '''                Helper address
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
    'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Vrfs.Vrf' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Vrfs.Vrf',
            False, 
            [
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', True),
            _MetaInfoClassMember('helper-addresses', REFERENCE_CLASS, 'HelperAddresses' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Vrfs.Vrf.HelperAddresses', 
                [], [], 
                '''                Helper addresses
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
    'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Vrfs' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Vrfs',
            False, 
            [
            _MetaInfoClassMember('vrf', REFERENCE_LIST, 'Vrf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Vrfs.Vrf', 
                [], [], 
                '''                VRF name
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
    'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Sessions.ProxyThrottleType.ProxyMacThrottle' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Sessions.ProxyThrottleType.ProxyMacThrottle',
            False, 
            [
            _MetaInfoClassMember('num-block', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Throttle blocking period (in secs)
                ''',
                'num_block',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('num-discover', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Number of discovers at which to throttle
                ''',
                'num_discover',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('num-request', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Throttle request period (in secs)
                ''',
                'num_request',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-cfg',
            'proxy-mac-throttle',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg'
        ),
    },
    'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Sessions.ProxyThrottleType' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Sessions.ProxyThrottleType',
            False, 
            [
            _MetaInfoClassMember('proxy-mac-throttle', REFERENCE_CLASS, 'ProxyMacThrottle' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Sessions.ProxyThrottleType.ProxyMacThrottle', 
                [], [], 
                '''                Throttle DHCP sessions from any one MAC
                address
                ''',
                'proxy_mac_throttle',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-cfg',
            'proxy-throttle-type',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg'
        ),
    },
    'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Sessions' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Sessions',
            False, 
            [
            _MetaInfoClassMember('proxy-throttle-type', REFERENCE_CLASS, 'ProxyThrottleType' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Sessions.ProxyThrottleType', 
                [], [], 
                '''                Throttle DHCP sessions based on MAC
                address
                ''',
                'proxy_throttle_type',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-cfg',
            'sessions',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg'
        ),
    },
    'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.LimitLease' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.LimitLease',
            False, 
            [
            _MetaInfoClassMember('limit-lease-count', ATTRIBUTE, 'int' , None, None, 
                [('1', '240000')], [], 
                '''                Limit lease count
                ''',
                'limit_lease_count',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('limit-type', REFERENCE_ENUM_CLASS, 'Dhcpv4LimitLease1Enum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Dhcpv4LimitLease1Enum', 
                [], [], 
                '''                Lease limit type
                ''',
                'limit_type',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-cfg',
            'limit-lease',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg'
        ),
    },
    'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.LeaseProxy' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.LeaseProxy',
            False, 
            [
            _MetaInfoClassMember('client-lease-time', ATTRIBUTE, 'int' , None, None, 
                [('300', '4294967295')], [], 
                '''                Specify client lease proxy time
                ''',
                'client_lease_time',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('set-server-options', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Set DHCP server sent options in lease
                proxy generating ACK
                ''',
                'set_server_options',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-cfg',
            'lease-proxy',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg'
        ),
    },
    'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.BroadcastFlag' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.BroadcastFlag',
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
            'broadcast-flag',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg'
        ),
    },
    'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Match.DefOptions.DefOption' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Match.DefOptions.DefOption',
            False, 
            [
            _MetaInfoClassMember('def-matchoption', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Match option 60
                ''',
                'def_matchoption',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', True),
            _MetaInfoClassMember('def-matchaction', REFERENCE_ENUM_CLASS, 'ProxyActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'ProxyActionEnum', 
                [], [], 
                '''                Vendor action
                ''',
                'def_matchaction',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-cfg',
            'def-option',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg'
        ),
    },
    'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Match.DefOptions' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Match.DefOptions',
            False, 
            [
            _MetaInfoClassMember('def-option', REFERENCE_LIST, 'DefOption' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Match.DefOptions.DefOption', 
                [], [], 
                '''                Specify match option
                ''',
                'def_option',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-cfg',
            'def-options',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg'
        ),
    },
    'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Match.OptionFilters.OptionFilter' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Match.OptionFilters.OptionFilter',
            False, 
            [
            _MetaInfoClassMember('matchoption', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Match option 60
                ''',
                'matchoption',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', True),
            _MetaInfoClassMember('pattern', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Enter hex pattern string
                ''',
                'pattern',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', True),
            _MetaInfoClassMember('format', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Set constant integer
                ''',
                'format',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', True),
            _MetaInfoClassMember('matchaction', REFERENCE_ENUM_CLASS, 'ProxyActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'ProxyActionEnum', 
                [], [], 
                '''                Vendor action
                ''',
                'matchaction',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-cfg',
            'option-filter',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg'
        ),
    },
    'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Match.OptionFilters' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Match.OptionFilters',
            False, 
            [
            _MetaInfoClassMember('option-filter', REFERENCE_LIST, 'OptionFilter' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Match.OptionFilters.OptionFilter', 
                [], [], 
                '''                Specify match option
                ''',
                'option_filter',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-cfg',
            'option-filters',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg'
        ),
    },
    'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Match' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Match',
            False, 
            [
            _MetaInfoClassMember('def-options', REFERENCE_CLASS, 'DefOptions' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Match.DefOptions', 
                [], [], 
                '''                Table of Option
                ''',
                'def_options',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('option-filters', REFERENCE_CLASS, 'OptionFilters' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Match.OptionFilters', 
                [], [], 
                '''                Table of Option
                ''',
                'option_filters',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-cfg',
            'match',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg'
        ),
    },
    'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy',
            False, 
            [
            _MetaInfoClassMember('broadcast-flag', REFERENCE_CLASS, 'BroadcastFlag' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.BroadcastFlag', 
                [], [], 
                '''                Specify broadcast flag
                ''',
                'broadcast_flag',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('classes', REFERENCE_CLASS, 'Classes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes', 
                [], [], 
                '''                DHCP class table
                ''',
                'classes',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                DHCP IPV4 profile mode enable
                ''',
                'enable',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('lease-proxy', REFERENCE_CLASS, 'LeaseProxy' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.LeaseProxy', 
                [], [], 
                '''                DHCPv4 lease proxy
                ''',
                'lease_proxy',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('limit-lease', REFERENCE_CLASS, 'LimitLease' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.LimitLease', 
                [], [], 
                '''                Proxy limit lease
                ''',
                'limit_lease',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('match', REFERENCE_CLASS, 'Match' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Match', 
                [], [], 
                '''                Insert match keyword
                ''',
                'match',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('proxy-allow-move', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Allow dhcp subscriber move
                ''',
                'proxy_allow_move',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('relay-information', REFERENCE_CLASS, 'RelayInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.RelayInformation', 
                [], [], 
                '''                Relay agent information option
                ''',
                'relay_information',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('secure-arp', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                DHCP IPV4 profile proxy secure-arp enable
                ''',
                'secure_arp',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('sessions', REFERENCE_CLASS, 'Sessions' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Sessions', 
                [], [], 
                '''                Change sessions configuration
                ''',
                'sessions',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('vrfs', REFERENCE_CLASS, 'Vrfs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Vrfs', 
                [], [], 
                '''                List of VRFs
                ''',
                'vrfs',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-cfg',
            'proxy',
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
            _MetaInfoClassMember('base', REFERENCE_CLASS, 'Base' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base', 
                [], [], 
                '''                DHCP Base Profile
                ''',
                'base',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable the DHCP IPV4 Profile mode
                ''',
                'enable',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('proxy', REFERENCE_CLASS, 'Proxy' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy', 
                [], [], 
                '''                DHCP proxy profile
                ''',
                'proxy',
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
            _MetaInfoClassMember('snoop', REFERENCE_CLASS, 'Snoop' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Snoop', 
                [], [], 
                '''                DHCP Snoop profile
                ''',
                'snoop',
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
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
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
    'Ipv4Dhcpd.Interfaces.Interface.BaseInterface.BaseDhcpCircuitId' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Interfaces.Interface.BaseInterface.BaseDhcpCircuitId',
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
            'base-dhcp-circuit-id',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg'
        ),
    },
    'Ipv4Dhcpd.Interfaces.Interface.BaseInterface' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Interfaces.Interface.BaseInterface',
            False, 
            [
            _MetaInfoClassMember('base-dhcp-circuit-id', REFERENCE_CLASS, 'BaseDhcpCircuitId' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4Dhcpd.Interfaces.Interface.BaseInterface.BaseDhcpCircuitId', 
                [], [], 
                '''                Circuit ID value
                ''',
                'base_dhcp_circuit_id',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
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
    'Ipv4Dhcpd.Interfaces.Interface.StaticMode.Statics.Static' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Interfaces.Interface.StaticMode.Statics.Static',
            False, 
            [
            _MetaInfoClassMember('mac-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                MACAddress
                ''',
                'mac_address',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', True),
            _MetaInfoClassMember('client-id', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                Client Id
                ''',
                'client_id',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', True),
            _MetaInfoClassMember('layer', REFERENCE_ENUM_CLASS, 'Ipv4DhcpdLayerEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4DhcpdLayerEnum', 
                [], [], 
                '''                DHCP IPV4 Static layer
                ''',
                'layer',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', True),
            _MetaInfoClassMember('static-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IP address
                ''',
                'static_address',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-cfg',
            'static',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg'
        ),
    },
    'Ipv4Dhcpd.Interfaces.Interface.StaticMode.Statics' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Interfaces.Interface.StaticMode.Statics',
            False, 
            [
            _MetaInfoClassMember('static', REFERENCE_LIST, 'Static' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4Dhcpd.Interfaces.Interface.StaticMode.Statics.Static', 
                [], [], 
                '''                DHCP static binding of Mac address to IP
                address
                ''',
                'static',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-cfg',
            'statics',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-dhcpd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg'
        ),
    },
    'Ipv4Dhcpd.Interfaces.Interface.StaticMode' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Interfaces.Interface.StaticMode',
            False, 
            [
            _MetaInfoClassMember('statics', REFERENCE_CLASS, 'Statics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4Dhcpd.Interfaces.Interface.StaticMode.Statics', 
                [], [], 
                '''                Static Table Entries containing MAC address
                to IP address bindings
                ''',
                'statics',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-dhcpd-cfg',
            'static-mode',
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
    'Ipv4Dhcpd.Interfaces.Interface.ServerInterface.ServerDhcpCircuitId' : {
        'meta_info' : _MetaInfoClass('Ipv4Dhcpd.Interfaces.Interface.ServerInterface.ServerDhcpCircuitId',
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
            'server-dhcp-circuit-id',
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
            _MetaInfoClassMember('server-dhcp-circuit-id', REFERENCE_CLASS, 'ServerDhcpCircuitId' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4Dhcpd.Interfaces.Interface.ServerInterface.ServerDhcpCircuitId', 
                [], [], 
                '''                Circuit ID value
                ''',
                'server_dhcp_circuit_id',
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
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
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
            _MetaInfoClassMember('static-mode', REFERENCE_CLASS, 'StaticMode' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4Dhcpd.Interfaces.Interface.StaticMode', 
                [], [], 
                '''                Static Table Entries containing MAC address to
                IP address bindings
                ''',
                'static_mode',
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
            _MetaInfoClassMember('inner-cos', ATTRIBUTE, 'int' , None, None, 
                [('0', '7')], [], 
                '''                Configure inner cos values for dhcp packets
                ''',
                'inner_cos',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4Dhcpd.Interfaces', 
                [], [], 
                '''                DHCP IPV4 Interface Table
                ''',
                'interfaces',
                'Cisco-IOS-XR-ipv4-dhcpd-cfg', False),
            _MetaInfoClassMember('outer-cos', ATTRIBUTE, 'int' , None, None, 
                [('0', '7')], [], 
                '''                Configure outer cos values for dhcp packets
                ''',
                'outer_cos',
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
_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Snoop.RelayInformationOption.RemoteId']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Snoop.RelayInformationOption']['meta_info']
_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Snoop.RelayInformationOption']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Snoop']['meta_info']
_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.Match.OptionFilters.OptionFilter']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.Match.OptionFilters']['meta_info']
_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.Match.DefOptions.DefOption']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.Match.DefOptions']['meta_info']
_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.Match.OptionFilters']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.Match']['meta_info']
_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.Match.DefOptions']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.Match']['meta_info']
_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.BaseMatch.Options.Option.OptionProfile']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.BaseMatch.Options.Option']['meta_info']
_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.BaseMatch.Options.Option']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.BaseMatch.Options']['meta_info']
_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.BaseMatch.Options']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.BaseMatch']['meta_info']
_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.DefaultProfile']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base']['meta_info']
_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.Match']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base']['meta_info']
_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.BaseRelayOpt']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base']['meta_info']
_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.BaseMatch']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base']['meta_info']
_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Match.OptionDefaults.OptionDefault']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Match.OptionDefaults']['meta_info']
_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Match.Options.Option']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Match.Options']['meta_info']
_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Match.OptionDefaults']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Match']['meta_info']
_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Match.Options']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Match']['meta_info']
_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Session.ThrottleType.MacThrottle']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Session.ThrottleType']['meta_info']
_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Session.ThrottleType']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Session']['meta_info']
_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.ClassMatch.ClassOptions.ClassOption']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.ClassMatch.ClassOptions']['meta_info']
_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.ClassMatch.ClassOptions']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.ClassMatch']['meta_info']
_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.OptionCodes.OptionCode']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.OptionCodes']['meta_info']
_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.DefaultRouters']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_']['meta_info']
_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.NetBiosNameServers']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_']['meta_info']
_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.ClassMatch']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_']['meta_info']
_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.Lease']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_']['meta_info']
_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.NetbiosNodeType']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_']['meta_info']
_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.DnsServers']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_']['meta_info']
_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.OptionCodes']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_']['meta_info']
_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes']['meta_info']
_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Aaa.DhcpOption']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Aaa']['meta_info']
_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.OptionCodes.OptionCode']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.OptionCodes']['meta_info']
_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.ServerIdCheck']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server']['meta_info']
_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.LeaseLimit']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server']['meta_info']
_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.RequestedIpAddress']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server']['meta_info']
_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.DefaultRouters']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server']['meta_info']
_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.NetBiosNameServers']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server']['meta_info']
_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Match']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server']['meta_info']
_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.BroadcastFlag']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server']['meta_info']
_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Session']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server']['meta_info']
_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server']['meta_info']
_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Relay']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server']['meta_info']
_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Lease']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server']['meta_info']
_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.NetbiosNodeType']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server']['meta_info']
_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Aaa']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server']['meta_info']
_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.DnsServers']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server']['meta_info']
_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.OptionCodes']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server']['meta_info']
_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.Vrfs.Vrf.HelperAddresses.HelperAddress']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.Vrfs.Vrf.HelperAddresses']['meta_info']
_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.Vrfs.Vrf.HelperAddresses']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.Vrfs.Vrf']['meta_info']
_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.Vrfs.Vrf']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.Vrfs']['meta_info']
_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.GiAddrPolicy']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay']['meta_info']
_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.Vrfs']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay']['meta_info']
_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.RelayInformationOption']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay']['meta_info']
_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.BroadcastPolicy']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay']['meta_info']
_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_.Match.Option']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_.Match']['meta_info']
_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_.Vrfs.Vrf.HelperAddresses.HelperAddress']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_.Vrfs.Vrf.HelperAddresses']['meta_info']
_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_.Vrfs.Vrf.HelperAddresses']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_.Vrfs.Vrf']['meta_info']
_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_.Vrfs.Vrf']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_.Vrfs']['meta_info']
_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_.Match']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_']['meta_info']
_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_.Vrfs']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_']['meta_info']
_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes']['meta_info']
_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Vrfs.Vrf.HelperAddresses.HelperAddress']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Vrfs.Vrf.HelperAddresses']['meta_info']
_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Vrfs.Vrf.HelperAddresses']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Vrfs.Vrf']['meta_info']
_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Vrfs.Vrf']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Vrfs']['meta_info']
_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Sessions.ProxyThrottleType.ProxyMacThrottle']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Sessions.ProxyThrottleType']['meta_info']
_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Sessions.ProxyThrottleType']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Sessions']['meta_info']
_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Match.DefOptions.DefOption']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Match.DefOptions']['meta_info']
_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Match.OptionFilters.OptionFilter']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Match.OptionFilters']['meta_info']
_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Match.DefOptions']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Match']['meta_info']
_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Match.OptionFilters']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Match']['meta_info']
_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy']['meta_info']
_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.RelayInformation']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy']['meta_info']
_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Vrfs']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy']['meta_info']
_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Sessions']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy']['meta_info']
_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.LimitLease']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy']['meta_info']
_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.LeaseProxy']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy']['meta_info']
_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.BroadcastFlag']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy']['meta_info']
_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Match']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy']['meta_info']
_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Snoop']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode']['meta_info']
_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode']['meta_info']
_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode']['meta_info']
_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode']['meta_info']
_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode']['meta_info']
_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes.Mode']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes']['meta_info']
_meta_table['Ipv4Dhcpd.Profiles.Profile.Modes']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Profiles.Profile']['meta_info']
_meta_table['Ipv4Dhcpd.Profiles.Profile']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Profiles']['meta_info']
_meta_table['Ipv4Dhcpd.Interfaces.Interface.ProxyInterface.DhcpCircuitId']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Interfaces.Interface.ProxyInterface']['meta_info']
_meta_table['Ipv4Dhcpd.Interfaces.Interface.BaseInterface.BaseDhcpCircuitId']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Interfaces.Interface.BaseInterface']['meta_info']
_meta_table['Ipv4Dhcpd.Interfaces.Interface.RelayInterface.RelayDhcpCircuitId']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Interfaces.Interface.RelayInterface']['meta_info']
_meta_table['Ipv4Dhcpd.Interfaces.Interface.StaticMode.Statics.Static']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Interfaces.Interface.StaticMode.Statics']['meta_info']
_meta_table['Ipv4Dhcpd.Interfaces.Interface.StaticMode.Statics']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Interfaces.Interface.StaticMode']['meta_info']
_meta_table['Ipv4Dhcpd.Interfaces.Interface.ServerInterface.ServerDhcpCircuitId']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Interfaces.Interface.ServerInterface']['meta_info']
_meta_table['Ipv4Dhcpd.Interfaces.Interface.SnoopInterface.SnoopCircuitId']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Interfaces.Interface.SnoopInterface']['meta_info']
_meta_table['Ipv4Dhcpd.Interfaces.Interface.ProxyInterface']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Interfaces.Interface']['meta_info']
_meta_table['Ipv4Dhcpd.Interfaces.Interface.BaseInterface']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Interfaces.Interface']['meta_info']
_meta_table['Ipv4Dhcpd.Interfaces.Interface.RelayInterface']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Interfaces.Interface']['meta_info']
_meta_table['Ipv4Dhcpd.Interfaces.Interface.StaticMode']['meta_info'].parent =_meta_table['Ipv4Dhcpd.Interfaces.Interface']['meta_info']
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
