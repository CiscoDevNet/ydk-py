


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'HostNames' : {
        'meta_info' : _MetaInfoClass('HostNames',
            False, 
            [
            _MetaInfoClassMember('host-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Configure system's hostname
                ''',
                'host_name',
                'Cisco-IOS-XR-shellutil-cfg', False),
            ],
            'Cisco-IOS-XR-shellutil-cfg',
            'host-names',
            _yang_ns._namespaces['Cisco-IOS-XR-shellutil-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_shellutil_cfg'
        ),
    },
}
