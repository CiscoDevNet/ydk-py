


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'InetaddresstypeEnum' : _MetaInfoEnum('InetaddresstypeEnum', 'ydk.models.cisco_ios_xe.INET_ADDRESS_MIB',
        {
            'unknown':'unknown',
            'ipv4':'ipv4',
            'ipv6':'ipv6',
            'ipv4z':'ipv4z',
            'ipv6z':'ipv6z',
            'dns':'dns',
        }, 'INET-ADDRESS-MIB', _yang_ns._namespaces['INET-ADDRESS-MIB']),
    'InetversionEnum' : _MetaInfoEnum('InetversionEnum', 'ydk.models.cisco_ios_xe.INET_ADDRESS_MIB',
        {
            'unknown':'unknown',
            'ipv4':'ipv4',
            'ipv6':'ipv6',
        }, 'INET-ADDRESS-MIB', _yang_ns._namespaces['INET-ADDRESS-MIB']),
    'InetscopetypeEnum' : _MetaInfoEnum('InetscopetypeEnum', 'ydk.models.cisco_ios_xe.INET_ADDRESS_MIB',
        {
            'interfaceLocal':'interfaceLocal',
            'linkLocal':'linkLocal',
            'subnetLocal':'subnetLocal',
            'adminLocal':'adminLocal',
            'siteLocal':'siteLocal',
            'organizationLocal':'organizationLocal',
            'global':'global_',
        }, 'INET-ADDRESS-MIB', _yang_ns._namespaces['INET-ADDRESS-MIB']),
}
