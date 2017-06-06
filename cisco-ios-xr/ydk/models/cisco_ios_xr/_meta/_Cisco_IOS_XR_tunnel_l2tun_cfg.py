


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'L2TpHashMethodEnum' : _MetaInfoEnum('L2TpHashMethodEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_cfg',
        {
            'md5':'md5',
            'sha1':'sha1',
            'none':'none',
        }, 'Cisco-IOS-XR-tunnel-l2tun-cfg', _yang_ns._namespaces['Cisco-IOS-XR-tunnel-l2tun-cfg']),
    'L2TpDigestHashMethodEnum' : _MetaInfoEnum('L2TpDigestHashMethodEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_cfg',
        {
            'md5':'md5',
            'sha1':'sha1',
        }, 'Cisco-IOS-XR-tunnel-l2tun-cfg', _yang_ns._namespaces['Cisco-IOS-XR-tunnel-l2tun-cfg']),
    'L2Tp.Classes.Class_.Security.Ip' : {
        'meta_info' : _MetaInfoClass('L2Tp.Classes.Class_.Security.Ip',
            False, 
            [
            _MetaInfoClassMember('address-check', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable IP address check for L2TP packets
                ''',
                'address_check',
                'Cisco-IOS-XR-tunnel-l2tun-cfg', False),
            ],
            'Cisco-IOS-XR-tunnel-l2tun-cfg',
            'ip',
            _yang_ns._namespaces['Cisco-IOS-XR-tunnel-l2tun-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_cfg'
        ),
    },
    'L2Tp.Classes.Class_.Security' : {
        'meta_info' : _MetaInfoClass('L2Tp.Classes.Class_.Security',
            False, 
            [
            _MetaInfoClassMember('ip', REFERENCE_CLASS, 'Ip' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_cfg', 'L2Tp.Classes.Class_.Security.Ip', 
                [], [], 
                '''                Security check for IP
                ''',
                'ip',
                'Cisco-IOS-XR-tunnel-l2tun-cfg', False),
            ],
            'Cisco-IOS-XR-tunnel-l2tun-cfg',
            'security',
            _yang_ns._namespaces['Cisco-IOS-XR-tunnel-l2tun-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_cfg'
        ),
    },
    'L2Tp.Classes.Class_.Retransmit.Initial.Timeout' : {
        'meta_info' : _MetaInfoClass('L2Tp.Classes.Class_.Retransmit.Initial.Timeout',
            False, 
            [
            _MetaInfoClassMember('maximum', ATTRIBUTE, 'int' , None, None, 
                [('1', '8')], [], 
                '''                Specify maximum timeout
                ''',
                'maximum',
                'Cisco-IOS-XR-tunnel-l2tun-cfg', False),
            _MetaInfoClassMember('minimum', ATTRIBUTE, 'int' , None, None, 
                [('1', '8')], [], 
                '''                Specify minimum timeout
                ''',
                'minimum',
                'Cisco-IOS-XR-tunnel-l2tun-cfg', False),
            ],
            'Cisco-IOS-XR-tunnel-l2tun-cfg',
            'timeout',
            _yang_ns._namespaces['Cisco-IOS-XR-tunnel-l2tun-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_cfg'
        ),
    },
    'L2Tp.Classes.Class_.Retransmit.Initial' : {
        'meta_info' : _MetaInfoClass('L2Tp.Classes.Class_.Retransmit.Initial',
            False, 
            [
            _MetaInfoClassMember('retry', ATTRIBUTE, 'int' , None, None, 
                [('1', '1000')], [], 
                '''                Specify the retry number
                ''',
                'retry',
                'Cisco-IOS-XR-tunnel-l2tun-cfg', False),
            _MetaInfoClassMember('timeout', REFERENCE_CLASS, 'Timeout' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_cfg', 'L2Tp.Classes.Class_.Retransmit.Initial.Timeout', 
                [], [], 
                '''                Set timeout value range
                ''',
                'timeout',
                'Cisco-IOS-XR-tunnel-l2tun-cfg', False),
            ],
            'Cisco-IOS-XR-tunnel-l2tun-cfg',
            'initial',
            _yang_ns._namespaces['Cisco-IOS-XR-tunnel-l2tun-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_cfg'
        ),
    },
    'L2Tp.Classes.Class_.Retransmit.Timeout' : {
        'meta_info' : _MetaInfoClass('L2Tp.Classes.Class_.Retransmit.Timeout',
            False, 
            [
            _MetaInfoClassMember('maximum', ATTRIBUTE, 'int' , None, None, 
                [('1', '8')], [], 
                '''                Specify maximum timeout
                ''',
                'maximum',
                'Cisco-IOS-XR-tunnel-l2tun-cfg', False),
            _MetaInfoClassMember('minimum', ATTRIBUTE, 'int' , None, None, 
                [('1', '8')], [], 
                '''                Specify minimum timeout
                ''',
                'minimum',
                'Cisco-IOS-XR-tunnel-l2tun-cfg', False),
            ],
            'Cisco-IOS-XR-tunnel-l2tun-cfg',
            'timeout',
            _yang_ns._namespaces['Cisco-IOS-XR-tunnel-l2tun-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_cfg'
        ),
    },
    'L2Tp.Classes.Class_.Retransmit' : {
        'meta_info' : _MetaInfoClass('L2Tp.Classes.Class_.Retransmit',
            False, 
            [
            _MetaInfoClassMember('initial', REFERENCE_CLASS, 'Initial' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_cfg', 'L2Tp.Classes.Class_.Retransmit.Initial', 
                [], [], 
                '''                Set retries and timeouts for initial
                ''',
                'initial',
                'Cisco-IOS-XR-tunnel-l2tun-cfg', False),
            _MetaInfoClassMember('retry', ATTRIBUTE, 'int' , None, None, 
                [('5', '1000')], [], 
                '''                Specify retransmit retry count
                ''',
                'retry',
                'Cisco-IOS-XR-tunnel-l2tun-cfg', False),
            _MetaInfoClassMember('timeout', REFERENCE_CLASS, 'Timeout' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_cfg', 'L2Tp.Classes.Class_.Retransmit.Timeout', 
                [], [], 
                '''                Set timeout value range
                ''',
                'timeout',
                'Cisco-IOS-XR-tunnel-l2tun-cfg', False),
            ],
            'Cisco-IOS-XR-tunnel-l2tun-cfg',
            'retransmit',
            _yang_ns._namespaces['Cisco-IOS-XR-tunnel-l2tun-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_cfg'
        ),
    },
    'L2Tp.Classes.Class_.Tunnel' : {
        'meta_info' : _MetaInfoClass('L2Tp.Classes.Class_.Tunnel',
            False, 
            [
            _MetaInfoClassMember('accounting', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Tunnel accounting
                ''',
                'accounting',
                'Cisco-IOS-XR-tunnel-l2tun-cfg', False),
            ],
            'Cisco-IOS-XR-tunnel-l2tun-cfg',
            'tunnel',
            _yang_ns._namespaces['Cisco-IOS-XR-tunnel-l2tun-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_cfg'
        ),
    },
    'L2Tp.Classes.Class_.Digest.Secrets.Secret' : {
        'meta_info' : _MetaInfoClass('L2Tp.Classes.Class_.Digest.Secrets.Secret',
            False, 
            [
            _MetaInfoClassMember('secret-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Specify the encrypted user secret
                ''',
                'secret_name',
                'Cisco-IOS-XR-tunnel-l2tun-cfg', True),
            _MetaInfoClassMember('hash', REFERENCE_ENUM_CLASS, 'L2TpHashMethodEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_cfg', 'L2TpHashMethodEnum', 
                [], [], 
                '''                Specify hash method
                ''',
                'hash',
                'Cisco-IOS-XR-tunnel-l2tun-cfg', False),
            ],
            'Cisco-IOS-XR-tunnel-l2tun-cfg',
            'secret',
            _yang_ns._namespaces['Cisco-IOS-XR-tunnel-l2tun-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_cfg'
        ),
    },
    'L2Tp.Classes.Class_.Digest.Secrets' : {
        'meta_info' : _MetaInfoClass('L2Tp.Classes.Class_.Digest.Secrets',
            False, 
            [
            _MetaInfoClassMember('secret', REFERENCE_LIST, 'Secret' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_cfg', 'L2Tp.Classes.Class_.Digest.Secrets.Secret', 
                [], [], 
                '''                The encrypted user secret and hash method
                ''',
                'secret',
                'Cisco-IOS-XR-tunnel-l2tun-cfg', False),
            ],
            'Cisco-IOS-XR-tunnel-l2tun-cfg',
            'secrets',
            _yang_ns._namespaces['Cisco-IOS-XR-tunnel-l2tun-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_cfg'
        ),
    },
    'L2Tp.Classes.Class_.Digest' : {
        'meta_info' : _MetaInfoClass('L2Tp.Classes.Class_.Digest',
            False, 
            [
            _MetaInfoClassMember('check-disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable digest checking
                ''',
                'check_disable',
                'Cisco-IOS-XR-tunnel-l2tun-cfg', False),
            _MetaInfoClassMember('hash', REFERENCE_ENUM_CLASS, 'L2TpDigestHashMethodEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_cfg', 'L2TpDigestHashMethodEnum', 
                [], [], 
                '''                Specify hash method
                ''',
                'hash',
                'Cisco-IOS-XR-tunnel-l2tun-cfg', False),
            _MetaInfoClassMember('secrets', REFERENCE_CLASS, 'Secrets' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_cfg', 'L2Tp.Classes.Class_.Digest.Secrets', 
                [], [], 
                '''                Set shared secret for message digest
                ''',
                'secrets',
                'Cisco-IOS-XR-tunnel-l2tun-cfg', False),
            ],
            'Cisco-IOS-XR-tunnel-l2tun-cfg',
            'digest',
            _yang_ns._namespaces['Cisco-IOS-XR-tunnel-l2tun-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_cfg'
        ),
    },
    'L2Tp.Classes.Class_.Ip' : {
        'meta_info' : _MetaInfoClass('L2Tp.Classes.Class_.Ip',
            False, 
            [
            _MetaInfoClassMember('tos', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                IP TOS value (decimal)
                ''',
                'tos',
                'Cisco-IOS-XR-tunnel-l2tun-cfg', False),
            ],
            'Cisco-IOS-XR-tunnel-l2tun-cfg',
            'ip',
            _yang_ns._namespaces['Cisco-IOS-XR-tunnel-l2tun-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_cfg'
        ),
    },
    'L2Tp.Classes.Class_' : {
        'meta_info' : _MetaInfoClass('L2Tp.Classes.Class_',
            False, 
            [
            _MetaInfoClassMember('class-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 31)], [], 
                '''                Specify the class name. Regexp:
                ^[a-z0-9A-Z][-_.a-z0-9A-Z]*$
                ''',
                'class_name',
                'Cisco-IOS-XR-tunnel-l2tun-cfg', True),
            _MetaInfoClassMember('authentication', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Authenticate the L2TP control connection
                ''',
                'authentication',
                'Cisco-IOS-XR-tunnel-l2tun-cfg', False),
            _MetaInfoClassMember('congestion-control', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Congestion control enabled
                ''',
                'congestion_control',
                'Cisco-IOS-XR-tunnel-l2tun-cfg', False),
            _MetaInfoClassMember('digest', REFERENCE_CLASS, 'Digest' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_cfg', 'L2Tp.Classes.Class_.Digest', 
                [], [], 
                '''                Message digest authentication for the L2TP
                control connection
                ''',
                'digest',
                'Cisco-IOS-XR-tunnel-l2tun-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable L2TPv3 class used for L2VPNs
                ''',
                'enable',
                'Cisco-IOS-XR-tunnel-l2tun-cfg', False),
            _MetaInfoClassMember('hello-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '1000')], [], 
                '''                Specify interval (in seconds)
                ''',
                'hello_interval',
                'Cisco-IOS-XR-tunnel-l2tun-cfg', False),
            _MetaInfoClassMember('hidden', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Specify to hide AVPs in outgoing control
                messages
                ''',
                'hidden',
                'Cisco-IOS-XR-tunnel-l2tun-cfg', False),
            _MetaInfoClassMember('host-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Local hostname for control connection
                authentication
                ''',
                'host_name',
                'Cisco-IOS-XR-tunnel-l2tun-cfg', False),
            _MetaInfoClassMember('ip', REFERENCE_CLASS, 'Ip' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_cfg', 'L2Tp.Classes.Class_.Ip', 
                [], [], 
                '''                IP TOS value
                ''',
                'ip',
                'Cisco-IOS-XR-tunnel-l2tun-cfg', False),
            _MetaInfoClassMember('password', ATTRIBUTE, 'str' , None, None, 
                [], [b'(!.+)|([^!].+)'], 
                '''                Specify the password for control channel
                authentication
                ''',
                'password',
                'Cisco-IOS-XR-tunnel-l2tun-cfg', False),
            _MetaInfoClassMember('receive-window', ATTRIBUTE, 'int' , None, None, 
                [('1', '16384')], [], 
                '''                Receive window size for the control connection
                ''',
                'receive_window',
                'Cisco-IOS-XR-tunnel-l2tun-cfg', False),
            _MetaInfoClassMember('retransmit', REFERENCE_CLASS, 'Retransmit' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_cfg', 'L2Tp.Classes.Class_.Retransmit', 
                [], [], 
                '''                Control message retransmission parameters
                ''',
                'retransmit',
                'Cisco-IOS-XR-tunnel-l2tun-cfg', False),
            _MetaInfoClassMember('security', REFERENCE_CLASS, 'Security' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_cfg', 'L2Tp.Classes.Class_.Security', 
                [], [], 
                '''                Security check
                ''',
                'security',
                'Cisco-IOS-XR-tunnel-l2tun-cfg', False),
            _MetaInfoClassMember('timeout-no-user', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Timeout value for no-user in seconds
                ''',
                'timeout_no_user',
                'Cisco-IOS-XR-tunnel-l2tun-cfg', False),
            _MetaInfoClassMember('timeout-setup', ATTRIBUTE, 'int' , None, None, 
                [('60', '6000')], [], 
                '''                Time permitted to set up a control connection
                ''',
                'timeout_setup',
                'Cisco-IOS-XR-tunnel-l2tun-cfg', False),
            _MetaInfoClassMember('tunnel', REFERENCE_CLASS, 'Tunnel' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_cfg', 'L2Tp.Classes.Class_.Tunnel', 
                [], [], 
                '''                l2TP tunnel
                ''',
                'tunnel',
                'Cisco-IOS-XR-tunnel-l2tun-cfg', False),
            ],
            'Cisco-IOS-XR-tunnel-l2tun-cfg',
            'class',
            _yang_ns._namespaces['Cisco-IOS-XR-tunnel-l2tun-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_cfg'
        ),
    },
    'L2Tp.Classes' : {
        'meta_info' : _MetaInfoClass('L2Tp.Classes',
            False, 
            [
            _MetaInfoClassMember('class', REFERENCE_LIST, 'Class_' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_cfg', 'L2Tp.Classes.Class_', 
                [], [], 
                '''                Configuration for a specific class
                ''',
                'class_',
                'Cisco-IOS-XR-tunnel-l2tun-cfg', False),
            ],
            'Cisco-IOS-XR-tunnel-l2tun-cfg',
            'classes',
            _yang_ns._namespaces['Cisco-IOS-XR-tunnel-l2tun-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_cfg'
        ),
    },
    'L2Tp' : {
        'meta_info' : _MetaInfoClass('L2Tp',
            False, 
            [
            _MetaInfoClassMember('classes', REFERENCE_CLASS, 'Classes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_cfg', 'L2Tp.Classes', 
                [], [], 
                '''                List of classes
                ''',
                'classes',
                'Cisco-IOS-XR-tunnel-l2tun-cfg', False),
            ],
            'Cisco-IOS-XR-tunnel-l2tun-cfg',
            'l2tp',
            _yang_ns._namespaces['Cisco-IOS-XR-tunnel-l2tun-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_cfg'
        ),
    },
}
_meta_table['L2Tp.Classes.Class_.Security.Ip']['meta_info'].parent =_meta_table['L2Tp.Classes.Class_.Security']['meta_info']
_meta_table['L2Tp.Classes.Class_.Retransmit.Initial.Timeout']['meta_info'].parent =_meta_table['L2Tp.Classes.Class_.Retransmit.Initial']['meta_info']
_meta_table['L2Tp.Classes.Class_.Retransmit.Initial']['meta_info'].parent =_meta_table['L2Tp.Classes.Class_.Retransmit']['meta_info']
_meta_table['L2Tp.Classes.Class_.Retransmit.Timeout']['meta_info'].parent =_meta_table['L2Tp.Classes.Class_.Retransmit']['meta_info']
_meta_table['L2Tp.Classes.Class_.Digest.Secrets.Secret']['meta_info'].parent =_meta_table['L2Tp.Classes.Class_.Digest.Secrets']['meta_info']
_meta_table['L2Tp.Classes.Class_.Digest.Secrets']['meta_info'].parent =_meta_table['L2Tp.Classes.Class_.Digest']['meta_info']
_meta_table['L2Tp.Classes.Class_.Security']['meta_info'].parent =_meta_table['L2Tp.Classes.Class_']['meta_info']
_meta_table['L2Tp.Classes.Class_.Retransmit']['meta_info'].parent =_meta_table['L2Tp.Classes.Class_']['meta_info']
_meta_table['L2Tp.Classes.Class_.Tunnel']['meta_info'].parent =_meta_table['L2Tp.Classes.Class_']['meta_info']
_meta_table['L2Tp.Classes.Class_.Digest']['meta_info'].parent =_meta_table['L2Tp.Classes.Class_']['meta_info']
_meta_table['L2Tp.Classes.Class_.Ip']['meta_info'].parent =_meta_table['L2Tp.Classes.Class_']['meta_info']
_meta_table['L2Tp.Classes.Class_']['meta_info'].parent =_meta_table['L2Tp.Classes']['meta_info']
_meta_table['L2Tp.Classes']['meta_info'].parent =_meta_table['L2Tp']['meta_info']
