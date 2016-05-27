


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'AtmVpShapingEnum' : _MetaInfoEnum('AtmVpShapingEnum', 'ydk.models.atm.Cisco_IOS_XR_atm_common_datatypes',
        {
            'cbr':'CBR',
            'vbr-nrt':'VBR_NRT',
            'vbr-rt':'VBR_RT',
            'ubr':'UBR',
        }, 'Cisco-IOS-XR-atm-common-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-atm-common-datatypes']),
    'AtmPvcShapingEnum' : _MetaInfoEnum('AtmPvcShapingEnum', 'ydk.models.atm.Cisco_IOS_XR_atm_common_datatypes',
        {
            'cbr':'CBR',
            'vbr-nrt':'VBR_NRT',
            'vbr-rt':'VBR_RT',
            'ubr':'UBR',
        }, 'Cisco-IOS-XR-atm-common-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-atm-common-datatypes']),
    'AtmPvcEncapsulationEnum' : _MetaInfoEnum('AtmPvcEncapsulationEnum', 'ydk.models.atm.Cisco_IOS_XR_atm_common_datatypes',
        {
            'snap':'SNAP',
            'vc-mux':'VC_MUX',
            'nlpid':'NLPID',
            'aal0':'AAL0',
            'aal5':'AAL5',
        }, 'Cisco-IOS-XR-atm-common-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-atm-common-datatypes']),
    'AtmPvcDataEnum' : _MetaInfoEnum('AtmPvcDataEnum', 'ydk.models.atm.Cisco_IOS_XR_atm_common_datatypes',
        {
            'data':'DATA',
            'ilmi':'ILMI',
            'layer2':'LAYER2',
        }, 'Cisco-IOS-XR-atm-common-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-atm-common-datatypes']),
}
