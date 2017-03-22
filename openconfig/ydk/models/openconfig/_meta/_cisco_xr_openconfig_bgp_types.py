


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'BgpOriginAttrTypeEnum' : _MetaInfoEnum('BgpOriginAttrTypeEnum', 'ydk.models.openconfig.cisco_xr_openconfig_bgp_types',
        {
            'IGP':'IGP',
            'EGP':'EGP',
            'INCOMPLETE':'INCOMPLETE',
        }, 'cisco-xr-openconfig-bgp-types', _yang_ns._namespaces['cisco-xr-openconfig-bgp-types']),
    'Afi_Safi_TypeIdentity' : {
        'meta_info' : _MetaInfoClass('Afi_Safi_TypeIdentity',
            False, 
            [
            ],
            'cisco-xr-openconfig-bgp-types',
            'AFI_SAFI_TYPE',
            _yang_ns._namespaces['cisco-xr-openconfig-bgp-types'],
        'ydk.models.openconfig.cisco_xr_openconfig_bgp_types'
        ),
    },
    'Ipv6_UnicastIdentity' : {
        'meta_info' : _MetaInfoClass('Ipv6_UnicastIdentity',
            False, 
            [
            ],
            'cisco-xr-openconfig-bgp-types',
            'IPV6_UNICAST',
            _yang_ns._namespaces['cisco-xr-openconfig-bgp-types'],
        'ydk.models.openconfig.cisco_xr_openconfig_bgp_types'
        ),
    },
    'Ipv4_UnicastIdentity' : {
        'meta_info' : _MetaInfoClass('Ipv4_UnicastIdentity',
            False, 
            [
            ],
            'cisco-xr-openconfig-bgp-types',
            'IPV4_UNICAST',
            _yang_ns._namespaces['cisco-xr-openconfig-bgp-types'],
        'ydk.models.openconfig.cisco_xr_openconfig_bgp_types'
        ),
    },
}
