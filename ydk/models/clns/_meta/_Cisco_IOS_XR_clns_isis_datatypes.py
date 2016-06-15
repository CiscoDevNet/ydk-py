


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYModelError
from ydk.models import _yang_ns

_meta_table = {
    'IsisInternalLevelEnum' : _MetaInfoEnum('IsisInternalLevelEnum', 'ydk.models.clns.Cisco_IOS_XR_clns_isis_datatypes',
        {
            'not-set':'NOT_SET',
            'level1':'LEVEL1',
            'level2':'LEVEL2',
        }, 'Cisco-IOS-XR-clns-isis-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-datatypes']),
    'IsisAddressFamilyEnum' : _MetaInfoEnum('IsisAddressFamilyEnum', 'ydk.models.clns.Cisco_IOS_XR_clns_isis_datatypes',
        {
            'ipv4':'IPV4',
            'ipv6':'IPV6',
        }, 'Cisco-IOS-XR-clns-isis-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-datatypes']),
    'IsisSubAddressFamilyEnum' : _MetaInfoEnum('IsisSubAddressFamilyEnum', 'ydk.models.clns.Cisco_IOS_XR_clns_isis_datatypes',
        {
            'unicast':'UNICAST',
            'multicast':'MULTICAST',
        }, 'Cisco-IOS-XR-clns-isis-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-datatypes']),
}
