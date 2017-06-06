


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'FileSystem.Node.FileSystem_' : {
        'meta_info' : _MetaInfoClass('FileSystem.Node.FileSystem_',
            False, 
            [
            _MetaInfoClassMember('flags', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Flags of file system
                ''',
                'flags',
                'Cisco-IOS-XR-shellutil-filesystem-oper', False),
            _MetaInfoClassMember('free', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Free space in the file system in bytes
                ''',
                'free',
                'Cisco-IOS-XR-shellutil-filesystem-oper', False),
            _MetaInfoClassMember('prefixes', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Prefixes of file system
                ''',
                'prefixes',
                'Cisco-IOS-XR-shellutil-filesystem-oper', False),
            _MetaInfoClassMember('size', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Size of the file system in bytes
                ''',
                'size',
                'Cisco-IOS-XR-shellutil-filesystem-oper', False),
            _MetaInfoClassMember('type', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Type of file system
                ''',
                'type',
                'Cisco-IOS-XR-shellutil-filesystem-oper', False),
            ],
            'Cisco-IOS-XR-shellutil-filesystem-oper',
            'file-system',
            _yang_ns._namespaces['Cisco-IOS-XR-shellutil-filesystem-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_shellutil_filesystem_oper'
        ),
    },
    'FileSystem.Node' : {
        'meta_info' : _MetaInfoClass('FileSystem.Node',
            False, 
            [
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Node name
                ''',
                'node_name',
                'Cisco-IOS-XR-shellutil-filesystem-oper', True),
            _MetaInfoClassMember('file-system', REFERENCE_LIST, 'FileSystem_' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_shellutil_filesystem_oper', 'FileSystem.Node.FileSystem_', 
                [], [], 
                '''                Available file systems
                ''',
                'file_system',
                'Cisco-IOS-XR-shellutil-filesystem-oper', False),
            ],
            'Cisco-IOS-XR-shellutil-filesystem-oper',
            'node',
            _yang_ns._namespaces['Cisco-IOS-XR-shellutil-filesystem-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_shellutil_filesystem_oper'
        ),
    },
    'FileSystem' : {
        'meta_info' : _MetaInfoClass('FileSystem',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_shellutil_filesystem_oper', 'FileSystem.Node', 
                [], [], 
                '''                Node ID
                ''',
                'node',
                'Cisco-IOS-XR-shellutil-filesystem-oper', False),
            ],
            'Cisco-IOS-XR-shellutil-filesystem-oper',
            'file-system',
            _yang_ns._namespaces['Cisco-IOS-XR-shellutil-filesystem-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_shellutil_filesystem_oper'
        ),
    },
}
_meta_table['FileSystem.Node.FileSystem_']['meta_info'].parent =_meta_table['FileSystem.Node']['meta_info']
_meta_table['FileSystem.Node']['meta_info'].parent =_meta_table['FileSystem']['meta_info']
