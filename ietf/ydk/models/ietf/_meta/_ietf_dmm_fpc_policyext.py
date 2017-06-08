


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns

_meta_table = {
    'ServiceFunctionIdentity' : {
        'meta_info' : _MetaInfoClass('ServiceFunctionIdentity',
            False, 
            [
            ],
            'ietf-dmm-fpc-policyext',
            'service-function',
            _yang_ns._namespaces['ietf-dmm-fpc-policyext'],
        'ydk.models.ietf.ietf_dmm_fpc_policyext'
        ),
    },
    'CopyForwardIdentity' : {
        'meta_info' : _MetaInfoClass('CopyForwardIdentity',
            False, 
            [
            ],
            'ietf-dmm-fpc-policyext',
            'copy-forward',
            _yang_ns._namespaces['ietf-dmm-fpc-policyext'],
        'ydk.models.ietf.ietf_dmm_fpc_policyext'
        ),
    },
    'NatServiceIdentity' : {
        'meta_info' : _MetaInfoClass('NatServiceIdentity',
            False, 
            [
            ],
            'ietf-dmm-fpc-policyext',
            'nat-service',
            _yang_ns._namespaces['ietf-dmm-fpc-policyext'],
        'ydk.models.ietf.ietf_dmm_fpc_policyext'
        ),
    },
    'NaptServiceIdentity' : {
        'meta_info' : _MetaInfoClass('NaptServiceIdentity',
            False, 
            [
            ],
            'ietf-dmm-fpc-policyext',
            'napt-service',
            _yang_ns._namespaces['ietf-dmm-fpc-policyext'],
        'ydk.models.ietf.ietf_dmm_fpc_policyext'
        ),
    },
}
