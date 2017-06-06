


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'NtpAccessAfEnum' : _MetaInfoEnum('NtpAccessAfEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg',
        {
            'ipv4':'ipv4',
            'ipv6':'ipv6',
        }, 'Cisco-IOS-XR-ip-ntp-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ip-ntp-cfg']),
    'NtpPeerEnum' : _MetaInfoEnum('NtpPeerEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg',
        {
            'peer':'peer',
            'server':'server',
        }, 'Cisco-IOS-XR-ip-ntp-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ip-ntp-cfg']),
    'NtpAccessEnum' : _MetaInfoEnum('NtpAccessEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg',
        {
            'peer':'peer',
            'serve':'serve',
            'serve-only':'serve_only',
            'query-only':'query_only',
        }, 'Cisco-IOS-XR-ip-ntp-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ip-ntp-cfg']),
    'NtpdscpEnum' : _MetaInfoEnum('NtpdscpEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg',
        {
            'ntp-precedence':'ntp_precedence',
            'ntpdscp':'ntpdscp',
        }, 'Cisco-IOS-XR-ip-ntp-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ip-ntp-cfg']),
    'Ntp.PeerVrfs.PeerVrf.PeerIpv4S.PeerIpv4.PeerTypeIpv4' : {
        'meta_info' : _MetaInfoClass('Ntp.PeerVrfs.PeerVrf.PeerIpv4S.PeerIpv4.PeerTypeIpv4',
            False, 
            [
            _MetaInfoClassMember('peer-type', REFERENCE_ENUM_CLASS, 'NtpPeerEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg', 'NtpPeerEnum', 
                [], [], 
                '''                Peer or Server
                ''',
                'peer_type',
                'Cisco-IOS-XR-ip-ntp-cfg', True),
            _MetaInfoClassMember('authentication-key', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Authentication Key
                ''',
                'authentication_key',
                'Cisco-IOS-XR-ip-ntp-cfg', False),
            _MetaInfoClassMember('burst', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Use burst mode
                ''',
                'burst',
                'Cisco-IOS-XR-ip-ntp-cfg', False),
            _MetaInfoClassMember('iburst', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Use iburst mode
                ''',
                'iburst',
                'Cisco-IOS-XR-ip-ntp-cfg', False),
            _MetaInfoClassMember('max-poll', ATTRIBUTE, 'int' , None, None, 
                [('4', '17')], [], 
                '''                Maxinum poll interval
                ''',
                'max_poll',
                'Cisco-IOS-XR-ip-ntp-cfg', False),
            _MetaInfoClassMember('min-poll', ATTRIBUTE, 'int' , None, None, 
                [('4', '17')], [], 
                '''                Minimum poll interval
                ''',
                'min_poll',
                'Cisco-IOS-XR-ip-ntp-cfg', False),
            _MetaInfoClassMember('ntp-version', ATTRIBUTE, 'int' , None, None, 
                [('2', '4')], [], 
                '''                NTP version
                ''',
                'ntp_version',
                'Cisco-IOS-XR-ip-ntp-cfg', False),
            _MetaInfoClassMember('preferred-peer', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Preferred peer
                ''',
                'preferred_peer',
                'Cisco-IOS-XR-ip-ntp-cfg', False),
            _MetaInfoClassMember('source-interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Source interface of this peer
                ''',
                'source_interface',
                'Cisco-IOS-XR-ip-ntp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-ntp-cfg',
            'peer-type-ipv4',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-ntp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg'
        ),
    },
    'Ntp.PeerVrfs.PeerVrf.PeerIpv4S.PeerIpv4' : {
        'meta_info' : _MetaInfoClass('Ntp.PeerVrfs.PeerVrf.PeerIpv4S.PeerIpv4',
            False, 
            [
            _MetaInfoClassMember('address-ipv4', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 Address of a peer
                ''',
                'address_ipv4',
                'Cisco-IOS-XR-ip-ntp-cfg', True),
            _MetaInfoClassMember('peer-type-ipv4', REFERENCE_LIST, 'PeerTypeIpv4' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg', 'Ntp.PeerVrfs.PeerVrf.PeerIpv4S.PeerIpv4.PeerTypeIpv4', 
                [], [], 
                '''                Configure an IPv4 NTP server or peer
                ''',
                'peer_type_ipv4',
                'Cisco-IOS-XR-ip-ntp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-ntp-cfg',
            'peer-ipv4',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-ntp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg'
        ),
    },
    'Ntp.PeerVrfs.PeerVrf.PeerIpv4S' : {
        'meta_info' : _MetaInfoClass('Ntp.PeerVrfs.PeerVrf.PeerIpv4S',
            False, 
            [
            _MetaInfoClassMember('peer-ipv4', REFERENCE_LIST, 'PeerIpv4' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg', 'Ntp.PeerVrfs.PeerVrf.PeerIpv4S.PeerIpv4', 
                [], [], 
                '''                Configure an IPv4 NTP server or peer
                ''',
                'peer_ipv4',
                'Cisco-IOS-XR-ip-ntp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-ntp-cfg',
            'peer-ipv4s',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-ntp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg'
        ),
    },
    'Ntp.PeerVrfs.PeerVrf.PeerIpv6S.PeerIpv6.PeerTypeIpv6' : {
        'meta_info' : _MetaInfoClass('Ntp.PeerVrfs.PeerVrf.PeerIpv6S.PeerIpv6.PeerTypeIpv6',
            False, 
            [
            _MetaInfoClassMember('peer-type', REFERENCE_ENUM_CLASS, 'NtpPeerEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg', 'NtpPeerEnum', 
                [], [], 
                '''                Peer or Server
                ''',
                'peer_type',
                'Cisco-IOS-XR-ip-ntp-cfg', True),
            _MetaInfoClassMember('address-ipv6', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address
                ''',
                'address_ipv6',
                'Cisco-IOS-XR-ip-ntp-cfg', False),
            _MetaInfoClassMember('authentication-key', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Authentication Key
                ''',
                'authentication_key',
                'Cisco-IOS-XR-ip-ntp-cfg', False),
            _MetaInfoClassMember('burst', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Use burst mode
                ''',
                'burst',
                'Cisco-IOS-XR-ip-ntp-cfg', False),
            _MetaInfoClassMember('iburst', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Use iburst mode
                ''',
                'iburst',
                'Cisco-IOS-XR-ip-ntp-cfg', False),
            _MetaInfoClassMember('max-poll', ATTRIBUTE, 'int' , None, None, 
                [('4', '17')], [], 
                '''                Maxinum poll interval
                ''',
                'max_poll',
                'Cisco-IOS-XR-ip-ntp-cfg', False),
            _MetaInfoClassMember('min-poll', ATTRIBUTE, 'int' , None, None, 
                [('4', '17')], [], 
                '''                Minimum poll interval
                ''',
                'min_poll',
                'Cisco-IOS-XR-ip-ntp-cfg', False),
            _MetaInfoClassMember('ntp-version', ATTRIBUTE, 'int' , None, None, 
                [('2', '4')], [], 
                '''                NTP version
                ''',
                'ntp_version',
                'Cisco-IOS-XR-ip-ntp-cfg', False),
            _MetaInfoClassMember('preferred-peer', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Preferred peer
                ''',
                'preferred_peer',
                'Cisco-IOS-XR-ip-ntp-cfg', False),
            _MetaInfoClassMember('source-interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Source interface of this peer
                ''',
                'source_interface',
                'Cisco-IOS-XR-ip-ntp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-ntp-cfg',
            'peer-type-ipv6',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-ntp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg'
        ),
    },
    'Ntp.PeerVrfs.PeerVrf.PeerIpv6S.PeerIpv6' : {
        'meta_info' : _MetaInfoClass('Ntp.PeerVrfs.PeerVrf.PeerIpv6S.PeerIpv6',
            False, 
            [
            _MetaInfoClassMember('address-ipv6', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                Address of a peer
                ''',
                'address_ipv6',
                'Cisco-IOS-XR-ip-ntp-cfg', True),
            _MetaInfoClassMember('peer-type-ipv6', REFERENCE_LIST, 'PeerTypeIpv6' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg', 'Ntp.PeerVrfs.PeerVrf.PeerIpv6S.PeerIpv6.PeerTypeIpv6', 
                [], [], 
                '''                Configure a NTP server or peer
                ''',
                'peer_type_ipv6',
                'Cisco-IOS-XR-ip-ntp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-ntp-cfg',
            'peer-ipv6',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-ntp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg'
        ),
    },
    'Ntp.PeerVrfs.PeerVrf.PeerIpv6S' : {
        'meta_info' : _MetaInfoClass('Ntp.PeerVrfs.PeerVrf.PeerIpv6S',
            False, 
            [
            _MetaInfoClassMember('peer-ipv6', REFERENCE_LIST, 'PeerIpv6' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg', 'Ntp.PeerVrfs.PeerVrf.PeerIpv6S.PeerIpv6', 
                [], [], 
                '''                Configure a NTP server or peer
                ''',
                'peer_ipv6',
                'Cisco-IOS-XR-ip-ntp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-ntp-cfg',
            'peer-ipv6s',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-ntp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg'
        ),
    },
    'Ntp.PeerVrfs.PeerVrf' : {
        'meta_info' : _MetaInfoClass('Ntp.PeerVrfs.PeerVrf',
            False, 
            [
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ip-ntp-cfg', True),
            _MetaInfoClassMember('peer-ipv4s', REFERENCE_CLASS, 'PeerIpv4S' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg', 'Ntp.PeerVrfs.PeerVrf.PeerIpv4S', 
                [], [], 
                '''                Configures IPv4 NTP Peers or Servers
                ''',
                'peer_ipv4s',
                'Cisco-IOS-XR-ip-ntp-cfg', False),
            _MetaInfoClassMember('peer-ipv6s', REFERENCE_CLASS, 'PeerIpv6S' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg', 'Ntp.PeerVrfs.PeerVrf.PeerIpv6S', 
                [], [], 
                '''                Configuration NTP Peers or Servers of IPV6
                ''',
                'peer_ipv6s',
                'Cisco-IOS-XR-ip-ntp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-ntp-cfg',
            'peer-vrf',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-ntp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg'
        ),
    },
    'Ntp.PeerVrfs' : {
        'meta_info' : _MetaInfoClass('Ntp.PeerVrfs',
            False, 
            [
            _MetaInfoClassMember('peer-vrf', REFERENCE_LIST, 'PeerVrf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg', 'Ntp.PeerVrfs.PeerVrf', 
                [], [], 
                '''                Configures NTP Peers or Servers for a single
                VRF. The 'default' must also be specified for
                default VRF
                ''',
                'peer_vrf',
                'Cisco-IOS-XR-ip-ntp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-ntp-cfg',
            'peer-vrfs',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-ntp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg'
        ),
    },
    'Ntp.DscpIpv4' : {
        'meta_info' : _MetaInfoClass('Ntp.DscpIpv4',
            False, 
            [
            _MetaInfoClassMember('dscp-or-precedence-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '63')], [], 
                '''                If Mode is set to 'NTPPRECEDENCE(0)' specify
                Precedence value , if Mode is set to
                'NTPDSCP(1)' specify DSCP
                ''',
                'dscp_or_precedence_value',
                'Cisco-IOS-XR-ip-ntp-cfg', False),
            _MetaInfoClassMember('mode', REFERENCE_ENUM_CLASS, 'NtpdscpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg', 'NtpdscpEnum', 
                [], [], 
                '''                NTPPRECEDENCE (0) to specify Precedence value 
                NTPDSCP (1) to specify DSCP value
                ''',
                'mode',
                'Cisco-IOS-XR-ip-ntp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-ntp-cfg',
            'dscp-ipv4',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-ntp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg'
        ),
    },
    'Ntp.DscpIpv6' : {
        'meta_info' : _MetaInfoClass('Ntp.DscpIpv6',
            False, 
            [
            _MetaInfoClassMember('dscp-or-precedence-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '63')], [], 
                '''                If Mode is set to 'NTPPRECEDENCE(0)' specify
                Precedence value , if Mode is set to
                'NTPDSCP(1)' specify DSCP
                ''',
                'dscp_or_precedence_value',
                'Cisco-IOS-XR-ip-ntp-cfg', False),
            _MetaInfoClassMember('mode', REFERENCE_ENUM_CLASS, 'NtpdscpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg', 'NtpdscpEnum', 
                [], [], 
                '''                NTPPRECEDENCE(0) to specify Precedence value
                NTPDSCP(1) to specify DSCP value
                ''',
                'mode',
                'Cisco-IOS-XR-ip-ntp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-ntp-cfg',
            'dscp-ipv6',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-ntp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg'
        ),
    },
    'Ntp.Sources.Source' : {
        'meta_info' : _MetaInfoClass('Ntp.Sources.Source',
            False, 
            [
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ip-ntp-cfg', True),
            _MetaInfoClassMember('source-interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Source Interface for NTP
                ''',
                'source_interface',
                'Cisco-IOS-XR-ip-ntp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-ntp-cfg',
            'source',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-ntp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg'
        ),
    },
    'Ntp.Sources' : {
        'meta_info' : _MetaInfoClass('Ntp.Sources',
            False, 
            [
            _MetaInfoClassMember('source', REFERENCE_LIST, 'Source' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg', 'Ntp.Sources.Source', 
                [], [], 
                '''                Configure  NTP source interface
                ''',
                'source',
                'Cisco-IOS-XR-ip-ntp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-ntp-cfg',
            'sources',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-ntp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg'
        ),
    },
    'Ntp.Authentication.Keies.Key' : {
        'meta_info' : _MetaInfoClass('Ntp.Authentication.Keies.Key',
            False, 
            [
            _MetaInfoClassMember('key-number', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Authentication Key number
                ''',
                'key_number',
                'Cisco-IOS-XR-ip-ntp-cfg', True),
            _MetaInfoClassMember('authentication-key', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Authentication key - maximum 32 characters
                ''',
                'authentication_key',
                'Cisco-IOS-XR-ip-ntp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-ntp-cfg',
            'key',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-ntp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg'
        ),
    },
    'Ntp.Authentication.Keies' : {
        'meta_info' : _MetaInfoClass('Ntp.Authentication.Keies',
            False, 
            [
            _MetaInfoClassMember('key', REFERENCE_LIST, 'Key' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg', 'Ntp.Authentication.Keies.Key', 
                [], [], 
                '''                Authentication key for trusted time sources
                ''',
                'key',
                'Cisco-IOS-XR-ip-ntp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-ntp-cfg',
            'keies',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-ntp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg'
        ),
    },
    'Ntp.Authentication.TrustedKeies.TrustedKey' : {
        'meta_info' : _MetaInfoClass('Ntp.Authentication.TrustedKeies.TrustedKey',
            False, 
            [
            _MetaInfoClassMember('key-number', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Key number
                ''',
                'key_number',
                'Cisco-IOS-XR-ip-ntp-cfg', True),
            ],
            'Cisco-IOS-XR-ip-ntp-cfg',
            'trusted-key',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-ntp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg'
        ),
    },
    'Ntp.Authentication.TrustedKeies' : {
        'meta_info' : _MetaInfoClass('Ntp.Authentication.TrustedKeies',
            False, 
            [
            _MetaInfoClassMember('trusted-key', REFERENCE_LIST, 'TrustedKey' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg', 'Ntp.Authentication.TrustedKeies.TrustedKey', 
                [], [], 
                '''                Configure NTP trusted key
                ''',
                'trusted_key',
                'Cisco-IOS-XR-ip-ntp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-ntp-cfg',
            'trusted-keies',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-ntp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg'
        ),
    },
    'Ntp.Authentication' : {
        'meta_info' : _MetaInfoClass('Ntp.Authentication',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable NTP authentication keys
                ''',
                'enable',
                'Cisco-IOS-XR-ip-ntp-cfg', False),
            _MetaInfoClassMember('keies', REFERENCE_CLASS, 'Keies' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg', 'Ntp.Authentication.Keies', 
                [], [], 
                '''                Authentication Key Table
                ''',
                'keies',
                'Cisco-IOS-XR-ip-ntp-cfg', False),
            _MetaInfoClassMember('trusted-keies', REFERENCE_CLASS, 'TrustedKeies' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg', 'Ntp.Authentication.TrustedKeies', 
                [], [], 
                '''                Key numbers for trusted time sources
                ''',
                'trusted_keies',
                'Cisco-IOS-XR-ip-ntp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-ntp-cfg',
            'authentication',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-ntp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg'
        ),
    },
    'Ntp.Passive' : {
        'meta_info' : _MetaInfoClass('Ntp.Passive',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable NTP Passive associations
                ''',
                'enable',
                'Cisco-IOS-XR-ip-ntp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-ntp-cfg',
            'passive',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-ntp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg'
        ),
    },
    'Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceMulticast.MulticastClients.MulticastClient' : {
        'meta_info' : _MetaInfoClass('Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceMulticast.MulticastClients.MulticastClient',
            False, 
            [
            _MetaInfoClassMember('ip-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IP address of a multicast group
                ''',
                'ip_address',
                'Cisco-IOS-XR-ip-ntp-cfg', True, [
                    _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP address of a multicast group
                        ''',
                        'ip_address',
                        'Cisco-IOS-XR-ip-ntp-cfg', True),
                    _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP address of a multicast group
                        ''',
                        'ip_address',
                        'Cisco-IOS-XR-ip-ntp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-ip-ntp-cfg',
            'multicast-client',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-ntp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg'
        ),
    },
    'Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceMulticast.MulticastClients' : {
        'meta_info' : _MetaInfoClass('Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceMulticast.MulticastClients',
            False, 
            [
            _MetaInfoClassMember('multicast-client', REFERENCE_LIST, 'MulticastClient' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg', 'Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceMulticast.MulticastClients.MulticastClient', 
                [], [], 
                '''                Listen to NTP multicasts
                ''',
                'multicast_client',
                'Cisco-IOS-XR-ip-ntp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-ntp-cfg',
            'multicast-clients',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-ntp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg'
        ),
    },
    'Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceMulticast.MulticastServers.MulticastServer' : {
        'meta_info' : _MetaInfoClass('Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceMulticast.MulticastServers.MulticastServer',
            False, 
            [
            _MetaInfoClassMember('ip-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IP address of a multicast group
                ''',
                'ip_address',
                'Cisco-IOS-XR-ip-ntp-cfg', True, [
                    _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP address of a multicast group
                        ''',
                        'ip_address',
                        'Cisco-IOS-XR-ip-ntp-cfg', True),
                    _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP address of a multicast group
                        ''',
                        'ip_address',
                        'Cisco-IOS-XR-ip-ntp-cfg', True),
                ]),
            _MetaInfoClassMember('authentication-key', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Authentication key
                ''',
                'authentication_key',
                'Cisco-IOS-XR-ip-ntp-cfg', False),
            _MetaInfoClassMember('ttl', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                TTL
                ''',
                'ttl',
                'Cisco-IOS-XR-ip-ntp-cfg', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'int' , None, None, 
                [('2', '4')], [], 
                '''                NTP version
                ''',
                'version',
                'Cisco-IOS-XR-ip-ntp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-ntp-cfg',
            'multicast-server',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-ntp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg'
        ),
    },
    'Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceMulticast.MulticastServers' : {
        'meta_info' : _MetaInfoClass('Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceMulticast.MulticastServers',
            False, 
            [
            _MetaInfoClassMember('multicast-server', REFERENCE_LIST, 'MulticastServer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg', 'Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceMulticast.MulticastServers.MulticastServer', 
                [], [], 
                '''                Configure NTP multicast group server peer
                ''',
                'multicast_server',
                'Cisco-IOS-XR-ip-ntp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-ntp-cfg',
            'multicast-servers',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-ntp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg'
        ),
    },
    'Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceMulticast' : {
        'meta_info' : _MetaInfoClass('Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceMulticast',
            False, 
            [
            _MetaInfoClassMember('multicast-clients', REFERENCE_CLASS, 'MulticastClients' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg', 'Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceMulticast.MulticastClients', 
                [], [], 
                '''                Configures multicast client peers
                ''',
                'multicast_clients',
                'Cisco-IOS-XR-ip-ntp-cfg', False),
            _MetaInfoClassMember('multicast-servers', REFERENCE_CLASS, 'MulticastServers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg', 'Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceMulticast.MulticastServers', 
                [], [], 
                '''                Configures multicast server peers
                ''',
                'multicast_servers',
                'Cisco-IOS-XR-ip-ntp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-ntp-cfg',
            'interface-multicast',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-ntp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg'
        ),
    },
    'Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceBroadcast.Broadcast' : {
        'meta_info' : _MetaInfoClass('Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceBroadcast.Broadcast',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Destination broadcast IPv4 address
                ''',
                'address',
                'Cisco-IOS-XR-ip-ntp-cfg', False),
            _MetaInfoClassMember('authentication-key', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Authentication key
                ''',
                'authentication_key',
                'Cisco-IOS-XR-ip-ntp-cfg', False),
            _MetaInfoClassMember('ntp-version', ATTRIBUTE, 'int' , None, None, 
                [('2', '4')], [], 
                '''                NTP version
                ''',
                'ntp_version',
                'Cisco-IOS-XR-ip-ntp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-ntp-cfg',
            'broadcast',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-ntp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg'
        ),
    },
    'Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceBroadcast' : {
        'meta_info' : _MetaInfoClass('Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceBroadcast',
            False, 
            [
            _MetaInfoClassMember('broadcast', REFERENCE_CLASS, 'Broadcast' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg', 'Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceBroadcast.Broadcast', 
                [], [], 
                '''                Configure NTP broadcast
                ''',
                'broadcast',
                'Cisco-IOS-XR-ip-ntp-cfg', False),
            _MetaInfoClassMember('broadcast-client', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Listen to NTP broadcasts
                ''',
                'broadcast_client',
                'Cisco-IOS-XR-ip-ntp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-ntp-cfg',
            'interface-broadcast',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-ntp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg'
        ),
    },
    'Ntp.InterfaceTables.InterfaceTable.Interface' : {
        'meta_info' : _MetaInfoClass('Ntp.InterfaceTables.InterfaceTable.Interface',
            False, 
            [
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                interface
                ''',
                'interface',
                'Cisco-IOS-XR-ip-ntp-cfg', True),
            _MetaInfoClassMember('disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable NTP
                ''',
                'disable',
                'Cisco-IOS-XR-ip-ntp-cfg', False),
            _MetaInfoClassMember('interface-broadcast', REFERENCE_CLASS, 'InterfaceBroadcast' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg', 'Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceBroadcast', 
                [], [], 
                '''                Configure NTP broadcast service
                ''',
                'interface_broadcast',
                'Cisco-IOS-XR-ip-ntp-cfg', False),
            _MetaInfoClassMember('interface-multicast', REFERENCE_CLASS, 'InterfaceMulticast' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg', 'Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceMulticast', 
                [], [], 
                '''                Configure NTP multicast service
                ''',
                'interface_multicast',
                'Cisco-IOS-XR-ip-ntp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-ntp-cfg',
            'interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-ntp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg'
        ),
    },
    'Ntp.InterfaceTables.InterfaceTable' : {
        'meta_info' : _MetaInfoClass('Ntp.InterfaceTables.InterfaceTable',
            False, 
            [
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ip-ntp-cfg', True),
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg', 'Ntp.InterfaceTables.InterfaceTable.Interface', 
                [], [], 
                '''                Name of the interface
                ''',
                'interface',
                'Cisco-IOS-XR-ip-ntp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-ntp-cfg',
            'interface-table',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-ntp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg'
        ),
    },
    'Ntp.InterfaceTables' : {
        'meta_info' : _MetaInfoClass('Ntp.InterfaceTables',
            False, 
            [
            _MetaInfoClassMember('interface-table', REFERENCE_LIST, 'InterfaceTable' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg', 'Ntp.InterfaceTables.InterfaceTable', 
                [], [], 
                '''                NTP per interface configuration
                ''',
                'interface_table',
                'Cisco-IOS-XR-ip-ntp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-ntp-cfg',
            'interface-tables',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-ntp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg'
        ),
    },
    'Ntp.AccessGroupTables.AccessGroupTable.AccessGroupAfTable.AccessGroup' : {
        'meta_info' : _MetaInfoClass('Ntp.AccessGroupTables.AccessGroupTable.AccessGroupAfTable.AccessGroup',
            False, 
            [
            _MetaInfoClassMember('access-group-type', REFERENCE_ENUM_CLASS, 'NtpAccessEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg', 'NtpAccessEnum', 
                [], [], 
                '''                Access group type
                ''',
                'access_group_type',
                'Cisco-IOS-XR-ip-ntp-cfg', True),
            _MetaInfoClassMember('access-list-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Access list name - maximum 32 characters
                ''',
                'access_list_name',
                'Cisco-IOS-XR-ip-ntp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-ntp-cfg',
            'access-group',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-ntp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg'
        ),
    },
    'Ntp.AccessGroupTables.AccessGroupTable.AccessGroupAfTable' : {
        'meta_info' : _MetaInfoClass('Ntp.AccessGroupTables.AccessGroupTable.AccessGroupAfTable',
            False, 
            [
            _MetaInfoClassMember('af', REFERENCE_ENUM_CLASS, 'NtpAccessAfEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg', 'NtpAccessAfEnum', 
                [], [], 
                '''                Address family
                ''',
                'af',
                'Cisco-IOS-XR-ip-ntp-cfg', True),
            _MetaInfoClassMember('access-group', REFERENCE_LIST, 'AccessGroup' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg', 'Ntp.AccessGroupTables.AccessGroupTable.AccessGroupAfTable.AccessGroup', 
                [], [], 
                '''                Configure NTP access group
                ''',
                'access_group',
                'Cisco-IOS-XR-ip-ntp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-ntp-cfg',
            'access-group-af-table',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-ntp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg'
        ),
    },
    'Ntp.AccessGroupTables.AccessGroupTable' : {
        'meta_info' : _MetaInfoClass('Ntp.AccessGroupTables.AccessGroupTable',
            False, 
            [
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ip-ntp-cfg', True),
            _MetaInfoClassMember('access-group-af-table', REFERENCE_LIST, 'AccessGroupAfTable' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg', 'Ntp.AccessGroupTables.AccessGroupTable.AccessGroupAfTable', 
                [], [], 
                '''                Configure NTP access address family
                ''',
                'access_group_af_table',
                'Cisco-IOS-XR-ip-ntp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-ntp-cfg',
            'access-group-table',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-ntp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg'
        ),
    },
    'Ntp.AccessGroupTables' : {
        'meta_info' : _MetaInfoClass('Ntp.AccessGroupTables',
            False, 
            [
            _MetaInfoClassMember('access-group-table', REFERENCE_LIST, 'AccessGroupTable' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg', 'Ntp.AccessGroupTables.AccessGroupTable', 
                [], [], 
                '''                Control NTP access
                ''',
                'access_group_table',
                'Cisco-IOS-XR-ip-ntp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-ntp-cfg',
            'access-group-tables',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-ntp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg'
        ),
    },
    'Ntp' : {
        'meta_info' : _MetaInfoClass('Ntp',
            False, 
            [
            _MetaInfoClassMember('access-group-tables', REFERENCE_CLASS, 'AccessGroupTables' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg', 'Ntp.AccessGroupTables', 
                [], [], 
                '''                Control NTP access
                ''',
                'access_group_tables',
                'Cisco-IOS-XR-ip-ntp-cfg', False),
            _MetaInfoClassMember('authentication', REFERENCE_CLASS, 'Authentication' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg', 'Ntp.Authentication', 
                [], [], 
                '''                Configure NTP Authentication keys
                ''',
                'authentication',
                'Cisco-IOS-XR-ip-ntp-cfg', False),
            _MetaInfoClassMember('broadcast-delay', ATTRIBUTE, 'int' , None, None, 
                [('1', '999999')], [], 
                '''                Estimated round-trip delay
                ''',
                'broadcast_delay',
                'Cisco-IOS-XR-ip-ntp-cfg', False),
            _MetaInfoClassMember('dscp-ipv4', REFERENCE_CLASS, 'DscpIpv4' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg', 'Ntp.DscpIpv4', 
                [], [], 
                '''                 Set IP DSCP value for outgoing NTP IPV4 packets
                ''',
                'dscp_ipv4',
                'Cisco-IOS-XR-ip-ntp-cfg', False),
            _MetaInfoClassMember('dscp-ipv6', REFERENCE_CLASS, 'DscpIpv6' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg', 'Ntp.DscpIpv6', 
                [], [], 
                '''                 Set IP DSCP value for outgoing NTP IPV6 packets
                ''',
                'dscp_ipv6',
                'Cisco-IOS-XR-ip-ntp-cfg', False),
            _MetaInfoClassMember('interface-tables', REFERENCE_CLASS, 'InterfaceTables' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg', 'Ntp.InterfaceTables', 
                [], [], 
                '''                NTP per interface configuration
                ''',
                'interface_tables',
                'Cisco-IOS-XR-ip-ntp-cfg', False),
            _MetaInfoClassMember('log-internal-sync', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                To enable logging internal sync conflicts
                ''',
                'log_internal_sync',
                'Cisco-IOS-XR-ip-ntp-cfg', False),
            _MetaInfoClassMember('master', ATTRIBUTE, 'int' , None, None, 
                [('1', '15')], [], 
                '''                Act as NTP master clock
                ''',
                'master',
                'Cisco-IOS-XR-ip-ntp-cfg', False),
            _MetaInfoClassMember('max-associations', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Set maximum number of associations
                ''',
                'max_associations',
                'Cisco-IOS-XR-ip-ntp-cfg', False),
            _MetaInfoClassMember('passive', REFERENCE_CLASS, 'Passive' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg', 'Ntp.Passive', 
                [], [], 
                '''                Configure NTP passive associations
                ''',
                'passive',
                'Cisco-IOS-XR-ip-ntp-cfg', False),
            _MetaInfoClassMember('peer-vrfs', REFERENCE_CLASS, 'PeerVrfs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg', 'Ntp.PeerVrfs', 
                [], [], 
                '''                Configures NTP Peers or Servers
                ''',
                'peer_vrfs',
                'Cisco-IOS-XR-ip-ntp-cfg', False),
            _MetaInfoClassMember('sources', REFERENCE_CLASS, 'Sources' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg', 'Ntp.Sources', 
                [], [], 
                '''                Configure  NTP source interface
                ''',
                'sources',
                'Cisco-IOS-XR-ip-ntp-cfg', False),
            _MetaInfoClassMember('update-calendar', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                To enable calendar update with NTP time
                ''',
                'update_calendar',
                'Cisco-IOS-XR-ip-ntp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-ntp-cfg',
            'ntp',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-ntp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_ntp_cfg'
        ),
    },
}
_meta_table['Ntp.PeerVrfs.PeerVrf.PeerIpv4S.PeerIpv4.PeerTypeIpv4']['meta_info'].parent =_meta_table['Ntp.PeerVrfs.PeerVrf.PeerIpv4S.PeerIpv4']['meta_info']
_meta_table['Ntp.PeerVrfs.PeerVrf.PeerIpv4S.PeerIpv4']['meta_info'].parent =_meta_table['Ntp.PeerVrfs.PeerVrf.PeerIpv4S']['meta_info']
_meta_table['Ntp.PeerVrfs.PeerVrf.PeerIpv6S.PeerIpv6.PeerTypeIpv6']['meta_info'].parent =_meta_table['Ntp.PeerVrfs.PeerVrf.PeerIpv6S.PeerIpv6']['meta_info']
_meta_table['Ntp.PeerVrfs.PeerVrf.PeerIpv6S.PeerIpv6']['meta_info'].parent =_meta_table['Ntp.PeerVrfs.PeerVrf.PeerIpv6S']['meta_info']
_meta_table['Ntp.PeerVrfs.PeerVrf.PeerIpv4S']['meta_info'].parent =_meta_table['Ntp.PeerVrfs.PeerVrf']['meta_info']
_meta_table['Ntp.PeerVrfs.PeerVrf.PeerIpv6S']['meta_info'].parent =_meta_table['Ntp.PeerVrfs.PeerVrf']['meta_info']
_meta_table['Ntp.PeerVrfs.PeerVrf']['meta_info'].parent =_meta_table['Ntp.PeerVrfs']['meta_info']
_meta_table['Ntp.Sources.Source']['meta_info'].parent =_meta_table['Ntp.Sources']['meta_info']
_meta_table['Ntp.Authentication.Keies.Key']['meta_info'].parent =_meta_table['Ntp.Authentication.Keies']['meta_info']
_meta_table['Ntp.Authentication.TrustedKeies.TrustedKey']['meta_info'].parent =_meta_table['Ntp.Authentication.TrustedKeies']['meta_info']
_meta_table['Ntp.Authentication.Keies']['meta_info'].parent =_meta_table['Ntp.Authentication']['meta_info']
_meta_table['Ntp.Authentication.TrustedKeies']['meta_info'].parent =_meta_table['Ntp.Authentication']['meta_info']
_meta_table['Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceMulticast.MulticastClients.MulticastClient']['meta_info'].parent =_meta_table['Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceMulticast.MulticastClients']['meta_info']
_meta_table['Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceMulticast.MulticastServers.MulticastServer']['meta_info'].parent =_meta_table['Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceMulticast.MulticastServers']['meta_info']
_meta_table['Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceMulticast.MulticastClients']['meta_info'].parent =_meta_table['Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceMulticast']['meta_info']
_meta_table['Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceMulticast.MulticastServers']['meta_info'].parent =_meta_table['Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceMulticast']['meta_info']
_meta_table['Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceBroadcast.Broadcast']['meta_info'].parent =_meta_table['Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceBroadcast']['meta_info']
_meta_table['Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceMulticast']['meta_info'].parent =_meta_table['Ntp.InterfaceTables.InterfaceTable.Interface']['meta_info']
_meta_table['Ntp.InterfaceTables.InterfaceTable.Interface.InterfaceBroadcast']['meta_info'].parent =_meta_table['Ntp.InterfaceTables.InterfaceTable.Interface']['meta_info']
_meta_table['Ntp.InterfaceTables.InterfaceTable.Interface']['meta_info'].parent =_meta_table['Ntp.InterfaceTables.InterfaceTable']['meta_info']
_meta_table['Ntp.InterfaceTables.InterfaceTable']['meta_info'].parent =_meta_table['Ntp.InterfaceTables']['meta_info']
_meta_table['Ntp.AccessGroupTables.AccessGroupTable.AccessGroupAfTable.AccessGroup']['meta_info'].parent =_meta_table['Ntp.AccessGroupTables.AccessGroupTable.AccessGroupAfTable']['meta_info']
_meta_table['Ntp.AccessGroupTables.AccessGroupTable.AccessGroupAfTable']['meta_info'].parent =_meta_table['Ntp.AccessGroupTables.AccessGroupTable']['meta_info']
_meta_table['Ntp.AccessGroupTables.AccessGroupTable']['meta_info'].parent =_meta_table['Ntp.AccessGroupTables']['meta_info']
_meta_table['Ntp.PeerVrfs']['meta_info'].parent =_meta_table['Ntp']['meta_info']
_meta_table['Ntp.DscpIpv4']['meta_info'].parent =_meta_table['Ntp']['meta_info']
_meta_table['Ntp.DscpIpv6']['meta_info'].parent =_meta_table['Ntp']['meta_info']
_meta_table['Ntp.Sources']['meta_info'].parent =_meta_table['Ntp']['meta_info']
_meta_table['Ntp.Authentication']['meta_info'].parent =_meta_table['Ntp']['meta_info']
_meta_table['Ntp.Passive']['meta_info'].parent =_meta_table['Ntp']['meta_info']
_meta_table['Ntp.InterfaceTables']['meta_info'].parent =_meta_table['Ntp']['meta_info']
_meta_table['Ntp.AccessGroupTables']['meta_info'].parent =_meta_table['Ntp']['meta_info']
