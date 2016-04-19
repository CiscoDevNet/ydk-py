


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'LinkUpDownStatusEnum' : _MetaInfoEnum('LinkUpDownStatusEnum', 'ydk.models.snmp.Cisco_IOS_XR_snmp_ifmib_oper',
        {
            'enabled':'ENABLED',
            'disabled':'DISABLED',
        }, 'Cisco-IOS-XR-snmp-ifmib-oper', _yang_ns._namespaces['Cisco-IOS-XR-snmp-ifmib-oper']),
}
