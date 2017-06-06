


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'DfBitEnum' : _MetaInfoEnum('DfBitEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg',
        {
            'clear':'clear',
            'reflect':'reflect',
            'set':'set',
        }, 'Cisco-IOS-XR-tunnel-vpdn-cfg', _yang_ns._namespaces['Cisco-IOS-XR-tunnel-vpdn-cfg']),
    'OptionEnum' : _MetaInfoEnum('OptionEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg',
        {
            'local':'local',
            'user':'user',
            'dead-cache':'dead_cache',
            'tunnel-drop':'tunnel_drop',
        }, 'Cisco-IOS-XR-tunnel-vpdn-cfg', _yang_ns._namespaces['Cisco-IOS-XR-tunnel-vpdn-cfg']),
    'Vpdn.History' : {
        'meta_info' : _MetaInfoClass('Vpdn.History',
            False, 
            [
            _MetaInfoClassMember('failure', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                User failure
                ''',
                'failure',
                'Cisco-IOS-XR-tunnel-vpdn-cfg', False),
            ],
            'Cisco-IOS-XR-tunnel-vpdn-cfg',
            'history',
            _yang_ns._namespaces['Cisco-IOS-XR-tunnel-vpdn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg'
        ),
    },
    'Vpdn.Redundancy.ProcessFailures' : {
        'meta_info' : _MetaInfoClass('Vpdn.Redundancy.ProcessFailures',
            False, 
            [
            _MetaInfoClassMember('switchover', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Force a switchover if the process crashes
                ''',
                'switchover',
                'Cisco-IOS-XR-tunnel-vpdn-cfg', False),
            ],
            'Cisco-IOS-XR-tunnel-vpdn-cfg',
            'process-failures',
            _yang_ns._namespaces['Cisco-IOS-XR-tunnel-vpdn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg'
        ),
    },
    'Vpdn.Redundancy' : {
        'meta_info' : _MetaInfoClass('Vpdn.Redundancy',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable Enable VPDN redundancy. Deletion of this
                object also causes deletion of all associated
                objects under Redundancy.
                ''',
                'enable',
                'Cisco-IOS-XR-tunnel-vpdn-cfg', False),
            _MetaInfoClassMember('process-failures', REFERENCE_CLASS, 'ProcessFailures' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg', 'Vpdn.Redundancy.ProcessFailures', 
                [], [], 
                '''                Process crash configuration
                ''',
                'process_failures',
                'Cisco-IOS-XR-tunnel-vpdn-cfg', False),
            ],
            'Cisco-IOS-XR-tunnel-vpdn-cfg',
            'redundancy',
            _yang_ns._namespaces['Cisco-IOS-XR-tunnel-vpdn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg'
        ),
    },
    'Vpdn.Local' : {
        'meta_info' : _MetaInfoClass('Vpdn.Local',
            False, 
            [
            _MetaInfoClassMember('cache-disabled', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Set constant integer
                ''',
                'cache_disabled',
                'Cisco-IOS-XR-tunnel-vpdn-cfg', False),
            _MetaInfoClassMember('path', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                local path of the saved profile
                ''',
                'path',
                'Cisco-IOS-XR-tunnel-vpdn-cfg', False),
            _MetaInfoClassMember('port', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                port value
                ''',
                'port',
                'Cisco-IOS-XR-tunnel-vpdn-cfg', False),
            _MetaInfoClassMember('secret-text', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                secret password
                ''',
                'secret_text',
                'Cisco-IOS-XR-tunnel-vpdn-cfg', False),
            ],
            'Cisco-IOS-XR-tunnel-vpdn-cfg',
            'local',
            _yang_ns._namespaces['Cisco-IOS-XR-tunnel-vpdn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg'
        ),
    },
    'Vpdn.Templates.Template.CallerId' : {
        'meta_info' : _MetaInfoClass('Vpdn.Templates.Template.CallerId',
            False, 
            [
            _MetaInfoClassMember('mask', ATTRIBUTE, 'str' , None, None, 
                [(1, 63)], [], 
                '''                Mask characters by method
                ''',
                'mask',
                'Cisco-IOS-XR-tunnel-vpdn-cfg', False),
            ],
            'Cisco-IOS-XR-tunnel-vpdn-cfg',
            'caller-id',
            _yang_ns._namespaces['Cisco-IOS-XR-tunnel-vpdn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg'
        ),
    },
    'Vpdn.Templates.Template.Vpn.Id' : {
        'meta_info' : _MetaInfoClass('Vpdn.Templates.Template.Vpn.Id',
            False, 
            [
            _MetaInfoClassMember('index', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{1,8}'], 
                '''                VPN ID, (OUI:VPN-Index) format(hex), 4 bytes
                VPN_Index Part
                ''',
                'index',
                'Cisco-IOS-XR-tunnel-vpdn-cfg', False),
            _MetaInfoClassMember('oui', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{1,8}'], 
                '''                VPN ID, (OUI:VPN-Index) format(hex), 3 bytes
                OUI Part
                ''',
                'oui',
                'Cisco-IOS-XR-tunnel-vpdn-cfg', False),
            ],
            'Cisco-IOS-XR-tunnel-vpdn-cfg',
            'id',
            _yang_ns._namespaces['Cisco-IOS-XR-tunnel-vpdn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg'
        ),
    },
    'Vpdn.Templates.Template.Vpn' : {
        'meta_info' : _MetaInfoClass('Vpdn.Templates.Template.Vpn',
            False, 
            [
            _MetaInfoClassMember('id', REFERENCE_CLASS, 'Id' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg', 'Vpdn.Templates.Template.Vpn.Id', 
                [], [], 
                '''                VPN ID
                ''',
                'id',
                'Cisco-IOS-XR-tunnel-vpdn-cfg', False),
            _MetaInfoClassMember('vrf', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                VRF name
                ''',
                'vrf',
                'Cisco-IOS-XR-tunnel-vpdn-cfg', False),
            ],
            'Cisco-IOS-XR-tunnel-vpdn-cfg',
            'vpn',
            _yang_ns._namespaces['Cisco-IOS-XR-tunnel-vpdn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg'
        ),
    },
    'Vpdn.Templates.Template.Tunnel' : {
        'meta_info' : _MetaInfoClass('Vpdn.Templates.Template.Tunnel',
            False, 
            [
            _MetaInfoClassMember('busy-timeout', ATTRIBUTE, 'int' , None, None, 
                [('60', '65535')], [], 
                '''                Busy time out value in seconds
                ''',
                'busy_timeout',
                'Cisco-IOS-XR-tunnel-vpdn-cfg', False),
            ],
            'Cisco-IOS-XR-tunnel-vpdn-cfg',
            'tunnel',
            _yang_ns._namespaces['Cisco-IOS-XR-tunnel-vpdn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg'
        ),
    },
    'Vpdn.Templates.Template.Ip' : {
        'meta_info' : _MetaInfoClass('Vpdn.Templates.Template.Ip',
            False, 
            [
            _MetaInfoClassMember('tos', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Set constant integer
                ''',
                'tos',
                'Cisco-IOS-XR-tunnel-vpdn-cfg', False),
            ],
            'Cisco-IOS-XR-tunnel-vpdn-cfg',
            'ip',
            _yang_ns._namespaces['Cisco-IOS-XR-tunnel-vpdn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg'
        ),
    },
    'Vpdn.Templates.Template.Ipv4' : {
        'meta_info' : _MetaInfoClass('Vpdn.Templates.Template.Ipv4',
            False, 
            [
            _MetaInfoClassMember('df-bit', REFERENCE_ENUM_CLASS, 'DfBitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg', 'DfBitEnum', 
                [], [], 
                '''                IPv4 don't fragment bit set/clear/reflect
                ''',
                'df_bit',
                'Cisco-IOS-XR-tunnel-vpdn-cfg', False),
            _MetaInfoClassMember('source', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Enter an IP address
                ''',
                'source',
                'Cisco-IOS-XR-tunnel-vpdn-cfg', False),
            ],
            'Cisco-IOS-XR-tunnel-vpdn-cfg',
            'ipv4',
            _yang_ns._namespaces['Cisco-IOS-XR-tunnel-vpdn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg'
        ),
    },
    'Vpdn.Templates.Template' : {
        'meta_info' : _MetaInfoClass('Vpdn.Templates.Template',
            False, 
            [
            _MetaInfoClassMember('template-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 63)], [], 
                '''                VPDN template name
                ''',
                'template_name',
                'Cisco-IOS-XR-tunnel-vpdn-cfg', True),
            _MetaInfoClassMember('caller-id', REFERENCE_CLASS, 'CallerId' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg', 'Vpdn.Templates.Template.CallerId', 
                [], [], 
                '''                Options to apply on calling station id
                ''',
                'caller_id',
                'Cisco-IOS-XR-tunnel-vpdn-cfg', False),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [(1, 100)], [], 
                '''                Up to 100 characters describing this VPDN
                template
                ''',
                'description',
                'Cisco-IOS-XR-tunnel-vpdn-cfg', False),
            _MetaInfoClassMember('dsl-line-forwarding', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Forward DSL Line Info attributes
                ''',
                'dsl_line_forwarding',
                'Cisco-IOS-XR-tunnel-vpdn-cfg', False),
            _MetaInfoClassMember('ip', REFERENCE_CLASS, 'Ip' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg', 'Vpdn.Templates.Template.Ip', 
                [], [], 
                '''                Set IP TOS value
                ''',
                'ip',
                'Cisco-IOS-XR-tunnel-vpdn-cfg', False),
            _MetaInfoClassMember('ipv4', REFERENCE_CLASS, 'Ipv4' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg', 'Vpdn.Templates.Template.Ipv4', 
                [], [], 
                '''                IPv4 settings for tunnel
                ''',
                'ipv4',
                'Cisco-IOS-XR-tunnel-vpdn-cfg', False),
            _MetaInfoClassMember('l2tp-class', ATTRIBUTE, 'str' , None, None, 
                [(1, 79)], [], 
                '''                L2TP class  command
                ''',
                'l2tp_class',
                'Cisco-IOS-XR-tunnel-vpdn-cfg', False),
            _MetaInfoClassMember('tunnel', REFERENCE_CLASS, 'Tunnel' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg', 'Vpdn.Templates.Template.Tunnel', 
                [], [], 
                '''                L2TP tunnel commands
                ''',
                'tunnel',
                'Cisco-IOS-XR-tunnel-vpdn-cfg', False),
            _MetaInfoClassMember('vpn', REFERENCE_CLASS, 'Vpn' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg', 'Vpdn.Templates.Template.Vpn', 
                [], [], 
                '''                VPN ID/VRF name
                ''',
                'vpn',
                'Cisco-IOS-XR-tunnel-vpdn-cfg', False),
            ],
            'Cisco-IOS-XR-tunnel-vpdn-cfg',
            'template',
            _yang_ns._namespaces['Cisco-IOS-XR-tunnel-vpdn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg'
        ),
    },
    'Vpdn.Templates' : {
        'meta_info' : _MetaInfoClass('Vpdn.Templates',
            False, 
            [
            _MetaInfoClassMember('template', REFERENCE_LIST, 'Template' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg', 'Vpdn.Templates.Template', 
                [], [], 
                '''                VPDN template configuration
                ''',
                'template',
                'Cisco-IOS-XR-tunnel-vpdn-cfg', False),
            ],
            'Cisco-IOS-XR-tunnel-vpdn-cfg',
            'templates',
            _yang_ns._namespaces['Cisco-IOS-XR-tunnel-vpdn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg'
        ),
    },
    'Vpdn.CallerId' : {
        'meta_info' : _MetaInfoClass('Vpdn.CallerId',
            False, 
            [
            _MetaInfoClassMember('mask', ATTRIBUTE, 'str' , None, None, 
                [(1, 63)], [], 
                '''                Mask characters by method
                ''',
                'mask',
                'Cisco-IOS-XR-tunnel-vpdn-cfg', False),
            ],
            'Cisco-IOS-XR-tunnel-vpdn-cfg',
            'caller-id',
            _yang_ns._namespaces['Cisco-IOS-XR-tunnel-vpdn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg'
        ),
    },
    'Vpdn.VpdNgroups.VpdNgroup.VpnId' : {
        'meta_info' : _MetaInfoClass('Vpdn.VpdNgroups.VpdNgroup.VpnId',
            False, 
            [
            _MetaInfoClassMember('vpn-id-index', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{1,8}'], 
                '''                VPN ID, (OUI:VPN-Index) format(hex), 4 bytes
                VPN_Index Part
                ''',
                'vpn_id_index',
                'Cisco-IOS-XR-tunnel-vpdn-cfg', False),
            _MetaInfoClassMember('vpn-id-oui', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{1,8}'], 
                '''                VPN ID, (OUI:VPN-Index) format(hex), 3 bytes
                OUI Part
                ''',
                'vpn_id_oui',
                'Cisco-IOS-XR-tunnel-vpdn-cfg', False),
            ],
            'Cisco-IOS-XR-tunnel-vpdn-cfg',
            'vpn-id',
            _yang_ns._namespaces['Cisco-IOS-XR-tunnel-vpdn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg'
        ),
    },
    'Vpdn.VpdNgroups.VpdNgroup.Ip' : {
        'meta_info' : _MetaInfoClass('Vpdn.VpdNgroups.VpdNgroup.Ip',
            False, 
            [
            _MetaInfoClassMember('tos', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                ip tos value
                ''',
                'tos',
                'Cisco-IOS-XR-tunnel-vpdn-cfg', False),
            ],
            'Cisco-IOS-XR-tunnel-vpdn-cfg',
            'ip',
            _yang_ns._namespaces['Cisco-IOS-XR-tunnel-vpdn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg'
        ),
    },
    'Vpdn.VpdNgroups.VpdNgroup' : {
        'meta_info' : _MetaInfoClass('Vpdn.VpdNgroups.VpdNgroup',
            False, 
            [
            _MetaInfoClassMember('vpd-ngroupname', ATTRIBUTE, 'str' , None, None, 
                [(1, 63)], [], 
                '''                vpdn-group name
                ''',
                'vpd_ngroupname',
                'Cisco-IOS-XR-tunnel-vpdn-cfg', True),
            _MetaInfoClassMember('attribute', ATTRIBUTE, 'str' , None, None, 
                [(1, 63)], [], 
                '''                match substring
                ''',
                'attribute',
                'Cisco-IOS-XR-tunnel-vpdn-cfg', False),
            _MetaInfoClassMember('desc', ATTRIBUTE, 'str' , None, None, 
                [(1, 100)], [], 
                '''                upto 100 characters describing this VPDN group
                ''',
                'desc',
                'Cisco-IOS-XR-tunnel-vpdn-cfg', False),
            _MetaInfoClassMember('dsl-line-forwarding', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Forward DSL Line Info attributes
                ''',
                'dsl_line_forwarding',
                'Cisco-IOS-XR-tunnel-vpdn-cfg', False),
            _MetaInfoClassMember('ip', REFERENCE_CLASS, 'Ip' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg', 'Vpdn.VpdNgroups.VpdNgroup.Ip', 
                [], [], 
                '''                set ip tos value
                ''',
                'ip',
                'Cisco-IOS-XR-tunnel-vpdn-cfg', False),
            _MetaInfoClassMember('l2tp-class', ATTRIBUTE, 'str' , None, None, 
                [(1, 79)], [], 
                '''                l2tp class name
                ''',
                'l2tp_class',
                'Cisco-IOS-XR-tunnel-vpdn-cfg', False),
            _MetaInfoClassMember('sr-ctemplate', ATTRIBUTE, 'str' , None, None, 
                [(1, 63)], [], 
                '''                Source vpdn-template
                ''',
                'sr_ctemplate',
                'Cisco-IOS-XR-tunnel-vpdn-cfg', False),
            _MetaInfoClassMember('tunnel-busy-timeout', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Busy list timeout length
                ''',
                'tunnel_busy_timeout',
                'Cisco-IOS-XR-tunnel-vpdn-cfg', False),
            _MetaInfoClassMember('vpn-id', REFERENCE_CLASS, 'VpnId' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg', 'Vpdn.VpdNgroups.VpdNgroup.VpnId', 
                [], [], 
                '''                Vpn id
                ''',
                'vpn_id',
                'Cisco-IOS-XR-tunnel-vpdn-cfg', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Vrf name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-tunnel-vpdn-cfg', False),
            ],
            'Cisco-IOS-XR-tunnel-vpdn-cfg',
            'vpd-ngroup',
            _yang_ns._namespaces['Cisco-IOS-XR-tunnel-vpdn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg'
        ),
    },
    'Vpdn.VpdNgroups' : {
        'meta_info' : _MetaInfoClass('Vpdn.VpdNgroups',
            False, 
            [
            _MetaInfoClassMember('vpd-ngroup', REFERENCE_LIST, 'VpdNgroup' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg', 'Vpdn.VpdNgroups.VpdNgroup', 
                [], [], 
                '''                vpdn-group configuration
                ''',
                'vpd_ngroup',
                'Cisco-IOS-XR-tunnel-vpdn-cfg', False),
            ],
            'Cisco-IOS-XR-tunnel-vpdn-cfg',
            'vpd-ngroups',
            _yang_ns._namespaces['Cisco-IOS-XR-tunnel-vpdn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg'
        ),
    },
    'Vpdn.Loggings.Logging' : {
        'meta_info' : _MetaInfoClass('Vpdn.Loggings.Logging',
            False, 
            [
            _MetaInfoClassMember('option', REFERENCE_ENUM_CLASS, 'OptionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg', 'OptionEnum', 
                [], [], 
                '''                VPDN logging options
                ''',
                'option',
                'Cisco-IOS-XR-tunnel-vpdn-cfg', True),
            ],
            'Cisco-IOS-XR-tunnel-vpdn-cfg',
            'logging',
            _yang_ns._namespaces['Cisco-IOS-XR-tunnel-vpdn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg'
        ),
    },
    'Vpdn.Loggings' : {
        'meta_info' : _MetaInfoClass('Vpdn.Loggings',
            False, 
            [
            _MetaInfoClassMember('logging', REFERENCE_LIST, 'Logging' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg', 'Vpdn.Loggings.Logging', 
                [], [], 
                '''                Configure logging for VPDN
                ''',
                'logging',
                'Cisco-IOS-XR-tunnel-vpdn-cfg', False),
            ],
            'Cisco-IOS-XR-tunnel-vpdn-cfg',
            'loggings',
            _yang_ns._namespaces['Cisco-IOS-XR-tunnel-vpdn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg'
        ),
    },
    'Vpdn.L2Tp.SessionId.Space' : {
        'meta_info' : _MetaInfoClass('Vpdn.L2Tp.SessionId.Space',
            False, 
            [
            _MetaInfoClassMember('hierarchy', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Session ID space hierarchical command
                ''',
                'hierarchy',
                'Cisco-IOS-XR-tunnel-vpdn-cfg', False),
            ],
            'Cisco-IOS-XR-tunnel-vpdn-cfg',
            'space',
            _yang_ns._namespaces['Cisco-IOS-XR-tunnel-vpdn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg'
        ),
    },
    'Vpdn.L2Tp.SessionId' : {
        'meta_info' : _MetaInfoClass('Vpdn.L2Tp.SessionId',
            False, 
            [
            _MetaInfoClassMember('space', REFERENCE_CLASS, 'Space' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg', 'Vpdn.L2Tp.SessionId.Space', 
                [], [], 
                '''                Session ID space commands
                ''',
                'space',
                'Cisco-IOS-XR-tunnel-vpdn-cfg', False),
            ],
            'Cisco-IOS-XR-tunnel-vpdn-cfg',
            'session-id',
            _yang_ns._namespaces['Cisco-IOS-XR-tunnel-vpdn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg'
        ),
    },
    'Vpdn.L2Tp' : {
        'meta_info' : _MetaInfoClass('Vpdn.L2Tp',
            False, 
            [
            _MetaInfoClassMember('reassembly', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                L2TP IP packet reassembly enable
                ''',
                'reassembly',
                'Cisco-IOS-XR-tunnel-vpdn-cfg', False),
            _MetaInfoClassMember('session-id', REFERENCE_CLASS, 'SessionId' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg', 'Vpdn.L2Tp.SessionId', 
                [], [], 
                '''                Session ID commands
                ''',
                'session_id',
                'Cisco-IOS-XR-tunnel-vpdn-cfg', False),
            _MetaInfoClassMember('tcp-mss-adjust', ATTRIBUTE, 'int' , None, None, 
                [('1280', '1460')], [], 
                '''                TCP MSS adjust value. The acceptable values
                might be further limited depending on platform.
                ''',
                'tcp_mss_adjust',
                'Cisco-IOS-XR-tunnel-vpdn-cfg', False),
            ],
            'Cisco-IOS-XR-tunnel-vpdn-cfg',
            'l2tp',
            _yang_ns._namespaces['Cisco-IOS-XR-tunnel-vpdn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg'
        ),
    },
    'Vpdn' : {
        'meta_info' : _MetaInfoClass('Vpdn',
            False, 
            [
            _MetaInfoClassMember('caller-id', REFERENCE_CLASS, 'CallerId' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg', 'Vpdn.CallerId', 
                [], [], 
                '''                Options to apply on calling station ID
                ''',
                'caller_id',
                'Cisco-IOS-XR-tunnel-vpdn-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable VPDN configuration. Deletion of this
                object also causes deletion of all associated
                objects under VPDN.
                ''',
                'enable',
                'Cisco-IOS-XR-tunnel-vpdn-cfg', False),
            _MetaInfoClassMember('history', REFERENCE_CLASS, 'History' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg', 'Vpdn.History', 
                [], [], 
                '''                VPDN history logging
                ''',
                'history',
                'Cisco-IOS-XR-tunnel-vpdn-cfg', False),
            _MetaInfoClassMember('l2tp', REFERENCE_CLASS, 'L2Tp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg', 'Vpdn.L2Tp', 
                [], [], 
                '''                L2TPv2 protocol commands
                ''',
                'l2tp',
                'Cisco-IOS-XR-tunnel-vpdn-cfg', False),
            _MetaInfoClassMember('local', REFERENCE_CLASS, 'Local' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg', 'Vpdn.Local', 
                [], [], 
                '''                VPDN Local radius process configuration
                ''',
                'local',
                'Cisco-IOS-XR-tunnel-vpdn-cfg', False),
            _MetaInfoClassMember('loggings', REFERENCE_CLASS, 'Loggings' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg', 'Vpdn.Loggings', 
                [], [], 
                '''                Table of Logging
                ''',
                'loggings',
                'Cisco-IOS-XR-tunnel-vpdn-cfg', False),
            _MetaInfoClassMember('redundancy', REFERENCE_CLASS, 'Redundancy' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg', 'Vpdn.Redundancy', 
                [], [], 
                '''                Enable VPDN redundancy
                ''',
                'redundancy',
                'Cisco-IOS-XR-tunnel-vpdn-cfg', False),
            _MetaInfoClassMember('session-limit', ATTRIBUTE, 'int' , None, None, 
                [('1', '131072')], [], 
                '''                Maximum simultaneous VPDN sessions
                ''',
                'session_limit',
                'Cisco-IOS-XR-tunnel-vpdn-cfg', False),
            _MetaInfoClassMember('soft-shut', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                New session no longer allowed
                ''',
                'soft_shut',
                'Cisco-IOS-XR-tunnel-vpdn-cfg', False),
            _MetaInfoClassMember('templates', REFERENCE_CLASS, 'Templates' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg', 'Vpdn.Templates', 
                [], [], 
                '''                Table of Template
                ''',
                'templates',
                'Cisco-IOS-XR-tunnel-vpdn-cfg', False),
            _MetaInfoClassMember('vpd-ngroups', REFERENCE_CLASS, 'VpdNgroups' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg', 'Vpdn.VpdNgroups', 
                [], [], 
                '''                Table of VPDNgroup
                ''',
                'vpd_ngroups',
                'Cisco-IOS-XR-tunnel-vpdn-cfg', False),
            ],
            'Cisco-IOS-XR-tunnel-vpdn-cfg',
            'vpdn',
            _yang_ns._namespaces['Cisco-IOS-XR-tunnel-vpdn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_vpdn_cfg'
        ),
    },
}
_meta_table['Vpdn.Redundancy.ProcessFailures']['meta_info'].parent =_meta_table['Vpdn.Redundancy']['meta_info']
_meta_table['Vpdn.Templates.Template.Vpn.Id']['meta_info'].parent =_meta_table['Vpdn.Templates.Template.Vpn']['meta_info']
_meta_table['Vpdn.Templates.Template.CallerId']['meta_info'].parent =_meta_table['Vpdn.Templates.Template']['meta_info']
_meta_table['Vpdn.Templates.Template.Vpn']['meta_info'].parent =_meta_table['Vpdn.Templates.Template']['meta_info']
_meta_table['Vpdn.Templates.Template.Tunnel']['meta_info'].parent =_meta_table['Vpdn.Templates.Template']['meta_info']
_meta_table['Vpdn.Templates.Template.Ip']['meta_info'].parent =_meta_table['Vpdn.Templates.Template']['meta_info']
_meta_table['Vpdn.Templates.Template.Ipv4']['meta_info'].parent =_meta_table['Vpdn.Templates.Template']['meta_info']
_meta_table['Vpdn.Templates.Template']['meta_info'].parent =_meta_table['Vpdn.Templates']['meta_info']
_meta_table['Vpdn.VpdNgroups.VpdNgroup.VpnId']['meta_info'].parent =_meta_table['Vpdn.VpdNgroups.VpdNgroup']['meta_info']
_meta_table['Vpdn.VpdNgroups.VpdNgroup.Ip']['meta_info'].parent =_meta_table['Vpdn.VpdNgroups.VpdNgroup']['meta_info']
_meta_table['Vpdn.VpdNgroups.VpdNgroup']['meta_info'].parent =_meta_table['Vpdn.VpdNgroups']['meta_info']
_meta_table['Vpdn.Loggings.Logging']['meta_info'].parent =_meta_table['Vpdn.Loggings']['meta_info']
_meta_table['Vpdn.L2Tp.SessionId.Space']['meta_info'].parent =_meta_table['Vpdn.L2Tp.SessionId']['meta_info']
_meta_table['Vpdn.L2Tp.SessionId']['meta_info'].parent =_meta_table['Vpdn.L2Tp']['meta_info']
_meta_table['Vpdn.History']['meta_info'].parent =_meta_table['Vpdn']['meta_info']
_meta_table['Vpdn.Redundancy']['meta_info'].parent =_meta_table['Vpdn']['meta_info']
_meta_table['Vpdn.Local']['meta_info'].parent =_meta_table['Vpdn']['meta_info']
_meta_table['Vpdn.Templates']['meta_info'].parent =_meta_table['Vpdn']['meta_info']
_meta_table['Vpdn.CallerId']['meta_info'].parent =_meta_table['Vpdn']['meta_info']
_meta_table['Vpdn.VpdNgroups']['meta_info'].parent =_meta_table['Vpdn']['meta_info']
_meta_table['Vpdn.Loggings']['meta_info'].parent =_meta_table['Vpdn']['meta_info']
_meta_table['Vpdn.L2Tp']['meta_info'].parent =_meta_table['Vpdn']['meta_info']
