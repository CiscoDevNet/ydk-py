


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'AtmPvcEncapsulationEnum' : _MetaInfoEnum('AtmPvcEncapsulationEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_common_datatypes',
        {
            'snap':'snap',
            'vc-mux':'vc_mux',
            'nlpid':'nlpid',
            'aal0':'aal0',
            'aal5':'aal5',
        }, 'Cisco-IOS-XR-atm-common-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-atm-common-datatypes']),
    'AtmPvcShapingEnum' : _MetaInfoEnum('AtmPvcShapingEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_common_datatypes',
        {
            'cbr':'cbr',
            'vbr-nrt':'vbr_nrt',
            'vbr-rt':'vbr_rt',
            'ubr':'ubr',
        }, 'Cisco-IOS-XR-atm-common-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-atm-common-datatypes']),
    'AtmVpShapingEnum' : _MetaInfoEnum('AtmVpShapingEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_common_datatypes',
        {
            'cbr':'cbr',
            'vbr-nrt':'vbr_nrt',
            'vbr-rt':'vbr_rt',
            'ubr':'ubr',
        }, 'Cisco-IOS-XR-atm-common-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-atm-common-datatypes']),
    'AtmPvcDataEnum' : _MetaInfoEnum('AtmPvcDataEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_atm_common_datatypes',
        {
            'data':'data',
            'ilmi':'ilmi',
            'layer2':'layer2',
        }, 'Cisco-IOS-XR-atm-common-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-atm-common-datatypes']),
}
