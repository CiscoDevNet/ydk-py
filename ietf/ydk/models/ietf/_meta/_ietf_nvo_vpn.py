


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns

_meta_table = {
    'Nvovpnmgr.Composedvpns.Vpnbasicinfo' : {
        'meta_info' : _MetaInfoClass('Nvovpnmgr.Composedvpns.Vpnbasicinfo',
            False, 
            [
            _MetaInfoClassMember('adminStatus', REFERENCE_ENUM_CLASS, 'AdminstatusEnum' , 'ydk.models.ietf.ietf_nvo_common_types', 'AdminstatusEnum', 
                [], [], 
                '''                administrative status.
                ''',
                'adminstatus',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('serviceType', REFERENCE_ENUM_CLASS, 'ServicetypeEnum' , 'ydk.models.ietf.ietf_nvo_vpn_types', 'ServicetypeEnum', 
                [], [], 
                '''                current support for mpls l3vpn/vxlan/L2VPN
                overlay, others is reserved for future extensions.
                ''',
                'servicetype',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('technology', REFERENCE_ENUM_CLASS, 'VpntunneltypeEnum' , 'ydk.models.ietf.ietf_nvo_vpn_types', 'VpntunneltypeEnum', 
                [], [], 
                '''                mpls|vxlan overlay l3vpn|eth over sdh|nop
                ''',
                'technology',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('topology', REFERENCE_ENUM_CLASS, 'TopologyEnum' , 'ydk.models.ietf.ietf_nvo_common_types', 'TopologyEnum', 
                [], [], 
                '''                current support for full-mesh and
                point_to_multipoint(hub-spoke), others is reserved for
                future extensions.
                ''',
                'topology',
                'ietf-nvo-vpn', False),
            ],
            'ietf-nvo-vpn',
            'vpnBasicInfo',
            _yang_ns._namespaces['ietf-nvo-vpn'],
        'ydk.models.ietf.ietf_nvo_vpn'
        ),
    },
    'Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Vpnbasicinfo' : {
        'meta_info' : _MetaInfoClass('Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Vpnbasicinfo',
            False, 
            [
            _MetaInfoClassMember('adminStatus', REFERENCE_ENUM_CLASS, 'AdminstatusEnum' , 'ydk.models.ietf.ietf_nvo_common_types', 'AdminstatusEnum', 
                [], [], 
                '''                administrative status.
                ''',
                'adminstatus',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('serviceType', REFERENCE_ENUM_CLASS, 'ServicetypeEnum' , 'ydk.models.ietf.ietf_nvo_vpn_types', 'ServicetypeEnum', 
                [], [], 
                '''                current support for mpls l3vpn/vxlan/L2VPN
                overlay, others is reserved for future extensions.
                ''',
                'servicetype',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('technology', REFERENCE_ENUM_CLASS, 'VpntunneltypeEnum' , 'ydk.models.ietf.ietf_nvo_vpn_types', 'VpntunneltypeEnum', 
                [], [], 
                '''                mpls|vxlan overlay l3vpn|eth over sdh|nop
                ''',
                'technology',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('topology', REFERENCE_ENUM_CLASS, 'TopologyEnum' , 'ydk.models.ietf.ietf_nvo_common_types', 'TopologyEnum', 
                [], [], 
                '''                current support for full-mesh and
                point_to_multipoint(hub-spoke), others is reserved for
                future extensions.
                ''',
                'topology',
                'ietf-nvo-vpn', False),
            ],
            'ietf-nvo-vpn',
            'vpnBasicInfo',
            _yang_ns._namespaces['ietf-nvo-vpn'],
        'ydk.models.ietf.ietf_nvo_vpn'
        ),
    },
    'Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Tpbasicinfo.Typespeclist.Ethernetspec.Qinqvlan' : {
        'meta_info' : _MetaInfoClass('Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Tpbasicinfo.Typespeclist.Ethernetspec.Qinqvlan',
            False, 
            [
            _MetaInfoClassMember('cvlanList', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                cvlanList
                ''',
                'cvlanlist',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('svlanList', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                svlanList
                ''',
                'svlanlist',
                'ietf-nvo-vpn', False),
            ],
            'ietf-nvo-vpn',
            'qinqVlan',
            _yang_ns._namespaces['ietf-nvo-vpn'],
        'ydk.models.ietf.ietf_nvo_vpn'
        ),
    },
    'Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Tpbasicinfo.Typespeclist.Ethernetspec.Dot1Q' : {
        'meta_info' : _MetaInfoClass('Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Tpbasicinfo.Typespeclist.Ethernetspec.Dot1Q',
            False, 
            [
            _MetaInfoClassMember('dot1qVlanList', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                dot1qVlanList
                ''',
                'dot1qvlanlist',
                'ietf-nvo-vpn', False),
            ],
            'ietf-nvo-vpn',
            'dot1q',
            _yang_ns._namespaces['ietf-nvo-vpn'],
        'ydk.models.ietf.ietf_nvo_vpn'
        ),
    },
    'Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Tpbasicinfo.Typespeclist.Ethernetspec' : {
        'meta_info' : _MetaInfoClass('Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Tpbasicinfo.Typespeclist.Ethernetspec',
            False, 
            [
            _MetaInfoClassMember('accessType', REFERENCE_ENUM_CLASS, 'EthernetencaptypeEnum' , 'ydk.models.ietf.ietf_nvo_common_types', 'EthernetencaptypeEnum', 
                [], [], 
                '''                access frame type
                ''',
                'accesstype',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('actionValue', ATTRIBUTE, 'str' , None, None, 
                [(0, 100)], [], 
                '''                action value
                ''',
                'actionvalue',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('dot1q', REFERENCE_CLASS, 'Dot1Q' , 'ydk.models.ietf.ietf_nvo_vpn', 'Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Tpbasicinfo.Typespeclist.Ethernetspec.Dot1Q', 
                [], [], 
                '''                dot1q
                ''',
                'dot1q',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('qinqVlan', REFERENCE_CLASS, 'Qinqvlan' , 'ydk.models.ietf.ietf_nvo_vpn', 'Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Tpbasicinfo.Typespeclist.Ethernetspec.Qinqvlan', 
                [], [], 
                '''                qinqVlan
                ''',
                'qinqvlan',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('vlanAction', REFERENCE_ENUM_CLASS, 'EthernetactionEnum' , 'ydk.models.ietf.ietf_nvo_common_types', 'EthernetactionEnum', 
                [], [], 
                '''                Frame type that can be accepted. not needed
                now
                ''',
                'vlanaction',
                'ietf-nvo-vpn', False),
            ],
            'ietf-nvo-vpn',
            'ethernetSpec',
            _yang_ns._namespaces['ietf-nvo-vpn'],
        'ydk.models.ietf.ietf_nvo_vpn'
        ),
    },
    'Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Tpbasicinfo.Typespeclist.Ipspec' : {
        'meta_info' : _MetaInfoClass('Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Tpbasicinfo.Typespeclist.Ipspec',
            False, 
            [
            _MetaInfoClassMember('masterIp', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                master IP address
                ''',
                'masterip',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('mtu', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                mtu for ip layer,scope:46~9600
                ''',
                'mtu',
                'ietf-nvo-vpn', False),
            ],
            'ietf-nvo-vpn',
            'ipSpec',
            _yang_ns._namespaces['ietf-nvo-vpn'],
        'ydk.models.ietf.ietf_nvo_vpn'
        ),
    },
    'Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Tpbasicinfo.Typespeclist.Vxlanspec' : {
        'meta_info' : _MetaInfoClass('Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Tpbasicinfo.Typespeclist.Vxlanspec',
            False, 
            [
            _MetaInfoClassMember('vni', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                vni
                ''',
                'vni',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('vtepIP', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                vtep ip
                ''',
                'vtepip',
                'ietf-nvo-vpn', False),
            ],
            'ietf-nvo-vpn',
            'vxlanSpec',
            _yang_ns._namespaces['ietf-nvo-vpn'],
        'ydk.models.ietf.ietf_nvo_vpn'
        ),
    },
    'Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Tpbasicinfo.Typespeclist' : {
        'meta_info' : _MetaInfoClass('Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Tpbasicinfo.Typespeclist',
            False, 
            [
            _MetaInfoClassMember('layerRate', REFERENCE_ENUM_CLASS, 'LayerrateEnum' , 'ydk.models.ietf.ietf_nvo_common_types', 'LayerrateEnum', 
                [], [], 
                '''                layerRate
                ''',
                'layerrate',
                'ietf-nvo-vpn', True),
            _MetaInfoClassMember('ethernetSpec', REFERENCE_CLASS, 'Ethernetspec' , 'ydk.models.ietf.ietf_nvo_vpn', 'Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Tpbasicinfo.Typespeclist.Ethernetspec', 
                [], [], 
                '''                ethernetSpec
                ''',
                'ethernetspec',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('ipSpec', REFERENCE_CLASS, 'Ipspec' , 'ydk.models.ietf.ietf_nvo_vpn', 'Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Tpbasicinfo.Typespeclist.Ipspec', 
                [], [], 
                '''                ipSpec
                ''',
                'ipspec',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('vxlanSpec', REFERENCE_CLASS, 'Vxlanspec' , 'ydk.models.ietf.ietf_nvo_vpn', 'Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Tpbasicinfo.Typespeclist.Vxlanspec', 
                [], [], 
                '''                vxlanSpec
                ''',
                'vxlanspec',
                'ietf-nvo-vpn', False),
            ],
            'ietf-nvo-vpn',
            'typeSpecList',
            _yang_ns._namespaces['ietf-nvo-vpn'],
        'ydk.models.ietf.ietf_nvo_vpn'
        ),
    },
    'Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Tpbasicinfo.Tpqosnode.Intpcar' : {
        'meta_info' : _MetaInfoClass('Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Tpbasicinfo.Tpqosnode.Intpcar',
            False, 
            [
            _MetaInfoClassMember('index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                index
                ''',
                'index',
                'ietf-nvo-vpn', True),
            _MetaInfoClassMember('action', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                action
                ''',
                'action',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('actionType', REFERENCE_ENUM_CLASS, 'ActiontypeEnum' , 'ydk.models.ietf.ietf_nvo_qos_types', 'ActiontypeEnum', 
                [], [], 
                '''                actionType
                ''',
                'actiontype',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('dataKind', REFERENCE_ENUM_CLASS, 'DatakindEnum' , 'ydk.models.ietf.ietf_nvo_qos_types', 'DatakindEnum', 
                [], [], 
                '''                dataKind
                ''',
                'datakind',
                'ietf-nvo-vpn', False),
            ],
            'ietf-nvo-vpn',
            'inTpCar',
            _yang_ns._namespaces['ietf-nvo-vpn'],
        'ydk.models.ietf.ietf_nvo_vpn'
        ),
    },
    'Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Tpbasicinfo.Tpqosnode.Outtpcar' : {
        'meta_info' : _MetaInfoClass('Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Tpbasicinfo.Tpqosnode.Outtpcar',
            False, 
            [
            _MetaInfoClassMember('index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                index
                ''',
                'index',
                'ietf-nvo-vpn', True),
            _MetaInfoClassMember('action', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                action
                ''',
                'action',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('actionType', REFERENCE_ENUM_CLASS, 'ActiontypeEnum' , 'ydk.models.ietf.ietf_nvo_qos_types', 'ActiontypeEnum', 
                [], [], 
                '''                actionType
                ''',
                'actiontype',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('dataKind', REFERENCE_ENUM_CLASS, 'DatakindEnum' , 'ydk.models.ietf.ietf_nvo_qos_types', 'DatakindEnum', 
                [], [], 
                '''                dataKind
                ''',
                'datakind',
                'ietf-nvo-vpn', False),
            ],
            'ietf-nvo-vpn',
            'outTpCar',
            _yang_ns._namespaces['ietf-nvo-vpn'],
        'ydk.models.ietf.ietf_nvo_vpn'
        ),
    },
    'Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Tpbasicinfo.Tpqosnode' : {
        'meta_info' : _MetaInfoClass('Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Tpbasicinfo.Tpqosnode',
            False, 
            [
            _MetaInfoClassMember('inQosProfileId', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}'], 
                '''                inQosProfileId
                ''',
                'inqosprofileid',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('inTpCar', REFERENCE_LIST, 'Intpcar' , 'ydk.models.ietf.ietf_nvo_vpn', 'Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Tpbasicinfo.Tpqosnode.Intpcar', 
                [], [], 
                '''                inTpCar
                ''',
                'intpcar',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('outQosProfileId', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}'], 
                '''                outQosProfileId
                ''',
                'outqosprofileid',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('outTpCar', REFERENCE_LIST, 'Outtpcar' , 'ydk.models.ietf.ietf_nvo_vpn', 'Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Tpbasicinfo.Tpqosnode.Outtpcar', 
                [], [], 
                '''                outTpCar
                ''',
                'outtpcar',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('qosConfigType', REFERENCE_ENUM_CLASS, 'QosconfigtypeEnum' , 'ydk.models.ietf.ietf_nvo_qos_types', 'QosconfigtypeEnum', 
                [], [], 
                '''                qosConfigType
                ''',
                'qosconfigtype',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('qosDetailType', REFERENCE_ENUM_CLASS, 'QosdetailtypeEnum' , 'ydk.models.ietf.ietf_nvo_qos_types', 'QosdetailtypeEnum', 
                [], [], 
                '''                qosDetailType
                ''',
                'qosdetailtype',
                'ietf-nvo-vpn', False),
            ],
            'ietf-nvo-vpn',
            'tpQosNode',
            _yang_ns._namespaces['ietf-nvo-vpn'],
        'ydk.models.ietf.ietf_nvo_vpn'
        ),
    },
    'Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Tpbasicinfo.Flowservices.Flowservices_.Flowbehaviors' : {
        'meta_info' : _MetaInfoClass('Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Tpbasicinfo.Flowservices.Flowservices_.Flowbehaviors',
            False, 
            [
            _MetaInfoClassMember('index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                index
                ''',
                'index',
                'ietf-nvo-vpn', True),
            _MetaInfoClassMember('action', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                action
                ''',
                'action',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('actionType', REFERENCE_ENUM_CLASS, 'ActiontypeEnum' , 'ydk.models.ietf.ietf_nvo_qos_types', 'ActiontypeEnum', 
                [], [], 
                '''                actionType
                ''',
                'actiontype',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('dataKind', REFERENCE_ENUM_CLASS, 'DatakindEnum' , 'ydk.models.ietf.ietf_nvo_qos_types', 'DatakindEnum', 
                [], [], 
                '''                dataKind
                ''',
                'datakind',
                'ietf-nvo-vpn', False),
            ],
            'ietf-nvo-vpn',
            'flowBehaviors',
            _yang_ns._namespaces['ietf-nvo-vpn'],
        'ydk.models.ietf.ietf_nvo_vpn'
        ),
    },
    'Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Tpbasicinfo.Flowservices.Flowservices_' : {
        'meta_info' : _MetaInfoClass('Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Tpbasicinfo.Flowservices.Flowservices_',
            False, 
            [
            _MetaInfoClassMember('flowClassifierId', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}'], 
                '''                flowClassifierId
                ''',
                'flowclassifierid',
                'ietf-nvo-vpn', True),
            _MetaInfoClassMember('flowBehaviors', REFERENCE_LIST, 'Flowbehaviors' , 'ydk.models.ietf.ietf_nvo_vpn', 'Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Tpbasicinfo.Flowservices.Flowservices_.Flowbehaviors', 
                [], [], 
                '''                flowBehaviors
                ''',
                'flowbehaviors',
                'ietf-nvo-vpn', False),
            ],
            'ietf-nvo-vpn',
            'flowServices',
            _yang_ns._namespaces['ietf-nvo-vpn'],
        'ydk.models.ietf.ietf_nvo_vpn'
        ),
    },
    'Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Tpbasicinfo.Flowservices' : {
        'meta_info' : _MetaInfoClass('Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Tpbasicinfo.Flowservices',
            False, 
            [
            _MetaInfoClassMember('flowQosTemplateID', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}'], 
                '''                flowQosTemplateID
                ''',
                'flowqostemplateid',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('flowServices', REFERENCE_LIST, 'Flowservices_' , 'ydk.models.ietf.ietf_nvo_vpn', 'Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Tpbasicinfo.Flowservices.Flowservices_', 
                [], [], 
                '''                default in flow and behaviors
                ''',
                'flowservices',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('inFlowQosTemplateID', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}'], 
                '''                inFlowQosTemplateID
                ''',
                'inflowqostemplateid',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('outFlowQosTemplateID', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}'], 
                '''                outFlowQosTemplateID
                ''',
                'outflowqostemplateid',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('qosConfigType', REFERENCE_ENUM_CLASS, 'QosconfigtypeEnum' , 'ydk.models.ietf.ietf_nvo_qos_types', 'QosconfigtypeEnum', 
                [], [], 
                '''                qosConfigType
                ''',
                'qosconfigtype',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('qosDetailType', REFERENCE_ENUM_CLASS, 'QosdetailtypeEnum' , 'ydk.models.ietf.ietf_nvo_qos_types', 'QosdetailtypeEnum', 
                [], [], 
                '''                qosDetailType
                ''',
                'qosdetailtype',
                'ietf-nvo-vpn', False),
            ],
            'ietf-nvo-vpn',
            'flowServices',
            _yang_ns._namespaces['ietf-nvo-vpn'],
        'ydk.models.ietf.ietf_nvo_vpn'
        ),
    },
    'Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Tpbasicinfo.Addtionalinfo' : {
        'meta_info' : _MetaInfoClass('Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Tpbasicinfo.Addtionalinfo',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                string name 
                ''',
                'name',
                'ietf-nvo-vpn', True),
            _MetaInfoClassMember('value', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                string value
                ''',
                'value',
                'ietf-nvo-vpn', False),
            ],
            'ietf-nvo-vpn',
            'addtionalInfo',
            _yang_ns._namespaces['ietf-nvo-vpn'],
        'ydk.models.ietf.ietf_nvo_vpn'
        ),
    },
    'Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Tpbasicinfo' : {
        'meta_info' : _MetaInfoClass('Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Tpbasicinfo',
            False, 
            [
            _MetaInfoClassMember('addtionalInfo', REFERENCE_LIST, 'Addtionalinfo' , 'ydk.models.ietf.ietf_nvo_vpn', 'Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Tpbasicinfo.Addtionalinfo', 
                [], [], 
                '''                addtionalInfo
                ''',
                'addtionalinfo',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('adminStatus', REFERENCE_ENUM_CLASS, 'AdminstatusEnum' , 'ydk.models.ietf.ietf_nvo_common_types', 'AdminstatusEnum', 
                [], [], 
                '''                administrative status.
                ''',
                'adminstatus',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('edgePointRole', REFERENCE_ENUM_CLASS, 'EdgepointroleEnum' , 'ydk.models.ietf.ietf_nvo_common_types', 'EdgepointroleEnum', 
                [], [], 
                '''                edge role for TP, for example:UNI/NNI 
                ''',
                'edgepointrole',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('flowServices', REFERENCE_CLASS, 'Flowservices' , 'ydk.models.ietf.ietf_nvo_vpn', 'Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Tpbasicinfo.Flowservices', 
                [], [], 
                '''                flow services in one TP
                ''',
                'flowservices',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('topologyRole', REFERENCE_ENUM_CLASS, 'ToponoderoleEnum' , 'ydk.models.ietf.ietf_nvo_common_types', 'ToponoderoleEnum', 
                [], [], 
                '''                hub/spoke role, etc
                ''',
                'topologyrole',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('tpQosNode', REFERENCE_CLASS, 'Tpqosnode' , 'ydk.models.ietf.ietf_nvo_vpn', 'Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Tpbasicinfo.Tpqosnode', 
                [], [], 
                '''                tpQosNode
                ''',
                'tpqosnode',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('Type', REFERENCE_ENUM_CLASS, 'TptypeEnum' , 'ydk.models.ietf.ietf_nvo_common_types', 'TptypeEnum', 
                [], [], 
                '''                Type
                ''',
                'type',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('typeSpecList', REFERENCE_LIST, 'Typespeclist' , 'ydk.models.ietf.ietf_nvo_vpn', 'Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Tpbasicinfo.Typespeclist', 
                [], [], 
                '''                typeSpecList
                ''',
                'typespeclist',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('workingLayer', REFERENCE_ENUM_CLASS, 'LayerrateEnum' , 'ydk.models.ietf.ietf_nvo_common_types', 'LayerrateEnum', 
                [], [], 
                '''                working layer
                ''',
                'workinglayer',
                'ietf-nvo-vpn', False),
            ],
            'ietf-nvo-vpn',
            'tpBasicInfo',
            _yang_ns._namespaces['ietf-nvo-vpn'],
        'ydk.models.ietf.ietf_nvo_vpn'
        ),
    },
    'Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Peercetp' : {
        'meta_info' : _MetaInfoClass('Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Peercetp',
            False, 
            [
            _MetaInfoClassMember('ceDirectNeID', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}'], 
                '''                direction connected NE ID, only valid in
                asbr 
                ''',
                'cedirectneid',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('ceDirectTPID', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}'], 
                '''                ce Direct TP id, only valid in asbr
                ''',
                'cedirecttpid',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('ceID', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}'], 
                '''                Site router ID
                ''',
                'ceid',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('ceIfmasterIp', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ceIfmasterIp
                ''',
                'ceifmasterip',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('location', ATTRIBUTE, 'str' , None, None, 
                [(0, 400)], [], 
                '''                CE device location 
                ''',
                'location',
                'ietf-nvo-vpn', False),
            ],
            'ietf-nvo-vpn',
            'peerCeTp',
            _yang_ns._namespaces['ietf-nvo-vpn'],
        'ydk.models.ietf.ietf_nvo_vpn'
        ),
    },
    'Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Routeprotocolspec.Staticrouteitems' : {
        'meta_info' : _MetaInfoClass('Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Routeprotocolspec.Staticrouteitems',
            False, 
            [
            _MetaInfoClassMember('index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                static item index
                ''',
                'index',
                'ietf-nvo-vpn', True),
            _MetaInfoClassMember('destinationCidr', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                destination ip cidr. 
                ''',
                'destinationcidr',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('egressTP', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}'], 
                '''                egress tp
                ''',
                'egresstp',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('nextHopIp', ATTRIBUTE, 'str' , None, None, 
                [(0, 200)], [], 
                '''                nextHopIp
                ''',
                'nexthopip',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('routePreference', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                route priority. Ordinary, work route have
                higher priority.
                ''',
                'routepreference',
                'ietf-nvo-vpn', False),
            ],
            'ietf-nvo-vpn',
            'staticRouteItems',
            _yang_ns._namespaces['ietf-nvo-vpn'],
        'ydk.models.ietf.ietf_nvo_vpn'
        ),
    },
    'Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Routeprotocolspec.Bgpprotocols' : {
        'meta_info' : _MetaInfoClass('Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Routeprotocolspec.Bgpprotocols',
            False, 
            [
            _MetaInfoClassMember('index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                index of BGP protocol item
                ''',
                'index',
                'ietf-nvo-vpn', True),
            _MetaInfoClassMember('bgpMaxPrefix', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                
                ''',
                'bgpmaxprefix',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('bgpMaxPrefixAlarm', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                alarm threshold of BGP rout
                ''',
                'bgpmaxprefixalarm',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('peerAsNumber', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                
                ''',
                'peerasnumber',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('peerIp', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                peerIp
                ''',
                'peerip',
                'ietf-nvo-vpn', False),
            ],
            'ietf-nvo-vpn',
            'bgpProtocols',
            _yang_ns._namespaces['ietf-nvo-vpn'],
        'ydk.models.ietf.ietf_nvo_vpn'
        ),
    },
    'Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Routeprotocolspec' : {
        'meta_info' : _MetaInfoClass('Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Routeprotocolspec',
            False, 
            [
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'RouteprotocoltypeEnum' , 'ydk.models.ietf.ietf_nvo_common_types', 'RouteprotocoltypeEnum', 
                [], [], 
                '''                Protocol type
                ''',
                'type',
                'ietf-nvo-vpn', True),
            _MetaInfoClassMember('bgpProtocols', REFERENCE_LIST, 'Bgpprotocols' , 'ydk.models.ietf.ietf_nvo_vpn', 'Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Routeprotocolspec.Bgpprotocols', 
                [], [], 
                '''                bgpProtocols
                ''',
                'bgpprotocols',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('staticRouteItems', REFERENCE_LIST, 'Staticrouteitems' , 'ydk.models.ietf.ietf_nvo_vpn', 'Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Routeprotocolspec.Staticrouteitems', 
                [], [], 
                '''                staticRouteItems
                ''',
                'staticrouteitems',
                'ietf-nvo-vpn', False),
            ],
            'ietf-nvo-vpn',
            'routeProtocolSpec',
            _yang_ns._namespaces['ietf-nvo-vpn'],
        'ydk.models.ietf.ietf_nvo_vpn'
        ),
    },
    'Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist' : {
        'meta_info' : _MetaInfoClass('Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist',
            False, 
            [
            _MetaInfoClassMember('id', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}'], 
                '''                yang:uuid-str for TP
                ''',
                'id',
                'ietf-nvo-vpn', True),
            _MetaInfoClassMember('containingMainTPID', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}'], 
                '''                uuid-str for main interface
                ''',
                'containingmaintpid',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [(0, 200)], [], 
                '''                description for this tp.
                ''',
                'description',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(0, 200)], [], 
                '''                Must abbey to name rule defined in system.
                Example FE0/0/1, GE1/2/1.1, Eth-Trunk1.1, etc
                ''',
                'name',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('neID', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}'], 
                '''                yang:uuid-str for NE 
                ''',
                'neid',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('operStatus', REFERENCE_ENUM_CLASS, 'OperstatusEnum' , 'ydk.models.ietf.ietf_nvo_common_types', 'OperstatusEnum', 
                [], [], 
                '''                Operational status.
                ''',
                'operstatus',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('peerCeTp', REFERENCE_CLASS, 'Peercetp' , 'ydk.models.ietf.ietf_nvo_vpn', 'Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Peercetp', 
                [], [], 
                '''                CE TP Information
                ''',
                'peercetp',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('routeProtocolSpec', REFERENCE_LIST, 'Routeprotocolspec' , 'ydk.models.ietf.ietf_nvo_vpn', 'Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Routeprotocolspec', 
                [], [], 
                '''                route protocol spec
                ''',
                'routeprotocolspec',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('tpBasicInfo', REFERENCE_CLASS, 'Tpbasicinfo' , 'ydk.models.ietf.ietf_nvo_vpn', 'Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Tpbasicinfo', 
                [], [], 
                '''                Tp non-instance basic info
                ''',
                'tpbasicinfo',
                'ietf-nvo-vpn', False),
            ],
            'ietf-nvo-vpn',
            'accessPointList',
            _yang_ns._namespaces['ietf-nvo-vpn'],
        'ydk.models.ietf.ietf_nvo_vpn'
        ),
    },
    'Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn' : {
        'meta_info' : _MetaInfoClass('Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn',
            False, 
            [
            _MetaInfoClassMember('accessPointList', REFERENCE_LIST, 'Accesspointlist' , 'ydk.models.ietf.ietf_nvo_vpn', 'Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist', 
                [], [], 
                '''                TP list of the access links which associated
                with CE and PE
                ''',
                'accesspointlist',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [(0, 200)], [], 
                '''                Detailed specification for the servcie.
                ''',
                'description',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('id', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}'], 
                '''                UUID-STR for VPN.
                ''',
                'id',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(0, 200)], [], 
                '''                Human-readable name for the service.
                ''',
                'name',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('operStatus', REFERENCE_ENUM_CLASS, 'OperstatusEnum' , 'ydk.models.ietf.ietf_nvo_common_types', 'OperstatusEnum', 
                [], [], 
                '''                Operational status.
                ''',
                'operstatus',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('syncStatus', REFERENCE_ENUM_CLASS, 'SyncstatusEnum' , 'ydk.models.ietf.ietf_nvo_common_types', 'SyncstatusEnum', 
                [], [], 
                '''                Sync status.
                ''',
                'syncstatus',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('vpnBasicInfo', REFERENCE_CLASS, 'Vpnbasicinfo' , 'ydk.models.ietf.ietf_nvo_vpn', 'Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Vpnbasicinfo', 
                [], [], 
                '''                vpn basic info
                ''',
                'vpnbasicinfo',
                'ietf-nvo-vpn', False),
            ],
            'ietf-nvo-vpn',
            'vpn',
            _yang_ns._namespaces['ietf-nvo-vpn'],
        'ydk.models.ietf.ietf_nvo_vpn'
        ),
    },
    'Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo' : {
        'meta_info' : _MetaInfoClass('Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo',
            False, 
            [
            _MetaInfoClassMember('vpn', REFERENCE_CLASS, 'Vpn' , 'ydk.models.ietf.ietf_nvo_vpn', 'Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn', 
                [], [], 
                '''                vpn.
                ''',
                'vpn',
                'ietf-nvo-vpn', False),
            ],
            'ietf-nvo-vpn',
            'vpnInfo',
            _yang_ns._namespaces['ietf-nvo-vpn'],
        'ydk.models.ietf.ietf_nvo_vpn'
        ),
    },
    'Nvovpnmgr.Composedvpns.Segvpnlist' : {
        'meta_info' : _MetaInfoClass('Nvovpnmgr.Composedvpns.Segvpnlist',
            False, 
            [
            _MetaInfoClassMember('index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                index of segment VPN in a composed VPN.
                ''',
                'index',
                'ietf-nvo-vpn', True),
            _MetaInfoClassMember('vpnInfo', REFERENCE_CLASS, 'Vpninfo' , 'ydk.models.ietf.ietf_nvo_vpn', 'Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo', 
                [], [], 
                '''                vpn information
                ''',
                'vpninfo',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('vpnRole', REFERENCE_ENUM_CLASS, 'ProtectionroleEnum' , 'ydk.models.ietf.ietf_nvo_vpn_types', 'ProtectionroleEnum', 
                [], [], 
                '''                value: nop|vpn
                ''',
                'vpnrole',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('vpnType', ATTRIBUTE, 'str' , None, None, 
                [(0, 30)], [], 
                '''                value: nop/wanVpn
                ''',
                'vpntype',
                'ietf-nvo-vpn', False),
            ],
            'ietf-nvo-vpn',
            'segVpnList',
            _yang_ns._namespaces['ietf-nvo-vpn'],
        'ydk.models.ietf.ietf_nvo_vpn'
        ),
    },
    'Nvovpnmgr.Composedvpns.Accesspointlist.Tpbasicinfo.Typespeclist.Ethernetspec.Qinqvlan' : {
        'meta_info' : _MetaInfoClass('Nvovpnmgr.Composedvpns.Accesspointlist.Tpbasicinfo.Typespeclist.Ethernetspec.Qinqvlan',
            False, 
            [
            _MetaInfoClassMember('cvlanList', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                cvlanList
                ''',
                'cvlanlist',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('svlanList', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                svlanList
                ''',
                'svlanlist',
                'ietf-nvo-vpn', False),
            ],
            'ietf-nvo-vpn',
            'qinqVlan',
            _yang_ns._namespaces['ietf-nvo-vpn'],
        'ydk.models.ietf.ietf_nvo_vpn'
        ),
    },
    'Nvovpnmgr.Composedvpns.Accesspointlist.Tpbasicinfo.Typespeclist.Ethernetspec.Dot1Q' : {
        'meta_info' : _MetaInfoClass('Nvovpnmgr.Composedvpns.Accesspointlist.Tpbasicinfo.Typespeclist.Ethernetspec.Dot1Q',
            False, 
            [
            _MetaInfoClassMember('dot1qVlanList', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                dot1qVlanList
                ''',
                'dot1qvlanlist',
                'ietf-nvo-vpn', False),
            ],
            'ietf-nvo-vpn',
            'dot1q',
            _yang_ns._namespaces['ietf-nvo-vpn'],
        'ydk.models.ietf.ietf_nvo_vpn'
        ),
    },
    'Nvovpnmgr.Composedvpns.Accesspointlist.Tpbasicinfo.Typespeclist.Ethernetspec' : {
        'meta_info' : _MetaInfoClass('Nvovpnmgr.Composedvpns.Accesspointlist.Tpbasicinfo.Typespeclist.Ethernetspec',
            False, 
            [
            _MetaInfoClassMember('accessType', REFERENCE_ENUM_CLASS, 'EthernetencaptypeEnum' , 'ydk.models.ietf.ietf_nvo_common_types', 'EthernetencaptypeEnum', 
                [], [], 
                '''                access frame type
                ''',
                'accesstype',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('actionValue', ATTRIBUTE, 'str' , None, None, 
                [(0, 100)], [], 
                '''                action value
                ''',
                'actionvalue',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('dot1q', REFERENCE_CLASS, 'Dot1Q' , 'ydk.models.ietf.ietf_nvo_vpn', 'Nvovpnmgr.Composedvpns.Accesspointlist.Tpbasicinfo.Typespeclist.Ethernetspec.Dot1Q', 
                [], [], 
                '''                dot1q
                ''',
                'dot1q',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('qinqVlan', REFERENCE_CLASS, 'Qinqvlan' , 'ydk.models.ietf.ietf_nvo_vpn', 'Nvovpnmgr.Composedvpns.Accesspointlist.Tpbasicinfo.Typespeclist.Ethernetspec.Qinqvlan', 
                [], [], 
                '''                qinqVlan
                ''',
                'qinqvlan',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('vlanAction', REFERENCE_ENUM_CLASS, 'EthernetactionEnum' , 'ydk.models.ietf.ietf_nvo_common_types', 'EthernetactionEnum', 
                [], [], 
                '''                Frame type that can be accepted. not needed
                now
                ''',
                'vlanaction',
                'ietf-nvo-vpn', False),
            ],
            'ietf-nvo-vpn',
            'ethernetSpec',
            _yang_ns._namespaces['ietf-nvo-vpn'],
        'ydk.models.ietf.ietf_nvo_vpn'
        ),
    },
    'Nvovpnmgr.Composedvpns.Accesspointlist.Tpbasicinfo.Typespeclist.Ipspec' : {
        'meta_info' : _MetaInfoClass('Nvovpnmgr.Composedvpns.Accesspointlist.Tpbasicinfo.Typespeclist.Ipspec',
            False, 
            [
            _MetaInfoClassMember('masterIp', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                master IP address
                ''',
                'masterip',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('mtu', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                mtu for ip layer,scope:46~9600
                ''',
                'mtu',
                'ietf-nvo-vpn', False),
            ],
            'ietf-nvo-vpn',
            'ipSpec',
            _yang_ns._namespaces['ietf-nvo-vpn'],
        'ydk.models.ietf.ietf_nvo_vpn'
        ),
    },
    'Nvovpnmgr.Composedvpns.Accesspointlist.Tpbasicinfo.Typespeclist.Vxlanspec' : {
        'meta_info' : _MetaInfoClass('Nvovpnmgr.Composedvpns.Accesspointlist.Tpbasicinfo.Typespeclist.Vxlanspec',
            False, 
            [
            _MetaInfoClassMember('vni', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                vni
                ''',
                'vni',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('vtepIP', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                vtep ip
                ''',
                'vtepip',
                'ietf-nvo-vpn', False),
            ],
            'ietf-nvo-vpn',
            'vxlanSpec',
            _yang_ns._namespaces['ietf-nvo-vpn'],
        'ydk.models.ietf.ietf_nvo_vpn'
        ),
    },
    'Nvovpnmgr.Composedvpns.Accesspointlist.Tpbasicinfo.Typespeclist' : {
        'meta_info' : _MetaInfoClass('Nvovpnmgr.Composedvpns.Accesspointlist.Tpbasicinfo.Typespeclist',
            False, 
            [
            _MetaInfoClassMember('layerRate', REFERENCE_ENUM_CLASS, 'LayerrateEnum' , 'ydk.models.ietf.ietf_nvo_common_types', 'LayerrateEnum', 
                [], [], 
                '''                layerRate
                ''',
                'layerrate',
                'ietf-nvo-vpn', True),
            _MetaInfoClassMember('ethernetSpec', REFERENCE_CLASS, 'Ethernetspec' , 'ydk.models.ietf.ietf_nvo_vpn', 'Nvovpnmgr.Composedvpns.Accesspointlist.Tpbasicinfo.Typespeclist.Ethernetspec', 
                [], [], 
                '''                ethernetSpec
                ''',
                'ethernetspec',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('ipSpec', REFERENCE_CLASS, 'Ipspec' , 'ydk.models.ietf.ietf_nvo_vpn', 'Nvovpnmgr.Composedvpns.Accesspointlist.Tpbasicinfo.Typespeclist.Ipspec', 
                [], [], 
                '''                ipSpec
                ''',
                'ipspec',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('vxlanSpec', REFERENCE_CLASS, 'Vxlanspec' , 'ydk.models.ietf.ietf_nvo_vpn', 'Nvovpnmgr.Composedvpns.Accesspointlist.Tpbasicinfo.Typespeclist.Vxlanspec', 
                [], [], 
                '''                vxlanSpec
                ''',
                'vxlanspec',
                'ietf-nvo-vpn', False),
            ],
            'ietf-nvo-vpn',
            'typeSpecList',
            _yang_ns._namespaces['ietf-nvo-vpn'],
        'ydk.models.ietf.ietf_nvo_vpn'
        ),
    },
    'Nvovpnmgr.Composedvpns.Accesspointlist.Tpbasicinfo.Tpqosnode.Intpcar' : {
        'meta_info' : _MetaInfoClass('Nvovpnmgr.Composedvpns.Accesspointlist.Tpbasicinfo.Tpqosnode.Intpcar',
            False, 
            [
            _MetaInfoClassMember('index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                index
                ''',
                'index',
                'ietf-nvo-vpn', True),
            _MetaInfoClassMember('action', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                action
                ''',
                'action',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('actionType', REFERENCE_ENUM_CLASS, 'ActiontypeEnum' , 'ydk.models.ietf.ietf_nvo_qos_types', 'ActiontypeEnum', 
                [], [], 
                '''                actionType
                ''',
                'actiontype',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('dataKind', REFERENCE_ENUM_CLASS, 'DatakindEnum' , 'ydk.models.ietf.ietf_nvo_qos_types', 'DatakindEnum', 
                [], [], 
                '''                dataKind
                ''',
                'datakind',
                'ietf-nvo-vpn', False),
            ],
            'ietf-nvo-vpn',
            'inTpCar',
            _yang_ns._namespaces['ietf-nvo-vpn'],
        'ydk.models.ietf.ietf_nvo_vpn'
        ),
    },
    'Nvovpnmgr.Composedvpns.Accesspointlist.Tpbasicinfo.Tpqosnode.Outtpcar' : {
        'meta_info' : _MetaInfoClass('Nvovpnmgr.Composedvpns.Accesspointlist.Tpbasicinfo.Tpqosnode.Outtpcar',
            False, 
            [
            _MetaInfoClassMember('index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                index
                ''',
                'index',
                'ietf-nvo-vpn', True),
            _MetaInfoClassMember('action', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                action
                ''',
                'action',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('actionType', REFERENCE_ENUM_CLASS, 'ActiontypeEnum' , 'ydk.models.ietf.ietf_nvo_qos_types', 'ActiontypeEnum', 
                [], [], 
                '''                actionType
                ''',
                'actiontype',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('dataKind', REFERENCE_ENUM_CLASS, 'DatakindEnum' , 'ydk.models.ietf.ietf_nvo_qos_types', 'DatakindEnum', 
                [], [], 
                '''                dataKind
                ''',
                'datakind',
                'ietf-nvo-vpn', False),
            ],
            'ietf-nvo-vpn',
            'outTpCar',
            _yang_ns._namespaces['ietf-nvo-vpn'],
        'ydk.models.ietf.ietf_nvo_vpn'
        ),
    },
    'Nvovpnmgr.Composedvpns.Accesspointlist.Tpbasicinfo.Tpqosnode' : {
        'meta_info' : _MetaInfoClass('Nvovpnmgr.Composedvpns.Accesspointlist.Tpbasicinfo.Tpqosnode',
            False, 
            [
            _MetaInfoClassMember('inQosProfileId', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}'], 
                '''                inQosProfileId
                ''',
                'inqosprofileid',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('inTpCar', REFERENCE_LIST, 'Intpcar' , 'ydk.models.ietf.ietf_nvo_vpn', 'Nvovpnmgr.Composedvpns.Accesspointlist.Tpbasicinfo.Tpqosnode.Intpcar', 
                [], [], 
                '''                inTpCar
                ''',
                'intpcar',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('outQosProfileId', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}'], 
                '''                outQosProfileId
                ''',
                'outqosprofileid',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('outTpCar', REFERENCE_LIST, 'Outtpcar' , 'ydk.models.ietf.ietf_nvo_vpn', 'Nvovpnmgr.Composedvpns.Accesspointlist.Tpbasicinfo.Tpqosnode.Outtpcar', 
                [], [], 
                '''                outTpCar
                ''',
                'outtpcar',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('qosConfigType', REFERENCE_ENUM_CLASS, 'QosconfigtypeEnum' , 'ydk.models.ietf.ietf_nvo_qos_types', 'QosconfigtypeEnum', 
                [], [], 
                '''                qosConfigType
                ''',
                'qosconfigtype',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('qosDetailType', REFERENCE_ENUM_CLASS, 'QosdetailtypeEnum' , 'ydk.models.ietf.ietf_nvo_qos_types', 'QosdetailtypeEnum', 
                [], [], 
                '''                qosDetailType
                ''',
                'qosdetailtype',
                'ietf-nvo-vpn', False),
            ],
            'ietf-nvo-vpn',
            'tpQosNode',
            _yang_ns._namespaces['ietf-nvo-vpn'],
        'ydk.models.ietf.ietf_nvo_vpn'
        ),
    },
    'Nvovpnmgr.Composedvpns.Accesspointlist.Tpbasicinfo.Flowservices.Flowservices_.Flowbehaviors' : {
        'meta_info' : _MetaInfoClass('Nvovpnmgr.Composedvpns.Accesspointlist.Tpbasicinfo.Flowservices.Flowservices_.Flowbehaviors',
            False, 
            [
            _MetaInfoClassMember('index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                index
                ''',
                'index',
                'ietf-nvo-vpn', True),
            _MetaInfoClassMember('action', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                action
                ''',
                'action',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('actionType', REFERENCE_ENUM_CLASS, 'ActiontypeEnum' , 'ydk.models.ietf.ietf_nvo_qos_types', 'ActiontypeEnum', 
                [], [], 
                '''                actionType
                ''',
                'actiontype',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('dataKind', REFERENCE_ENUM_CLASS, 'DatakindEnum' , 'ydk.models.ietf.ietf_nvo_qos_types', 'DatakindEnum', 
                [], [], 
                '''                dataKind
                ''',
                'datakind',
                'ietf-nvo-vpn', False),
            ],
            'ietf-nvo-vpn',
            'flowBehaviors',
            _yang_ns._namespaces['ietf-nvo-vpn'],
        'ydk.models.ietf.ietf_nvo_vpn'
        ),
    },
    'Nvovpnmgr.Composedvpns.Accesspointlist.Tpbasicinfo.Flowservices.Flowservices_' : {
        'meta_info' : _MetaInfoClass('Nvovpnmgr.Composedvpns.Accesspointlist.Tpbasicinfo.Flowservices.Flowservices_',
            False, 
            [
            _MetaInfoClassMember('flowClassifierId', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}'], 
                '''                flowClassifierId
                ''',
                'flowclassifierid',
                'ietf-nvo-vpn', True),
            _MetaInfoClassMember('flowBehaviors', REFERENCE_LIST, 'Flowbehaviors' , 'ydk.models.ietf.ietf_nvo_vpn', 'Nvovpnmgr.Composedvpns.Accesspointlist.Tpbasicinfo.Flowservices.Flowservices_.Flowbehaviors', 
                [], [], 
                '''                flowBehaviors
                ''',
                'flowbehaviors',
                'ietf-nvo-vpn', False),
            ],
            'ietf-nvo-vpn',
            'flowServices',
            _yang_ns._namespaces['ietf-nvo-vpn'],
        'ydk.models.ietf.ietf_nvo_vpn'
        ),
    },
    'Nvovpnmgr.Composedvpns.Accesspointlist.Tpbasicinfo.Flowservices' : {
        'meta_info' : _MetaInfoClass('Nvovpnmgr.Composedvpns.Accesspointlist.Tpbasicinfo.Flowservices',
            False, 
            [
            _MetaInfoClassMember('flowQosTemplateID', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}'], 
                '''                flowQosTemplateID
                ''',
                'flowqostemplateid',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('flowServices', REFERENCE_LIST, 'Flowservices_' , 'ydk.models.ietf.ietf_nvo_vpn', 'Nvovpnmgr.Composedvpns.Accesspointlist.Tpbasicinfo.Flowservices.Flowservices_', 
                [], [], 
                '''                default in flow and behaviors
                ''',
                'flowservices',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('inFlowQosTemplateID', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}'], 
                '''                inFlowQosTemplateID
                ''',
                'inflowqostemplateid',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('outFlowQosTemplateID', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}'], 
                '''                outFlowQosTemplateID
                ''',
                'outflowqostemplateid',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('qosConfigType', REFERENCE_ENUM_CLASS, 'QosconfigtypeEnum' , 'ydk.models.ietf.ietf_nvo_qos_types', 'QosconfigtypeEnum', 
                [], [], 
                '''                qosConfigType
                ''',
                'qosconfigtype',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('qosDetailType', REFERENCE_ENUM_CLASS, 'QosdetailtypeEnum' , 'ydk.models.ietf.ietf_nvo_qos_types', 'QosdetailtypeEnum', 
                [], [], 
                '''                qosDetailType
                ''',
                'qosdetailtype',
                'ietf-nvo-vpn', False),
            ],
            'ietf-nvo-vpn',
            'flowServices',
            _yang_ns._namespaces['ietf-nvo-vpn'],
        'ydk.models.ietf.ietf_nvo_vpn'
        ),
    },
    'Nvovpnmgr.Composedvpns.Accesspointlist.Tpbasicinfo.Addtionalinfo' : {
        'meta_info' : _MetaInfoClass('Nvovpnmgr.Composedvpns.Accesspointlist.Tpbasicinfo.Addtionalinfo',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                string name 
                ''',
                'name',
                'ietf-nvo-vpn', True),
            _MetaInfoClassMember('value', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                string value
                ''',
                'value',
                'ietf-nvo-vpn', False),
            ],
            'ietf-nvo-vpn',
            'addtionalInfo',
            _yang_ns._namespaces['ietf-nvo-vpn'],
        'ydk.models.ietf.ietf_nvo_vpn'
        ),
    },
    'Nvovpnmgr.Composedvpns.Accesspointlist.Tpbasicinfo' : {
        'meta_info' : _MetaInfoClass('Nvovpnmgr.Composedvpns.Accesspointlist.Tpbasicinfo',
            False, 
            [
            _MetaInfoClassMember('addtionalInfo', REFERENCE_LIST, 'Addtionalinfo' , 'ydk.models.ietf.ietf_nvo_vpn', 'Nvovpnmgr.Composedvpns.Accesspointlist.Tpbasicinfo.Addtionalinfo', 
                [], [], 
                '''                addtionalInfo
                ''',
                'addtionalinfo',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('adminStatus', REFERENCE_ENUM_CLASS, 'AdminstatusEnum' , 'ydk.models.ietf.ietf_nvo_common_types', 'AdminstatusEnum', 
                [], [], 
                '''                administrative status.
                ''',
                'adminstatus',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('edgePointRole', REFERENCE_ENUM_CLASS, 'EdgepointroleEnum' , 'ydk.models.ietf.ietf_nvo_common_types', 'EdgepointroleEnum', 
                [], [], 
                '''                edge role for TP, for example:UNI/NNI 
                ''',
                'edgepointrole',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('flowServices', REFERENCE_CLASS, 'Flowservices' , 'ydk.models.ietf.ietf_nvo_vpn', 'Nvovpnmgr.Composedvpns.Accesspointlist.Tpbasicinfo.Flowservices', 
                [], [], 
                '''                flow services in one TP
                ''',
                'flowservices',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('topologyRole', REFERENCE_ENUM_CLASS, 'ToponoderoleEnum' , 'ydk.models.ietf.ietf_nvo_common_types', 'ToponoderoleEnum', 
                [], [], 
                '''                hub/spoke role, etc
                ''',
                'topologyrole',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('tpQosNode', REFERENCE_CLASS, 'Tpqosnode' , 'ydk.models.ietf.ietf_nvo_vpn', 'Nvovpnmgr.Composedvpns.Accesspointlist.Tpbasicinfo.Tpqosnode', 
                [], [], 
                '''                tpQosNode
                ''',
                'tpqosnode',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('Type', REFERENCE_ENUM_CLASS, 'TptypeEnum' , 'ydk.models.ietf.ietf_nvo_common_types', 'TptypeEnum', 
                [], [], 
                '''                Type
                ''',
                'type',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('typeSpecList', REFERENCE_LIST, 'Typespeclist' , 'ydk.models.ietf.ietf_nvo_vpn', 'Nvovpnmgr.Composedvpns.Accesspointlist.Tpbasicinfo.Typespeclist', 
                [], [], 
                '''                typeSpecList
                ''',
                'typespeclist',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('workingLayer', REFERENCE_ENUM_CLASS, 'LayerrateEnum' , 'ydk.models.ietf.ietf_nvo_common_types', 'LayerrateEnum', 
                [], [], 
                '''                working layer
                ''',
                'workinglayer',
                'ietf-nvo-vpn', False),
            ],
            'ietf-nvo-vpn',
            'tpBasicInfo',
            _yang_ns._namespaces['ietf-nvo-vpn'],
        'ydk.models.ietf.ietf_nvo_vpn'
        ),
    },
    'Nvovpnmgr.Composedvpns.Accesspointlist.Peercetp' : {
        'meta_info' : _MetaInfoClass('Nvovpnmgr.Composedvpns.Accesspointlist.Peercetp',
            False, 
            [
            _MetaInfoClassMember('ceDirectNeID', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}'], 
                '''                direction connected NE ID, only valid in
                asbr 
                ''',
                'cedirectneid',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('ceDirectTPID', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}'], 
                '''                ce Direct TP id, only valid in asbr
                ''',
                'cedirecttpid',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('ceID', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}'], 
                '''                Site router ID
                ''',
                'ceid',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('ceIfmasterIp', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ceIfmasterIp
                ''',
                'ceifmasterip',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('location', ATTRIBUTE, 'str' , None, None, 
                [(0, 400)], [], 
                '''                CE device location 
                ''',
                'location',
                'ietf-nvo-vpn', False),
            ],
            'ietf-nvo-vpn',
            'peerCeTp',
            _yang_ns._namespaces['ietf-nvo-vpn'],
        'ydk.models.ietf.ietf_nvo_vpn'
        ),
    },
    'Nvovpnmgr.Composedvpns.Accesspointlist.Routeprotocolspec.Staticrouteitems' : {
        'meta_info' : _MetaInfoClass('Nvovpnmgr.Composedvpns.Accesspointlist.Routeprotocolspec.Staticrouteitems',
            False, 
            [
            _MetaInfoClassMember('index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                static item index
                ''',
                'index',
                'ietf-nvo-vpn', True),
            _MetaInfoClassMember('destinationCidr', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                destination ip cidr. 
                ''',
                'destinationcidr',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('egressTP', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}'], 
                '''                egress tp
                ''',
                'egresstp',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('nextHopIp', ATTRIBUTE, 'str' , None, None, 
                [(0, 200)], [], 
                '''                nextHopIp
                ''',
                'nexthopip',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('routePreference', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                route priority. Ordinary, work route have
                higher priority.
                ''',
                'routepreference',
                'ietf-nvo-vpn', False),
            ],
            'ietf-nvo-vpn',
            'staticRouteItems',
            _yang_ns._namespaces['ietf-nvo-vpn'],
        'ydk.models.ietf.ietf_nvo_vpn'
        ),
    },
    'Nvovpnmgr.Composedvpns.Accesspointlist.Routeprotocolspec.Bgpprotocols' : {
        'meta_info' : _MetaInfoClass('Nvovpnmgr.Composedvpns.Accesspointlist.Routeprotocolspec.Bgpprotocols',
            False, 
            [
            _MetaInfoClassMember('index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                index of BGP protocol item
                ''',
                'index',
                'ietf-nvo-vpn', True),
            _MetaInfoClassMember('bgpMaxPrefix', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                
                ''',
                'bgpmaxprefix',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('bgpMaxPrefixAlarm', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                alarm threshold of BGP rout
                ''',
                'bgpmaxprefixalarm',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('peerAsNumber', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                
                ''',
                'peerasnumber',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('peerIp', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                peerIp
                ''',
                'peerip',
                'ietf-nvo-vpn', False),
            ],
            'ietf-nvo-vpn',
            'bgpProtocols',
            _yang_ns._namespaces['ietf-nvo-vpn'],
        'ydk.models.ietf.ietf_nvo_vpn'
        ),
    },
    'Nvovpnmgr.Composedvpns.Accesspointlist.Routeprotocolspec' : {
        'meta_info' : _MetaInfoClass('Nvovpnmgr.Composedvpns.Accesspointlist.Routeprotocolspec',
            False, 
            [
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'RouteprotocoltypeEnum' , 'ydk.models.ietf.ietf_nvo_common_types', 'RouteprotocoltypeEnum', 
                [], [], 
                '''                Protocol type
                ''',
                'type',
                'ietf-nvo-vpn', True),
            _MetaInfoClassMember('bgpProtocols', REFERENCE_LIST, 'Bgpprotocols' , 'ydk.models.ietf.ietf_nvo_vpn', 'Nvovpnmgr.Composedvpns.Accesspointlist.Routeprotocolspec.Bgpprotocols', 
                [], [], 
                '''                bgpProtocols
                ''',
                'bgpprotocols',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('staticRouteItems', REFERENCE_LIST, 'Staticrouteitems' , 'ydk.models.ietf.ietf_nvo_vpn', 'Nvovpnmgr.Composedvpns.Accesspointlist.Routeprotocolspec.Staticrouteitems', 
                [], [], 
                '''                staticRouteItems
                ''',
                'staticrouteitems',
                'ietf-nvo-vpn', False),
            ],
            'ietf-nvo-vpn',
            'routeProtocolSpec',
            _yang_ns._namespaces['ietf-nvo-vpn'],
        'ydk.models.ietf.ietf_nvo_vpn'
        ),
    },
    'Nvovpnmgr.Composedvpns.Accesspointlist' : {
        'meta_info' : _MetaInfoClass('Nvovpnmgr.Composedvpns.Accesspointlist',
            False, 
            [
            _MetaInfoClassMember('id', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}'], 
                '''                yang:uuid-str for TP
                ''',
                'id',
                'ietf-nvo-vpn', True),
            _MetaInfoClassMember('containingMainTPID', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}'], 
                '''                uuid-str for main interface
                ''',
                'containingmaintpid',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [(0, 200)], [], 
                '''                description for this tp.
                ''',
                'description',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(0, 200)], [], 
                '''                Must abbey to name rule defined in system.
                Example FE0/0/1, GE1/2/1.1, Eth-Trunk1.1, etc
                ''',
                'name',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('neID', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}'], 
                '''                yang:uuid-str for NE 
                ''',
                'neid',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('operStatus', REFERENCE_ENUM_CLASS, 'OperstatusEnum' , 'ydk.models.ietf.ietf_nvo_common_types', 'OperstatusEnum', 
                [], [], 
                '''                Operational status.
                ''',
                'operstatus',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('peerCeTp', REFERENCE_CLASS, 'Peercetp' , 'ydk.models.ietf.ietf_nvo_vpn', 'Nvovpnmgr.Composedvpns.Accesspointlist.Peercetp', 
                [], [], 
                '''                CE TP Information
                ''',
                'peercetp',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('routeProtocolSpec', REFERENCE_LIST, 'Routeprotocolspec' , 'ydk.models.ietf.ietf_nvo_vpn', 'Nvovpnmgr.Composedvpns.Accesspointlist.Routeprotocolspec', 
                [], [], 
                '''                route protocol spec
                ''',
                'routeprotocolspec',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('tpBasicInfo', REFERENCE_CLASS, 'Tpbasicinfo' , 'ydk.models.ietf.ietf_nvo_vpn', 'Nvovpnmgr.Composedvpns.Accesspointlist.Tpbasicinfo', 
                [], [], 
                '''                Tp non-instance basic info
                ''',
                'tpbasicinfo',
                'ietf-nvo-vpn', False),
            ],
            'ietf-nvo-vpn',
            'accessPointList',
            _yang_ns._namespaces['ietf-nvo-vpn'],
        'ydk.models.ietf.ietf_nvo_vpn'
        ),
    },
    'Nvovpnmgr.Composedvpns' : {
        'meta_info' : _MetaInfoClass('Nvovpnmgr.Composedvpns',
            False, 
            [
            _MetaInfoClassMember('id', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}'], 
                '''                UUID-STR for service .
                ''',
                'id',
                'ietf-nvo-vpn', True),
            _MetaInfoClassMember('accessPointList', REFERENCE_LIST, 'Accesspointlist' , 'ydk.models.ietf.ietf_nvo_vpn', 'Nvovpnmgr.Composedvpns.Accesspointlist', 
                [], [], 
                '''                TP list of the access links which associated
                with CE and PE
                ''',
                'accesspointlist',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('businessTypeID', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}'], 
                '''                business Type Name
                ''',
                'businesstypeid',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [(0, 200)], [], 
                '''                Detailed specification for the servcie.
                ''',
                'description',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(0, 200)], [], 
                '''                Human-readable name for the service.
                ''',
                'name',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('operStatus', REFERENCE_ENUM_CLASS, 'OperstatusEnum' , 'ydk.models.ietf.ietf_nvo_common_types', 'OperstatusEnum', 
                [], [], 
                '''                Operational status.
                ''',
                'operstatus',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('segVpnList', REFERENCE_LIST, 'Segvpnlist' , 'ydk.models.ietf.ietf_nvo_vpn', 'Nvovpnmgr.Composedvpns.Segvpnlist', 
                [], [], 
                '''                SegVpn list 
                ''',
                'segvpnlist',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('startTime', ATTRIBUTE, 'str' , None, None, 
                [], ['\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})'], 
                '''                Service lifecycle: request for service start
                time.
                ''',
                'starttime',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('syncStatus', REFERENCE_ENUM_CLASS, 'SyncstatusEnum' , 'ydk.models.ietf.ietf_nvo_common_types', 'SyncstatusEnum', 
                [], [], 
                '''                Sync status.
                ''',
                'syncstatus',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('tenantId', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}'], 
                '''                UUID-STR for tenant.
                ''',
                'tenantid',
                'ietf-nvo-vpn', False),
            _MetaInfoClassMember('vpnBasicInfo', REFERENCE_CLASS, 'Vpnbasicinfo' , 'ydk.models.ietf.ietf_nvo_vpn', 'Nvovpnmgr.Composedvpns.Vpnbasicinfo', 
                [], [], 
                '''                VPN BASIC INFO
                ''',
                'vpnbasicinfo',
                'ietf-nvo-vpn', False),
            ],
            'ietf-nvo-vpn',
            'composedVPNs',
            _yang_ns._namespaces['ietf-nvo-vpn'],
        'ydk.models.ietf.ietf_nvo_vpn'
        ),
    },
    'Nvovpnmgr' : {
        'meta_info' : _MetaInfoClass('Nvovpnmgr',
            False, 
            [
            _MetaInfoClassMember('composedVPNs', REFERENCE_LIST, 'Composedvpns' , 'ydk.models.ietf.ietf_nvo_vpn', 'Nvovpnmgr.Composedvpns', 
                [], [], 
                '''                
                ''',
                'composedvpns',
                'ietf-nvo-vpn', False),
            ],
            'ietf-nvo-vpn',
            'nvoVPNMgr',
            _yang_ns._namespaces['ietf-nvo-vpn'],
        'ydk.models.ietf.ietf_nvo_vpn'
        ),
    },
}
_meta_table['Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Tpbasicinfo.Typespeclist.Ethernetspec.Qinqvlan']['meta_info'].parent =_meta_table['Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Tpbasicinfo.Typespeclist.Ethernetspec']['meta_info']
_meta_table['Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Tpbasicinfo.Typespeclist.Ethernetspec.Dot1Q']['meta_info'].parent =_meta_table['Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Tpbasicinfo.Typespeclist.Ethernetspec']['meta_info']
_meta_table['Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Tpbasicinfo.Typespeclist.Ethernetspec']['meta_info'].parent =_meta_table['Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Tpbasicinfo.Typespeclist']['meta_info']
_meta_table['Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Tpbasicinfo.Typespeclist.Ipspec']['meta_info'].parent =_meta_table['Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Tpbasicinfo.Typespeclist']['meta_info']
_meta_table['Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Tpbasicinfo.Typespeclist.Vxlanspec']['meta_info'].parent =_meta_table['Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Tpbasicinfo.Typespeclist']['meta_info']
_meta_table['Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Tpbasicinfo.Tpqosnode.Intpcar']['meta_info'].parent =_meta_table['Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Tpbasicinfo.Tpqosnode']['meta_info']
_meta_table['Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Tpbasicinfo.Tpqosnode.Outtpcar']['meta_info'].parent =_meta_table['Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Tpbasicinfo.Tpqosnode']['meta_info']
_meta_table['Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Tpbasicinfo.Flowservices.Flowservices_.Flowbehaviors']['meta_info'].parent =_meta_table['Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Tpbasicinfo.Flowservices.Flowservices_']['meta_info']
_meta_table['Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Tpbasicinfo.Flowservices.Flowservices_']['meta_info'].parent =_meta_table['Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Tpbasicinfo.Flowservices']['meta_info']
_meta_table['Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Tpbasicinfo.Typespeclist']['meta_info'].parent =_meta_table['Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Tpbasicinfo']['meta_info']
_meta_table['Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Tpbasicinfo.Tpqosnode']['meta_info'].parent =_meta_table['Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Tpbasicinfo']['meta_info']
_meta_table['Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Tpbasicinfo.Flowservices']['meta_info'].parent =_meta_table['Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Tpbasicinfo']['meta_info']
_meta_table['Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Tpbasicinfo.Addtionalinfo']['meta_info'].parent =_meta_table['Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Tpbasicinfo']['meta_info']
_meta_table['Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Routeprotocolspec.Staticrouteitems']['meta_info'].parent =_meta_table['Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Routeprotocolspec']['meta_info']
_meta_table['Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Routeprotocolspec.Bgpprotocols']['meta_info'].parent =_meta_table['Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Routeprotocolspec']['meta_info']
_meta_table['Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Tpbasicinfo']['meta_info'].parent =_meta_table['Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist']['meta_info']
_meta_table['Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Peercetp']['meta_info'].parent =_meta_table['Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist']['meta_info']
_meta_table['Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist.Routeprotocolspec']['meta_info'].parent =_meta_table['Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist']['meta_info']
_meta_table['Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Vpnbasicinfo']['meta_info'].parent =_meta_table['Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn']['meta_info']
_meta_table['Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn.Accesspointlist']['meta_info'].parent =_meta_table['Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn']['meta_info']
_meta_table['Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo.Vpn']['meta_info'].parent =_meta_table['Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo']['meta_info']
_meta_table['Nvovpnmgr.Composedvpns.Segvpnlist.Vpninfo']['meta_info'].parent =_meta_table['Nvovpnmgr.Composedvpns.Segvpnlist']['meta_info']
_meta_table['Nvovpnmgr.Composedvpns.Accesspointlist.Tpbasicinfo.Typespeclist.Ethernetspec.Qinqvlan']['meta_info'].parent =_meta_table['Nvovpnmgr.Composedvpns.Accesspointlist.Tpbasicinfo.Typespeclist.Ethernetspec']['meta_info']
_meta_table['Nvovpnmgr.Composedvpns.Accesspointlist.Tpbasicinfo.Typespeclist.Ethernetspec.Dot1Q']['meta_info'].parent =_meta_table['Nvovpnmgr.Composedvpns.Accesspointlist.Tpbasicinfo.Typespeclist.Ethernetspec']['meta_info']
_meta_table['Nvovpnmgr.Composedvpns.Accesspointlist.Tpbasicinfo.Typespeclist.Ethernetspec']['meta_info'].parent =_meta_table['Nvovpnmgr.Composedvpns.Accesspointlist.Tpbasicinfo.Typespeclist']['meta_info']
_meta_table['Nvovpnmgr.Composedvpns.Accesspointlist.Tpbasicinfo.Typespeclist.Ipspec']['meta_info'].parent =_meta_table['Nvovpnmgr.Composedvpns.Accesspointlist.Tpbasicinfo.Typespeclist']['meta_info']
_meta_table['Nvovpnmgr.Composedvpns.Accesspointlist.Tpbasicinfo.Typespeclist.Vxlanspec']['meta_info'].parent =_meta_table['Nvovpnmgr.Composedvpns.Accesspointlist.Tpbasicinfo.Typespeclist']['meta_info']
_meta_table['Nvovpnmgr.Composedvpns.Accesspointlist.Tpbasicinfo.Tpqosnode.Intpcar']['meta_info'].parent =_meta_table['Nvovpnmgr.Composedvpns.Accesspointlist.Tpbasicinfo.Tpqosnode']['meta_info']
_meta_table['Nvovpnmgr.Composedvpns.Accesspointlist.Tpbasicinfo.Tpqosnode.Outtpcar']['meta_info'].parent =_meta_table['Nvovpnmgr.Composedvpns.Accesspointlist.Tpbasicinfo.Tpqosnode']['meta_info']
_meta_table['Nvovpnmgr.Composedvpns.Accesspointlist.Tpbasicinfo.Flowservices.Flowservices_.Flowbehaviors']['meta_info'].parent =_meta_table['Nvovpnmgr.Composedvpns.Accesspointlist.Tpbasicinfo.Flowservices.Flowservices_']['meta_info']
_meta_table['Nvovpnmgr.Composedvpns.Accesspointlist.Tpbasicinfo.Flowservices.Flowservices_']['meta_info'].parent =_meta_table['Nvovpnmgr.Composedvpns.Accesspointlist.Tpbasicinfo.Flowservices']['meta_info']
_meta_table['Nvovpnmgr.Composedvpns.Accesspointlist.Tpbasicinfo.Typespeclist']['meta_info'].parent =_meta_table['Nvovpnmgr.Composedvpns.Accesspointlist.Tpbasicinfo']['meta_info']
_meta_table['Nvovpnmgr.Composedvpns.Accesspointlist.Tpbasicinfo.Tpqosnode']['meta_info'].parent =_meta_table['Nvovpnmgr.Composedvpns.Accesspointlist.Tpbasicinfo']['meta_info']
_meta_table['Nvovpnmgr.Composedvpns.Accesspointlist.Tpbasicinfo.Flowservices']['meta_info'].parent =_meta_table['Nvovpnmgr.Composedvpns.Accesspointlist.Tpbasicinfo']['meta_info']
_meta_table['Nvovpnmgr.Composedvpns.Accesspointlist.Tpbasicinfo.Addtionalinfo']['meta_info'].parent =_meta_table['Nvovpnmgr.Composedvpns.Accesspointlist.Tpbasicinfo']['meta_info']
_meta_table['Nvovpnmgr.Composedvpns.Accesspointlist.Routeprotocolspec.Staticrouteitems']['meta_info'].parent =_meta_table['Nvovpnmgr.Composedvpns.Accesspointlist.Routeprotocolspec']['meta_info']
_meta_table['Nvovpnmgr.Composedvpns.Accesspointlist.Routeprotocolspec.Bgpprotocols']['meta_info'].parent =_meta_table['Nvovpnmgr.Composedvpns.Accesspointlist.Routeprotocolspec']['meta_info']
_meta_table['Nvovpnmgr.Composedvpns.Accesspointlist.Tpbasicinfo']['meta_info'].parent =_meta_table['Nvovpnmgr.Composedvpns.Accesspointlist']['meta_info']
_meta_table['Nvovpnmgr.Composedvpns.Accesspointlist.Peercetp']['meta_info'].parent =_meta_table['Nvovpnmgr.Composedvpns.Accesspointlist']['meta_info']
_meta_table['Nvovpnmgr.Composedvpns.Accesspointlist.Routeprotocolspec']['meta_info'].parent =_meta_table['Nvovpnmgr.Composedvpns.Accesspointlist']['meta_info']
_meta_table['Nvovpnmgr.Composedvpns.Vpnbasicinfo']['meta_info'].parent =_meta_table['Nvovpnmgr.Composedvpns']['meta_info']
_meta_table['Nvovpnmgr.Composedvpns.Segvpnlist']['meta_info'].parent =_meta_table['Nvovpnmgr.Composedvpns']['meta_info']
_meta_table['Nvovpnmgr.Composedvpns.Accesspointlist']['meta_info'].parent =_meta_table['Nvovpnmgr.Composedvpns']['meta_info']
_meta_table['Nvovpnmgr.Composedvpns']['meta_info'].parent =_meta_table['Nvovpnmgr']['meta_info']
