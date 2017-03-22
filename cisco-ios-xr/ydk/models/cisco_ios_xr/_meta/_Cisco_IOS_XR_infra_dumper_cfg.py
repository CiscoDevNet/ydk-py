


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'Exception.Choice1' : {
        'meta_info' : _MetaInfoClass('Exception.Choice1',
            False, 
            [
            _MetaInfoClassMember('compress', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Specify 'true' to compress core files dumped on
                this path, 'false' to not compress
                ''',
                'compress',
                'Cisco-IOS-XR-infra-dumper-cfg', False),
            _MetaInfoClassMember('file-path', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Protocol and directory
                ''',
                'file_path',
                'Cisco-IOS-XR-infra-dumper-cfg', False),
            _MetaInfoClassMember('filename', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Dump filename
                ''',
                'filename',
                'Cisco-IOS-XR-infra-dumper-cfg', False),
            _MetaInfoClassMember('higher-limit', ATTRIBUTE, 'int' , None, None, 
                [('5', '64')], [], 
                '''                Higher limit.  This is required if Filename is
                specified.
                ''',
                'higher_limit',
                'Cisco-IOS-XR-infra-dumper-cfg', False),
            _MetaInfoClassMember('lower-limit', ATTRIBUTE, 'int' , None, None, 
                [('0', '4')], [], 
                '''                Lower limit.  This is required if Filename is
                specified.
                ''',
                'lower_limit',
                'Cisco-IOS-XR-infra-dumper-cfg', False),
            ],
            'Cisco-IOS-XR-infra-dumper-cfg',
            'choice1',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-dumper-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_dumper_cfg'
        ),
    },
    'Exception.Choice3' : {
        'meta_info' : _MetaInfoClass('Exception.Choice3',
            False, 
            [
            _MetaInfoClassMember('compress', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Specify 'true' to compress core files dumped on
                this path, 'false' to not compress
                ''',
                'compress',
                'Cisco-IOS-XR-infra-dumper-cfg', False),
            _MetaInfoClassMember('file-path', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Protocol and directory
                ''',
                'file_path',
                'Cisco-IOS-XR-infra-dumper-cfg', False),
            _MetaInfoClassMember('filename', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Dump filename
                ''',
                'filename',
                'Cisco-IOS-XR-infra-dumper-cfg', False),
            _MetaInfoClassMember('higher-limit', ATTRIBUTE, 'int' , None, None, 
                [('5', '64')], [], 
                '''                Higher limit.  This is required if Filename is
                specified.
                ''',
                'higher_limit',
                'Cisco-IOS-XR-infra-dumper-cfg', False),
            _MetaInfoClassMember('lower-limit', ATTRIBUTE, 'int' , None, None, 
                [('0', '4')], [], 
                '''                Lower limit.  This is required if Filename is
                specified.
                ''',
                'lower_limit',
                'Cisco-IOS-XR-infra-dumper-cfg', False),
            ],
            'Cisco-IOS-XR-infra-dumper-cfg',
            'choice3',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-dumper-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_dumper_cfg'
        ),
    },
    'Exception.Choice2' : {
        'meta_info' : _MetaInfoClass('Exception.Choice2',
            False, 
            [
            _MetaInfoClassMember('compress', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Specify 'true' to compress core files dumped on
                this path, 'false' to not compress
                ''',
                'compress',
                'Cisco-IOS-XR-infra-dumper-cfg', False),
            _MetaInfoClassMember('file-path', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Protocol and directory
                ''',
                'file_path',
                'Cisco-IOS-XR-infra-dumper-cfg', False),
            _MetaInfoClassMember('filename', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Dump filename
                ''',
                'filename',
                'Cisco-IOS-XR-infra-dumper-cfg', False),
            _MetaInfoClassMember('higher-limit', ATTRIBUTE, 'int' , None, None, 
                [('5', '64')], [], 
                '''                Higher limit.  This is required if Filename is
                specified.
                ''',
                'higher_limit',
                'Cisco-IOS-XR-infra-dumper-cfg', False),
            _MetaInfoClassMember('lower-limit', ATTRIBUTE, 'int' , None, None, 
                [('0', '4')], [], 
                '''                Lower limit.  This is required if Filename is
                specified.
                ''',
                'lower_limit',
                'Cisco-IOS-XR-infra-dumper-cfg', False),
            ],
            'Cisco-IOS-XR-infra-dumper-cfg',
            'choice2',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-dumper-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_dumper_cfg'
        ),
    },
    'Exception' : {
        'meta_info' : _MetaInfoClass('Exception',
            False, 
            [
            _MetaInfoClassMember('choice1', REFERENCE_CLASS, 'Choice1' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_dumper_cfg', 'Exception.Choice1', 
                [], [], 
                '''                Preference of the dump location
                ''',
                'choice1',
                'Cisco-IOS-XR-infra-dumper-cfg', False),
            _MetaInfoClassMember('choice2', REFERENCE_CLASS, 'Choice2' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_dumper_cfg', 'Exception.Choice2', 
                [], [], 
                '''                Preference of the dump location
                ''',
                'choice2',
                'Cisco-IOS-XR-infra-dumper-cfg', False),
            _MetaInfoClassMember('choice3', REFERENCE_CLASS, 'Choice3' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_dumper_cfg', 'Exception.Choice3', 
                [], [], 
                '''                Preference of the dump location
                ''',
                'choice3',
                'Cisco-IOS-XR-infra-dumper-cfg', False),
            _MetaInfoClassMember('kernel-debugger', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable kernel debugger
                ''',
                'kernel_debugger',
                'Cisco-IOS-XR-infra-dumper-cfg', False),
            _MetaInfoClassMember('packet-memory', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Specify 'true' to dump packet memory for all
                process, 'false' to disable dump of packet
                memory
                ''',
                'packet_memory',
                'Cisco-IOS-XR-infra-dumper-cfg', False),
            _MetaInfoClassMember('sparse', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Specify 'true' to enable sparse core dump,
                'false' to disable sparse core dump
                ''',
                'sparse',
                'Cisco-IOS-XR-infra-dumper-cfg', False),
            _MetaInfoClassMember('sparse-size', ATTRIBUTE, 'int' , None, None, 
                [('1', '4095')], [], 
                '''                Switch to sparse core dump at this size
                ''',
                'sparse_size',
                'Cisco-IOS-XR-infra-dumper-cfg', False),
            ],
            'Cisco-IOS-XR-infra-dumper-cfg',
            'exception',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-dumper-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_dumper_cfg'
        ),
    },
}
_meta_table['Exception.Choice1']['meta_info'].parent =_meta_table['Exception']['meta_info']
_meta_table['Exception.Choice3']['meta_info'].parent =_meta_table['Exception']['meta_info']
_meta_table['Exception.Choice2']['meta_info'].parent =_meta_table['Exception']['meta_info']
