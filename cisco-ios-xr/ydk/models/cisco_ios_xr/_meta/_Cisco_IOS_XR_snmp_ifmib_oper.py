


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'LinkUpDownStatusEnum' : _MetaInfoEnum('LinkUpDownStatusEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_ifmib_oper',
        {
            'enabled':'enabled',
            'disabled':'disabled',
        }, 'Cisco-IOS-XR-snmp-ifmib-oper', _yang_ns._namespaces['Cisco-IOS-XR-snmp-ifmib-oper']),
}
