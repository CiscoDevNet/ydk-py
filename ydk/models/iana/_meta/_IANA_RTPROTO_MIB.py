


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'IANAipMRouteProtocol_Enum' : _MetaInfoEnum('IANAipMRouteProtocol_Enum', 'ydk.models.iana.IANA_RTPROTO_MIB',
        {
            'other':'OTHER',
            'local':'LOCAL',
            'netmgmt':'NETMGMT',
            'dvmrp':'DVMRP',
            'mospf':'MOSPF',
            'pimSparseDense':'PIMSPARSEDENSE',
            'cbt':'CBT',
            'pimSparseMode':'PIMSPARSEMODE',
            'pimDenseMode':'PIMDENSEMODE',
            'igmpOnly':'IGMPONLY',
            'bgmp':'BGMP',
            'msdp':'MSDP',
        }, 'IANA-RTPROTO-MIB', _yang_ns._namespaces['IANA-RTPROTO-MIB']),
    'IANAipRouteProtocol_Enum' : _MetaInfoEnum('IANAipRouteProtocol_Enum', 'ydk.models.iana.IANA_RTPROTO_MIB',
        {
            'other':'OTHER',
            'local':'LOCAL',
            'netmgmt':'NETMGMT',
            'icmp':'ICMP',
            'egp':'EGP',
            'ggp':'GGP',
            'hello':'HELLO',
            'rip':'RIP',
            'isIs':'ISIS',
            'esIs':'ESIS',
            'ciscoIgrp':'CISCOIGRP',
            'bbnSpfIgp':'BBNSPFIGP',
            'ospf':'OSPF',
            'bgp':'BGP',
            'idpr':'IDPR',
            'ciscoEigrp':'CISCOEIGRP',
            'dvmrp':'DVMRP',
        }, 'IANA-RTPROTO-MIB', _yang_ns._namespaces['IANA-RTPROTO-MIB']),
}
