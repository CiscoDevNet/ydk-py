


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns

_meta_table = {
    'SaviSendStateIdentity' : {
        'meta_info' : _MetaInfoClass('SaviSendStateIdentity',
            False, 
            [
            ],
            'ietf-savi-send',
            'savi-send-state',
            _yang_ns._namespaces['ietf-savi-send'],
        'ydk.models.ietf.ietf_savi_send'
        ),
    },
    'TentativeNudIdentity' : {
        'meta_info' : _MetaInfoClass('TentativeNudIdentity',
            False, 
            [
            ],
            'ietf-savi-send',
            'tentative-nud',
            _yang_ns._namespaces['ietf-savi-send'],
        'ydk.models.ietf.ietf_savi_send'
        ),
    },
    'Testing_Vp_1Identity' : {
        'meta_info' : _MetaInfoClass('Testing_Vp_1Identity',
            False, 
            [
            ],
            'ietf-savi-send',
            'testing_vp_1',
            _yang_ns._namespaces['ietf-savi-send'],
        'ydk.models.ietf.ietf_savi_send'
        ),
    },
    'Testing_VpIdentity' : {
        'meta_info' : _MetaInfoClass('Testing_VpIdentity',
            False, 
            [
            ],
            'ietf-savi-send',
            'testing_vp',
            _yang_ns._namespaces['ietf-savi-send'],
        'ydk.models.ietf.ietf_savi_send'
        ),
    },
    'ValidIdentity' : {
        'meta_info' : _MetaInfoClass('ValidIdentity',
            False, 
            [
            ],
            'ietf-savi-send',
            'valid',
            _yang_ns._namespaces['ietf-savi-send'],
        'ydk.models.ietf.ietf_savi_send'
        ),
    },
    'TentativeDadIdentity' : {
        'meta_info' : _MetaInfoClass('TentativeDadIdentity',
            False, 
            [
            ],
            'ietf-savi-send',
            'tentative-dad',
            _yang_ns._namespaces['ietf-savi-send'],
        'ydk.models.ietf.ietf_savi_send'
        ),
    },
}
