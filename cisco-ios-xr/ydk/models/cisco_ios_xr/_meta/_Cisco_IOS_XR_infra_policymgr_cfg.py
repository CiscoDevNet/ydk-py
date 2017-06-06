


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'EventTypeEnum' : _MetaInfoEnum('EventTypeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg',
        {
            'account-logoff':'account_logoff',
            'account-logon':'account_logon',
            'authentication-failure':'authentication_failure',
            'authentication-no-response':'authentication_no_response',
            'authorization-failure':'authorization_failure',
            'authorization-no-response':'authorization_no_response',
            'credit-exhausted':'credit_exhausted',
            'exception':'exception',
            'idle-timeout':'idle_timeout',
            'quota-depleted':'quota_depleted',
            'service-start':'service_start',
            'service-stop':'service_stop',
            'session-activate':'session_activate',
            'session-start':'session_start',
            'session-stop':'session_stop',
            'timer-expiry':'timer_expiry',
        }, 'Cisco-IOS-XR-infra-policymgr-cfg', _yang_ns._namespaces['Cisco-IOS-XR-infra-policymgr-cfg']),
    'ClassMapTypeEnum' : _MetaInfoEnum('ClassMapTypeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg',
        {
            'qos':'qos',
            'traffic':'traffic',
            'control':'control',
        }, 'Cisco-IOS-XR-infra-policymgr-cfg', _yang_ns._namespaces['Cisco-IOS-XR-infra-policymgr-cfg']),
    'PolicyMapTypeEnum' : _MetaInfoEnum('PolicyMapTypeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg',
        {
            'qos':'qos',
            'pbr':'pbr',
            'traffic':'traffic',
            'subscriber-control':'subscriber_control',
            'redirect':'redirect',
            'flow-monitor':'flow_monitor',
        }, 'Cisco-IOS-XR-infra-policymgr-cfg', _yang_ns._namespaces['Cisco-IOS-XR-infra-policymgr-cfg']),
    'AuthorizeIdentifierEnum' : _MetaInfoEnum('AuthorizeIdentifierEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg',
        {
            'circuit-id':'circuit_id',
            'dhcp-client-id':'dhcp_client_id',
            'remote-id':'remote_id',
            'source-address-ipv4':'source_address_ipv4',
            'source-address-ipv6':'source_address_ipv6',
            'source-address-mac':'source_address_mac',
            'username':'username',
        }, 'Cisco-IOS-XR-infra-policymgr-cfg', _yang_ns._namespaces['Cisco-IOS-XR-infra-policymgr-cfg']),
    'PmapClassMapTypeEnum' : _MetaInfoEnum('PmapClassMapTypeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg',
        {
            'qos':'qos',
            'traffic':'traffic',
            'subscriber-control':'subscriber_control',
        }, 'Cisco-IOS-XR-infra-policymgr-cfg', _yang_ns._namespaces['Cisco-IOS-XR-infra-policymgr-cfg']),
    'ExecutionStrategyEnum' : _MetaInfoEnum('ExecutionStrategyEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg',
        {
            'do-all':'do_all',
            'do-until-failure':'do_until_failure',
            'do-until-success':'do_until_success',
        }, 'Cisco-IOS-XR-infra-policymgr-cfg', _yang_ns._namespaces['Cisco-IOS-XR-infra-policymgr-cfg']),
    'PolicyManager.ClassMaps.ClassMap.Match.DestinationAddressIpv4' : {
        'meta_info' : _MetaInfoClass('PolicyManager.ClassMaps.ClassMap.Match.DestinationAddressIpv4',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address.
                ''',
                'address',
                'Cisco-IOS-XR-infra-policymgr-cfg', True),
            _MetaInfoClassMember('netmask', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 netmask.
                ''',
                'netmask',
                'Cisco-IOS-XR-infra-policymgr-cfg', True),
            ],
            'Cisco-IOS-XR-infra-policymgr-cfg',
            'destination-address-ipv4',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-policymgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg'
        ),
    },
    'PolicyManager.ClassMaps.ClassMap.Match.DestinationAddressIpv6' : {
        'meta_info' : _MetaInfoClass('PolicyManager.ClassMaps.ClassMap.Match.DestinationAddressIpv6',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address.
                ''',
                'address',
                'Cisco-IOS-XR-infra-policymgr-cfg', True),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '128')], [], 
                '''                IPv6 prefix length.
                ''',
                'prefix_length',
                'Cisco-IOS-XR-infra-policymgr-cfg', True),
            ],
            'Cisco-IOS-XR-infra-policymgr-cfg',
            'destination-address-ipv6',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-policymgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg'
        ),
    },
    'PolicyManager.ClassMaps.ClassMap.Match.SourceAddressIpv4' : {
        'meta_info' : _MetaInfoClass('PolicyManager.ClassMaps.ClassMap.Match.SourceAddressIpv4',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address.
                ''',
                'address',
                'Cisco-IOS-XR-infra-policymgr-cfg', True),
            _MetaInfoClassMember('netmask', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 netmask.
                ''',
                'netmask',
                'Cisco-IOS-XR-infra-policymgr-cfg', True),
            ],
            'Cisco-IOS-XR-infra-policymgr-cfg',
            'source-address-ipv4',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-policymgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg'
        ),
    },
    'PolicyManager.ClassMaps.ClassMap.Match.SourceAddressIpv6' : {
        'meta_info' : _MetaInfoClass('PolicyManager.ClassMaps.ClassMap.Match.SourceAddressIpv6',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address.
                ''',
                'address',
                'Cisco-IOS-XR-infra-policymgr-cfg', True),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '128')], [], 
                '''                IPv6 prefix length.
                ''',
                'prefix_length',
                'Cisco-IOS-XR-infra-policymgr-cfg', True),
            ],
            'Cisco-IOS-XR-infra-policymgr-cfg',
            'source-address-ipv6',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-policymgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg'
        ),
    },
    'PolicyManager.ClassMaps.ClassMap.Match.DomainName' : {
        'meta_info' : _MetaInfoClass('PolicyManager.ClassMaps.ClassMap.Match.DomainName',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Domain name or regular expression.
                ''',
                'name',
                'Cisco-IOS-XR-infra-policymgr-cfg', True),
            _MetaInfoClassMember('format', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Domain-format name.
                ''',
                'format',
                'Cisco-IOS-XR-infra-policymgr-cfg', True),
            ],
            'Cisco-IOS-XR-infra-policymgr-cfg',
            'domain-name',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-policymgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg'
        ),
    },
    'PolicyManager.ClassMaps.ClassMap.Match.DomainNameRegex' : {
        'meta_info' : _MetaInfoClass('PolicyManager.ClassMaps.ClassMap.Match.DomainNameRegex',
            False, 
            [
            _MetaInfoClassMember('regex', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Domain name or regular expression.
                ''',
                'regex',
                'Cisco-IOS-XR-infra-policymgr-cfg', True),
            _MetaInfoClassMember('format', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Domain-format name.
                ''',
                'format',
                'Cisco-IOS-XR-infra-policymgr-cfg', True),
            ],
            'Cisco-IOS-XR-infra-policymgr-cfg',
            'domain-name-regex',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-policymgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg'
        ),
    },
    'PolicyManager.ClassMaps.ClassMap.Match.Flow.FlowCache' : {
        'meta_info' : _MetaInfoClass('PolicyManager.ClassMaps.ClassMap.Match.Flow.FlowCache',
            False, 
            [
            _MetaInfoClassMember('idle-timeout', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Maximum time of inactivity for a flow.
                ''',
                'idle_timeout',
                'Cisco-IOS-XR-infra-policymgr-cfg', False, [
                    _MetaInfoClassMember('idle-timeout', ATTRIBUTE, 'int' , None, None, 
                        [('10', '2550')], [], 
                        '''                        Maximum time of inactivity for a flow.
                        ''',
                        'idle_timeout',
                        'Cisco-IOS-XR-infra-policymgr-cfg', False),
                    _MetaInfoClassMember('idle-timeout', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(None)|(none)'], 
                        '''                        Maximum time of inactivity for a flow.
                        ''',
                        'idle_timeout',
                        'Cisco-IOS-XR-infra-policymgr-cfg', False),
                ]),
            ],
            'Cisco-IOS-XR-infra-policymgr-cfg',
            'flow-cache',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-policymgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg'
        ),
    },
    'PolicyManager.ClassMaps.ClassMap.Match.Flow' : {
        'meta_info' : _MetaInfoClass('PolicyManager.ClassMaps.ClassMap.Match.Flow',
            False, 
            [
            _MetaInfoClassMember('flow-cache', REFERENCE_CLASS, 'FlowCache' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg', 'PolicyManager.ClassMaps.ClassMap.Match.Flow.FlowCache', 
                [], [], 
                '''                Configure the flow-cache parameters
                ''',
                'flow_cache',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('flow-key', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'(SourceIP)|(DestinationIP)|(5Tuple)'], 
                '''                Configure the flow-key parameters.
                ''',
                'flow_key',
                'Cisco-IOS-XR-infra-policymgr-cfg', False, max_elements=2),
            ],
            'Cisco-IOS-XR-infra-policymgr-cfg',
            'flow',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-policymgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg'
        ),
    },
    'PolicyManager.ClassMaps.ClassMap.Match' : {
        'meta_info' : _MetaInfoClass('PolicyManager.ClassMaps.ClassMap.Match',
            False, 
            [
            _MetaInfoClassMember('atm-clp', ATTRIBUTE, 'int' , None, None, 
                [('0', '1')], [], 
                '''                Match ATM CLP bit.
                ''',
                'atm_clp',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('atm-oam', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Match ATM OAM.
                ''',
                'atm_oam',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('authen-status', ATTRIBUTE, 'str' , None, None, 
                [], [b'(authenticated)|(unauthenticated)'], 
                '''                Match authentication status.
                ''',
                'authen_status',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('cac-admit', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Match CAC admitted.
                ''',
                'cac_admit',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('cac-unadmit', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Match CAC unadmitted.
                ''',
                'cac_unadmit',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('circuit-id', REFERENCE_LEAFLIST, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Match Circuit ID.
                ''',
                'circuit_id',
                'Cisco-IOS-XR-infra-policymgr-cfg', False, max_elements=8),
            _MetaInfoClassMember('circuit-id-regex', REFERENCE_LEAFLIST, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Match Circuit id regex.
                ''',
                'circuit_id_regex',
                'Cisco-IOS-XR-infra-policymgr-cfg', False, max_elements=8),
            _MetaInfoClassMember('cos', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '7')], [], 
                '''                Match CoS.
                ''',
                'cos',
                'Cisco-IOS-XR-infra-policymgr-cfg', False, max_elements=8),
            _MetaInfoClassMember('dei', ATTRIBUTE, 'int' , None, None, 
                [('0', '1')], [], 
                '''                Match DEI bit.
                ''',
                'dei',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('dei-inner', ATTRIBUTE, 'int' , None, None, 
                [('0', '1')], [], 
                '''                Match DEI INNER  bit.
                ''',
                'dei_inner',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('destination-address-ipv4', REFERENCE_LIST, 'DestinationAddressIpv4' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg', 'PolicyManager.ClassMaps.ClassMap.Match.DestinationAddressIpv4', 
                [], [], 
                '''                Match destination IPv4 address.
                ''',
                'destination_address_ipv4',
                'Cisco-IOS-XR-infra-policymgr-cfg', False, max_elements=8),
            _MetaInfoClassMember('destination-address-ipv6', REFERENCE_LIST, 'DestinationAddressIpv6' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg', 'PolicyManager.ClassMaps.ClassMap.Match.DestinationAddressIpv6', 
                [], [], 
                '''                Match destination IPv6 address.
                ''',
                'destination_address_ipv6',
                'Cisco-IOS-XR-infra-policymgr-cfg', False, max_elements=8),
            _MetaInfoClassMember('destination-mac', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                Match destination MAC address.
                ''',
                'destination_mac',
                'Cisco-IOS-XR-infra-policymgr-cfg', False, max_elements=8),
            _MetaInfoClassMember('destination-port', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'(\\d+)|(\\d+\\-\\d+)'], 
                '''                Match destination port. 
                Should be value 0..65535 or range.
                ''',
                'destination_port',
                'Cisco-IOS-XR-infra-policymgr-cfg', False, max_elements=8),
            _MetaInfoClassMember('dhcp-client-id', REFERENCE_LEAFLIST, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Match dhcp client ID.
                ''',
                'dhcp_client_id',
                'Cisco-IOS-XR-infra-policymgr-cfg', False, max_elements=8),
            _MetaInfoClassMember('dhcp-client-id-regex', REFERENCE_LEAFLIST, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Match dhcp client id regex.
                ''',
                'dhcp_client_id_regex',
                'Cisco-IOS-XR-infra-policymgr-cfg', False, max_elements=8),
            _MetaInfoClassMember('discard-class', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '7')], [], 
                '''                Match discard class.
                ''',
                'discard_class',
                'Cisco-IOS-XR-infra-policymgr-cfg', False, max_elements=8),
            _MetaInfoClassMember('domain-name', REFERENCE_LIST, 'DomainName' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg', 'PolicyManager.ClassMaps.ClassMap.Match.DomainName', 
                [], [], 
                '''                Match domain name.
                ''',
                'domain_name',
                'Cisco-IOS-XR-infra-policymgr-cfg', False, max_elements=8),
            _MetaInfoClassMember('domain-name-regex', REFERENCE_LIST, 'DomainNameRegex' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg', 'PolicyManager.ClassMaps.ClassMap.Match.DomainNameRegex', 
                [], [], 
                '''                Match domain name.
                ''',
                'domain_name_regex',
                'Cisco-IOS-XR-infra-policymgr-cfg', False, max_elements=8),
            _MetaInfoClassMember('dscp', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'([0-9]|[1-5][0-9]|6[0-3])|(([0-9]|[1-5][0-9]|6[0-3])-([0-9]|[1-5][0-9]|6[0-3]))|(af11)|(af12)|(af13)|(af21)|(af22)|(af23)|(af31)|(af32)|(af33)|(af41)|(af42)|(af43)|(ef)|(default)|(cs1)|(cs2)|(cs3)|(cs4)|(cs5)|(cs6)|(cs7)'], 
                '''                Match DSCP.
                ''',
                'dscp',
                'Cisco-IOS-XR-infra-policymgr-cfg', False, max_elements=8),
            _MetaInfoClassMember('ethernet-services-acl', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Match Ethernet Services
                ''',
                'ethernet_services_acl',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('ethertype', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'((153[6-9]|15[4-9][0-9]|1[6-9][0-9][0-9]|[2-9][0-9][0-9][0-9])|([1-5][0-9][0-9][0-9][0-9]|6[0-4][0-9][0-9][0-9])|(65[0-4][0-9][0-9]|655[0-2][0-9]|6553[0-5]))|((arp)|(ipv4)|(ipv6))'], 
                '''                Match Ethertype.
                ''',
                'ethertype',
                'Cisco-IOS-XR-infra-policymgr-cfg', False, max_elements=8),
            _MetaInfoClassMember('flow', REFERENCE_CLASS, 'Flow' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg', 'PolicyManager.ClassMaps.ClassMap.Match.Flow', 
                [], [], 
                '''                Match flow.
                ''',
                'flow',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('flow-tag', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'(\\d+)|(\\d+\\-\\d+)'], 
                '''                Match flow-tag. Should be value 1..63 or range.
                ''',
                'flow_tag',
                'Cisco-IOS-XR-infra-policymgr-cfg', False, max_elements=8),
            _MetaInfoClassMember('fr-de', ATTRIBUTE, 'int' , None, None, 
                [('0', '1')], [], 
                '''                Set FrameRelay DE bit.
                ''',
                'fr_de',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('fragment-type', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'(first-fragment)|(is-fragment)|(last-fragment)'], 
                '''                Match fragment type for a packet.
                ''',
                'fragment_type',
                'Cisco-IOS-XR-infra-policymgr-cfg', False, max_elements=3),
            _MetaInfoClassMember('frame-relay-dlci', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'(\\d+)|(\\d+\\-\\d+)'], 
                '''                Match frame-relay DLCI value. 
                Should be value 16..1007 or range.
                ''',
                'frame_relay_dlci',
                'Cisco-IOS-XR-infra-policymgr-cfg', False, max_elements=8),
            _MetaInfoClassMember('icmpv4-code', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'(\\d+)|(\\d+\\-\\d+)'], 
                '''                Match IPv4 ICMP code. 
                Should be value 0..255 or range.
                ''',
                'icmpv4_code',
                'Cisco-IOS-XR-infra-policymgr-cfg', False, max_elements=8),
            _MetaInfoClassMember('icmpv4-type', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'(\\d+)|(\\d+\\-\\d+)'], 
                '''                Match IPv4 ICMP type. 
                Should be value 0..255 or range.
                ''',
                'icmpv4_type',
                'Cisco-IOS-XR-infra-policymgr-cfg', False, max_elements=8),
            _MetaInfoClassMember('icmpv6-code', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'(\\d+)|(\\d+\\-\\d+)'], 
                '''                Match IPv6 ICMP code. 
                Should be value 0..255 or range.
                ''',
                'icmpv6_code',
                'Cisco-IOS-XR-infra-policymgr-cfg', False, max_elements=8),
            _MetaInfoClassMember('icmpv6-type', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'(\\d+)|(\\d+\\-\\d+)'], 
                '''                Match IPv6 ICMP type. 
                Should be value 0..255 or range.
                ''',
                'icmpv6_type',
                'Cisco-IOS-XR-infra-policymgr-cfg', False, max_elements=8),
            _MetaInfoClassMember('inner-cos', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '7')], [], 
                '''                Match inner CoS.
                ''',
                'inner_cos',
                'Cisco-IOS-XR-infra-policymgr-cfg', False, max_elements=8),
            _MetaInfoClassMember('inner-vlan', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'(\\d+)|(\\d+\\-\\d+)'], 
                '''                Match inner VLAN ID.
                ''',
                'inner_vlan',
                'Cisco-IOS-XR-infra-policymgr-cfg', False, max_elements=8),
            _MetaInfoClassMember('ipv4-acl', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Match IPv4 ACL.
                ''',
                'ipv4_acl',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('ipv4-dscp', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'([0-9]|[1-5][0-9]|6[0-3])|(([0-9]|[1-5][0-9]|6[0-3])-([0-9]|[1-5][0-9]|6[0-3]))|(af11)|(af12)|(af13)|(af21)|(af22)|(af23)|(af31)|(af32)|(af33)|(af41)|(af42)|(af43)|(ef)|(default)|(cs1)|(cs2)|(cs3)|(cs4)|(cs5)|(cs6)|(cs7)'], 
                '''                Match IPv4 DSCP.
                ''',
                'ipv4_dscp',
                'Cisco-IOS-XR-infra-policymgr-cfg', False, max_elements=8),
            _MetaInfoClassMember('ipv4-packet-length', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'(\\d+)|(\\d+\\-\\d+)'], 
                '''                Match IPv4 packet length.
                Should be value 0..65535 or range.
                ''',
                'ipv4_packet_length',
                'Cisco-IOS-XR-infra-policymgr-cfg', False, max_elements=8),
            _MetaInfoClassMember('ipv4-precedence', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Match IPv4 precedence.
                ''',
                'ipv4_precedence',
                'Cisco-IOS-XR-infra-policymgr-cfg', False, [
                    _MetaInfoClassMember('ipv4-precedence', REFERENCE_LEAFLIST, 'int' , None, None, 
                        [('0', '7')], [], 
                        '''                        Match IPv4 precedence.
                        ''',
                        'ipv4_precedence',
                        'Cisco-IOS-XR-infra-policymgr-cfg', False, max_elements=8),
                    _MetaInfoClassMember('ipv4-precedence', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [b'(critical)|(flash)|(flash-override)|(immediate)|(internet)|(network)|(priority)|(routine)'], 
                        '''                        Match IPv4 precedence.
                        ''',
                        'ipv4_precedence',
                        'Cisco-IOS-XR-infra-policymgr-cfg', False, max_elements=8),
                ], max_elements=8),
            _MetaInfoClassMember('ipv6-acl', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Match IPv6 ACL.
                ''',
                'ipv6_acl',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('ipv6-dscp', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'([0-9]|[1-5][0-9]|6[0-3])|(([0-9]|[1-5][0-9]|6[0-3])-([0-9]|[1-5][0-9]|6[0-3]))|(af11)|(af12)|(af13)|(af21)|(af22)|(af23)|(af31)|(af32)|(af33)|(af41)|(af42)|(af43)|(ef)|(default)|(cs1)|(cs2)|(cs3)|(cs4)|(cs5)|(cs6)|(cs7)'], 
                '''                Match IPv6 DSCP.
                ''',
                'ipv6_dscp',
                'Cisco-IOS-XR-infra-policymgr-cfg', False, max_elements=8),
            _MetaInfoClassMember('ipv6-packet-length', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'(\\d+)|(\\d+\\-\\d+)'], 
                '''                Match IPv6 packet length. 
                Should be value 0..65535 or range.
                ''',
                'ipv6_packet_length',
                'Cisco-IOS-XR-infra-policymgr-cfg', False, max_elements=8),
            _MetaInfoClassMember('ipv6-precedence', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Match IPv6 precedence.
                ''',
                'ipv6_precedence',
                'Cisco-IOS-XR-infra-policymgr-cfg', False, [
                    _MetaInfoClassMember('ipv6-precedence', REFERENCE_LEAFLIST, 'int' , None, None, 
                        [('0', '7')], [], 
                        '''                        Match IPv6 precedence.
                        ''',
                        'ipv6_precedence',
                        'Cisco-IOS-XR-infra-policymgr-cfg', False, max_elements=8),
                    _MetaInfoClassMember('ipv6-precedence', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [b'(critical)|(flash)|(flash-override)|(immediate)|(internet)|(network)|(priority)|(routine)'], 
                        '''                        Match IPv6 precedence.
                        ''',
                        'ipv6_precedence',
                        'Cisco-IOS-XR-infra-policymgr-cfg', False, max_elements=8),
                ], max_elements=8),
            _MetaInfoClassMember('mpls-disposition-ipv4-access-list', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Match MPLS Label Disposition IPv4 access list.
                ''',
                'mpls_disposition_ipv4_access_list',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('mpls-disposition-ipv6-access-list', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Match MPLS Label Disposition IPv6 access list.
                ''',
                'mpls_disposition_ipv6_access_list',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('mpls-experimental-imposition', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '7')], [], 
                '''                Match MPLS experimental imposition label.
                ''',
                'mpls_experimental_imposition',
                'Cisco-IOS-XR-infra-policymgr-cfg', False, max_elements=8),
            _MetaInfoClassMember('mpls-experimental-topmost', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '7')], [], 
                '''                Match MPLS experimental topmost label.
                ''',
                'mpls_experimental_topmost',
                'Cisco-IOS-XR-infra-policymgr-cfg', False, max_elements=8),
            _MetaInfoClassMember('packet-length', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'(\\d+)|(\\d+\\-\\d+)'], 
                '''                Match packet length. 
                Should be value 0..65535 or range.
                ''',
                'packet_length',
                'Cisco-IOS-XR-infra-policymgr-cfg', False, max_elements=8),
            _MetaInfoClassMember('precedence', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Match precedence.
                ''',
                'precedence',
                'Cisco-IOS-XR-infra-policymgr-cfg', False, [
                    _MetaInfoClassMember('precedence', REFERENCE_LEAFLIST, 'int' , None, None, 
                        [('0', '7')], [], 
                        '''                        Match precedence.
                        ''',
                        'precedence',
                        'Cisco-IOS-XR-infra-policymgr-cfg', False, max_elements=8),
                    _MetaInfoClassMember('precedence', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [b'(critical)|(flash)|(flash-override)|(immediate)|(internet)|(network)|(priority)|(routine)'], 
                        '''                        Match precedence.
                        ''',
                        'precedence',
                        'Cisco-IOS-XR-infra-policymgr-cfg', False, max_elements=8),
                ], max_elements=8),
            _MetaInfoClassMember('protocol', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])|(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\-([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]))|((ahp)|(dhcpv4)|(dhcpv6)|(eigrp)|(esp)|(gre)|(icmp)|(igmp)|(igrp)|(ipinip)|(ipv4)|(ipv6)|(ipv6icmp)|(mpls)|(nos)|(ospf)|(pcp)|(pim)|(ppp)|(sctp)|(tcp)|(udp))'], 
                '''                Match protocol.
                ''',
                'protocol',
                'Cisco-IOS-XR-infra-policymgr-cfg', False, max_elements=7),
            _MetaInfoClassMember('qos-group', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'(\\d+)|(\\d+\\-\\d+)'], 
                '''                Match QoS group.
                Should be value 0..512 or range.
                ''',
                'qos_group',
                'Cisco-IOS-XR-infra-policymgr-cfg', False, max_elements=8),
            _MetaInfoClassMember('remote-id', REFERENCE_LEAFLIST, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Match remote ID.
                ''',
                'remote_id',
                'Cisco-IOS-XR-infra-policymgr-cfg', False, max_elements=8),
            _MetaInfoClassMember('remote-id-regex', REFERENCE_LEAFLIST, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Match remote id regex.
                ''',
                'remote_id_regex',
                'Cisco-IOS-XR-infra-policymgr-cfg', False, max_elements=8),
            _MetaInfoClassMember('service-name', REFERENCE_LEAFLIST, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Match servicve name.
                ''',
                'service_name',
                'Cisco-IOS-XR-infra-policymgr-cfg', False, max_elements=8),
            _MetaInfoClassMember('service-name-regex', REFERENCE_LEAFLIST, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Match servicve name regular expression.
                ''',
                'service_name_regex',
                'Cisco-IOS-XR-infra-policymgr-cfg', False, max_elements=8),
            _MetaInfoClassMember('source-address-ipv4', REFERENCE_LIST, 'SourceAddressIpv4' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg', 'PolicyManager.ClassMaps.ClassMap.Match.SourceAddressIpv4', 
                [], [], 
                '''                Match source IPv4 address.
                ''',
                'source_address_ipv4',
                'Cisco-IOS-XR-infra-policymgr-cfg', False, max_elements=8),
            _MetaInfoClassMember('source-address-ipv6', REFERENCE_LIST, 'SourceAddressIpv6' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg', 'PolicyManager.ClassMaps.ClassMap.Match.SourceAddressIpv6', 
                [], [], 
                '''                Match source IPv6 address.
                ''',
                'source_address_ipv6',
                'Cisco-IOS-XR-infra-policymgr-cfg', False, max_elements=8),
            _MetaInfoClassMember('source-mac', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                Match source MAC address.
                ''',
                'source_mac',
                'Cisco-IOS-XR-infra-policymgr-cfg', False, max_elements=8),
            _MetaInfoClassMember('source-port', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'(\\d+)|(\\d+\\-\\d+)'], 
                '''                Match source port. 
                Should be value 0..65535 or range.
                ''',
                'source_port',
                'Cisco-IOS-XR-infra-policymgr-cfg', False, max_elements=8),
            _MetaInfoClassMember('tcp-flag', ATTRIBUTE, 'int' , None, None, 
                [('0', '4095')], [], 
                '''                Match TCP flags.
                ''',
                'tcp_flag',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('timer', REFERENCE_LEAFLIST, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Match timer.
                ''',
                'timer',
                'Cisco-IOS-XR-infra-policymgr-cfg', False, max_elements=8),
            _MetaInfoClassMember('timer-regex', REFERENCE_LEAFLIST, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Match timer regular expression.
                ''',
                'timer_regex',
                'Cisco-IOS-XR-infra-policymgr-cfg', False, max_elements=8),
            _MetaInfoClassMember('traffic-class', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'(\\d+)|(\\d+\\-\\d+)'], 
                '''                Match Traffic Class.
                Should be value 0..63 or range.
                ''',
                'traffic_class',
                'Cisco-IOS-XR-infra-policymgr-cfg', False, max_elements=8),
            _MetaInfoClassMember('user-name', REFERENCE_LEAFLIST, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Match user name.
                ''',
                'user_name',
                'Cisco-IOS-XR-infra-policymgr-cfg', False, max_elements=8),
            _MetaInfoClassMember('user-name-regex', REFERENCE_LEAFLIST, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Match user name regular expression.
                ''',
                'user_name_regex',
                'Cisco-IOS-XR-infra-policymgr-cfg', False, max_elements=8),
            _MetaInfoClassMember('vlan', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'(\\d+)|(\\d+\\-\\d+)'], 
                '''                Match VLAN ID.
                ''',
                'vlan',
                'Cisco-IOS-XR-infra-policymgr-cfg', False, max_elements=8),
            _MetaInfoClassMember('vpls-broadcast', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Match VPLS Broadcast
                ''',
                'vpls_broadcast',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('vpls-control', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Match VPLS control
                ''',
                'vpls_control',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('vpls-known', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Match VPLS Known
                ''',
                'vpls_known',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('vpls-multicast', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Match VPLS Multicast
                ''',
                'vpls_multicast',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('vpls-unknown', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Match VPLS Unknown
                ''',
                'vpls_unknown',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            ],
            'Cisco-IOS-XR-infra-policymgr-cfg',
            'match',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-policymgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg'
        ),
    },
    'PolicyManager.ClassMaps.ClassMap.MatchNot.DestinationAddressIpv4' : {
        'meta_info' : _MetaInfoClass('PolicyManager.ClassMaps.ClassMap.MatchNot.DestinationAddressIpv4',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address.
                ''',
                'address',
                'Cisco-IOS-XR-infra-policymgr-cfg', True),
            _MetaInfoClassMember('netmask', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 netmask.
                ''',
                'netmask',
                'Cisco-IOS-XR-infra-policymgr-cfg', True),
            ],
            'Cisco-IOS-XR-infra-policymgr-cfg',
            'destination-address-ipv4',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-policymgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg'
        ),
    },
    'PolicyManager.ClassMaps.ClassMap.MatchNot.DestinationAddressIpv6' : {
        'meta_info' : _MetaInfoClass('PolicyManager.ClassMaps.ClassMap.MatchNot.DestinationAddressIpv6',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address.
                ''',
                'address',
                'Cisco-IOS-XR-infra-policymgr-cfg', True),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '128')], [], 
                '''                IPv6 prefix length.
                ''',
                'prefix_length',
                'Cisco-IOS-XR-infra-policymgr-cfg', True),
            ],
            'Cisco-IOS-XR-infra-policymgr-cfg',
            'destination-address-ipv6',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-policymgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg'
        ),
    },
    'PolicyManager.ClassMaps.ClassMap.MatchNot.SourceAddressIpv4' : {
        'meta_info' : _MetaInfoClass('PolicyManager.ClassMaps.ClassMap.MatchNot.SourceAddressIpv4',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address.
                ''',
                'address',
                'Cisco-IOS-XR-infra-policymgr-cfg', True),
            _MetaInfoClassMember('netmask', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 netmask.
                ''',
                'netmask',
                'Cisco-IOS-XR-infra-policymgr-cfg', True),
            ],
            'Cisco-IOS-XR-infra-policymgr-cfg',
            'source-address-ipv4',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-policymgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg'
        ),
    },
    'PolicyManager.ClassMaps.ClassMap.MatchNot.SourceAddressIpv6' : {
        'meta_info' : _MetaInfoClass('PolicyManager.ClassMaps.ClassMap.MatchNot.SourceAddressIpv6',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address.
                ''',
                'address',
                'Cisco-IOS-XR-infra-policymgr-cfg', True),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '128')], [], 
                '''                IPv6 prefix length.
                ''',
                'prefix_length',
                'Cisco-IOS-XR-infra-policymgr-cfg', True),
            ],
            'Cisco-IOS-XR-infra-policymgr-cfg',
            'source-address-ipv6',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-policymgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg'
        ),
    },
    'PolicyManager.ClassMaps.ClassMap.MatchNot.DomainName' : {
        'meta_info' : _MetaInfoClass('PolicyManager.ClassMaps.ClassMap.MatchNot.DomainName',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Domain name or regular expression.
                ''',
                'name',
                'Cisco-IOS-XR-infra-policymgr-cfg', True),
            _MetaInfoClassMember('format', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Domain-format name.
                ''',
                'format',
                'Cisco-IOS-XR-infra-policymgr-cfg', True),
            ],
            'Cisco-IOS-XR-infra-policymgr-cfg',
            'domain-name',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-policymgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg'
        ),
    },
    'PolicyManager.ClassMaps.ClassMap.MatchNot.DomainNameRegex' : {
        'meta_info' : _MetaInfoClass('PolicyManager.ClassMaps.ClassMap.MatchNot.DomainNameRegex',
            False, 
            [
            _MetaInfoClassMember('regex', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Domain name or regular expression.
                ''',
                'regex',
                'Cisco-IOS-XR-infra-policymgr-cfg', True),
            _MetaInfoClassMember('format', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Domain-format name.
                ''',
                'format',
                'Cisco-IOS-XR-infra-policymgr-cfg', True),
            ],
            'Cisco-IOS-XR-infra-policymgr-cfg',
            'domain-name-regex',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-policymgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg'
        ),
    },
    'PolicyManager.ClassMaps.ClassMap.MatchNot.Flow' : {
        'meta_info' : _MetaInfoClass('PolicyManager.ClassMaps.ClassMap.MatchNot.Flow',
            False, 
            [
            _MetaInfoClassMember('flow-tag', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('1', '63')], [], 
                '''                Configure the flow-tag parameters.
                ''',
                'flow_tag',
                'Cisco-IOS-XR-infra-policymgr-cfg', False, max_elements=2),
            ],
            'Cisco-IOS-XR-infra-policymgr-cfg',
            'flow',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-policymgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg'
        ),
    },
    'PolicyManager.ClassMaps.ClassMap.MatchNot' : {
        'meta_info' : _MetaInfoClass('PolicyManager.ClassMaps.ClassMap.MatchNot',
            False, 
            [
            _MetaInfoClassMember('authen-status', ATTRIBUTE, 'str' , None, None, 
                [], [b'(authenticated)|(unauthenticated)'], 
                '''                Match authentication status.
                ''',
                'authen_status',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('circuit-id', REFERENCE_LEAFLIST, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Match Circuit ID.
                ''',
                'circuit_id',
                'Cisco-IOS-XR-infra-policymgr-cfg', False, max_elements=8),
            _MetaInfoClassMember('circuit-id-regex', REFERENCE_LEAFLIST, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Match Circuit id regex.
                ''',
                'circuit_id_regex',
                'Cisco-IOS-XR-infra-policymgr-cfg', False, max_elements=8),
            _MetaInfoClassMember('cos', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '7')], [], 
                '''                Match CoS.
                ''',
                'cos',
                'Cisco-IOS-XR-infra-policymgr-cfg', False, max_elements=8),
            _MetaInfoClassMember('dei', ATTRIBUTE, 'int' , None, None, 
                [('0', '1')], [], 
                '''                Match DEI bit.
                ''',
                'dei',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('dei-inner', ATTRIBUTE, 'int' , None, None, 
                [('0', '1')], [], 
                '''                Match DEI INNER  bit.
                ''',
                'dei_inner',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('destination-address-ipv4', REFERENCE_LIST, 'DestinationAddressIpv4' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg', 'PolicyManager.ClassMaps.ClassMap.MatchNot.DestinationAddressIpv4', 
                [], [], 
                '''                Match destination IPv4 address.
                ''',
                'destination_address_ipv4',
                'Cisco-IOS-XR-infra-policymgr-cfg', False, max_elements=8),
            _MetaInfoClassMember('destination-address-ipv6', REFERENCE_LIST, 'DestinationAddressIpv6' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg', 'PolicyManager.ClassMaps.ClassMap.MatchNot.DestinationAddressIpv6', 
                [], [], 
                '''                Match destination IPv6 address.
                ''',
                'destination_address_ipv6',
                'Cisco-IOS-XR-infra-policymgr-cfg', False, max_elements=8),
            _MetaInfoClassMember('destination-mac', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                Match destination MAC address.
                ''',
                'destination_mac',
                'Cisco-IOS-XR-infra-policymgr-cfg', False, max_elements=8),
            _MetaInfoClassMember('destination-port', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'(\\d+)|(\\d+\\-\\d+)'], 
                '''                Match destination port. 
                Should be value 0..65535 or range.
                ''',
                'destination_port',
                'Cisco-IOS-XR-infra-policymgr-cfg', False, max_elements=8),
            _MetaInfoClassMember('dhcp-client-id', REFERENCE_LEAFLIST, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Match dhcp client ID.
                ''',
                'dhcp_client_id',
                'Cisco-IOS-XR-infra-policymgr-cfg', False, max_elements=8),
            _MetaInfoClassMember('dhcp-client-id-regex', REFERENCE_LEAFLIST, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Match dhcp client id regex.
                ''',
                'dhcp_client_id_regex',
                'Cisco-IOS-XR-infra-policymgr-cfg', False, max_elements=8),
            _MetaInfoClassMember('discard-class', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '7')], [], 
                '''                Match discard class.
                ''',
                'discard_class',
                'Cisco-IOS-XR-infra-policymgr-cfg', False, max_elements=8),
            _MetaInfoClassMember('domain-name', REFERENCE_LIST, 'DomainName' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg', 'PolicyManager.ClassMaps.ClassMap.MatchNot.DomainName', 
                [], [], 
                '''                Match domain name.
                ''',
                'domain_name',
                'Cisco-IOS-XR-infra-policymgr-cfg', False, max_elements=8),
            _MetaInfoClassMember('domain-name-regex', REFERENCE_LIST, 'DomainNameRegex' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg', 'PolicyManager.ClassMaps.ClassMap.MatchNot.DomainNameRegex', 
                [], [], 
                '''                Match domain name.
                ''',
                'domain_name_regex',
                'Cisco-IOS-XR-infra-policymgr-cfg', False, max_elements=8),
            _MetaInfoClassMember('dscp', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'([0-9]|[1-5][0-9]|6[0-3])|(([0-9]|[1-5][0-9]|6[0-3])-([0-9]|[1-5][0-9]|6[0-3]))|(af11)|(af12)|(af13)|(af21)|(af22)|(af23)|(af31)|(af32)|(af33)|(af41)|(af42)|(af43)|(ef)|(default)|(cs1)|(cs2)|(cs3)|(cs4)|(cs5)|(cs6)|(cs7)'], 
                '''                Match DSCP.
                ''',
                'dscp',
                'Cisco-IOS-XR-infra-policymgr-cfg', False, max_elements=8),
            _MetaInfoClassMember('ethernet-services-acl', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Match Ethernet Services
                ''',
                'ethernet_services_acl',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('ethertype', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'((153[6-9]|15[4-9][0-9]|1[6-9][0-9][0-9]|[2-9][0-9][0-9][0-9])|([1-5][0-9][0-9][0-9][0-9]|6[0-4][0-9][0-9][0-9])|(65[0-4][0-9][0-9]|655[0-2][0-9]|6553[0-5]))|((arp)|(ipv4)|(ipv6))'], 
                '''                Match Ethertype.
                ''',
                'ethertype',
                'Cisco-IOS-XR-infra-policymgr-cfg', False, max_elements=8),
            _MetaInfoClassMember('flow', REFERENCE_CLASS, 'Flow' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg', 'PolicyManager.ClassMaps.ClassMap.MatchNot.Flow', 
                [], [], 
                '''                Match flow.
                ''',
                'flow',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('flow-tag', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'(\\d+)|(\\d+\\-\\d+)'], 
                '''                Match flow-tag. Should be value 1..63 or range.
                ''',
                'flow_tag',
                'Cisco-IOS-XR-infra-policymgr-cfg', False, max_elements=8),
            _MetaInfoClassMember('fr-de', ATTRIBUTE, 'int' , None, None, 
                [('0', '1')], [], 
                '''                Set FrameRelay DE bit.
                ''',
                'fr_de',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('fragment-type', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'(first-fragment)|(is-fragment)|(last-fragment)'], 
                '''                Match fragment type for a packet.
                ''',
                'fragment_type',
                'Cisco-IOS-XR-infra-policymgr-cfg', False, max_elements=3),
            _MetaInfoClassMember('frame-relay-dlci', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'(\\d+)|(\\d+\\-\\d+)'], 
                '''                Match frame-relay DLCI value. 
                Should be value 16..1007 or range.
                ''',
                'frame_relay_dlci',
                'Cisco-IOS-XR-infra-policymgr-cfg', False, max_elements=8),
            _MetaInfoClassMember('icmpv4-code', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'(\\d+)|(\\d+\\-\\d+)'], 
                '''                Match IPv4 ICMP code. 
                Should be value 0..255 or range.
                ''',
                'icmpv4_code',
                'Cisco-IOS-XR-infra-policymgr-cfg', False, max_elements=8),
            _MetaInfoClassMember('icmpv4-type', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'(\\d+)|(\\d+\\-\\d+)'], 
                '''                Match IPv4 ICMP type. 
                Should be value 0..255 or range.
                ''',
                'icmpv4_type',
                'Cisco-IOS-XR-infra-policymgr-cfg', False, max_elements=8),
            _MetaInfoClassMember('icmpv6-code', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'(\\d+)|(\\d+\\-\\d+)'], 
                '''                Match IPv6 ICMP code. 
                Should be value 0..255 or range.
                ''',
                'icmpv6_code',
                'Cisco-IOS-XR-infra-policymgr-cfg', False, max_elements=8),
            _MetaInfoClassMember('icmpv6-type', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'(\\d+)|(\\d+\\-\\d+)'], 
                '''                Match IPv6 ICMP type. 
                Should be value 0..255 or range.
                ''',
                'icmpv6_type',
                'Cisco-IOS-XR-infra-policymgr-cfg', False, max_elements=8),
            _MetaInfoClassMember('inner-cos', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '7')], [], 
                '''                Match inner CoS.
                ''',
                'inner_cos',
                'Cisco-IOS-XR-infra-policymgr-cfg', False, max_elements=8),
            _MetaInfoClassMember('inner-vlan', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'(\\d+)|(\\d+\\-\\d+)'], 
                '''                Match inner VLAN ID.
                ''',
                'inner_vlan',
                'Cisco-IOS-XR-infra-policymgr-cfg', False, max_elements=8),
            _MetaInfoClassMember('ipv4-acl', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Match IPv4 ACL.
                ''',
                'ipv4_acl',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('ipv4-dscp', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'([0-9]|[1-5][0-9]|6[0-3])|(([0-9]|[1-5][0-9]|6[0-3])-([0-9]|[1-5][0-9]|6[0-3]))|(af11)|(af12)|(af13)|(af21)|(af22)|(af23)|(af31)|(af32)|(af33)|(af41)|(af42)|(af43)|(ef)|(default)|(cs1)|(cs2)|(cs3)|(cs4)|(cs5)|(cs6)|(cs7)'], 
                '''                Match IPv4 DSCP.
                ''',
                'ipv4_dscp',
                'Cisco-IOS-XR-infra-policymgr-cfg', False, max_elements=8),
            _MetaInfoClassMember('ipv4-packet-length', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'(\\d+)|(\\d+\\-\\d+)'], 
                '''                Match IPv4 packet length.
                Should be value 0..65535 or range.
                ''',
                'ipv4_packet_length',
                'Cisco-IOS-XR-infra-policymgr-cfg', False, max_elements=8),
            _MetaInfoClassMember('ipv4-precedence', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Match IPv4 precedence.
                ''',
                'ipv4_precedence',
                'Cisco-IOS-XR-infra-policymgr-cfg', False, [
                    _MetaInfoClassMember('ipv4-precedence', REFERENCE_LEAFLIST, 'int' , None, None, 
                        [('0', '7')], [], 
                        '''                        Match IPv4 precedence.
                        ''',
                        'ipv4_precedence',
                        'Cisco-IOS-XR-infra-policymgr-cfg', False, max_elements=8),
                    _MetaInfoClassMember('ipv4-precedence', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [b'(critical)|(flash)|(flash-override)|(immediate)|(internet)|(network)|(priority)|(routine)'], 
                        '''                        Match IPv4 precedence.
                        ''',
                        'ipv4_precedence',
                        'Cisco-IOS-XR-infra-policymgr-cfg', False, max_elements=8),
                ], max_elements=8),
            _MetaInfoClassMember('ipv6-acl', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Match IPv6 ACL.
                ''',
                'ipv6_acl',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('ipv6-dscp', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'([0-9]|[1-5][0-9]|6[0-3])|(([0-9]|[1-5][0-9]|6[0-3])-([0-9]|[1-5][0-9]|6[0-3]))|(af11)|(af12)|(af13)|(af21)|(af22)|(af23)|(af31)|(af32)|(af33)|(af41)|(af42)|(af43)|(ef)|(default)|(cs1)|(cs2)|(cs3)|(cs4)|(cs5)|(cs6)|(cs7)'], 
                '''                Match IPv6 DSCP.
                ''',
                'ipv6_dscp',
                'Cisco-IOS-XR-infra-policymgr-cfg', False, max_elements=8),
            _MetaInfoClassMember('ipv6-packet-length', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'(\\d+)|(\\d+\\-\\d+)'], 
                '''                Match IPv6 packet length. 
                Should be value 0..65535 or range.
                ''',
                'ipv6_packet_length',
                'Cisco-IOS-XR-infra-policymgr-cfg', False, max_elements=8),
            _MetaInfoClassMember('ipv6-precedence', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Match IPv6 precedence.
                ''',
                'ipv6_precedence',
                'Cisco-IOS-XR-infra-policymgr-cfg', False, [
                    _MetaInfoClassMember('ipv6-precedence', REFERENCE_LEAFLIST, 'int' , None, None, 
                        [('0', '7')], [], 
                        '''                        Match IPv6 precedence.
                        ''',
                        'ipv6_precedence',
                        'Cisco-IOS-XR-infra-policymgr-cfg', False, max_elements=8),
                    _MetaInfoClassMember('ipv6-precedence', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [b'(critical)|(flash)|(flash-override)|(immediate)|(internet)|(network)|(priority)|(routine)'], 
                        '''                        Match IPv6 precedence.
                        ''',
                        'ipv6_precedence',
                        'Cisco-IOS-XR-infra-policymgr-cfg', False, max_elements=8),
                ], max_elements=8),
            _MetaInfoClassMember('mpls-disposition-ipv4-access-list', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Match MPLS Label Disposition IPv4 access list.
                ''',
                'mpls_disposition_ipv4_access_list',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('mpls-disposition-ipv6-access-list', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Match MPLS Label Disposition IPv6 access list.
                ''',
                'mpls_disposition_ipv6_access_list',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('mpls-experimental-imposition', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '7')], [], 
                '''                Match MPLS experimental imposition label.
                ''',
                'mpls_experimental_imposition',
                'Cisco-IOS-XR-infra-policymgr-cfg', False, max_elements=8),
            _MetaInfoClassMember('mpls-experimental-topmost', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '7')], [], 
                '''                Match MPLS experimental topmost label.
                ''',
                'mpls_experimental_topmost',
                'Cisco-IOS-XR-infra-policymgr-cfg', False, max_elements=8),
            _MetaInfoClassMember('packet-length', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'(\\d+)|(\\d+\\-\\d+)'], 
                '''                Match packet length. 
                Should be value 0..65535 or range.
                ''',
                'packet_length',
                'Cisco-IOS-XR-infra-policymgr-cfg', False, max_elements=8),
            _MetaInfoClassMember('precedence', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Match precedence.
                ''',
                'precedence',
                'Cisco-IOS-XR-infra-policymgr-cfg', False, [
                    _MetaInfoClassMember('precedence', REFERENCE_LEAFLIST, 'int' , None, None, 
                        [('0', '7')], [], 
                        '''                        Match precedence.
                        ''',
                        'precedence',
                        'Cisco-IOS-XR-infra-policymgr-cfg', False, max_elements=8),
                    _MetaInfoClassMember('precedence', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [b'(critical)|(flash)|(flash-override)|(immediate)|(internet)|(network)|(priority)|(routine)'], 
                        '''                        Match precedence.
                        ''',
                        'precedence',
                        'Cisco-IOS-XR-infra-policymgr-cfg', False, max_elements=8),
                ], max_elements=8),
            _MetaInfoClassMember('protocol', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])|(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\-([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]))|((ahp)|(dhcpv4)|(dhcpv6)|(eigrp)|(esp)|(gre)|(icmp)|(igmp)|(igrp)|(ipinip)|(ipv4)|(ipv6)|(ipv6icmp)|(mpls)|(nos)|(ospf)|(pcp)|(pim)|(ppp)|(sctp)|(tcp)|(udp))'], 
                '''                Match protocol.
                ''',
                'protocol',
                'Cisco-IOS-XR-infra-policymgr-cfg', False, max_elements=7),
            _MetaInfoClassMember('qos-group', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'(\\d+)|(\\d+\\-\\d+)'], 
                '''                Match QoS group.
                Should be value 0..512 or range.
                ''',
                'qos_group',
                'Cisco-IOS-XR-infra-policymgr-cfg', False, max_elements=8),
            _MetaInfoClassMember('remote-id', REFERENCE_LEAFLIST, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Match remote ID.
                ''',
                'remote_id',
                'Cisco-IOS-XR-infra-policymgr-cfg', False, max_elements=8),
            _MetaInfoClassMember('remote-id-regex', REFERENCE_LEAFLIST, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Match remote id regex.
                ''',
                'remote_id_regex',
                'Cisco-IOS-XR-infra-policymgr-cfg', False, max_elements=8),
            _MetaInfoClassMember('service-name', REFERENCE_LEAFLIST, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Match servicve name.
                ''',
                'service_name',
                'Cisco-IOS-XR-infra-policymgr-cfg', False, max_elements=8),
            _MetaInfoClassMember('service-name-regex', REFERENCE_LEAFLIST, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Match servicve name regular expression.
                ''',
                'service_name_regex',
                'Cisco-IOS-XR-infra-policymgr-cfg', False, max_elements=8),
            _MetaInfoClassMember('source-address-ipv4', REFERENCE_LIST, 'SourceAddressIpv4' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg', 'PolicyManager.ClassMaps.ClassMap.MatchNot.SourceAddressIpv4', 
                [], [], 
                '''                Match source IPv4 address.
                ''',
                'source_address_ipv4',
                'Cisco-IOS-XR-infra-policymgr-cfg', False, max_elements=8),
            _MetaInfoClassMember('source-address-ipv6', REFERENCE_LIST, 'SourceAddressIpv6' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg', 'PolicyManager.ClassMaps.ClassMap.MatchNot.SourceAddressIpv6', 
                [], [], 
                '''                Match source IPv6 address.
                ''',
                'source_address_ipv6',
                'Cisco-IOS-XR-infra-policymgr-cfg', False, max_elements=8),
            _MetaInfoClassMember('source-mac', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                Match source MAC address.
                ''',
                'source_mac',
                'Cisco-IOS-XR-infra-policymgr-cfg', False, max_elements=8),
            _MetaInfoClassMember('source-port', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'(\\d+)|(\\d+\\-\\d+)'], 
                '''                Match source port. 
                Should be value 0..65535 or range.
                ''',
                'source_port',
                'Cisco-IOS-XR-infra-policymgr-cfg', False, max_elements=8),
            _MetaInfoClassMember('tcp-flag', ATTRIBUTE, 'int' , None, None, 
                [('0', '4095')], [], 
                '''                Match TCP flags.
                ''',
                'tcp_flag',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('timer', REFERENCE_LEAFLIST, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Match timer.
                ''',
                'timer',
                'Cisco-IOS-XR-infra-policymgr-cfg', False, max_elements=8),
            _MetaInfoClassMember('timer-regex', REFERENCE_LEAFLIST, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Match timer regular expression.
                ''',
                'timer_regex',
                'Cisco-IOS-XR-infra-policymgr-cfg', False, max_elements=8),
            _MetaInfoClassMember('traffic-class', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'(\\d+)|(\\d+\\-\\d+)'], 
                '''                Match Traffic Class.
                Should be value 0..63 or range.
                ''',
                'traffic_class',
                'Cisco-IOS-XR-infra-policymgr-cfg', False, max_elements=8),
            _MetaInfoClassMember('user-name', REFERENCE_LEAFLIST, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Match user name.
                ''',
                'user_name',
                'Cisco-IOS-XR-infra-policymgr-cfg', False, max_elements=8),
            _MetaInfoClassMember('user-name-regex', REFERENCE_LEAFLIST, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Match user name regular expression.
                ''',
                'user_name_regex',
                'Cisco-IOS-XR-infra-policymgr-cfg', False, max_elements=8),
            _MetaInfoClassMember('vlan', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'(\\d+)|(\\d+\\-\\d+)'], 
                '''                Match VLAN ID.
                ''',
                'vlan',
                'Cisco-IOS-XR-infra-policymgr-cfg', False, max_elements=8),
            _MetaInfoClassMember('vpls-broadcast', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Match VPLS Broadcast
                ''',
                'vpls_broadcast',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('vpls-control', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Match VPLS control
                ''',
                'vpls_control',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('vpls-known', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Match VPLS Known
                ''',
                'vpls_known',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('vpls-multicast', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Match VPLS Multicast
                ''',
                'vpls_multicast',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('vpls-unknown', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Match VPLS Unknown
                ''',
                'vpls_unknown',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            ],
            'Cisco-IOS-XR-infra-policymgr-cfg',
            'match-not',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-policymgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg'
        ),
    },
    'PolicyManager.ClassMaps.ClassMap' : {
        'meta_info' : _MetaInfoClass('PolicyManager.ClassMaps.ClassMap',
            False, 
            [
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'ClassMapTypeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg', 'ClassMapTypeEnum', 
                [], [], 
                '''                Type of class-map.
                ''',
                'type',
                'Cisco-IOS-XR-infra-policymgr-cfg', True),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[a-zA-Z0-9][a-zA-Z0-9\\._@$%+#:=<>\\-]{0,62}'], 
                '''                Name of class-map.
                ''',
                'name',
                'Cisco-IOS-XR-infra-policymgr-cfg', True),
            _MetaInfoClassMember('class-map-mode-match-all', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Match any match criteria.
                ''',
                'class_map_mode_match_all',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('class-map-mode-match-any', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Match all match criteria
                ''',
                'class_map_mode_match_any',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Description for this policy-map.
                ''',
                'description',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('match', REFERENCE_CLASS, 'Match' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg', 'PolicyManager.ClassMaps.ClassMap.Match', 
                [], [], 
                '''                Match rules.
                ''',
                'match',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('match-not', REFERENCE_CLASS, 'MatchNot' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg', 'PolicyManager.ClassMaps.ClassMap.MatchNot', 
                [], [], 
                '''                Match not rules.
                ''',
                'match_not',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            ],
            'Cisco-IOS-XR-infra-policymgr-cfg',
            'class-map',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-policymgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg'
        ),
    },
    'PolicyManager.ClassMaps' : {
        'meta_info' : _MetaInfoClass('PolicyManager.ClassMaps',
            False, 
            [
            _MetaInfoClassMember('class-map', REFERENCE_LIST, 'ClassMap' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg', 'PolicyManager.ClassMaps.ClassMap', 
                [], [], 
                '''                Class-map configuration.
                ''',
                'class_map',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            ],
            'Cisco-IOS-XR-infra-policymgr-cfg',
            'class-maps',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-policymgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg'
        ),
    },
    'PolicyManager.PolicyMaps.PolicyMap.Event.Class_.ActionRule.ActivateDynamicTemplate' : {
        'meta_info' : _MetaInfoClass('PolicyManager.PolicyMaps.PolicyMap.Event.Class_.ActionRule.ActivateDynamicTemplate',
            False, 
            [
            _MetaInfoClassMember('aaa-list', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the AAA method list.
                ''',
                'aaa_list',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Dynamic template name.
                ''',
                'name',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            ],
            'Cisco-IOS-XR-infra-policymgr-cfg',
            'activate-dynamic-template',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-policymgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg'
        ),
    },
    'PolicyManager.PolicyMaps.PolicyMap.Event.Class_.ActionRule.Authenticate' : {
        'meta_info' : _MetaInfoClass('PolicyManager.PolicyMaps.PolicyMap.Event.Class_.ActionRule.Authenticate',
            False, 
            [
            _MetaInfoClassMember('aaa-list', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the AAA method list.
                ''',
                'aaa_list',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            ],
            'Cisco-IOS-XR-infra-policymgr-cfg',
            'authenticate',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-policymgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg'
        ),
    },
    'PolicyManager.PolicyMaps.PolicyMap.Event.Class_.ActionRule.Authorize' : {
        'meta_info' : _MetaInfoClass('PolicyManager.PolicyMaps.PolicyMap.Event.Class_.ActionRule.Authorize',
            False, 
            [
            _MetaInfoClassMember('aaa-list', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the AAA method list.
                ''',
                'aaa_list',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('format', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Specify an Authorize format name.
                ''',
                'format',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('identifier', REFERENCE_ENUM_CLASS, 'AuthorizeIdentifierEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg', 'AuthorizeIdentifierEnum', 
                [], [], 
                '''                Specify an Authorize format name.
                ''',
                'identifier',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('password', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Specify a password to be used for AAA
                request.
                ''',
                'password',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            ],
            'Cisco-IOS-XR-infra-policymgr-cfg',
            'authorize',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-policymgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg'
        ),
    },
    'PolicyManager.PolicyMaps.PolicyMap.Event.Class_.ActionRule.DeactivateDynamicTemplate' : {
        'meta_info' : _MetaInfoClass('PolicyManager.PolicyMaps.PolicyMap.Event.Class_.ActionRule.DeactivateDynamicTemplate',
            False, 
            [
            _MetaInfoClassMember('aaa-list', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the AAA method list.
                ''',
                'aaa_list',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Dynamic template name.
                ''',
                'name',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            ],
            'Cisco-IOS-XR-infra-policymgr-cfg',
            'deactivate-dynamic-template',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-policymgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg'
        ),
    },
    'PolicyManager.PolicyMaps.PolicyMap.Event.Class_.ActionRule.SetTimer' : {
        'meta_info' : _MetaInfoClass('PolicyManager.PolicyMaps.PolicyMap.Event.Class_.ActionRule.SetTimer',
            False, 
            [
            _MetaInfoClassMember('timer-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the timer.
                ''',
                'timer_name',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('timer-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Timer value in minutes.
                ''',
                'timer_value',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            ],
            'Cisco-IOS-XR-infra-policymgr-cfg',
            'set-timer',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-policymgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg'
        ),
    },
    'PolicyManager.PolicyMaps.PolicyMap.Event.Class_.ActionRule.StopTimer' : {
        'meta_info' : _MetaInfoClass('PolicyManager.PolicyMaps.PolicyMap.Event.Class_.ActionRule.StopTimer',
            False, 
            [
            _MetaInfoClassMember('timer-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the timer.
                ''',
                'timer_name',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            ],
            'Cisco-IOS-XR-infra-policymgr-cfg',
            'stop-timer',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-policymgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg'
        ),
    },
    'PolicyManager.PolicyMaps.PolicyMap.Event.Class_.ActionRule' : {
        'meta_info' : _MetaInfoClass('PolicyManager.PolicyMaps.PolicyMap.Event.Class_.ActionRule',
            False, 
            [
            _MetaInfoClassMember('action-sequence-number', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Sequence number for this action.
                ''',
                'action_sequence_number',
                'Cisco-IOS-XR-infra-policymgr-cfg', True),
            _MetaInfoClassMember('activate-dynamic-template', REFERENCE_CLASS, 'ActivateDynamicTemplate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg', 'PolicyManager.PolicyMaps.PolicyMap.Event.Class_.ActionRule.ActivateDynamicTemplate', 
                [], [], 
                '''                Activate dynamic templates.
                ''',
                'activate_dynamic_template',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('authenticate', REFERENCE_CLASS, 'Authenticate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg', 'PolicyManager.PolicyMaps.PolicyMap.Event.Class_.ActionRule.Authenticate', 
                [], [], 
                '''                Authentication related configuration.
                ''',
                'authenticate',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('authorize', REFERENCE_CLASS, 'Authorize' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg', 'PolicyManager.PolicyMaps.PolicyMap.Event.Class_.ActionRule.Authorize', 
                [], [], 
                '''                Authorize.
                ''',
                'authorize',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('deactivate-dynamic-template', REFERENCE_CLASS, 'DeactivateDynamicTemplate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg', 'PolicyManager.PolicyMaps.PolicyMap.Event.Class_.ActionRule.DeactivateDynamicTemplate', 
                [], [], 
                '''                Deactivate dynamic templates.
                ''',
                'deactivate_dynamic_template',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('disconnect', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disconnect session.
                ''',
                'disconnect',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('monitor', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Monitor session.
                ''',
                'monitor',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('set-timer', REFERENCE_CLASS, 'SetTimer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg', 'PolicyManager.PolicyMaps.PolicyMap.Event.Class_.ActionRule.SetTimer', 
                [], [], 
                '''                Set a timer to execute a rule on its 
                expiry
                ''',
                'set_timer',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('stop-timer', REFERENCE_CLASS, 'StopTimer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg', 'PolicyManager.PolicyMaps.PolicyMap.Event.Class_.ActionRule.StopTimer', 
                [], [], 
                '''                Disable timer before it expires.
                ''',
                'stop_timer',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            ],
            'Cisco-IOS-XR-infra-policymgr-cfg',
            'action-rule',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-policymgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg'
        ),
    },
    'PolicyManager.PolicyMaps.PolicyMap.Event.Class_' : {
        'meta_info' : _MetaInfoClass('PolicyManager.PolicyMaps.PolicyMap.Event.Class_',
            False, 
            [
            _MetaInfoClassMember('class-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[a-zA-Z0-9][a-zA-Z0-9\\._@$%+#:=<>\\-]{0,62}'], 
                '''                Name of class.
                ''',
                'class_name',
                'Cisco-IOS-XR-infra-policymgr-cfg', True),
            _MetaInfoClassMember('class-type', REFERENCE_ENUM_CLASS, 'PmapClassMapTypeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg', 'PmapClassMapTypeEnum', 
                [], [], 
                '''                Type of class.
                ''',
                'class_type',
                'Cisco-IOS-XR-infra-policymgr-cfg', True),
            _MetaInfoClassMember('action-rule', REFERENCE_LIST, 'ActionRule' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg', 'PolicyManager.PolicyMaps.PolicyMap.Event.Class_.ActionRule', 
                [], [], 
                '''                Action rule.
                ''',
                'action_rule',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('class-execution-strategy', REFERENCE_ENUM_CLASS, 'ExecutionStrategyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg', 'ExecutionStrategyEnum', 
                [], [], 
                '''                Class execution strategy.
                ''',
                'class_execution_strategy',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            ],
            'Cisco-IOS-XR-infra-policymgr-cfg',
            'class',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-policymgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg'
        ),
    },
    'PolicyManager.PolicyMaps.PolicyMap.Event' : {
        'meta_info' : _MetaInfoClass('PolicyManager.PolicyMaps.PolicyMap.Event',
            False, 
            [
            _MetaInfoClassMember('event-type', REFERENCE_ENUM_CLASS, 'EventTypeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg', 'EventTypeEnum', 
                [], [], 
                '''                Event type.
                ''',
                'event_type',
                'Cisco-IOS-XR-infra-policymgr-cfg', True),
            _MetaInfoClassMember('class', REFERENCE_LIST, 'Class_' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg', 'PolicyManager.PolicyMaps.PolicyMap.Event.Class_', 
                [], [], 
                '''                Class-map rule.
                ''',
                'class_',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('event-mode-match-all', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Execute all the matched classes.
                ''',
                'event_mode_match_all',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('event-mode-match-first', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Execute only the first matched class.
                ''',
                'event_mode_match_first',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            ],
            'Cisco-IOS-XR-infra-policymgr-cfg',
            'event',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-policymgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg'
        ),
    },
    'PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Shape.Rate' : {
        'meta_info' : _MetaInfoClass('PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Shape.Rate',
            False, 
            [
            _MetaInfoClassMember('unit', ATTRIBUTE, 'str' , None, None, 
                [], [b'(bps)|(kbps)|(mbps)|(gbps)|(percent)|(per-million)|(per-thousand)'], 
                '''                Shape bandwidth units.
                ''',
                'unit',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Shape bandwidth value.
                ''',
                'value',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            ],
            'Cisco-IOS-XR-infra-policymgr-cfg',
            'rate',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-policymgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg'
        ),
    },
    'PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Shape.Burst' : {
        'meta_info' : _MetaInfoClass('PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Shape.Burst',
            False, 
            [
            _MetaInfoClassMember('units', ATTRIBUTE, 'str' , None, None, 
                [], [b'(bytes)|(kbytes)|(mbytes)|(gbytes)|(us)|(ms)|(packets)|(cells)'], 
                '''                Burst size units.
                ''',
                'units',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Burst size value.
                ''',
                'value',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            ],
            'Cisco-IOS-XR-infra-policymgr-cfg',
            'burst',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-policymgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg'
        ),
    },
    'PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Shape' : {
        'meta_info' : _MetaInfoClass('PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Shape',
            False, 
            [
            _MetaInfoClassMember('burst', REFERENCE_CLASS, 'Burst' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg', 'PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Shape.Burst', 
                [], [], 
                '''                Burst size configuration.
                ''',
                'burst',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('rate', REFERENCE_CLASS, 'Rate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg', 'PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Shape.Rate', 
                [], [], 
                '''                Rate configuration.
                ''',
                'rate',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            ],
            'Cisco-IOS-XR-infra-policymgr-cfg',
            'shape',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-policymgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg'
        ),
    },
    'PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.MinBandwidth' : {
        'meta_info' : _MetaInfoClass('PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.MinBandwidth',
            False, 
            [
            _MetaInfoClassMember('unit', ATTRIBUTE, 'str' , None, None, 
                [], [b'(bps)|(kbps)|(mbps)|(gbps)|(percent)|(per-million)|(per-thousand)'], 
                '''                Minimum bandwidth units.
                ''',
                'unit',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Minimum bandwidth value.
                ''',
                'value',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            ],
            'Cisco-IOS-XR-infra-policymgr-cfg',
            'min-bandwidth',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-policymgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg'
        ),
    },
    'PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.BandwidthRemaining' : {
        'meta_info' : _MetaInfoClass('PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.BandwidthRemaining',
            False, 
            [
            _MetaInfoClassMember('unit', ATTRIBUTE, 'str' , None, None, 
                [], [b'(percent)|(ratio)'], 
                '''                Remaining bandwidth units.
                ''',
                'unit',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Remaining bandwidth value.
                ''',
                'value',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            ],
            'Cisco-IOS-XR-infra-policymgr-cfg',
            'bandwidth-remaining',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-policymgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg'
        ),
    },
    'PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.QueueLimit' : {
        'meta_info' : _MetaInfoClass('PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.QueueLimit',
            False, 
            [
            _MetaInfoClassMember('unit', ATTRIBUTE, 'str' , None, None, 
                [], [b'(bytes)|(kbytes)|(mbytes)|(gbytes)|(us)|(ms)|(packets)|(cells)|(percent)'], 
                '''                Remaining bandwidth units.
                ''',
                'unit',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Remaining bandwidth value.
                ''',
                'value',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            ],
            'Cisco-IOS-XR-infra-policymgr-cfg',
            'queue-limit',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-policymgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg'
        ),
    },
    'PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Pfc.PfcBufferSize' : {
        'meta_info' : _MetaInfoClass('PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Pfc.PfcBufferSize',
            False, 
            [
            _MetaInfoClassMember('unit', ATTRIBUTE, 'str' , None, None, 
                [], [b'(bytes)|(kbytes)|(mbytes)|(gbytes)|(us)|(ms)|(packets)|(cells)'], 
                '''                Pfc buffer size units.
                ''',
                'unit',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Pfc buffer size value.
                ''',
                'value',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            ],
            'Cisco-IOS-XR-infra-policymgr-cfg',
            'pfc-buffer-size',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-policymgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg'
        ),
    },
    'PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Pfc.PfcPauseThreshold' : {
        'meta_info' : _MetaInfoClass('PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Pfc.PfcPauseThreshold',
            False, 
            [
            _MetaInfoClassMember('unit', ATTRIBUTE, 'str' , None, None, 
                [], [b'(bytes)|(kbytes)|(mbytes)|(gbytes)|(us)|(ms)|(packets)|(cells)'], 
                '''                Pfc pause threshold units.
                ''',
                'unit',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Pfc pause threshold value.
                ''',
                'value',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            ],
            'Cisco-IOS-XR-infra-policymgr-cfg',
            'pfc-pause-threshold',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-policymgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg'
        ),
    },
    'PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Pfc.PfcResumeThreshold' : {
        'meta_info' : _MetaInfoClass('PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Pfc.PfcResumeThreshold',
            False, 
            [
            _MetaInfoClassMember('unit', ATTRIBUTE, 'str' , None, None, 
                [], [b'(bytes)|(kbytes)|(mbytes)|(gbytes)|(us)|(ms)|(packets)|(cells)'], 
                '''                Pfc resume threshold units.
                ''',
                'unit',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Pfc resume threshold value.
                ''',
                'value',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            ],
            'Cisco-IOS-XR-infra-policymgr-cfg',
            'pfc-resume-threshold',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-policymgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg'
        ),
    },
    'PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Pfc' : {
        'meta_info' : _MetaInfoClass('PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Pfc',
            False, 
            [
            _MetaInfoClassMember('pfc-buffer-size', REFERENCE_CLASS, 'PfcBufferSize' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg', 'PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Pfc.PfcBufferSize', 
                [], [], 
                '''                ''',
                'pfc_buffer_size',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('pfc-pause-set', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Pfc Pause set value.
                ''',
                'pfc_pause_set',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('pfc-pause-threshold', REFERENCE_CLASS, 'PfcPauseThreshold' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg', 'PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Pfc.PfcPauseThreshold', 
                [], [], 
                '''                ''',
                'pfc_pause_threshold',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('pfc-resume-threshold', REFERENCE_CLASS, 'PfcResumeThreshold' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg', 'PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Pfc.PfcResumeThreshold', 
                [], [], 
                '''                ''',
                'pfc_resume_threshold',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            ],
            'Cisco-IOS-XR-infra-policymgr-cfg',
            'pfc',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-policymgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg'
        ),
    },
    'PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.RandomDetect' : {
        'meta_info' : _MetaInfoClass('PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.RandomDetect',
            False, 
            [
            _MetaInfoClassMember('threshold-min-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Minimum RED threshold value.
                ''',
                'threshold_min_value',
                'Cisco-IOS-XR-infra-policymgr-cfg', True),
            _MetaInfoClassMember('threshold-min-units', ATTRIBUTE, 'str' , None, None, 
                [], [b'(bytes)|(kbytes)|(mbytes)|(gbytes)|(us)|(ms)|(packets)|(cells)'], 
                '''                Minimum RED threshold units.
                ''',
                'threshold_min_units',
                'Cisco-IOS-XR-infra-policymgr-cfg', True),
            _MetaInfoClassMember('threshold-max-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum RED threshold value.
                ''',
                'threshold_max_value',
                'Cisco-IOS-XR-infra-policymgr-cfg', True),
            _MetaInfoClassMember('threshold-max-units', ATTRIBUTE, 'str' , None, None, 
                [], [b'(bytes)|(kbytes)|(mbytes)|(gbytes)|(us)|(ms)|(packets)|(cells)'], 
                '''                Maximum RED threshold units.
                ''',
                'threshold_max_units',
                'Cisco-IOS-XR-infra-policymgr-cfg', True),
            _MetaInfoClassMember('cos', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'([0-9]|[1-5][0-9]|6[0-3])|(([0-9]|[1-5][0-9]|6[0-3])-([0-9]|[1-5][0-9]|6[0-3]))|(af11)|(af12)|(af13)|(af21)|(af22)|(af23)|(af31)|(af32)|(af33)|(af41)|(af42)|(af43)|(ef)|(default)|(cs1)|(cs2)|(cs3)|(cs4)|(cs5)|(cs6)|(cs7)'], 
                '''                WRED based on CoS.
                ''',
                'cos',
                'Cisco-IOS-XR-infra-policymgr-cfg', False, max_elements=8),
            _MetaInfoClassMember('dei', ATTRIBUTE, 'int' , None, None, 
                [('0', '1')], [], 
                '''                DEI based WRED.
                ''',
                'dei',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('discard-class', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '7')], [], 
                '''                WRED based on discard class.
                ''',
                'discard_class',
                'Cisco-IOS-XR-infra-policymgr-cfg', False, max_elements=8),
            _MetaInfoClassMember('dscp', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'([0-9]|[1-5][0-9]|6[0-3])|(([0-9]|[1-5][0-9]|6[0-3])-([0-9]|[1-5][0-9]|6[0-3]))|(af11)|(af12)|(af13)|(af21)|(af22)|(af23)|(af31)|(af32)|(af33)|(af41)|(af42)|(af43)|(ef)|(default)|(cs1)|(cs2)|(cs3)|(cs4)|(cs5)|(cs6)|(cs7)'], 
                '''                WRED based on DSCP.
                ''',
                'dscp',
                'Cisco-IOS-XR-infra-policymgr-cfg', False, max_elements=8),
            _MetaInfoClassMember('ecn', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                ECN based WRED.
                ''',
                'ecn',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('mpls-exp', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '7')], [], 
                '''                MPLS Experimental value based WRED.
                ''',
                'mpls_exp',
                'Cisco-IOS-XR-infra-policymgr-cfg', False, max_elements=8),
            _MetaInfoClassMember('precedence', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                WRED based on precedence.
                ''',
                'precedence',
                'Cisco-IOS-XR-infra-policymgr-cfg', False, [
                    _MetaInfoClassMember('precedence', REFERENCE_LEAFLIST, 'int' , None, None, 
                        [('0', '7')], [], 
                        '''                        WRED based on precedence.
                        ''',
                        'precedence',
                        'Cisco-IOS-XR-infra-policymgr-cfg', False, max_elements=8),
                    _MetaInfoClassMember('precedence', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [b'(critical)|(flash)|(flash-override)|(immediate)|(internet)|(network)|(priority)|(routine)'], 
                        '''                        WRED based on precedence.
                        ''',
                        'precedence',
                        'Cisco-IOS-XR-infra-policymgr-cfg', False, max_elements=8),
                ], max_elements=8),
            ],
            'Cisco-IOS-XR-infra-policymgr-cfg',
            'random-detect',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-policymgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg'
        ),
    },
    'PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Set' : {
        'meta_info' : _MetaInfoClass('PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Set',
            False, 
            [
            _MetaInfoClassMember('cos', ATTRIBUTE, 'int' , None, None, 
                [('0', '7')], [], 
                '''                Sets the specific IEEE 802.1Q Layer 2 CoS value of an
                outgoing packet.
                This command should be used by a router if a user wants
                to mark a packet that is being sent to a switch. 
                Switches can leverage Layer 2 header information, 
                including a CoS value marking. Packets entering an 
                interface cannot be set with a CoS value.
                ''',
                'cos',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('dei', ATTRIBUTE, 'int' , None, None, 
                [('0', '1')], [], 
                '''                Set DEI bit.
                ''',
                'dei',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('dei-imposition', ATTRIBUTE, 'int' , None, None, 
                [('0', '1')], [], 
                '''                Set DEI imposition bit.
                ''',
                'dei_imposition',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('destination-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Destination IPv4 address.
                ''',
                'destination_address',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('df', ATTRIBUTE, 'int' , None, None, 
                [('0', '1')], [], 
                '''                Set DF bit.
                ''',
                'df',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('discard-class', ATTRIBUTE, 'int' , None, None, 
                [('0', '7')], [], 
                '''                Sets the discard class on IPv4 or MPLS packets.
                The discard-class can be used only in service policies 
                that are attached in the ingress policy.
                ''',
                'discard_class',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('dscp', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9]|[1-5][0-9]|6[0-3])|(af11)|(af12)|(af13)|(af21)|(af22)|(af23)|(af31)|(af32)|(af33)|(af41)|(af42)|(af43)|(ef)|(default)|(cs1)|(cs2)|(cs3)|(cs4)|(cs5)|(cs6)|(cs7)'], 
                '''                Marks a packet by setting the DSCP in the ToS byte.
                ''',
                'dscp',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('forward-class', ATTRIBUTE, 'int' , None, None, 
                [('0', '7')], [], 
                '''                Sets the discard class.
                ''',
                'forward_class',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('fr-de', ATTRIBUTE, 'int' , None, None, 
                [('0', '1')], [], 
                '''                Set FrameRelay DE bit.
                ''',
                'fr_de',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('inner-cos', ATTRIBUTE, 'int' , None, None, 
                [('0', '7')], [], 
                '''                Set inner cos.
                ''',
                'inner_cos',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('mpls-experimental-imposition', ATTRIBUTE, 'int' , None, None, 
                [('0', '7')], [], 
                '''                Sets the experimental value of the MPLS packet 
                imposition labels.
                Imposition can be used only in service policies that 
                are attached in the ingress policy
                ''',
                'mpls_experimental_imposition',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('mpls-experimental-top-most', ATTRIBUTE, 'int' , None, None, 
                [('0', '7')], [], 
                '''                Sets the experimental value of the MPLS packet top-most
                labels.
                ''',
                'mpls_experimental_top_most',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('precedence', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Sets the precedence value in the IP header.
                ''',
                'precedence',
                'Cisco-IOS-XR-infra-policymgr-cfg', False, [
                    _MetaInfoClassMember('precedence', ATTRIBUTE, 'int' , None, None, 
                        [('0', '7')], [], 
                        '''                        Sets the precedence value in the IP header.
                        ''',
                        'precedence',
                        'Cisco-IOS-XR-infra-policymgr-cfg', False),
                    _MetaInfoClassMember('precedence', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(critical)|(flash)|(flash-override)|(immediate)|(internet)|(network)|(priority)|(routine)'], 
                        '''                        Sets the precedence value in the IP header.
                        ''',
                        'precedence',
                        'Cisco-IOS-XR-infra-policymgr-cfg', False),
                ]),
            _MetaInfoClassMember('precedence-tunnel', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Sets the precedence tunnel value for ipsec.
                ''',
                'precedence_tunnel',
                'Cisco-IOS-XR-infra-policymgr-cfg', False, [
                    _MetaInfoClassMember('precedence-tunnel', ATTRIBUTE, 'int' , None, None, 
                        [('0', '7')], [], 
                        '''                        Sets the precedence tunnel value for ipsec.
                        ''',
                        'precedence_tunnel',
                        'Cisco-IOS-XR-infra-policymgr-cfg', False),
                    _MetaInfoClassMember('precedence-tunnel', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(critical)|(flash)|(flash-override)|(immediate)|(internet)|(network)|(priority)|(routine)'], 
                        '''                        Sets the precedence tunnel value for ipsec.
                        ''',
                        'precedence_tunnel',
                        'Cisco-IOS-XR-infra-policymgr-cfg', False),
                ]),
            _MetaInfoClassMember('qos-group', ATTRIBUTE, 'int' , None, None, 
                [('0', '512')], [], 
                '''                Sets the QoS group identifiers on IPv4 or MPLS packets.
                The set qos-group is supported only on an ingress policy.
                ''',
                'qos_group',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Source IPv4 address.
                ''',
                'source_address',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('srp-priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '7')], [], 
                '''                Sets the spatial reuse protocol priority value of an 
                outgoing packet.
                ''',
                'srp_priority',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('traffic-class', ATTRIBUTE, 'int' , None, None, 
                [('0', '63')], [], 
                '''                Sets the Traffic class identifiers on IPv4 or MPLS packets.
                ''',
                'traffic_class',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            ],
            'Cisco-IOS-XR-infra-policymgr-cfg',
            'set',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-policymgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg'
        ),
    },
    'PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.Rate' : {
        'meta_info' : _MetaInfoClass('PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.Rate',
            False, 
            [
            _MetaInfoClassMember('units', ATTRIBUTE, 'str' , None, None, 
                [], [b'(bps)|(kbps)|(mbps)|(gbps)|(pps)|(percent)|(cellsps)'], 
                '''                Rate units.
                ''',
                'units',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Rate value.
                ''',
                'value',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            ],
            'Cisco-IOS-XR-infra-policymgr-cfg',
            'rate',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-policymgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg'
        ),
    },
    'PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.PeakRate' : {
        'meta_info' : _MetaInfoClass('PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.PeakRate',
            False, 
            [
            _MetaInfoClassMember('units', ATTRIBUTE, 'str' , None, None, 
                [], [b'(bps)|(kbps)|(mbps)|(gbps)|(pps)|(percent)|(cellsps)'], 
                '''                Peak rate units.
                ''',
                'units',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Peak rate value.
                ''',
                'value',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            ],
            'Cisco-IOS-XR-infra-policymgr-cfg',
            'peak-rate',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-policymgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg'
        ),
    },
    'PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.Burst' : {
        'meta_info' : _MetaInfoClass('PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.Burst',
            False, 
            [
            _MetaInfoClassMember('units', ATTRIBUTE, 'str' , None, None, 
                [], [b'(bytes)|(kbytes)|(mbytes)|(gbytes)|(us)|(ms)|(packets)|(cells)'], 
                '''                Burst units.
                ''',
                'units',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Burst value.
                ''',
                'value',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            ],
            'Cisco-IOS-XR-infra-policymgr-cfg',
            'burst',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-policymgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg'
        ),
    },
    'PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.PeakBurst' : {
        'meta_info' : _MetaInfoClass('PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.PeakBurst',
            False, 
            [
            _MetaInfoClassMember('units', ATTRIBUTE, 'str' , None, None, 
                [], [b'(bytes)|(kbytes)|(mbytes)|(gbytes)|(us)|(ms)|(packets)|(cells)'], 
                '''                Peak burst units.
                ''',
                'units',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Peak burst value.
                ''',
                'value',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            ],
            'Cisco-IOS-XR-infra-policymgr-cfg',
            'peak-burst',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-policymgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg'
        ),
    },
    'PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ConformAction.Set' : {
        'meta_info' : _MetaInfoClass('PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ConformAction.Set',
            False, 
            [
            _MetaInfoClassMember('cos', ATTRIBUTE, 'int' , None, None, 
                [('0', '7')], [], 
                '''                Sets the specific IEEE 802.1Q Layer 2 CoS value of an
                outgoing packet.
                This command should be used by a router if a user wants
                to mark a packet that is being sent to a switch. 
                Switches can leverage Layer 2 header information, 
                including a CoS value marking. Packets entering an 
                interface cannot be set with a CoS value.
                ''',
                'cos',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('dei', ATTRIBUTE, 'int' , None, None, 
                [('0', '1')], [], 
                '''                Set DEI bit.
                ''',
                'dei',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('dei-imposition', ATTRIBUTE, 'int' , None, None, 
                [('0', '1')], [], 
                '''                Set DEI imposition bit.
                ''',
                'dei_imposition',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('destination-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Destination IPv4 address.
                ''',
                'destination_address',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('df', ATTRIBUTE, 'int' , None, None, 
                [('0', '1')], [], 
                '''                Set DF bit.
                ''',
                'df',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('discard-class', ATTRIBUTE, 'int' , None, None, 
                [('0', '7')], [], 
                '''                Sets the discard class on IPv4 or MPLS packets.
                The discard-class can be used only in service policies 
                that are attached in the ingress policy.
                ''',
                'discard_class',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('dscp', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9]|[1-5][0-9]|6[0-3])|(af11)|(af12)|(af13)|(af21)|(af22)|(af23)|(af31)|(af32)|(af33)|(af41)|(af42)|(af43)|(ef)|(default)|(cs1)|(cs2)|(cs3)|(cs4)|(cs5)|(cs6)|(cs7)'], 
                '''                Marks a packet by setting the DSCP in the ToS byte.
                ''',
                'dscp',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('forward-class', ATTRIBUTE, 'int' , None, None, 
                [('0', '7')], [], 
                '''                Sets the discard class.
                ''',
                'forward_class',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('fr-de', ATTRIBUTE, 'int' , None, None, 
                [('0', '1')], [], 
                '''                Set FrameRelay DE bit.
                ''',
                'fr_de',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('inner-cos', ATTRIBUTE, 'int' , None, None, 
                [('0', '7')], [], 
                '''                Set inner cos.
                ''',
                'inner_cos',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('mpls-experimental-imposition', ATTRIBUTE, 'int' , None, None, 
                [('0', '7')], [], 
                '''                Sets the experimental value of the MPLS packet 
                imposition labels.
                Imposition can be used only in service policies that 
                are attached in the ingress policy
                ''',
                'mpls_experimental_imposition',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('mpls-experimental-top-most', ATTRIBUTE, 'int' , None, None, 
                [('0', '7')], [], 
                '''                Sets the experimental value of the MPLS packet top-most
                labels.
                ''',
                'mpls_experimental_top_most',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('precedence', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Sets the precedence value in the IP header.
                ''',
                'precedence',
                'Cisco-IOS-XR-infra-policymgr-cfg', False, [
                    _MetaInfoClassMember('precedence', ATTRIBUTE, 'int' , None, None, 
                        [('0', '7')], [], 
                        '''                        Sets the precedence value in the IP header.
                        ''',
                        'precedence',
                        'Cisco-IOS-XR-infra-policymgr-cfg', False),
                    _MetaInfoClassMember('precedence', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(critical)|(flash)|(flash-override)|(immediate)|(internet)|(network)|(priority)|(routine)'], 
                        '''                        Sets the precedence value in the IP header.
                        ''',
                        'precedence',
                        'Cisco-IOS-XR-infra-policymgr-cfg', False),
                ]),
            _MetaInfoClassMember('precedence-tunnel', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Sets the precedence tunnel value for ipsec.
                ''',
                'precedence_tunnel',
                'Cisco-IOS-XR-infra-policymgr-cfg', False, [
                    _MetaInfoClassMember('precedence-tunnel', ATTRIBUTE, 'int' , None, None, 
                        [('0', '7')], [], 
                        '''                        Sets the precedence tunnel value for ipsec.
                        ''',
                        'precedence_tunnel',
                        'Cisco-IOS-XR-infra-policymgr-cfg', False),
                    _MetaInfoClassMember('precedence-tunnel', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(critical)|(flash)|(flash-override)|(immediate)|(internet)|(network)|(priority)|(routine)'], 
                        '''                        Sets the precedence tunnel value for ipsec.
                        ''',
                        'precedence_tunnel',
                        'Cisco-IOS-XR-infra-policymgr-cfg', False),
                ]),
            _MetaInfoClassMember('qos-group', ATTRIBUTE, 'int' , None, None, 
                [('0', '512')], [], 
                '''                Sets the QoS group identifiers on IPv4 or MPLS packets.
                The set qos-group is supported only on an ingress policy.
                ''',
                'qos_group',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Source IPv4 address.
                ''',
                'source_address',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('srp-priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '7')], [], 
                '''                Sets the spatial reuse protocol priority value of an 
                outgoing packet.
                ''',
                'srp_priority',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('traffic-class', ATTRIBUTE, 'int' , None, None, 
                [('0', '63')], [], 
                '''                Sets the Traffic class identifiers on IPv4 or MPLS packets.
                ''',
                'traffic_class',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            ],
            'Cisco-IOS-XR-infra-policymgr-cfg',
            'set',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-policymgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg'
        ),
    },
    'PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ConformAction' : {
        'meta_info' : _MetaInfoClass('PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ConformAction',
            False, 
            [
            _MetaInfoClassMember('drop', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Police action drop.
                ''',
                'drop',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('set', REFERENCE_CLASS, 'Set' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg', 'PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ConformAction.Set', 
                [], [], 
                '''                Police action packet marking.
                ''',
                'set',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('Transmit', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Police action transmit.
                ''',
                'transmit',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            ],
            'Cisco-IOS-XR-infra-policymgr-cfg',
            'conform-action',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-policymgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg'
        ),
    },
    'PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ExceedAction.Set' : {
        'meta_info' : _MetaInfoClass('PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ExceedAction.Set',
            False, 
            [
            _MetaInfoClassMember('cos', ATTRIBUTE, 'int' , None, None, 
                [('0', '7')], [], 
                '''                Sets the specific IEEE 802.1Q Layer 2 CoS value of an
                outgoing packet.
                This command should be used by a router if a user wants
                to mark a packet that is being sent to a switch. 
                Switches can leverage Layer 2 header information, 
                including a CoS value marking. Packets entering an 
                interface cannot be set with a CoS value.
                ''',
                'cos',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('dei', ATTRIBUTE, 'int' , None, None, 
                [('0', '1')], [], 
                '''                Set DEI bit.
                ''',
                'dei',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('dei-imposition', ATTRIBUTE, 'int' , None, None, 
                [('0', '1')], [], 
                '''                Set DEI imposition bit.
                ''',
                'dei_imposition',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('destination-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Destination IPv4 address.
                ''',
                'destination_address',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('df', ATTRIBUTE, 'int' , None, None, 
                [('0', '1')], [], 
                '''                Set DF bit.
                ''',
                'df',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('discard-class', ATTRIBUTE, 'int' , None, None, 
                [('0', '7')], [], 
                '''                Sets the discard class on IPv4 or MPLS packets.
                The discard-class can be used only in service policies 
                that are attached in the ingress policy.
                ''',
                'discard_class',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('dscp', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9]|[1-5][0-9]|6[0-3])|(af11)|(af12)|(af13)|(af21)|(af22)|(af23)|(af31)|(af32)|(af33)|(af41)|(af42)|(af43)|(ef)|(default)|(cs1)|(cs2)|(cs3)|(cs4)|(cs5)|(cs6)|(cs7)'], 
                '''                Marks a packet by setting the DSCP in the ToS byte.
                ''',
                'dscp',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('forward-class', ATTRIBUTE, 'int' , None, None, 
                [('0', '7')], [], 
                '''                Sets the discard class.
                ''',
                'forward_class',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('fr-de', ATTRIBUTE, 'int' , None, None, 
                [('0', '1')], [], 
                '''                Set FrameRelay DE bit.
                ''',
                'fr_de',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('inner-cos', ATTRIBUTE, 'int' , None, None, 
                [('0', '7')], [], 
                '''                Set inner cos.
                ''',
                'inner_cos',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('mpls-experimental-imposition', ATTRIBUTE, 'int' , None, None, 
                [('0', '7')], [], 
                '''                Sets the experimental value of the MPLS packet 
                imposition labels.
                Imposition can be used only in service policies that 
                are attached in the ingress policy
                ''',
                'mpls_experimental_imposition',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('mpls-experimental-top-most', ATTRIBUTE, 'int' , None, None, 
                [('0', '7')], [], 
                '''                Sets the experimental value of the MPLS packet top-most
                labels.
                ''',
                'mpls_experimental_top_most',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('precedence', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Sets the precedence value in the IP header.
                ''',
                'precedence',
                'Cisco-IOS-XR-infra-policymgr-cfg', False, [
                    _MetaInfoClassMember('precedence', ATTRIBUTE, 'int' , None, None, 
                        [('0', '7')], [], 
                        '''                        Sets the precedence value in the IP header.
                        ''',
                        'precedence',
                        'Cisco-IOS-XR-infra-policymgr-cfg', False),
                    _MetaInfoClassMember('precedence', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(critical)|(flash)|(flash-override)|(immediate)|(internet)|(network)|(priority)|(routine)'], 
                        '''                        Sets the precedence value in the IP header.
                        ''',
                        'precedence',
                        'Cisco-IOS-XR-infra-policymgr-cfg', False),
                ]),
            _MetaInfoClassMember('precedence-tunnel', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Sets the precedence tunnel value for ipsec.
                ''',
                'precedence_tunnel',
                'Cisco-IOS-XR-infra-policymgr-cfg', False, [
                    _MetaInfoClassMember('precedence-tunnel', ATTRIBUTE, 'int' , None, None, 
                        [('0', '7')], [], 
                        '''                        Sets the precedence tunnel value for ipsec.
                        ''',
                        'precedence_tunnel',
                        'Cisco-IOS-XR-infra-policymgr-cfg', False),
                    _MetaInfoClassMember('precedence-tunnel', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(critical)|(flash)|(flash-override)|(immediate)|(internet)|(network)|(priority)|(routine)'], 
                        '''                        Sets the precedence tunnel value for ipsec.
                        ''',
                        'precedence_tunnel',
                        'Cisco-IOS-XR-infra-policymgr-cfg', False),
                ]),
            _MetaInfoClassMember('qos-group', ATTRIBUTE, 'int' , None, None, 
                [('0', '512')], [], 
                '''                Sets the QoS group identifiers on IPv4 or MPLS packets.
                The set qos-group is supported only on an ingress policy.
                ''',
                'qos_group',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Source IPv4 address.
                ''',
                'source_address',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('srp-priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '7')], [], 
                '''                Sets the spatial reuse protocol priority value of an 
                outgoing packet.
                ''',
                'srp_priority',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('traffic-class', ATTRIBUTE, 'int' , None, None, 
                [('0', '63')], [], 
                '''                Sets the Traffic class identifiers on IPv4 or MPLS packets.
                ''',
                'traffic_class',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            ],
            'Cisco-IOS-XR-infra-policymgr-cfg',
            'set',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-policymgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg'
        ),
    },
    'PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ExceedAction' : {
        'meta_info' : _MetaInfoClass('PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ExceedAction',
            False, 
            [
            _MetaInfoClassMember('drop', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Police action drop.
                ''',
                'drop',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('set', REFERENCE_CLASS, 'Set' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg', 'PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ExceedAction.Set', 
                [], [], 
                '''                Police action packet marking.
                ''',
                'set',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('Transmit', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Police action transmit.
                ''',
                'transmit',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            ],
            'Cisco-IOS-XR-infra-policymgr-cfg',
            'exceed-action',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-policymgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg'
        ),
    },
    'PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ViolateAction.Set' : {
        'meta_info' : _MetaInfoClass('PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ViolateAction.Set',
            False, 
            [
            _MetaInfoClassMember('cos', ATTRIBUTE, 'int' , None, None, 
                [('0', '7')], [], 
                '''                Sets the specific IEEE 802.1Q Layer 2 CoS value of an
                outgoing packet.
                This command should be used by a router if a user wants
                to mark a packet that is being sent to a switch. 
                Switches can leverage Layer 2 header information, 
                including a CoS value marking. Packets entering an 
                interface cannot be set with a CoS value.
                ''',
                'cos',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('dei', ATTRIBUTE, 'int' , None, None, 
                [('0', '1')], [], 
                '''                Set DEI bit.
                ''',
                'dei',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('dei-imposition', ATTRIBUTE, 'int' , None, None, 
                [('0', '1')], [], 
                '''                Set DEI imposition bit.
                ''',
                'dei_imposition',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('destination-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Destination IPv4 address.
                ''',
                'destination_address',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('df', ATTRIBUTE, 'int' , None, None, 
                [('0', '1')], [], 
                '''                Set DF bit.
                ''',
                'df',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('discard-class', ATTRIBUTE, 'int' , None, None, 
                [('0', '7')], [], 
                '''                Sets the discard class on IPv4 or MPLS packets.
                The discard-class can be used only in service policies 
                that are attached in the ingress policy.
                ''',
                'discard_class',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('dscp', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9]|[1-5][0-9]|6[0-3])|(af11)|(af12)|(af13)|(af21)|(af22)|(af23)|(af31)|(af32)|(af33)|(af41)|(af42)|(af43)|(ef)|(default)|(cs1)|(cs2)|(cs3)|(cs4)|(cs5)|(cs6)|(cs7)'], 
                '''                Marks a packet by setting the DSCP in the ToS byte.
                ''',
                'dscp',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('forward-class', ATTRIBUTE, 'int' , None, None, 
                [('0', '7')], [], 
                '''                Sets the discard class.
                ''',
                'forward_class',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('fr-de', ATTRIBUTE, 'int' , None, None, 
                [('0', '1')], [], 
                '''                Set FrameRelay DE bit.
                ''',
                'fr_de',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('inner-cos', ATTRIBUTE, 'int' , None, None, 
                [('0', '7')], [], 
                '''                Set inner cos.
                ''',
                'inner_cos',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('mpls-experimental-imposition', ATTRIBUTE, 'int' , None, None, 
                [('0', '7')], [], 
                '''                Sets the experimental value of the MPLS packet 
                imposition labels.
                Imposition can be used only in service policies that 
                are attached in the ingress policy
                ''',
                'mpls_experimental_imposition',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('mpls-experimental-top-most', ATTRIBUTE, 'int' , None, None, 
                [('0', '7')], [], 
                '''                Sets the experimental value of the MPLS packet top-most
                labels.
                ''',
                'mpls_experimental_top_most',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('precedence', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Sets the precedence value in the IP header.
                ''',
                'precedence',
                'Cisco-IOS-XR-infra-policymgr-cfg', False, [
                    _MetaInfoClassMember('precedence', ATTRIBUTE, 'int' , None, None, 
                        [('0', '7')], [], 
                        '''                        Sets the precedence value in the IP header.
                        ''',
                        'precedence',
                        'Cisco-IOS-XR-infra-policymgr-cfg', False),
                    _MetaInfoClassMember('precedence', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(critical)|(flash)|(flash-override)|(immediate)|(internet)|(network)|(priority)|(routine)'], 
                        '''                        Sets the precedence value in the IP header.
                        ''',
                        'precedence',
                        'Cisco-IOS-XR-infra-policymgr-cfg', False),
                ]),
            _MetaInfoClassMember('precedence-tunnel', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Sets the precedence tunnel value for ipsec.
                ''',
                'precedence_tunnel',
                'Cisco-IOS-XR-infra-policymgr-cfg', False, [
                    _MetaInfoClassMember('precedence-tunnel', ATTRIBUTE, 'int' , None, None, 
                        [('0', '7')], [], 
                        '''                        Sets the precedence tunnel value for ipsec.
                        ''',
                        'precedence_tunnel',
                        'Cisco-IOS-XR-infra-policymgr-cfg', False),
                    _MetaInfoClassMember('precedence-tunnel', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(critical)|(flash)|(flash-override)|(immediate)|(internet)|(network)|(priority)|(routine)'], 
                        '''                        Sets the precedence tunnel value for ipsec.
                        ''',
                        'precedence_tunnel',
                        'Cisco-IOS-XR-infra-policymgr-cfg', False),
                ]),
            _MetaInfoClassMember('qos-group', ATTRIBUTE, 'int' , None, None, 
                [('0', '512')], [], 
                '''                Sets the QoS group identifiers on IPv4 or MPLS packets.
                The set qos-group is supported only on an ingress policy.
                ''',
                'qos_group',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Source IPv4 address.
                ''',
                'source_address',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('srp-priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '7')], [], 
                '''                Sets the spatial reuse protocol priority value of an 
                outgoing packet.
                ''',
                'srp_priority',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('traffic-class', ATTRIBUTE, 'int' , None, None, 
                [('0', '63')], [], 
                '''                Sets the Traffic class identifiers on IPv4 or MPLS packets.
                ''',
                'traffic_class',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            ],
            'Cisco-IOS-XR-infra-policymgr-cfg',
            'set',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-policymgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg'
        ),
    },
    'PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ViolateAction' : {
        'meta_info' : _MetaInfoClass('PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ViolateAction',
            False, 
            [
            _MetaInfoClassMember('drop', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Police action drop.
                ''',
                'drop',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('set', REFERENCE_CLASS, 'Set' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg', 'PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ViolateAction.Set', 
                [], [], 
                '''                Police action packet marking.
                ''',
                'set',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('Transmit', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Police action transmit.
                ''',
                'transmit',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            ],
            'Cisco-IOS-XR-infra-policymgr-cfg',
            'violate-action',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-policymgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg'
        ),
    },
    'PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police' : {
        'meta_info' : _MetaInfoClass('PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police',
            False, 
            [
            _MetaInfoClassMember('burst', REFERENCE_CLASS, 'Burst' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg', 'PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.Burst', 
                [], [], 
                '''                Burst configuration.
                ''',
                'burst',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('conform-action', REFERENCE_CLASS, 'ConformAction' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg', 'PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ConformAction', 
                [], [], 
                '''                Configures the action to take on packets that conform 
                to the rate limit.
                ''',
                'conform_action',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('exceed-action', REFERENCE_CLASS, 'ExceedAction' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg', 'PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ExceedAction', 
                [], [], 
                '''                Configures the action to take on packets that exceed 
                the rate limit.
                ''',
                'exceed_action',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('peak-burst', REFERENCE_CLASS, 'PeakBurst' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg', 'PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.PeakBurst', 
                [], [], 
                '''                Peak burst configuration.
                ''',
                'peak_burst',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('peak-rate', REFERENCE_CLASS, 'PeakRate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg', 'PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.PeakRate', 
                [], [], 
                '''                Peak rate configuration.
                ''',
                'peak_rate',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('rate', REFERENCE_CLASS, 'Rate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg', 'PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.Rate', 
                [], [], 
                '''                Rate configuration.
                ''',
                'rate',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('violate-action', REFERENCE_CLASS, 'ViolateAction' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg', 'PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ViolateAction', 
                [], [], 
                '''                Configures the action to take on packets that violate
                the rate limit.
                ''',
                'violate_action',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            ],
            'Cisco-IOS-XR-infra-policymgr-cfg',
            'police',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-policymgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg'
        ),
    },
    'PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.ServicePolicy' : {
        'meta_info' : _MetaInfoClass('PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.ServicePolicy',
            False, 
            [
            _MetaInfoClassMember('policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[a-zA-Z0-9][a-zA-Z0-9\\._@$%+#:=<>\\-]{0,62}'], 
                '''                Name of service-policy.
                ''',
                'policy_name',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('type', ATTRIBUTE, 'str' , None, None, 
                [], [b'(PBR)|(QOS)|(REDIRECT)|(TRAFFIC)|(pbr)|(qos)|(redirect)|(traffic)'], 
                '''                Type of service-policy.
                ''',
                'type',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            ],
            'Cisco-IOS-XR-infra-policymgr-cfg',
            'service-policy',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-policymgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg'
        ),
    },
    'PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.CacLocal.Rate' : {
        'meta_info' : _MetaInfoClass('PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.CacLocal.Rate',
            False, 
            [
            _MetaInfoClassMember('units', ATTRIBUTE, 'str' , None, None, 
                [], [b'(bps)|(kbps)|(mbps)|(gbps)|(cellsps)'], 
                '''                Rate units.
                ''',
                'units',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                Rate value.
                ''',
                'value',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            ],
            'Cisco-IOS-XR-infra-policymgr-cfg',
            'rate',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-policymgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg'
        ),
    },
    'PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.CacLocal.FlowRate' : {
        'meta_info' : _MetaInfoClass('PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.CacLocal.FlowRate',
            False, 
            [
            _MetaInfoClassMember('units', ATTRIBUTE, 'str' , None, None, 
                [], [b'(bps)|(kbps)|(mbps)|(gbps)|(cellsps)'], 
                '''                Rate units.
                ''',
                'units',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                Rate value.
                ''',
                'value',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            ],
            'Cisco-IOS-XR-infra-policymgr-cfg',
            'flow-rate',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-policymgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg'
        ),
    },
    'PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.CacLocal' : {
        'meta_info' : _MetaInfoClass('PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.CacLocal',
            False, 
            [
            _MetaInfoClassMember('flow-idle-timeout', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                The interval after which a flow is removed, 
                if there is no activity.
                If timeout is 0 this flow does not expire.
                ''',
                'flow_idle_timeout',
                'Cisco-IOS-XR-infra-policymgr-cfg', False, [
                    _MetaInfoClassMember('flow-idle-timeout', ATTRIBUTE, 'int' , None, None, 
                        [('10', '2550')], [], 
                        '''                        The interval after which a flow is removed, 
                        if there is no activity.
                        If timeout is 0 this flow does not expire.
                        ''',
                        'flow_idle_timeout',
                        'Cisco-IOS-XR-infra-policymgr-cfg', False),
                    _MetaInfoClassMember('flow-idle-timeout', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(None)|(none)'], 
                        '''                        The interval after which a flow is removed, 
                        if there is no activity.
                        If timeout is 0 this flow does not expire.
                        ''',
                        'flow_idle_timeout',
                        'Cisco-IOS-XR-infra-policymgr-cfg', False),
                ]),
            _MetaInfoClassMember('flow-rate', REFERENCE_CLASS, 'FlowRate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg', 'PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.CacLocal.FlowRate', 
                [], [], 
                '''                The rate allocated per flow.
                ''',
                'flow_rate',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('rate', REFERENCE_CLASS, 'Rate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg', 'PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.CacLocal.Rate', 
                [], [], 
                '''                The rate allocated for all flows.
                ''',
                'rate',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            ],
            'Cisco-IOS-XR-infra-policymgr-cfg',
            'cac-local',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-policymgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg'
        ),
    },
    'PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.FlowParams' : {
        'meta_info' : _MetaInfoClass('PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.FlowParams',
            False, 
            [
            _MetaInfoClassMember('history', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Keep stats/metrics on box for so many intervals.
                ''',
                'history',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('interval-duration', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Monitored interval duration.
                ''',
                'interval_duration',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('max-flow', ATTRIBUTE, 'int' , None, None, 
                [('0', '4096')], [], 
                '''                Max simultaneous flows monitored per policy class
                ''',
                'max_flow',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('timeout', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Declare a flow dead if no packets received in
                so much time
                ''',
                'timeout',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            ],
            'Cisco-IOS-XR-infra-policymgr-cfg',
            'flow-params',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-policymgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg'
        ),
    },
    'PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.MetricsIpcbr.Rate' : {
        'meta_info' : _MetaInfoClass('PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.MetricsIpcbr.Rate',
            False, 
            [
            _MetaInfoClassMember('layer3', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Nominal rate specified at the L3 (IP).
                ''',
                'layer3',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('media', ATTRIBUTE, 'int' , None, None, 
                [('1', '3000000000')], [], 
                '''                Nominal data rate of the media flow (ip payload).
                ''',
                'media',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('packet', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Nominal IP layer packet rate (in pps).
                ''',
                'packet',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            ],
            'Cisco-IOS-XR-infra-policymgr-cfg',
            'rate',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-policymgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg'
        ),
    },
    'PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.MetricsIpcbr.MediaPacket' : {
        'meta_info' : _MetaInfoClass('PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.MetricsIpcbr.MediaPacket',
            False, 
            [
            _MetaInfoClassMember('count-in-layer3', ATTRIBUTE, 'int' , None, None, 
                [('1', '64')], [], 
                '''                Nominal number of media packets in an IP payload.
                ''',
                'count_in_layer3',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('size', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Nominal size of the media-packet.
                ''',
                'size',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            ],
            'Cisco-IOS-XR-infra-policymgr-cfg',
            'media-packet',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-policymgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg'
        ),
    },
    'PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.MetricsIpcbr' : {
        'meta_info' : _MetaInfoClass('PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.MetricsIpcbr',
            False, 
            [
            _MetaInfoClassMember('media-packet', REFERENCE_CLASS, 'MediaPacket' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg', 'PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.MetricsIpcbr.MediaPacket', 
                [], [], 
                '''                Media-packet structure.
                ''',
                'media_packet',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('rate', REFERENCE_CLASS, 'Rate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg', 'PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.MetricsIpcbr.Rate', 
                [], [], 
                '''                Nominal per-flow data rate.
                ''',
                'rate',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            ],
            'Cisco-IOS-XR-infra-policymgr-cfg',
            'metrics-ipcbr',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-policymgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg'
        ),
    },
    'PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Action' : {
        'meta_info' : _MetaInfoClass('PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Action',
            False, 
            [
            _MetaInfoClassMember('snmp', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                SNMP.
                ''',
                'snmp',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('syslog', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Syslog.
                ''',
                'syslog',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            ],
            'Cisco-IOS-XR-infra-policymgr-cfg',
            'action',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-policymgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg'
        ),
    },
    'PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Alarm.Type' : {
        'meta_info' : _MetaInfoClass('PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Alarm.Type',
            False, 
            [
            _MetaInfoClassMember('discrete', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Discrete alarm type.
                ''',
                'discrete',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('group-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Number of flows to reach before 
                triggering alarm
                ''',
                'group_count',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('group-percent', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Percent to reach before triggering alarm
                ''',
                'group_percent',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            ],
            'Cisco-IOS-XR-infra-policymgr-cfg',
            'type',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-policymgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg'
        ),
    },
    'PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Alarm' : {
        'meta_info' : _MetaInfoClass('PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Alarm',
            False, 
            [
            _MetaInfoClassMember('severity', ATTRIBUTE, 'str' , None, None, 
                [], [b'(informational)|(notification)|(warning)|(error)|(critical)|(alert)|(emergency)'], 
                '''                Severity of the alarm.
                ''',
                'severity',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('type', REFERENCE_CLASS, 'Type' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg', 'PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Alarm.Type', 
                [], [], 
                '''                Alarm type.
                ''',
                'type',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            ],
            'Cisco-IOS-XR-infra-policymgr-cfg',
            'alarm',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-policymgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg'
        ),
    },
    'PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Threshold.TriggerValue' : {
        'meta_info' : _MetaInfoClass('PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Threshold.TriggerValue',
            False, 
            [
            _MetaInfoClassMember('greater-than', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Greater than
                ''',
                'greater_than',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('greater-than-equal', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Greater than equal
                ''',
                'greater_than_equal',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('less-than', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Less than
                ''',
                'less_than',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('less-than-equal', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Less than equal
                ''',
                'less_than_equal',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('range', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Range
                ''',
                'range',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            ],
            'Cisco-IOS-XR-infra-policymgr-cfg',
            'trigger-value',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-policymgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg'
        ),
    },
    'PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Threshold.TriggerType' : {
        'meta_info' : _MetaInfoClass('PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Threshold.TriggerType',
            False, 
            [
            _MetaInfoClassMember('average', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Trigger averaged over N intervals.
                ''',
                'average',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('immediate', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Immediate trigger.
                ''',
                'immediate',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            ],
            'Cisco-IOS-XR-infra-policymgr-cfg',
            'trigger-type',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-policymgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg'
        ),
    },
    'PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Threshold' : {
        'meta_info' : _MetaInfoClass('PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Threshold',
            False, 
            [
            _MetaInfoClassMember('trigger-type', REFERENCE_CLASS, 'TriggerType' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg', 'PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Threshold.TriggerType', 
                [], [], 
                '''                Alarm trigger type settings.
                ''',
                'trigger_type',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('trigger-value', REFERENCE_CLASS, 'TriggerValue' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg', 'PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Threshold.TriggerValue', 
                [], [], 
                '''                Alarm trigger value settings.
                ''',
                'trigger_value',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            ],
            'Cisco-IOS-XR-infra-policymgr-cfg',
            'threshold',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-policymgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg'
        ),
    },
    'PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React' : {
        'meta_info' : _MetaInfoClass('PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React',
            False, 
            [
            _MetaInfoClassMember('action', REFERENCE_CLASS, 'Action' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg', 'PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Action', 
                [], [], 
                '''                Action on alert.
                ''',
                'action',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('alarm', REFERENCE_CLASS, 'Alarm' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg', 'PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Alarm', 
                [], [], 
                '''                Alaram settings.
                ''',
                'alarm',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('criterion-delay-factor', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                React criterion delay factor.
                ''',
                'criterion_delay_factor',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('criterion-flow-count', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                React criterion flow count.
                ''',
                'criterion_flow_count',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('criterion-media-stop', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                React criterion media stop.
                ''',
                'criterion_media_stop',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('criterion-mrv', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                React criterion mrv.
                ''',
                'criterion_mrv',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('criterion-packet-rate', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                React criterion packet rate.
                ''',
                'criterion_packet_rate',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('descrition', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                String describing the react statement.
                ''',
                'descrition',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('threshold', REFERENCE_CLASS, 'Threshold' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg', 'PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Threshold', 
                [], [], 
                '''                Alarm threshold settings.
                ''',
                'threshold',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            ],
            'Cisco-IOS-XR-infra-policymgr-cfg',
            'react',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-policymgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg'
        ),
    },
    'PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.PbrForward.NextHop' : {
        'meta_info' : _MetaInfoClass('PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.PbrForward.NextHop',
            False, 
            [
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address.
                ''',
                'ipv4_address',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address.
                ''',
                'ipv6_address',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('vrf', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                VRF name.
                ''',
                'vrf',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            ],
            'Cisco-IOS-XR-infra-policymgr-cfg',
            'next-hop',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-policymgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg'
        ),
    },
    'PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.PbrForward' : {
        'meta_info' : _MetaInfoClass('PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.PbrForward',
            False, 
            [
            _MetaInfoClassMember('default', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Use system default routing table.
                ''',
                'default',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('next-hop', REFERENCE_CLASS, 'NextHop' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg', 'PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.PbrForward.NextHop', 
                [], [], 
                '''                Use specific next-hop.
                Here we present 5 different combination 
                for the pbf next-hop.
                 1. vrf with v6 address
                 2. vrf with v4 address
                 3. vrf 
                 4. v4 address
                 5. v6 address
                ''',
                'next_hop',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            ],
            'Cisco-IOS-XR-infra-policymgr-cfg',
            'pbr-forward',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-policymgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg'
        ),
    },
    'PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.ServiceFunctionPath' : {
        'meta_info' : _MetaInfoClass('PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.ServiceFunctionPath',
            False, 
            [
            _MetaInfoClassMember('index', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                Service function path index.
                ''',
                'index',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('metadata', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Service function path metadata name.
                ''',
                'metadata',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('path-id', ATTRIBUTE, 'int' , None, None, 
                [('1', '16777215')], [], 
                '''                Service function path id.
                ''',
                'path_id',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            ],
            'Cisco-IOS-XR-infra-policymgr-cfg',
            'service-function-path',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-policymgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg'
        ),
    },
    'PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule' : {
        'meta_info' : _MetaInfoClass('PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule',
            False, 
            [
            _MetaInfoClassMember('class-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[a-zA-Z0-9][a-zA-Z0-9\\._@$%+#:=<>\\-]{0,62}'], 
                '''                Name of class-map.
                ''',
                'class_name',
                'Cisco-IOS-XR-infra-policymgr-cfg', True),
            _MetaInfoClassMember('class-type', REFERENCE_ENUM_CLASS, 'PmapClassMapTypeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg', 'PmapClassMapTypeEnum', 
                [], [], 
                '''                Type of class-map.
                ''',
                'class_type',
                'Cisco-IOS-XR-infra-policymgr-cfg', True),
            _MetaInfoClassMember('bandwidth-remaining', REFERENCE_CLASS, 'BandwidthRemaining' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg', 'PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.BandwidthRemaining', 
                [], [], 
                '''                Policy action bandwidth remaining queue.
                ''',
                'bandwidth_remaining',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('cac-local', REFERENCE_CLASS, 'CacLocal' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg', 'PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.CacLocal', 
                [], [], 
                '''                Policy action CAC.
                ''',
                'cac_local',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('decap-gre', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Policy action DECAP GRE.
                ''',
                'decap_gre',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('default-red', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Default random early detection
                ''',
                'default_red',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('ecn-red', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                ECN based random early detection
                ''',
                'ecn_red',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('flow-params', REFERENCE_CLASS, 'FlowParams' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg', 'PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.FlowParams', 
                [], [], 
                '''                Policy flow monitoring action.
                ''',
                'flow_params',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('fragment', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Policy action fragment. Fragment name
                ''',
                'fragment',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('http-redirect', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Policy action http redirect.
                Redirect to this url.
                ''',
                'http_redirect',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('metrics-ipcbr', REFERENCE_CLASS, 'MetricsIpcbr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg', 'PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.MetricsIpcbr', 
                [], [], 
                '''                Policy IP-CBR metric action.
                ''',
                'metrics_ipcbr',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('min-bandwidth', REFERENCE_CLASS, 'MinBandwidth' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg', 'PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.MinBandwidth', 
                [], [], 
                '''                Policy action minimum bandwidth queue.
                ''',
                'min_bandwidth',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('pbr-drop', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Policy action PBR drop.
                ''',
                'pbr_drop',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('pbr-forward', REFERENCE_CLASS, 'PbrForward' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg', 'PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.PbrForward', 
                [], [], 
                '''                Policy action PBR forward.
                ''',
                'pbr_forward',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('pbr-transmit', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Policy action PBR transmit.
                ''',
                'pbr_transmit',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('pfc', REFERENCE_CLASS, 'Pfc' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg', 'PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Pfc', 
                [], [], 
                '''                Policy action pfc.
                ''',
                'pfc',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('police', REFERENCE_CLASS, 'Police' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg', 'PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police', 
                [], [], 
                '''                Configures traffic policing action.
                ''',
                'police',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('priority-level', ATTRIBUTE, 'int' , None, None, 
                [('1', '7')], [], 
                '''                Priority level.
                ''',
                'priority_level',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('queue-limit', REFERENCE_CLASS, 'QueueLimit' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg', 'PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.QueueLimit', 
                [], [], 
                '''                Policy action queue limit.
                ''',
                'queue_limit',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('random-detect', REFERENCE_LIST, 'RandomDetect' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg', 'PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.RandomDetect', 
                [], [], 
                '''                Random early detection.
                All RED profiles in a class must be based
                on the same field.
                ''',
                'random_detect',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('react', REFERENCE_CLASS, 'React' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg', 'PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React', 
                [], [], 
                '''                Policy action react.
                ''',
                'react',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('service-fragment', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Policy action service fragment. 
                Service fragment name
                ''',
                'service_fragment',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('service-function-path', REFERENCE_CLASS, 'ServiceFunctionPath' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg', 'PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.ServiceFunctionPath', 
                [], [], 
                '''                Policy action service function path.
                ''',
                'service_function_path',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('service-policy', REFERENCE_CLASS, 'ServicePolicy' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg', 'PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.ServicePolicy', 
                [], [], 
                '''                Configure a child service policy.
                ''',
                'service_policy',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('set', REFERENCE_CLASS, 'Set' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg', 'PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Set', 
                [], [], 
                '''                Policy action packet marking.
                ''',
                'set',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('shape', REFERENCE_CLASS, 'Shape' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg', 'PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Shape', 
                [], [], 
                '''                Policy action shape.
                ''',
                'shape',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            ],
            'Cisco-IOS-XR-infra-policymgr-cfg',
            'policy-map-rule',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-policymgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg'
        ),
    },
    'PolicyManager.PolicyMaps.PolicyMap' : {
        'meta_info' : _MetaInfoClass('PolicyManager.PolicyMaps.PolicyMap',
            False, 
            [
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'PolicyMapTypeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg', 'PolicyMapTypeEnum', 
                [], [], 
                '''                Type of policy-map.
                ''',
                'type',
                'Cisco-IOS-XR-infra-policymgr-cfg', True),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[a-zA-Z0-9][a-zA-Z0-9\\._@$%+#:=<>\\-]{0,62}'], 
                '''                Name of policy-map.
                ''',
                'name',
                'Cisco-IOS-XR-infra-policymgr-cfg', True),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Description for this policy-map.
                ''',
                'description',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('event', REFERENCE_LIST, 'Event' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg', 'PolicyManager.PolicyMaps.PolicyMap.Event', 
                [], [], 
                '''                Policy event.
                ''',
                'event',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('policy-map-rule', REFERENCE_LIST, 'PolicyMapRule' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg', 'PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule', 
                [], [], 
                '''                Class-map rule.
                ''',
                'policy_map_rule',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            ],
            'Cisco-IOS-XR-infra-policymgr-cfg',
            'policy-map',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-policymgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg'
        ),
    },
    'PolicyManager.PolicyMaps' : {
        'meta_info' : _MetaInfoClass('PolicyManager.PolicyMaps',
            False, 
            [
            _MetaInfoClassMember('policy-map', REFERENCE_LIST, 'PolicyMap' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg', 'PolicyManager.PolicyMaps.PolicyMap', 
                [], [], 
                '''                Policy-map configuration.
                ''',
                'policy_map',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            ],
            'Cisco-IOS-XR-infra-policymgr-cfg',
            'policy-maps',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-policymgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg'
        ),
    },
    'PolicyManager' : {
        'meta_info' : _MetaInfoClass('PolicyManager',
            False, 
            [
            _MetaInfoClassMember('class-maps', REFERENCE_CLASS, 'ClassMaps' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg', 'PolicyManager.ClassMaps', 
                [], [], 
                '''                Class-maps configuration.
                ''',
                'class_maps',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            _MetaInfoClassMember('policy-maps', REFERENCE_CLASS, 'PolicyMaps' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg', 'PolicyManager.PolicyMaps', 
                [], [], 
                '''                Policy-maps configuration.
                ''',
                'policy_maps',
                'Cisco-IOS-XR-infra-policymgr-cfg', False),
            ],
            'Cisco-IOS-XR-infra-policymgr-cfg',
            'policy-manager',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-policymgr-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg'
        ),
    },
}
_meta_table['PolicyManager.ClassMaps.ClassMap.Match.Flow.FlowCache']['meta_info'].parent =_meta_table['PolicyManager.ClassMaps.ClassMap.Match.Flow']['meta_info']
_meta_table['PolicyManager.ClassMaps.ClassMap.Match.DestinationAddressIpv4']['meta_info'].parent =_meta_table['PolicyManager.ClassMaps.ClassMap.Match']['meta_info']
_meta_table['PolicyManager.ClassMaps.ClassMap.Match.DestinationAddressIpv6']['meta_info'].parent =_meta_table['PolicyManager.ClassMaps.ClassMap.Match']['meta_info']
_meta_table['PolicyManager.ClassMaps.ClassMap.Match.SourceAddressIpv4']['meta_info'].parent =_meta_table['PolicyManager.ClassMaps.ClassMap.Match']['meta_info']
_meta_table['PolicyManager.ClassMaps.ClassMap.Match.SourceAddressIpv6']['meta_info'].parent =_meta_table['PolicyManager.ClassMaps.ClassMap.Match']['meta_info']
_meta_table['PolicyManager.ClassMaps.ClassMap.Match.DomainName']['meta_info'].parent =_meta_table['PolicyManager.ClassMaps.ClassMap.Match']['meta_info']
_meta_table['PolicyManager.ClassMaps.ClassMap.Match.DomainNameRegex']['meta_info'].parent =_meta_table['PolicyManager.ClassMaps.ClassMap.Match']['meta_info']
_meta_table['PolicyManager.ClassMaps.ClassMap.Match.Flow']['meta_info'].parent =_meta_table['PolicyManager.ClassMaps.ClassMap.Match']['meta_info']
_meta_table['PolicyManager.ClassMaps.ClassMap.MatchNot.DestinationAddressIpv4']['meta_info'].parent =_meta_table['PolicyManager.ClassMaps.ClassMap.MatchNot']['meta_info']
_meta_table['PolicyManager.ClassMaps.ClassMap.MatchNot.DestinationAddressIpv6']['meta_info'].parent =_meta_table['PolicyManager.ClassMaps.ClassMap.MatchNot']['meta_info']
_meta_table['PolicyManager.ClassMaps.ClassMap.MatchNot.SourceAddressIpv4']['meta_info'].parent =_meta_table['PolicyManager.ClassMaps.ClassMap.MatchNot']['meta_info']
_meta_table['PolicyManager.ClassMaps.ClassMap.MatchNot.SourceAddressIpv6']['meta_info'].parent =_meta_table['PolicyManager.ClassMaps.ClassMap.MatchNot']['meta_info']
_meta_table['PolicyManager.ClassMaps.ClassMap.MatchNot.DomainName']['meta_info'].parent =_meta_table['PolicyManager.ClassMaps.ClassMap.MatchNot']['meta_info']
_meta_table['PolicyManager.ClassMaps.ClassMap.MatchNot.DomainNameRegex']['meta_info'].parent =_meta_table['PolicyManager.ClassMaps.ClassMap.MatchNot']['meta_info']
_meta_table['PolicyManager.ClassMaps.ClassMap.MatchNot.Flow']['meta_info'].parent =_meta_table['PolicyManager.ClassMaps.ClassMap.MatchNot']['meta_info']
_meta_table['PolicyManager.ClassMaps.ClassMap.Match']['meta_info'].parent =_meta_table['PolicyManager.ClassMaps.ClassMap']['meta_info']
_meta_table['PolicyManager.ClassMaps.ClassMap.MatchNot']['meta_info'].parent =_meta_table['PolicyManager.ClassMaps.ClassMap']['meta_info']
_meta_table['PolicyManager.ClassMaps.ClassMap']['meta_info'].parent =_meta_table['PolicyManager.ClassMaps']['meta_info']
_meta_table['PolicyManager.PolicyMaps.PolicyMap.Event.Class_.ActionRule.ActivateDynamicTemplate']['meta_info'].parent =_meta_table['PolicyManager.PolicyMaps.PolicyMap.Event.Class_.ActionRule']['meta_info']
_meta_table['PolicyManager.PolicyMaps.PolicyMap.Event.Class_.ActionRule.Authenticate']['meta_info'].parent =_meta_table['PolicyManager.PolicyMaps.PolicyMap.Event.Class_.ActionRule']['meta_info']
_meta_table['PolicyManager.PolicyMaps.PolicyMap.Event.Class_.ActionRule.Authorize']['meta_info'].parent =_meta_table['PolicyManager.PolicyMaps.PolicyMap.Event.Class_.ActionRule']['meta_info']
_meta_table['PolicyManager.PolicyMaps.PolicyMap.Event.Class_.ActionRule.DeactivateDynamicTemplate']['meta_info'].parent =_meta_table['PolicyManager.PolicyMaps.PolicyMap.Event.Class_.ActionRule']['meta_info']
_meta_table['PolicyManager.PolicyMaps.PolicyMap.Event.Class_.ActionRule.SetTimer']['meta_info'].parent =_meta_table['PolicyManager.PolicyMaps.PolicyMap.Event.Class_.ActionRule']['meta_info']
_meta_table['PolicyManager.PolicyMaps.PolicyMap.Event.Class_.ActionRule.StopTimer']['meta_info'].parent =_meta_table['PolicyManager.PolicyMaps.PolicyMap.Event.Class_.ActionRule']['meta_info']
_meta_table['PolicyManager.PolicyMaps.PolicyMap.Event.Class_.ActionRule']['meta_info'].parent =_meta_table['PolicyManager.PolicyMaps.PolicyMap.Event.Class_']['meta_info']
_meta_table['PolicyManager.PolicyMaps.PolicyMap.Event.Class_']['meta_info'].parent =_meta_table['PolicyManager.PolicyMaps.PolicyMap.Event']['meta_info']
_meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Shape.Rate']['meta_info'].parent =_meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Shape']['meta_info']
_meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Shape.Burst']['meta_info'].parent =_meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Shape']['meta_info']
_meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Pfc.PfcBufferSize']['meta_info'].parent =_meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Pfc']['meta_info']
_meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Pfc.PfcPauseThreshold']['meta_info'].parent =_meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Pfc']['meta_info']
_meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Pfc.PfcResumeThreshold']['meta_info'].parent =_meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Pfc']['meta_info']
_meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ConformAction.Set']['meta_info'].parent =_meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ConformAction']['meta_info']
_meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ExceedAction.Set']['meta_info'].parent =_meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ExceedAction']['meta_info']
_meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ViolateAction.Set']['meta_info'].parent =_meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ViolateAction']['meta_info']
_meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.Rate']['meta_info'].parent =_meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police']['meta_info']
_meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.PeakRate']['meta_info'].parent =_meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police']['meta_info']
_meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.Burst']['meta_info'].parent =_meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police']['meta_info']
_meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.PeakBurst']['meta_info'].parent =_meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police']['meta_info']
_meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ConformAction']['meta_info'].parent =_meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police']['meta_info']
_meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ExceedAction']['meta_info'].parent =_meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police']['meta_info']
_meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ViolateAction']['meta_info'].parent =_meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police']['meta_info']
_meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.CacLocal.Rate']['meta_info'].parent =_meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.CacLocal']['meta_info']
_meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.CacLocal.FlowRate']['meta_info'].parent =_meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.CacLocal']['meta_info']
_meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.MetricsIpcbr.Rate']['meta_info'].parent =_meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.MetricsIpcbr']['meta_info']
_meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.MetricsIpcbr.MediaPacket']['meta_info'].parent =_meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.MetricsIpcbr']['meta_info']
_meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Alarm.Type']['meta_info'].parent =_meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Alarm']['meta_info']
_meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Threshold.TriggerValue']['meta_info'].parent =_meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Threshold']['meta_info']
_meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Threshold.TriggerType']['meta_info'].parent =_meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Threshold']['meta_info']
_meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Action']['meta_info'].parent =_meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React']['meta_info']
_meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Alarm']['meta_info'].parent =_meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React']['meta_info']
_meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Threshold']['meta_info'].parent =_meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React']['meta_info']
_meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.PbrForward.NextHop']['meta_info'].parent =_meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.PbrForward']['meta_info']
_meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Shape']['meta_info'].parent =_meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule']['meta_info']
_meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.MinBandwidth']['meta_info'].parent =_meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule']['meta_info']
_meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.BandwidthRemaining']['meta_info'].parent =_meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule']['meta_info']
_meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.QueueLimit']['meta_info'].parent =_meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule']['meta_info']
_meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Pfc']['meta_info'].parent =_meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule']['meta_info']
_meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.RandomDetect']['meta_info'].parent =_meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule']['meta_info']
_meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Set']['meta_info'].parent =_meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule']['meta_info']
_meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police']['meta_info'].parent =_meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule']['meta_info']
_meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.ServicePolicy']['meta_info'].parent =_meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule']['meta_info']
_meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.CacLocal']['meta_info'].parent =_meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule']['meta_info']
_meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.FlowParams']['meta_info'].parent =_meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule']['meta_info']
_meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.MetricsIpcbr']['meta_info'].parent =_meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule']['meta_info']
_meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React']['meta_info'].parent =_meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule']['meta_info']
_meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.PbrForward']['meta_info'].parent =_meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule']['meta_info']
_meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.ServiceFunctionPath']['meta_info'].parent =_meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule']['meta_info']
_meta_table['PolicyManager.PolicyMaps.PolicyMap.Event']['meta_info'].parent =_meta_table['PolicyManager.PolicyMaps.PolicyMap']['meta_info']
_meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule']['meta_info'].parent =_meta_table['PolicyManager.PolicyMaps.PolicyMap']['meta_info']
_meta_table['PolicyManager.PolicyMaps.PolicyMap']['meta_info'].parent =_meta_table['PolicyManager.PolicyMaps']['meta_info']
_meta_table['PolicyManager.ClassMaps']['meta_info'].parent =_meta_table['PolicyManager']['meta_info']
_meta_table['PolicyManager.PolicyMaps']['meta_info'].parent =_meta_table['PolicyManager']['meta_info']
