


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'IpUdp.NumThread' : {
        'meta_info' : _MetaInfoClass('IpUdp.NumThread',
            False, 
            [
            _MetaInfoClassMember('udp-in-q-threads', ATTRIBUTE, 'int' , None, None, 
                [('1', '16')], [], 
                '''                InQ Threads
                ''',
                'udp_in_q_threads',
                'Cisco-IOS-XR-ip-udp-cfg', False),
            _MetaInfoClassMember('udp-out-q-threads', ATTRIBUTE, 'int' , None, None, 
                [('1', '16')], [], 
                '''                OutQ Threads
                ''',
                'udp_out_q_threads',
                'Cisco-IOS-XR-ip-udp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-udp-cfg',
            'num-thread',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-udp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_cfg'
        ),
    },
    'IpUdp.Directory' : {
        'meta_info' : _MetaInfoClass('IpUdp.Directory',
            False, 
            [
            _MetaInfoClassMember('directoryname', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Directory name
                ''',
                'directoryname',
                'Cisco-IOS-XR-ip-udp-cfg', False),
            _MetaInfoClassMember('max-file-size-files', ATTRIBUTE, 'int' , None, None, 
                [('1024', '4294967295')], [], 
                '''                Set size of debug files in bytes
                ''',
                'max_file_size_files',
                'Cisco-IOS-XR-ip-udp-cfg', False),
            _MetaInfoClassMember('max-udp-debug-files', ATTRIBUTE, 'int' , None, None, 
                [('1', '5000')], [], 
                '''                Set number of Debug files
                ''',
                'max_udp_debug_files',
                'Cisco-IOS-XR-ip-udp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-udp-cfg',
            'directory',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-udp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_cfg'
        ),
    },
    'IpUdp' : {
        'meta_info' : _MetaInfoClass('IpUdp',
            False, 
            [
            _MetaInfoClassMember('directory', REFERENCE_CLASS, 'Directory' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_cfg', 'IpUdp.Directory', 
                [], [], 
                '''                UDP directory details
                ''',
                'directory',
                'Cisco-IOS-XR-ip-udp-cfg', False),
            _MetaInfoClassMember('num-thread', REFERENCE_CLASS, 'NumThread' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_cfg', 'IpUdp.NumThread', 
                [], [], 
                '''                UDP InQueue and OutQueue threads
                ''',
                'num_thread',
                'Cisco-IOS-XR-ip-udp-cfg', False),
            _MetaInfoClassMember('receive-q', ATTRIBUTE, 'int' , None, None, 
                [('40', '800')], [], 
                '''                UDP receive Queue Size
                ''',
                'receive_q',
                'Cisco-IOS-XR-ip-udp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-udp-cfg',
            'ip-udp',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-udp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_cfg'
        ),
    },
}
_meta_table['IpUdp.NumThread']['meta_info'].parent =_meta_table['IpUdp']['meta_info']
_meta_table['IpUdp.Directory']['meta_info'].parent =_meta_table['IpUdp']['meta_info']
