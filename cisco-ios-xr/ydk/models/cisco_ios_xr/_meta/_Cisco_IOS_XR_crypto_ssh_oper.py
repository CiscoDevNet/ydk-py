


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns

_meta_table = {
    'KexNameEnum' : _MetaInfoEnum('KexNameEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper',
        {
            'diffie-hellman':'DIFFIE_HELLMAN',
            'password-authenticated':'PASSWORD_AUTHENTICATED',
        }, 'Cisco-IOS-XR-crypto-ssh-oper', _yang_ns._namespaces['Cisco-IOS-XR-crypto-ssh-oper']),
    'HostkeyEnum' : _MetaInfoEnum('HostkeyEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper',
        {
            'ssh-dss':'SSH_DSS',
            'ssh-rsa':'SSH_RSA',
        }, 'Cisco-IOS-XR-crypto-ssh-oper', _yang_ns._namespaces['Cisco-IOS-XR-crypto-ssh-oper']),
    'VersionEnum' : _MetaInfoEnum('VersionEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper',
        {
            'v2':'V2',
            'v1':'V1',
        }, 'Cisco-IOS-XR-crypto-ssh-oper', _yang_ns._namespaces['Cisco-IOS-XR-crypto-ssh-oper']),
    'ConnectionEnum' : _MetaInfoEnum('ConnectionEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper',
        {
            'undefined':'UNDEFINED',
            'shell':'SHELL',
            'exec':'EXEC',
            'scp':'SCP',
            'sftp-subsystem':'SFTP_SUBSYSTEM',
            'netconf-subsystem':'NETCONF_SUBSYSTEM',
        }, 'Cisco-IOS-XR-crypto-ssh-oper', _yang_ns._namespaces['Cisco-IOS-XR-crypto-ssh-oper']),
    'StatesEnum' : _MetaInfoEnum('StatesEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper',
        {
            'open':'OPEN',
            'version-ok':'VERSION_OK',
            'key-exchange-initialize':'KEY_EXCHANGE_INITIALIZE',
            'key-exchange-dh':'KEY_EXCHANGE_DH',
            'new-keys':'NEW_KEYS',
            'authenticate-information':'AUTHENTICATE_INFORMATION',
            'authenticated':'AUTHENTICATED',
            'channel-open':'CHANNEL_OPEN',
            'pty-open':'PTY_OPEN',
            'session-open':'SESSION_OPEN',
            'rekey':'REKEY',
            'suspended':'SUSPENDED',
            'session-closed':'SESSION_CLOSED',
        }, 'Cisco-IOS-XR-crypto-ssh-oper', _yang_ns._namespaces['Cisco-IOS-XR-crypto-ssh-oper']),
    'MacEnum' : _MetaInfoEnum('MacEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper',
        {
            'hmac-md5':'HMAC_MD5',
            'hmac-sha1':'HMAC_SHA1',
        }, 'Cisco-IOS-XR-crypto-ssh-oper', _yang_ns._namespaces['Cisco-IOS-XR-crypto-ssh-oper']),
    'CipherEnum' : _MetaInfoEnum('CipherEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper',
        {
            'aes128-cbc':'AES128_CBC',
            'aes192-cbc':'AES192_CBC',
            'aes256-cbc':'AES256_CBC',
            'triple-des-cbc':'TRIPLE_DES_CBC',
        }, 'Cisco-IOS-XR-crypto-ssh-oper', _yang_ns._namespaces['Cisco-IOS-XR-crypto-ssh-oper']),
    'AuthenEnum' : _MetaInfoEnum('AuthenEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_ssh_oper',
        {
            'password':'PASSWORD',
            'rsa-public-key':'RSA_PUBLIC_KEY',
            'keyboard-interactive':'KEYBOARD_INTERACTIVE',
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
                [], ['([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
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
                [], ['([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
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
                [], ['([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
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
_meta_table['Ssh.Session.Brief.IncomingSessions.SessionBriefInfo']['meta_info'].parent =_meta_table['Ssh.Session.Brief.IncomingSessions']['meta_info']
_meta_table['Ssh.Session.Brief.OutgoingSessions.SessionBriefInfo']['meta_info'].parent =_meta_table['Ssh.Session.Brief.OutgoingSessions']['meta_info']
_meta_table['Ssh.Session.Brief.IncomingSessions']['meta_info'].parent =_meta_table['Ssh.Session.Brief']['meta_info']
_meta_table['Ssh.Session.Brief.OutgoingSessions']['meta_info'].parent =_meta_table['Ssh.Session.Brief']['meta_info']
_meta_table['Ssh.Session.Detail.IncomingSessions.SessionDetailInfo']['meta_info'].parent =_meta_table['Ssh.Session.Detail.IncomingSessions']['meta_info']
_meta_table['Ssh.Session.Detail.OutgoingConnections.SessionDetailInfo']['meta_info'].parent =_meta_table['Ssh.Session.Detail.OutgoingConnections']['meta_info']
_meta_table['Ssh.Session.Detail.IncomingSessions']['meta_info'].parent =_meta_table['Ssh.Session.Detail']['meta_info']
_meta_table['Ssh.Session.Detail.OutgoingConnections']['meta_info'].parent =_meta_table['Ssh.Session.Detail']['meta_info']
_meta_table['Ssh.Session.Brief']['meta_info'].parent =_meta_table['Ssh.Session']['meta_info']
_meta_table['Ssh.Session.Detail']['meta_info'].parent =_meta_table['Ssh.Session']['meta_info']
_meta_table['Ssh.Session']['meta_info'].parent =_meta_table['Ssh']['meta_info']
