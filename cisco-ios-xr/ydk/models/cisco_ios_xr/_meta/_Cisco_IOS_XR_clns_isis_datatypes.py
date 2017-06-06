


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'IsisSubAddressFamilyEnum' : _MetaInfoEnum('IsisSubAddressFamilyEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes',
        {
            'unicast':'unicast',
            'multicast':'multicast',
        }, 'Cisco-IOS-XR-clns-isis-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-datatypes']),
    'IsisAddressFamilyEnum' : _MetaInfoEnum('IsisAddressFamilyEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes',
        {
            'ipv4':'ipv4',
            'ipv6':'ipv6',
        }, 'Cisco-IOS-XR-clns-isis-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-datatypes']),
    'IsisInternalLevelEnum' : _MetaInfoEnum('IsisInternalLevelEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_datatypes',
        {
            'not-set':'not_set',
            'level1':'level1',
            'level2':'level2',
        }, 'Cisco-IOS-XR-clns-isis-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-datatypes']),
}
