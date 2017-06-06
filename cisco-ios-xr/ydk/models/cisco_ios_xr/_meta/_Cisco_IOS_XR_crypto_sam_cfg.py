


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'CryptoSamActionEnum' : _MetaInfoEnum('CryptoSamActionEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_cfg',
        {
            'proceed':'proceed',
            'terminate':'terminate',
        }, 'Cisco-IOS-XR-crypto-sam-cfg', _yang_ns._namespaces['Cisco-IOS-XR-crypto-sam-cfg']),
    'Crypto.Sam.PromptInterval' : {
        'meta_info' : _MetaInfoClass('Crypto.Sam.PromptInterval',
            False, 
            [
            _MetaInfoClassMember('action', REFERENCE_ENUM_CLASS, 'CryptoSamActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_cfg', 'CryptoSamActionEnum', 
                [], [], 
                '''                Respond to SAM prompt either Proceed/Terminate
                ''',
                'action',
                'Cisco-IOS-XR-crypto-sam-cfg', False),
            _MetaInfoClassMember('prompt-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '300')], [], 
                '''                Prompt time from 0 - 300 seconds
                ''',
                'prompt_time',
                'Cisco-IOS-XR-crypto-sam-cfg', False),
            ],
            'Cisco-IOS-XR-crypto-sam-cfg',
            'prompt-interval',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-sam-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_cfg'
        ),
    },
    'Crypto.Sam' : {
        'meta_info' : _MetaInfoClass('Crypto.Sam',
            False, 
            [
            _MetaInfoClassMember('prompt-interval', REFERENCE_CLASS, 'PromptInterval' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_cfg', 'Crypto.Sam.PromptInterval', 
                [], [], 
                '''                Set prompt interval at reboot time
                ''',
                'prompt_interval',
                'Cisco-IOS-XR-crypto-sam-cfg', False),
            ],
            'Cisco-IOS-XR-crypto-sam-cfg',
            'sam',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-sam-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_cfg'
        ),
    },
    'Crypto.Ssh.Client' : {
        'meta_info' : _MetaInfoClass('Crypto.Ssh.Client',
            False, 
            [
            _MetaInfoClassMember('client-vrf', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Source interface VRF for ssh client sessions
                ''',
                'client_vrf',
                'Cisco-IOS-XR-crypto-ssh-cfg', False),
            _MetaInfoClassMember('dscp', ATTRIBUTE, 'int' , None, None, 
                [('0', '63')], [], 
                '''                Cisco sshd DSCP value
                ''',
                'dscp',
                'Cisco-IOS-XR-crypto-ssh-cfg', False),
            _MetaInfoClassMember('host-public-key', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Filename - where to store known host file
                ''',
                'host_public_key',
                'Cisco-IOS-XR-crypto-ssh-cfg', False),
            _MetaInfoClassMember('source-interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Source interface for ssh client sessions
                ''',
                'source_interface',
                'Cisco-IOS-XR-crypto-ssh-cfg', False),
            ],
            'Cisco-IOS-XR-crypto-ssh-cfg',
            'client',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-ssh-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_cfg'
        ),
    },
    'Crypto.Ssh.Server.Disable.Hmac' : {
        'meta_info' : _MetaInfoClass('Crypto.Ssh.Server.Disable.Hmac',
            False, 
            [
            _MetaInfoClassMember('hmac-sha512', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Disable Hmac-sha2-512 negotiation
                ''',
                'hmac_sha512',
                'Cisco-IOS-XR-crypto-ssh-cfg', False),
            ],
            'Cisco-IOS-XR-crypto-ssh-cfg',
            'hmac',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-ssh-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_cfg'
        ),
    },
    'Crypto.Ssh.Server.Disable' : {
        'meta_info' : _MetaInfoClass('Crypto.Ssh.Server.Disable',
            False, 
            [
            _MetaInfoClassMember('hmac', REFERENCE_CLASS, 'Hmac' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_cfg', 'Crypto.Ssh.Server.Disable.Hmac', 
                [], [], 
                '''                hmac
                ''',
                'hmac',
                'Cisco-IOS-XR-crypto-ssh-cfg', False),
            ],
            'Cisco-IOS-XR-crypto-ssh-cfg',
            'disable',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-ssh-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_cfg'
        ),
    },
    'Crypto.Ssh.Server.VrfTable.Vrf' : {
        'meta_info' : _MetaInfoClass('Crypto.Ssh.Server.VrfTable.Vrf',
            False, 
            [
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Enter VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-crypto-ssh-cfg', True),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable to use VRF
                ''',
                'enable',
                'Cisco-IOS-XR-crypto-ssh-cfg', False),
            _MetaInfoClassMember('ipv4-access-list', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                SSH v4 access-list name
                ''',
                'ipv4_access_list',
                'Cisco-IOS-XR-crypto-ssh-cfg', False),
            _MetaInfoClassMember('ipv6-access-list', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                SSH v6 access-list name
                ''',
                'ipv6_access_list',
                'Cisco-IOS-XR-crypto-ssh-cfg', False),
            ],
            'Cisco-IOS-XR-crypto-ssh-cfg',
            'vrf',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-ssh-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_cfg'
        ),
    },
    'Crypto.Ssh.Server.VrfTable' : {
        'meta_info' : _MetaInfoClass('Crypto.Ssh.Server.VrfTable',
            False, 
            [
            _MetaInfoClassMember('vrf', REFERENCE_LIST, 'Vrf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_cfg', 'Crypto.Ssh.Server.VrfTable.Vrf', 
                [], [], 
                '''                Enter VRF name
                ''',
                'vrf',
                'Cisco-IOS-XR-crypto-ssh-cfg', False),
            ],
            'Cisco-IOS-XR-crypto-ssh-cfg',
            'vrf-table',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-ssh-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_cfg'
        ),
    },
    'Crypto.Ssh.Server.NetconfVrfTable.Vrf' : {
        'meta_info' : _MetaInfoClass('Crypto.Ssh.Server.NetconfVrfTable.Vrf',
            False, 
            [
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Enter VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-crypto-ssh-cfg', True),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable to use VRF
                ''',
                'enable',
                'Cisco-IOS-XR-crypto-ssh-cfg', False),
            _MetaInfoClassMember('ipv4-access-list', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                SSH v4 access-list name
                ''',
                'ipv4_access_list',
                'Cisco-IOS-XR-crypto-ssh-cfg', False),
            _MetaInfoClassMember('ipv6-access-list', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                SSH v6 access-list name
                ''',
                'ipv6_access_list',
                'Cisco-IOS-XR-crypto-ssh-cfg', False),
            ],
            'Cisco-IOS-XR-crypto-ssh-cfg',
            'vrf',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-ssh-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_cfg'
        ),
    },
    'Crypto.Ssh.Server.NetconfVrfTable' : {
        'meta_info' : _MetaInfoClass('Crypto.Ssh.Server.NetconfVrfTable',
            False, 
            [
            _MetaInfoClassMember('vrf', REFERENCE_LIST, 'Vrf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_cfg', 'Crypto.Ssh.Server.NetconfVrfTable.Vrf', 
                [], [], 
                '''                Enter VRF name
                ''',
                'vrf',
                'Cisco-IOS-XR-crypto-ssh-cfg', False),
            ],
            'Cisco-IOS-XR-crypto-ssh-cfg',
            'netconf-vrf-table',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-ssh-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_cfg'
        ),
    },
    'Crypto.Ssh.Server' : {
        'meta_info' : _MetaInfoClass('Crypto.Ssh.Server',
            False, 
            [
            _MetaInfoClassMember('disable', REFERENCE_CLASS, 'Disable' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_cfg', 'Crypto.Ssh.Server.Disable', 
                [], [], 
                '''                disable
                ''',
                'disable',
                'Cisco-IOS-XR-crypto-ssh-cfg', False),
            _MetaInfoClassMember('dscp', ATTRIBUTE, 'int' , None, None, 
                [('0', '63')], [], 
                '''                Cisco sshd DSCP value
                ''',
                'dscp',
                'Cisco-IOS-XR-crypto-ssh-cfg', False),
            _MetaInfoClassMember('logging', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable ssh server logging
                ''',
                'logging',
                'Cisco-IOS-XR-crypto-ssh-cfg', False),
            _MetaInfoClassMember('netconf', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                port number on which ssh service to be started
                for netconf
                ''',
                'netconf',
                'Cisco-IOS-XR-crypto-ssh-cfg', False),
            _MetaInfoClassMember('netconf-vrf-table', REFERENCE_CLASS, 'NetconfVrfTable' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_cfg', 'Crypto.Ssh.Server.NetconfVrfTable', 
                [], [], 
                '''                Cisco sshd Netconf VRF name
                ''',
                'netconf_vrf_table',
                'Cisco-IOS-XR-crypto-ssh-cfg', False),
            _MetaInfoClassMember('rate-limit', ATTRIBUTE, 'int' , None, None, 
                [('1', '600')], [], 
                '''                Cisco sshd rate-limit of service requests
                ''',
                'rate_limit',
                'Cisco-IOS-XR-crypto-ssh-cfg', False),
            _MetaInfoClassMember('rekey-time', ATTRIBUTE, 'int' , None, None, 
                [('30', '1440')], [], 
                '''                Time Period in minutes, defalut 60
                ''',
                'rekey_time',
                'Cisco-IOS-XR-crypto-ssh-cfg', False),
            _MetaInfoClassMember('rekey-volume', ATTRIBUTE, 'int' , None, None, 
                [('1024', '4095')], [], 
                '''                Configure volume-based rekey for SSH
                ''',
                'rekey_volume',
                'Cisco-IOS-XR-crypto-ssh-cfg', False),
            _MetaInfoClassMember('session-limit', ATTRIBUTE, 'int' , None, None, 
                [('1', '1024')], [], 
                '''                Cisco sshd session-limit of service requests
                ''',
                'session_limit',
                'Cisco-IOS-XR-crypto-ssh-cfg', False),
            _MetaInfoClassMember('timeout', ATTRIBUTE, 'int' , None, None, 
                [('5', '120')], [], 
                '''                Timeout value between 5-120 seconds defalut 30
                ''',
                'timeout',
                'Cisco-IOS-XR-crypto-ssh-cfg', False),
            _MetaInfoClassMember('v2', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Cisco sshd force protocol version 2 only
                ''',
                'v2',
                'Cisco-IOS-XR-crypto-ssh-cfg', False),
            _MetaInfoClassMember('vrf-table', REFERENCE_CLASS, 'VrfTable' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_cfg', 'Crypto.Ssh.Server.VrfTable', 
                [], [], 
                '''                Cisco sshd VRF name
                ''',
                'vrf_table',
                'Cisco-IOS-XR-crypto-ssh-cfg', False),
            ],
            'Cisco-IOS-XR-crypto-ssh-cfg',
            'server',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-ssh-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_cfg'
        ),
    },
    'Crypto.Ssh' : {
        'meta_info' : _MetaInfoClass('Crypto.Ssh',
            False, 
            [
            _MetaInfoClassMember('client', REFERENCE_CLASS, 'Client' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_cfg', 'Crypto.Ssh.Client', 
                [], [], 
                '''                Provide SSH client service
                ''',
                'client',
                'Cisco-IOS-XR-crypto-ssh-cfg', False),
            _MetaInfoClassMember('server', REFERENCE_CLASS, 'Server' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_cfg', 'Crypto.Ssh.Server', 
                [], [], 
                '''                Provide SSH server service
                ''',
                'server',
                'Cisco-IOS-XR-crypto-ssh-cfg', False),
            ],
            'Cisco-IOS-XR-crypto-ssh-cfg',
            'ssh',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-ssh-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_cfg'
        ),
    },
    'Crypto' : {
        'meta_info' : _MetaInfoClass('Crypto',
            False, 
            [
            _MetaInfoClassMember('sam', REFERENCE_CLASS, 'Sam' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_cfg', 'Crypto.Sam', 
                [], [], 
                '''                Software Authentication Manager (SAM) Config
                ''',
                'sam',
                'Cisco-IOS-XR-crypto-sam-cfg', False),
            _MetaInfoClassMember('ssh', REFERENCE_CLASS, 'Ssh' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_cfg', 'Crypto.Ssh', 
                [], [], 
                '''                Secure Shell configuration
                ''',
                'ssh',
                'Cisco-IOS-XR-crypto-ssh-cfg', False),
            ],
            'Cisco-IOS-XR-crypto-sam-cfg',
            'crypto',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-sam-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_sam_cfg'
        ),
    },
}
_meta_table['Crypto.Sam.PromptInterval']['meta_info'].parent =_meta_table['Crypto.Sam']['meta_info']
_meta_table['Crypto.Ssh.Server.Disable.Hmac']['meta_info'].parent =_meta_table['Crypto.Ssh.Server.Disable']['meta_info']
_meta_table['Crypto.Ssh.Server.VrfTable.Vrf']['meta_info'].parent =_meta_table['Crypto.Ssh.Server.VrfTable']['meta_info']
_meta_table['Crypto.Ssh.Server.NetconfVrfTable.Vrf']['meta_info'].parent =_meta_table['Crypto.Ssh.Server.NetconfVrfTable']['meta_info']
_meta_table['Crypto.Ssh.Server.Disable']['meta_info'].parent =_meta_table['Crypto.Ssh.Server']['meta_info']
_meta_table['Crypto.Ssh.Server.VrfTable']['meta_info'].parent =_meta_table['Crypto.Ssh.Server']['meta_info']
_meta_table['Crypto.Ssh.Server.NetconfVrfTable']['meta_info'].parent =_meta_table['Crypto.Ssh.Server']['meta_info']
_meta_table['Crypto.Ssh.Client']['meta_info'].parent =_meta_table['Crypto.Ssh']['meta_info']
_meta_table['Crypto.Ssh.Server']['meta_info'].parent =_meta_table['Crypto.Ssh']['meta_info']
_meta_table['Crypto.Sam']['meta_info'].parent =_meta_table['Crypto']['meta_info']
_meta_table['Crypto.Ssh']['meta_info'].parent =_meta_table['Crypto']['meta_info']
