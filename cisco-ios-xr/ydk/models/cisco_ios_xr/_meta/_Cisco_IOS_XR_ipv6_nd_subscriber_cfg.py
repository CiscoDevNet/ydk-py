


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'Ipv6NdRouterPrefTemplateEnum' : _MetaInfoEnum('Ipv6NdRouterPrefTemplateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_subscriber_cfg',
        {
            'high':'high',
            'medium':'medium',
            'low':'low',
        }, 'Cisco-IOS-XR-ipv6-nd-subscriber-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv6-nd-subscriber-cfg']),
}
