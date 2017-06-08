


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns

_meta_table = {
    'AdminstatusEnum' : _MetaInfoEnum('AdminstatusEnum', 'ydk.models.ietf.ietf_nvo_common_types',
        {
            'active':'active',
            'inactive':'inactive',
            'partial':'partial',
        }, 'ietf-nvo-common-types', _yang_ns._namespaces['ietf-nvo-common-types']),
    'ConnectiondirectionEnum' : _MetaInfoEnum('ConnectiondirectionEnum', 'ydk.models.ietf.ietf_nvo_common_types',
        {
            'CD-UNI':'CD_UNI',
            'CD-BI':'CD_BI',
        }, 'ietf-nvo-common-types', _yang_ns._namespaces['ietf-nvo-common-types']),
    'TptypeEnum' : _MetaInfoEnum('TptypeEnum', 'ydk.models.ietf.ietf_nvo_common_types',
        {
            'nop':'nop',
            'PTP':'PTP',
            'CTP':'CTP',
            'TRUNK':'TRUNK',
            'LoopBack':'LoopBack',
            'TPPool':'TPPool',
        }, 'ietf-nvo-common-types', _yang_ns._namespaces['ietf-nvo-common-types']),
    'EthernetencaptypeEnum' : _MetaInfoEnum('EthernetencaptypeEnum', 'ydk.models.ietf.ietf_nvo_common_types',
        {
            'DEFAULT':'DEFAULT',
            'DOT1Q':'DOT1Q',
            'QINQ':'QINQ',
            'UNTAG':'UNTAG',
        }, 'ietf-nvo-common-types', _yang_ns._namespaces['ietf-nvo-common-types']),
    'QosprioritytypeEnum' : _MetaInfoEnum('QosprioritytypeEnum', 'ydk.models.ietf.ietf_nvo_common_types',
        {
            'nop':'nop',
            '802dot1p':'Y_802dot1p',
            'dscp':'dscp',
            'mplsExp':'mplsExp',
            'cos':'cos',
            'ipPrecedence':'ipPrecedence',
        }, 'ietf-nvo-common-types', _yang_ns._namespaces['ietf-nvo-common-types']),
    'EthernetactionEnum' : _MetaInfoEnum('EthernetactionEnum', 'ydk.models.ietf.ietf_nvo_common_types',
        {
            'nop':'nop',
            'UNTAG':'UNTAG',
            'STACKING':'STACKING',
        }, 'ietf-nvo-common-types', _yang_ns._namespaces['ietf-nvo-common-types']),
    'RouteprotocoltypeEnum' : _MetaInfoEnum('RouteprotocoltypeEnum', 'ydk.models.ietf.ietf_nvo_common_types',
        {
            'staticRouting':'staticRouting',
            'bgp':'bgp',
            'rip':'rip',
            'ospf':'ospf',
            'isis':'isis',
        }, 'ietf-nvo-common-types', _yang_ns._namespaces['ietf-nvo-common-types']),
    'OperstatusEnum' : _MetaInfoEnum('OperstatusEnum', 'ydk.models.ietf.ietf_nvo_common_types',
        {
            'up':'up',
            'down':'down',
            'degrade':'degrade',
        }, 'ietf-nvo-common-types', _yang_ns._namespaces['ietf-nvo-common-types']),
    'ColortypeEnum' : _MetaInfoEnum('ColortypeEnum', 'ydk.models.ietf.ietf_nvo_common_types',
        {
            'nop':'nop',
            'green':'green',
            'yellow':'yellow',
            'red':'red',
        }, 'ietf-nvo-common-types', _yang_ns._namespaces['ietf-nvo-common-types']),
    'ObjectdirectionEnum' : _MetaInfoEnum('ObjectdirectionEnum', 'ydk.models.ietf.ietf_nvo_common_types',
        {
            'IN':'IN',
            'OUT':'OUT',
            'BI-DIRECTION':'BI_DIRECTION',
        }, 'ietf-nvo-common-types', _yang_ns._namespaces['ietf-nvo-common-types']),
    'EdgepointroleEnum' : _MetaInfoEnum('EdgepointroleEnum', 'ydk.models.ietf.ietf_nvo_common_types',
        {
            'nop':'nop',
            'PE':'PE',
            'P':'P',
            'UNI':'UNI',
            'NNI':'NNI',
            'AsbTP':'AsbTP',
        }, 'ietf-nvo-common-types', _yang_ns._namespaces['ietf-nvo-common-types']),
    'FlowclassifiertypeEnum' : _MetaInfoEnum('FlowclassifiertypeEnum', 'ydk.models.ietf.ietf_nvo_common_types',
        {
            'nop':'nop',
            '802dot1p':'Y_802dot1p',
            'dscp':'dscp',
            'cos':'cos',
            'mpls-exp':'mpls_exp',
            'sourceIP':'sourceIP',
            'destinationIP':'destinationIP',
        }, 'ietf-nvo-common-types', _yang_ns._namespaces['ietf-nvo-common-types']),
    'ToponoderoleEnum' : _MetaInfoEnum('ToponoderoleEnum', 'ydk.models.ietf.ietf_nvo_common_types',
        {
            'other':'other',
            'hub':'hub',
            'spoke':'spoke',
        }, 'ietf-nvo-common-types', _yang_ns._namespaces['ietf-nvo-common-types']),
    'SyncstatusEnum' : _MetaInfoEnum('SyncstatusEnum', 'ydk.models.ietf.ietf_nvo_common_types',
        {
            'SYNC':'SYNC',
            'OUT-SYNC':'OUT_SYNC',
        }, 'ietf-nvo-common-types', _yang_ns._namespaces['ietf-nvo-common-types']),
    'DomainroleEnum' : _MetaInfoEnum('DomainroleEnum', 'ydk.models.ietf.ietf_nvo_common_types',
        {
            'nop':'nop',
            'external':'external',
            'internal':'internal',
            'asb':'asb',
        }, 'ietf-nvo-common-types', _yang_ns._namespaces['ietf-nvo-common-types']),
    'DiversitytypeEnum' : _MetaInfoEnum('DiversitytypeEnum', 'ydk.models.ietf.ietf_nvo_common_types',
        {
            'NOP':'NOP',
            'PE-DIFF':'PE_DIFF',
            'MAIN-TP-DIFF':'MAIN_TP_DIFF',
        }, 'ietf-nvo-common-types', _yang_ns._namespaces['ietf-nvo-common-types']),
    'LayerrateEnum' : _MetaInfoEnum('LayerrateEnum', 'ydk.models.ietf.ietf_nvo_common_types',
        {
            'LR_UNKNOW':'LR_UNKNOW',
            'LR_IP':'LR_IP',
            'LR_ETHERNET':'LR_ETHERNET',
            'LR_VXLAN':'LR_VXLAN',
        }, 'ietf-nvo-common-types', _yang_ns._namespaces['ietf-nvo-common-types']),
    'ObjecttypeEnum' : _MetaInfoEnum('ObjecttypeEnum', 'ydk.models.ietf.ietf_nvo_common_types',
        {
            'nop':'nop',
            'SEG-VPN':'SEG_VPN',
            'TP':'TP',
            'TPL':'TPL',
            'NE':'NE',
            'BUSINESSTYPE':'BUSINESSTYPE',
            'COMPOSED-VPN':'COMPOSED_VPN',
            'SUBNETWORK':'SUBNETWORK',
        }, 'ietf-nvo-common-types', _yang_ns._namespaces['ietf-nvo-common-types']),
    'TechnologyEnum' : _MetaInfoEnum('TechnologyEnum', 'ydk.models.ietf.ietf_nvo_common_types',
        {
            'mpls':'mpls',
            'rosen_multivpn':'rosen_multivpn',
            'ng_multivpn':'ng_multivpn',
            'vxlan_overlay_l3vpn':'vxlan_overlay_l3vpn',
            'eth_oversdh':'eth_oversdh',
        }, 'ietf-nvo-common-types', _yang_ns._namespaces['ietf-nvo-common-types']),
    'TopologyEnum' : _MetaInfoEnum('TopologyEnum', 'ydk.models.ietf.ietf_nvo_common_types',
        {
            'full-mesh':'full_mesh',
            'point_to_multipoint':'point_to_multipoint',
            'point_to_point':'point_to_point',
            'complex':'complex',
        }, 'ietf-nvo-common-types', _yang_ns._namespaces['ietf-nvo-common-types']),
}
