


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'CpwOperStatus_Enum' : _MetaInfoEnum('CpwOperStatus_Enum', 'ydk.models.ietf.CISCO_IETF_PW_TC_MIB',
        {
            'up':'UP',
            'down':'DOWN',
            'testing':'TESTING',
            'unknown':'UNKNOWN',
            'dormant':'DORMANT',
            'notPresent':'NOTPRESENT',
            'lowerLayerDown':'LOWERLAYERDOWN',
        }, 'CISCO-IETF-PW-TC-MIB', _yang_ns._namespaces['CISCO-IETF-PW-TC-MIB']),
    'CpwVcType_Enum' : _MetaInfoEnum('CpwVcType_Enum', 'ydk.models.ietf.CISCO_IETF_PW_TC_MIB',
        {
            'other':'OTHER',
            'frameRelay':'FRAMERELAY',
            'atmAal5Vcc':'ATMAAL5VCC',
            'atmTransparent':'ATMTRANSPARENT',
            'ethernetVLAN':'ETHERNETVLAN',
            'ethernet':'ETHERNET',
            'hdlc':'HDLC',
            'ppp':'PPP',
            'cep':'CEP',
            'atmVccCell':'ATMVCCCELL',
            'atmVpcCell':'ATMVPCCELL',
            'ethernetVPLS':'ETHERNETVPLS',
            'e1Satop':'E1SATOP',
            't1Satop':'T1SATOP',
            'e3Satop':'E3SATOP',
            't3Satop':'T3SATOP',
            'basicCesPsn':'BASICCESPSN',
            'basicTdmIp':'BASICTDMIP',
            'tdmCasCesPsn':'TDMCASCESPSN',
            'tdmCasTdmIp':'TDMCASTDMIP',
        }, 'CISCO-IETF-PW-TC-MIB', _yang_ns._namespaces['CISCO-IETF-PW-TC-MIB']),
}
