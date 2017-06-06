


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'MacEnum' : _MetaInfoEnum('MacEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper',
        {
            'hmac-md5':'hmac_md5',
            'hmac-sha1':'hmac_sha1',
            'hmac-sha2-256':'hmac_sha2_256',
            'hmac-sha2-512':'hmac_sha2_512',
        }, 'Cisco-IOS-XR-crypto-ssh-oper', _yang_ns._namespaces['Cisco-IOS-XR-crypto-ssh-oper']),
    'KexNameEnum' : _MetaInfoEnum('KexNameEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper',
        {
            'diffie-hellman-group1':'diffie_hellman_group1',
            'diffie-hellman-group14':'diffie_hellman_group14',
            'diffie-hellman-group15':'diffie_hellman_group15',
            'diffie-hellman-group16':'diffie_hellman_group16',
            'diffie-hellman-group17':'diffie_hellman_group17',
            'diffie-hellman-group18':'diffie_hellman_group18',
            'ecdh-nistp256':'ecdh_nistp256',
            'ecdh-nistp384':'ecdh_nistp384',
            'ecdh-nistp521':'ecdh_nistp521',
            'password-authenticated':'password_authenticated',
        }, 'Cisco-IOS-XR-crypto-ssh-oper', _yang_ns._namespaces['Cisco-IOS-XR-crypto-ssh-oper']),
    'ConnectionEnum' : _MetaInfoEnum('ConnectionEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper',
        {
            'undefined':'undefined',
            'shell':'shell',
            'exec':'exec_',
            'scp':'scp',
            'sftp-subsystem':'sftp_subsystem',
            'netconf-subsystem':'netconf_subsystem',
        }, 'Cisco-IOS-XR-crypto-ssh-oper', _yang_ns._namespaces['Cisco-IOS-XR-crypto-ssh-oper']),
    'StatesEnum' : _MetaInfoEnum('StatesEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper',
        {
            'open':'open',
            'version-ok':'version_ok',
            'key-exchange-initialize':'key_exchange_initialize',
            'key-exchange-dh':'key_exchange_dh',
            'new-keys':'new_keys',
            'authenticate-information':'authenticate_information',
            'authenticated':'authenticated',
            'channel-open':'channel_open',
            'pty-open':'pty_open',
            'session-open':'session_open',
            'rekey':'rekey',
            'suspended':'suspended',
            'session-closed':'session_closed',
        }, 'Cisco-IOS-XR-crypto-ssh-oper', _yang_ns._namespaces['Cisco-IOS-XR-crypto-ssh-oper']),
    'CipherEnum' : _MetaInfoEnum('CipherEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper',
        {
            'aes128-cbc':'aes128_cbc',
            'aes192-cbc':'aes192_cbc',
            'aes256-cbc':'aes256_cbc',
            'triple-des-cbc':'triple_des_cbc',
            'aes128-ctr':'aes128_ctr',
            'aes192-ctr':'aes192_ctr',
            'aes256-ctr':'aes256_ctr',
        }, 'Cisco-IOS-XR-crypto-ssh-oper', _yang_ns._namespaces['Cisco-IOS-XR-crypto-ssh-oper']),
    'VersionEnum' : _MetaInfoEnum('VersionEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper',
        {
            'v2':'v2',
            'v1':'v1',
        }, 'Cisco-IOS-XR-crypto-ssh-oper', _yang_ns._namespaces['Cisco-IOS-XR-crypto-ssh-oper']),
    'AuthenEnum' : _MetaInfoEnum('AuthenEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper',
        {
            'password':'password',
            'rsa-public-key':'rsa_public_key',
            'keyboard-interactive':'keyboard_interactive',
        }, 'Cisco-IOS-XR-crypto-ssh-oper', _yang_ns._namespaces['Cisco-IOS-XR-crypto-ssh-oper']),
    'HostkeyEnum' : _MetaInfoEnum('HostkeyEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper',
        {
            'ssh-dss':'ssh_dss',
            'ssh-rsa':'ssh_rsa',
        }, 'Cisco-IOS-XR-crypto-ssh-oper', _yang_ns._namespaces['Cisco-IOS-XR-crypto-ssh-oper']),
    'Ssh1.Kex.Nodes.Node.IncomingSessions.SessionDetailInfo' : {
        'meta_info' : _MetaInfoClass('Ssh1.Kex.Nodes.Node.IncomingSessions.SessionDetailInfo',
            False, 
            [
            _MetaInfoClassMember('in-cipher', REFERENCE_ENUM_CLASS, 'CipherEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper', 'CipherEnum', 
                [], [], 
                '''                In cipher algorithm
                ''',
                'in_cipher',
                'Cisco-IOS-XR-crypto-ssh-oper', False),
            _MetaInfoClassMember('in-mac', REFERENCE_ENUM_CLASS, 'MacEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper', 'MacEnum', 
                [], [], 
                '''                In MAC
                ''',
                'in_mac',
                'Cisco-IOS-XR-crypto-ssh-oper', False),
            _MetaInfoClassMember('key-exchange', REFERENCE_ENUM_CLASS, 'KexNameEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper', 'KexNameEnum', 
                [], [], 
                '''                Key exchange name
                ''',
                'key_exchange',
                'Cisco-IOS-XR-crypto-ssh-oper', False),
            _MetaInfoClassMember('out-cipher', REFERENCE_ENUM_CLASS, 'CipherEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper', 'CipherEnum', 
                [], [], 
                '''                Out cipher algorithm
                ''',
                'out_cipher',
                'Cisco-IOS-XR-crypto-ssh-oper', False),
            _MetaInfoClassMember('out-mac', REFERENCE_ENUM_CLASS, 'MacEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper', 'MacEnum', 
                [], [], 
                '''                Out MAC
                ''',
                'out_mac',
                'Cisco-IOS-XR-crypto-ssh-oper', False),
            _MetaInfoClassMember('public-key', REFERENCE_ENUM_CLASS, 'HostkeyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper', 'HostkeyEnum', 
                [], [], 
                '''                Host key algorithm
                ''',
                'public_key',
                'Cisco-IOS-XR-crypto-ssh-oper', False),
            _MetaInfoClassMember('session-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Session ID
                ''',
                'session_id',
                'Cisco-IOS-XR-crypto-ssh-oper', False),
            ],
            'Cisco-IOS-XR-crypto-ssh-oper',
            'session-detail-info',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-ssh-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper'
        ),
    },
    'Ssh1.Kex.Nodes.Node.IncomingSessions' : {
        'meta_info' : _MetaInfoClass('Ssh1.Kex.Nodes.Node.IncomingSessions',
            False, 
            [
            _MetaInfoClassMember('session-detail-info', REFERENCE_LIST, 'SessionDetailInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper', 'Ssh1.Kex.Nodes.Node.IncomingSessions.SessionDetailInfo', 
                [], [], 
                '''                session detail info
                ''',
                'session_detail_info',
                'Cisco-IOS-XR-crypto-ssh-oper', False),
            ],
            'Cisco-IOS-XR-crypto-ssh-oper',
            'incoming-sessions',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-ssh-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper'
        ),
    },
    'Ssh1.Kex.Nodes.Node.OutgoingConnections.SessionDetailInfo' : {
        'meta_info' : _MetaInfoClass('Ssh1.Kex.Nodes.Node.OutgoingConnections.SessionDetailInfo',
            False, 
            [
            _MetaInfoClassMember('in-cipher', REFERENCE_ENUM_CLASS, 'CipherEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper', 'CipherEnum', 
                [], [], 
                '''                In cipher algorithm
                ''',
                'in_cipher',
                'Cisco-IOS-XR-crypto-ssh-oper', False),
            _MetaInfoClassMember('in-mac', REFERENCE_ENUM_CLASS, 'MacEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper', 'MacEnum', 
                [], [], 
                '''                In MAC
                ''',
                'in_mac',
                'Cisco-IOS-XR-crypto-ssh-oper', False),
            _MetaInfoClassMember('key-exchange', REFERENCE_ENUM_CLASS, 'KexNameEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper', 'KexNameEnum', 
                [], [], 
                '''                Key exchange name
                ''',
                'key_exchange',
                'Cisco-IOS-XR-crypto-ssh-oper', False),
            _MetaInfoClassMember('out-cipher', REFERENCE_ENUM_CLASS, 'CipherEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper', 'CipherEnum', 
                [], [], 
                '''                Out cipher algorithm
                ''',
                'out_cipher',
                'Cisco-IOS-XR-crypto-ssh-oper', False),
            _MetaInfoClassMember('out-mac', REFERENCE_ENUM_CLASS, 'MacEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper', 'MacEnum', 
                [], [], 
                '''                Out MAC
                ''',
                'out_mac',
                'Cisco-IOS-XR-crypto-ssh-oper', False),
            _MetaInfoClassMember('public-key', REFERENCE_ENUM_CLASS, 'HostkeyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper', 'HostkeyEnum', 
                [], [], 
                '''                Host key algorithm
                ''',
                'public_key',
                'Cisco-IOS-XR-crypto-ssh-oper', False),
            _MetaInfoClassMember('session-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Session ID
                ''',
                'session_id',
                'Cisco-IOS-XR-crypto-ssh-oper', False),
            ],
            'Cisco-IOS-XR-crypto-ssh-oper',
            'session-detail-info',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-ssh-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper'
        ),
    },
    'Ssh1.Kex.Nodes.Node.OutgoingConnections' : {
        'meta_info' : _MetaInfoClass('Ssh1.Kex.Nodes.Node.OutgoingConnections',
            False, 
            [
            _MetaInfoClassMember('session-detail-info', REFERENCE_LIST, 'SessionDetailInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper', 'Ssh1.Kex.Nodes.Node.OutgoingConnections.SessionDetailInfo', 
                [], [], 
                '''                session detail info
                ''',
                'session_detail_info',
                'Cisco-IOS-XR-crypto-ssh-oper', False),
            ],
            'Cisco-IOS-XR-crypto-ssh-oper',
            'outgoing-connections',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-ssh-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper'
        ),
    },
    'Ssh1.Kex.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('Ssh1.Kex.Nodes.Node',
            False, 
            [
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Node name
                ''',
                'node_name',
                'Cisco-IOS-XR-crypto-ssh-oper', True),
            _MetaInfoClassMember('incoming-sessions', REFERENCE_CLASS, 'IncomingSessions' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper', 'Ssh1.Kex.Nodes.Node.IncomingSessions', 
                [], [], 
                '''                List of incoming sessions
                ''',
                'incoming_sessions',
                'Cisco-IOS-XR-crypto-ssh-oper', False),
            _MetaInfoClassMember('outgoing-connections', REFERENCE_CLASS, 'OutgoingConnections' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper', 'Ssh1.Kex.Nodes.Node.OutgoingConnections', 
                [], [], 
                '''                List of outgoing connections
                ''',
                'outgoing_connections',
                'Cisco-IOS-XR-crypto-ssh-oper', False),
            ],
            'Cisco-IOS-XR-crypto-ssh-oper',
            'node',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-ssh-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper'
        ),
    },
    'Ssh1.Kex.Nodes' : {
        'meta_info' : _MetaInfoClass('Ssh1.Kex.Nodes',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper', 'Ssh1.Kex.Nodes.Node', 
                [], [], 
                '''                SSH session details for a particular node
                ''',
                'node',
                'Cisco-IOS-XR-crypto-ssh-oper', False),
            ],
            'Cisco-IOS-XR-crypto-ssh-oper',
            'nodes',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-ssh-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper'
        ),
    },
    'Ssh1.Kex' : {
        'meta_info' : _MetaInfoClass('Ssh1.Kex',
            False, 
            [
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper', 'Ssh1.Kex.Nodes', 
                [], [], 
                '''                Node-specific ssh session details
                ''',
                'nodes',
                'Cisco-IOS-XR-crypto-ssh-oper', False),
            ],
            'Cisco-IOS-XR-crypto-ssh-oper',
            'kex',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-ssh-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper'
        ),
    },
    'Ssh1' : {
        'meta_info' : _MetaInfoClass('Ssh1',
            False, 
            [
            _MetaInfoClassMember('kex', REFERENCE_CLASS, 'Kex' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper', 'Ssh1.Kex', 
                [], [], 
                '''                key exchange method data
                ''',
                'kex',
                'Cisco-IOS-XR-crypto-ssh-oper', False),
            ],
            'Cisco-IOS-XR-crypto-ssh-oper',
            'ssh1',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-ssh-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper'
        ),
    },
    'Ssh.Session.Rekey.IncomingSessions.SessionRekeyInfo' : {
        'meta_info' : _MetaInfoClass('Ssh.Session.Rekey.IncomingSessions.SessionRekeyInfo',
            False, 
            [
            _MetaInfoClassMember('session-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Session ID
                ''',
                'session_id',
                'Cisco-IOS-XR-crypto-ssh-oper', False),
            _MetaInfoClassMember('session-rekey-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Session Rekey Count
                ''',
                'session_rekey_count',
                'Cisco-IOS-XR-crypto-ssh-oper', False),
            _MetaInfoClassMember('time-to-rekey', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Time To Rekey
                ''',
                'time_to_rekey',
                'Cisco-IOS-XR-crypto-ssh-oper', False),
            _MetaInfoClassMember('volume-to-rekey', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Volume To Rekey
                ''',
                'volume_to_rekey',
                'Cisco-IOS-XR-crypto-ssh-oper', False),
            ],
            'Cisco-IOS-XR-crypto-ssh-oper',
            'session-rekey-info',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-ssh-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper'
        ),
    },
    'Ssh.Session.Rekey.IncomingSessions' : {
        'meta_info' : _MetaInfoClass('Ssh.Session.Rekey.IncomingSessions',
            False, 
            [
            _MetaInfoClassMember('session-rekey-info', REFERENCE_LIST, 'SessionRekeyInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper', 'Ssh.Session.Rekey.IncomingSessions.SessionRekeyInfo', 
                [], [], 
                '''                session rekey info
                ''',
                'session_rekey_info',
                'Cisco-IOS-XR-crypto-ssh-oper', False),
            ],
            'Cisco-IOS-XR-crypto-ssh-oper',
            'incoming-sessions',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-ssh-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper'
        ),
    },
    'Ssh.Session.Rekey.OutgoingConnections.SessionRekeyInfo' : {
        'meta_info' : _MetaInfoClass('Ssh.Session.Rekey.OutgoingConnections.SessionRekeyInfo',
            False, 
            [
            _MetaInfoClassMember('session-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Session ID
                ''',
                'session_id',
                'Cisco-IOS-XR-crypto-ssh-oper', False),
            _MetaInfoClassMember('session-rekey-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Session Rekey Count
                ''',
                'session_rekey_count',
                'Cisco-IOS-XR-crypto-ssh-oper', False),
            _MetaInfoClassMember('time-to-rekey', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Time To Rekey
                ''',
                'time_to_rekey',
                'Cisco-IOS-XR-crypto-ssh-oper', False),
            _MetaInfoClassMember('volume-to-rekey', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Volume To Rekey
                ''',
                'volume_to_rekey',
                'Cisco-IOS-XR-crypto-ssh-oper', False),
            ],
            'Cisco-IOS-XR-crypto-ssh-oper',
            'session-rekey-info',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-ssh-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper'
        ),
    },
    'Ssh.Session.Rekey.OutgoingConnections' : {
        'meta_info' : _MetaInfoClass('Ssh.Session.Rekey.OutgoingConnections',
            False, 
            [
            _MetaInfoClassMember('session-rekey-info', REFERENCE_LIST, 'SessionRekeyInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper', 'Ssh.Session.Rekey.OutgoingConnections.SessionRekeyInfo', 
                [], [], 
                '''                session rekey info
                ''',
                'session_rekey_info',
                'Cisco-IOS-XR-crypto-ssh-oper', False),
            ],
            'Cisco-IOS-XR-crypto-ssh-oper',
            'outgoing-connections',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-ssh-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper'
        ),
    },
    'Ssh.Session.Rekey' : {
        'meta_info' : _MetaInfoClass('Ssh.Session.Rekey',
            False, 
            [
            _MetaInfoClassMember('incoming-sessions', REFERENCE_CLASS, 'IncomingSessions' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper', 'Ssh.Session.Rekey.IncomingSessions', 
                [], [], 
                '''                List of incoming sessions
                ''',
                'incoming_sessions',
                'Cisco-IOS-XR-crypto-ssh-oper', False),
            _MetaInfoClassMember('outgoing-connections', REFERENCE_CLASS, 'OutgoingConnections' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper', 'Ssh.Session.Rekey.OutgoingConnections', 
                [], [], 
                '''                List of outgoing connections
                ''',
                'outgoing_connections',
                'Cisco-IOS-XR-crypto-ssh-oper', False),
            ],
            'Cisco-IOS-XR-crypto-ssh-oper',
            'rekey',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-ssh-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper'
        ),
    },
    'Ssh.Session.Brief.IncomingSessions.SessionBriefInfo' : {
        'meta_info' : _MetaInfoClass('Ssh.Session.Brief.IncomingSessions.SessionBriefInfo',
            False, 
            [
            _MetaInfoClassMember('authentication-type', REFERENCE_ENUM_CLASS, 'AuthenEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper', 'AuthenEnum', 
                [], [], 
                '''                Authentication method
                ''',
                'authentication_type',
                'Cisco-IOS-XR-crypto-ssh-oper', False),
            _MetaInfoClassMember('channel-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Channel ID
                ''',
                'channel_id',
                'Cisco-IOS-XR-crypto-ssh-oper', False),
            _MetaInfoClassMember('connection-type', REFERENCE_ENUM_CLASS, 'ConnectionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper', 'ConnectionEnum', 
                [], [], 
                '''                Channel Connection Type
                ''',
                'connection_type',
                'Cisco-IOS-XR-crypto-ssh-oper', False),
            _MetaInfoClassMember('host-address', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Host address
                ''',
                'host_address',
                'Cisco-IOS-XR-crypto-ssh-oper', False),
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Node name
                ''',
                'node_name',
                'Cisco-IOS-XR-crypto-ssh-oper', False),
            _MetaInfoClassMember('session-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Session ID
                ''',
                'session_id',
                'Cisco-IOS-XR-crypto-ssh-oper', False),
            _MetaInfoClassMember('session-state', REFERENCE_ENUM_CLASS, 'StatesEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper', 'StatesEnum', 
                [], [], 
                '''                SSH session state
                ''',
                'session_state',
                'Cisco-IOS-XR-crypto-ssh-oper', False),
            _MetaInfoClassMember('user-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                User ID
                ''',
                'user_id',
                'Cisco-IOS-XR-crypto-ssh-oper', False),
            _MetaInfoClassMember('version', REFERENCE_ENUM_CLASS, 'VersionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper', 'VersionEnum', 
                [], [], 
                '''                SSH state version
                ''',
                'version',
                'Cisco-IOS-XR-crypto-ssh-oper', False),
            _MetaInfoClassMember('vty-assigned', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Boolean indicating whether line VTY line number
                is valid
                ''',
                'vty_assigned',
                'Cisco-IOS-XR-crypto-ssh-oper', False),
            _MetaInfoClassMember('vty-line-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                VTY line number
                ''',
                'vty_line_number',
                'Cisco-IOS-XR-crypto-ssh-oper', False),
            ],
            'Cisco-IOS-XR-crypto-ssh-oper',
            'session-brief-info',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-ssh-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper'
        ),
    },
    'Ssh.Session.Brief.IncomingSessions' : {
        'meta_info' : _MetaInfoClass('Ssh.Session.Brief.IncomingSessions',
            False, 
            [
            _MetaInfoClassMember('session-brief-info', REFERENCE_LIST, 'SessionBriefInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper', 'Ssh.Session.Brief.IncomingSessions.SessionBriefInfo', 
                [], [], 
                '''                session brief info
                ''',
                'session_brief_info',
                'Cisco-IOS-XR-crypto-ssh-oper', False),
            ],
            'Cisco-IOS-XR-crypto-ssh-oper',
            'incoming-sessions',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-ssh-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper'
        ),
    },
    'Ssh.Session.Brief.OutgoingSessions.SessionBriefInfo' : {
        'meta_info' : _MetaInfoClass('Ssh.Session.Brief.OutgoingSessions.SessionBriefInfo',
            False, 
            [
            _MetaInfoClassMember('authentication-type', REFERENCE_ENUM_CLASS, 'AuthenEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper', 'AuthenEnum', 
                [], [], 
                '''                Authentication method
                ''',
                'authentication_type',
                'Cisco-IOS-XR-crypto-ssh-oper', False),
            _MetaInfoClassMember('channel-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Channel ID
                ''',
                'channel_id',
                'Cisco-IOS-XR-crypto-ssh-oper', False),
            _MetaInfoClassMember('connection-type', REFERENCE_ENUM_CLASS, 'ConnectionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper', 'ConnectionEnum', 
                [], [], 
                '''                Channel Connection Type
                ''',
                'connection_type',
                'Cisco-IOS-XR-crypto-ssh-oper', False),
            _MetaInfoClassMember('host-address', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Host address
                ''',
                'host_address',
                'Cisco-IOS-XR-crypto-ssh-oper', False),
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Node name
                ''',
                'node_name',
                'Cisco-IOS-XR-crypto-ssh-oper', False),
            _MetaInfoClassMember('session-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Session ID
                ''',
                'session_id',
                'Cisco-IOS-XR-crypto-ssh-oper', False),
            _MetaInfoClassMember('session-state', REFERENCE_ENUM_CLASS, 'StatesEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper', 'StatesEnum', 
                [], [], 
                '''                SSH session state
                ''',
                'session_state',
                'Cisco-IOS-XR-crypto-ssh-oper', False),
            _MetaInfoClassMember('user-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                User ID
                ''',
                'user_id',
                'Cisco-IOS-XR-crypto-ssh-oper', False),
            _MetaInfoClassMember('version', REFERENCE_ENUM_CLASS, 'VersionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper', 'VersionEnum', 
                [], [], 
                '''                SSH state version
                ''',
                'version',
                'Cisco-IOS-XR-crypto-ssh-oper', False),
            _MetaInfoClassMember('vty-assigned', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Boolean indicating whether line VTY line number
                is valid
                ''',
                'vty_assigned',
                'Cisco-IOS-XR-crypto-ssh-oper', False),
            _MetaInfoClassMember('vty-line-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                VTY line number
                ''',
                'vty_line_number',
                'Cisco-IOS-XR-crypto-ssh-oper', False),
            ],
            'Cisco-IOS-XR-crypto-ssh-oper',
            'session-brief-info',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-ssh-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper'
        ),
    },
    'Ssh.Session.Brief.OutgoingSessions' : {
        'meta_info' : _MetaInfoClass('Ssh.Session.Brief.OutgoingSessions',
            False, 
            [
            _MetaInfoClassMember('session-brief-info', REFERENCE_LIST, 'SessionBriefInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper', 'Ssh.Session.Brief.OutgoingSessions.SessionBriefInfo', 
                [], [], 
                '''                session brief info
                ''',
                'session_brief_info',
                'Cisco-IOS-XR-crypto-ssh-oper', False),
            ],
            'Cisco-IOS-XR-crypto-ssh-oper',
            'outgoing-sessions',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-ssh-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper'
        ),
    },
    'Ssh.Session.Brief' : {
        'meta_info' : _MetaInfoClass('Ssh.Session.Brief',
            False, 
            [
            _MetaInfoClassMember('incoming-sessions', REFERENCE_CLASS, 'IncomingSessions' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper', 'Ssh.Session.Brief.IncomingSessions', 
                [], [], 
                '''                List of incoming sessions
                ''',
                'incoming_sessions',
                'Cisco-IOS-XR-crypto-ssh-oper', False),
            _MetaInfoClassMember('outgoing-sessions', REFERENCE_CLASS, 'OutgoingSessions' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper', 'Ssh.Session.Brief.OutgoingSessions', 
                [], [], 
                '''                List of outgoing sessions
                ''',
                'outgoing_sessions',
                'Cisco-IOS-XR-crypto-ssh-oper', False),
            ],
            'Cisco-IOS-XR-crypto-ssh-oper',
            'brief',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-ssh-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper'
        ),
    },
    'Ssh.Session.Detail.IncomingSessions.SessionDetailInfo' : {
        'meta_info' : _MetaInfoClass('Ssh.Session.Detail.IncomingSessions.SessionDetailInfo',
            False, 
            [
            _MetaInfoClassMember('in-cipher', REFERENCE_ENUM_CLASS, 'CipherEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper', 'CipherEnum', 
                [], [], 
                '''                In cipher algorithm
                ''',
                'in_cipher',
                'Cisco-IOS-XR-crypto-ssh-oper', False),
            _MetaInfoClassMember('in-mac', REFERENCE_ENUM_CLASS, 'MacEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper', 'MacEnum', 
                [], [], 
                '''                In MAC
                ''',
                'in_mac',
                'Cisco-IOS-XR-crypto-ssh-oper', False),
            _MetaInfoClassMember('key-exchange', REFERENCE_ENUM_CLASS, 'KexNameEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper', 'KexNameEnum', 
                [], [], 
                '''                Key exchange name
                ''',
                'key_exchange',
                'Cisco-IOS-XR-crypto-ssh-oper', False),
            _MetaInfoClassMember('out-cipher', REFERENCE_ENUM_CLASS, 'CipherEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper', 'CipherEnum', 
                [], [], 
                '''                Out cipher algorithm
                ''',
                'out_cipher',
                'Cisco-IOS-XR-crypto-ssh-oper', False),
            _MetaInfoClassMember('out-mac', REFERENCE_ENUM_CLASS, 'MacEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper', 'MacEnum', 
                [], [], 
                '''                Out MAC
                ''',
                'out_mac',
                'Cisco-IOS-XR-crypto-ssh-oper', False),
            _MetaInfoClassMember('public-key', REFERENCE_ENUM_CLASS, 'HostkeyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper', 'HostkeyEnum', 
                [], [], 
                '''                Host key algorithm
                ''',
                'public_key',
                'Cisco-IOS-XR-crypto-ssh-oper', False),
            _MetaInfoClassMember('session-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Session ID
                ''',
                'session_id',
                'Cisco-IOS-XR-crypto-ssh-oper', False),
            ],
            'Cisco-IOS-XR-crypto-ssh-oper',
            'session-detail-info',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-ssh-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper'
        ),
    },
    'Ssh.Session.Detail.IncomingSessions' : {
        'meta_info' : _MetaInfoClass('Ssh.Session.Detail.IncomingSessions',
            False, 
            [
            _MetaInfoClassMember('session-detail-info', REFERENCE_LIST, 'SessionDetailInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper', 'Ssh.Session.Detail.IncomingSessions.SessionDetailInfo', 
                [], [], 
                '''                session detail info
                ''',
                'session_detail_info',
                'Cisco-IOS-XR-crypto-ssh-oper', False),
            ],
            'Cisco-IOS-XR-crypto-ssh-oper',
            'incoming-sessions',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-ssh-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper'
        ),
    },
    'Ssh.Session.Detail.OutgoingConnections.SessionDetailInfo' : {
        'meta_info' : _MetaInfoClass('Ssh.Session.Detail.OutgoingConnections.SessionDetailInfo',
            False, 
            [
            _MetaInfoClassMember('in-cipher', REFERENCE_ENUM_CLASS, 'CipherEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper', 'CipherEnum', 
                [], [], 
                '''                In cipher algorithm
                ''',
                'in_cipher',
                'Cisco-IOS-XR-crypto-ssh-oper', False),
            _MetaInfoClassMember('in-mac', REFERENCE_ENUM_CLASS, 'MacEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper', 'MacEnum', 
                [], [], 
                '''                In MAC
                ''',
                'in_mac',
                'Cisco-IOS-XR-crypto-ssh-oper', False),
            _MetaInfoClassMember('key-exchange', REFERENCE_ENUM_CLASS, 'KexNameEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper', 'KexNameEnum', 
                [], [], 
                '''                Key exchange name
                ''',
                'key_exchange',
                'Cisco-IOS-XR-crypto-ssh-oper', False),
            _MetaInfoClassMember('out-cipher', REFERENCE_ENUM_CLASS, 'CipherEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper', 'CipherEnum', 
                [], [], 
                '''                Out cipher algorithm
                ''',
                'out_cipher',
                'Cisco-IOS-XR-crypto-ssh-oper', False),
            _MetaInfoClassMember('out-mac', REFERENCE_ENUM_CLASS, 'MacEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper', 'MacEnum', 
                [], [], 
                '''                Out MAC
                ''',
                'out_mac',
                'Cisco-IOS-XR-crypto-ssh-oper', False),
            _MetaInfoClassMember('public-key', REFERENCE_ENUM_CLASS, 'HostkeyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper', 'HostkeyEnum', 
                [], [], 
                '''                Host key algorithm
                ''',
                'public_key',
                'Cisco-IOS-XR-crypto-ssh-oper', False),
            _MetaInfoClassMember('session-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Session ID
                ''',
                'session_id',
                'Cisco-IOS-XR-crypto-ssh-oper', False),
            ],
            'Cisco-IOS-XR-crypto-ssh-oper',
            'session-detail-info',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-ssh-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper'
        ),
    },
    'Ssh.Session.Detail.OutgoingConnections' : {
        'meta_info' : _MetaInfoClass('Ssh.Session.Detail.OutgoingConnections',
            False, 
            [
            _MetaInfoClassMember('session-detail-info', REFERENCE_LIST, 'SessionDetailInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper', 'Ssh.Session.Detail.OutgoingConnections.SessionDetailInfo', 
                [], [], 
                '''                session detail info
                ''',
                'session_detail_info',
                'Cisco-IOS-XR-crypto-ssh-oper', False),
            ],
            'Cisco-IOS-XR-crypto-ssh-oper',
            'outgoing-connections',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-ssh-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper'
        ),
    },
    'Ssh.Session.Detail' : {
        'meta_info' : _MetaInfoClass('Ssh.Session.Detail',
            False, 
            [
            _MetaInfoClassMember('incoming-sessions', REFERENCE_CLASS, 'IncomingSessions' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper', 'Ssh.Session.Detail.IncomingSessions', 
                [], [], 
                '''                List of incoming sessions
                ''',
                'incoming_sessions',
                'Cisco-IOS-XR-crypto-ssh-oper', False),
            _MetaInfoClassMember('outgoing-connections', REFERENCE_CLASS, 'OutgoingConnections' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper', 'Ssh.Session.Detail.OutgoingConnections', 
                [], [], 
                '''                List of outgoing connections
                ''',
                'outgoing_connections',
                'Cisco-IOS-XR-crypto-ssh-oper', False),
            ],
            'Cisco-IOS-XR-crypto-ssh-oper',
            'detail',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-ssh-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper'
        ),
    },
    'Ssh.Session' : {
        'meta_info' : _MetaInfoClass('Ssh.Session',
            False, 
            [
            _MetaInfoClassMember('brief', REFERENCE_CLASS, 'Brief' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper', 'Ssh.Session.Brief', 
                [], [], 
                '''                SSH session brief information
                ''',
                'brief',
                'Cisco-IOS-XR-crypto-ssh-oper', False),
            _MetaInfoClassMember('detail', REFERENCE_CLASS, 'Detail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper', 'Ssh.Session.Detail', 
                [], [], 
                '''                SSH session detail information
                ''',
                'detail',
                'Cisco-IOS-XR-crypto-ssh-oper', False),
            _MetaInfoClassMember('rekey', REFERENCE_CLASS, 'Rekey' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper', 'Ssh.Session.Rekey', 
                [], [], 
                '''                SSH session rekey information
                ''',
                'rekey',
                'Cisco-IOS-XR-crypto-ssh-oper', False),
            ],
            'Cisco-IOS-XR-crypto-ssh-oper',
            'session',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-ssh-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper'
        ),
    },
    'Ssh' : {
        'meta_info' : _MetaInfoClass('Ssh',
            False, 
            [
            _MetaInfoClassMember('session', REFERENCE_CLASS, 'Session' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper', 'Ssh.Session', 
                [], [], 
                '''                Crypto SSH session
                ''',
                'session',
                'Cisco-IOS-XR-crypto-ssh-oper', False),
            ],
            'Cisco-IOS-XR-crypto-ssh-oper',
            'ssh',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-ssh-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper'
        ),
    },
}
_meta_table['Ssh1.Kex.Nodes.Node.IncomingSessions.SessionDetailInfo']['meta_info'].parent =_meta_table['Ssh1.Kex.Nodes.Node.IncomingSessions']['meta_info']
_meta_table['Ssh1.Kex.Nodes.Node.OutgoingConnections.SessionDetailInfo']['meta_info'].parent =_meta_table['Ssh1.Kex.Nodes.Node.OutgoingConnections']['meta_info']
_meta_table['Ssh1.Kex.Nodes.Node.IncomingSessions']['meta_info'].parent =_meta_table['Ssh1.Kex.Nodes.Node']['meta_info']
_meta_table['Ssh1.Kex.Nodes.Node.OutgoingConnections']['meta_info'].parent =_meta_table['Ssh1.Kex.Nodes.Node']['meta_info']
_meta_table['Ssh1.Kex.Nodes.Node']['meta_info'].parent =_meta_table['Ssh1.Kex.Nodes']['meta_info']
_meta_table['Ssh1.Kex.Nodes']['meta_info'].parent =_meta_table['Ssh1.Kex']['meta_info']
_meta_table['Ssh1.Kex']['meta_info'].parent =_meta_table['Ssh1']['meta_info']
_meta_table['Ssh.Session.Rekey.IncomingSessions.SessionRekeyInfo']['meta_info'].parent =_meta_table['Ssh.Session.Rekey.IncomingSessions']['meta_info']
_meta_table['Ssh.Session.Rekey.OutgoingConnections.SessionRekeyInfo']['meta_info'].parent =_meta_table['Ssh.Session.Rekey.OutgoingConnections']['meta_info']
_meta_table['Ssh.Session.Rekey.IncomingSessions']['meta_info'].parent =_meta_table['Ssh.Session.Rekey']['meta_info']
_meta_table['Ssh.Session.Rekey.OutgoingConnections']['meta_info'].parent =_meta_table['Ssh.Session.Rekey']['meta_info']
_meta_table['Ssh.Session.Brief.IncomingSessions.SessionBriefInfo']['meta_info'].parent =_meta_table['Ssh.Session.Brief.IncomingSessions']['meta_info']
_meta_table['Ssh.Session.Brief.OutgoingSessions.SessionBriefInfo']['meta_info'].parent =_meta_table['Ssh.Session.Brief.OutgoingSessions']['meta_info']
_meta_table['Ssh.Session.Brief.IncomingSessions']['meta_info'].parent =_meta_table['Ssh.Session.Brief']['meta_info']
_meta_table['Ssh.Session.Brief.OutgoingSessions']['meta_info'].parent =_meta_table['Ssh.Session.Brief']['meta_info']
_meta_table['Ssh.Session.Detail.IncomingSessions.SessionDetailInfo']['meta_info'].parent =_meta_table['Ssh.Session.Detail.IncomingSessions']['meta_info']
_meta_table['Ssh.Session.Detail.OutgoingConnections.SessionDetailInfo']['meta_info'].parent =_meta_table['Ssh.Session.Detail.OutgoingConnections']['meta_info']
_meta_table['Ssh.Session.Detail.IncomingSessions']['meta_info'].parent =_meta_table['Ssh.Session.Detail']['meta_info']
_meta_table['Ssh.Session.Detail.OutgoingConnections']['meta_info'].parent =_meta_table['Ssh.Session.Detail']['meta_info']
_meta_table['Ssh.Session.Rekey']['meta_info'].parent =_meta_table['Ssh.Session']['meta_info']
_meta_table['Ssh.Session.Brief']['meta_info'].parent =_meta_table['Ssh.Session']['meta_info']
_meta_table['Ssh.Session.Detail']['meta_info'].parent =_meta_table['Ssh.Session']['meta_info']
_meta_table['Ssh.Session']['meta_info'].parent =_meta_table['Ssh']['meta_info']
