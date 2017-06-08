


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns

_meta_table = {
    'QosAttrubiteTypeEnumEnum' : _MetaInfoEnum('QosAttrubiteTypeEnumEnum', 'ydk.models.ietf.ietf_pmip_qos',
        {
            'Reserved':'Reserved',
            'Per-MN-Agg-Max-DL-Bit-Rate':'Per_MN_Agg_Max_DL_Bit_Rate',
            'Per-MN-Agg-Max-UL-Bit-Rate':'Per_MN_Agg_Max_UL_Bit_Rate',
            'Per-Session-Agg-Max-DL-Bit-Rate':'Per_Session_Agg_Max_DL_Bit_Rate',
            'Per-Session-Agg-Max-UL-Bit-Rate':'Per_Session_Agg_Max_UL_Bit_Rate',
            'Allocation-Retention-Priority':'Allocation_Retention_Priority',
            'Aggregate-Max-DL-Bit-Rate':'Aggregate_Max_DL_Bit_Rate',
            'Aggregate-Max-UL-Bit-Rate':'Aggregate_Max_UL_Bit_Rate',
            'Guaranteed-DL-Bit-Rate':'Guaranteed_DL_Bit_Rate',
            'Guaranteed-UL-Bit-Rate':'Guaranteed_UL_Bit_Rate',
            'QoS-Traffic-Selector':'QoS_Traffic_Selector',
            'QoS-Vendor-Specific-Attribute':'QoS_Vendor_Specific_Attribute',
        }, 'ietf-pmip-qos', _yang_ns._namespaces['ietf-pmip-qos']),
    'OperationalCodeEnum' : _MetaInfoEnum('OperationalCodeEnum', 'ydk.models.ietf.ietf_pmip_qos',
        {
            'RESPONSE':'RESPONSE',
            'ALLOCATE':'ALLOCATE',
            'DE-ALLOCATE':'DE_ALLOCATE',
            'MODIFY':'MODIFY',
            'QUERY':'QUERY',
            'NEGOTIATE':'NEGOTIATE',
        }, 'ietf-pmip-qos', _yang_ns._namespaces['ietf-pmip-qos']),
    'QosAttributeTypeIdentity' : {
        'meta_info' : _MetaInfoClass('QosAttributeTypeIdentity',
            False, 
            [
            ],
            'ietf-pmip-qos',
            'qos-attribute-type',
            _yang_ns._namespaces['ietf-pmip-qos'],
        'ydk.models.ietf.ietf_pmip_qos'
        ),
    },
    'QosTrafficSelectorTypeIdentity' : {
        'meta_info' : _MetaInfoClass('QosTrafficSelectorTypeIdentity',
            False, 
            [
            ],
            'ietf-pmip-qos',
            'QoS-Traffic-Selector-type',
            _yang_ns._namespaces['ietf-pmip-qos'],
        'ydk.models.ietf.ietf_pmip_qos'
        ),
    },
    'PerMnAggMaxUlBitRateTypeIdentity' : {
        'meta_info' : _MetaInfoClass('PerMnAggMaxUlBitRateTypeIdentity',
            False, 
            [
            ],
            'ietf-pmip-qos',
            'Per-MN-Agg-Max-UL-Bit-Rate-type',
            _yang_ns._namespaces['ietf-pmip-qos'],
        'ydk.models.ietf.ietf_pmip_qos'
        ),
    },
    'PerSessionAggMaxDlBitRateTypeIdentity' : {
        'meta_info' : _MetaInfoClass('PerSessionAggMaxDlBitRateTypeIdentity',
            False, 
            [
            ],
            'ietf-pmip-qos',
            'Per-Session-Agg-Max-DL-Bit-Rate-type',
            _yang_ns._namespaces['ietf-pmip-qos'],
        'ydk.models.ietf.ietf_pmip_qos'
        ),
    },
    'GuaranteedDlBitRateTypeIdentity' : {
        'meta_info' : _MetaInfoClass('GuaranteedDlBitRateTypeIdentity',
            False, 
            [
            ],
            'ietf-pmip-qos',
            'Guaranteed-DL-Bit-Rate-type',
            _yang_ns._namespaces['ietf-pmip-qos'],
        'ydk.models.ietf.ietf_pmip_qos'
        ),
    },
    'AggregateMaxUlBitRateTypeIdentity' : {
        'meta_info' : _MetaInfoClass('AggregateMaxUlBitRateTypeIdentity',
            False, 
            [
            ],
            'ietf-pmip-qos',
            'Aggregate-Max-UL-Bit-Rate-type',
            _yang_ns._namespaces['ietf-pmip-qos'],
        'ydk.models.ietf.ietf_pmip_qos'
        ),
    },
    'QosVendorSpecificAttributeTypeIdentity' : {
        'meta_info' : _MetaInfoClass('QosVendorSpecificAttributeTypeIdentity',
            False, 
            [
            ],
            'ietf-pmip-qos',
            'QoS-Vendor-Specific-Attribute-type',
            _yang_ns._namespaces['ietf-pmip-qos'],
        'ydk.models.ietf.ietf_pmip_qos'
        ),
    },
    'AggregateMaxDlBitRateTypeIdentity' : {
        'meta_info' : _MetaInfoClass('AggregateMaxDlBitRateTypeIdentity',
            False, 
            [
            ],
            'ietf-pmip-qos',
            'Aggregate-Max-DL-Bit-Rate-type',
            _yang_ns._namespaces['ietf-pmip-qos'],
        'ydk.models.ietf.ietf_pmip_qos'
        ),
    },
    'PerMnAggMaxDlBitRateTypeIdentity' : {
        'meta_info' : _MetaInfoClass('PerMnAggMaxDlBitRateTypeIdentity',
            False, 
            [
            ],
            'ietf-pmip-qos',
            'Per-MN-Agg-Max-DL-Bit-Rate-type',
            _yang_ns._namespaces['ietf-pmip-qos'],
        'ydk.models.ietf.ietf_pmip_qos'
        ),
    },
    'AllocationRetentionPriorityTypeIdentity' : {
        'meta_info' : _MetaInfoClass('AllocationRetentionPriorityTypeIdentity',
            False, 
            [
            ],
            'ietf-pmip-qos',
            'Allocation-Retention-Priority-type',
            _yang_ns._namespaces['ietf-pmip-qos'],
        'ydk.models.ietf.ietf_pmip_qos'
        ),
    },
    'PerSessionAggMaxUlBitRateTypeIdentity' : {
        'meta_info' : _MetaInfoClass('PerSessionAggMaxUlBitRateTypeIdentity',
            False, 
            [
            ],
            'ietf-pmip-qos',
            'Per-Session-Agg-Max-UL-Bit-Rate-type',
            _yang_ns._namespaces['ietf-pmip-qos'],
        'ydk.models.ietf.ietf_pmip_qos'
        ),
    },
    'GuaranteedUlBitRateTypeIdentity' : {
        'meta_info' : _MetaInfoClass('GuaranteedUlBitRateTypeIdentity',
            False, 
            [
            ],
            'ietf-pmip-qos',
            'Guaranteed-UL-Bit-Rate-type',
            _yang_ns._namespaces['ietf-pmip-qos'],
        'ydk.models.ietf.ietf_pmip_qos'
        ),
    },
}
