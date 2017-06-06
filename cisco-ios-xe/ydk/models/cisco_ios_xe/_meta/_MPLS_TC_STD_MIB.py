


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'MplsretentionmodeEnum' : _MetaInfoEnum('MplsretentionmodeEnum', 'ydk.models.cisco_ios_xe.MPLS_TC_STD_MIB',
        {
            'conservative':'conservative',
            'liberal':'liberal',
        }, 'MPLS-TC-STD-MIB', _yang_ns._namespaces['MPLS-TC-STD-MIB']),
    'TehopaddresstypeEnum' : _MetaInfoEnum('TehopaddresstypeEnum', 'ydk.models.cisco_ios_xe.MPLS_TC_STD_MIB',
        {
            'unknown':'unknown',
            'ipv4':'ipv4',
            'ipv6':'ipv6',
            'asnumber':'asnumber',
            'unnum':'unnum',
            'lspid':'lspid',
        }, 'MPLS-TC-STD-MIB', _yang_ns._namespaces['MPLS-TC-STD-MIB']),
    'MplsldplabeltypeEnum' : _MetaInfoEnum('MplsldplabeltypeEnum', 'ydk.models.cisco_ios_xe.MPLS_TC_STD_MIB',
        {
            'generic':'generic',
            'atm':'atm',
            'frameRelay':'frameRelay',
        }, 'MPLS-TC-STD-MIB', _yang_ns._namespaces['MPLS-TC-STD-MIB']),
    'MplslsptypeEnum' : _MetaInfoEnum('MplslsptypeEnum', 'ydk.models.cisco_ios_xe.MPLS_TC_STD_MIB',
        {
            'unknown':'unknown',
            'terminatingLsp':'terminatingLsp',
            'originatingLsp':'originatingLsp',
            'crossConnectingLsp':'crossConnectingLsp',
        }, 'MPLS-TC-STD-MIB', _yang_ns._namespaces['MPLS-TC-STD-MIB']),
    'MplsownerEnum' : _MetaInfoEnum('MplsownerEnum', 'ydk.models.cisco_ios_xe.MPLS_TC_STD_MIB',
        {
            'unknown':'unknown',
            'other':'other',
            'snmp':'snmp',
            'ldp':'ldp',
            'crldp':'crldp',
            'rsvpTe':'rsvpTe',
            'policyAgent':'policyAgent',
        }, 'MPLS-TC-STD-MIB', _yang_ns._namespaces['MPLS-TC-STD-MIB']),
    'MplslabeldistributionmethodEnum' : _MetaInfoEnum('MplslabeldistributionmethodEnum', 'ydk.models.cisco_ios_xe.MPLS_TC_STD_MIB',
        {
            'downstreamOnDemand':'downstreamOnDemand',
            'downstreamUnsolicited':'downstreamUnsolicited',
        }, 'MPLS-TC-STD-MIB', _yang_ns._namespaces['MPLS-TC-STD-MIB']),
}
