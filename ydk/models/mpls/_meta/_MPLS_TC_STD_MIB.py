


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'MplsLabelDistributionMethod_Enum' : _MetaInfoEnum('MplsLabelDistributionMethod_Enum', 'ydk.models.mpls.MPLS_TC_STD_MIB',
        {
            'downstreamOnDemand':'DOWNSTREAMONDEMAND',
            'downstreamUnsolicited':'DOWNSTREAMUNSOLICITED',
        }, 'MPLS-TC-STD-MIB', _yang_ns._namespaces['MPLS-TC-STD-MIB']),
    'MplsRetentionMode_Enum' : _MetaInfoEnum('MplsRetentionMode_Enum', 'ydk.models.mpls.MPLS_TC_STD_MIB',
        {
            'conservative':'CONSERVATIVE',
            'liberal':'LIBERAL',
        }, 'MPLS-TC-STD-MIB', _yang_ns._namespaces['MPLS-TC-STD-MIB']),
    'MplsLdpLabelType_Enum' : _MetaInfoEnum('MplsLdpLabelType_Enum', 'ydk.models.mpls.MPLS_TC_STD_MIB',
        {
            'generic':'GENERIC',
            'atm':'ATM',
            'frameRelay':'FRAMERELAY',
        }, 'MPLS-TC-STD-MIB', _yang_ns._namespaces['MPLS-TC-STD-MIB']),
    'TeHopAddressType_Enum' : _MetaInfoEnum('TeHopAddressType_Enum', 'ydk.models.mpls.MPLS_TC_STD_MIB',
        {
            'unknown':'UNKNOWN',
            'ipv4':'IPV4',
            'ipv6':'IPV6',
            'asnumber':'ASNUMBER',
            'unnum':'UNNUM',
            'lspid':'LSPID',
        }, 'MPLS-TC-STD-MIB', _yang_ns._namespaces['MPLS-TC-STD-MIB']),
    'MplsLspType_Enum' : _MetaInfoEnum('MplsLspType_Enum', 'ydk.models.mpls.MPLS_TC_STD_MIB',
        {
            'unknown':'UNKNOWN',
            'terminatingLsp':'TERMINATINGLSP',
            'originatingLsp':'ORIGINATINGLSP',
            'crossConnectingLsp':'CROSSCONNECTINGLSP',
        }, 'MPLS-TC-STD-MIB', _yang_ns._namespaces['MPLS-TC-STD-MIB']),
    'MplsOwner_Enum' : _MetaInfoEnum('MplsOwner_Enum', 'ydk.models.mpls.MPLS_TC_STD_MIB',
        {
            'unknown':'UNKNOWN',
            'other':'OTHER',
            'snmp':'SNMP',
            'ldp':'LDP',
            'crldp':'CRLDP',
            'rsvpTe':'RSVPTE',
            'policyAgent':'POLICYAGENT',
        }, 'MPLS-TC-STD-MIB', _yang_ns._namespaces['MPLS-TC-STD-MIB']),
}
