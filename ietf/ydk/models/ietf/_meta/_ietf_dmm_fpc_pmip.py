


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns

_meta_table = {
    'FpcpQosIndexPmipIdentity' : {
        'meta_info' : _MetaInfoClass('FpcpQosIndexPmipIdentity',
            False, 
            [
            ],
            'ietf-dmm-fpc-pmip',
            'fpcp-qos-index-pmip',
            _yang_ns._namespaces['ietf-dmm-fpc-pmip'],
        'ydk.models.ietf.ietf_dmm_fpc_pmip'
        ),
    },
    'PmipTunnelTypeIdentity' : {
        'meta_info' : _MetaInfoClass('PmipTunnelTypeIdentity',
            False, 
            [
            ],
            'ietf-dmm-fpc-pmip',
            'pmip-tunnel-type',
            _yang_ns._namespaces['ietf-dmm-fpc-pmip'],
        'ydk.models.ietf.ietf_dmm_fpc_pmip'
        ),
    },
    'TrafficSelectorMip6Identity' : {
        'meta_info' : _MetaInfoClass('TrafficSelectorMip6Identity',
            False, 
            [
            ],
            'ietf-dmm-fpc-pmip',
            'traffic-selector-mip6',
            _yang_ns._namespaces['ietf-dmm-fpc-pmip'],
        'ydk.models.ietf.ietf_dmm_fpc_pmip'
        ),
    },
    'IetfPmipAccessTypeIdentity' : {
        'meta_info' : _MetaInfoClass('IetfPmipAccessTypeIdentity',
            False, 
            [
            ],
            'ietf-dmm-fpc-pmip',
            'ietf-pmip-access-type',
            _yang_ns._namespaces['ietf-dmm-fpc-pmip'],
        'ydk.models.ietf.ietf_dmm_fpc_pmip'
        ),
    },
    'IetfPmipIdentity' : {
        'meta_info' : _MetaInfoClass('IetfPmipIdentity',
            False, 
            [
            ],
            'ietf-dmm-fpc-pmip',
            'ietf-pmip',
            _yang_ns._namespaces['ietf-dmm-fpc-pmip'],
        'ydk.models.ietf.ietf_dmm_fpc_pmip'
        ),
    },
    'Grev2Identity' : {
        'meta_info' : _MetaInfoClass('Grev2Identity',
            False, 
            [
            ],
            'ietf-dmm-fpc-pmip',
            'grev2',
            _yang_ns._namespaces['ietf-dmm-fpc-pmip'],
        'ydk.models.ietf.ietf_dmm_fpc_pmip'
        ),
    },
    'Grev1Identity' : {
        'meta_info' : _MetaInfoClass('Grev1Identity',
            False, 
            [
            ],
            'ietf-dmm-fpc-pmip',
            'grev1',
            _yang_ns._namespaces['ietf-dmm-fpc-pmip'],
        'ydk.models.ietf.ietf_dmm_fpc_pmip'
        ),
    },
    'IpinipIdentity' : {
        'meta_info' : _MetaInfoClass('IpinipIdentity',
            False, 
            [
            ],
            'ietf-dmm-fpc-pmip',
            'ipinip',
            _yang_ns._namespaces['ietf-dmm-fpc-pmip'],
        'ydk.models.ietf.ietf_dmm_fpc_pmip'
        ),
    },
}
