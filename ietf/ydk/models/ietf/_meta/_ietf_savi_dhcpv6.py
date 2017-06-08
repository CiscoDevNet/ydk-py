


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns

_meta_table = {
    'SaviDhcpStateIdentity' : {
        'meta_info' : _MetaInfoClass('SaviDhcpStateIdentity',
            False, 
            [
            ],
            'ietf-savi-dhcpv6',
            'savi-dhcp-state',
            _yang_ns._namespaces['ietf-savi-dhcpv6'],
        'ydk.models.ietf.ietf_savi_dhcpv6'
        ),
    },
    'VerifyIdentity' : {
        'meta_info' : _MetaInfoClass('VerifyIdentity',
            False, 
            [
            ],
            'ietf-savi-dhcpv6',
            'verify',
            _yang_ns._namespaces['ietf-savi-dhcpv6'],
        'ydk.models.ietf.ietf_savi_dhcpv6'
        ),
    },
    'RecoveryIdentity' : {
        'meta_info' : _MetaInfoClass('RecoveryIdentity',
            False, 
            [
            ],
            'ietf-savi-dhcpv6',
            'recovery',
            _yang_ns._namespaces['ietf-savi-dhcpv6'],
        'ydk.models.ietf.ietf_savi_dhcpv6'
        ),
    },
    'Init_BindIdentity' : {
        'meta_info' : _MetaInfoClass('Init_BindIdentity',
            False, 
            [
            ],
            'ietf-savi-dhcpv6',
            'init_bind',
            _yang_ns._namespaces['ietf-savi-dhcpv6'],
        'ydk.models.ietf.ietf_savi_dhcpv6'
        ),
    },
    'DetectionIdentity' : {
        'meta_info' : _MetaInfoClass('DetectionIdentity',
            False, 
            [
            ],
            'ietf-savi-dhcpv6',
            'detection',
            _yang_ns._namespaces['ietf-savi-dhcpv6'],
        'ydk.models.ietf.ietf_savi_dhcpv6'
        ),
    },
    'BindIdentity' : {
        'meta_info' : _MetaInfoClass('BindIdentity',
            False, 
            [
            ],
            'ietf-savi-dhcpv6',
            'bind',
            _yang_ns._namespaces['ietf-savi-dhcpv6'],
        'ydk.models.ietf.ietf_savi_dhcpv6'
        ),
    },
    'No_BindIdentity' : {
        'meta_info' : _MetaInfoClass('No_BindIdentity',
            False, 
            [
            ],
            'ietf-savi-dhcpv6',
            'no_bind',
            _yang_ns._namespaces['ietf-savi-dhcpv6'],
        'ydk.models.ietf.ietf_savi_dhcpv6'
        ),
    },
}
