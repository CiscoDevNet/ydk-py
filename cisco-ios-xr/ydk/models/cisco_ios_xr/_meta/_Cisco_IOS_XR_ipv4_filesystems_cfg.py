


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'Rcp.RcpClient' : {
        'meta_info' : _MetaInfoClass('Rcp.RcpClient',
            False, 
            [
            _MetaInfoClassMember('source-interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Specify interface for source address in
                connections
                ''',
                'source_interface',
                'Cisco-IOS-XR-ipv4-filesystems-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-filesystems-cfg',
            'rcp-client',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-filesystems-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_filesystems_cfg'
        ),
    },
    'Rcp' : {
        'meta_info' : _MetaInfoClass('Rcp',
            False, 
            [
            _MetaInfoClassMember('rcp-client', REFERENCE_CLASS, 'RcpClient' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_filesystems_cfg', 'Rcp.RcpClient', 
                [], [], 
                '''                RCP client configuration
                ''',
                'rcp_client',
                'Cisco-IOS-XR-ipv4-filesystems-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-filesystems-cfg',
            'rcp',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-filesystems-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_filesystems_cfg'
        ),
    },
    'Ftp.FtpClient' : {
        'meta_info' : _MetaInfoClass('Ftp.FtpClient',
            False, 
            [
            _MetaInfoClassMember('anonymous-password', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Password for anonymous user (ftp server
                dependent)
                ''',
                'anonymous_password',
                'Cisco-IOS-XR-ipv4-filesystems-cfg', False),
            _MetaInfoClassMember('passive', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable connect using passive mode
                ''',
                'passive',
                'Cisco-IOS-XR-ipv4-filesystems-cfg', False),
            _MetaInfoClassMember('password', ATTRIBUTE, 'str' , None, None, 
                [], [b'(!.+)|([^!].+)'], 
                '''                Specify password for ftp connnection
                ''',
                'password',
                'Cisco-IOS-XR-ipv4-filesystems-cfg', False),
            _MetaInfoClassMember('source-interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Specify interface for source address in
                connections
                ''',
                'source_interface',
                'Cisco-IOS-XR-ipv4-filesystems-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-filesystems-cfg',
            'ftp-client',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-filesystems-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_filesystems_cfg'
        ),
    },
    'Ftp' : {
        'meta_info' : _MetaInfoClass('Ftp',
            False, 
            [
            _MetaInfoClassMember('ftp-client', REFERENCE_CLASS, 'FtpClient' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_filesystems_cfg', 'Ftp.FtpClient', 
                [], [], 
                '''                FTP client configuration
                ''',
                'ftp_client',
                'Cisco-IOS-XR-ipv4-filesystems-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-filesystems-cfg',
            'ftp',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-filesystems-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_filesystems_cfg'
        ),
    },
    'Tftp.TftpClient' : {
        'meta_info' : _MetaInfoClass('Tftp.TftpClient',
            False, 
            [
            _MetaInfoClassMember('source-interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Specify interface for source address in
                connections
                ''',
                'source_interface',
                'Cisco-IOS-XR-ipv4-filesystems-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-filesystems-cfg',
            'tftp-client',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-filesystems-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_filesystems_cfg'
        ),
    },
    'Tftp' : {
        'meta_info' : _MetaInfoClass('Tftp',
            False, 
            [
            _MetaInfoClassMember('tftp-client', REFERENCE_CLASS, 'TftpClient' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_filesystems_cfg', 'Tftp.TftpClient', 
                [], [], 
                '''                TFTP client configuration
                ''',
                'tftp_client',
                'Cisco-IOS-XR-ipv4-filesystems-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-filesystems-cfg',
            'tftp',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-filesystems-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_filesystems_cfg'
        ),
    },
}
_meta_table['Rcp.RcpClient']['meta_info'].parent =_meta_table['Rcp']['meta_info']
_meta_table['Ftp.FtpClient']['meta_info'].parent =_meta_table['Ftp']['meta_info']
_meta_table['Tftp.TftpClient']['meta_info'].parent =_meta_table['Tftp']['meta_info']
