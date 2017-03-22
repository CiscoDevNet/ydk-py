


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'Grpc.Tls' : {
        'meta_info' : _MetaInfoClass('Grpc.Tls',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable TLS
                ''',
                'enable',
                'Cisco-IOS-XR-man-ems-cfg', False),
            _MetaInfoClassMember('trustpoint', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Trustpoint Name
                ''',
                'trustpoint',
                'Cisco-IOS-XR-man-ems-cfg', False),
            ],
            'Cisco-IOS-XR-man-ems-cfg',
            'tls',
            _yang_ns._namespaces['Cisco-IOS-XR-man-ems-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ems_cfg'
        ),
    },
    'Grpc' : {
        'meta_info' : _MetaInfoClass('Grpc',
            False, 
            [
            _MetaInfoClassMember('address-family', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Address family identifier type
                ''',
                'address_family',
                'Cisco-IOS-XR-man-ems-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable GRPC
                ''',
                'enable',
                'Cisco-IOS-XR-man-ems-cfg', False),
            _MetaInfoClassMember('max-request-per-user', ATTRIBUTE, 'int' , None, None, 
                [('1', '32')], [], 
                '''                Maximum concurrent requests per user
                ''',
                'max_request_per_user',
                'Cisco-IOS-XR-man-ems-cfg', False),
            _MetaInfoClassMember('max-request-total', ATTRIBUTE, 'int' , None, None, 
                [('1', '256')], [], 
                '''                Maximum concurrent requests in total
                ''',
                'max_request_total',
                'Cisco-IOS-XR-man-ems-cfg', False),
            _MetaInfoClassMember('port', ATTRIBUTE, 'int' , None, None, 
                [('10000', '57999')], [], 
                '''                Server listening port
                ''',
                'port',
                'Cisco-IOS-XR-man-ems-cfg', False),
            _MetaInfoClassMember('tls', REFERENCE_CLASS, 'Tls' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ems_cfg', 'Grpc.Tls', 
                [], [], 
                '''                Transport Layer Security (TLS)
                ''',
                'tls',
                'Cisco-IOS-XR-man-ems-cfg', False),
            ],
            'Cisco-IOS-XR-man-ems-cfg',
            'grpc',
            _yang_ns._namespaces['Cisco-IOS-XR-man-ems-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ems_cfg'
        ),
    },
}
_meta_table['Grpc.Tls']['meta_info'].parent =_meta_table['Grpc']['meta_info']
