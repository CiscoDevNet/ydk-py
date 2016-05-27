


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'WredEnum' : _MetaInfoEnum('WredEnum', 'ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_pi_oper',
        {
            'wred-cos-cmd':'WRED_COS_CMD',
            'wred-dscp-cmd':'WRED_DSCP_CMD',
            'wred-precedence-cmd':'WRED_PRECEDENCE_CMD',
            'wred-discard-class-cmd':'WRED_DISCARD_CLASS_CMD',
            'wred-mpls-exp-cmd':'WRED_MPLS_EXP_CMD',
            'red-with-user-min-max':'RED_WITH_USER_MIN_MAX',
            'red-with-default-min-max':'RED_WITH_DEFAULT_MIN_MAX',
            'wred-dei-cmd':'WRED_DEI_CMD',
            'wred-ecn-cmd':'WRED_ECN_CMD',
            'wred-invalid-cmd':'WRED_INVALID_CMD',
        }, 'Cisco-IOS-XR-ncs5500-pi-oper', _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-pi-oper']),
    'CacStateEnum' : _MetaInfoEnum('CacStateEnum', 'ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_pi_oper',
        {
            'unknown':'UNKNOWN',
            'admit':'ADMIT',
            'redirect':'REDIRECT',
            'ubrl':'UBRL',
        }, 'Cisco-IOS-XR-ncs5500-pi-oper', _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-pi-oper']),
    'PolicyParamUnitEnum' : _MetaInfoEnum('PolicyParamUnitEnum', 'ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_pi_oper',
        {
            'policy-param-unit-invalid':'POLICY_PARAM_UNIT_INVALID',
            'policy-param-unit-bytes':'POLICY_PARAM_UNIT_BYTES',
            'policy-param-unit-kbytes':'POLICY_PARAM_UNIT_KBYTES',
            'policy-param-unit-mbytes':'POLICY_PARAM_UNIT_MBYTES',
            'policy-param-unit-gbytes':'POLICY_PARAM_UNIT_GBYTES',
            'policy-param-unit-bitsps':'POLICY_PARAM_UNIT_BITSPS',
            'policy-param-unit-kbitsps':'POLICY_PARAM_UNIT_KBITSPS',
            'policy-param-unit-mbitsps':'POLICY_PARAM_UNIT_MBITSPS',
            'policy-param-unit-gbitsps':'POLICY_PARAM_UNIT_GBITSPS',
            'policy-param-unit-cells-ps':'POLICY_PARAM_UNIT_CELLS_PS',
            'policy-param-unit-packets-ps':'POLICY_PARAM_UNIT_PACKETS_PS',
            'policy-param-unit-us':'POLICY_PARAM_UNIT_US',
            'policy-param-unit-ms':'POLICY_PARAM_UNIT_MS',
            'policy-param-unit-seconds':'POLICY_PARAM_UNIT_SECONDS',
            'policy-param-unit-packets':'POLICY_PARAM_UNIT_PACKETS',
            'policy-param-unit-cells':'POLICY_PARAM_UNIT_CELLS',
            'policy-param-unit-percent':'POLICY_PARAM_UNIT_PERCENT',
            'policy-param-unit-per-thousand':'POLICY_PARAM_UNIT_PER_THOUSAND',
            'policy-param-unit-per-million':'POLICY_PARAM_UNIT_PER_MILLION',
            'policy-param-unit-hz':'POLICY_PARAM_UNIT_HZ',
            'policy-param-unit-khz':'POLICY_PARAM_UNIT_KHZ',
            'policy-param-unit-mhz':'POLICY_PARAM_UNIT_MHZ',
            'policy-param-unit-ratio':'POLICY_PARAM_UNIT_RATIO',
            'policy-param-unit-max':'POLICY_PARAM_UNIT_MAX',
        }, 'Cisco-IOS-XR-ncs5500-pi-oper', _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-pi-oper']),
    'PolicyStateEnum' : _MetaInfoEnum('PolicyStateEnum', 'ydk.models.ncs5500.Cisco_IOS_XR_ncs5500_pi_oper',
        {
            'active':'ACTIVE',
            'suspended':'SUSPENDED',
        }, 'Cisco-IOS-XR-ncs5500-pi-oper', _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-pi-oper']),
}
