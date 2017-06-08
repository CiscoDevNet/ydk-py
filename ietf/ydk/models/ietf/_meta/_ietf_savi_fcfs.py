


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns

_meta_table = {
    'SaviFcfsStateIdentity' : {
        'meta_info' : _MetaInfoClass('SaviFcfsStateIdentity',
            False, 
            [
            ],
            'ietf-savi-fcfs',
            'savi-fcfs-state',
            _yang_ns._namespaces['ietf-savi-fcfs'],
        'ydk.models.ietf.ietf_savi_fcfs'
        ),
    },
    'Testing_VpIdentity' : {
        'meta_info' : _MetaInfoClass('Testing_VpIdentity',
            False, 
            [
            ],
            'ietf-savi-fcfs',
            'testing_vp',
            _yang_ns._namespaces['ietf-savi-fcfs'],
        'ydk.models.ietf.ietf_savi_fcfs'
        ),
    },
    'TentativeIdentity' : {
        'meta_info' : _MetaInfoClass('TentativeIdentity',
            False, 
            [
            ],
            'ietf-savi-fcfs',
            'tentative',
            _yang_ns._namespaces['ietf-savi-fcfs'],
        'ydk.models.ietf.ietf_savi_fcfs'
        ),
    },
    'Testing_VpLtIdentity' : {
        'meta_info' : _MetaInfoClass('Testing_VpLtIdentity',
            False, 
            [
            ],
            'ietf-savi-fcfs',
            'testing_vp-lt',
            _yang_ns._namespaces['ietf-savi-fcfs'],
        'ydk.models.ietf.ietf_savi_fcfs'
        ),
    },
    'ValidIdentity' : {
        'meta_info' : _MetaInfoClass('ValidIdentity',
            False, 
            [
            ],
            'ietf-savi-fcfs',
            'valid',
            _yang_ns._namespaces['ietf-savi-fcfs'],
        'ydk.models.ietf.ietf_savi_fcfs'
        ),
    },
}
