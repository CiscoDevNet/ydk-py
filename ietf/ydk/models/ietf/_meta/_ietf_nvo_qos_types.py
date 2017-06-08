


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns

_meta_table = {
    'ClassifierdetailtypeEnum' : _MetaInfoEnum('ClassifierdetailtypeEnum', 'ydk.models.ietf.ietf_nvo_qos_types',
        {
            'nop':'nop',
            'ipPrefixList':'ipPrefixList',
        }, 'ietf-nvo-qos-types', _yang_ns._namespaces['ietf-nvo-qos-types']),
    'ClassifiertypeEnum' : _MetaInfoEnum('ClassifiertypeEnum', 'ydk.models.ietf.ietf_nvo_qos_types',
        {
            '802dot1p':'Y_802dot1p',
            'dscp':'dscp',
            'cos':'cos',
            'mpls-exp':'mpls_exp',
            'sourceIP':'sourceIP',
            'destinationIP':'destinationIP',
        }, 'ietf-nvo-qos-types', _yang_ns._namespaces['ietf-nvo-qos-types']),
    'RuletypeEnum' : _MetaInfoEnum('RuletypeEnum', 'ydk.models.ietf.ietf_nvo_qos_types',
        {
            '802dot1p':'Y_802dot1p',
            'dscp':'dscp',
            'cos':'cos',
            'mpls_exp':'mpls_exp',
            'source_ip':'source_ip',
            'destination_ip':'destination_ip',
        }, 'ietf-nvo-qos-types', _yang_ns._namespaces['ietf-nvo-qos-types']),
    'QosprioritytypeEnum' : _MetaInfoEnum('QosprioritytypeEnum', 'ydk.models.ietf.ietf_nvo_qos_types',
        {
            'nop':'nop',
            '802dot1p':'Y_802dot1p',
            'dscp':'dscp',
            'mplsExp':'mplsExp',
            'cos':'cos',
            'ipPrecedence':'ipPrecedence',
        }, 'ietf-nvo-qos-types', _yang_ns._namespaces['ietf-nvo-qos-types']),
    'FlowclassifiertypeEnum' : _MetaInfoEnum('FlowclassifiertypeEnum', 'ydk.models.ietf.ietf_nvo_qos_types',
        {
            'nop':'nop',
            'aluFlowClassifier':'aluFlowClassifier',
        }, 'ietf-nvo-qos-types', _yang_ns._namespaces['ietf-nvo-qos-types']),
    'DatakindEnum' : _MetaInfoEnum('DatakindEnum', 'ydk.models.ietf.ietf_nvo_qos_types',
        {
            'green':'green',
            'yellow':'yellow',
            'red':'red',
            'all':'all',
        }, 'ietf-nvo-qos-types', _yang_ns._namespaces['ietf-nvo-qos-types']),
    'QosconfigtypeEnum' : _MetaInfoEnum('QosconfigtypeEnum', 'ydk.models.ietf.ietf_nvo_qos_types',
        {
            'nop':'nop',
            'template':'template',
            'agile':'agile',
        }, 'ietf-nvo-qos-types', _yang_ns._namespaces['ietf-nvo-qos-types']),
    'QosdetailtypeEnum' : _MetaInfoEnum('QosdetailtypeEnum', 'ydk.models.ietf.ietf_nvo_qos_types',
        {
            'nop':'nop',
            'car':'car',
            'qosProfile':'qosProfile',
            'diffServDomain':'diffServDomain',
            'diffServ':'diffServ',
            'aluDiffServ':'aluDiffServ',
        }, 'ietf-nvo-qos-types', _yang_ns._namespaces['ietf-nvo-qos-types']),
    'RuleoperatortypeEnum' : _MetaInfoEnum('RuleoperatortypeEnum', 'ydk.models.ietf.ietf_nvo_qos_types',
        {
            'and':'and_',
            'or':'or_',
        }, 'ietf-nvo-qos-types', _yang_ns._namespaces['ietf-nvo-qos-types']),
    'OrchpermittypeEnum' : _MetaInfoEnum('OrchpermittypeEnum', 'ydk.models.ietf.ietf_nvo_qos_types',
        {
            'readUse':'readUse',
            'crud':'crud',
        }, 'ietf-nvo-qos-types', _yang_ns._namespaces['ietf-nvo-qos-types']),
    'ActiontypeEnum' : _MetaInfoEnum('ActiontypeEnum', 'ydk.models.ietf.ietf_nvo_qos_types',
        {
            'nop':'nop',
            'bandwidth':'bandwidth',
            'pass':'pass_',
            'discard':'discard',
            'remark':'remark',
            'redirect':'redirect',
            'recolor':'recolor',
            'addRt':'addRt',
        }, 'ietf-nvo-qos-types', _yang_ns._namespaces['ietf-nvo-qos-types']),
    'MatchmodetypeEnum' : _MetaInfoEnum('MatchmodetypeEnum', 'ydk.models.ietf.ietf_nvo_qos_types',
        {
            'nop':'nop',
            'match':'match',
            'unmatch':'unmatch',
        }, 'ietf-nvo-qos-types', _yang_ns._namespaces['ietf-nvo-qos-types']),
    'ProfiletypeEnum' : _MetaInfoEnum('ProfiletypeEnum', 'ydk.models.ietf.ietf_nvo_qos_types',
        {
            'profile':'profile',
        }, 'ietf-nvo-qos-types', _yang_ns._namespaces['ietf-nvo-qos-types']),
    'QosbehaviortypeEnum' : _MetaInfoEnum('QosbehaviortypeEnum', 'ydk.models.ietf.ietf_nvo_qos_types',
        {
            'qosCarBehavior':'qosCarBehavior',
            'qosServiceChainBehavior':'qosServiceChainBehavior',
        }, 'ietf-nvo-qos-types', _yang_ns._namespaces['ietf-nvo-qos-types']),
    'QosbehaviordirectiontypeEnum' : _MetaInfoEnum('QosbehaviordirectiontypeEnum', 'ydk.models.ietf.ietf_nvo_qos_types',
        {
            'upstream':'upstream',
            'downstream':'downstream',
            'bidirectional':'bidirectional',
        }, 'ietf-nvo-qos-types', _yang_ns._namespaces['ietf-nvo-qos-types']),
}
