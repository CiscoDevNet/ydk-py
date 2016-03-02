


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'AclUsageAppIdEnum_Enum' : _MetaInfoEnum('AclUsageAppIdEnum_Enum', 'ydk.models.common.Cisco_IOS_XR_common_acl_datatypes',
        {
            'pfilter':'PFILTER',
            'bgp':'BGP',
            'ospf':'OSPF',
        }, 'Cisco-IOS-XR-common-acl-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-common-acl-datatypes']),
}
