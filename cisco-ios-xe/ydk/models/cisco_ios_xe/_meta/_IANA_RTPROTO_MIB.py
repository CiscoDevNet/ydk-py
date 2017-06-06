


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'IanaiprouteprotocolEnum' : _MetaInfoEnum('IanaiprouteprotocolEnum', 'ydk.models.cisco_ios_xe.IANA_RTPROTO_MIB',
        {
            'other':'other',
            'local':'local',
            'netmgmt':'netmgmt',
            'icmp':'icmp',
            'egp':'egp',
            'ggp':'ggp',
            'hello':'hello',
            'rip':'rip',
            'isIs':'isIs',
            'esIs':'esIs',
            'ciscoIgrp':'ciscoIgrp',
            'bbnSpfIgp':'bbnSpfIgp',
            'ospf':'ospf',
            'bgp':'bgp',
            'idpr':'idpr',
            'ciscoEigrp':'ciscoEigrp',
            'dvmrp':'dvmrp',
        }, 'IANA-RTPROTO-MIB', _yang_ns._namespaces['IANA-RTPROTO-MIB']),
    'IanaipmrouteprotocolEnum' : _MetaInfoEnum('IanaipmrouteprotocolEnum', 'ydk.models.cisco_ios_xe.IANA_RTPROTO_MIB',
        {
            'other':'other',
            'local':'local',
            'netmgmt':'netmgmt',
            'dvmrp':'dvmrp',
            'mospf':'mospf',
            'pimSparseDense':'pimSparseDense',
            'cbt':'cbt',
            'pimSparseMode':'pimSparseMode',
            'pimDenseMode':'pimDenseMode',
            'igmpOnly':'igmpOnly',
            'bgmp':'bgmp',
            'msdp':'msdp',
        }, 'IANA-RTPROTO-MIB', _yang_ns._namespaces['IANA-RTPROTO-MIB']),
}
