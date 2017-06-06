


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'SwitchRpc.Input.Statck' : {
        'meta_info' : _MetaInfoClass('SwitchRpc.Input.Statck',
            False, 
            [
            _MetaInfoClassMember('port', ATTRIBUTE, 'int' , None, None, 
                [('1', '2')], [], 
                '''                <1-2>  Stack port number to enable/disable
                ''',
                'port',
                'Cisco-IOS-XE-rpc', False),
            ],
            'Cisco-IOS-XE-rpc',
            'statck',
            _yang_ns._namespaces['Cisco-IOS-XE-rpc'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc'
        ),
    },
    'SwitchRpc.Input' : {
        'meta_info' : _MetaInfoClass('SwitchRpc.Input',
            False, 
            [
            _MetaInfoClassMember('switch-number', ATTRIBUTE, 'int' , None, None, 
                [('1', '9')], [], 
                '''                ''',
                'switch_number',
                'Cisco-IOS-XE-rpc', False),
            _MetaInfoClassMember('priority', ATTRIBUTE, 'int' , None, None, 
                [('1', '15')], [], 
                '''                <1-15>  Switch Priority
                ''',
                'priority',
                'Cisco-IOS-XE-rpc', False),
            _MetaInfoClassMember('renumber', ATTRIBUTE, 'int' , None, None, 
                [('1', '9')], [], 
                '''                <1-9>  New number of the Switch
                ''',
                'renumber',
                'Cisco-IOS-XE-rpc', False),
            _MetaInfoClassMember('statck', REFERENCE_CLASS, 'Statck' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc', 'SwitchRpc.Input.Statck', 
                [], [], 
                '''                ''',
                'statck',
                'Cisco-IOS-XE-rpc', False),
            ],
            'Cisco-IOS-XE-rpc',
            'input',
            _yang_ns._namespaces['Cisco-IOS-XE-rpc'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc'
        ),
    },
    'SwitchRpc.Output' : {
        'meta_info' : _MetaInfoClass('SwitchRpc.Output',
            False, 
            [
            _MetaInfoClassMember('result', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Output returned by the network element
                ''',
                'result',
                'Cisco-IOS-XE-rpc', False),
            ],
            'Cisco-IOS-XE-rpc',
            'output',
            _yang_ns._namespaces['Cisco-IOS-XE-rpc'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc'
        ),
    },
    'SwitchRpc' : {
        'meta_info' : _MetaInfoClass('SwitchRpc',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc', 'SwitchRpc.Input', 
                [], [], 
                '''                ''',
                'input',
                'Cisco-IOS-XE-rpc', False),
            _MetaInfoClassMember('output', REFERENCE_CLASS, 'Output' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc', 'SwitchRpc.Output', 
                [], [], 
                '''                ''',
                'output',
                'Cisco-IOS-XE-rpc', False),
            ],
            'Cisco-IOS-XE-rpc',
            'switch',
            _yang_ns._namespaces['Cisco-IOS-XE-rpc'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc'
        ),
    },
    'DefaultRpc.Input' : {
        'meta_info' : _MetaInfoClass('DefaultRpc.Input',
            False, 
            [
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-zA-Z.]+)'], 
                '''                Select an interface to configure
                ''',
                'interface',
                'Cisco-IOS-XE-rpc', False),
            ],
            'Cisco-IOS-XE-rpc',
            'input',
            _yang_ns._namespaces['Cisco-IOS-XE-rpc'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc'
        ),
    },
    'DefaultRpc.Output' : {
        'meta_info' : _MetaInfoClass('DefaultRpc.Output',
            False, 
            [
            _MetaInfoClassMember('result', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Output returned by the network element
                ''',
                'result',
                'Cisco-IOS-XE-rpc', False),
            ],
            'Cisco-IOS-XE-rpc',
            'output',
            _yang_ns._namespaces['Cisco-IOS-XE-rpc'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc'
        ),
    },
    'DefaultRpc' : {
        'meta_info' : _MetaInfoClass('DefaultRpc',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc', 'DefaultRpc.Input', 
                [], [], 
                '''                ''',
                'input',
                'Cisco-IOS-XE-rpc', False),
            _MetaInfoClassMember('output', REFERENCE_CLASS, 'Output' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc', 'DefaultRpc.Output', 
                [], [], 
                '''                ''',
                'output',
                'Cisco-IOS-XE-rpc', False),
            ],
            'Cisco-IOS-XE-rpc',
            'default',
            _yang_ns._namespaces['Cisco-IOS-XE-rpc'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc'
        ),
    },
    'ReloadRpc.Output' : {
        'meta_info' : _MetaInfoClass('ReloadRpc.Output',
            False, 
            [
            _MetaInfoClassMember('result', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Output returned by the network element
                ''',
                'result',
                'Cisco-IOS-XE-rpc', False),
            ],
            'Cisco-IOS-XE-rpc',
            'output',
            _yang_ns._namespaces['Cisco-IOS-XE-rpc'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc'
        ),
    },
    'ReloadRpc' : {
        'meta_info' : _MetaInfoClass('ReloadRpc',
            False, 
            [
            _MetaInfoClassMember('output', REFERENCE_CLASS, 'Output' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc', 'ReloadRpc.Output', 
                [], [], 
                '''                ''',
                'output',
                'Cisco-IOS-XE-rpc', False),
            ],
            'Cisco-IOS-XE-rpc',
            'reload',
            _yang_ns._namespaces['Cisco-IOS-XE-rpc'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc'
        ),
    },
    'LicenseRpc.Input.Smart.Register' : {
        'meta_info' : _MetaInfoClass('LicenseRpc.Input.Smart.Register',
            False, 
            [
            _MetaInfoClassMember('idtoken', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                ''',
                'idtoken',
                'Cisco-IOS-XE-rpc', False),
            ],
            'Cisco-IOS-XE-rpc',
            'register',
            _yang_ns._namespaces['Cisco-IOS-XE-rpc'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc'
        ),
    },
    'LicenseRpc.Input.Smart.Renew' : {
        'meta_info' : _MetaInfoClass('LicenseRpc.Input.Smart.Renew',
            False, 
            [
            _MetaInfoClassMember('id', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                ''',
                'id',
                'Cisco-IOS-XE-rpc', False),
            _MetaInfoClassMember('auth', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                ''',
                'auth',
                'Cisco-IOS-XE-rpc', False),
            ],
            'Cisco-IOS-XE-rpc',
            'renew',
            _yang_ns._namespaces['Cisco-IOS-XE-rpc'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc'
        ),
    },
    'LicenseRpc.Input.Smart' : {
        'meta_info' : _MetaInfoClass('LicenseRpc.Input.Smart',
            False, 
            [
            _MetaInfoClassMember('register', REFERENCE_CLASS, 'Register' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc', 'LicenseRpc.Input.Smart.Register', 
                [], [], 
                '''                ''',
                'register',
                'Cisco-IOS-XE-rpc', False),
            _MetaInfoClassMember('deregister', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                ''',
                'deregister',
                'Cisco-IOS-XE-rpc', False),
            _MetaInfoClassMember('renew', REFERENCE_CLASS, 'Renew' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc', 'LicenseRpc.Input.Smart.Renew', 
                [], [], 
                '''                ''',
                'renew',
                'Cisco-IOS-XE-rpc', False),
            ],
            'Cisco-IOS-XE-rpc',
            'smart',
            _yang_ns._namespaces['Cisco-IOS-XE-rpc'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc'
        ),
    },
    'LicenseRpc.Input' : {
        'meta_info' : _MetaInfoClass('LicenseRpc.Input',
            False, 
            [
            _MetaInfoClassMember('smart', REFERENCE_CLASS, 'Smart' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc', 'LicenseRpc.Input.Smart', 
                [], [], 
                '''                ''',
                'smart',
                'Cisco-IOS-XE-rpc', False),
            ],
            'Cisco-IOS-XE-rpc',
            'input',
            _yang_ns._namespaces['Cisco-IOS-XE-rpc'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc'
        ),
    },
    'LicenseRpc.Output' : {
        'meta_info' : _MetaInfoClass('LicenseRpc.Output',
            False, 
            [
            _MetaInfoClassMember('result', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Output returned by the network element
                ''',
                'result',
                'Cisco-IOS-XE-rpc', False),
            ],
            'Cisco-IOS-XE-rpc',
            'output',
            _yang_ns._namespaces['Cisco-IOS-XE-rpc'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc'
        ),
    },
    'LicenseRpc' : {
        'meta_info' : _MetaInfoClass('LicenseRpc',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc', 'LicenseRpc.Input', 
                [], [], 
                '''                ''',
                'input',
                'Cisco-IOS-XE-rpc', False),
            _MetaInfoClassMember('output', REFERENCE_CLASS, 'Output' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc', 'LicenseRpc.Output', 
                [], [], 
                '''                ''',
                'output',
                'Cisco-IOS-XE-rpc', False),
            ],
            'Cisco-IOS-XE-rpc',
            'license',
            _yang_ns._namespaces['Cisco-IOS-XE-rpc'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_rpc'
        ),
    },
}
_meta_table['SwitchRpc.Input.Statck']['meta_info'].parent =_meta_table['SwitchRpc.Input']['meta_info']
_meta_table['SwitchRpc.Input']['meta_info'].parent =_meta_table['SwitchRpc']['meta_info']
_meta_table['SwitchRpc.Output']['meta_info'].parent =_meta_table['SwitchRpc']['meta_info']
_meta_table['DefaultRpc.Input']['meta_info'].parent =_meta_table['DefaultRpc']['meta_info']
_meta_table['DefaultRpc.Output']['meta_info'].parent =_meta_table['DefaultRpc']['meta_info']
_meta_table['ReloadRpc.Output']['meta_info'].parent =_meta_table['ReloadRpc']['meta_info']
_meta_table['LicenseRpc.Input.Smart.Register']['meta_info'].parent =_meta_table['LicenseRpc.Input.Smart']['meta_info']
_meta_table['LicenseRpc.Input.Smart.Renew']['meta_info'].parent =_meta_table['LicenseRpc.Input.Smart']['meta_info']
_meta_table['LicenseRpc.Input.Smart']['meta_info'].parent =_meta_table['LicenseRpc.Input']['meta_info']
_meta_table['LicenseRpc.Input']['meta_info'].parent =_meta_table['LicenseRpc']['meta_info']
_meta_table['LicenseRpc.Output']['meta_info'].parent =_meta_table['LicenseRpc']['meta_info']
