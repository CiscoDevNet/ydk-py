


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns

_meta_table = {
    'Nvotpmgr.Tps.Tpbasicinfo.Typespeclist.Ethernetspec.Qinqvlan' : {
        'meta_info' : _MetaInfoClass('Nvotpmgr.Tps.Tpbasicinfo.Typespeclist.Ethernetspec.Qinqvlan',
            False, 
            [
            _MetaInfoClassMember('cvlanList', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                cvlanList
                ''',
                'cvlanlist',
                'ietf-nvo-tp', False),
            _MetaInfoClassMember('svlanList', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                svlanList
                ''',
                'svlanlist',
                'ietf-nvo-tp', False),
            ],
            'ietf-nvo-tp',
            'qinqVlan',
            _yang_ns._namespaces['ietf-nvo-tp'],
        'ydk.models.ietf.ietf_nvo_tp'
        ),
    },
    'Nvotpmgr.Tps.Tpbasicinfo.Typespeclist.Ethernetspec.Dot1Q' : {
        'meta_info' : _MetaInfoClass('Nvotpmgr.Tps.Tpbasicinfo.Typespeclist.Ethernetspec.Dot1Q',
            False, 
            [
            _MetaInfoClassMember('dot1qVlanList', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                dot1qVlanList
                ''',
                'dot1qvlanlist',
                'ietf-nvo-tp', False),
            ],
            'ietf-nvo-tp',
            'dot1q',
            _yang_ns._namespaces['ietf-nvo-tp'],
        'ydk.models.ietf.ietf_nvo_tp'
        ),
    },
    'Nvotpmgr.Tps.Tpbasicinfo.Typespeclist.Ethernetspec' : {
        'meta_info' : _MetaInfoClass('Nvotpmgr.Tps.Tpbasicinfo.Typespeclist.Ethernetspec',
            False, 
            [
            _MetaInfoClassMember('accessType', REFERENCE_ENUM_CLASS, 'EthernetencaptypeEnum' , 'ydk.models.ietf.ietf_nvo_common_types', 'EthernetencaptypeEnum', 
                [], [], 
                '''                access frame type
                ''',
                'accesstype',
                'ietf-nvo-tp', False),
            _MetaInfoClassMember('actionValue', ATTRIBUTE, 'str' , None, None, 
                [(0, 100)], [], 
                '''                action value
                ''',
                'actionvalue',
                'ietf-nvo-tp', False),
            _MetaInfoClassMember('dot1q', REFERENCE_CLASS, 'Dot1Q' , 'ydk.models.ietf.ietf_nvo_tp', 'Nvotpmgr.Tps.Tpbasicinfo.Typespeclist.Ethernetspec.Dot1Q', 
                [], [], 
                '''                dot1q
                ''',
                'dot1q',
                'ietf-nvo-tp', False),
            _MetaInfoClassMember('qinqVlan', REFERENCE_CLASS, 'Qinqvlan' , 'ydk.models.ietf.ietf_nvo_tp', 'Nvotpmgr.Tps.Tpbasicinfo.Typespeclist.Ethernetspec.Qinqvlan', 
                [], [], 
                '''                qinqVlan
                ''',
                'qinqvlan',
                'ietf-nvo-tp', False),
            _MetaInfoClassMember('vlanAction', REFERENCE_ENUM_CLASS, 'EthernetactionEnum' , 'ydk.models.ietf.ietf_nvo_common_types', 'EthernetactionEnum', 
                [], [], 
                '''                Frame type that can be accepted. not needed
                now
                ''',
                'vlanaction',
                'ietf-nvo-tp', False),
            ],
            'ietf-nvo-tp',
            'ethernetSpec',
            _yang_ns._namespaces['ietf-nvo-tp'],
        'ydk.models.ietf.ietf_nvo_tp'
        ),
    },
    'Nvotpmgr.Tps.Tpbasicinfo.Typespeclist.Ipspec' : {
        'meta_info' : _MetaInfoClass('Nvotpmgr.Tps.Tpbasicinfo.Typespeclist.Ipspec',
            False, 
            [
            _MetaInfoClassMember('masterIp', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                master IP address
                ''',
                'masterip',
                'ietf-nvo-tp', False),
            _MetaInfoClassMember('mtu', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                mtu for ip layer,scope:46~9600
                ''',
                'mtu',
                'ietf-nvo-tp', False),
            ],
            'ietf-nvo-tp',
            'ipSpec',
            _yang_ns._namespaces['ietf-nvo-tp'],
        'ydk.models.ietf.ietf_nvo_tp'
        ),
    },
    'Nvotpmgr.Tps.Tpbasicinfo.Typespeclist.Vxlanspec' : {
        'meta_info' : _MetaInfoClass('Nvotpmgr.Tps.Tpbasicinfo.Typespeclist.Vxlanspec',
            False, 
            [
            _MetaInfoClassMember('vni', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                vni
                ''',
                'vni',
                'ietf-nvo-tp', False),
            _MetaInfoClassMember('vtepIP', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                vtep ip
                ''',
                'vtepip',
                'ietf-nvo-tp', False),
            ],
            'ietf-nvo-tp',
            'vxlanSpec',
            _yang_ns._namespaces['ietf-nvo-tp'],
        'ydk.models.ietf.ietf_nvo_tp'
        ),
    },
    'Nvotpmgr.Tps.Tpbasicinfo.Typespeclist' : {
        'meta_info' : _MetaInfoClass('Nvotpmgr.Tps.Tpbasicinfo.Typespeclist',
            False, 
            [
            _MetaInfoClassMember('layerRate', REFERENCE_ENUM_CLASS, 'LayerrateEnum' , 'ydk.models.ietf.ietf_nvo_common_types', 'LayerrateEnum', 
                [], [], 
                '''                layerRate
                ''',
                'layerrate',
                'ietf-nvo-tp', True),
            _MetaInfoClassMember('ethernetSpec', REFERENCE_CLASS, 'Ethernetspec' , 'ydk.models.ietf.ietf_nvo_tp', 'Nvotpmgr.Tps.Tpbasicinfo.Typespeclist.Ethernetspec', 
                [], [], 
                '''                ethernetSpec
                ''',
                'ethernetspec',
                'ietf-nvo-tp', False),
            _MetaInfoClassMember('ipSpec', REFERENCE_CLASS, 'Ipspec' , 'ydk.models.ietf.ietf_nvo_tp', 'Nvotpmgr.Tps.Tpbasicinfo.Typespeclist.Ipspec', 
                [], [], 
                '''                ipSpec
                ''',
                'ipspec',
                'ietf-nvo-tp', False),
            _MetaInfoClassMember('vxlanSpec', REFERENCE_CLASS, 'Vxlanspec' , 'ydk.models.ietf.ietf_nvo_tp', 'Nvotpmgr.Tps.Tpbasicinfo.Typespeclist.Vxlanspec', 
                [], [], 
                '''                vxlanSpec
                ''',
                'vxlanspec',
                'ietf-nvo-tp', False),
            ],
            'ietf-nvo-tp',
            'typeSpecList',
            _yang_ns._namespaces['ietf-nvo-tp'],
        'ydk.models.ietf.ietf_nvo_tp'
        ),
    },
    'Nvotpmgr.Tps.Tpbasicinfo.Tpqosnode.Intpcar' : {
        'meta_info' : _MetaInfoClass('Nvotpmgr.Tps.Tpbasicinfo.Tpqosnode.Intpcar',
            False, 
            [
            _MetaInfoClassMember('index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                index
                ''',
                'index',
                'ietf-nvo-tp', True),
            _MetaInfoClassMember('action', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                action
                ''',
                'action',
                'ietf-nvo-tp', False),
            _MetaInfoClassMember('actionType', REFERENCE_ENUM_CLASS, 'ActiontypeEnum' , 'ydk.models.ietf.ietf_nvo_qos_types', 'ActiontypeEnum', 
                [], [], 
                '''                actionType
                ''',
                'actiontype',
                'ietf-nvo-tp', False),
            _MetaInfoClassMember('dataKind', REFERENCE_ENUM_CLASS, 'DatakindEnum' , 'ydk.models.ietf.ietf_nvo_qos_types', 'DatakindEnum', 
                [], [], 
                '''                dataKind
                ''',
                'datakind',
                'ietf-nvo-tp', False),
            ],
            'ietf-nvo-tp',
            'inTpCar',
            _yang_ns._namespaces['ietf-nvo-tp'],
        'ydk.models.ietf.ietf_nvo_tp'
        ),
    },
    'Nvotpmgr.Tps.Tpbasicinfo.Tpqosnode.Outtpcar' : {
        'meta_info' : _MetaInfoClass('Nvotpmgr.Tps.Tpbasicinfo.Tpqosnode.Outtpcar',
            False, 
            [
            _MetaInfoClassMember('index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                index
                ''',
                'index',
                'ietf-nvo-tp', True),
            _MetaInfoClassMember('action', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                action
                ''',
                'action',
                'ietf-nvo-tp', False),
            _MetaInfoClassMember('actionType', REFERENCE_ENUM_CLASS, 'ActiontypeEnum' , 'ydk.models.ietf.ietf_nvo_qos_types', 'ActiontypeEnum', 
                [], [], 
                '''                actionType
                ''',
                'actiontype',
                'ietf-nvo-tp', False),
            _MetaInfoClassMember('dataKind', REFERENCE_ENUM_CLASS, 'DatakindEnum' , 'ydk.models.ietf.ietf_nvo_qos_types', 'DatakindEnum', 
                [], [], 
                '''                dataKind
                ''',
                'datakind',
                'ietf-nvo-tp', False),
            ],
            'ietf-nvo-tp',
            'outTpCar',
            _yang_ns._namespaces['ietf-nvo-tp'],
        'ydk.models.ietf.ietf_nvo_tp'
        ),
    },
    'Nvotpmgr.Tps.Tpbasicinfo.Tpqosnode' : {
        'meta_info' : _MetaInfoClass('Nvotpmgr.Tps.Tpbasicinfo.Tpqosnode',
            False, 
            [
            _MetaInfoClassMember('inQosProfileId', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}'], 
                '''                inQosProfileId
                ''',
                'inqosprofileid',
                'ietf-nvo-tp', False),
            _MetaInfoClassMember('inTpCar', REFERENCE_LIST, 'Intpcar' , 'ydk.models.ietf.ietf_nvo_tp', 'Nvotpmgr.Tps.Tpbasicinfo.Tpqosnode.Intpcar', 
                [], [], 
                '''                inTpCar
                ''',
                'intpcar',
                'ietf-nvo-tp', False),
            _MetaInfoClassMember('outQosProfileId', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}'], 
                '''                outQosProfileId
                ''',
                'outqosprofileid',
                'ietf-nvo-tp', False),
            _MetaInfoClassMember('outTpCar', REFERENCE_LIST, 'Outtpcar' , 'ydk.models.ietf.ietf_nvo_tp', 'Nvotpmgr.Tps.Tpbasicinfo.Tpqosnode.Outtpcar', 
                [], [], 
                '''                outTpCar
                ''',
                'outtpcar',
                'ietf-nvo-tp', False),
            _MetaInfoClassMember('qosConfigType', REFERENCE_ENUM_CLASS, 'QosconfigtypeEnum' , 'ydk.models.ietf.ietf_nvo_qos_types', 'QosconfigtypeEnum', 
                [], [], 
                '''                qosConfigType
                ''',
                'qosconfigtype',
                'ietf-nvo-tp', False),
            _MetaInfoClassMember('qosDetailType', REFERENCE_ENUM_CLASS, 'QosdetailtypeEnum' , 'ydk.models.ietf.ietf_nvo_qos_types', 'QosdetailtypeEnum', 
                [], [], 
                '''                qosDetailType
                ''',
                'qosdetailtype',
                'ietf-nvo-tp', False),
            ],
            'ietf-nvo-tp',
            'tpQosNode',
            _yang_ns._namespaces['ietf-nvo-tp'],
        'ydk.models.ietf.ietf_nvo_tp'
        ),
    },
    'Nvotpmgr.Tps.Tpbasicinfo.Flowservices.Flowservices_.Flowbehaviors' : {
        'meta_info' : _MetaInfoClass('Nvotpmgr.Tps.Tpbasicinfo.Flowservices.Flowservices_.Flowbehaviors',
            False, 
            [
            _MetaInfoClassMember('index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                index
                ''',
                'index',
                'ietf-nvo-tp', True),
            _MetaInfoClassMember('action', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                action
                ''',
                'action',
                'ietf-nvo-tp', False),
            _MetaInfoClassMember('actionType', REFERENCE_ENUM_CLASS, 'ActiontypeEnum' , 'ydk.models.ietf.ietf_nvo_qos_types', 'ActiontypeEnum', 
                [], [], 
                '''                actionType
                ''',
                'actiontype',
                'ietf-nvo-tp', False),
            _MetaInfoClassMember('dataKind', REFERENCE_ENUM_CLASS, 'DatakindEnum' , 'ydk.models.ietf.ietf_nvo_qos_types', 'DatakindEnum', 
                [], [], 
                '''                dataKind
                ''',
                'datakind',
                'ietf-nvo-tp', False),
            ],
            'ietf-nvo-tp',
            'flowBehaviors',
            _yang_ns._namespaces['ietf-nvo-tp'],
        'ydk.models.ietf.ietf_nvo_tp'
        ),
    },
    'Nvotpmgr.Tps.Tpbasicinfo.Flowservices.Flowservices_' : {
        'meta_info' : _MetaInfoClass('Nvotpmgr.Tps.Tpbasicinfo.Flowservices.Flowservices_',
            False, 
            [
            _MetaInfoClassMember('flowClassifierId', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}'], 
                '''                flowClassifierId
                ''',
                'flowclassifierid',
                'ietf-nvo-tp', True),
            _MetaInfoClassMember('flowBehaviors', REFERENCE_LIST, 'Flowbehaviors' , 'ydk.models.ietf.ietf_nvo_tp', 'Nvotpmgr.Tps.Tpbasicinfo.Flowservices.Flowservices_.Flowbehaviors', 
                [], [], 
                '''                flowBehaviors
                ''',
                'flowbehaviors',
                'ietf-nvo-tp', False),
            ],
            'ietf-nvo-tp',
            'flowServices',
            _yang_ns._namespaces['ietf-nvo-tp'],
        'ydk.models.ietf.ietf_nvo_tp'
        ),
    },
    'Nvotpmgr.Tps.Tpbasicinfo.Flowservices' : {
        'meta_info' : _MetaInfoClass('Nvotpmgr.Tps.Tpbasicinfo.Flowservices',
            False, 
            [
            _MetaInfoClassMember('flowQosTemplateID', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}'], 
                '''                flowQosTemplateID
                ''',
                'flowqostemplateid',
                'ietf-nvo-tp', False),
            _MetaInfoClassMember('flowServices', REFERENCE_LIST, 'Flowservices_' , 'ydk.models.ietf.ietf_nvo_tp', 'Nvotpmgr.Tps.Tpbasicinfo.Flowservices.Flowservices_', 
                [], [], 
                '''                default in flow and behaviors
                ''',
                'flowservices',
                'ietf-nvo-tp', False),
            _MetaInfoClassMember('inFlowQosTemplateID', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}'], 
                '''                inFlowQosTemplateID
                ''',
                'inflowqostemplateid',
                'ietf-nvo-tp', False),
            _MetaInfoClassMember('outFlowQosTemplateID', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}'], 
                '''                outFlowQosTemplateID
                ''',
                'outflowqostemplateid',
                'ietf-nvo-tp', False),
            _MetaInfoClassMember('qosConfigType', REFERENCE_ENUM_CLASS, 'QosconfigtypeEnum' , 'ydk.models.ietf.ietf_nvo_qos_types', 'QosconfigtypeEnum', 
                [], [], 
                '''                qosConfigType
                ''',
                'qosconfigtype',
                'ietf-nvo-tp', False),
            _MetaInfoClassMember('qosDetailType', REFERENCE_ENUM_CLASS, 'QosdetailtypeEnum' , 'ydk.models.ietf.ietf_nvo_qos_types', 'QosdetailtypeEnum', 
                [], [], 
                '''                qosDetailType
                ''',
                'qosdetailtype',
                'ietf-nvo-tp', False),
            ],
            'ietf-nvo-tp',
            'flowServices',
            _yang_ns._namespaces['ietf-nvo-tp'],
        'ydk.models.ietf.ietf_nvo_tp'
        ),
    },
    'Nvotpmgr.Tps.Tpbasicinfo.Addtionalinfo' : {
        'meta_info' : _MetaInfoClass('Nvotpmgr.Tps.Tpbasicinfo.Addtionalinfo',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                string name 
                ''',
                'name',
                'ietf-nvo-tp', True),
            _MetaInfoClassMember('value', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                string value
                ''',
                'value',
                'ietf-nvo-tp', False),
            ],
            'ietf-nvo-tp',
            'addtionalInfo',
            _yang_ns._namespaces['ietf-nvo-tp'],
        'ydk.models.ietf.ietf_nvo_tp'
        ),
    },
    'Nvotpmgr.Tps.Tpbasicinfo' : {
        'meta_info' : _MetaInfoClass('Nvotpmgr.Tps.Tpbasicinfo',
            False, 
            [
            _MetaInfoClassMember('addtionalInfo', REFERENCE_LIST, 'Addtionalinfo' , 'ydk.models.ietf.ietf_nvo_tp', 'Nvotpmgr.Tps.Tpbasicinfo.Addtionalinfo', 
                [], [], 
                '''                addtionalInfo
                ''',
                'addtionalinfo',
                'ietf-nvo-tp', False),
            _MetaInfoClassMember('adminStatus', REFERENCE_ENUM_CLASS, 'AdminstatusEnum' , 'ydk.models.ietf.ietf_nvo_common_types', 'AdminstatusEnum', 
                [], [], 
                '''                administrative status.
                ''',
                'adminstatus',
                'ietf-nvo-tp', False),
            _MetaInfoClassMember('edgePointRole', REFERENCE_ENUM_CLASS, 'EdgepointroleEnum' , 'ydk.models.ietf.ietf_nvo_common_types', 'EdgepointroleEnum', 
                [], [], 
                '''                edge role for TP, for example:UNI/NNI 
                ''',
                'edgepointrole',
                'ietf-nvo-tp', False),
            _MetaInfoClassMember('flowServices', REFERENCE_CLASS, 'Flowservices' , 'ydk.models.ietf.ietf_nvo_tp', 'Nvotpmgr.Tps.Tpbasicinfo.Flowservices', 
                [], [], 
                '''                flow services in one TP
                ''',
                'flowservices',
                'ietf-nvo-tp', False),
            _MetaInfoClassMember('topologyRole', REFERENCE_ENUM_CLASS, 'ToponoderoleEnum' , 'ydk.models.ietf.ietf_nvo_common_types', 'ToponoderoleEnum', 
                [], [], 
                '''                hub/spoke role, etc
                ''',
                'topologyrole',
                'ietf-nvo-tp', False),
            _MetaInfoClassMember('tpQosNode', REFERENCE_CLASS, 'Tpqosnode' , 'ydk.models.ietf.ietf_nvo_tp', 'Nvotpmgr.Tps.Tpbasicinfo.Tpqosnode', 
                [], [], 
                '''                tpQosNode
                ''',
                'tpqosnode',
                'ietf-nvo-tp', False),
            _MetaInfoClassMember('Type', REFERENCE_ENUM_CLASS, 'TptypeEnum' , 'ydk.models.ietf.ietf_nvo_common_types', 'TptypeEnum', 
                [], [], 
                '''                Type
                ''',
                'type',
                'ietf-nvo-tp', False),
            _MetaInfoClassMember('typeSpecList', REFERENCE_LIST, 'Typespeclist' , 'ydk.models.ietf.ietf_nvo_tp', 'Nvotpmgr.Tps.Tpbasicinfo.Typespeclist', 
                [], [], 
                '''                typeSpecList
                ''',
                'typespeclist',
                'ietf-nvo-tp', False),
            _MetaInfoClassMember('workingLayer', REFERENCE_ENUM_CLASS, 'LayerrateEnum' , 'ydk.models.ietf.ietf_nvo_common_types', 'LayerrateEnum', 
                [], [], 
                '''                working layer
                ''',
                'workinglayer',
                'ietf-nvo-tp', False),
            ],
            'ietf-nvo-tp',
            'tpBasicInfo',
            _yang_ns._namespaces['ietf-nvo-tp'],
        'ydk.models.ietf.ietf_nvo_tp'
        ),
    },
    'Nvotpmgr.Tps.Peercetp' : {
        'meta_info' : _MetaInfoClass('Nvotpmgr.Tps.Peercetp',
            False, 
            [
            _MetaInfoClassMember('ceDirectNeID', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}'], 
                '''                direction connected NE ID, only valid in
                asbr 
                ''',
                'cedirectneid',
                'ietf-nvo-tp', False),
            _MetaInfoClassMember('ceDirectTPID', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}'], 
                '''                ce Direct TP id, only valid in asbr
                ''',
                'cedirecttpid',
                'ietf-nvo-tp', False),
            _MetaInfoClassMember('ceID', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}'], 
                '''                Site router ID
                ''',
                'ceid',
                'ietf-nvo-tp', False),
            _MetaInfoClassMember('ceIfmasterIp', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ceIfmasterIp
                ''',
                'ceifmasterip',
                'ietf-nvo-tp', False),
            _MetaInfoClassMember('location', ATTRIBUTE, 'str' , None, None, 
                [(0, 400)], [], 
                '''                CE device location 
                ''',
                'location',
                'ietf-nvo-tp', False),
            ],
            'ietf-nvo-tp',
            'peerCeTp',
            _yang_ns._namespaces['ietf-nvo-tp'],
        'ydk.models.ietf.ietf_nvo_tp'
        ),
    },
    'Nvotpmgr.Tps.Routeprotocolspec.Staticrouteitems' : {
        'meta_info' : _MetaInfoClass('Nvotpmgr.Tps.Routeprotocolspec.Staticrouteitems',
            False, 
            [
            _MetaInfoClassMember('index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                static item index
                ''',
                'index',
                'ietf-nvo-tp', True),
            _MetaInfoClassMember('destinationCidr', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                destination ip cidr. 
                ''',
                'destinationcidr',
                'ietf-nvo-tp', False),
            _MetaInfoClassMember('egressTP', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}'], 
                '''                egress tp
                ''',
                'egresstp',
                'ietf-nvo-tp', False),
            _MetaInfoClassMember('nextHopIp', ATTRIBUTE, 'str' , None, None, 
                [(0, 200)], [], 
                '''                nextHopIp
                ''',
                'nexthopip',
                'ietf-nvo-tp', False),
            _MetaInfoClassMember('routePreference', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                route priority. Ordinary, work route have
                higher priority.
                ''',
                'routepreference',
                'ietf-nvo-tp', False),
            ],
            'ietf-nvo-tp',
            'staticRouteItems',
            _yang_ns._namespaces['ietf-nvo-tp'],
        'ydk.models.ietf.ietf_nvo_tp'
        ),
    },
    'Nvotpmgr.Tps.Routeprotocolspec.Bgpprotocols' : {
        'meta_info' : _MetaInfoClass('Nvotpmgr.Tps.Routeprotocolspec.Bgpprotocols',
            False, 
            [
            _MetaInfoClassMember('index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                index of BGP protocol item
                ''',
                'index',
                'ietf-nvo-tp', True),
            _MetaInfoClassMember('bgpMaxPrefix', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                
                ''',
                'bgpmaxprefix',
                'ietf-nvo-tp', False),
            _MetaInfoClassMember('bgpMaxPrefixAlarm', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                alarm threshold of BGP rout
                ''',
                'bgpmaxprefixalarm',
                'ietf-nvo-tp', False),
            _MetaInfoClassMember('peerAsNumber', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                
                ''',
                'peerasnumber',
                'ietf-nvo-tp', False),
            _MetaInfoClassMember('peerIp', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                peerIp
                ''',
                'peerip',
                'ietf-nvo-tp', False),
            ],
            'ietf-nvo-tp',
            'bgpProtocols',
            _yang_ns._namespaces['ietf-nvo-tp'],
        'ydk.models.ietf.ietf_nvo_tp'
        ),
    },
    'Nvotpmgr.Tps.Routeprotocolspec' : {
        'meta_info' : _MetaInfoClass('Nvotpmgr.Tps.Routeprotocolspec',
            False, 
            [
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'RouteprotocoltypeEnum' , 'ydk.models.ietf.ietf_nvo_common_types', 'RouteprotocoltypeEnum', 
                [], [], 
                '''                Protocol type
                ''',
                'type',
                'ietf-nvo-tp', True),
            _MetaInfoClassMember('bgpProtocols', REFERENCE_LIST, 'Bgpprotocols' , 'ydk.models.ietf.ietf_nvo_tp', 'Nvotpmgr.Tps.Routeprotocolspec.Bgpprotocols', 
                [], [], 
                '''                bgpProtocols
                ''',
                'bgpprotocols',
                'ietf-nvo-tp', False),
            _MetaInfoClassMember('staticRouteItems', REFERENCE_LIST, 'Staticrouteitems' , 'ydk.models.ietf.ietf_nvo_tp', 'Nvotpmgr.Tps.Routeprotocolspec.Staticrouteitems', 
                [], [], 
                '''                staticRouteItems
                ''',
                'staticrouteitems',
                'ietf-nvo-tp', False),
            ],
            'ietf-nvo-tp',
            'routeProtocolSpec',
            _yang_ns._namespaces['ietf-nvo-tp'],
        'ydk.models.ietf.ietf_nvo_tp'
        ),
    },
    'Nvotpmgr.Tps' : {
        'meta_info' : _MetaInfoClass('Nvotpmgr.Tps',
            False, 
            [
            _MetaInfoClassMember('id', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}'], 
                '''                yang:uuid-str for TP
                ''',
                'id',
                'ietf-nvo-tp', True),
            _MetaInfoClassMember('containingMainTPID', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}'], 
                '''                uuid-str for main interface
                ''',
                'containingmaintpid',
                'ietf-nvo-tp', False),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [(0, 200)], [], 
                '''                description for this tp.
                ''',
                'description',
                'ietf-nvo-tp', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(0, 200)], [], 
                '''                Must abbey to name rule defined in system.
                Example FE0/0/1, GE1/2/1.1, Eth-Trunk1.1, etc
                ''',
                'name',
                'ietf-nvo-tp', False),
            _MetaInfoClassMember('neID', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}'], 
                '''                yang:uuid-str for NE 
                ''',
                'neid',
                'ietf-nvo-tp', False),
            _MetaInfoClassMember('operStatus', REFERENCE_ENUM_CLASS, 'OperstatusEnum' , 'ydk.models.ietf.ietf_nvo_common_types', 'OperstatusEnum', 
                [], [], 
                '''                Operational status.
                ''',
                'operstatus',
                'ietf-nvo-tp', False),
            _MetaInfoClassMember('peerCeTp', REFERENCE_CLASS, 'Peercetp' , 'ydk.models.ietf.ietf_nvo_tp', 'Nvotpmgr.Tps.Peercetp', 
                [], [], 
                '''                CE TP Information
                ''',
                'peercetp',
                'ietf-nvo-tp', False),
            _MetaInfoClassMember('routeProtocolSpec', REFERENCE_LIST, 'Routeprotocolspec' , 'ydk.models.ietf.ietf_nvo_tp', 'Nvotpmgr.Tps.Routeprotocolspec', 
                [], [], 
                '''                route protocol spec
                ''',
                'routeprotocolspec',
                'ietf-nvo-tp', False),
            _MetaInfoClassMember('tpBasicInfo', REFERENCE_CLASS, 'Tpbasicinfo' , 'ydk.models.ietf.ietf_nvo_tp', 'Nvotpmgr.Tps.Tpbasicinfo', 
                [], [], 
                '''                Tp non-instance basic info
                ''',
                'tpbasicinfo',
                'ietf-nvo-tp', False),
            ],
            'ietf-nvo-tp',
            'tps',
            _yang_ns._namespaces['ietf-nvo-tp'],
        'ydk.models.ietf.ietf_nvo_tp'
        ),
    },
    'Nvotpmgr' : {
        'meta_info' : _MetaInfoClass('Nvotpmgr',
            False, 
            [
            _MetaInfoClassMember('tps', REFERENCE_LIST, 'Tps' , 'ydk.models.ietf.ietf_nvo_tp', 'Nvotpmgr.Tps', 
                [], [], 
                '''                tp retrieve functions
                ''',
                'tps',
                'ietf-nvo-tp', False),
            ],
            'ietf-nvo-tp',
            'nvoTPMgr',
            _yang_ns._namespaces['ietf-nvo-tp'],
        'ydk.models.ietf.ietf_nvo_tp'
        ),
    },
}
_meta_table['Nvotpmgr.Tps.Tpbasicinfo.Typespeclist.Ethernetspec.Qinqvlan']['meta_info'].parent =_meta_table['Nvotpmgr.Tps.Tpbasicinfo.Typespeclist.Ethernetspec']['meta_info']
_meta_table['Nvotpmgr.Tps.Tpbasicinfo.Typespeclist.Ethernetspec.Dot1Q']['meta_info'].parent =_meta_table['Nvotpmgr.Tps.Tpbasicinfo.Typespeclist.Ethernetspec']['meta_info']
_meta_table['Nvotpmgr.Tps.Tpbasicinfo.Typespeclist.Ethernetspec']['meta_info'].parent =_meta_table['Nvotpmgr.Tps.Tpbasicinfo.Typespeclist']['meta_info']
_meta_table['Nvotpmgr.Tps.Tpbasicinfo.Typespeclist.Ipspec']['meta_info'].parent =_meta_table['Nvotpmgr.Tps.Tpbasicinfo.Typespeclist']['meta_info']
_meta_table['Nvotpmgr.Tps.Tpbasicinfo.Typespeclist.Vxlanspec']['meta_info'].parent =_meta_table['Nvotpmgr.Tps.Tpbasicinfo.Typespeclist']['meta_info']
_meta_table['Nvotpmgr.Tps.Tpbasicinfo.Tpqosnode.Intpcar']['meta_info'].parent =_meta_table['Nvotpmgr.Tps.Tpbasicinfo.Tpqosnode']['meta_info']
_meta_table['Nvotpmgr.Tps.Tpbasicinfo.Tpqosnode.Outtpcar']['meta_info'].parent =_meta_table['Nvotpmgr.Tps.Tpbasicinfo.Tpqosnode']['meta_info']
_meta_table['Nvotpmgr.Tps.Tpbasicinfo.Flowservices.Flowservices_.Flowbehaviors']['meta_info'].parent =_meta_table['Nvotpmgr.Tps.Tpbasicinfo.Flowservices.Flowservices_']['meta_info']
_meta_table['Nvotpmgr.Tps.Tpbasicinfo.Flowservices.Flowservices_']['meta_info'].parent =_meta_table['Nvotpmgr.Tps.Tpbasicinfo.Flowservices']['meta_info']
_meta_table['Nvotpmgr.Tps.Tpbasicinfo.Typespeclist']['meta_info'].parent =_meta_table['Nvotpmgr.Tps.Tpbasicinfo']['meta_info']
_meta_table['Nvotpmgr.Tps.Tpbasicinfo.Tpqosnode']['meta_info'].parent =_meta_table['Nvotpmgr.Tps.Tpbasicinfo']['meta_info']
_meta_table['Nvotpmgr.Tps.Tpbasicinfo.Flowservices']['meta_info'].parent =_meta_table['Nvotpmgr.Tps.Tpbasicinfo']['meta_info']
_meta_table['Nvotpmgr.Tps.Tpbasicinfo.Addtionalinfo']['meta_info'].parent =_meta_table['Nvotpmgr.Tps.Tpbasicinfo']['meta_info']
_meta_table['Nvotpmgr.Tps.Routeprotocolspec.Staticrouteitems']['meta_info'].parent =_meta_table['Nvotpmgr.Tps.Routeprotocolspec']['meta_info']
_meta_table['Nvotpmgr.Tps.Routeprotocolspec.Bgpprotocols']['meta_info'].parent =_meta_table['Nvotpmgr.Tps.Routeprotocolspec']['meta_info']
_meta_table['Nvotpmgr.Tps.Tpbasicinfo']['meta_info'].parent =_meta_table['Nvotpmgr.Tps']['meta_info']
_meta_table['Nvotpmgr.Tps.Peercetp']['meta_info'].parent =_meta_table['Nvotpmgr.Tps']['meta_info']
_meta_table['Nvotpmgr.Tps.Routeprotocolspec']['meta_info'].parent =_meta_table['Nvotpmgr.Tps']['meta_info']
_meta_table['Nvotpmgr.Tps']['meta_info'].parent =_meta_table['Nvotpmgr']['meta_info']
