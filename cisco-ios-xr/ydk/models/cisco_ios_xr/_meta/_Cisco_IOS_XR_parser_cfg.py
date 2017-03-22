


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'Parser.Indentation' : {
        'meta_info' : _MetaInfoClass('Parser.Indentation',
            False, 
            [
            _MetaInfoClassMember('indentation-disable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                disable the indentation
                ''',
                'indentation_disable',
                'Cisco-IOS-XR-parser-cfg', False),
            ],
            'Cisco-IOS-XR-parser-cfg',
            'indentation',
            _yang_ns._namespaces['Cisco-IOS-XR-parser-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_parser_cfg'
        ),
    },
    'Parser.Alias.Execs.Exec_' : {
        'meta_info' : _MetaInfoClass('Parser.Alias.Execs.Exec_',
            False, 
            [
            _MetaInfoClassMember('identifier', ATTRIBUTE, 'str' , None, None, 
                [(1, 30)], [], 
                '''                Exec Alias name
                ''',
                'identifier',
                'Cisco-IOS-XR-parser-cfg', True),
            _MetaInfoClassMember('identifier-xr', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Aliased exec command
                ''',
                'identifier_xr',
                'Cisco-IOS-XR-parser-cfg', False),
            ],
            'Cisco-IOS-XR-parser-cfg',
            'exec',
            _yang_ns._namespaces['Cisco-IOS-XR-parser-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_parser_cfg'
        ),
    },
    'Parser.Alias.Execs' : {
        'meta_info' : _MetaInfoClass('Parser.Alias.Execs',
            False, 
            [
            _MetaInfoClassMember('exec', REFERENCE_LIST, 'Exec_' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_parser_cfg', 'Parser.Alias.Execs.Exec_', 
                [], [], 
                '''                Exec alias name
                ''',
                'exec_',
                'Cisco-IOS-XR-parser-cfg', False),
            ],
            'Cisco-IOS-XR-parser-cfg',
            'execs',
            _yang_ns._namespaces['Cisco-IOS-XR-parser-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_parser_cfg'
        ),
    },
    'Parser.Alias.Configurations.Configuration' : {
        'meta_info' : _MetaInfoClass('Parser.Alias.Configurations.Configuration',
            False, 
            [
            _MetaInfoClassMember('identifier', ATTRIBUTE, 'str' , None, None, 
                [(1, 30)], [], 
                '''                Configuration alias name
                ''',
                'identifier',
                'Cisco-IOS-XR-parser-cfg', True),
            _MetaInfoClassMember('identifier-xr', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Aliased config command
                ''',
                'identifier_xr',
                'Cisco-IOS-XR-parser-cfg', False),
            ],
            'Cisco-IOS-XR-parser-cfg',
            'configuration',
            _yang_ns._namespaces['Cisco-IOS-XR-parser-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_parser_cfg'
        ),
    },
    'Parser.Alias.Configurations' : {
        'meta_info' : _MetaInfoClass('Parser.Alias.Configurations',
            False, 
            [
            _MetaInfoClassMember('configuration', REFERENCE_LIST, 'Configuration' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_parser_cfg', 'Parser.Alias.Configurations.Configuration', 
                [], [], 
                '''                Configuration Alias name
                ''',
                'configuration',
                'Cisco-IOS-XR-parser-cfg', False),
            ],
            'Cisco-IOS-XR-parser-cfg',
            'configurations',
            _yang_ns._namespaces['Cisco-IOS-XR-parser-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_parser_cfg'
        ),
    },
    'Parser.Alias.Alls.All' : {
        'meta_info' : _MetaInfoClass('Parser.Alias.Alls.All',
            False, 
            [
            _MetaInfoClassMember('identifier', ATTRIBUTE, 'str' , None, None, 
                [(1, 30)], [], 
                '''                Alias name
                ''',
                'identifier',
                'Cisco-IOS-XR-parser-cfg', True),
            _MetaInfoClassMember('identifier-xr', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The actual command
                ''',
                'identifier_xr',
                'Cisco-IOS-XR-parser-cfg', False),
            ],
            'Cisco-IOS-XR-parser-cfg',
            'all',
            _yang_ns._namespaces['Cisco-IOS-XR-parser-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_parser_cfg'
        ),
    },
    'Parser.Alias.Alls' : {
        'meta_info' : _MetaInfoClass('Parser.Alias.Alls',
            False, 
            [
            _MetaInfoClassMember('all', REFERENCE_LIST, 'All' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_parser_cfg', 'Parser.Alias.Alls.All', 
                [], [], 
                '''                Alias name to command mapping
                ''',
                'all',
                'Cisco-IOS-XR-parser-cfg', False),
            ],
            'Cisco-IOS-XR-parser-cfg',
            'alls',
            _yang_ns._namespaces['Cisco-IOS-XR-parser-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_parser_cfg'
        ),
    },
    'Parser.Alias' : {
        'meta_info' : _MetaInfoClass('Parser.Alias',
            False, 
            [
            _MetaInfoClassMember('alls', REFERENCE_CLASS, 'Alls' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_parser_cfg', 'Parser.Alias.Alls', 
                [], [], 
                '''                Table of all aliases configured
                ''',
                'alls',
                'Cisco-IOS-XR-parser-cfg', False),
            _MetaInfoClassMember('configurations', REFERENCE_CLASS, 'Configurations' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_parser_cfg', 'Parser.Alias.Configurations', 
                [], [], 
                '''                Configuration command alias
                ''',
                'configurations',
                'Cisco-IOS-XR-parser-cfg', False),
            _MetaInfoClassMember('execs', REFERENCE_CLASS, 'Execs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_parser_cfg', 'Parser.Alias.Execs', 
                [], [], 
                '''                Exec command alias
                ''',
                'execs',
                'Cisco-IOS-XR-parser-cfg', False),
            ],
            'Cisco-IOS-XR-parser-cfg',
            'alias',
            _yang_ns._namespaces['Cisco-IOS-XR-parser-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_parser_cfg'
        ),
    },
    'Parser.History' : {
        'meta_info' : _MetaInfoClass('Parser.History',
            False, 
            [
            _MetaInfoClassMember('size', ATTRIBUTE, 'int' , None, None, 
                [('1000', '5000')], [], 
                '''                maximum number of commands in history
                ''',
                'size',
                'Cisco-IOS-XR-parser-cfg', False),
            ],
            'Cisco-IOS-XR-parser-cfg',
            'history',
            _yang_ns._namespaces['Cisco-IOS-XR-parser-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_parser_cfg'
        ),
    },
    'Parser.InterfaceDisplay' : {
        'meta_info' : _MetaInfoClass('Parser.InterfaceDisplay',
            False, 
            [
            _MetaInfoClassMember('slot-order', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Configure Interface display order as slot order
                ''',
                'slot_order',
                'Cisco-IOS-XR-parser-cfg', False),
            ],
            'Cisco-IOS-XR-parser-cfg',
            'interface-display',
            _yang_ns._namespaces['Cisco-IOS-XR-parser-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_parser_cfg'
        ),
    },
    'Parser.NetmaskFormat' : {
        'meta_info' : _MetaInfoClass('Parser.NetmaskFormat',
            False, 
            [
            _MetaInfoClassMember('bit-count', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable ipv4 netmask-format as bit-count
                ''',
                'bit_count',
                'Cisco-IOS-XR-parser-cfg', False),
            ],
            'Cisco-IOS-XR-parser-cfg',
            'netmask-format',
            _yang_ns._namespaces['Cisco-IOS-XR-parser-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_parser_cfg'
        ),
    },
    'Parser.Configuration.Disable' : {
        'meta_info' : _MetaInfoClass('Parser.Configuration.Disable',
            False, 
            [
            _MetaInfoClassMember('usergroup', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Disable config mode for usergroup
                ''',
                'usergroup',
                'Cisco-IOS-XR-parser-cfg', False),
            ],
            'Cisco-IOS-XR-parser-cfg',
            'disable',
            _yang_ns._namespaces['Cisco-IOS-XR-parser-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_parser_cfg'
        ),
    },
    'Parser.Configuration' : {
        'meta_info' : _MetaInfoClass('Parser.Configuration',
            False, 
            [
            _MetaInfoClassMember('disable', REFERENCE_CLASS, 'Disable' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_parser_cfg', 'Parser.Configuration.Disable', 
                [], [], 
                '''                disable for read-only access users
                ''',
                'disable',
                'Cisco-IOS-XR-parser-cfg', False),
            ],
            'Cisco-IOS-XR-parser-cfg',
            'configuration',
            _yang_ns._namespaces['Cisco-IOS-XR-parser-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_parser_cfg'
        ),
    },
    'Parser.SubmodeExit' : {
        'meta_info' : _MetaInfoClass('Parser.SubmodeExit',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable the feature
                ''',
                'enable',
                'Cisco-IOS-XR-parser-cfg', False),
            ],
            'Cisco-IOS-XR-parser-cfg',
            'submode-exit',
            _yang_ns._namespaces['Cisco-IOS-XR-parser-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_parser_cfg'
        ),
    },
    'Parser' : {
        'meta_info' : _MetaInfoClass('Parser',
            False, 
            [
            _MetaInfoClassMember('alias', REFERENCE_CLASS, 'Alias' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_parser_cfg', 'Parser.Alias', 
                [], [], 
                '''                Alias for command mapping
                ''',
                'alias',
                'Cisco-IOS-XR-parser-cfg', False),
            _MetaInfoClassMember('configuration', REFERENCE_CLASS, 'Configuration' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_parser_cfg', 'Parser.Configuration', 
                [], [], 
                '''                cli configuration services
                ''',
                'configuration',
                'Cisco-IOS-XR-parser-cfg', False),
            _MetaInfoClassMember('history', REFERENCE_CLASS, 'History' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_parser_cfg', 'Parser.History', 
                [], [], 
                '''                cli commands history
                ''',
                'history',
                'Cisco-IOS-XR-parser-cfg', False),
            _MetaInfoClassMember('indentation', REFERENCE_CLASS, 'Indentation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_parser_cfg', 'Parser.Indentation', 
                [], [], 
                '''                indentation tracking
                ''',
                'indentation',
                'Cisco-IOS-XR-parser-cfg', False),
            _MetaInfoClassMember('interface-display', REFERENCE_CLASS, 'InterfaceDisplay' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_parser_cfg', 'Parser.InterfaceDisplay', 
                [], [], 
                '''                Configure the Interface display order
                ''',
                'interface_display',
                'Cisco-IOS-XR-parser-cfg', False),
            _MetaInfoClassMember('netmask-format', REFERENCE_CLASS, 'NetmaskFormat' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_parser_cfg', 'Parser.NetmaskFormat', 
                [], [], 
                '''                Ipv4 netmask-format to be configured
                ''',
                'netmask_format',
                'Cisco-IOS-XR-parser-cfg', False),
            _MetaInfoClassMember('submode-exit', REFERENCE_CLASS, 'SubmodeExit' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_parser_cfg', 'Parser.SubmodeExit', 
                [], [], 
                '''                Exit submode when only '!' seen in interactive
                mode
                ''',
                'submode_exit',
                'Cisco-IOS-XR-parser-cfg', False),
            ],
            'Cisco-IOS-XR-parser-cfg',
            'parser',
            _yang_ns._namespaces['Cisco-IOS-XR-parser-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_parser_cfg'
        ),
    },
}
_meta_table['Parser.Alias.Execs.Exec_']['meta_info'].parent =_meta_table['Parser.Alias.Execs']['meta_info']
_meta_table['Parser.Alias.Configurations.Configuration']['meta_info'].parent =_meta_table['Parser.Alias.Configurations']['meta_info']
_meta_table['Parser.Alias.Alls.All']['meta_info'].parent =_meta_table['Parser.Alias.Alls']['meta_info']
_meta_table['Parser.Alias.Execs']['meta_info'].parent =_meta_table['Parser.Alias']['meta_info']
_meta_table['Parser.Alias.Configurations']['meta_info'].parent =_meta_table['Parser.Alias']['meta_info']
_meta_table['Parser.Alias.Alls']['meta_info'].parent =_meta_table['Parser.Alias']['meta_info']
_meta_table['Parser.Configuration.Disable']['meta_info'].parent =_meta_table['Parser.Configuration']['meta_info']
_meta_table['Parser.Indentation']['meta_info'].parent =_meta_table['Parser']['meta_info']
_meta_table['Parser.Alias']['meta_info'].parent =_meta_table['Parser']['meta_info']
_meta_table['Parser.History']['meta_info'].parent =_meta_table['Parser']['meta_info']
_meta_table['Parser.InterfaceDisplay']['meta_info'].parent =_meta_table['Parser']['meta_info']
_meta_table['Parser.NetmaskFormat']['meta_info'].parent =_meta_table['Parser']['meta_info']
_meta_table['Parser.Configuration']['meta_info'].parent =_meta_table['Parser']['meta_info']
_meta_table['Parser.SubmodeExit']['meta_info'].parent =_meta_table['Parser']['meta_info']
