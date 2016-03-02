


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'InetAddressType_Enum' : _MetaInfoEnum('InetAddressType_Enum', 'ydk.models.inet.INET_ADDRESS_MIB',
        {
            'unknown':'UNKNOWN',
            'ipv4':'IPV4',
            'ipv6':'IPV6',
            'ipv4z':'IPV4Z',
            'ipv6z':'IPV6Z',
            'dns':'DNS',
        }, 'INET-ADDRESS-MIB', _yang_ns._namespaces['INET-ADDRESS-MIB']),
    'InetScopeType_Enum' : _MetaInfoEnum('InetScopeType_Enum', 'ydk.models.inet.INET_ADDRESS_MIB',
        {
            'interfaceLocal':'INTERFACELOCAL',
            'linkLocal':'LINKLOCAL',
            'subnetLocal':'SUBNETLOCAL',
            'adminLocal':'ADMINLOCAL',
            'siteLocal':'SITELOCAL',
            'organizationLocal':'ORGANIZATIONLOCAL',
            'global':'GLOBAL',
        }, 'INET-ADDRESS-MIB', _yang_ns._namespaces['INET-ADDRESS-MIB']),
    'InetVersion_Enum' : _MetaInfoEnum('InetVersion_Enum', 'ydk.models.inet.INET_ADDRESS_MIB',
        {
            'unknown':'UNKNOWN',
            'ipv4':'IPV4',
            'ipv6':'IPV6',
        }, 'INET-ADDRESS-MIB', _yang_ns._namespaces['INET-ADDRESS-MIB']),
}
